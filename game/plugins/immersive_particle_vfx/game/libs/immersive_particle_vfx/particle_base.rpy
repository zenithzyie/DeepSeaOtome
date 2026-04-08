################################################################################
##
## Immersive Particle VFX for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
## https://feniksdev.itch.io/immersive-particle-vfx-for-renpy
##
################################################################################
## This file contains the base code for improved particle effects in Ren'Py.
## Two other files, perspective_particles.rpy and flutter_particles.rpy, build
## off of this code.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
## This tool also comes with assets from several artists. The folders with their
## art is labelled and comes with a credits.txt file so you can credit them
## if you use their work alongside this code.
##
## If you'd like to see how to use this tool, check the other file,
## particle_examples.rpy! This is just the backend; you don't need to
## understand everything in this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################

## Included for backwards compatibility with Ren'Py versions prior to 8.4.0.
init -999 python in particle_vfx:
    import random, math
    def _interpolate(a, b, step):
        return a + (b - a) * step
    def linear(a, b):
        """Linear distribution: Value has an equal chance of being
        anywhere between a and b."""
        return random.uniform(a, b)
    def gaussian(a, b):
        """Gaussian distribution: Value is more likely to be near the
        mean and less likely to be near the extremes."""
        mu = _interpolate(a, b, 0.5)
        sigma = (b - a) / 6
        return random.gauss(mu, sigma)
    def arcsine(a, b):
        """Arcsine distribution: Value is more likely to be near the
        extremes and less likely to be near the mean."""
        u = random.random()
        x = math.sin((math.pi / 2) * u) ** 2
        return _interpolate(a, b, x)

    distribution_func_map = {
        "linear": linear,
        "gaussian": gaussian,
        "arcsine": arcsine,
    }

    def compute_raw(value, room):
        """
        Converts a position from one of the Ren'Py position types into an
        absolute number of pixels, without regard for the return type.
        """
        if isinstance(value, position):
            return value.relative * room + value.absolute
        elif isinstance(value, (absolute, int)):
            return value
        elif isinstance(value, float):
            return value * room
        else:
            raise TypeError(f"Value {value} of type {type(value)} not recognized as a position.")

    ## A custom distribution function example which trends towards b the closer
    ## current_time is to max_time.
    def speed_up_over_time(a, b, current_time, max_time):
        """
        A distribution function that returns a value between a and b,
        starting near a at time 0 and approaching b as current_time
        approaches max_time.
        """
        if current_time >= max_time:
            return b
        t = current_time / max_time
        x = t * t
        return _interpolate(a, b, x)

    def a_to_b_over_t_time(a, b, t):
        """
        Given two numbers, a and b, return a percent value between a and b
        depending on t, a value between 0.0 and 1.0.
        """
        return (b - a) * t + a

init -990 python in particle_vfx:

    from store import NoRollback, Particles, AlphaMask, Null, ConditionSwitch
    from store import config, particle_config, Transform, DynamicDisplayable
    from store import create_gradient_mask, create_radius_mask

    try:
        sb_func_map = renpy.display.particle.distribution_func_map
    except AttributeError:
        sb_func_map = distribution_func_map

    ## A few math functions for acceleration
    # https://mytimecalculator.com/escape-time-calculator
    def get_time_with_distance(acceleration, speed, distance, invalid):
        """
        Get the time to cover the provided distance given the acceleration
        and starting speed.
        """
        if acceleration == 0:
            return distance / max(abs(speed), 1)

        a = acceleration
        s = speed
        ## Idea: positive acceleration always goes more in the direction
        ## the particle is already travelling. Negative acceleration always
        ## slows it down. Ergo, if the speed is negative, the acceleration
        ## should be flipped.
        if speed < 0:
            acceleration = -acceleration

        if speed < 0 and acceleration < 0:
            ## Going negative, but accelerating.
            ## Flip both for time calculation
            speed = -speed
            acceleration = -acceleration

        ## Match the distance sign to the speed
        if (distance < 0 and speed > 0) or (distance > 0 and speed < 0):
            distance = -distance

        ## QUADRATIC FORMULA:
        # ax² + bx + c = 0
        # 0 = (0.5*a)t² + (vi)t + (-d)
        # x = (-b ± √(b² - 4ac)) / 2a
        # t = (-vi ± √(vi² - 4*0.5*a*(-d))) / 2*0.5*a
        # t = (-vi ± √(vi² + 2ad)) / a
        vi = speed
        a = acceleration
        d = distance

        sqrt_term = vi**2 + 2*a*d
        if sqrt_term < 0:
            return invalid
        sqrt_term = math.sqrt(sqrt_term)
        t1 = (-vi + sqrt_term) / a
        t2 = (-vi - sqrt_term) / a
        valid_times = [ t for t in (t1, t2) if t >= 0 ]
        if valid_times:
            return min(valid_times)
        else:
            return invalid

    def dist_covered_in_time(vi, t, acceleration):
        """
        Given a time, how far does this particle travel, knowing its initial
        speed and acceleration?
        """
        if acceleration == 0:
            return vi * t
        if vi < 0:
            acceleration = -acceleration
        return vi * t + 0.5 * acceleration * t**2

    def get_maximum_decel(speed, distance):
        """
        Return the maximum deceleration that can be applied to a particle
        and still have it cover the given distance before stopping.
        Returns a negative number e.g. -100
        """
        ## Reverse question: start speed is 0. End speed is speed.
        ## Time unknown. Solve for acceleration.
        # t = (vf - vi) / a
        # Distance during acceleration: d = vi*t + ½*a*t²
        ## vi = 0 so d = 0.5*a*t²
        ## t = vf / a
        ## d = 0.5*a*(vf/a)² = 0.5*vf²/a
        # a = (0.5*vf²) / d
        speed = abs(speed)
        distance = abs(distance)
        ret = (-0.5 * (speed**2)) / distance
        ## Round it down a little (aka up because it's negative) to ensure
        ## it doesn't overshoot.
        return math.ceil(ret*1000.0)/1000.0

    def final_speed_after_distance(vi, a, d):
        """
        Return the final speed after a particle with starting speed vi and
        acceleration a has travelled distance d.
        """
        if a == 0:
            return vi
        # vf^2 = vi^2 + 2ad
        vf_squared = vi**2 + 2*a*d
        if vf_squared < 0:
            return 0.0
        return math.copysign(math.sqrt(vf_squared), vi)

    def final_speed_after_time(vi, a, t):
        """
        Return the final speed after a particle with starting speed vi and
        acceleration a has travelled for time t.
        """
        return vi + a*t

    ## The main class! It handles and creates particles.
    class ImmersiveParticleFactory(NoRollback):

        def __setstate__(self, state):
            self.max_travel_time = 0
            vars(self).update(state)
            self.last_st = 0
            self.last_particle_added = 0
            self.queue = [ ]
            self.delayed_queue = [ ]
            self.temp_fast_target = 0
            self.temp_fast_time_stopped = 0
            self.init()

        def __init__(self, image, **kwargs):
            """
            Create a SnowBlossom factory.

            Attributes:
            -----------
            (Omitted attributes named in ImmersiveParticles function below)
            xborder : integer
                How many pixels outside the active area the particle needs to
                clear before it's offscreen horizontally.
            yborder : integer
                How many pixels outside the active area the particle needs to
                clear before it's offscreen vertically.
            width : int
                The width of the particle area.
            height : int
                The height of the particle area.
            is_vertical : bool
                True if the particles are primarily moving vertically.
            max_travel_time : float
                The maximum time it takes for a particle to travel from its
                start position to offscreen in its primary direction.
            last_st : float
                The last st recorded in the factory. Used to determine if the
                factory was likely hidden or not.
            st_offset : float
                The time when the animation was restarted. Used so the animation
                can be reset when it's hidden and re-shown without having
                "gaps".
            queue : list
                A list of start times for particles during the startup period.
            last_particle_added : float
                The time when the last particle was added. Used to prevent
                too many particles from spawning in a given time frame.
            delayed_queue : list
                A list of start times for particles that have a delay before
                being re-added to the screen.
            temp_fast_target : int
                The target number of particles to have on-screen after there's
                been a delay in update times (to catch up).
            temp_fast_time_stopped : float
                The last update time before a larger gap in update times. Used
                to help fill in the positions of particles when there's a gap
                in update times.
            """
            self.original_kwargs = kwargs.copy() ## For inheriting!
            self.original_kwargs['image'] = image
            xspeed = kwargs.get('xspeed', None)
            yspeed = kwargs.get('yspeed', None)
            xacceleration = kwargs.get('xacceleration', None)
            yacceleration = kwargs.get('yacceleration', None)
            angle = kwargs.get('angle', None)
            acceleration = kwargs.get('acceleration', None)
            velocity = kwargs.get('velocity', None)

            if xspeed is None and yspeed is None and velocity is None:
                raise ValueError("Must provide both xspeed and yspeed, or just velocity.")
            if velocity is None and angle is not None:
                raise ValueError("Must provide velocity to use angle.")
            if velocity is not None and angle is None:
                raise ValueError("Must provide angle to use velocity.")
            if xspeed is not None and velocity is not None:
                raise ValueError("Cannot provide both xspeed and velocity.")
            if yspeed is not None and velocity is not None:
                raise ValueError("Cannot provide both yspeed and velocity.")
            if xacceleration is not None and acceleration is not None:
                raise ValueError("Cannot provide both xacceleration and acceleration.")
            if yacceleration is not None and acceleration is not None:
                raise ValueError("Cannot provide both yacceleration and acceleration.")

            if xspeed is not None and yspeed is not None and acceleration is None:
                if xacceleration is None:
                    xacceleration = 0
                if yacceleration is None:
                    yacceleration = 0
            elif (velocity is not None and angle is not None
                    and xacceleration is None and yacceleration is None):
                if acceleration is None:
                    acceleration = 0

            if velocity is not None and angle is not None:
                using_speed = False
                if xacceleration is None and acceleration is None:
                    xacceleration = 0
                if yacceleration is None and acceleration is None:
                    yacceleration = 0
            else:
                using_speed = True
                if xacceleration is None and yacceleration is None and acceleration is None:
                    acceleration = 0

            if isinstance(image, list):
                try:
                    self.image = [renpy.displayable(img) for img in image]
                except:
                    self.image = image
            else:
                self.image = renpy.displayable(image)

            self.amount = kwargs.get('amount', kwargs.get("count", 10))
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.xacceleration = xacceleration
            self.yacceleration = yacceleration
            self.angle = angle
            ## For calculations, subtract angles from 180 so 0 degrees is 12:00
            if angle is not None:
                if isinstance(angle, tuple):
                    angle = (180 - angle[0], 180 - angle[1])
                else:
                    angle = 180 - angle
            self.acceleration = acceleration
            self.velocity = velocity
            border = kwargs.get('particle_size', 0)
            if isinstance(border, tuple):
                self.xborder = border[0]
                self.yborder = border[1]
            else:
                self.xborder = border
                self.yborder = border
            self.fast = kwargs.get('fast', False)
            self.delay = kwargs.get('delay', None)
            self.position_variance = kwargs.get('position_variance', 0)
            self.slow_start = kwargs.get('slow_start', None)
            self.slow_start_ramp = max(kwargs.get('slow_start_ramp', 2), 1)
            xysize = kwargs.get('xysize', (config.screen_width, config.screen_height))
            self.width, self.height = xysize or (config.screen_width, config.screen_height)
            self.distribute_fast_start = kwargs.get('distribute_fast_start', None)
            self.force_direction = kwargs.get('force_direction', None)
            self.enter_exit_from_sides = kwargs.get('enter_exit_from_sides', True)
            self.origin_points = kwargs.get('origin_points', None)
            if self.origin_points and not isinstance(self.origin_points, dict):
                self.origin_points = dict(points=self.origin_points)
            self.update_frequency = kwargs.get('update_frequency', 1.0/30.0)
            distribution = kwargs.get('distribution', 'linear')
            if isinstance(distribution, str):
                distribution = sb_func_map[distribution]
            self.distribution = distribution
            self.creation_callback = kwargs.get('create_callback', None)

            self.st_offset = 0
            self.last_st = 0
            self.last_particle_added = 0
            self.queue = [ ]
            self.delayed_queue = [ ]
            self.temp_fast_target = 0
            self.temp_fast_time_stopped = 0

            ## Determine which direction these particles are primarily moving in.
            def get_max_or_min(n, fn):
                """
                If n is a tuple of two numbers, return the max or min
                based on fn. Otherwise, return n.
                """
                if isinstance(n, (tuple, list)):
                    return fn(n[0], n[1])
                else:
                    return n

            def get_speed(spd, fn, default=1, acceleration=0):
                """
                Given spd in the form of a number or a tuple of two numbers,
                return the max/min speed possible in terms of absolute value.
                e.g. if spd is (20, 50), and fn is max, then return 50.
                If spd is (-200, 100), and fn is max, return 200.
                Also returns the max/min acceleration value, without absolute
                value.

                Parameters:
                -----------
                spd : number or tuple
                    The speed value(s), or range of speed values.
                fn : function
                    The function to apply (max or min).
                default : number
                    The default value to use against fn (min/max).
                acceleration : number or tuple
                    The acceleration value(s), or range of acceleration values.
                """
                acceleration = get_max_or_min(acceleration, fn) if acceleration is not None else 0

                if isinstance(spd, tuple):
                    return abs(fn([abs(i) for i in spd[:2]]+[default])), acceleration
                else:
                    return abs(fn(abs(spd), default)), acceleration

            # d = (vi * t) + (0.5 * a * t²)
            # t = (-vi ± √(vi² + 2ad)) / a
            if self.force_direction is None:
                ## Which direction does it take longer to clear? We are not
                ## falling in that direction.
                if using_speed:
                    max_yspeed, max_yaccel = get_speed(yspeed, max, 1, yacceleration)
                else:
                    ## Using velocity/angle
                    ## 0 degrees is 12:00
                    ## For vertical speed, what's the closest angle we can get to
                    ## We'll ignore 180-360 directions so just mod the angle by 180
                    if isinstance(angle, (tuple, list)):
                        angle1 = angle[0] % 180
                        angle2 = angle[1] % 180
                        ## Get the angle closest to 0 or 180
                        rng = (min(angle1, angle2), max(angle1, angle2))
                        if rng[0] == rng[1]:
                            best_yangle = angle1
                        else:
                            best_yangle = min(range(*rng), key=lambda a: min(a, 180 - a))
                    else:
                        best_yangle = angle % 180
                    ## SOHCAHTOA to get the vertical component of the velocity
                    temp_yspeed = abs(math.cos(math.radians(best_yangle)) * get_max_or_min(velocity, max))
                    if yacceleration is not None:
                        temp_yacceleration = get_max_or_min(yacceleration, max)
                    else:
                        temp_yacceleration = abs(math.cos(math.radians(best_yangle)) * get_max_or_min(acceleration, max))
                    max_yspeed, max_yaccel = get_speed(temp_yspeed, max, 1, temp_yacceleration)
                ## What's the absolute highest deceleration we can have that still
                ## allows the particle to fall offscreen before stopping?
                max_yaccel = max(max_yaccel, get_maximum_decel(max_yspeed, 2.0*self.yborder+self.height))
                ## The shortest time it takes to clear the area in the y direction.
                min_y_travel_time = get_time_with_distance(max_yaccel, max_yspeed, 2.0*self.yborder + self.height, max_yspeed*(2.0*self.yborder + self.height))

                if using_speed:
                    max_xspeed, max_xaccel = get_speed(xspeed, max, 1, xacceleration)
                else:
                    ## Using velocity/angle
                    ## 0 degrees is 12:00
                    ## Find closest angle to 90 or 270. Start by subtracting 90
                    ## and modding by 180 to get it in the range of 0-180, where 0 is 90 and 180 is 270.
                    if isinstance(angle, (tuple, list)):
                        angle1 = (angle[0]-90) % 180
                        angle2 = (angle[1]-90) % 180
                        ## Get the angle closest to 0 or 180
                        rng = (min(angle1, angle2), max(angle1, angle2))
                        if rng[0] == rng[1]:
                            best_xangle = angle1
                        else:
                            best_xangle = min(range(*rng), key=lambda a: min(a, 180 - a))
                    else:
                        best_xangle = (angle-90) % 180
                    best_xangle += 90
                    temp_xspeed = abs(math.sin(math.radians(best_xangle)) * get_max_or_min(velocity, max))
                    if xacceleration is not None:
                        temp_xacceleration = get_max_or_min(xacceleration, max)
                    else:
                        temp_xacceleration = abs(math.sin(math.radians(best_xangle)) * get_max_or_min(acceleration, max))
                    max_xspeed, max_xaccel = get_speed(temp_xspeed, max, 1, temp_xacceleration)
                max_xaccel = max(max_xaccel, get_maximum_decel(max_xspeed, 2.0*self.xborder+self.width))
                ## The shortest time it takes to clear the area in the x direction.
                min_x_travel_time = get_time_with_distance(max_xaccel, max_xspeed, 2.0*self.xborder + self.width, max_xspeed*(2.0*self.xborder + self.width))

                ## If we're generally clearing the area faster in the y direction
                ## than the x direction, it's vertical.
                if min_x_travel_time > min_y_travel_time:
                    self.is_vertical = True
                elif min_x_travel_time == min_y_travel_time:
                    if abs(max_yspeed/(2.0*self.yborder + self.height)) <= abs(max_xspeed/(2.0*self.xborder + self.width)):
                        self.is_vertical = True
                    else:
                        self.is_vertical = False
                else:
                    self.is_vertical = False
            elif self.force_direction == "vertical":
                self.is_vertical = True
            else:
                self.is_vertical = False

            ## What's the longest it takes to get one particle from the start
            ## to the end?
            if using_speed:
                y_movement, min_yaccel = get_speed(yspeed, min, float('inf'), yacceleration)
            else:
                ## Stands to reason that the best xangle is the worst yangle
                temp_yspeed = abs(math.cos(math.radians(best_xangle)) * get_max_or_min(velocity, max))
                if yacceleration is not None:
                    temp_yacceleration = get_max_or_min(yacceleration, min)
                else:
                    temp_yacceleration = abs(math.cos(math.radians(best_xangle)) * get_max_or_min(acceleration, max))
                y_movement, min_yaccel = get_speed(temp_yspeed, min, float('inf'), temp_yacceleration)
            y_movement = y_movement or 1
            min_yaccel = max(min_yaccel, get_maximum_decel(y_movement, 2.0*self.yborder + self.height))
            y_travel_time = get_time_with_distance(min_yaccel, y_movement, 2.0*self.yborder + self.height, float('inf'))

            if using_speed:
                x_movement, min_xaccel = get_speed(xspeed, min, float('inf'), xacceleration)
            else:
                temp_xspeed = abs(math.sin(math.radians(best_yangle)) * get_max_or_min(velocity, max))
                if xacceleration is not None:
                    temp_xacceleration = get_max_or_min(xacceleration, min)
                else:
                    temp_xacceleration = abs(math.sin(math.radians(best_yangle)) * get_max_or_min(acceleration, max))
                x_movement, min_xaccel = get_speed(temp_xspeed, min, float('inf'), temp_xacceleration)
            x_movement = x_movement or 1
            min_xaccel = max(min_xaccel, get_maximum_decel(x_movement, 2.0*self.xborder + self.width))
            x_travel_time = get_time_with_distance(min_xaccel, x_movement, 2.0*self.xborder + self.width, float('inf'))
            ## Pick the smaller of the two - it's likely we're going in one
            ## direction in particular (e.g. down) so in that case we're not
            ## concerned with how long it takes to travel horizontally.
            self.max_travel_time = min(x_travel_time, y_travel_time)

            if self.slow_start:
                self.slow_start = max(self.slow_start, self.max_travel_time)

            ## If we're not starting with all particles on the screen, then we
            ## should spend the first max_travel_time seconds starting particles
            ## at regular intervals. This will mean that by the time the first
            ## particle clears the area, all `amount` particles should be shown.
            ## We need a particle to start at regular intervals up until
            ## the travel time, when that first particle can go offscreen.
            self.init()

        def init(self):
            """
            Queue up the start times for the particles, based on slow start,
            fast, distribute_fast_start, and max_travel_time.
            """
            self.queue = [ ]
            self.delayed_queue = [ ]
            if self.fast:
                ## Starting in fast mode, but we need to stagger start times
                ## to make sure particles don't all start on the same frame.
                ## Create a list of start times.
                if self.distribute_fast_start is not None:
                    self.queue = [ random.uniform(0, self.distribute_fast_start) for _i in range(0, self.amount-1) ]
                    self.queue.insert(0, 0.0)
                    self.queue.sort()
            else:
                ## Not starting in fast mode. Create a uniform distribution
                ## of times from the earliest particle to the maximum travel
                ## time, when the first particle can be removed from the screen.
                self.queue = [ random.uniform(0, self.max_travel_time) for _i in range(0, self.amount-1) ]
                self.queue.insert(0, 0.0)
                self.queue.sort()
                if self.slow_start:
                    def power_distribution(a, b):
                        """A distribution function that favors lower values."""
                        u = random.random()
                        x = math.pow(u, 1.0 / (self.slow_start_ramp))
                        return a + (b - a) * x
                    ## We are slowly starting amount particles over slow_start
                    ## seconds. This distribution should be set up such that the
                    ## range is (0, 0) if slow_start and max_travel_time are the
                    ## same, and (0, slow_start - max_travel_time) otherwise,
                    ## since we add these numbers to the original distribution.
                    slow_queue = [ power_distribution(0.0, self.slow_start - self.max_travel_time) for _i in range(0, self.amount-1) ]
                    slow_queue.insert(0, 0.0)
                    slow_queue.sort()
                    ## Now we add the original start times to these slow start
                    ## times to ensure we're never spawning particles faster
                    ## than the standard rate (to avoid waves).
                    slow_queue = [ self.queue[i] + slow_queue[i] for i in range(0, len(self.queue)) ]
                    self.queue = slow_queue + [ q+slow_queue[-1] for q in self.queue[1:] ]

        def ranged(self, n, fn=None):
            """
            Return a random number in the range specified by n, or n itself if
            n is not a tuple. If n is a tuple, and it contains two numbers,
            and the returned value will be selected based on the distribution
            function provided as fn. If n is a tuple, and it contains 3 items,
            the first two must be numbers and the third a distribution function.
            If n is a tuple with four items, the first two must be numbers, the
            third a distribution function, and the fourth another number. This
            will cause the current time to be passed to the distribution function
            along with the range and the final number.
            If n is a single value, it is returned as is.
            If n is a tuple or list of something other than numbers, a random
            element from the tuple is returned.
            """
            if fn is None:
                fn = random.uniform
            if isinstance(n, dict):
                ## For origin points
                if 'function' in n:
                    ## Has a function. Provide it the width and height of the
                    ## area and return the result.
                    return n['function'](self.width, self.height)
                if 'distribution' in n:
                    if isinstance(n['distribution'], str):
                        fn = sb_func_map[n['distribution']]
                    else:
                        fn = n['distribution']
                ## Do we have points or min/max?
                if 'points' in n:
                    points = round(fn(0, len(n['points'])-1))
                    x, y = n['points'][points]
                    ## Resolve int/float/position
                    x = compute_raw(x, self.width)
                    y = compute_raw(y, self.height)
                elif 'hotspots' in n:
                    ## Comes as a list of (x, y, w, h) tuples. Calculate the
                    ## areas and use the distribution to weight which one is
                    ## shown.
                    total_area = sum([ w*h for x, y, w, h in n['hotspots'] ])
                    areas = [ w*h for x, y, w, h in n['hotspots'] ]
                    chosen = fn(0, total_area)
                    ## Find which hotspot it comes from
                    index = 0
                    acc = areas[0]
                    while chosen > acc:
                        index += 1
                        acc += areas[index]
                    x, y, w, h = n['hotspots'][index]
                    ## Adjust the numbers based on the area size
                    x = compute_raw(x, self.width)
                    y = compute_raw(y, self.height)
                    w = compute_raw(w, self.width)
                    h = compute_raw(h, self.height)
                    return (x, y, w, h)
                else:
                    ## Otherwise, we have min/max ranges
                    xmin = n.get('x_min', -self.xborder)
                    xmax = n.get('x_max', self.width + self.xborder)
                    ymin = n.get('y_min', -self.yborder)
                    ymax = n.get('y_max', self.height + self.yborder)
                    xmin = compute_raw(xmin, self.width)
                    xmax = compute_raw(xmax, self.width)
                    ymin = compute_raw(ymin, self.height)
                    ymax = compute_raw(ymax, self.height)
                    x = fn(xmin, xmax)
                    y = fn(ymin, ymax)
                return (x, y)
            elif isinstance(n, tuple) or isinstance(n, list):
                if len(n) == 2:
                    if isinstance(n[0], int) or isinstance(n[0], float):
                        return fn(n[0], n[1])
                elif len(n) == 3:
                    ## Third is a distribution function if the first are
                    ## int/float
                    if (isinstance(n[0], int) or isinstance(n[0], float)):
                        distr = n[2]
                        if isinstance(distr, str):
                            distr = sb_func_map[distr]
                        return distr(n[0], n[1])
                elif len(n) == 4:
                    if (isinstance(n[0], int) or isinstance(n[0], float)):
                        ## Has a function that takes time
                        to = self.last_st - self.st_offset
                        distr = n[2]
                        return distr(n[0], n[1], to, n[3])
                return random.choice(n)
            else:
                return n

        def make_particle(self, **kwargs):
            """
            Create a new particle with the given keyword arguments and
            return it.
            """
            particle_kwargs = dict(image=self.ranged(self.image),
                                        xspeed=self.ranged(self.xspeed),
                                        yspeed=self.ranged(self.yspeed),
                                        xacceleration=self.ranged(self.xacceleration),
                                        yacceleration=self.ranged(self.yacceleration),
                                        velocity=self.ranged(self.velocity),
                                        acceleration=self.ranged(self.acceleration),
                                        angle=self.ranged(self.angle),
                                        xborder=self.xborder, yborder=self.yborder,
                                        position_variance=self.position_variance,
                                        width=self.width, height=self.height,
                                        st_offset=self.st_offset,
                                        distribution=self.distribution,
                                        was_fast=self.fast,
                                        force_direction=self.force_direction,
                                        enter_exit_from_sides=self.enter_exit_from_sides,
                                        origin_point=self.ranged(self.origin_points),
                                        **kwargs)
            if self.creation_callback:
                renpy.run(self.creation_callback, particle_kwargs, self)
            return SingleImmersiveParticle(**particle_kwargs)

        def get_amount(self, to):
            """
            Return the amount of particles that should be showing. Used
            in inherited classes.
            """
            return self.amount

        def create(self, particles, st):
            """
            Create new particles as they are ready and add them to the
            factory.
            """
            new_particles = None
            if st <= 0:
                ## Animation is starting over, probably shown for first time.
                self.temp_fast_target = 0
                self.temp_fast_time_stopped = 0
                self.delayed_queue = [ ]
                self.st_offset = st
                ## Get rid of particles
                for sprite, p in particles:
                    sprite.destroy()
                particles.clear()
                self.init()
            elif (((st - self.last_st) > max(self.max_travel_time, self.update_frequency*10))
                    or ((st - self.last_st > self.update_frequency*10)
                        and self.fast and not self.distribute_fast_start)
            ):
                ## Some time has passed since the last update. Assume it was
                ## hidden, so reset the start time offset and delete the
                ## particles to start over in fast mode.
                for sprite, p in particles:
                    sprite.destroy()
                particles.clear()
                self.st_offset = st
                self.temp_fast_target = 0
                self.temp_fast_time_stopped = 0
                if self.fast:
                    self.init()
            elif (st - self.last_st) > self.update_frequency*5:
                ## Some time has passed since the last update, but not enough
                ## for the whole animation to have finished showing. We need
                ## to start a chunk of particles in fast mode to catch up to
                ## what's already included.
                ## When time originally stopped
                self.temp_fast_time_stopped = self.last_st
                ## How many particles should've been shown during that period?
                new_particles = [ ]
                for sprite, p in particles:
                    ret = p.update(st)
                    if ret is not None:
                        new_particles.append((sprite, p))
                if len(new_particles) == 0:
                    ## Just start the whole thing over
                    self.temp_fast_target = 0
                    self.temp_fast_time_stopped = 0
                    self.st_offset = st
                    ## Get rid of particles
                    for sprite, p in particles:
                        sprite.destroy()
                    particles.clear()
                    self.init()
                elif self.queue and (st - self.st_offset) < self.queue[-1]:
                    ## We didn't even finish the startup phase. How many starts
                    ## passed during the stopped time?
                    self.temp_fast_target = 0
                    for q in self.queue:
                        if q < (st - self.st_offset):
                            self.temp_fast_target += 1
                else:
                    self.temp_fast_target = self.amount

            fast = self.fast

            if new_particles is None:
                new_particles = list(particles) if particles else [ ]

            self.last_st = st
            to = st - self.st_offset
            if to < 0:
                ## Something went wrong; set the offset back to 0 and start over.
                if not new_particles:
                    self.st_offset = st
                    to = 0
                else:
                    self.st_offset = 0
                    to = st

            if not new_particles and not self.delayed_queue and self.amount > 1:
                ## Start over
                self.st_offset = st
                to = 0

            startup_over = False
            if self.queue:
                startup_over = to > self.queue[-1]
            else:
                startup_over = True

            if self.distribute_fast_start:
                ## If we want to evenly distribute particle start times every
                ## distribute_fast_start seconds, we need to calculate how many
                ## particles to make per frame.
                part_per_second = self.amount / self.distribute_fast_start
                time_since_last = st - self.last_particle_added
                max_per_frame = round(part_per_second * time_since_last)
                if to == 0:
                    max_per_frame = max(max_per_frame, 1)
            else:
                max_per_frame = self.amount

            amount = self.get_amount(to)

            if new_particles and self.temp_fast_target > 0 and len(new_particles) >= self.temp_fast_target:
                ## Done getting back up to speed
                self.temp_fast_target = 0
                self.temp_fast_time_stopped = 0
                fast_stop_time = 0
            else:
                fast_stop_time = self.temp_fast_time_stopped
                fast = True

            rv = [ ]
            if fast and amount == self.amount and amount > 1 and (
                    (not new_particles and not self.queue)
                    or (len(new_particles) < self.temp_fast_target)):
                ## Starting from scratch, nothing queued. Spawn all particles
                ## immediately.
                if new_particles and len(new_particles) < self.temp_fast_target:
                    max_per_frame = min(max_per_frame, self.temp_fast_target - len(new_particles))
                for _i in range(0, max_per_frame):
                    ## Just make a bunch of particles and return them.
                    rv.append(self.make_particle(start_time=st,
                                                fast=True,
                                                fast_stop_time=fast_stop_time))
                self.last_particle_added = st

                if self.temp_fast_target == 0:
                    return rv
                elif len(rv) + (len(new_particles) if new_particles else 0) >= self.temp_fast_target:
                    self.temp_fast_target = 0
                    self.temp_fast_time_stopped = 0
                    fast_stop_time = 0

            num_particles = len(new_particles)
            num_particles += len(rv)

            num_created = 0
            ## Check if we have any queued particles ready to start.
            if not startup_over:
                if (amount == self.amount
                        and self.queue and num_particles < len(self.queue)
                        and to >= self.queue[num_particles]):
                    ## There are queued particles ready to start.
                    while (num_particles+num_created < len(self.queue)
                            and num_created < max_per_frame
                            and num_particles+num_created < amount):
                        if to >= self.queue[num_particles+num_created]:
                            if self.temp_fast_target >= max(num_particles+num_created, 1):
                                rv.append(self.make_particle(start_time=st,
                                                    fast=True,
                                                    fast_stop_time=fast_stop_time))
                            else:
                                rv.append(self.make_particle(start_time=st,
                                                fast=False))
                            num_created += 1
                        else:
                            break

            # if not startup_over:
                if rv:
                    self.last_particle_added = st
                return rv

            ## Otherwise, we're out of the startup phase. So, if there are
            ## outstanding particles, we need to make or queue them.
            outstanding = amount - num_particles - num_created - len(self.delayed_queue)
            while outstanding > 0 and num_created < max_per_frame:
                if self.delay is None or self.temp_fast_target >= max(num_particles+num_created, 1):
                    ## No delay, just make the particle.
                    if self.temp_fast_target >= max(num_particles+num_created, 1):
                        rv.append(self.make_particle(start_time=st,
                                            fast=True,
                                            fast_stop_time=fast_stop_time))
                    else:
                        rv.append(self.make_particle(start_time=st,
                                        fast=False))
                    num_created += 1
                    outstanding -= 1
                else:
                    ## Queue the particle.
                    self.delayed_queue.append(to + self.ranged(self.delay))
                    outstanding -= 1

            if self.delayed_queue:
                delay_starts = 0
                if (amount == self.amount
                        and to >= self.delayed_queue[delay_starts]):
                    ## There are queued particles ready to start.
                    while (delay_starts < len(self.delayed_queue)
                            and num_created < max_per_frame
                            and num_particles+num_created < amount):
                        if to >= self.delayed_queue[delay_starts]:
                            if self.temp_fast_target >= max(num_particles+num_created, 1):
                                rv.append(self.make_particle(start_time=st,
                                                    fast=True,
                                                    fast_stop_time=fast_stop_time))
                            else:
                                rv.append(self.make_particle(start_time=st,
                                                fast=False))
                            num_created += 1
                            delay_starts += 1
                        else:
                            break
                ## Update the delayed queue to remove the ones we've started.
                self.delayed_queue = self.delayed_queue[delay_starts:]

            if rv:
                self.last_particle_added = st
            return rv

        def predict(self):
            if isinstance(self.image, list):
                return self.image
            return [self.image]


    class SingleImmersiveParticle(NoRollback):
        """
        A class which creates a single particle.

        Omitted parameters are as seen in ImmersiveParticleFactory.

        Parameters:
        -----------
        was_fast : bool
            Whether the factory this particle was a part of has fast=True.
            If so, we don't have to worry about the particle's starting position
            putting it ahead of the earliest particle start time. This is
            different from fast=True, which is whether this specific particle
            is spawning in fast mode (might be true if we're playing catch up
            after missed update cycles).
        origin_point : tuple or None
            If not None, the position this particle spawns from. Otherwise,
            a random position is selected based on the particle's speed.
        start_time : float
            The time when this particle was first shown.
        fast_stop_time : float
            The time when the animation last updated, if we're catching up. If
            so, then the difference between fast_stop_time and start_time is
            how long the animation wasn't updating for.
        st_offset : float
            The offset to the timebase for this animation. It can be reset to
            0 if we're in fast-restart mode, in which case we use this offset
            to pretend we're starting over from 0.

        Attributes:
        -----------
        lifetime : float or None
            Some particles receive a lifetime to ensure they are removed after
            they stop moving due to deceleration.
        xstart, ystart : float
            The starting x and y position of this particle.
        original_speed_properties : dict
            A dict containing the original speed properties of this particle,
            before adjustments based on start position.
        """
        def __init__(self, image, xspeed, yspeed, velocity, angle,
                xacceleration, yacceleration, acceleration,
                xborder, yborder, distribution, fast, position_variance,
                width, height, st_offset, was_fast, enter_exit_from_sides,
                force_direction, origin_point, start_time, fast_stop_time=None):
            self.image = image
            if xspeed is None or yspeed is None:
                ## 0 degrees is 12:00. Subtract angle from 180.
                angle = 180 - angle
                xspeed = math.sin(math.radians(angle)) * velocity
                yspeed = math.cos(math.radians(angle)) * velocity
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.xborder = xborder
            self.yborder = yborder
            new_position_variance = random.uniform(0, position_variance)
            self.start_time = start_time
            if origin_point and len(origin_point) == 4:
                ## It's a hotspot
                xoffset, yoffset, width, height = origin_point
                self.origin_point = None
            else:
                xoffset = 0
                yoffset = 0
                self.origin_point = origin_point

            self.xoffset = xoffset
            self.yoffset = yoffset
            self.width = width
            self.height = height
            if acceleration is not None:
                xacceleration = (math.sin(math.radians(angle)) * acceleration) if angle is not None else 0
                yacceleration = (math.cos(math.radians(angle)) * acceleration) if angle is not None else 0
                ## Match the signs
                xacceleration = abs(xacceleration) if acceleration >= 0 else -abs(xacceleration)
                yacceleration = abs(yacceleration) if acceleration >= 0 else -abs(yacceleration)
            self.xacceleration = xacceleration
            self.yacceleration = yacceleration
            self.lifetime = 0
            self.force_direction = force_direction
            self.enter_exit_from_sides = enter_exit_from_sides

            if new_position_variance:
                self.width += dist_covered_in_time(self.xspeed, new_position_variance, self.xacceleration)
                self.height += dist_covered_in_time(self.yspeed, new_position_variance, self.yacceleration)

            x_time, y_time = self.cap_deceleration(True)
            xacceleration = self.xacceleration
            yacceleration = self.yacceleration

            self.original_speed_properties = dict(
                xspeed=self.xspeed, yspeed=self.yspeed,
                xacceleration=self.xacceleration, yacceleration=self.yacceleration
            )

            ## Figure out if the primary direction is vertical or horizontal
            ## for this specific particle.
            if self.is_vertical:
                particle_time = y_time
            else:
                particle_time = x_time

            if fast and not fast_stop_time:
                ## Spawn it randomly on the screen.
                if self.origin_point is None:
                    self.ystart = distribution(-self.yborder, self.height + self.yborder)
                    self.xstart = distribution(-self.xborder, self.width + self.xborder)
                else:
                    self.xstart, self.ystart = self.origin_point
                    ## Pass a random amount of time to offset it
                    to = random.uniform(0, particle_time)
                    self.xstart += dist_covered_in_time(self.xspeed, to, self.xacceleration)
                    self.ystart += dist_covered_in_time(self.yspeed, to, self.yacceleration)
                self.calculate_speed_at_start()
                return

            elif not (fast and fast_stop_time) and not self.enter_exit_from_sides:
                ## This particle can't come in from the sides, so we just have
                ## to spawn it randomly on the top/bottom or left/right.
                if self.is_vertical:
                    if self.yspeed >= 0:
                        self.ystart = -self.yborder
                    else:
                        self.ystart = self.height + self.yborder
                    self.xstart = distribution(-self.xborder, self.width + self.xborder)
                else:
                    if self.xspeed >= 0:
                        self.xstart = -self.xborder
                    else:
                        self.xstart = self.width + self.xborder
                    self.ystart = distribution(-self.yborder, self.height + self.yborder)
                ## Add position variance
                if new_position_variance:
                    self.xstart -= dist_covered_in_time(self.xspeed, new_position_variance, self.xacceleration)
                    self.ystart -= dist_covered_in_time(self.yspeed, new_position_variance, self.yacceleration)
                self.calculate_speed_at_start()
                return

            ## The particle may also spawn offscreen and move onscreen, but
            ## we'll reposition it to put it at the edge of the screen. That
            ## means it can't take too long to travel to the edge, or it'll
            ## begin ahead of the earliest particle start time.
            ## This prevents things like a top-to-bottom snowfall spawning in
            ## from too far down the left/right edges.
            if fast_stop_time:
                travel_time = particle_time if was_fast else min(particle_time, (fast_stop_time-st_offset))
            else:
                travel_time = particle_time if was_fast else min(particle_time, (self.start_time-st_offset))

            if self.origin_point is None:
                ## Idea: For a particle falling down and to the right, calculate
                ## how far to the right it's fallen during travel_time.
                if self.is_vertical:
                    ## Calculate the distance travelled horizontally during the
                    ## travel time.
                    the_dist = abs(dist_covered_in_time(self.xspeed, travel_time, self.xacceleration))
                    speed1, speed2 = self.xspeed, self.yspeed
                    accel1, accel2 = self.xacceleration, self.yacceleration
                    area_dim1, area_dim2 = self.width, self.height
                    border1, border2 = self.xborder, self.yborder
                else:
                    ## Calculate the distance travelled vertically during the
                    ## travel time.
                    the_dist = abs(dist_covered_in_time(self.yspeed, travel_time, self.yacceleration))
                    speed1, speed2 = self.yspeed, self.xspeed
                    accel1, accel2 = self.yacceleration, self.xacceleration
                    area_dim1, area_dim2 = self.height, self.width
                    border1, border2 = self.yborder, self.xborder

                ## Pick an ending position along the border in the appropriate
                ## direction (e.g. particles travelling up and left need to start at
                ## least a little from the right to be seen before going offscreen).
                if speed1 < 0: # Travelling left/up, offscreen right/bottom
                    start1 = distribution(-border1, area_dim1 + the_dist)
                else: # Travelling right/down, offscreen left/top
                    start1 = distribution(-border1 - the_dist, area_dim1)
                start2 = 0

                ## Reverse engineer the other coordinate based on travel time
                if start1 < -border1 or start1 > area_dim1:
                    ## travel time = dist / speed
                    if start1 > area_dim1: # Travelling left/up, offscreen right/bottom
                        t = get_time_with_distance(accel1, speed1, area_dim1-start1, 0)
                        start1 = area_dim1
                    else: # Travelling right/down, offscreen left/top
                        #(start1 + self.border) / -speed1
                        t = get_time_with_distance(accel1, speed1, -start1-border1, 0)
                        start1 = -border1
                    ## Use the travel time to get the other position
                    start2 = dist_covered_in_time(speed2, abs(t), accel2)

                if speed2 < 0: # Travelling left/up
                    start2 += area_dim2
                else: # Travelling right/down
                    start2 -= border2

                ## Set up the actual values
                self.xstart = start1 if self.is_vertical else start2
                self.ystart = start2 if self.is_vertical else start1

            else:
                ## Already have a starting point
                self.xstart, self.ystart = self.origin_point

            ## Add position variance
            if new_position_variance:
                self.xstart -= dist_covered_in_time(self.xspeed, new_position_variance, self.xacceleration)
                self.ystart -= dist_covered_in_time(self.yspeed, new_position_variance, self.yacceleration)
            self.calculate_speed_at_start()

            if fast and fast_stop_time:
                ## This particle is filling in a gap. Run the update function
                ## to simulate time passing from fast_stop_time to start_time.
                for i in range(10):
                    ## Try 10 times to find a stop time that works.
                    stop_time = random.uniform(1.0/30.0,
                        min((self.start_time-st_offset), self.start_time-fast_stop_time)) + self.start_time
                    ret = self.update(stop_time)
                    if ret is not None:
                        break
                if ret is None:
                    ## No saving this one really; we'll just start it offscreen
                    ## so it immediately respawns
                    if self.yspeed >= 0:
                        self.ystart = self.height + self.yborder + 1
                    else:
                        self.ystart = -self.yborder - 1
                    if self.xspeed >= 0:
                        self.xstart = self.width + self.xborder + 1
                    else:
                        self.xstart = -self.xborder - 1
                    return
                ## Otherwise, we have our position
                ## Reset speeds since we'll have a different start position
                self.xspeed = xspeed
                self.yspeed = yspeed
                self.xacceleration = xacceleration
                self.yacceleration = yacceleration
                self.xstart, self.ystart, x, x = ret
                self.calculate_speed_at_start()
            return

        def cap_deceleration(self, set_vertical=False, ydist=None, xdist=None):
            """
            Cap the acceleration so the particle will always clear the area
            rather than reversing direction.
            """
            if self.origin_point is None:
                if ydist is None:
                    ydist = 2.0*self.yborder + self.height
                if xdist is None:
                    xdist = 2.0*self.xborder + self.width
            else:
                if ydist is None:
                    if self.yspeed >= 0: # Going down
                        ydist = self.height - self.origin_point[1]
                    else: # Going up
                        ydist = self.origin_point[1] + self.yborder
                if xdist is None:
                    if self.xspeed >= 0: # Going right
                        xdist = self.width - self.origin_point[0]
                    else: # Going left
                        xdist = self.origin_point[0] + self.xborder

            if self.xacceleration < 0:
                self.xacceleration = max(self.xacceleration,
                    get_maximum_decel(self.xspeed, xdist))
            if self.yacceleration < 0:
                self.yacceleration = max(self.yacceleration,
                    get_maximum_decel(self.yspeed, ydist))

            ## Calculate the final time given the acceleration
            x_time = get_time_with_distance(self.xacceleration, self.xspeed,
                xdist, float('inf'))
            y_time = get_time_with_distance(self.yacceleration, self.yspeed,
                ydist, float('inf'))

            if set_vertical:
                if self.force_direction is not None:
                    if self.force_direction == "vertical":
                        self.is_vertical = True
                    else:
                        self.is_vertical = False
                else:
                    if x_time > y_time:
                        self.is_vertical = True
                    elif x_time == y_time:
                        if abs(self.yspeed/(2.0*self.yborder + self.height)) >= abs(self.xspeed/(2.0*self.xborder + self.width)):
                            self.is_vertical = True
                        else:
                            self.is_vertical = False
                    else:
                        self.is_vertical = False

            ## Check if the particle will stop before expiring
            if self.xacceleration < 0 and not self.is_vertical:
                ## Possible for the movement to stop or reverse, and this
                ## is the primary direction.
                self.lifetime = x_time
            elif self.yacceleration < 0 and self.is_vertical:
                self.lifetime = y_time

            return x_time, y_time

        def calculate_speed_at_start(self):
            """
            If this particle has acceleration, and it's falling in a particular
            direction, and it's spawned on-screen on an edge other than its
            primary direction or because of fast=True, we need to figure out
            what the new speed is based on the acceleration that would have
            brought it to this point.
            """
            if not self.origin_point:
                if self.yspeed >= 0: # Going down
                    ydist_covered = self.ystart + self.yborder
                else: # Going up
                    ydist_covered = self.height - self.ystart
                total_ydist = self.yborder + self.height
                if self.xspeed >= 0: # Going right
                    xdist_covered = self.xstart + self.xborder
                else: # Going left
                    xdist_covered = self.width - self.xstart
                total_xdist = self.xborder + self.width
            else:
                if self.yspeed >= 0: # Going down
                    ydist_covered = self.ystart - self.origin_point[1]
                    total_ydist = self.height - self.origin_point[1]
                else: # Going up
                    ydist_covered = self.origin_point[1] - self.ystart
                    total_ydist = self.origin_point[1] + self.yborder
                if self.xspeed >= 0: # Going right
                    xdist_covered = self.xstart - self.origin_point[0]
                    total_xdist = self.width - self.origin_point[0]
                else: # Going left
                    xdist_covered = self.origin_point[0] - self.xstart
                    total_xdist = self.origin_point[0] + self.xborder

            self.yspeed = final_speed_after_distance(self.yspeed, self.yacceleration, ydist_covered)
            self.xspeed = final_speed_after_distance(self.xspeed, self.xacceleration, xdist_covered)
            self.cap_deceleration(ydist=total_ydist-ydist_covered,
                xdist=total_xdist-xdist_covered)

        def update(self, st):
            """
            Update the position of the particle based on how much
            time has passed.
            """
            to = st - self.start_time

            xdist = dist_covered_in_time(self.xspeed, to, self.xacceleration)
            ydist = dist_covered_in_time(self.yspeed, to, self.yacceleration)

            ## Nerf the particle if it's slowing down and reversed direction
            ## or hit speed 0.
            if self.lifetime and to >= self.lifetime:
                return None

            xpos = self.xstart + xdist
            ypos = self.ystart + ydist

            ## Check if it's gone offscreen, and return None if it's
            ## no longer visible to delete it and start a new particle.
            if self.yspeed <= 0 and ypos < -self.yborder and (self.is_vertical or self.enter_exit_from_sides):
                ## Off the top, travelling up
                return None
            elif self.yspeed >= 0 and ypos > self.height and (self.is_vertical or self.enter_exit_from_sides):
                ## Off the bottom, travelling down
                return None
            elif self.xspeed <= 0 and xpos < -self.xborder and (not self.is_vertical or self.enter_exit_from_sides):
                ## Off to the left, travelling left
                return None
            elif self.xspeed >= 0 and xpos > self.width and (not self.is_vertical or self.enter_exit_from_sides):
                ## Off to the right, travelling right
                return None

            return int(xpos+self.xoffset), int(ypos+self.yoffset), 0, self.image


    def get_snowblossom_kind(image, **kwargs):
        """
        A helper function for getting the appropriate Factory object out
        of an image or Particles declaration.
        """
        kind = kwargs.get("kind")
        if kind is not None:
            ## Check if it's a ImmersiveParticleFactory, and if so, inherit from it.
            if not isinstance(kind, Particles):
                ## Assume they provided the string name of an image which is
                ## a ImmersiveParticleFactory, and try to find it.
                try:
                    kind = renpy.get_registered_image(kind)
                except:
                    pass
                while isinstance(kind, AlphaMask):
                    kind = kind.child
                if isinstance(kind, renpy.display.layout.Position):
                    ## This is probably a ConditionSwitch that was created.
                    ## Grab the child
                    kind = kind.child
                    if not isinstance(kind, DynamicDisplayable):
                        raise ValueError(f"Kind provided to ImmersiveParticles is not an ImmersiveParticleFactory or registered image: {kind}")
                    ## This should be a DynamicDisplayable. Try to grab
                    ## the last case.
                    kind = kind.args[0][-1][-1]
                while isinstance(kind, AlphaMask):
                    kind = kind.child
                if not isinstance(kind, Particles):
                    raise ValueError(f"Kind provided to ImmersiveParticles is not an ImmersiveParticleFactory: {kind}")
            ## Grab the factory from the Particles
            kind = kind.factory
            factory_kwargs = kind.original_kwargs.copy()
            factory_kwargs.update(kwargs)
            kwargs = factory_kwargs
            if image is None:
                image = factory_kwargs.pop("image", None)
            else:
                factory_kwargs.pop("image", None) # Don't allow the image to be set both places
        elif image is None:
            raise ValueError("Must provide either kind or image to ImmersiveParticles.")
        return image, kind, kwargs


    def create_static_condition_switch(original, **kwargs):
        """
        A function which returns a ConditionSwitch that switches between the
        original particles and a static version of the particles based on
        STATIC_CONDITION, or just returns the original particle factory if
        static variations are not enabled.
        """
        mask_borders = kwargs.get('mask_borders', None)
        circular_mask = kwargs.get('circular_mask', None)
        if circular_mask and mask_borders is not None:
            ## They want a circular mask
            xysize = kwargs.get("xysize", (config.screen_width, config.screen_height))
            the_mask = create_radius_mask(Transform("#FFF", xysize=xysize),
                mask_borders, xysize)
            original = AlphaMask(child=original, mask=the_mask)
        elif mask_borders is not None:
            ## They want to mask this
            xysize = kwargs.get("xysize", (config.screen_width, config.screen_height))
            the_mask = create_gradient_mask(Transform("#FFF", xysize=xysize),
                mask_borders, xysize)
            original = AlphaMask(child=original, mask=the_mask)

        if ((particle_config.CREATE_STATIC_VARIANTS or kwargs.get("create_static", None))
                and kwargs.get("create_static", None) is not False):
            if kwargs.get("static_displayable", None) is not None:
                static = kwargs.get("static_displayable")
            elif (particle_config.NULL_INSTEAD_OF_STATIC
                    and kwargs.get("create_static", None) is not False):
                static = Null()
            else:
                static = CreateStaticParticles(kind=original)
            if kwargs.get("static_condition", None) is not None:
                condition = kwargs.get("static_condition")
            else:
                condition = particle_config.STATIC_CONDITION
            return ConditionSwitch(
                condition, static,
                "True", original
            )
        return original


    def ImmersiveParticles(image=None, **kwargs):
        """
        An update to SnowBlossom which has improved performance and additional
        features.

        The ImmersiveParticles effect moves multiple instances of a particle around
        the provided area. When the particle leaves the area, it is reset to
        the beginning.

        Aside from image, all parameters should be provided as keyword arguments.

        NOTE: Anytime `DISTRIBUTION` is specified as a possible value, it can be
        a str or Callable in the following form:
            A function or the name of a built-in distribution function to
            determine the starting position of a particle.
            If a string, must be one of the following:
            - `linear`: Value has an equal chance of being anywhere along an axis.
            - `gaussian`: Value is more likely to be near the middle and less
                likely to be near the edges.
            - `arcsine`: Value is more likely to be near the edges and less
                likely to be near the middle.
            If a function, it must take two floats as arguments and return a float.

        NOTE: Anytime `number or tuple` is specified as a possible value, it can
        be of the following forms:
            - A single number: All particles will use this value. e.g. 50
            - A tuple of two numbers: Each particle will have a random value
                between the two numbers. e.g. (-20, 20)
            - A tuple of two numbers and a distribution: Each particle will have
                a random value between the two numbers, determined by the
                provided distribution. e.g. (50, 120, "linear")
            - A tuple of two numbers, a distribution, and a fourth number: Each
                particle will have a random value between the two numbers,
                determined by the distribution function. The distribution
                function will be passed the first two numbers along with the
                current time since the animation started and the fourth provided
                number. e.g. (50, 120, "linear", 10)

        image : Displayable
            The displayable to use for the particles. (Renamed from `d`)
        amount : int
            The number of particles to display. (Renamed from `count`)
        particle_size : int or tuple
            The size of the particles. The particle is considered to be on the
            screen until its bounding box has cleared the area, ensuring that
            particles do not disappear abruptly. This can be a single integer, in
            which case it is used for all dimensions, or a tuple of two integers,
            in which case the first number is used for the xsize (width) and the
            second for the ysize (height). (Renamed and updated `border`)

        xspeed, yspeed : number or tuple
            The speed of the particles in the x and y directions, respectively.
            See above for the possible formats. Mutually exclusive with
            specifying velocity and angle.
        xacceleration, yacceleration : number or tuple
            The acceleration of the particles in the x and y directions,
            respectively. Negative numbers cause deceleration, regardless of
            whether the speed is negative or positive, and positive numbers
            always cause acceleration. (New)
        velocity : number or tuple
            An alternate way to specify speed, alongside the angle property.
            This is mutually exclusive with specifying xspeed and yspeed.
            See above for the possible formats. (New)
        angle : number or tuple
            An angle, in degrees from -360 to 360, which is used alongside the
            velocity property to specify the direction and speed of particles.
            0 degrees is 12:00, so from the bottom travelling straight up.
            90 degrees is 3:00, so from the left travelling straight right, and
            so on. (New)
        acceleration : number or tuple
            An alternate way to specify acceleration, alongside velocity and
            angle. This is mutually exclusive with specifying xacceleration and
            yacceleration. As before, positive numbers cause acceleration and
            negative numbers cause deceleration, regardless of the angle or
            velocity. (New)

        fast : bool
            If True, particles start in the center of the screen, with the full
            amount immediately visible. If False, they will begin falling from
            the edges of the area and take some time to reach the full amount.
            Default is False.
        distribute_fast_start : float or None
            If not None, and fast is True, then rather than all particles
            starting at the exact same time, their start times will be evenly
            distributed from 0 to the provided time. This is most often useful
            as an inherited property for particles with lifetimes, to avoid
            all particles beginning on the exact same animation frame. Default
            is None. (New)
        distribution : DISTRIBUTION
            A function or the name of a built-in distribution function to
            determine the starting position of a particle. As described above.
            Default is `linear`.

        slow_start : float or None
            If not None, this is a float time in seconds during which the
            particles will be added to the area until reaching the usual
            particle starting pace. This can be used with slow_start_ramp to
            start fewer particles at the start of the animation, and then add
            more particles as the animation progresses. It needs to be at least
            as long as the time it takes for the slowest particle to clear
            the area (otherwise it'd just be starting at the usual pace).
            Default is None. (New)
        slow_start_ramp : int
            If `slow_start` is not None, this should be an integer that's
            greater than 0. The higher the number, the more heavily particles
            will be favoured to start towards the end of the slow_start time.
            The default is 2, which has a gentle bias towards the end of the
            slow_start time. 1 is linear. (New)
        delay : number or tuple or None
            The delay before a particle will reappear on the screen after it
            has left the area. If None, the default, particles will be queued
            immediately after they leave the particle area. Most useful with
            small numbers of particles, to prevent them from syncing up or
            looking too predictable. The delay does not affect particles during
            the initial startup time; only when it is time to restart. Default
            is 0. (New)
        position_variance : float
            The amount of variance in the starting position of the particles.
            This number will be used along with the speed of the particle to
            begin it <random variance> seconds before its start position. This
            means particles do not all start at the same position (e.g. at the
            top of the screen), which avoids "line" effects due to the framerate
            syncing up the start time of particles. The exact variance is
            randomized between 0 and this value. Most useful for high numbers of
            particles or high particle speeds. Default is 0. (New)

        xysize : (width, height) or None
            The width and height of the particle area, in pixels. If not
            provided, the screen size is used. Note that particles will be
            visible outside of this area if border is greater than 0, to prevent
            particles from popping in at the edges of the area. You can
            use `crop (0.0, 0.0, 1.0, 1.0)` to avoid this. (New)
        origin_points : list of (x, y), dictionary, or None
            If provided, a list of (x, y) tuples representing points within
            the particle area where particles may originate. It may also be a
            dictionary, which takes the following keys:
            - points : list of (x, y)
                The list of origin points.
            - x_min : int or float or position
                The minimum x coordinate for origin points.
            - x_max : int or float or position
                The maximum x coordinate for origin points.
            - y_min : int or float or position
                The minimum y coordinate for origin points.
            - y_max : int or float or position
                The maximum y coordinate for origin points.
            - distribution : DISTRIBUTION
                A function or the name of a built-in distribution function to
                determine the starting position of a particle if using the
                min/max values.
            - hotspots : list of (x, y, w, h) tuples
                If provided, other keys are ignored. This is a list of hotspots
                in the format (x, y, w, h) where particles may spawn. For moving
                particles, this is treated as if it were its own area, so
                particles will spawn at the edges of the hotspot area and
                despawn once they have moved across it. New particles are shared
                across all hotspots. This can allow for custom placement of
                particles without requiring a unique mask.
            - function : Callable
                If provided, other keys are ignored. This is a function that is
                provided the width and height of the particle area, and returns
                an (x, y) tuple representing the origin point for a particle.
                This allows for complete customization over the origin point,
                e.g. spawning in a circle, or a triangle, etc.
            `points`, `hotspots`, or the min/max values must be provided as
            dictionary keys. If multiple are provided, hotspots takes priority,
            then points, then min/max values.
            If not provided, particles begin from randomly offscreen. This
            allows for effects spawning from specific locations. (New)
        force_direction : str or None
            If provided, must be one of 'vertical' or 'horizontal'. This
            forces all particles to consider their primary direction to be
            vertical or horizontal, respectively. This affects how particles
            are initially positioned when fast=False. If None, the primary
            direction is calculated based on the xspeed and yspeed values,
            which is usually accurate unless you have particularly diagonal
            particles. (New)
        enter_exit_from_sides : bool
            If True, the default, particles are allowed to spawn in from the
            sides of the screen and will be removed if they go offscreen from
            the sides. The "sides" are the left/right sides for vertical
            particles and the top/bottom sides for horizontal particles.
            If False, particles will only spawn from the top/bottom for vertical
            particles and left/right for horizontal particles, and they will
            only be removed if they go offscreen in their primary direction.
            True will be more performant for full-screen animations or animations
            where the edges are hidden; False is useful if you're sequestering
            particles to certain areas but they might fall a little outside
            of that and you don't want them popping in/out of existence. (New)
        creation_callback : callable
            If provided, a callable which takes two arguments. It is called
            when a new particle is created. The first argument is a dictionary
            of the properties of the particle, which can be modified. The
            second is the factory spawning the particle. It is not expected
            to return anything but may modify the dictionary.

        animation : bool
            If True, then this animation uses the animation timebase.
            This prevents it from resetting when shown twice. Default is False.
        update_frequency : float
            How often the animation is expected to be updating, at minimum. Gaps
            of 5*update_frequency or more will cause the animation to play catch
            up for missing particles. Set this number to higher values if you
            find the restart animations are occurring too frequently. Default
            is 1.0/30.0 aka 30FPS. (New)
        mask_borders : integer/float/position, or tuple of such, or None
            If not None, this specifies a border where a gradient will be
            applied so particles fade in over that border size. You can provide
            a single number (float/int or position object), in which case the
            same border is applied to all sides. A tuple with two numbers is
            the xborder and yborder respectively, and a tuple with four numbers
            is the (left, top, right, bottom) borders respectively. (New)
        circular_mask : bool
            If True, and mask_borders is provided, then instead of being a
            rectangular gradient, it will be elliptical from the edge of the
            particle effect. In this case, mask_borders should just be a
            singular number (float/int or position object) representing the
            border size. (New)

        create_static : bool or None
            If None, the default, the creation of a static variant of this
            particle animation depends on the value of particle_config.CREATE_STATIC_VARIANTS.
            If True, the function will return a ConditionSwitch which only
            shows the particle animation if the condition provided in
            particle_config.STATIC_CONDITION is False. Otherwise, either a
            static variant of the animation will be generated, or a Null
            displayable if particle_config.NULL_INSTEAD_OF_STATIC is True. (New)
        static_displayable : Displayable or None
            If provided, this displayable will be used as the static version of
            the animation when the condition in particle_config.STATIC_CONDITION
            is True, instead of generating a static version of the animation
            or using Null(). (New)
        num_frames : int
            If a static variant is created, this is a number of frames an
            individual particle image has. This can be literal for frame-based
            animations, or just indicate the number of distinct time periods
            to use for the static version of the animation. (New)
        frame_time_range : (float, float)
            A range of times during which the static frames can be captured for
            this animation. If the particle has a lifetime or distribute_fast_start,
            that will automatically be used if this is not provided. Otherwise,
            the default is (0.0, 1.0). (New)

        kind : Particles
            If provided, this should point to another ImmersiveParticles
            declaration. It can be provided the string name of a declared image,
            such as kind="snow_animation", or a direct reference to a Particles
            object. It can handle particles which are wrapped in ConditionSwitch
            and AlphaMask for static variants. The result is that the new
            ImmersiveParticles object will inherit all the properties of the
            provided one, except where new properties are supplied.
        """
        image, kind, kwargs = get_snowblossom_kind(image, **kwargs)
        animation = kwargs.get("animation", False)
        xysize = kwargs.get("xysize", (config.screen_width, config.screen_height))
        ret = Particles(ImmersiveParticleFactory(image=image, **kwargs),
                                    animation=animation,
                                    xysize=xysize)
        return create_static_condition_switch(ret, **kwargs)


init -500 python:
    from store.particle_vfx import ImmersiveParticles, CreateFlutterParticles
    from store.particle_vfx import CreateStaticParticles, CreatePerspectiveParticles
    from store.particle_vfx import StaticDisplayable
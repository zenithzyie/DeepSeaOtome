################################################################################
##
## Immersive Particle VFX for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
## https://feniksdev.itch.io/immersive-particle-vfx-for-renpy
##
################################################################################
## This file contains the base code for improved particle effects in Ren'Py.
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
init -980 python in particle_vfx:

    ## Particles with flutter movement and an optional lifetime

    class FlutterParticleFactory(ImmersiveParticleFactory):
        """
        A particle factory which creates particles that have fluttering motion.
        Undocumented parameters are the same as for ImmersiveParticleFactory.

        Parameters and arguments are as seen in CreateFlutterParticles.
        """
        def __init__(self, image, **kwargs):
            super(FlutterParticleFactory, self).__init__(image, **kwargs)
            self.flutter_xtime = kwargs.get('flutter_xtime', 0)
            self.flutter_ytime = kwargs.get('flutter_ytime', 0)
            self.flutter_width = kwargs.get('flutter_width', 0)
            self.flutter_height = kwargs.get('flutter_height', 0)
            self.damp_xflutter = kwargs.get('damp_xflutter', 0)
            self.damp_yflutter = kwargs.get('damp_yflutter', 0)
            self.flutter_xacceleration = kwargs.get('flutter_xacceleration', 0)
            self.flutter_yacceleration = kwargs.get('flutter_yacceleration', 0)
            self.start_anywhere = kwargs.get('start_anywhere', False)
            self.lifetime = kwargs.get('lifetime', None)
            self.strict_offscreen = kwargs.get('strict_offscreen', False)

            if self.lifetime:
                self.max_travel_time = max(*self.lifetime) if isinstance(self.lifetime, tuple) else self.lifetime
                self.init()

        def make_particle(self, **kwargs):
            """
            Create a new particle with the given keyword arguments and
            return it.
            """
            particle_kwargs = dict(image=self.ranged(self.image),
                                xspeed=self.ranged(self.xspeed),
                                yspeed=self.ranged(self.yspeed),
                                xborder=self.xborder, yborder=self.yborder,
                                position_variance=self.position_variance,
                                width=self.width, height=self.height,
                                st_offset=self.st_offset,
                                distribution=self.distribution,
                                was_fast=self.fast,
                                xacceleration=self.ranged(self.xacceleration),
                                yacceleration=self.ranged(self.yacceleration),
                                velocity=self.ranged(self.velocity),
                                acceleration=self.ranged(self.acceleration),
                                angle=self.ranged(self.angle),
                                flutter_xtime=self.ranged(self.flutter_xtime),
                                flutter_ytime=self.ranged(self.flutter_ytime),
                                flutter_width=self.ranged(self.flutter_width),
                                flutter_height=self.ranged(self.flutter_height),
                                damp_xflutter=self.ranged(self.damp_xflutter),
                                damp_yflutter=self.ranged(self.damp_yflutter),
                                flutter_xacceleration=self.ranged(self.flutter_xacceleration),
                                flutter_yacceleration=self.ranged(self.flutter_yacceleration),
                                start_anywhere=self.start_anywhere,
                                lifetime=self.ranged(self.lifetime),
                                strict_offscreen=self.strict_offscreen,
                                force_direction=self.force_direction,
                                enter_exit_from_sides=self.enter_exit_from_sides,
                                origin_point=self.ranged(self.origin_points),
                                **kwargs)
            if self.creation_callback:
                renpy.run(self.creation_callback, particle_kwargs, self)
            return FlutterParticle(**particle_kwargs)


    class FlutterParticle(SingleImmersiveParticle):
        """
        A class which creates a single particle with fluttering motion.

        Parameters and arguments are as seen in CreateFlutterParticles, as well
        as the following:

        x_flutter_start, y_flutter_start : number
            The starting point in the flutter cycle for the x/y direction, in
            radians. Helps ensure that not all particles, say, start in the
            middle and flutter left upon spawning.
        x_flutter_mult, y_flutter_mult : -1 or 1
            A multiplier for the fluttering motion in the x/y direction.
            Reverses the direction.
        """
        def __init__(self, image, xspeed, yspeed, xborder, yborder, start_time,
                fast, position_variance, width, height, st_offset, distribution,
                was_fast, xacceleration, yacceleration,flutter_xtime,
                flutter_ytime, flutter_width, flutter_height, damp_xflutter,
                damp_yflutter, flutter_xacceleration, flutter_yacceleration,
                start_anywhere, lifetime, strict_offscreen, force_direction,
                enter_exit_from_sides, velocity, acceleration, angle,
                origin_point, fast_stop_time=None):
            ## The flutter speeds are the time it takes to go from
            ## 0 to 0.5 to 0 to -0.5 to 0 using the sin function.
            ## sin(2x*pi)*0.5 goes from 0 to 0.5 to 0 to -0.5 to 0

            self.flutter_xtime = flutter_xtime
            self.flutter_ytime = flutter_ytime
            self.flutter_width = flutter_width
            self.flutter_height = flutter_height
            self.damp_xflutter = damp_xflutter
            self.damp_yflutter = damp_yflutter
            self.flutter_xacceleration = flutter_xacceleration
            self.flutter_yacceleration = flutter_yacceleration
            self.lifetime = lifetime
            self.strict_offscreen = strict_offscreen
            ## These properties help the flutter not start on the same
            ## position/cycle/direction each time
            self.x_flutter_start = random.uniform(0, math.pi)
            self.y_flutter_start = random.uniform(0, math.pi)
            self.x_flutter_mult = random.choice([-1, 1])
            self.y_flutter_mult = random.choice([-1, 1])
            self.lifetime_pct_offset = 0
            super(FlutterParticle, self).__init__(
                image, xspeed=xspeed, yspeed=yspeed, xborder=xborder, yborder=yborder,
                start_time=start_time, fast=fast or start_anywhere,
                position_variance=position_variance, width=width, height=height,
                st_offset=st_offset, distribution=distribution,
                was_fast=was_fast, xacceleration=xacceleration, yacceleration=yacceleration,
                force_direction=force_direction, fast_stop_time=fast_stop_time,
                enter_exit_from_sides=enter_exit_from_sides, velocity=velocity,
                acceleration=acceleration, angle=angle, origin_point=origin_point)
            self.lifetime = lifetime

            if not self.lifetime:
                ## Figure out the approximate lifetime of this particle based
                ## on the direction it's travelling and when it'll clear
                ## the screen edge.
                self.lifetime = self.get_lifetime(self.ystart, self.xstart,
                    self.xspeed, self.yspeed, self.yacceleration, self.xacceleration)

            if self.xspeed != 0 or self.yspeed != 0:
                original_ystart = -self.yborder if self.yspeed > 0 else self.height
                original_xstart = -self.xborder if self.xspeed > 0 else self.width
                original_lifetime = self.get_lifetime(original_ystart, original_xstart,
                    self.original_speed_properties['xspeed'], self.original_speed_properties['yspeed'],
                    self.original_speed_properties['yacceleration'], self.original_speed_properties['xacceleration'])
            else:
                original_lifetime = self.lifetime
            self.lifetime_pct_offset = 1.0 - self.lifetime / original_lifetime
            ## Figure out the flutter acceleration
            self.flutter_ytime = final_speed_after_time(self.flutter_ytime, self.flutter_yacceleration, original_lifetime-self.lifetime)
            self.flutter_xtime = final_speed_after_time(self.flutter_xtime, self.flutter_xacceleration, original_lifetime-self.lifetime)

        def get_lifetime(self, ystart, xstart, xspeed, yspeed, yacceleration, xacceleration):
            if not self.strict_offscreen:
                if yspeed < 0: # Going up
                    y_lifetime = get_time_with_distance(yacceleration,
                        yspeed, ystart+self.flutter_height+self.yborder,
                        float('inf'))
                elif yspeed > 0: # Going down
                    y_lifetime = get_time_with_distance(yacceleration,
                        yspeed, self.height - ystart + self.flutter_height + self.yborder,
                        float('inf'))
                else:
                    y_lifetime = float('inf') # No vertical movement
                if xspeed < 0: # Going left
                    x_lifetime = get_time_with_distance(xacceleration,
                            xspeed, xstart+self.flutter_width+self.xborder,
                            float('inf'))
                elif xspeed > 0: # Going right
                    x_lifetime = get_time_with_distance(xacceleration,
                            xspeed, self.width - xstart + self.flutter_width + self.xborder,
                            float('inf'))
                else:
                    x_lifetime = float('inf') # No horizontal movement
            else:
                if yspeed < 0: # Going up
                    y_lifetime = get_time_with_distance(yacceleration,
                        yspeed, ystart + self.yborder,
                        float('inf'))
                elif yspeed > 0: # Going down
                    y_lifetime = get_time_with_distance(yacceleration,
                        yspeed, self.height - ystart + self.yborder,
                        float('inf'))
                else:
                    y_lifetime = float('inf')
                if xspeed < 0: # Going left
                    x_lifetime = get_time_with_distance(xacceleration,
                            xspeed, xstart + self.xborder,
                            float('inf'))
                elif xspeed > 0: # Going right
                    x_lifetime = get_time_with_distance(xacceleration,
                            xspeed, self.width - xstart + self.xborder,
                            float('inf'))
                else:
                    x_lifetime = float('inf')

            if self.is_vertical and not self.enter_exit_from_sides:
                return y_lifetime
            elif not self.is_vertical and not self.enter_exit_from_sides:
                return x_lifetime
            else:
                return min(x_lifetime, y_lifetime)

        def update(self, st):
            """
            Update the position of this particle based on the time
            that has passed.
            """
            to = st - self.start_time

            xdist = dist_covered_in_time(self.xspeed, to, self.xacceleration)
            ydist = dist_covered_in_time(self.yspeed, to, self.yacceleration)

            xpos = self.xstart + xdist
            ypos = self.ystart + ydist

            try:
                lifetime_pct = to / self.lifetime
            except:
                lifetime_pct = 0.0

            if lifetime_pct >= 1.0:
                ## Particle has lived long enough, so it should be removed.
                return None

            pos_extra_x = self.flutter_width
            neg_extra_x = self.flutter_width
            pos_extra_y = self.flutter_height
            neg_extra_y = self.flutter_height

            ## Flutter
            if self.flutter_width and self.flutter_xtime:
                flutter_xtime = self.flutter_xtime + (self.flutter_xacceleration * to)
                flutter_xpos = math.sin(((2.0*to*math.pi)/flutter_xtime)+self.x_flutter_start) * 0.5
                amount = flutter_xpos * float(self.flutter_width) * self.x_flutter_mult
                ## What's the amount it could flutter in either direction?
                if amount > 0:
                    pos_extra_x = self.flutter_width * 0.5 - amount
                    neg_extra_x = self.flutter_width - pos_extra_x
                else:
                    neg_extra_x = self.flutter_width * 0.5 + amount
                    pos_extra_x = self.flutter_width - neg_extra_x
                ## Dampen the fluttering motion
                if self.damp_xflutter and self.damp_xflutter > 0:
                    ## Idea: 1.0 means that by 100% lifetime, amount is 0
                    ## 0.4 means that by 100% lifetime, amount is 60% of what
                    ## it started as, so the mult goes from 1 to 0.4
                    amount *= a_to_b_over_t_time(1.0, 1.0-self.damp_xflutter, lifetime_pct+self.lifetime_pct_offset)
                elif self.damp_xflutter and self.damp_xflutter < 0:
                    ## Idea: -1.0 means that at the start, flutter is 0, and
                    ## ramps up to 100%. -0.4 means that at the start, flutter is
                    ## 60% of what it will be at the end.
                    ## I want the number to go from 0.4 to 1.0
                    amount *= a_to_b_over_t_time(self.damp_xflutter+1.0, 1.0, lifetime_pct+self.lifetime_pct_offset)
                xpos += amount
            if self.flutter_height and self.flutter_ytime:
                flutter_ytime = self.flutter_ytime + (self.flutter_yacceleration * to)
                flutter_ypos = math.sin(((2.0*to*math.pi)/flutter_ytime)+self.y_flutter_start) * 0.5
                amount = flutter_ypos * float(self.flutter_height) * self.y_flutter_mult
                ## What's the amount it could flutter in either direction?
                if amount > 0:
                    pos_extra_y = self.flutter_height * 0.5 - amount
                    neg_extra_y = self.flutter_height - pos_extra_y
                else:
                    neg_extra_y = self.flutter_height * 0.5 + amount
                    pos_extra_y = self.flutter_height - neg_extra_y
                if self.damp_yflutter and self.damp_yflutter > 0:
                    amount *= a_to_b_over_t_time(1.0, 1.0-self.damp_yflutter, lifetime_pct+self.lifetime_pct_offset)
                elif self.damp_yflutter and self.damp_yflutter < 0:
                    amount *= a_to_b_over_t_time(self.damp_yflutter+1.0, 1.0, lifetime_pct+self.lifetime_pct_offset)
                ypos += amount

            ## Check if it's gone offscreen
            if self.strict_offscreen:
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
            else:
                if self.yspeed <= 0 and ypos < (-self.yborder - pos_extra_y) and (self.is_vertical or self.enter_exit_from_sides):
                    ## Off the top, travelling up
                    return None
                elif self.yspeed >= 0 and ypos > (self.height + neg_extra_y) and (self.is_vertical or self.enter_exit_from_sides):
                    ## Off the bottom, travelling down
                    return None
                elif self.xspeed <= 0 and xpos < (-self.xborder - pos_extra_x) and (not self.is_vertical or self.enter_exit_from_sides):
                    ## Off to the left, travelling left
                    return None
                elif self.xspeed >= 0 and xpos > (self.width + neg_extra_x) and (not self.is_vertical or self.enter_exit_from_sides):
                    ## Off to the right, travelling right
                    return None

            return int(xpos), int(ypos), 0, self.image


    def CreateFlutterParticles(image=None, **kwargs):
        """
        Create a fluttering particle effect.

        Note: CreateFlutterParticles takes all the same parameters as
        ImmersiveParticles, as well as the following:

        New Parameters:
        ---------------
        flutter_xtime, flutter_ytime : number or tuple
            How long it takes for a particle to complete one full flutter cycle,
            that is, how long it takes to sway to the left, right, and back.
            Higher numbers result in slower fluttering, while lower numbers
            result in quick back and forth.
        flutter_width : number or tuple
            The width of the fluttering motion in the x direction, in pixels.
        flutter_height : number or tuple
            The height of the fluttering motion in the y direction, in pixels.
        damp_xflutter, damp_yflutter : number or tuple
            If a positive number, the particle's x/y flutter will be dampened
            over the course of its lifetime (so it flutters less as it travels).
            If negative, the particle's x/y flutter will be un-dampened over the
            course of its lifetime (so it flutters more as it travels).
            The value is the percent of dampening that occurs. 1.0 or -1.0
            results in zero fluttering at the beginning/end of the particle's
            lifetime. A value like 0.5 results in the particle fluttering half
            as much at the end of its lifetime.
        flutter_xacceleration, flutter_yacceleration : number or tuple
            The acceleration of the fluttering motion in the x/y direction.
            Positive numbers increase the time it takes to complete a flutter
            cycle (has the effect of making it sway more slowly as it travels),
            while negative numbers decrease the time it takes to complete a
            flutter cycle (has the effect of making it sway more quickly as it
            travels).
        start_anywhere : bool
            If True, the particles can start anywhere on the screen when they
            are added (not just when the image is first shown). This is
            different from fast=True, as particles will still start slowly over
            time. They are simply allowed to start anywhere on-screen. Default
            is False.
        lifetime : number or tuple
            The lifetime of the particle, in seconds. If None, the particle
            will disappear when it goes offscreen.
        strict_offscreen : bool
            If True, the particle will be removed immediately when it goes
            offscreen, including if it sways offscreen due to fluttering.
            If False, the default, the particle will only be removed if no
            amount of flutter or regular movement can bring it back onscreen.
            Default is False.

        Returns:
        --------
        A new fluttering particle effect displayable.
        """
        image, kind, kwargs = get_snowblossom_kind(image, **kwargs)
        xysize = kwargs.get('xysize', None)
        animation = kwargs.get("animation", False)
        ret = Particles(FlutterParticleFactory(image=image, **kwargs),
                        animation=animation,
                        xysize=xysize or (config.screen_width,
                                            config.screen_height))
        return create_static_condition_switch(ret, **kwargs)

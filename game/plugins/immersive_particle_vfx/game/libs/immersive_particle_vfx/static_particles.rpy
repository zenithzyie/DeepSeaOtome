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
init -800 python in particle_vfx:

    class StaticParticle(Particles):
        """
        A version of the Particle class which creates a SpriteManager that does
        not need to update its children images.
        """
        def __init__(self, factory, animation=False, **properties):
            """
            @param factory: A factory object.
            """

            super(Particles, self).__init__(**properties)

            self.sm = SpriteManager(update=self.update_callback,
                predict=self.predict_callback, animation=animation,
                ignore_time=True)

            self.factory = factory
            self.particles = None

            self.properties = properties

        def update_callback(self, st):
            ret = super(Particles, self).update_callback(st)
            return None # don't actually call the update callback again

    class StaticDisplayable(renpy.Displayable):
        """
        A wrapper for a general image which does not update the provided image.
        It can optionally show it at a given time, frozen at that time.

        Attributes:
        -----------
        image : Displayable
            The image to display.
        t : float
            The time to show the image frozen at (as if that amount of time
            had passed and then the image froze on that frame).
        rendered_first_time : bool
            Whether this has been rendered at least once. Used to first render
            the image at 0 seconds, then at the provided time, to ensure it
            shows the correct frame.
        """
        def __init__(self, image, t=0, **kwargs):
            super(StaticDisplayable, self).__init__(**kwargs)
            try:
                d = renpy.displayable(image)
            except:
                d = image
            try:
                if d._duplicatable:
                    self.image = d._duplicate(None)
                    self.image._unique()
                else:
                    self.image = d
            except:
                self.image = d
            self.t = t
            self.rendered_first_time = False

        def render(self, width, height, st, at):
            ## Render it at 0 to pretend it was shown then
            if not self.rendered_first_time:
                self.rendered_first_time = True
                renpy.render(self.image, width, height, 0, 0)
            ## Then render it at the given time update
            return renpy.render(self.image, width, height, self.t, self.t)

    class StaticSnowBlossomFactory(FlutterParticleFactory):
        """
        A factory for creating particles that look like their moving equivalents,
        but the particles are static. Suitable for creating no-movement versions
        of your existing SnowBlossom effects for accessibility purposes.
        """
        def __init__(self, image, **kwargs):
            self.original_kwargs = kwargs.copy() ## For inheriting!
            num_frames = kwargs.get('num_frames', 1)
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

            self.amount = kwargs.get('amount', 10)
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
            self.fast = True
            self.delay = None
            self.position_variance = 0
            self.slow_start = None
            self.slow_start_ramp = 1
            xysize = kwargs.get('xysize', (config.screen_width, config.screen_height))
            self.width, self.height = xysize or (config.screen_width, config.screen_height)
            self.distribute_fast_start = kwargs.get('distribute_fast_start', None)
            self.force_direction = "vertical"
            self.enter_exit_from_sides = True
            self.origin_points = kwargs.get('origin_points', None)
            if self.origin_points and not isinstance(self.origin_points, dict):
                self.origin_points = dict(points=self.origin_points)
            self.update_frequency = kwargs.get('update_frequency', 1.0/30.0)
            distribution = kwargs.get('distribution', 'linear')
            if isinstance(distribution, str):
                distribution = sb_func_map[distribution]
            self.distribution = distribution
            self.distribute_fast_start = kwargs.get('distribute_fast_start', None)
            self.lifetime = kwargs.get('lifetime', None)
            self.creation_callback = kwargs.get('creation_callback', None)

            ## Wrap all images in StaticDisplayable to prevent them from updating.
            t = 0
            frame_time_range = kwargs.get('frame_time_range', None)
            if frame_time_range is None:
                if self.lifetime and isinstance(self.lifetime, (int, float)):
                    frame_time_range = (0, self.lifetime)
                elif self.lifetime and isinstance(self.lifetime, (tuple, list)):
                    frame_time_range = (0, max(self.lifetime[:2]))
                elif self.distribute_fast_start and isinstance(self.distribute_fast_start, (int, float)):
                    frame_time_range = (0, self.distribute_fast_start)
                else:
                    frame_time_range = (0, 1.0)
            frame_time = (frame_time_range[-1]-frame_time_range[0]) / num_frames if num_frames > 1 else frame_time_range[0]
            if isinstance(image, list):
                try:
                    self.image = [ ]
                    for img in image:
                        if num_frames > 1:
                            sub_image_list = [ ]
                            for j in range(num_frames):
                                t = j * frame_time + frame_time_range[0]
                                sub_image_list.append(StaticDisplayable(img, t=t))
                            self.image.append(sub_image_list)
                        else:
                            t = self.ranged(frame_time_range)
                            self.image.append(StaticDisplayable(img, t=t))
                except:
                    t = self.ranged(frame_time_range)
                    self.image = StaticDisplayable(image, t=t)
            else:
                self.image = [ ]
                for j in range(num_frames):
                    t = j * frame_time + frame_time_range[0]
                    self.image.append(StaticDisplayable(image, t=t))

            self.st_offset = 0
            self.last_st = 0
            self.last_particle_added = 0
            self.queue = [ ]
            self.delayed_queue = [ ]
            self.temp_fast_target = 0
            self.temp_fast_time_stopped = 0

            self.is_vertical = True # Irrelevant

            self.max_travel_time = 0

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

        def init(self):
            """
            No queueing happens.
            """
            return

        def create(self, particles, st):
            if not particles:
                rv = [ ]
                for i in range(self.amount):
                    rv.append(self.make_particle())
                return rv
            return None

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
                                        width=self.width, height=self.height,
                                        distribution=self.distribution,
                                        force_direction=self.force_direction,
                                        origin_point=self.ranged(self.origin_points),
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
                                        **kwargs)
            if self.creation_callback:
                renpy.run(self.creation_callback, particle_kwargs, self)
            return SingleStaticParticle(**particle_kwargs)

    class SingleStaticParticle(SingleImmersiveParticle):
        """
        A single particle that does not move. Used by StaticSnowBlossomFactory.
        """
        def __init__(self, image, xspeed, yspeed, xborder, yborder,
                width, height, distribution,
                xacceleration, yacceleration,flutter_xtime,
                flutter_ytime, flutter_width, flutter_height, damp_xflutter,
                damp_yflutter, flutter_xacceleration, flutter_yacceleration,
                start_anywhere, lifetime, force_direction,
                velocity, acceleration, angle,
                origin_point):
            self.flutter_xtime = flutter_xtime
            self.flutter_ytime = flutter_ytime
            self.flutter_width = flutter_width
            self.flutter_height = flutter_height
            self.damp_xflutter = damp_xflutter
            self.damp_yflutter = damp_yflutter
            self.flutter_xacceleration = flutter_xacceleration
            self.flutter_yacceleration = flutter_yacceleration
            self.lifetime = lifetime
            ## These properties help the flutter not start on the same
            ## position/cycle/direction each time
            self.x_flutter_start = random.uniform(0, math.pi)
            self.y_flutter_start = random.uniform(0, math.pi)
            self.x_flutter_mult = random.choice([-1, 1])
            self.y_flutter_mult = random.choice([-1, 1])
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
            self.origin_point = origin_point

            x_time, y_time = self.cap_deceleration(True)
            xacceleration = self.xacceleration
            yacceleration = self.yacceleration

            ## Figure out if the primary direction is vertical or horizontal
            ## for this specific particle.
            if self.is_vertical:
                particle_time = y_time
            else:
                particle_time = x_time

            ## Spawn it randomly on the screen.
            if origin_point is None:
                self.ystart = distribution(0, self.height-self.yborder)
                self.xstart = distribution(0, self.width-self.xborder)
            else:
                self.xstart, self.ystart = origin_point
                ## Pass a random amount of time to offset it
                to = random.uniform(0, particle_time)
                self.xstart += dist_covered_in_time(self.xspeed, to, self.xacceleration)
                self.ystart += dist_covered_in_time(self.yspeed, to, self.yacceleration)
            return

        def update(self, st):
            """
            Return this particle, frozen in place.
            """
            return int(self.xstart), int(self.ystart), 0, self.image


    class StaticPerspectiveParticleFactory(StaticSnowBlossomFactory):
        """
        A version of the perspective particle factory which creates static
        particles.
        """
        def __init__(self, image, **kwargs):
            min_scale = kwargs.get('min_scale', 0.5)
            max_scale = kwargs.get('max_scale', 1.0)
            stages = kwargs.get('stages', 1)
            border = kwargs.get('particle_size', 0)
            image_list = []
            borders = []
            lifetime = kwargs.get('lifetime', None)
            distribute_fast_start = kwargs.get('distribute_fast_start', None)
            ## Number of variations of the image we should allow.
            num_frames = kwargs.get('num_frames', 1)
            frame_time_range = kwargs.get('frame_time_range', None)
            if frame_time_range is None:
                if lifetime and isinstance(lifetime, (int, float)):
                    frame_time_range = (0, lifetime)
                elif lifetime and isinstance(lifetime, (tuple, list)):
                    frame_time_range = (0, max(lifetime[:2]))
                elif distribute_fast_start and isinstance(distribute_fast_start, (int, float)):
                    frame_time_range = (0, distribute_fast_start)
                else:
                    frame_time_range = (0, 1.0)
            frame_time = (frame_time_range[-1]-frame_time_range[0]) / num_frames if num_frames > 1 else frame_time_range[0]
            if not isinstance(border, (list, tuple)):
                border = (border, border)

            if not isinstance(image, list):
                image = [image]
            new_images = [ ]

            for img in image:
                if stages > 1:
                    for i in range(stages):
                        scale = min_scale + (i/(stages-1))*(max_scale - min_scale)
                        sub_image_list = [ ]
                        for j in range(num_frames):
                            t = j * frame_time + frame_time_range[0]
                            sub_image_list.append(StaticDisplayable(Transform(img, zoom=scale), t=t))
                        image_list.append(
                            sub_image_list
                        )
                        if len(borders) < stages:
                            borders.append( (int(border[0]*scale), int(border[1]*scale)) )
                    new_images.append(image_list)
                    image_list = []
                else:
                    sub_image_list = [ ]
                    for j in range(num_frames):
                        t = j * frame_time + frame_time_range[0]
                        sub_image_list.append(StaticDisplayable(img, t=t))
                    new_images.append([sub_image_list])
                    if len(borders) < 1:
                        borders.append(border)

            self.image = new_images
            self.borders = borders
            self.slow_start = None
            self.max_travel_time = 0
            self.amount = kwargs.get('amount', 10)
            xysize = kwargs.get('xysize', (config.screen_width, config.screen_height))
            self.width, self.height = xysize or (config.screen_width, config.screen_height)
            self.distribution = kwargs.get('distribution', 'linear')
            if isinstance(self.distribution, str):
                self.distribution = sb_func_map[self.distribution]
            self.creation_callback = kwargs.get('creation_callback', None)

        def make_particle(self, **kwargs):
            """
            Create a new particle with the given keyword arguments and
            return it.
            """
            particle_kwargs = dict(image=self.ranged(self.image),
                                        width=self.width, height=self.height,
                                        distribution=self.distribution,
                                        borders=self.borders,
                                        **kwargs)
            if self.creation_callback:
                renpy.run(self.creation_callback, particle_kwargs, self)
            return StaticPerspectiveParticle(**particle_kwargs)

        def create(self, particles, st):
            if not particles:
                rv = [ ]
                for i in range(self.amount):
                    rv.append(self.make_particle())
                return rv
            else:
                ## Assign particles zorder based on their y position
                for sprite, p in particles:
                    sprite.zorder = int(p.ystart)
            return None

        def recurse_get_all_images(self, image):
            all_images = [ ]
            if isinstance(image, list):
                for img in image:
                    all_images.extend(self.recurse_get_all_images(img))
            else:
                all_images.append(image)
            return all_images

        def predict(self):
            return self.recurse_get_all_images(self.image)


    class StaticPerspectiveParticle(SingleStaticParticle):
        """
        A class which creates a single particle that scales based
        on its vertical position. Not animated.
        """
        def __init__(self, image, width, height, distribution, borders):

            self.width = width
            self.height = height
            height_per_stage = self.height / len(image)

            ## First, pick a random stage so we can calculate the borders
            stage = renpy.random.randint(0, len(image)-1)
            xborder, yborder = borders[stage]
            self.xstart = distribution(0, self.width - xborder)
            self.ystart = distribution(stage*height_per_stage, (stage+1)*height_per_stage - yborder)

            image_list = image[stage]
            ## Pick a random image
            self.image = random.choice(image_list)

    def CreateStaticParticles(image=None, **kwargs):
        """
        A helper function to create a StaticParticle with a StaticSnowBlossomFactory.
        """
        image, kind, kwargs = get_snowblossom_kind(image, **kwargs)
        animation = kwargs.get("animation", False)
        xysize = kwargs.get("xysize", None)

        if kind is not None and isinstance(kind, PerspectiveParticleFactory):
            return Particles(StaticPerspectiveParticleFactory(image=image, **kwargs),
                                    animation=animation,
                                    xysize=xysize or (config.screen_width,
                                            config.screen_height))
        return Particles(StaticSnowBlossomFactory(image=image, **kwargs),
                                    animation=animation,
                                    xysize=xysize or (config.screen_width,
                                            config.screen_height))


init -999 python in particle_config:

    CREATE_STATIC_VARIANTS = True
    STATIC_CONDITION = "persistent.particle_animations_off"
    NULL_INSTEAD_OF_STATIC = False

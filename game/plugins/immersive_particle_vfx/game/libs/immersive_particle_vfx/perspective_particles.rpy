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
## Additional SnowBlossom variants that build off the ImmersiveParticles base.
init -980 python in particle_vfx:

    ## Particles which get smaller based on their vertical position, have
    ## a lifetime, and do not move. They may start anywhere on-screen.
    class PerspectiveParticleFactory(ImmersiveParticleFactory):
        """
        A particle factory which creates particles that scale based on
        their vertical position to create a perspective effect.
        Undocumented parameters are the same as for ImmersiveParticleFactory
        and as seen in CreatePerspectiveParticles.
        """
        def __init__(self, image, **kwargs):
            lifetime = kwargs.get('lifetime', None)
            min_scale = kwargs.get('min_scale', 0.5)
            max_scale = kwargs.get('max_scale', 1.0)
            stages = kwargs.get('stages', 1)
            slow_start = kwargs.get('slow_start', None)
            original_image = image
            if not lifetime:
                kwargs["fast"] = True
            border = kwargs.get('particle_size', 0)
            ## The images will actually be a list of Transformed images
            ## zoomed based on the number of stages. So if there are 3 stages
            ## and the zoom goes from 0.5 to 1.0, the stages are 0.5, 0.75,
            ## and 1.0.
            image_list = []
            borders = []
            if not isinstance(border, (list, tuple)):
                border = (border, border)

            if not isinstance(image, list):
                image = [image]
            new_images = [ ]

            for img in image:
                if stages > 1:
                    for i in range(stages):
                        scale = min_scale + (i/(stages-1))*(max_scale - min_scale)
                        image_list.append(Transform(img, zoom=scale))
                        if len(borders) < stages:
                            borders.append( (int(border[0]*scale), int(border[1]*scale)) )
                    new_images.append(image_list)
                    image_list = []
                else:
                    new_images.append([renpy.displayable(img)])
                    if len(borders) < 1:
                        borders.append(border)

            image = new_images

            kwargs["xspeed"] = 0
            kwargs["yspeed"] = 0
            kwargs["position_variance"] = 0
            self.area_height = kwargs.get('xysize', (config.screen_width, config.screen_height))[1]
            self.height_offset = 0
            super(PerspectiveParticleFactory, self).__init__(image, **kwargs)
            self.original_kwargs["image"] = original_image

            self.lifetime = lifetime
            self.borders = borders
            self.slow_start = slow_start

            if isinstance(self.origin_points, dict) and self.origin_points.get("hotspots", None):
                ## Adjust the actual width and height of the area based on the
                ## hotspot areas
                topmost = float('inf')
                bottommost = float('-inf')
                for hotspot in self.origin_points["hotspots"]:
                    x, y, w, h = hotspot
                    topmost = min(topmost, compute_raw(y, self.height))
                    bottommost = max(bottommost, compute_raw(y, self.height)+compute_raw(h, self.height))
                self.height_offset = topmost
                self.area_height = bottommost - topmost
            elif isinstance(self.origin_points, dict) and self.origin_points.get("points", None):
                topmost = float('inf')
                bottommost = float('-inf')
                for point in self.origin_points["points"]:
                    x, y = point
                    topmost = min(topmost, compute_raw(y, self.height))
                    bottommost = max(bottommost, compute_raw(y, self.height))
                self.height_offset = topmost
                self.area_height = bottommost - topmost
            else:
                self.area_height = self.height

            if self.lifetime:
                self.max_travel_time = max(*self.lifetime) if isinstance(self.lifetime, tuple) else self.lifetime
                self.init()

        def init(self):
            """
            Queue up the start times for the particles, based on slow start,
            fast, distribute_fast_start, and max_travel_time.
            """
            self.queue = [ ]
            if self.slow_start:
                pass
            elif self.fast:
                if self.distribute_fast_start is not None:
                    self.queue = [ random.uniform(0, self.distribute_fast_start) for _i in range(0, self.amount-1) ]
                    self.queue.insert(0, 0.0)
                    self.queue.sort()
            else:
                self.queue = [ random.uniform(0, self.max_travel_time) for _i in range(0, self.amount-1) ]
                self.queue.insert(0, 0.0)
                self.queue.sort()

        def get_amount(self, to):
            """
            Return the target number of particles on a given update cycle. Used
            for slow_start.
            """
            if not self.slow_start:
                return self.amount
            if to >= self.slow_start:
                return self.amount
            ret = self.amount - int((self.amount-1) * (1 - (to / self.slow_start) ** (self.slow_start_ramp)))
            return ret

        def make_particle(self, **kwargs):
            """
            Create a new particle with the given keyword arguments and
            return it.
            """
            particle_kwargs = dict(image=self.ranged(self.image),
                                        width=self.width, height=self.height,
                                        st_offset=self.st_offset,
                                        distribution=self.distribution,
                                        lifetime=self.ranged(self.lifetime),
                                        borders=self.borders,
                                        origin_point=self.ranged(self.origin_points),
                                        area_height=self.area_height,
                                        height_offset=self.height_offset,
                                        **kwargs)
            if self.creation_callback:
                renpy.run(self.creation_callback, particle_kwargs, self)
            return PerspectiveParticle(**particle_kwargs)

        def create(self, particles, st):
            """
            Assign particle zorder based on vertical position.
            """
            ret = super(PerspectiveParticleFactory, self).create(particles, st)
            ## Assign particles zorder based on their y position, so the bigger
            ## particles lower down are in front of the smaller ones farther
            ## back.
            if particles:
                for sprite, p in particles:
                    sprite.zorder = int(p.ystart)
            return ret

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


    class PerspectiveParticle(SingleImmersiveParticle):
        """
        A class which creates a single particle that scales based
        on its vertical position.

        Attributes:
        -----------
        lifetime : float or (float, float)
            The lifetime of the particle, in seconds. If a tuple, the lifetime
            is randomly chosen between the two values.
        """
        def __init__(self, image, start_time, fast, width, height,
                st_offset, distribution, lifetime, borders, origin_point,
                area_height, height_offset, fast_stop_time=None):

            if origin_point and len(origin_point) == 4:
                ## It's a hotspot
                xoffset, yoffset, hotspot_width, hotspot_height = origin_point
                self.origin_point = None
            else:
                self.origin_point = origin_point
                xoffset = 0
                yoffset = 0
                hotspot_width = width
                hotspot_height = height

            self.start_time = start_time
            self.fast = fast
            self.width = width
            self.height = height
            self.st_offset = st_offset
            self.lifetime = lifetime
            height_per_stage = area_height / len(image)

            ## First, pick a random stage so we can calculate the borders
            if self.origin_point:
                self.xstart, self.ystart = self.origin_point
                ## Find out what stage that is
                stage = min(int((self.ystart-height_offset) // height_per_stage), len(image)-1)
                stage = max(stage, 0)
            elif hotspot_height != height:
                ## What's the stage of the lowest ypos in the hotspot?
                lowest_stage = min(int((yoffset + hotspot_height - height_offset) // height_per_stage), len(image)-1)
                lowest_stage = max(lowest_stage, 0)
                ## Get the borders for that stage
                xborder, yborder = borders[lowest_stage]
                ## Does that still fit at the lowest part of the hotspot?
                lowest_stage = min(int((yoffset + hotspot_height - height_offset - yborder) // height_per_stage), len(image)-1)
                lowest_stage = max(lowest_stage, 0)
                xborder, yborder = borders[lowest_stage]
                ## It's in a hotspot. Pick a random height in the hotspot
                self.ystart = distribution(yoffset, yoffset + max(hotspot_height-yborder, 0))
                stage = min(int((self.ystart-height_offset) // height_per_stage), len(image)-1)
                stage = max(stage, 0)
                ## Pick a random x in the hotspot
                xborder, yborder = borders[stage]
                self.xstart = distribution(xoffset, xoffset + max(hotspot_width-xborder, 0))
            else:
                stage = renpy.random.randint(0, len(image)-1)
                xborder, yborder = borders[stage]
                self.xstart = distribution(xoffset, xoffset + max(hotspot_width-xborder, 0))
                self.ystart = distribution(stage*height_per_stage, (stage+1)*height_per_stage - yborder)

            self.image = image[stage]

        def update(self, st):
            """
            Remove this particle if its lifetime has passed.
            """
            to = st - self.start_time

            if to > self.lifetime:
                ## Particle has lived long enough, so it should be removed.
                return None

            return int(self.xstart), int(self.ystart), 0, self.image

    def CreatePerspectiveParticles(image=None, **kwargs):
        """
        Create a perspective particle effect. See ImmersiveParticles for
        explanations on distributions and (number or tuple) parameters.

        Parameters:
        -----------
        image : Displayable
            The displayable to use for the particles.
        amount : int
            The number of particles to display.
        particle_size : int or tuple
            The size of the particles. The particle is considered to be on the
            screen until its bounding box has cleared the area, ensuring that
            particles do not disappear abruptly. This can be a single integer, in
            which case it is used for all dimensions, or a tuple of two integers,
            in which case the first number is used for the xsize (width) and the
            second for the ysize (height).

        fast : bool
            If True, particles start in the center of the screen, with the full
            amount immediately visible. If False, the default, they will take
            some time to work up to the full amount.
        distribute_fast_start : float or None
            If not None, and fast is True, then rather than all particles
            starting at the exact same time, their start times will be evenly
            distributed from 0 to the provided time. This is to avoid
            all particles beginning on the exact same animation frame. Default
            is None.
        distribution : DISTRIBUTION
            A function or the name of a built-in distribution function to
            determine the starting position of a particle. As described above.
            Default is "linear".

        slow_start : float or None
            If not None, this is a float time in seconds during which the
            particles will be added to the area until reaching the usual
            particle starting pace. This can be used with slow_start_ramp to
            start fewer particles at the start of the animation, and then add
            more particles as the animation progresses. Default is None.
        slow_start_ramp : int
            If `slow_start` is not None, this should be an integer that's
            greater than 0. The higher the number, the more heavily particles
            will be favoured to start towards the end of the slow_start time.
            The default is 2, which has a gentle bias towards the end of the
            slow_start time. 1 is linear.
        delay : number or tuple or None
            The delay before a particle will reappear on the screen after it
            has left the area. If None, the default, particles will be queued
            immediately after they leave the particle area. Most useful with
            small numbers of particles, to prevent them from syncing up or
            looking too predictable. The delay does not affect particles during
            the initial startup time; only when it is time to restart. Default
            is 0.

        xysize : (width, height) or None
            The width and height of the particle area, in pixels. If not
            provided, the screen size is used. Note that particles will be
            visible outside of this area if border is greater than 0, to prevent
            particles from popping in at the edges of the area. You can
            use `crop (0.0, 0.0, 1.0, 1.0)` to avoid this.
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

        animation : bool
            If True, then this animation uses the animation timebase.
            This prevents it from resetting when shown twice. Default is False.
        update_frequency : float
            How often the animation is expected to be updating, at minimum. Gaps
            of 5*update_frequency or more will cause the animation to play catch
            up for missing particles. Set this number to higher values if you
            find the restart animations are occurring too frequently. Default
            is 1.0/30.0 aka 30FPS.
        creation_callback : callable
            If provided, a callable which takes two arguments. It is called
            when a new particle is created. The first argument is a dictionary
            of the properties of the particle, which can be modified. The
            second is the factory spawning the particle. It is not expected
            to return anything but may modify the dictionary.

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
        static_condition : str or None
            If create_static is True, this is a string representing the
            condition under which the static version of the animation will be
            shown instead of the animated version. If None, the default, then
            the condition provided in particle_config.STATIC_CONDITION is used.
            (New)
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

        min_scale : float
            The minimum scale of the particle when it is at the top of
            the area. (New)
        max_scale : float
            The maximum scale of the particle when it is at the bottom
            of the area. (New)
        stages : int
            The number of scaling stages to use between min_scale and
            max_scale. More stages results in smoother scaling, but
            requires more memory. (New)
        """
        image, kind, kwargs = get_snowblossom_kind(image, **kwargs)
        animation = kwargs.get("animation", False)
        xysize = kwargs.get('xysize', None)
        ret = Particles(PerspectiveParticleFactory(image=image, **kwargs),
                        animation=animation,
                        xysize=xysize or (config.screen_width,
                                            config.screen_height))
        return create_static_condition_switch(ret, **kwargs)

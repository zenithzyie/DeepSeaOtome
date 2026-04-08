################################################################################
##
## Immersive Particle VFX for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
## https://feniksdev.itch.io/immersive-particle-vfx-for-renpy
##
################################################################################
## This file contains the base code for a sprite sheet animation in Ren'Py.
## It is used to create animations for the various included rain splashes,
## but can be used for whatever else you like.
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
init python:

    class BasicSheetAnim(renpy.Displayable):
        """
        A displayable that draws a sprite sheet animation.

        Attributes:
        -----------
        sheet : Displayable
            The sprite sheet image.
        cols : int
            The number of columns in the sprite sheet.
        rows : int
            The number of rows in the sprite sheet.
        delays : list of float
            A list of delays for each frame in seconds. This is also used to
            know how many frames there are.
        loop : bool
            Whether the animation should loop. Default is True.
        repeats : int
            The number of times to repeat the animation. 0 means infinite.
            This overrides loop if greater than 0. Default is 0.
        anim_timebase : bool
            Whether to use the animation timebase (True) or the shown timebase.
        hold_last_frame : bool
            For non-looping animations, whether to hold the last frame when done.

        current_frame : int
            The current frame being displayed.
        current_delay : float
            The time spent on the current frame.
        done : bool
            Whether the animation is done playing.
        original_properties : dict
            A copy of the original properties passed to the constructor.
        width : int
            The width of the sprite sheet image.
        height : int
            The height of the sprite sheet image.
        img_width : int
            The width of each frame in the sprite sheet.
        img_height : int
            The height of each frame in the sprite sheet.
        current_st : float
            The current show time.
        start_st : float
            The start show time.
        last_delay : float
            The total duration of the animation.
        done_showing : bool
            Whether the animation has finished showing.
        num_loops : int
            How many times the animation has looped.
        """
        def __init__(self, sheet, cols, rows, delays, **properties):
            self.sheet = renpy.easy.displayable(sheet)
            self.cols = cols
            self.rows = rows
            self.delays = delays
            self.current_frame = 0
            self.current_delay = 0
            self.done = False
            self.original_properties = properties.copy()
            self.loop = properties.pop('loop', True)
            self.repeats = properties.pop('repeats', 0)
            self.num_loops = 1
            if self.repeats > 0:
                self.loop = True
            self.hold_last_frame = properties.pop('hold_last_frame', False)

            properties.setdefault('style', 'animation')
            self.anim_timebase = properties.pop('anim_timebase', True)

            self.width = None
            self.height = None
            self.img_width = None
            self.img_height = None

            self.current_st = None
            self.start_st = None
            self.last_delay = sum(delays)
            self.done_showing = False

            super(BasicSheetAnim, self).__init__(**properties)

        def copy(self):
            """Return a copy of this VFX."""
            return BasicSheetAnim(self.sheet, self.cols, self.rows,
                self.delays, **self.original_properties)

        def visit(self):
            return [ self.sheet ]

        def restart(self):
            self.start_st = None
            self.current_st = None
            self.done_showing = False
            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            if self.width is None:
                ## Determine the width and height of each frame
                img = renpy.render(self.sheet, width, height, st, at)
                self.width, self.height = img.get_size()
                self.img_width = self.width // self.cols
                self.img_height = self.height // self.rows

            if self.anim_timebase:
                current_t = at
            else:
                current_t = st

            if self.current_st is None:
                self.current_st = current_t
            if self.start_st is None:
                self.start_st = current_t

            t = current_t - self.start_st

            if t > self.last_delay:
                if not self.loop:
                    self.done_showing = True
                elif self.repeats > 0 and self.num_loops >= self.repeats:
                    self.done_showing = True
                else:
                    self.num_loops += 1
                    t = t % self.last_delay

            if self.done_showing:
                if self.hold_last_frame:
                    self.current_frame = len(self.delays) - 1
                    frame_x = (self.current_frame % self.cols) * self.img_width
                    frame_y = (self.current_frame // self.cols) * self.img_height
                    rv = renpy.render(self.sheet, self.width, self.height, t, at)
                    return rv.subsurface((frame_x, frame_y, self.img_width, self.img_height))
                rv = renpy.Render(self.img_width, self.img_height)
                return rv

            for i, delay in enumerate(self.delays):
                if t < delay:
                    self.current_frame = i
                    if not renpy.game.less_updates:
                        renpy.redraw(self, delay - t)

                    frame_x = (self.current_frame % self.cols) * self.img_width
                    frame_y = (self.current_frame // self.cols) * self.img_height

                    rv = renpy.render(self.sheet, self.width, self.height, t, at)
                    return rv.subsurface((frame_x, frame_y, self.img_width, self.img_height))

                else:
                    t = t - delay


    def sheet_to_images(sheet, cols, rows, width, height, image_prefix, num_frames=None):
        """
        Takes the provided sprite sheet and cuts it into individual images,
        then declares them via renpy.image with the provided image_prefix.

        Arguments:
        ----------
        sheet : Displayable
            The sprite sheet image.
        cols : int
            The number of columns in the sprite sheet.
        rows : int
            The number of rows in the sprite sheet.
        width : int
            The width of the sprite sheet image.
        height : int
            The height of the sprite sheet image.
        image_prefix : str
            The prefix to use for the generated image names. Each frame will be
            named as image_prefix followed by the frame number (starting from 0)
            e.g. if image_prefix is "raindrop" then the frames will be named
            "raindrop0", "raindrop1", etc.
        num_frames : int, optional
            The total number of frames in the sprite sheet. If not provided, it
            will be calculated as cols * rows.
        """
        if num_frames is None:
            num_frames = cols * rows
        sheet_d = renpy.easy.displayable(sheet)

        ## Determine the width and height of each frame
        img_width = width // cols
        img_height = height // rows
        for i in range(num_frames):
            frame_x = (i % cols) * img_width
            frame_y = (i // cols) * img_height
            renpy.image("{}{}".format(image_prefix, i),
                Crop((absolute(frame_x), absolute(frame_y),
                    absolute(img_width), absolute(img_height)), sheet_d))
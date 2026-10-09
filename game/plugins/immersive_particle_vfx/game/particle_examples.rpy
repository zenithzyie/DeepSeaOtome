################################################################################
##
## Immersive Particle VFX for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
## https://feniksdev.itch.io/immersive-particle-vfx-for-renpy
##
################################################################################
## This file contains an example label and several example image declarations
## walking you through how to create different effects using the included
## particle systems. You are free to delete this file if you don't
## need the examples; all the backend code is in the libs/ folder. However,
## you may want to take a look at the configuration values below and some of
## the image declarations if you aren't sure how to get started with your own
## projects.
##
## To see the examples, jump to the included test_particles label e.g.
##
# label start:
#     jump test_particles
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################

## Some configuration values you might want to adjust!
## If True, all ImmersiveParticles (and classes that inherit from it) will
## automatically create a ConditionSwitch with a static variant.
define particle_config.CREATE_STATIC_VARIANTS = True
## This is the condition in the ConditionSwitch which will cause the static
## animation to be shown instead of the usual animation.
define particle_config.STATIC_CONDITION = "persistent.particle_animations_off"
## If True, instead of a static variant of the particles, it will simply
## show a Null displayable instead (aka nothing)
## You can override this with the keyword argument static_displayable for
## any individual animation.
define particle_config.NULL_INSTEAD_OF_STATIC = False

image example_bg = Solid("#292835")
image example_backdrop = Transform("#21212d", xsize=1000, ysize=700)
image test_particle_base_example = ImmersiveParticles(
    Transform("npckc_leaf_birch_2", xsize=50, fit="contain"),
    amount=10, particle_size=50,
    xspeed=0, yspeed=200,
    xysize=(1000, 700), fast=True, animation=True
)
image test_particle_speed_example = ImmersiveParticles(
    Transform("devourfish_leaf3", xsize=50, fit="contain"),
    amount=10, particle_size=50,
    xspeed=0, yspeed=200,
    xysize=(1000, 700), fast=True, animation=True
)
image test_particle_slow_example = ImmersiveParticles(
    Transform("npckc_snow_3", xsize=20, fit="contain"),
    amount=30, particle_size=20,
    xspeed=(-10, 10), yspeed=(150, 200),
    xysize=(1000, 700), fast=False, animation=True
)
image test_particle_distr_example = ImmersiveParticles(
    Transform("bigeishe_oak_3_2", xsize=50, fit="contain"),
    amount=50, particle_size=50,
    xspeed=(-20, 20), yspeed=200,
    xysize=(1000, 700), fast=True, animation=True
)
image test_particle_startpos_example = ImmersiveParticles(
    Transform("firefly1", xsize=20, fit="contain"),
    amount=30, particle_size=20,
    velocity=200, angle=(-30, 30),
    xysize=(1000, 700), fast=True, animation=True
)
image test_particle_masks_example = ImmersiveParticles(
    rotate_leaf("devourfish_petal2", zoom=0.16),
    amount=10, particle_size=50,
    xspeed=(-15, 15), yspeed=(140, 200),
    xysize=(1000, 700), fast=True, animation=True,
    create_static=True, static_condition="test_particles_off",
)
image test_particle_example_static_petal_image = Fixed(
    Transform("devourfish_petal2", align=(0.5, 0.5)), xysize=(1000, 700))

image test_particle_flutter_example = CreateFlutterParticles(
    Transform("npckc_snow_6", xsize=20, fit="contain"),
    amount=30, particle_size=20,
    xspeed=(-10, 10), yspeed=(150, 200),
    xysize=(1000, 700), fast=True, animation=True,

    flutter_width=200, flutter_xtime=3.0,
)

image wet_drop_anim = BasicSheetAnim("raindrop_wet_drop", 1, 6, [0.04]*6, loop=False)
image dry_drop_anim = BasicSheetAnim("raindrop_dry_drop2", 1, 6, [0.04]*6, loop=False)
image test_particle_perspective_example = CreatePerspectiveParticles(
    image=Transform("wet_drop_anim", alpha=0.7),
    particle_size=(300*0.7, 149*0.7),
    amount=12, fast=True, delay=None, distribute_fast_start=0.04*6,
    xysize=(1000, 400), distribution='linear',
    min_scale=0.1, max_scale=0.6, lifetime=0.04*6, stages=4,
    animation=True, num_frames=6)

transform offcenter(crop=(0.0, 0.0, 1.0, 1.0)):
    xalign 0.5 ypos 60 crop crop

transform perspective_offcenter(crop=(0.0, 0.0, 1.0, 1.0)):
    xalign 0.5 yanchor 1.0 ypos 60+700 crop crop

## A transform that randomly rotates the particle back and forth
## or round and round. It can be provided a speed multiplier to
## make the rotation happen faster or slower.
transform rotate_leaf(child, speed_mult=1.0, zoom=1.0, alpha=1.0):
    child
    zoom zoom alpha alpha
    choice:
        rotate 0
        linear 6.3*speed_mult rotate 360
        repeat
    choice:
        rotate 0
        linear 6.0*speed_mult rotate -360
        repeat
    choice:
        rotate -60
        ease 4.1*speed_mult rotate 60
        ease 3.9*speed_mult rotate -60
        repeat
    choice:
        rotate 60+180
        ease 4.2*speed_mult rotate -60+180
        ease 3.8*speed_mult rotate 60+180
        repeat
    choice:
        rotate 0+180
        linear 6.3*speed_mult rotate 360+180
        repeat
    choice:
        rotate 0+180
        linear 6.0*speed_mult rotate -360+180
        repeat
    choice:
        rotate -60+180
        ease 4.1*speed_mult rotate 60+180
        ease 3.9*speed_mult rotate -60+180
        repeat
    choice:
        rotate 60+180
        ease 4.2*speed_mult rotate -60+180
        ease 3.8*speed_mult rotate 60+180
        repeat
default test_particles_off = False

## A transform that rotates and slightly skews the image
transform rotate_and_flip(child=None, zoom=1.0, speed_mult=1.0):
    child
    zoom zoom
    parallel:
        choice:
            rotate 0
            linear 6.3*speed_mult rotate 360
            repeat
        choice:
            rotate 0
            linear 6.0*speed_mult rotate -360
            repeat
        choice:
            rotate -60
            ease 4.1*speed_mult rotate 60
            ease 3.9*speed_mult rotate -60
            repeat
        choice:
            rotate 60
            ease 4.2*speed_mult rotate -60
            ease 3.8*speed_mult rotate 60
            repeat
    parallel:
        choice:
            xzoom 1.0
            ease 3.0*speed_mult xzoom 0.5
            ease 3.0*speed_mult xzoom 1.0
            repeat
        choice 5:
            xzoom 1.0
        choice:
            yzoom 1.0
            ease 2.8*speed_mult yzoom 0.5
            ease 3.9*speed_mult yzoom 1.0
            repeat
        choice:
            xzoom 0.5
            ease 3.4*speed_mult xzoom 1.0
            ease 3.2*speed_mult xzoom 0.5
            repeat
        choice:
            yzoom 0.5
            ease 3.9*speed_mult yzoom 1.0
            ease 2.8*speed_mult yzoom 0.5
            repeat


## An animation that fades in over fade_time and then fades out for a total
## animation time of visible_time.
transform firefly_blink(child=None, fade_time=0.2, visible_time=1.0, zoom=1.0):
    child
    zoom zoom
    alpha 0.0
    linear fade_time alpha 1.0
    pause visible_time-fade_time*2
    linear fade_time alpha 0.0
    repeat


image firefly_background_example = CreateFlutterParticles(
    ## The background fireflies are the smallest and most plentiful!
    image=firefly_blink("firefly2", zoom=0.2), particle_size=60, fast=False,
    ## For these fireflies, we'll only make them move by fluttering, so
    ## they aren't moving in straight lines.
    amount=35, xspeed=0, yspeed=0,
    ## distribute_fast_start helps so particles aren't all starting at the
    ## same time blinking in sync
    distribute_fast_start=0.5,
    ## Our flutter motion! The backmost fireflies move the least, so they
    ## have the longest times and the smallest width/height.
    flutter_xtime=(4, 7), flutter_width=(40, 90),
    flutter_ytime=(4, 7), flutter_height=(40, 90),
    ## These two properties are key for the effect. They'll start anywhere,
    ## and disappear after the animation is done.
    start_anywhere=True, lifetime=2.0,
    ## This means that if a particle goes offscreen from the fluttering motion,
    ## it is immediately removed and a new one spawned.
    strict_offscreen=True,
    ## frame_time_range means the frozen version of this animation will always
    ## show actual fireflies rather than the fade in/out period
    animation=False, frame_time_range=(0.2, 0.8))
image firefly_midground_example = CreateFlutterParticles(
    image=firefly_blink("firefly2", zoom=0.5), particle_size=70, fast=False,
    ## Not quite as many fireflies in the midground
    amount=15, xspeed=0, yspeed=0, distribute_fast_start=0.5,
    ## These fireflies have a bigger flutter width and height
    flutter_xtime=(40, 90), flutter_ytime=(40, 90),
    flutter_width=(40, 200), flutter_height=(40, 200),
    start_anywhere=True, lifetime=3.0, strict_offscreen=True,
    animation=False, frame_time_range=(0.2, 0.8))
image firefly_foreground_example = CreateFlutterParticles(
    image=firefly_blink("firefly2", zoom=1.0), particle_size=90, fast=False,
    ## These are the biggest fireflies, closest to the camera. There's only two
    ## of them, so there's a delay for when they reappear.
    amount=2, xspeed=0, yspeed=0, distribute_fast_start=0.5,
    delay=(0.0, 0.5),
    ## They also have the largest flutter distance
    flutter_xtime=(40, 70), flutter_ytime=(40, 70),
    flutter_width=(120, 300), flutter_height=(120, 300),
    start_anywhere=True, lifetime=3.0, strict_offscreen=True,
    animation=False, frame_time_range=(0.2, 0.8))

image background_rain_example = ImmersiveParticles(
    image=Transform("raindrop", alpha=0.8, xzoom=0.2, yzoom=1.5), particle_size=(9*0.2, 179*1.5),
    xysize=(1920, 750), amount=300, yspeed=(1300, 1800), xspeed=0,
    mask_borders=(0, 0, 0, 100), fast=True
)
image midground_rain_example = ImmersiveParticles(
    image=Transform("raindrop", alpha=0.8, xzoom=0.4, yzoom=2.4), particle_size=(9*0.4, 179*2.4),
    amount=120, xspeed=0, yspeed=(2000, 2500),
    slow_start=None, fast=True,
    xysize=(1920, 900), mask_borders=(0, 0, 0, 100),
)
image foreground_rain_example = ImmersiveParticles(
    image=Transform("raindrop", alpha=1.0, xzoom=0.6, yzoom=3.2), particle_size=(9*0.6, 179*3.2),
    amount=35, xspeed=0, yspeed=(2700, 3100),
    slow_start=None, fast=True,
    xysize=(1920, config.screen_height),
)

image rain_splash_example = CreatePerspectiveParticles(
    kind="test_particle_perspective_example",
    image=Transform("wet_drop_anim", alpha=0.5),
    xysize=(config.screen_width, 400), amount=8)
image rain_splash_example2 = CreatePerspectiveParticles(
    kind="test_particle_perspective_example",
    image=Transform("dry_drop_anim", alpha=0.8),
    xysize=(config.screen_width, 400), amount=8)

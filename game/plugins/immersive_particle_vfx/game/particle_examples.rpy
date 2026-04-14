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


## Below are example particle images and some helper screens.
screen test_particles_choices(items):
    vbox:
        style_prefix 'test_particles'
        for i in items:
            textbutton i.caption action i.action
style test_particles_vbox:
    is empty
    align (0.5, 0.3)
    yfill True
style test_particles_button:
    is empty
    background "#1a1a1f"
    padding (10, 20) xsize 800
    hover_background "#3b3b40"
style test_particles_button_text:
    is empty
    color "#fff"
    font "DejaVuSans.ttf"
    align (0.5, 0.5) text_align 0.5
    layout "subtitle" size 32


label test_particles():
    scene example_bg
    "Welcome to Immersive Particle VFX for Ren'Py!"
    "This label has a general walkthrough of the different particle features, as well as specific examples for different particle effects."
    "All choices loop back around to this menu."

    menu test_particles_menu(screen="test_particles_choices"):
        "Walkthroughs"

        "Image, amount, and particle_size":
            call test_particles_image_amount_size

        "Speed, velocity, and acceleration":
            call test_particles_speed

        "Slow start, fast, and delay":
            call test_particles_slow_fast_delay

        "Distribution functions":
            call test_particles_distribution

        "Start positions":
            call test_particles_start_positions

        "Masks and static images":
            call test_particles_masks_static

        "Flutter Particles":
            call test_flutter_particles

        "Perspective Particles":
            call test_perspective_particles

        "-> Particle Examples":
            jump test_particles_examples

    scene example_bg
    jump test_particles_menu

    menu test_particles_examples(screen="test_particles_choices"):
        "Falling snow":
            call test_particles_snow
        "Campfire smoke and sparks":
            call test_particles_campfire
        "Falling leaves":
            call test_particles_leaves
        "Fireflies":
            call test_particles_fireflies
        "Rain":
            call test_particles_rain
        "-> Back to walkthroughs":
            jump test_particles_menu

    scene example_bg
    jump test_particles_examples

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

label test_particles_image_amount_size():
    scene example_bg
    "At its most basic, particle effects will have an image (for the particles), an amount of particles to display on the screen, and a particle_size for the size of the image."
    show example_backdrop at offcenter
    "We'll show particles on top of this backdrop to make them easier to see."
    show test_particle_base_example as tp at offcenter
    "This example uses the \"npckc_leaf_birch_2\" image, set to be 50x50 pixels in size."
    "So, {b}particle_size=50{/b}. This means the particles spawn 50 pixels off the edge of the particle area before they start moving."
    "{b}amount=10{/b}, which means there are 10 particles on the screen. Feel free to count them!"
    show expression ImmersiveParticles(kind="test_particle_base_example", amount=100) as tp at offcenter
    "If we increase the count to 100, you'll see significantly more particles."
    show expression ImmersiveParticles(kind="test_particle_base_example", amount=10, yspeed=50, particle_size=0) as tp at offcenter
    "If we set particle_size to 0, you'll notice that the particles spawn inside the particle area now, rather than \"offscreen\"."
    show expression ImmersiveParticles(kind="test_particle_base_example",
        image=[Transform("npckc_leaf_birch_1", xsize=50, fit="contain"),
            Transform("npckc_leaf_birch_2", xsize=50, fit="contain"),
            Transform("npckc_leaf_birch_3", xsize=50, fit="contain"),]) as tp at offcenter
    "Instead of just one image, you can also provide ImmersiveParticles with a list of images. It will randomly select one of the images for every new particle."
    "Note that more particle images takes up more memory than just having one particle image. So, for very small background images, it's usually more performant to just use one particle image."
    show expression ImmersiveParticles(kind="test_particle_base_example",
        image=rotate_leaf("npckc_leaf_birch_3", zoom=0.16)) as tp at offcenter
    "You can also provide animated images as a particle, including ATL animations with randomness."
    "Animated particles are more costly to render than non-animated particles, so it's best used for particles closer to the foreground, and you can have a larger number of smaller static particles in the background."
    "That's all for this walkthrough!"
    return

label test_particles_speed():
    scene example_bg
    "When particles are on-screen, they're generally moving in some direction or another."
    "You can specify what this direction is with the various speed parameters. First, we'll look at {b}xspeed{/b} and {b}yspeed{/b}, which specify how fast the particles move in the x and y directions, respectively."
    show example_backdrop at offcenter
    show test_particle_speed_example as tp at offcenter
    "These particles have xspeed=0 and yspeed=200. That means they're falling 200 pixels per second straight down."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=200) as tp
    "If we change xspeed to 200, the particles will also move 200 pixels to the right every second. Combined with yspeed=200, this means the particles are moving diagonally down and right."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        yspeed=-200, xspeed=-200) as tp
    "You can use negative speeds also. Negative yspeed moves particles up, and negative xspeed moves particles to the left."
    "But, having just one speed is pretty uninteresting and unrealistic for a lot of effects. So, you can provide a range of speeds instead by passing in two numbers."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        yspeed=200, xspeed=(-100, 100)) as tp
    "For example, these particles have a yspeed of 200, and {b}xspeed=(-100, 100){/b}. This means that all the particles are falling down at 200 pixels per second, but the xspeed is chosen randomly between -100 and 100."
    "It can be *any* value within those ranges - including zero. So, some particles will fall more to the left, some more to the right, and some straight down."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        yspeed=(150, 250), xspeed=(-100, 100)) as tp
    "If we also set {b}yspeed=(150, 250){/b}, we get a lot of variation in falling speeds and horizontal movement."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        yspeed=-200, xspeed=0, yacceleration=200) as tp
    "Particles also have {b}yacceleration{/b} and {b}xacceleration{/b}. Positive numbers will speed a particle up in the direction it's travelling, and negative numbers will slow it down."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        yspeed=-200, xspeed=0, yacceleration=-200) as tp
    "For this base particles class, negative acceleration is capped so that particles will always get to the other side of the area before their speed hits 0."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        yspeed=(200, 600), xspeed=0, yacceleration=-9999) as tp
    "This is true even for very high negative acceleration values, and for particles going at different speeds."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=None, yspeed=None, velocity=200, angle=180) as tp
    "Besides xspeed and yspeed, you can also specify how fast particles are going using {b}velocity{/b} and {b}angle{/b}."
    "Here, the particles have velocity=200 and angle=180, which results in them going 200px per second straight down, like {b}yspeed=200{b} did."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=None, yspeed=None, velocity=200, angle=90) as tp
    "The angle has 0 degrees at 12:00 (if you imagine the angle to be the hands of the clock). So, {b}angle=90{/b} will make the particles move from left to right (3:00)."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=None, yspeed=None, velocity=200, angle=(100, 130)) as tp
    "As with xspeed and yspeed, you can provide a range of values to both velocity and angle. Here, {b}angle=(100, 130){/b}."
    "Note that this results in different movement than if we'd set xspeed and yspeed to ranges, because the velocity is constant at 200."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=None, yspeed=None, velocity=(150, 250), angle=125) as tp
    "You can provide a range of values to velocity as well. Here, {b}velocity=(150, 250){/b} and {b}angle=125{/b}."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=None, yspeed=None, velocity=200, angle=270, acceleration=200) as tp
    "Finally, you can also provide {b}acceleration{/b} to particles with velocity and an angle."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=None, yspeed=None, velocity=800, angle=270, acceleration=-999) as tp
    "As with xacceleration and yacceleration, positive numbers speed the particle up, and negative numbers slow it down. It will always reach the end of the screen before its speed hits 0."
    show expression ImmersiveParticles(kind='test_particle_speed_example',
        xspeed=None, yspeed=None, velocity=500, angle=230, xacceleration=-999) as tp
    "You can also provide xacceleration and yacceleration separately, which can result in some unique movement."
    "That's all for speed, velocity, and acceleration!"
    return

label test_particles_slow_fast_delay():
    scene example_bg
    "Particles come with several properties to adjust how they get on-screen. By default, particles will spawn at a steady rate until they reach the specified amount."
    show example_backdrop at offcenter
    show test_particle_slow_example as tp at offcenter
    "This is what that looks like."
    show expression ImmersiveParticles(kind="test_particle_slow_example",
        amount=300, yspeed=(60, 80)) as tp at offcenter
    "However, at higher particle counts, and slower speeds, this can look a bit like a \"sheet\" coming down."
    show expression ImmersiveParticles(kind="test_particle_slow_example",
        amount=300, yspeed=(60, 80), slow_start=25, slow_start_ramp=4) as tp at offcenter
    "To fix this, there is a {b}slow_start{/b} property. It's playing now."
    "This is a number of seconds, during which the number of particles added will be gradually ramped up."
    "You can adjust this ramp with {b}slow_start_ramp{/b}. 1 is linear, and higher numbers will have a heavier bias towards starting particles near the end."
    "{b}slow_start{/b} needs to be at least as long as it takes a particle to clear the screen, or else you won't see much of a difference in how it starts. If your particles seem to be coming down in a sheet, try setting {b}slow_start{/b} to a higher number."
    show expression ImmersiveParticles(kind="test_particle_slow_example",
        amount=30, yspeed=(60, 80), fast=True) as tp at offcenter
    "Besides slow start and regular start, you can also instantly begin particles on-screen with {b}fast=True{/b}."
    show expression ImmersiveParticles(kind="test_particle_slow_example",
        amount=2, yspeed=(200, 250)) as tp at offcenter
    "Finally, if you have a small particle count, you might want to use {b}delay{/b} to prevent your particles from restarting immediately after they go offscreen (as seen here)."
    show expression ImmersiveParticles(kind="test_particle_slow_example",
        amount=2, yspeed=(200, 250), delay=1.0) as tp at offcenter
    "With {b}delay=1.0{/b}, particles will wait a second before they get restarted."
    "And that's all for this tutorial!"
    return

label test_particles_distribution():
    scene example_bg
    "By default, whenever the particle animation receives a range of numbers, like {b}xspeed=(-10, 10){/b}, it will pick a number within that range, and all numbers have equal likelihood of being chosen."
    show example_backdrop at offcenter
    show test_particle_distr_example as tp at offcenter
    "The same goes for the starting position of a particle - all possible positions are equally likely to be chosen."
    "If you want to adjust the odds certain numbers are chosen, you can use a distribution function. This is a function that receives two numbers (the upper and lower range) and returns a number in that range."
    "Three functions are built-in: \"linear\", the default, weights all options equally."
    show expression ImmersiveParticles(kind="test_particle_distr_example",
        distribution="gaussian") as tp at offcenter
    "If you set {b}distribution=\"gaussian\"{/b}, then the starting positions in the middle will be more likely than the ones at the edges."
    show expression ImmersiveParticles(kind="test_particle_distr_example",
        distribution="arcsine") as tp at offcenter
    "{b}distribution=\"arcsine\"{/b} is the opposite - the starting position is more likely to be at the extremes than in the middle."
    show expression ImmersiveParticles(kind="test_particle_distr_example",
        xspeed=(-200, 200, "arcsine")) as tp at offcenter
    "Besides supplying {b}distribution{/b} for the particle starting position, you can also provide a distribution to any of the other parameters that take ranges, such as speed, acceleration, angle, or delay."
    "To do so, simply pass in the distribution function or name of an existing distribution function as the third argument, after your lower and upper range."
    "So, the animation showing now has {b}xspeed=(-200, 200, \"arcsine\"){/b}. That means speeds are more likely to be 200 or -200, and less likely to be 0."
    "The parameters unique to FlutterParticles, like {b}flutter_xtime{/b} and {b}damp_yflutter{/b} all take parameters in this format also."
    "That's all for distribution functions."
    return

label test_particles_start_positions():
    scene example_bg
    show example_backdrop at offcenter
    show test_particle_startpos_example as tp at offcenter
    "By default, particles only start at the edges of the screen."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        origin_points=[(0.5, 0.8)]) as tp at offcenter
    "However, you can also provide \"origin points\" to particles, to start them at specific locations."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        origin_points=[(0.3, 0.8), (0.7, 0.8)]) as tp at offcenter
    "{b}origin_points{/b} can be a list of (xpos, ypos) positions where particles can start, or you can also provide a dictionary."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        origin_points=dict(x_min=400, x_max=500, y_min=400, y_max=500),
        amount=200, angle=(0, 360)) as tp at offcenter
    "The dictionary takes {b}x_min{/b}, {b}x_max{/b}, {b}y_min{/b} and {b}y_max{/b} values, which are valid ranges for the particle to start in."
    show expression Fixed(Transform("#ce2020c5", xysize=(100, 100), xpos=400, ypos=400), xysize=(1000, 700)) behind tp at offcenter as tp_box
    "In the current example, particles can spawn in this box here."
    hide tp_box
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        origin_points=[(0.5, 0.5)],
        amount=200, angle=(0, 360)) as tp at offcenter
    "You can also provide a distribution function to the dictionary, or a function where you'll do the math yourself on where to place particles."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        origin_points=dict(hotspots=[(100, 100, 300, 300)])) as tp at offcenter
    "The origin points dictionary can also be provided a {b}hotspots{/b} key, which takes a list of (x, y, width, height) tuples."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        origin_points=dict(hotspots=[(100, 100, 300, 300), (150, 500, 400, 80), (500, 200, 300, 150)])) as tp at offcenter
    show expression Fixed(Window(Null(), background="#ce2020c5", area=(100, 100, 300, 300)), xysize=(1000, 700)) behind tp at offcenter as tp_box
    show expression Fixed(Window(Null(), background="#ce2020c5", area=(150, 500, 400, 80)), xysize=(1000, 700)) behind tp at offcenter as tp_box2
    show expression Fixed(Window(Null(), background="#ce2020c5", area=(500, 200, 300, 150)), xysize=(1000, 700)) behind tp at offcenter as tp_box3
    "These hotspots act like miniature particle areas, though new particles will be distributed across the particle areas. The odds are higher for a larger hotspot to get a new particle."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        position_variance=0.2, velocity=400, angle=(182, 178), amount=700) as tp at offcenter
    hide tp_box
    hide tp_box2
    hide tp_box3
    "Another property related to start positions is {b}position_variance{/b}."
    "This is a good property to use for very high particle amounts, and fast speeds, when multiple particles may need to spawn on the same update cycle."
    "{b}position_variance{/b} will slightly adjust the starting position of particles so they're not all starting exactly lined up at the edge of the particle area. It takes a number of seconds to \"rewind\" the animation to give it a slightly offset starting position."
    "The rewind time is randomized between 0 and {b}position_variance{/b} seconds."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        velocity=None, angle=None, xspeed=120, yspeed=100, yacceleration=-900,
        animation=False, fast=False) as tp at offcenter
    "Occasionally, you may need to use {b}force_direction{/b} to determine which direction particles should primarily be falling from."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        velocity=None, angle=None, xspeed=120, yspeed=100, yacceleration=-900,
        animation=False, fast=False, force_direction="vertical") as tp at offcenter
    "Generally, the animation will automatically determine the primary direction of particles based on their speeds. This influences which edge the particles spawn from when fast=False."
    "However, if the particles are not coming from the direction you want, you can force it with {b}force_direction=\"vertical\"{/b} or {b}force_direction=\"horizontal\"{/b}."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        velocity=None, angle=None, xspeed=300, yspeed=400) as tp at offcenter(crop=None)
    "Finally, there's a property called {b}enter_exit_from_sides{/b}. This is useful if you're using multiple particle animations for layering an effect, and you don't want particles to spawn in or out from the sides of the animation."
    "We'll remove the cropped sides of the backdrop to demonstrate. Here's the default setting, where particles can spawn in and out from the edges."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        velocity=None, angle=None, xspeed=300, yspeed=400,
        enter_exit_from_sides=False) as tp at offcenter(crop=None)
    "This version of the animation will not spawn or despawn from the sides. It always waits to clear the top/bottom edge (because this is a vertical animation - if it was horizontal, the opposite would be true). You can see this leaves a gap."
    show expression ImmersiveParticles(kind="test_particle_startpos_example",
        velocity=None, angle=None, xspeed=(-10, 10), yspeed=300,
        enter_exit_from_sides=False) as tp at offcenter(crop=None)
    "Normally you wouldn't want this setting, unless your particles are mostly falling straight down and you have this animation on-screen where the sides are visible (so it would be jarring to have a particle appear or disappear suddenly)."
    "That's all for this tutorial on starting positions."
    return

label test_particles_masks_static():
    scene example_bg
    show example_backdrop at offcenter
    show test_particle_masks_example as tp at offcenter
    "Sometimes you may want your particles to fade in or out at the edges instead of appearing from \"offscreen\" or in a particular spawn location."
    show expression ImmersiveParticles(kind="test_particle_masks_example",
        mask_borders=(0, 150)) as tp at offcenter
    "You can do so with {b}mask_borders{/b} and {b}circular_mask{/b}. This animation has {b}mask_borders=(0, 150){/b}, so the left/right borders are 0 and the top/right 150."
    "That means the top/bottom 150 pixels have a mask applied to make particles fade in and out."
    show expression ImmersiveParticles(kind="test_particle_masks_example",
        mask_borders=150, circular_mask=True, xspeed=(-30, 30), amount=100) as tp at offcenter
    "With {b}circular_mask=True{/b} and {b}mask_borders=150{/b}, the mask becomes circular in shape."
    show test_particle_masks_example as tp at offcenter
    "Another feature of these particles is that you can automatically create static images alongside the usual particle animation. You can use the configuration values at the top of this file to adjust the default behaviour."
    $ test_particles_off = True
    "You can also override any of the defaults. For this animation, it will simply freeze when we turn on {b}test_particles_off{/b}. This is because it has the properties {b}create_static=True{/b} and {b}static_condition=\"test_particles_off\"{/b}."
    "You might notice, though, that this also froze all the rotating particles in the exact same position. We can fix this with {b}num_frames{/b} and {b}frame_time_range{/b}."
    show expression ImmersiveParticles(kind="test_particle_masks_example",
        amount=15, num_frames=6, frame_time_range=(0.0, 3.0), animation=False) as tp at offcenter
    "{b}num_frames{/b} is the number of distinct \"frames\" we want to capture in the static version. Lower numbers are easier on calculation, but it's static, so higher numbers shouldn't noticeably impact performance. We'll go with {b}num_frames=6{/b}."
    "{b}frame_time_range{/b} is the time period during which those frames are captured. If you have an actual frame-by-frame animation, this would be the total time it takes until the animation loops, e.g. (0.0, 0.6)."
    "Here, the animations tend to be around 3-6 seconds, so we'll go with {b}frame_time_range=(0.0, 3.0){/b}."
    "You might want to set the lower range higher than 0 for some animations, such as animations which fade in and out, so you don't capture frames of the animation when it's invisible."
    $ test_particles_off = False
    "If you want, you can also provide ImmersiveParticles with a specific image to use if the condition is fulfilled with {b}static_displayable{/b} e.g. {b}static_displayable=Null(){/b} or {b}static_displayable=\"static_petal_image\"{/b}"
    show expression ImmersiveParticles(kind="test_particle_masks_example",
        static_displayable="test_particle_example_static_petal_image") as tp at offcenter
    $ test_particles_off = True
    "This image will just show one giant petal if the static condition is True."
    $ test_particles_off = False
    "That's all for masks and static images!"
    return

label test_flutter_particles():
    scene example_bg
    show example_backdrop at offcenter
    show test_particle_flutter_example as tp at offcenter
    "This tool also comes with two new particle kinds, built off of the base ImmersiveParticles class. The first is FlutterParticles."
    "As you can see, they come with additional movement options that make particles flutter back and forth on a sine curve."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        origin_points=[(0.5, 0.0)], amount=5, xspeed=0) as tp at offcenter
    show expression Fixed(Transform("#ce2020c5", xysize=(200+20, 700), xpos=position(-100, 0.5), ypos=0.0), xysize=(1000, 700)) behind tp at offcenter as tp_box
    "To define the flutter movement, there are several properties. First is {b}flutter_width{/b} and {b}flutter_height{/b}, which specify the width/height of the fluttering motion."
    "Here, it's represented by the red box. You can see all particles flutter back and forth within this area."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        origin_points=[(0.5, 0.0)], amount=5, xspeed=0, flutter_xtime=3.0) as tp at offcenter
    "You can adjust how fast it goes back and forth with {b}flutter_xtime{/b} and {b}flutter_ytime{/b}. Here it's set to {b}flutter_xtime=3.0{/b}, so it takes 3 seconds to go back and forth and return to the center."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        origin_points=[(0.5, 0.0)], amount=5, xspeed=0, flutter_xtime=1.0) as tp at offcenter
    "Smaller numbers, like 1.0, make it go back and forth much more quickly."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        origin_points=[(0.5, 0.0)], amount=5, xspeed=0, flutter_xtime=(1.0, 4.0)) as tp at offcenter
    "As with most movement properties, flutter_width/height and flutter_x/y_time all take a range of numbers, or a range of numbers + a distribution function."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        origin_points=[(0.5, 0.0)], amount=1, xspeed=0, flutter_xtime=1.0,
        damp_xflutter=1.0) as tp at offcenter
    "There is also {b}damp_xflutter{/b} and {b}damp_yflutter{/b}, which can dampen fluttering motion over time, or un-dampen it. Positive numbers (0.0-1.0) mean the particle flutters less over time - 1.0 means zero fluttering at the end."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        origin_points=[(0.5, 0.0)], amount=5, xspeed=0, flutter_xtime=1.0,
        damp_xflutter=-0.8) as tp at offcenter
    "And negative numbers (-1.0-0.0) mean the particle starts off with less fluttering and flutters more as it falls. {b}damp_xflutter=-0.8{/b} seen here means the particle flutters only 20%% of its usual amount at the start."
    hide tp_box
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        flutter_xtime=1.0, flutter_xacceleration=0.3) as tp at offcenter
    "The flutter xtime and ytime also have acceleration and deceleration via {b}flutter_xacceleration{/b} and {b}flutter_yacceleration{/b}. Positive numbers increase the time it takes to complete a flutter cycle."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        flutter_xtime=4.0, flutter_xacceleration=-0.6) as tp at offcenter
    "On the other hand, negative numbers will decrease the time it takes to complete a flutter cycle, which has the effect of \"speeding up\" the fluttering motion over time."
    show expression CreateFlutterParticles(kind="test_particle_flutter_example",
        image=firefly_blink(Transform("firefly2", zoom=0.5)), lifetime=1.0,
        distribute_fast_start=0.5, frame_time_range=(0.2, 0.8),
        flutter_height=(40, 200), flutter_ytime=(4, 7), flutter_width=(40, 200), flutter_xtime=(4, 7),
        xspeed=0, yspeed=0, start_anywhere=True) as tp at offcenter
    "Flutter particles also have a special property \"start_anywhere\", which will let particles spawn in anywhere on the screen."
    "If you use this property, may also want to provide a {b}lifetime{/b} so the particles can be replaced when the lifetime is up."
    "This is great for effects that fade in and out, such as fireflies."
    "And that's all for flutter particles!"
    return


label test_perspective_particles():
    scene example_bg
    show example_backdrop at offcenter
    show test_particle_perspective_example as tp at perspective_offcenter
    "The third particle animation variant is called PerspectiveParticles. It creates particles in \"stages\", so they look like they get farther away the higher the ypos."
    show expression CreatePerspectiveParticles(kind="test_particle_perspective_example",
        stages=2, min_scale=0.25, max_scale=0.75) as tp at perspective_offcenter
    "For example, this animation has {b}stages=2{/b}. The min_scale is set to 0.25, and the max_scale to 0.75, so the particles appear at 25%% size on the top half, and 75%% size on the bottom half."
    show test_particle_perspective_example as tp at perspective_offcenter
    "For perspective particles, you need to provide a {b}lifetime{/b} for how long the particle should be on screen before it disappears. This animation has 6 frames at 0.04s apiece, so its lifetime is 0.04*6=0.24"
    show expression CreatePerspectiveParticles(kind="test_particle_perspective_example",
        distribute_fast_start=None) as tp at perspective_offcenter
    "You may also want to set {b}distribute_fast_start{/b} to 0.24 (the length of the animation) to ensure that particles do not all begin on the same animation frame, as seen here."
    show expression CreatePerspectiveParticles(kind="test_particle_perspective_example",
        create_static=True, static_condition="test_particles_off",) as tp at perspective_offcenter
    $ test_particles_off = True
    "You should also set num_frames if you're going to use static versions of these particles, to make sure the particles do not freeze on the same frame. Here, {b}num_frames=6{/b}."
    $ test_particles_off = False
    "You don't have to provide {b}frame_time_range{/b} if the particle's lifetime or distribute_fast_start number can be used instead. Otherwise, it works as described earlier."
    show expression CreatePerspectiveParticles(kind="test_particle_perspective_example",
        amount=3, origin_points=[(x*0.1, x*0.1) for x in range(10)]) as tp at perspective_offcenter
    "Perspective particles can also be provided {b}origin_points{/b} as described earlier."
    show expression CreatePerspectiveParticles(kind="test_particle_perspective_example",
        amount=10, origin_points=dict(hotspots=[
            (0.0, 0.0, 0.4, 0.4),
            (0.6, 0.4, 0.3, 0.3),
        ]), min_size=0.3, max_size=0.7) as tp at perspective_offcenter
    "Though, you may find the {b}hotspots{/b} key for an {b}origin_points{/b} dictionary the most helpful. The height of the particle area for size distribution will be automatically calculated based on the hotspot areas."
    show expression CreatePerspectiveParticles(kind="test_particle_perspective_example",
        amount=10, origin_points=dict(hotspots=[
            (0, 0, 420, 400),
            (530, 0, 1000-530, 400),
        ]), min_size=0.3, max_size=0.7) as tp at perspective_offcenter
    show faux_tree behind tp at perspective_offcenter
    "This means you can use the image location picker to select areas where your particles will spawn, which will allow you to avoid obstacles like trees or fences in your foreground without cutting them out in an image editor."
    "And that's all for perspective particles! They're best used with animations like the rain splashes to add some depth to your background animations."
    return




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
label test_particles_fireflies():
    scene example_bg
    show firefly_background_example
    show firefly_midground_example
    show firefly_foreground_example
    "The key to these fireflies is in the layering."
    scene example_bg
    show firefly_background_example
    "Layer 1 has the smallest particles, moving the slowest, and with the highest number."
    show firefly_midground_example
    "Layer 2 has bigger particles, moving a bit faster, and with a lower number."
    show firefly_foreground_example
    "Layer 3 has only 2 particles, added on a delay, with the most movement."
    scene example_bg
    show expression CreateFlutterParticles(kind="firefly_background_example",
            xysize=(config.screen_width, 500)):
        ypos 350
    show expression CreateFlutterParticles(kind="firefly_midground_example",
            xysize=(config.screen_width, 600)):
        ypos 300
    show firefly_foreground_example
    "Depending on your background, you can adjust the xysize of these animations also so the fireflies appear to only be at a certain height."
    return


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

label test_particles_rain():
    scene example_bg
    show rain_splash_example:
        yalign 1.0
    show background_rain_example:
        yalign 0.0
    show midground_rain_example:
        yalign 0.0
    show foreground_rain_example:
        yalign 0.0
    "For rain, it really helps if you can add rain splashes around your background."
    "Often this means mapping out rectangles where you can put the particles, or making a mask to apply to the particles so they only appear in certain areas."
    "If you use AlphaMask, be sure to set the xysize of the splash animation to the xysize of the mask image."
    scene example_bg
    show rain_splash_example2:
        yalign 1.0
    "Try different splash animations for different surfaces also. Some look better on wet surfaces, and others on dry or uneven surfaces."
    show background_rain_example:
        yalign 0.0
    "As per usual, layering is also helpful."
    show midground_rain_example:
        yalign 0.0
    "In particular, if you want heavier rain, don't just speed up the particles, but also increase the yzoom of your particle image. Otherwise, your particles will look like dotted lines."
    show foreground_rain_example:
        yalign 0.0
    "If you make the particle longer instead, it looks like it's motion blurred from how fast it's falling."

    return

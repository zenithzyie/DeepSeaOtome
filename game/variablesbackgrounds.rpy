####################################################################################
#Layered Backgrounds
####################################################################################
#Hunter's Boat - Stormy
############
transform lightning1:
    alpha 0.0
    #random intervals for blinking
    choice:
        5.5
    choice:
        4.0
    choice:
        1.5
    alpha 1.0
    linear(0.8) alpha 0.0
    repeat
############
transform lightning2:
    alpha 0.0
    #random intervals for blinking
    choice:
        2.5
    choice:
        7.0
    choice:
        3.5
    alpha 1.0
    linear(0.8) alpha 0.0
    repeat
############
#Boat image
layeredimage bg_hunterboat_stormy:
    group oceansky:
        attribute oceansky default:
            "images/bgs/hunterstormyboat/stormy1.jpg"

    group lightning auto:
        attribute showlightning default:
            "images/bgs/hunterstormyboat/lightning1.png" at lightning1
        attribute showlightning2 default:
            "images/bgs/hunterstormyboat/lightning2.png" at lightning2
        attribute nolightning:
            Null()

    attribute glowybuddy:
        "images/bgs/hunterstormyboat/glow.png"

    group huntersboat:
        attribute huntersboat default:
            "images/bgs/hunterstormyboat/stormy2.png"
            #alpha 0.2
####################################################################################
#testing cetus image
####################################################################################
transform firefly_blink(child=None, fade_time=0.2, visible_time=1.0, zoom=1.0):
    child
    zoom zoom
    alpha 0.0
    linear fade_time alpha 1.0
    pause visible_time-fade_time*2
    linear fade_time alpha 0.0
    repeat
image test_firefly = ImmersiveParticles(
    Transform("firefly1", xsize=20, fit="contain"),
    amount=30, particle_size=20,
    velocity=200, angle=(-30, 30),
    xysize=(1000, 700), fast=True, animation=True
)

layeredimage bg_cetusoffice1:
#    attribute fireflies default:
#        "test_firefly" at firefly_blink
    attribute bg_cetus default:
        "images/bgs/bg cetus study.jpg"

####################################################################################
#Maris Lumina - Capital City
####################################################################################
transform luminastars_blink(child=None, fade_time=0.5, visible_time=2.0, zoom=1.0):
    child
    zoom zoom
    alpha 0.0
    linear fade_time alpha 1.0
    pause visible_time-fade_time*0.5
    linear fade_time alpha 0.0
    repeat
layeredimage bg_marislumina:
    group city:
        attribute day default:
            "images/bgs/marislumina/bg capitalcity.jpg"
        attribute night:
            "images/bgs/marislumina/bg capitalcity night.jpg"

    #group sparkle auto:
    #    attribute showsparkle default:
    #        "images/bgs/marislumina/sparkle.png" at luminastars_blink
            #fit "contain"
        attribute nosparkle:
            Null()

####################################################################################
#Prashadi's Cave
####################################################################################
#transform prashadistars1_blink(child=None, fade_time=0.8, visible_time=2.5, zoom=1.0):
#    child
#    zoom zoom
#    alpha 0.0
#    linear fade_time alpha 1.0
#    pause visible_time-fade_time*0.5
#    linear fade_time alpha 0.0
#    repeat
############
transform prashadistars2_blink(child=None, fade_time=0.8, visible_time=4.0):
    child
#    zoom zoom
    alpha 0.0
    linear fade_time alpha 1.0
    pause visible_time-fade_time*0.5
    linear fade_time alpha 0.0
    repeat
############
layeredimage bg_prashadicave:
    attribute cave default:
        "images/bgs/prashadicave/base.jpg"

    group sparkle auto:
        attribute star2 default:
            "images/bgs/prashadicave/star2.png" at prashadistars2_blink
            #fit "contain"
        attribute star1 default:
            "images/bgs/prashadicave/star1.png"
            #at prashadistars1_blink
            #fit "contain"

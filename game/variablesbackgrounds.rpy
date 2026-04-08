############
#Layered Backgrounds
############
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

############

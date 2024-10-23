
define y = Character("[player_name]", image="june")
define ny = Character(None, image="june") # for narration
define g = Character("Grandfather", image="june")
define h = Character("Hunter", image="june")
define s = Character("Skylla", image="june")
define c = Character("Cetus", image="june")
define p = Character("Prince Thioran", image="june")
define j = Character("Jorunn", image="june")
define t = Character("Townsperson", image="june")
define kid = Character("Kid", image="june")
define woman = Character("Elderly Woman", image="june")
define fishmonger = Character("Fishmonger", image="june")

define u = Character("???", image="june")
define guard = Character("Guard", image="june")
define up = Character("Striking Prince", image="june")
define uj = Character("Thieving Merman", image="june")

define furthleft = Position(xpos=0.20)
define farleft = Position(xpos=0.25)
define moreleft = Position(xpos=0.35)
define center = Position(xpos=0.45)
define moreright = Position(xpos=0.60)
define farright = Position(xpos=0.70)
define prettyfarright = Position(xpos=0.85)

default newspaper = False
default seastorm = False
default promermaid = 0
default antimermaid = 0

default menuset = set()

#Character blinking
transform blink:
    alpha 0.0
    #random intervals for blinking
    choice:
        5.5
    choice:
        4.0
    choice:
        1.5
    alpha 1.0
    0.15
    alpha 0.0
    repeat

layeredimage prince:
    group expressions:
        attribute angry:
            "prince_angry.png"
        attribute blush:
            "prince_blush.png"
        attribute neutral:
            "prince_neutral.png"
        attribute soft:
            "prince_soft.png"
        attribute sweat:
            "prince_sweat.png"
    #group eyes auto:
        #attribute blinking default:
            #"prince_eye_closed.png" at blink


init python:
    config.side_image_tag = "june"
    #proritize voice as highest volume
    config.emphasize_audio_channels = [ 'voice' ]

transform jumpin:
    ease2 0.2 yoffset -5
    ease2 0.2 yoffset 0

transform jump_up:
    pause .15
    yoffset 0
    easein .150 yoffset -25
    easeout .150 yoffset 0
    yoffset 0

#USE SHIFT + P TO OPEN THE ACTION BUTTON CAMERA THING
#YOU COULD DO ANYTHING WITH THIS HOLY FUCK

    # "NARRATION"

    # # If you want to hide the side image
    # $ config.side_image_tag = "None"

    # "This is a narration so the side image shouldn't appear."

    # # ""

    # #this above one makes a blank thing, good for comedic effect?

    # #NEED TO DO THIS EVERY TIME THERES NARRATION W/ NO PROTAG
    # # To unhide the side image
    # $ config.side_image_tag = "june"

    # m neutral "It's so cold"

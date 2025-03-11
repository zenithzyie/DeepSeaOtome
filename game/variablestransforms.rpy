
######################################################################
#Protagonist + Narrator Names
define y = Character("[player_name]", image="june", color="#ee701f")
define ny = Character(None, what_italic=True, image="june") # for narration
define narrator = Character(None, what_italic=True) #for pure narration no image
######################################################################
#Main Character Names
define h = Character("Hunter", image="june", color="#c6271d")
define s = Character("Skylla", image="june", color="#e9a1d6")
define c = Character("Cetus", image="june", color="#70418b")
define p = Character("Prince Thioran", image="june", color="#4e94c9")
define j = Character("Jorunn", image="june", color="#cb8b4f")
define g = Character("Grandfather", image="june", color="#bcc0a3")
define Pr = Character("Prashadi", image="june", color="#d3ffff")
######################################################################
#NPC Names
define t = Character("Townsperson", image="june")
define kid = Character("Kid", image="june")
define woman = Character("Elderly Woman", image="june")
define fishmonger = Character("Fishmonger", image="june")
define conductor = Character("Conductor", image="june")
define badguy = Character("Ne'er-do-well", image="june")
define paperboy = Character("Paperboy", image="june")
define guard = Character("Guard", image="june")
######################################################################
#Unknown Character Names
define u = Character("???", image="june")
define novisualthio = Character("Angry Voice", image="june", color="#4e94c9")
define novisualjor = Character("Mischievous Voice", image="june", color="#cb8b4f")
define up = Character("Princely Merman", image="june", color="#4e94c9")
define uj = Character("Thieving Merman", image="june", color="#cb8b4f")
define uhunter = Character("Strange Man", image="june", color="#c6271d")
define ucetus = Character("Royal Merman", image="june", color="#70418b")
define siren = Character("Melodious Voice", image="june", color="#e9a1d6")
define gpa = Character("Grandfather?", image="june", color="#bcc0a3")
######################################################################
#Various Variables
default newspaper = False
default childrenplaying = False
default seastorm = False
default promermaid = 0
default antimermaid = 0
######################################################################
#Various Variables 2: Electric Boogaloo
default menuset = set()
init:
    $ flash = Fade(.25, 0, .75, color="#fff")
######################################################################
#Transforms and Locations
define left2 = Position(xpos=0.32)
define right2 = Position(xpos=0.66)

define furthleft = Position(xpos=0.20)
define farleft = Position(xpos=0.25)
define moreleft = Position(xpos=0.35)
define center = Position(xpos=0.75)
define moreright = Position(xpos=0.60)
define farright = Position(xpos=0.70)
define prettyfarright = Position(xpos=0.85)

#For when we add the ability to toggle gore (eventually)
#define show_gross = False

transform ts_moveZ(dist, ts_speed=0.5):
    linear ts_speed zoom dist yoffset (-dist*100 if dist < 1.0 else (dist-1.0) * 750)

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
        attribute frown:
            "prince_frown.png"
        attribute soft:
            "prince_soft.png"
        attribute sweat:
            "prince_sweat.png"
    zoom 0.28
    ypos 730
    group eyes auto:
        attribute blinking default:
            "prince_eye_closed.png" at blink

layeredimage grandpa:
    group expressions:
        attribute happy:
            "grandpa_happy.png"
        attribute surprised:
            "grandpa_surprised.png"
        attribute neutral:
            "grandpa_neutral.png"
    zoom 0.124
    group eyes auto:
        attribute blinking default:
            "grandpa_eye_closed.png" at blink

layeredimage side june:
    group expressions:
        attribute flustered:
            "side_june_flustered.png"
        attribute huffed:
            "side_june_huffed.png"
        attribute neutral:
            "side_june_neutral.png"
        attribute shocked:
            "testjune2.png"
            zoom 0.277
            xpos -218
            ypos 20
    group eyes auto:
        attribute blinking default:
            "side_june_eye_closed.png" at blink

layeredimage skylla:
    group expressions:
        attribute neutral:
            "skylla_neutral.png"
        attribute angry:
            "SKYLLA_ANGRY.png"
        attribute angryteeth:
            "SKYLLA_ANGRYTEETH.png"
        attribute flustered:
            "SKYLLA_FLUSTERED.png"
        attribute happy:
            "SKYLLA_HAPPY.png"
        attribute nervous:
            "SKYLLA_NERVOUS.png"
        attribute sad:
            "SKYLLA_SAD.png"
        attribute surprised:
            "SKYLLA_SURPRISED.png"
    zoom 0.29
    ypos 780
    group eyes auto:
        attribute blinking default:
            "SKYLLA_BLINK.png" at blink

layeredimage prashadi:
    group expressions:
        attribute neutral:
            "prashgrandpa1.png"
            zoom 0.2
    ypos 1410

layeredimage cetus:
    group expressions:
        attribute neutral:
            "cetus_neutral.png"
    zoom 0.55
    ypos 0.07
    group eyes auto:
        attribute blinking default:
            "cetus_blink.png" at blink

layeredimage side june fish:
    group expressions:
        attribute neutral:
            "side_june_fish_neutral.png"
            zoom 0.4
            xpos 172
            ypos 250

layeredimage hunter:
    group expressions:
        attribute neutral:
            "hunter_neutral.png"
    zoom 0.3
    ypos 1.46
    group eyes auto:
        attribute blinking default:
            "hunter_eye_closed.png" at blink

layeredimage jorunn:
    group expressions:
        attribute pissed:
            "jorunn_pissed.png"
        attribute flustered:
            "jorunn_flustered.png"
        attribute neutral:
            "jorunn_neutral.png"
        attribute glee:
            "jorunn_glee.png"
        attribute sweat:
            "jorunn_sweat.png"
    zoom 0.34
    ypos 1080

init python:
    config.side_image_tag = "june"
    #proritize voice as highest volume
    config.emphasize_audio_channels = [ 'voice' ]

transform jumpin:
    ease2 0.2 yoffset -18
    ease2 0.2 yoffset 0

transform jumpin2:
    ease2 0.2 ypos 700
    ease2 0.2 ypos 730

transform jump_up:
    pause .15
    yoffset 0
    easein .150 yoffset -25
    easeout .150 yoffset 0
    yoffset 0

transform slightRight:
    xpos 0.6

transform centre:
    xpos 0.5

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

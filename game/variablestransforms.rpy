init python:
    _game_menu_screen = "prefs_menu"

######################################################################
#Click to continue icon
image ctc_pos:
    "gui/ctc_icon.png"
    xpos 0.88 ypos 0.94
    xanchor 1.0 yanchor 1.0
    linear 0.3 alpha 1.0
    pause 1.7
    linear 0.3 alpha 0.0
    pause 0.2
    repeat
######################################################################
transform logoappear:
    alpha 0.0
    xpos 40
    ypos 100
    zoom 0.7
    linear 0.3 alpha 1.0
    pause 0.2
#transform that the logo does on main menu
######################################################################
#Protagonist + Narrator Names
define y = Character("[player_name]", image="june", ctc="ctc_pos", ctc_position="fixed", namebox_background=Frame("gui/namebox_june.png", 0, 0))
define ny = Character(None, what_italic=True, image="june", ctc="ctc_pos", ctc_position="fixed") # for narration
define narrator = Character(None, what_italic=True, ctc="ctc_pos", ctc_position="fixed") #for pure narration no image
######################################################################
#Main Character Names
define h = Character("Hunter", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter", namebox_background=Frame("gui/namebox_hunter.png", 0, 0))
define s = Character("Skylla", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla", namebox_background=Frame("gui/namebox_skylla.png", 0, 0))
define c = Character("Cetus", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Cetus", namebox_background=Frame("gui/namebox_cetus.png", 0, 0))
define p = Character("Prince Thioran", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prince Thioran", namebox_background=Frame("gui/namebox_thio.png", 0, 0))
define j = Character("Jorunn", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Jorunn", namebox_background=Frame("gui/namebox_jor.png", 0, 0))
define g = Character("Grandfather", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Grandfather", namebox_background=Frame("gui/namebox_grandpa.png", 0, 0))
define Pr = Character("Prashadi", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prashadi", namebox_background=Frame("gui/namebox_prashadi.png", 0, 0))
######################################################################
#Secondary Character Names (no nameplate but has sprite)
define unna = Character("Unna", image="june", ctc="ctc_pos", ctc_position="fixed", callback = name_callback, cb_name="Unna")
define parvy = Character("Parvy", image="june", ctc="ctc_pos", ctc_position="fixed", callback = name_callback, cb_name="Parvy")
######################################################################
#NPC Names
define t = Character("Townsperson", image="june", ctc="ctc_pos", ctc_position="fixed")
define kid = Character("Kid", image="june", ctc="ctc_pos", ctc_position="fixed")
define energetickid = Character("Energetic Kid", image="june", ctc="ctc_pos", ctc_position="fixed")
define playfulkid = Character("Playful Kid", image="june", ctc="ctc_pos", ctc_position="fixed")
define woman = Character("Elderly Woman", image="june", ctc="ctc_pos", ctc_position="fixed")
define fishmonger = Character("Fishmonger", image="june", ctc="ctc_pos", ctc_position="fixed")
define conductor = Character("Conductor", image="june", ctc="ctc_pos", ctc_position="fixed")
define badguy = Character("Ne'er-do-well", image="june", ctc="ctc_pos", ctc_position="fixed")
define paperboy = Character("Paperboy", image="june", ctc="ctc_pos", ctc_position="fixed")
define guard = Character("Guard", image="june", ctc="ctc_pos", ctc_position="fixed")
define quietmaid = Character("Quiet Servant", image="june", ctc="ctc_pos", ctc_position="fixed")
define loudmaid = Character("Loud Servant", image="june", ctc="ctc_pos", ctc_position="fixed")
define moss = Character("Moss", image="june", ctc="ctc_pos", ctc_position="fixed")
######################################################################
#Unknown Character Names
define u = Character("???", image="june", ctc="ctc_pos", ctc_position="fixed")
define novisualthio = Character("Angry Voice", image="june", ctc="ctc_pos", ctc_position="fixed")
define novisualjor = Character("Mischievous Voice", image="june", ctc="ctc_pos", ctc_position="fixed")
define up = Character("Princely Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Thioran", namebox_background=Frame("gui/namebox_thio.png", 0, 0))
define uj = Character("Thieving Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Jorunn", namebox_background=Frame("gui/namebox_jor.png", 0, 0))
define uhunter = Character("Strange Man", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter",namebox_background=Frame("gui/namebox_hunter.png", 0, 0))
define novisualhunter = Character("Familiar Voice", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter", namebox_background=Frame("gui/namebox_hunter.png", 0, 0))
define ucetus = Character("Royal Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Cetus",namebox_background=Frame("gui/namebox_cetus.png", 0, 0))
define siren = Character("Melodious Voice", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla", namebox_background=Frame("gui/namebox_skylla.png", 0, 0))
define siren2 = Character("Siren", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla", namebox_background=Frame("gui/namebox_skylla.png", 0, 0))
define gpa = Character("Grandfather?", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prashadi", namebox_background=Frame("gui/namebox_grandpa.png", 0, 0))
######################################################################
#Various Variables
default newspaper = False
default childrenplaying = False
default seastorm = False
default promermaid = 0
default antimermaid = 0
default knocking = 0
default merjune = False
default hairpin = False
default coinpurse = False
default letter = False
default failescape = 0
default punchwindow = False
default bribeguard = False
default lookedatwindow = False
default pickedsomeone = False
default pickedsomething = False
default pickedforward = False
default pickedback = False
default sillyjune = False
default takehand = False
default traderpick = False
default amnesiapick = False
default kansaspick = False
default pr_questions = 0
default greens = 0
default fruit = 0
default fish = 0
default looked_through = False
default addfood = 0
default snoop = False
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

transform cflip:
    xzoom -1
#For when we add the ability to toggle gore (eventually)
#define show_gross = False
######################################################################
transform ts_moveZ(dist, ts_speed=0.5):
    linear ts_speed zoom dist yoffset (-dist*100 if dist < 1.0 else (dist-1.0) * 750)

######################################################################
#Audio / BGM
define audio.bgm_prashCave = "audio/music/02 Magic in the Meadow.mp3"
define audio.bgm_blackMarket = "audio/music/05 The Matron_s Scribe.ogg"
define audio.bgm_portTown = "audio/music/07 Song for Slumber.ogg"
define audio.bgm_cave = "audio/music/08 Mist Across the Castle Plains.mp3"
define audio.bgm_jorVilliage = "audio/music/10 Tiny Creatures Along the Way.mp3"
define audio.bgm_palaceThrone = "audio/music/11 Successful Journey.mp3"
define audio.bgm_skyllaCave = "audio/music/12 Spectral Phantoms Awake.ogg"
define audio.bgm_capital = "audio/music/13 Beatiful Reflections.ogg"
######################################################################
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

######################################################################
#FOR PROPS
transform atcamera:
    pos (422, 115)
transform atphoto:
    zoom 0.09
    subpixel True pos (510, 148)

######################################################################
## Thioran Sprite ####################################################
######################################################################
define thioran_left = Position(xpos=0.23)
define thioran_center = Position(xpos=0.45)
######################################################################
layeredimage thioran:
    at sprite_highlight('Thioran')
    group expressions auto:
        attribute frown default

    group closedeyes:
        attribute closedeyes:
            "images/sprites/thioran/expressions/thioran_expressions_blink.png"
    zoom 0.27
    ypos 730
    group eyes auto:
        attribute blinking default:
            "images/sprites/thioran/expressions/thioran_expressions_blink.png" at blink
        attribute closedeyes:
            Null()
######################################################################
## Grandpa Sprite ####################################################
######################################################################
layeredimage grandpa:
    at sprite_highlight('Grandfather')
    group expressions auto:
        attribute neutral default

    zoom 0.124
    group eyes auto:
        attribute blinking default:
            "images/sprites/grandpa/expressions/grandpa_expressions_blink.png" at blink
######################################################################
##June - Mermaid and Human Sprites ###################################
##The expressions automatically swap to mermaid w/ body mermaid ######
######################################################################
transform june_location:
    zoom 0.12
    pos (169, 151)
######################################################################
layeredimage side june:
    group bordbehind:
        attribute border default:
            "images/sprites/june/ui/border_behind.png"
            fit "contain"
            xsize 320
            pos (157, 130)
    group base:
        attribute base default:
            "images/sprites/june/base/side_june_base.png"
        attribute mermaid:
            "images/sprites/june/base/side_june_mermaid_base.png"
        at june_location

    group expressions:
        attribute neutral default:
            "images/sprites/june/expressions/side_june_expressions_neutral.png"
        attribute happy:
            "images/sprites/june/expressions/side_june_expressions_happy.png"
        attribute frustrated:
            "images/sprites/june/expressions/side_june_expressions_frustrated.png"
        attribute shocked:
            "images/sprites/june/expressions/side_june_expressions_shocked.png"
        attribute nervous:
            "images/sprites/june/expressions/side_june_expressions_nervous.png"
        attribute sad:
            "images/sprites/june/expressions/side_june_expressions_sad.png"
        attribute flustered:
            "images/sprites/june/expressions/side_june_expressions_flustered.png"
        attribute veryhappy:
            "images/sprites/june/expressions/side_june_expressions_veryhappy.png"
        at june_location

    group expressions if_any["mermaid"]:
        attribute neutral default:
            "images/sprites/june/expressions/side_june_mermaid_expressions_neutral.png"
        attribute happy:
            "images/sprites/june/expressions/side_june_mermaid_expressions_happy.png"
        attribute frustrated:
            "images/sprites/june/expressions/side_june_mermaid_expressions_frustrated.png"
        attribute shocked:
            "images/sprites/june/expressions/side_june_mermaid_expressions_shocked.png"
        attribute nervous:
            "images/sprites/june/expressions/side_june_mermaid_expressions_nervous.png"
        attribute sad:
            "images/sprites/june/expressions/side_june_mermaid_expressions_sad.png"
        attribute flustered:
            "images/sprites/june/expressions/side_june_mermaid_expressions_flustered.png"
        attribute veryhappy:
            "images/sprites/june/expressions/side_june_mermaid_expressions_veryhappy.png"
        at june_location
    group closedeyes:
        attribute closedeyes:
            "images/sprites/june/expressions/side_june_closedeyes_veryhappy.png"
            zoom 0.12
            pos (169, 153)
    group closedeyes if_any["mermaid"]:
        attribute closedeyes:
            "images/sprites/june/expressions/side_june_mermaid_closedeyes_veryhappy.png"
            zoom 0.12
            pos (169, 153)
    group eyes auto:
        attribute blinking default:
            "images/sprites/june/expressions/side_june_expressions_blink.png" at blink
            zoom 0.12
            pos (169, 153)
        attribute veryhappy:
            Null()
        attribute closedeyes:
            Null()
    group hairbrow:
        attribute hairbrow default:
            "images/sprites/june/base/side_june_hairbrow.png"
        at june_location
    group hairbrow if_any["mermaid"]:
        attribute hairbrow default:
            "images/sprites/june/base/side_june_mermaid_hairbrow.png"
        at june_location
    group frontborder:
        attribute frontborder default:
            "images/sprites/june/ui/border_front.png"
            fit "contain"
            xsize 320
            pos (157, 130)
######################################################################
## June Fish Sprite ##################################################
######################################################################
layeredimage side june fish:
    group expressions:
        attribute neutral:
            "images/sprites/june/base/side_june_fish_neutral.png"
            zoom 0.12
            xpos 138
            ypos 310
######################################################################
## Skylla Sprite #####################################################
######################################################################
layeredimage skylla:
    at sprite_highlight('Skylla')
    group expressions auto:
        attribute neutral default

    zoom 0.29
    ypos 780
    group eyes auto:
        attribute blinking default:
            "images/sprites/skylla/expressions/skylla_expressions_blink.png" at blink
######################################################################
## Prashadi Sprite ###################################################
######################################################################
layeredimage prashadi:
    at sprite_highlight('Prashadi')
    group expressions auto:
        attribute neutral default
        fit "contain"
        xysize (1250,1250)
    group eyes auto:
        attribute blinking default:
            "images/sprites/prashadi/expressions/prashadi_expressions_blink.png" at blink
            fit "contain"
            xysize (1250,1250)
    ypos 1300
######################################################################
##Cetus Sprite #######################################################
######################################################################
define cetus_right = Position(xpos=0.46)
define cetus_center = Position(xpos=0.29)
######################################################################
layeredimage cetus:
    at sprite_highlight('Cetus')
    attribute base default

    group expressions auto:
        attribute neutral default

    group closedeyes:
        attribute closedeyes:
            "images/sprites/cetus/expressions/cetus_expressions_blink.png"
    zoom 0.16
    ypos 60
    group eyes auto:
        attribute blinking default:
            "images/sprites/cetus/expressions/cetus_expressions_blink.png" at blink
        attribute closedeyes:
            Null()
######################################################################
##Hunter Sprite ######################################################
######################################################################
define hunter_center = Position(xpos=0.53)
######################################################################
layeredimage hunter:
    at sprite_highlight('Hunter')
    attribute base default

    group expressions auto:
        attribute neutral default

    group coverings:
        attribute facemask:
            "images/sprites/hunter/accessories/hunter_mask.png"

    group eyes auto:
        attribute blinking default:
            "images/sprites/hunter/expressions/hunter_blink.png" at blink
        attribute flustered:
            Null()
    zoom 0.15
    ypos 1.17
######################################################################
## Jorunn Sprite #####################################################
######################################################################
define jorunn_center = Position(xpos=0.47)
define jorunn_right = Position(xpos=0.65)
######################################################################
layeredimage jorunn:
    at sprite_highlight('Jorunn')
    attribute base default

    group expressions auto:
        attribute neutral default

    zoom 0.133
    ypos 804
######################################################################
## Unna Sprite #######################################################
######################################################################
define unna_left = Position(xpos=0.34)
######################################################################
layeredimage unna:
    at sprite_highlight('Unna')
    attribute base default

    group expressions auto:
        attribute neutral default

    zoom 0.133
    ypos 804
######################################################################
## Parvy Sprite ######################################################
######################################################################
define parvy_left = Position(xpos=0.13)
define parvy_center = Position(xpos=0.47)
######################################################################
layeredimage parvy:
    at sprite_highlight('Parvy')
    attribute base default

    group expressions auto:
        attribute neutral default

    zoom 0.133
    ypos 804
######################################################################
init python:
    config.side_image_tag = "june"
    #proritize voice as highest volume
    config.emphasize_audio_channels = [ 'voice' ]

transform jumpin:
    ease 0.2 yoffset -18
    ease 0.2 yoffset 0

transform jumpin2:
    ease 0.2 ypos 700
    ease 0.2 ypos 730

transform jump_up:
    pause .15
    yoffset 0
    easein .150 yoffset -25
    easeout .150 yoffset 0
    yoffset 0

transform slightRight:
    xpos 0.6

transform centre:
    xpos 0.55

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

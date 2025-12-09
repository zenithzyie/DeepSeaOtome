
#Click to continue icon
image ctc_pos:
    "gui/ctc_icon.png"
    xpos 0.78 ypos 0.94
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
#Logo Imagebutton
#imagebutton auto ("gui/logo_%s.png") focus_mask True action NullAction()
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
#NPC Names
define t = Character("Townsperson", image="june", ctc="ctc_pos", ctc_position="fixed")
define kid = Character("Kid", image="june", ctc="ctc_pos", ctc_position="fixed")
define woman = Character("Elderly Woman", image="june", ctc="ctc_pos", ctc_position="fixed")
define fishmonger = Character("Fishmonger", image="june", ctc="ctc_pos", ctc_position="fixed")
define conductor = Character("Conductor", image="june", ctc="ctc_pos", ctc_position="fixed")
define badguy = Character("Ne'er-do-well", image="june", ctc="ctc_pos", ctc_position="fixed")
define paperboy = Character("Paperboy", image="june", ctc="ctc_pos", ctc_position="fixed")
define guard = Character("Guard", image="june", ctc="ctc_pos", ctc_position="fixed")
define quietmaid = Character("Quiet Servant", image="june", ctc="ctc_pos", ctc_position="fixed")
define loudmaid = Character("Loud Servant", image="june", ctc="ctc_pos", ctc_position="fixed")
######################################################################
#Unknown Character Names
define u = Character("???", image="june", ctc="ctc_pos", ctc_position="fixed")
define novisualthio = Character("Angry Voice", image="june", ctc="ctc_pos", ctc_position="fixed")
define novisualjor = Character("Mischievous Voice", image="june", ctc="ctc_pos", ctc_position="fixed")
define up = Character("Princely Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prince Thioran", namebox_background=Frame("gui/namebox_thio.png", 0, 0))
define uj = Character("Thieving Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Jorunn", namebox_background=Frame("gui/namebox_jor.png", 0, 0))
define uhunter = Character("Strange Man", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter",namebox_background=Frame("gui/namebox_hunter.png", 0, 0))
define ucetus = Character("Royal Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Cetus",namebox_background=Frame("gui/namebox_cetus.png", 0, 0))
define siren = Character("Melodious Voice", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla", namebox_background=Frame("gui/namebox_skylla.png", 0, 0))
define gpa = Character("Grandfather?", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prashadi", namebox_background=Frame("gui/namebox_grandpa.png", 0, 0))
######################################################################
#Various Variables
default newspaper = False
default childrenplaying = False
default seastorm = False
default promermaid = 0
default antimermaid = 0
default knocking = 0
default hairpin = False
default coinpurse = False
default letter = False
default failescape = 0
default punchwindow = False
default bribeguard = False
default lookedatwindow = False
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

######################################################################
layeredimage thioran:
    at sprite_highlight('Prince Thioran')
    group expressions:
        attribute angry:
            "images/sprites/thioran/expressions/thioran_angry.png"
        attribute blush:
            "images/sprites/thioran/expressions/thioran_blush.png"
        attribute neutral:
            "images/sprites/thioran/expressions/thioran_neutral.png"
        attribute frown:
            "images/sprites/thioran/expressions/thioran_frown.png"
        attribute soft:
            "images/sprites/thioran/expressions/thioran_soft.png"
        attribute sweat:
            "images/sprites/thioran/expressions/thioran_sweat.png"
    zoom 0.28
    ypos 730
    group eyes auto:
        attribute blinking default:
            "images/sprites/thioran/expressions/thioran_blink.png" at blink
######################################################################
layeredimage grandpa:
    at sprite_highlight('Grandfather')
    group expressions:
        attribute happy:
            "images/sprites/grandpa/expressions/grandpa_happy.png"
        attribute surprised:
            "images/sprites/grandpa/expressions/grandpa_surprised.png"
        attribute neutral:
            "images/sprites/grandpa/expressions/grandpa_neutral.png"
    zoom 0.124
    group eyes auto:
        attribute blinking default:
            "images/sprites/grandpa/expressions/grandpa_blink.png" at blink
######################################################################
image june_masked = LayeredImageMask("side june",
    Transform("june_masked_smaller", crop=(100, 100, 225, 263)),
    background="images/sprites/june/ui/border_behind.png",
    mask="images/sprites/june/ui/border_mask.png",
    foreground="images/sprites/june/ui/border_front.png")

image june_masked_smaller = LayeredImageProxy("side june", Transform("side june"))


layeredimage side june:
    group bordbehind: #FOR NEW JUNE SPRITE
        attribute border default:
            "images/sprites/june/ui/border_behind.png"
            fit "contain"
            xsize 320
            pos (157, 130)
            #same as:
            # xpos -120
            # ypos 134
    group body: #FOR NEW JUNE SPRITE
        attribute body default:
            "images/sprites/june/base/side_june_base.png"
            zoom 0.12
            pos (159, 153)
    group expressions:
        attribute neutral:
            "images/sprites/june/expressions/side_june_neutral.png"
            zoom 0.12
            pos (159, 153)
        attribute happy:
            "images/sprites/june/expressions/side_june_happy.png"
            zoom 0.12
            pos (159, 153)
        attribute veryhappy:
            "images/sprites/june/expressions/side_june_veryhappy.png"
            zoom 0.12
            pos (159, 153)
        attribute annoyed:
            "images/sprites/june/expressions/side_june_annoyed.png"
            zoom 0.12
            pos (159, 153)
        attribute shocked:
            "images/sprites/june/expressions/side_june_neutral.png"
            zoom 0.12
            pos (159, 153)
        # attribute huffed:
        #     "side_june_huffed.png"
        # attribute neutral:
        #     "side_june_neutral.png"
        # attribute shocked:
        #     "side_june_shocked.png"
        # xzoom -1
        # xpos -80
        # ypos 20
    group frontborder:
        attribute frontborder default:
            "images/sprites/june/ui/border_front.png"
            fit "contain"
            xsize 320
            pos (157, 130)
            #pos (-110, 153)
            #alpha 0.0
        #zoom 0.17
        #xpos -120
        #    ypos 257
        #    zoom 0.53
    #FOR NEW JUNE SPRITE
    #xzoom -1 #FOR NEW JUNE SPRITE
#    group eyes auto:
        #attribute blinking default:
        #    "images/sprites/june/expressions/side_june_veryhappy.png" at blink
        #    zoom 0.13
        #    xpos 40
        #    ypos 125
######################################################################
layeredimage skylla:
    at sprite_highlight('Skylla')
    group expressions:
        attribute neutral:
            "images/sprites/skylla/expressions/skylla_neutral.png"
        attribute angry:
            "images/sprites/skylla/expressions/skylla_angry.png"
        attribute angryteeth:
            "images/sprites/skylla/expressions/skylla_angryteeth.png"
        attribute flustered:
            "images/sprites/skylla/expressions/skylla_flustered.png"
        attribute happy:
            "images/sprites/skylla/expressions/skylla_happy.png"
        attribute nervous:
            "images/sprites/skylla/expressions/skylla_nervous.png"
        attribute sad:
            "images/sprites/skylla/expressions/skylla_sad.png"
        attribute surprised:
            "images/sprites/skylla/expressions/skylla_surprised.png"
    zoom 0.29
    ypos 780
    group eyes auto:
        attribute blinking default:
            "images/sprites/skylla/expressions/skylla_blink.png" at blink
######################################################################
layeredimage prashadi:
    at sprite_highlight('Prashadi')
    group expressions:
        attribute neutral:
            "images/sprites/prashadi/expressions/prashgrandpa_neutral.png"
            fit "contain"
            xysize (1100,1100)
        attribute angry:
            "images/sprites/prashadi/expressions/prashgrandpa_angry.png"
            fit "contain"
            xysize (1100,1100)
        attribute happy:
            "images/sprites/prashadi/expressions/prashgrandpa_happy.png"
            fit "contain"
            xysize (1100,1100)
        attribute nervous:
            "images/sprites/pr`ashadi/expressions/prashgrandpa_nervous.png"
            fit "contain"
            xysize (1100,1100)
        attribute shocked:
            "images/sprites/prashadi/expressions/prashgrandpa_shocked.png"
            fit "contain"
            xysize (1100,1100)
    group eyes auto:
        attribute blinking default:
            "images/sprites/prashadi/expressions/prashgrandpa_blink.png" at blink
            fit "contain"
            xysize (1100,1100)
    ypos 1190
######################################################################
layeredimage cetus:
    at sprite_highlight('Cetus')
    group expressions:
        attribute neutral:
            "images/sprites/cetus/expressions/cetus_neutral2.png"
            fit "contain"
            ypos 45
            zoom 1.17
    #zoom 0.55
    #ypos 0.07
    #group eyes auto:
        #attribute blinking default:
            #"images/sprites/cetus/expressions/cetus_blink.png" at blink
######################################################################
layeredimage side june fish:
    group expressions:
        attribute neutral:
            "images/sprites/june/base/side_june_fish_neutral.png"
            zoom 0.12
            xpos 138
            ypos 310
######################################################################
layeredimage hunter:
    at sprite_highlight('Hunter')
    group body:
        attribute body default:
            "images/sprites/hunter/base/hunter_base.png"
    group expressions:
        attribute neutral:
            "images/sprites/hunter/expressions/hunter_neutral.png"
        attribute angry:
            "images/sprites/hunter/expressions/hunter_angry.png"
        attribute raisedeyebrow:
            "images/sprites/hunter/expressions/hunter_eyebrowraise.png"
        attribute flustered:
            "images/sprites/hunter/expressions/hunter_flustered.png"
        attribute happy:
            "images/sprites/hunter/expressions/hunter_happy.png"
        attribute nervous:
            "images/sprites/hunter/expressions/hunter_nervous.png"
        attribute sad:
            "images/sprites/hunter/expressions/hunter_sad.png"
        attribute shocked:
            "images/sprites/hunter/expressions/hunter_shocked.png"
        attribute warmsmile:
            "images/sprites/hunter/expressions/hunter_warmsmile.png"
        attribute 2:
            "images/sprites/hunter/expressions/hunter_neutral.png"
    group coverings:
        attribute mask:
            "images/sprites/hunter/accessories/hunter_mask.png"
    group eyes auto:
        attribute blinking default:
            "images/sprites/hunter/expressions/hunter_blink.png" at blink
    zoom 0.15
    ypos 1.17
######################################################################
layeredimage jorunn:
    at sprite_highlight('Jorunn')
    group expressions:
        attribute pissed:
            "images/sprites/jorunn/expressions/jorunn_pissed.png"
        attribute flustered:
            "images/sprites/jorunn/expressions/jorunn_flustered.png"
        attribute neutral:
            "images/sprites/jorunn/expressions/jorunn_neutral.png"
        attribute glee:
            "images/sprites/jorunn/expressions/jorunn_glee.png"
        attribute sweat:
            "images/sprites/jorunn/expressions/jorunn_sweat.png"
    zoom 0.34
    ypos 1080
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

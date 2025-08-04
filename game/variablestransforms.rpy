
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
    xalign 0.5
    zoom 0.7
    pause 1.7
    linear 0.3 alpha 1.0
    pause 0.2
#transform that the logo does on main menu
######################################################################
#Logo Imagebutton
#imagebutton auto ("gui/logo_%s.png") focus_mask True action NullAction()
######################################################################
#Protagonist + Narrator Names
define y = Character("[player_name]", image="june",color="#ffffff", ctc="ctc_pos", ctc_position="fixed")
#color="#ee701f",
define ny = Character(None, what_italic=True, image="june", ctc="ctc_pos", ctc_position="fixed") # for narration
define narrator = Character(None, what_italic=True, ctc="ctc_pos", ctc_position="fixed") #for pure narration no image
######################################################################
#Main Character Names
define h = Character("Hunter", image="june", color="#c6271d", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter")
define s = Character("Skylla", image="june", color="#e9a1d6", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla")
define c = Character("Cetus", image="june", color="#70418b", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Cetus")
define p = Character("Prince Thioran", image="june", color="#4e94c9", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prince Thioran")
define j = Character("Jorunn", image="june", color="#cb8b4f", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Jorunn")
define g = Character("Grandfather", image="june", color="#bcc0a3", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Grandfather")
define Pr = Character("Prashadi", image="june", color="#d3ffff", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prashadi")
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
######################################################################
#Unknown Character Names
define u = Character("???", image="june", ctc="ctc_pos", ctc_position="fixed")
define novisualthio = Character("Angry Voice", image="june", color="#4e94c9", ctc="ctc_pos", ctc_position="fixed")
define novisualjor = Character("Mischievous Voice", image="june", color="#cb8b4f", ctc="ctc_pos", ctc_position="fixed")
define up = Character("Princely Merman", image="june", color="#4e94c9", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prince Thioran")
define uj = Character("Thieving Merman", image="june", color="#cb8b4f", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Jorunn")
define uhunter = Character("Strange Man", image="june", color="#c6271d", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter")
define ucetus = Character("Royal Merman", image="june", color="#70418b", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Cetus")
define siren = Character("Melodious Voice", image="june", color="#e9a1d6", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla")
define gpa = Character("Grandfather?", image="june", color="#bcc0a3", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prashadi")
######################################################################
#Various Variables
default newspaper = False
default childrenplaying = False
default seastorm = False
default promermaid = 0
default antimermaid = 0
default knocking = 0
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
layeredimage prince:
    at sprite_highlight('Prince Thioran')
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
######################################################################
layeredimage grandpa:
    at sprite_highlight('Grandfather')
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
######################################################################
layeredimage side june:
    # group body: #FOR NEW JUNE SPRITE
    #     attribute body default:
    #         "side_june_base.png"
    group expressions:
        # attribute happy: #FOR NEW JUNE SPRITE
        #     "side_june_happy.png"
        attribute flustered:
            "side_june_flustered.png"
        attribute huffed:
            "side_june_huffed.png"
        attribute neutral:
            "side_june_neutral.png"
        attribute shocked:
            "side_june_shocked.png"
        xzoom -1
        xpos -80
        ypos 20
    # zoom 0.3 #FOR NEW JUNE SPRITE
    # xzoom -1 #FOR NEW JUNE SPRITE
    group eyes auto:
        attribute blinking default:
            "side_june_eye_closed.png" at blink
        xzoom -1
        xpos -80
        ypos 20
######################################################################
layeredimage skylla:
    at sprite_highlight('Skylla')
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
######################################################################
layeredimage prashadi:
    at sprite_highlight('Prashadi')
    group expressions:
        attribute neutral:
            "prashgrandpa NUETRAL2.png"
            fit "contain"
            xysize (1100,1100)
        attribute angry:
            "prashgrandpa ANGRY2.png"
            fit "contain"
            xysize (1100,1100)
        attribute happy:
            "prashgrandpa HAPPY2.png"
            fit "contain"
            xysize (1100,1100)
        attribute nervous:
            "prashgrandpa NERVOUS2.png"
            fit "contain"
            xysize (1100,1100)
        attribute shocked:
            "prashgrandpa SHOCKED2.png"
            fit "contain"
            xysize (1100,1100)
    group eyes auto:
        attribute blinking default:
            "prashgrandpa_eye_closed.png" at blink
            fit "contain"
            xysize (1100,1100)
    ypos 1190
######################################################################
layeredimage cetus:
    at sprite_highlight('Cetus')
    group expressions:
        attribute neutral:
            "cetus_neutral.png"
    zoom 0.55
    ypos 0.07
    group eyes auto:
        attribute blinking default:
            "cetus_blink.png" at blink
######################################################################
layeredimage side june fish:
    group expressions:
        attribute neutral:
            "side_june_fish_neutral.png"
            zoom 0.12
            xpos 138
            ypos 310
######################################################################
layeredimage hunter:
    at sprite_highlight('Hunter')
    group body:
        attribute body default:
            "hunter_base.png"
    group expressions:
        attribute neutral:
            "hunter_neutral.png"
        attribute angry:
            "hunter_angry.png"
        attribute raisedeyebrow:
            "hunter_eyebrowraise.png"
        attribute flustered:
            "hunter_flustered.png"
        attribute happy:
            "hunter_happy.png"
        attribute nervous:
            "hunter_nervous.png"
        attribute sad:
            "hunter_sad.png"
        attribute shocked:
            "hunter_shocked.png"
        attribute warmsmile:
            "hunter_warmsmile.png"
        attribute 2:
            "hunter_neutral.png"
    group coverings:
        attribute mask:
            "hunter_mask.png"
    group eyes auto:
        attribute blinking default:
            "hunter_eye_closed.png" at blink
    zoom 0.15
    ypos 1.17
######################################################################
layeredimage jorunn:
    at sprite_highlight('Jorunn')
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
######################################################################
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

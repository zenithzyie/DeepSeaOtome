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
define p = Character("Prince Thioran", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Thioran", namebox_background=Frame("gui/namebox_thio.png", 0, 0))
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
define person = Character("Passerby", image="june", ctc="ctc_pos", ctc_position="fixed")
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
define novisualthio = Character("Angry Voice", image="june", ctc="ctc_pos", ctc_position="fixed", callback = name_callback, cb_name="Thioran", namebox_background=Frame("gui/namebox_thio.png", 0, 0))
define novisualjor = Character("Mischievous Voice", image="june", ctc="ctc_pos", ctc_position="fixed", callback = name_callback, cb_name="Jorunn", namebox_background=Frame("gui/namebox_jor.png", 0, 0))
define up = Character("Princely Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Thioran", namebox_background=Frame("gui/namebox_thio.png", 0, 0))
define uj = Character("Thieving Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Jorunn", namebox_background=Frame("gui/namebox_jor.png", 0, 0))
define uhunter = Character("Strange Man", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter",namebox_background=Frame("gui/namebox_hunter.png", 0, 0))
define novisualhunter = Character("Familiar Voice", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Hunter", namebox_background=Frame("gui/namebox_hunter.png", 0, 0))
define ucetus = Character("Royal Merman", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Cetus",namebox_background=Frame("gui/namebox_cetus.png", 0, 0))
define siren = Character("Melodious Voice", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla", namebox_background=Frame("gui/namebox_skylla.png", 0, 0))
define siren2 = Character("Siren", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Skylla", namebox_background=Frame("gui/namebox_skylla.png", 0, 0))
define gpa = Character("Grandfather?", image="june", ctc="ctc_pos", ctc_position="fixed",callback = name_callback, cb_name="Prashadi", namebox_background=Frame("gui/namebox_grandpa.png", 0, 0))
######################################################################

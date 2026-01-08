################################################################################
##
## Achievements for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.5
##
################################################################################
## This file contains code for an achievement system in Ren'Py. It is designed
## as a wrapper to the built-in achievement system, so it hooks into the
## Steam backend as well if you set up your achievement IDs the same as in
## the Steam backend.
##
## You don't have to register the achievements or anything with the backend,
## or worry about syncing - that's all automatically done for you when the
## achievements are declared and granted.
##
## To get started, declare a few achievements below. Some samples are included.
## You may also replace the `image locked_achievement` image with something
## appropriate - this image is used as the default "Locked" image for all your
## achievements unless you specify something else.
##
## Then you can make a button to go to your achievement gallery screen, e.g.
# textbutton _("Achievements") action ShowMenu("achievement_gallery")
## This will show the achievement gallery screen, declared below. You can
## further customize it however you like.
## If you click on an achievement in the gallery during development (this will
## not happen in a release build), it will toggle the achievement on/off.
## This will also let you see the achievement popup screen, similarly declared
## below. It can be customized however you like.
##
## There's also an example label you can jump to via a line like
## `jump achievement_examples` which has examples of how to grant achievements
## and track progress during gameplay.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## Leave a comment on the tool page on itch.io or an issue on the GitHub
## if you run into any issues.
################################################################################

################################################################################
## CONFIGURATION
################################################################################
## This is a configuration value which determines whether the in-game
## achievement popup should appear when Steam is detected. Since Steam
## already has its own built-in popup, you may want to set this to False
## if you don't want to show the in-game popup alongside it.
## The in-game popup will still work on non-Steam builds, such as builds
## released DRM-free on itch.io.
define myconfig.INGAME_POPUP_WITH_STEAM = True
## The length of time the in-game popup spends hiding itself (see
## transform achievement_popout below).
define myconfig.ACHIEVEMENT_HIDE_TIME = 1.0
## True if the game should show in-game achievement popups when an
## achievement is earned. You can set this to False if you just want an
## achievement gallery screen and don't want any popups.
define myconfig.SHOW_ACHIEVEMENT_POPUPS = True
## This can be set to a sound that plays when the achievement popup appears.
## None does not play a sound.
define myconfig.ACHIEVEMENT_SOUND = None # "audio/sfx/achievement.ogg"
## If the sound plays, this sets the channel it will play on. The audio
## channel plays on the sfx mixer, and can play overlapping sounds if multiple
## achievements are earned at once.
define myconfig.ACHIEVEMENT_CHANNEL = "audio"
## This is the default name and description used for hidden achievements, unless
## you provide a more specific one. See the examples below for how to do so.
define myconfig.HIDDEN_ACHIEVEMENT_NAME = _("???{#hidden_achievement_name}")
define myconfig.HIDDEN_ACHIEVEMENT_DESCRIPTION = _("???{#hidden_achievement_description}")

## A callback, or list of callbacks, which are called when an achievement
## is granted. It is called with one argument, the achievement which
## was granted. It is only called if the achievement has not previously
## been earned. See the README for more information.
define myconfig.ACHIEVEMENT_CALLBACK = [
    ## This first example is an achievement which unlocks after two other
    ## achievements have been granted ("hidden_achievement" and
    ## "hidden_description").
    LinkedAchievement(hidden3=['hidden_achievement', 'hidden_description']),
    ## The second example is an achievement which unlocks after all achievements
    ## have been granted. This is a special case.
    LinkedAchievement(platinum_achievement='all'),
    ## You may remove these examples!
]

## This is a built-in configuration value. It will set the position of
## the Steam popup. You can change this to any of the following:
## "top_left", "top_right", "bottom_left", "bottom_right"
## You may want to use this to ensure any Steam notifications don't conflict
## with the position of the built-in notification, if you're using both.
define achievement.steam_position = None

################################################################################
## DEFINING ACHIEVEMENTS
################################################################################
## Replace this with whatever locked image you want to use as the default
## for a locked achievement.
image locked_achievement = "gui/ach/ach_icon.png"

image blackmask = "gui/ach/blackmask.png"
################################################################################
## Start of example achievement declarations and in-game examples.
## You may remove this code down to the "End of example achievement declarations"
## comment if you don't need it - they are simply examples.
################################################################################
## Example 1 ###################################################################
## This is how you declare achievements. You will use `define` and NOT
## `default`, so you can update the achievements later (you wouldn't want the
## description to be tied to a specific save file, for example).
## The order you declare achievements in is the order they will appear in the
## achievement gallery, by default.
define knockknock = Achievement(
    ## The human-readable name, as it'll appear in the popup and in the gallery.
    name=_("ALRIGHT ALREADY"),
    id="alright-already",
    ## Description.
    description=_("At least you got in, right?"),
    unlocked_image="gui/ach/chibi_june.png",
    locked_image=AlphaMask("blackmask", At("gui/ach/chibi_june.png")),
    hide_name=True,
    hide_description=True,
)
define followprince = Achievement(
    ## The human-readable name, as it'll appear in the popup and in the gallery.
    name=_("The Royal Road"),
    id="follow-prince",
    ## Description.
    description=_("Chose to follow the Striking Prince."),
    unlocked_image="gui/ach/chibi_thio.png",
    locked_image=AlphaMask("blackmask", At("gui/ach/chibi_thio.png")),
    hide_name=False,
    hide_description=False,
)
define perfectescaperoom = Achievement(
    ## The human-readable name, as it'll appear in the popup and in the gallery.
    name=_("Sought A Way Out"),
    id="escaped-room",
    ## Description.
    description=_("Escaped the guest room on your first try."),
    unlocked_image="gui/ach/chibi_cetus.png",
    locked_image=AlphaMask("blackmask", At("gui/ach/chibi_cetus.png")),
    hide_name=False,
    hide_description=True,
)
define followthief = Achievement(
    ## The human-readable name, as it'll appear in the popup and in the gallery.
    name=_("Into The Wild"),
    id="follow-thief",
    ## Description.
    description=_("Chose to follow the Thieving Merman."),
    unlocked_image="gui/ach/chibi_jor.png",
    locked_image=AlphaMask("blackmask", At("gui/ach/chibi_jor.png")),
    hide_name=False,
    hide_description=False,
)
define finished_demo_thio = Achievement(
    ## The human-readable name, as it'll appear in the popup and in the gallery.
    name=_("Part Of Your World"),
    id="finished-demo-thio",
    ## Description.
    description=_("Thank you for playing the demo! (Thioran Side)"),
    unlocked_image="gui/ach/chibi_merjune.png",
    locked_image=AlphaMask("blackmask", At("gui/ach/chibi_merjune.png")),
    hide_name=True,
    hide_description=True,
)
define badend1 = Achievement(
    ## The human-readable name, as it'll appear in the popup and in the gallery.
    name=_("Early Demise"),
    id="early-demise",
    ## Description.
    description=_("Small fish caught in a big storm."),
    unlocked_image="gui/ach/chibi_hunter.png",
    locked_image=AlphaMask("blackmask", At("gui/ach/chibi_hunter.png")),
    hide_name=False,
    hide_description=False,
)
## You can grant an achievement in-game with `$ sample_achievement.grant()`
################################################################################
## SCREENS
################################################################################
## POPUP SCREEN
################################################################################
## A screen which shows a popup for an achievement the first time
## it is obtained. You may modify this however you like.
## The relevant information is:
## a.name = the human-readable name of the achievement
## a.description = the description
## a.unlocked_image = the image of the achievement, now that it's unlocked
## a.timestamp = the time the achievement was unlocked at
screen achievement_popup(a, tag, num):

    zorder 190

    ## Allows multiple achievements to be slightly offset from each other.
    ## This number should be at least as tall as one achievement.
    default achievement_yoffset = num*170

    frame:
        style_prefix 'achieve_popup'
        ymaximum 130
        ## The transform that makes it pop out
        at achievement_popout()
        ## Offsets the achievement down if there are multiple
        yoffset achievement_yoffset
        has hbox
        add a.unlocked_image:
            ## Make sure the image is within a certain size. Useful because
            ## often popups are smaller than the full gallery image.
            ## In this case it will not exceed 95 pixels tall but will retain
            ## its dimensions.
            fit "contain" ysize 95
            xalign 0.5
            ypos -15
        vbox:
            text a.name
            null height 3
            text a.description size 16

    ## Hide the screen after 5 seconds. You can change the time but shouldn't
    ## change the action.
    timer 5.0 action [Hide("achievement_popup"),
            Show('finish_animating_achievement', num=num, _tag=tag+"1")]

style achieve_popup_frame:
    is confirm_frame
    align (0.0, 0.0)
style achieve_popup_hbox:
    spacing 10
style achieve_popup_vbox:
    spacing 2
style achieve_popup_text:
    is text
    size 19


## A transform that pops the achievement out from the left side of
## the screen and bounces it slightly into place, then does the
## reverse when the achievement is hidden.
transform achievement_popout():
    ## The `on show` event occurs when the screen is first shown.
    on show:
        ## Align it off-screen at the left. Note that no y information is
        ## given, as that is handled on the popup screen.
        xpos 0.0 xanchor 1.0
        ## Ease it on-screen
        easein_back 1.0 xpos 0.0 xanchor 0.0
    ## The `on hide, replaced` event occurs when the screen is hidden.
    on hide, replaced:
        ## Ease it off-screen again.
        ## This uses the hide time above so it supports displaying multiple
        ## achievements at once.
        easeout_back myconfig.ACHIEVEMENT_HIDE_TIME xpos 0.0 xanchor 1.0

################################################################################
## ACHIEVEMENT GALLERY SCREEN
################################################################################
## The screen displaying a list of the achievements the player has earned.
## Feel free to update the styling for this however you like; this is just one
## way to display the various information.
screen achievement_gallery():
    tag menu

#    add VBox(Transform("#1d2847", ysize=110), "#131b31") # Background
#    add "images/bgs/bg drowning.jpg" size (1280, 720)
    add gui.main_menu_background:
        fit "contain"
#    add HBox(Transform("#1d2847", xsize=800)):
#        alpha 0.5
    add Solid("#1d2847", xysize = (742,800)):
        alpha 0.5

#    add "gui/game_menu.png":
#        alpha 0.8
#        #xsize 820
#        fit "contain"
#        xpos -425

#    add Solid("#1d2847", xysize = (742,100))

    ############################################################################
    ## Version 1 ###############################################################
    ## If you're using a default template/typical Ren'Py layout, uncomment
    ## the following:
    # use game_menu(_("Achievement Gallery"), scroll='viewport'):
    ############################################################################
    ## Version 2 ###############################################################
    ## Otherwise, if you'd like this to be independent of the game menu,
    ## use the following:
    textbutton _("Return") action [ShowMenu("gallery_B"), Hide("achievement_gallery")]:
        style 'return_button'
    viewport:
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        #xpos 40
        yalign 0.5
        xsize int(config.screen_width*0.6) ysize int(config.screen_height*0.73)
        xfill False yfill False
        has vbox
        #spacing 20

    ############################################################################
        ## This list contains every achievement you declared. You can also
        ## create your own lists to iterate over, if desired. That would be
        ## useful if you wanted to group achievements by category, for example.
        for a in Achievement.all_achievements:
            frame:
                if a.has():
                    #background "#26325e"
                    background "gui/textbox.png"
                    #xsize 700
                    #xfill True
                    ysize 155
                #    padding (15,8)
                else:
                    background "#141c38"
                    #xsize 700
                    xfill True
                    ysize 155
                #    padding (15,8)
                button:
                    style_prefix 'achievement'
                    ## During development, you can click on achievements in the
                    ## gallery and they will toggle on/off.
                    if config.developer:
                        action a.Toggle()
                    else:
                        ## This prevents the button from changing style when not
                        ## in development mode.
                        action NullAction()
                    has hbox
                    if a.idle_img:
                        fixed:
                            align (0.5, 0.5)
                            xysize (155, 155)
                            add a.idle_img fit "scale-down" ysize 145 align (0.5, 0.5)
                    else:
                        null width -10
                    null width -6
                    vbox:
                        null height 10
                        label a.name:
                            xalign 0.0
                        null height 6
                        text a.description:
                            xalign 0.0
                        if a.has():
                            text a.timestamp size 18 color "#8c8c8c"
                        elif a.stat_max and a.show_progress_bar:
                            # Has a bar to show stat progress.
                            fixed:
                                fit_first True
                                bar value a.stat_progress range a.stat_max:
                                    style 'achievement_bar'
                                text "[a.stat_progress]/[a.stat_max]":
                                    style_suffix "progress_text"
        ## So there's a bit of space at the bottom after scrolling all the way.
        null height 100

    ## A header that shows how many achievements you've earned, out of
    ## the total number of achievements in the game. Feel free to remove
    ## or relocate this.
    label __("Achievements: ") + "{earned}/{total}".format(
            earned=Achievement.num_earned(), total=Achievement.num_total()):
        text_size 52 xpos 155 ypos 10 text_color "#fff" top_padding 15

    ## This is an example of a button you might have during development which
    ## will reset all achievement progress at once. It can also be provided
    ## to players if you'd like them to be able to reset their achievement
    ## progress.
    # textbutton "Reset All" action Achievement.Reset() align (1.0, 0.0)

style achievement_button:
    size_group 'achievement'
    xmaximum 750
style achievement_label:
    padding (2, 2)
style achievement_label_text:
    size 40 color "#97c9e6"
style achievement_hbox:
    spacing 10
style achievement_vbox:
    spacing 2
style achievement_bar:
    xmaximum 600

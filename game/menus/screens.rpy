################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## CONTAINS THE FOLLOWING SCREENS:
## Say - Character says what? screen.
## Input - Player types what? screen.
## Choice - Player chooses what? screen.
## Quick Menu - Contains buttons displayed under the textbox.
## Game Menu - Not really sure what this does, but it makes the game work?
################################################################################
## The styles for these are stored in styles.rpy.
################################################################################

################################################################################
## Say screen ##################################################################
################################################################################
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign -0.2 ypos 0.3


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

################################################################################
## Input screen ################################################################
################################################################################
screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

################################################################################
## Choice screen ###############################################################
################################################################################
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

################################################################################
## Quick Menu screen ###########################################################
################################################################################
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.489
            yalign 0.995

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("      ") action None
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('prefs_menu')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

################################################################################
## Game Menu screen ############################################################
################################################################################
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.
################################################################################
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.game_menu_background:
            #alpha 0.9
            fit "contain"
    else:
        add gui.game_menu_background:
            #alpha 0.9
            fit "contain"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title:
        xalign 0.5

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen game_menu_prefs(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.game_menu_background:
            alpha 0.9
            fit "contain"
    else:
        add gui.game_menu_background:
            alpha 0.9
            fit "contain"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            # frame:
            #     style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    #use navigation

## SOMEHOW, FIGURE OUT HOW TO HIDE RETURN BUTTON ON prefs_menu HERE????
    textbutton _("Return"):
        style "return_button"
        if main_menu:
                action ShowMenu("main_menu")
        else:
            if renpy.get_screen("prefs_menu"):
                if renpy.get_screen("main_menu"):
                    action Return()
            else:
                action ShowMenu("prefs_menu")
        #action Return()

    label title:
        xalign 0.5

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

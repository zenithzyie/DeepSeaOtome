################################################################################
## CONTAINS THE FOLLOWING SCREENS AND THEIR STYLES:
## History - Where our text log lives.
## Help - Where keyboard shortcuts are located.
## Confirm - Do you want to exit, yes/no type menus.
## Skip Indicator - The menu that shows when we're skipping stuff.
## Notify - You unlocked a new gallery thing! menu.
################################################################################

################################################################################
## History screen ##############################################################
################################################################################
## Dialogue history stored in _history_list. ###################################
################################################################################
screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu_prefs(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

################################################################################
## Help screen #################################################################
################################################################################
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
    if renpy.get_screen("preferences"):
        if renpy.variant("pc") or renpy.variant("web"):

            default device = "keyboard"

        hbox:
            xpos 540
            ypos 110
            spacing gui.navigation_spacing
            imagebutton:
                auto "gui/button/mainside_%s.png"
                hover_foreground Text("Keyboard", style ="main_menu_imagebutton_text")
                idle_foreground Text("Keyboard", style ="main_menu_imagebutton_text")
                action SetScreenVariable("device", "keyboard")
                at customzoomsmall
            imagebutton:
                auto "gui/button/mainside_%s.png"
                hover_foreground Text("Mouse", style ="main_menu_imagebutton_text")
                idle_foreground Text("Mouse", style ="main_menu_imagebutton_text")
                action SetScreenVariable("device", "mouse")
                at customzoomsmall
            #textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            #textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                imagebutton:
                    auto "gui/button/mainside_%s.png"
                    hover_foreground Text("Gamepad", style ="main_menu_imagebutton_text")
                    idle_foreground Text("Gamepad", style ="main_menu_imagebutton_text")
                    action SetScreenVariable("device", "gamepad")
                    at customzoomsmall
                #textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help

        null width (10 * gui.pref_spacing)

#sub-menus
screen keyboard_help():
    if renpy.get_screen("preferences"):
        vbox:
            xpos 400
            box_wrap True
            xalign 0.5
            yalign 0.5

            if renpy.variant("pc") or renpy.variant("web"):

                hbox:
                    null width 1500

        vbox:
            style_prefix "help"
            box_wrap True
            ypos 160
            xpos 310

            hbox:
                label _("Enter")
                text _("Advances dialogue and activates the interface.")

            hbox:
                label _("Space")
                text _("Advances dialogue without selecting choices.")

            hbox:
                label _("Arrow Keys")
                text _("Navigate the interface.")

            hbox:
                label _("Escape")
                text _("Accesses the game menu.")

            hbox:
                label _("Ctrl")
                text _("Skips dialogue while held down.")

            hbox:
                label _("Tab")
                text _("Toggles dialogue skipping.")

            hbox:
                label _("Page Up")
                text _("Rolls back to earlier dialogue.")

            hbox:
                label _("Page Down")
                text _("Rolls forward to later dialogue.")

            hbox:
                label "H"
                text _("Hides the user interface.")

            hbox:
                label "S"
                text _("Takes a screenshot.")

            hbox:
                label "V"
                text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

            hbox:
                label "Shift+A"
                text _("Opens the accessibility menu.")


screen mouse_help():
    if renpy.get_screen("preferences"):
        vbox:
            xpos 400
            box_wrap True
            xalign 0.5
            yalign 0.5

            if renpy.variant("pc") or renpy.variant("web"):

                hbox:
                    null width 1500

        vbox:
            style_prefix "help"
            box_wrap True
            ypos 160
            xpos 310

            hbox:
                label _("Left Click")
                text _("Advances dialogue and activates the interface.")

            hbox:
                label _("Middle Click")
                text _("Hides the user interface.")

            hbox:
                label _("Right Click")
                text _("Accesses the game menu.")

            hbox:
                label _("Mouse Wheel Up")
                text _("Rolls back to earlier dialogue.")

            hbox:
                label _("Mouse Wheel Down")
                text _("Rolls forward to later dialogue.")


screen gamepad_help():
    if renpy.get_screen("preferences"):
        vbox:
            xpos 400
            box_wrap True
            xalign 0.5
            yalign 0.5

            if renpy.variant("pc") or renpy.variant("web"):

                hbox:
                    null width 1500

        vbox:
            style_prefix "help"
            box_wrap True
            ypos 160
            xpos 310
            hbox:
                label _("Right Trigger\nA/Bottom Button")
                text _("Advances dialogue and activates the interface.")

            hbox:
                label _("Left Trigger\nLeft Shoulder")
                text _("Rolls back to earlier dialogue.")

            hbox:
                label _("Right Shoulder")
                text _("Rolls forward to later dialogue.")

            hbox:
                label _("D-Pad, Sticks")
                text _("Navigate the interface.")

            hbox:
                label _("Start, Guide, B/Right Button")
                text _("Accesses the game menu.")

            hbox:
                label _("Y/Top Button")
                text _("Hides the user interface.")

            vbox:
                xalign 0.5
                textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

################################################################################
## Additional screens
################################################################################

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                ypos 20
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

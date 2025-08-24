################################################################################
#MAIN MENU - title screen, when the game starts
################################################################################

image startbutton_hover = im.Scale("gui/button/start_hover.png", 116, 28)
image startbutton_idle = im.Scale("gui/button/start_idle.png", 116, 28)

image loadbutton_hover = im.Scale("gui/button/load_hover.png", 116, 29)
image loadbutton_idle = im.Scale("gui/button/load_idle.png", 116, 29)

screen titleMainMenu():
    vbox:
        if renpy.get_screen("main_menu"):
            style_prefix "main_menu"
            xalign 0.5
            yalign 0.88

        spacing gui.navigation_spacing

        if main_menu:
            #textbutton _("Start") action Start()
            imagebutton:
                auto "startbutton_%s"
                hover_foreground Text("Start", style ="main_menu_imagebutton_text")
                idle_foreground Text("Start", style ="main_menu_imagebutton_text")
                action Start()

            imagebutton:
                auto "loadbutton_%s"
                hover_foreground Text("Load", style ="main_menu_imagebutton_text")
                idle_foreground Text("Load", style ="main_menu_imagebutton_text")
                action ShowMenu("load")

        textbutton _("Album") action ShowMenu("gallery_B")

        textbutton _("Settings") action [ShowMenu("preferences"), ShowMenu("sub_menu_text")]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background size (1280, 720)
#    imagebutton auto ("gui/logo_%s.png") focus_mask True action NullAction() at logoappear

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


################################################################################
##MAIN MENU STYLES
################################################################################
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style main_menu:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style main_menu_button:
    properties gui.text_properties("navigation_button")
    xalign 0.5

style main_menu_button_text:
    properties gui.text_properties("navigation_button")
    xalign 0.5
    xpos 0.5
    idle_color "#fff"
    hover_color '#66a3e0'
    size 29

style main_menu_imagebutton_text:
    color "#fff"
    xalign 0.5
    yalign 0.49
    size 29

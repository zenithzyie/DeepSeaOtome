################################################################################
#MAIN MENU - title screen, when the game starts
################################################################################

image startbutton_hover = Transform("gui/button/start_hover.png", zoom=0.24)
image startbutton_idle = Transform("gui/button/mm_idle.png", zoom=0.24)

image loadbutton_hover = Transform("gui/button/load_hover.png", zoom=0.24)
image loadbutton_idle = Transform("gui/button/mm_idle.png", zoom=0.24)

image albumbutton_hover = Transform("gui/button/album_hover.png", zoom=0.24)
image albumbutton_idle = Transform("gui/button/mm_idle.png", zoom=0.24)

image settingsbutton_hover = Transform("gui/button/settings_hover.png", zoom=0.24)
image settingsbutton_idle = Transform("gui/button/mm_idle.png", zoom=0.24)

image quitbutton_hover = Transform("gui/button/quit_hover.png", zoom=0.24)
image quitbutton_idle = Transform("gui/button/mm_idle.png", zoom=0.24)

image newsbutton_hover = Transform("gui/button/ticket_hover.png", zoom=0.24)
image newsbutton_idle = Transform("gui/button/ticket_idle.png", zoom=0.24)

screen titleMainMenu():
    vbox:
        if renpy.get_screen("main_menu"):
            style_prefix "main_menu"
            xpos 355
            ypos 550

        spacing 12


        if main_menu:
            imagebutton:
                auto "startbutton_%s"
                hover_foreground Text("Start", style ="main_menu_imagebutton_text1", color ="#66a3e0")
                idle_foreground Text("Start", style ="main_menu_imagebutton_text1")
                action Start()

            imagebutton:
                auto "loadbutton_%s"
                hover_foreground Text("Load", style ="main_menu_imagebutton_text1", color ="#66a3e0")
                idle_foreground Text("Load", style ="main_menu_imagebutton_text1")
                action ShowMenu("load")

            imagebutton:
                auto "albumbutton_%s"
                hover_foreground Text("Album", style ="main_menu_imagebutton_text1", color ="#66a3e0")
                idle_foreground Text("Album", style ="main_menu_imagebutton_text1")
                action ShowMenu("gallery_B")

            imagebutton:
                auto "settingsbutton_%s"
                hover_foreground Text("Achievements", style ="main_menu_imagebutton_text1", color ="#66a3e0")
                idle_foreground Text("Achievements", style ="main_menu_imagebutton_text1")
                action ShowMenu("achievement_gallery")


            imagebutton:
                auto "settingsbutton_%s"
                hover_foreground Text("Settings", style ="main_menu_imagebutton_text1", color ="#66a3e0")
                idle_foreground Text("Settings", style ="main_menu_imagebutton_text1")
                action [ShowMenu("preferences"), ShowMenu("sub_menu_text"), ShowMenu("sub_menu_text"), Hide("sub_menu_audio"), Hide("help"), Hide("credits")]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton:
                auto "quitbutton_%s"
                hover_foreground Text("Quit", style ="main_menu_imagebutton_text1", color ="#66a3e0")
                idle_foreground Text("Quit", style ="main_menu_imagebutton_text1")
                action Quit(confirm=not main_menu)

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background size (1280, 720)
    add "gui/logo_idle.png" at logoappear size (550, 264)

    if main_menu:
        imagebutton:
            auto "gui/button/mainside_%s.png"
            hover_foreground Text("News", style ="main_menu_imagebutton_text")
            idle_foreground Text("News", style ="main_menu_imagebutton_text")
            action OpenURL("https://zenithzyie.itch.io/hearts-depth/devlog")
            xalign 0.105
            yalign 0.95
            at customzoomsmall



#    imagebutton:
#        auto "newsbutton_%s"
#        hover_foreground Text("News", style ="main_menu_imagebutton_text1", color ="#66a3e0")
#        idle_foreground Text("News", style ="main_menu_imagebutton_text1")
#        action [ShowMenu("gameNews")]

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

#            text "[config.name!t]":
#                style "main_menu_title"

            text "Demo Version [config.version]":
                style "main_menu_version"
                size 18


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

style main_menu_imagebutton_text1:
    properties gui.text_properties("navigation_button")
    xalign 0.5
    yalign 0.49
    size 29

style main_menu_imagebutton_text:
    properties gui.text_properties("navigation_button")
    color "#fff"
    xalign 0.5
    yalign 0.49
    idle_color "#66a3e0"
    hover_color '#66a3e0'
    size 29

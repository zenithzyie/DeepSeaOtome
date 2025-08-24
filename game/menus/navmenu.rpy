## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.
## WE DON'T USE THIS ANYMORE!!?!?!??! except for screen navigation()

screen navigation():
    if renpy.get_screen("main_menu"):
        use titleMainMenu
    else:
        pass
#GAME MENU (OLD)
screen gameNavMenu():
    vbox:
        if renpy.get_screen("main_menu"):
            pass
        else:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Gallery") action ShowMenu("gallery_B")

            textbutton _("Preferences") action [ShowMenu("preferences"), ShowMenu("sub_menu_text")]

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

        if not main_menu:

            textbutton _("Main Menu") action MainMenu()

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") action ShowMenu("help")


        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

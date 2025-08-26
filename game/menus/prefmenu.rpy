################################################################################
## Navigate like BG3
################################################################################
screen prefs_menu():
    tag menu

    use game_menu_noreturn(_("Menu"), scroll="viewport"):

        vbox:
            #style_prefix "game_menu"
            #xpos gui.navigation_xpos

            xpos 485

            vbox:
                xalign 0.5
                spacing gui.navigation_spacing

                imagebutton:
                    auto "gui/button/mainside_%s.png"
                    hover_foreground Text("Resume", style ="main_menu_imagebutton_text")
                    idle_foreground Text("Resume", style ="main_menu_imagebutton_text")
                    action Return()
                    at customzoom

                imagebutton:
                    auto "gui/button/mainside_%s.png"
                    hover_foreground Text("History", style ="main_menu_imagebutton_text")
                    idle_foreground Text("History", style ="main_menu_imagebutton_text")
                    action ShowMenu("history")
                    at customzoom

                imagebutton:
                    auto "gui/button/mainside_%s.png"
                    hover_foreground Text("Save", style ="main_menu_imagebutton_text")
                    idle_foreground Text("Save", style ="main_menu_imagebutton_text")
                    action ShowMenu("save")
                    at customzoom

                imagebutton:
                    auto "gui/button/mainside_%s.png"
                    hover_foreground Text("Load", style ="main_menu_imagebutton_text")
                    idle_foreground Text("Load", style ="main_menu_imagebutton_text")
                    action ShowMenu("load")
                    at customzoom

                imagebutton:
                    auto "gui/button/mainside_%s.png"
                    hover_foreground Text("Settings", style ="main_menu_imagebutton_text")
                    idle_foreground Text("Settings", style ="main_menu_imagebutton_text")
                    action [ShowMenu("preferences"),ShowMenu("sub_menu_text"), Hide("sub_menu_audio"), Hide("help"), Hide("credits")]
                    at customzoom

                if _in_replay:
                    imagebutton:
                        auto "gui/button/mainside_%s.png"
                        hover_foreground Text("End Replay", style ="main_menu_imagebutton_text")
                        idle_foreground Text("End Replay", style ="main_menu_imagebutton_text")
                        action EndReplay(confirm=True)
                        at customzoom

                if not main_menu:
                    imagebutton:
                        auto "gui/button/mainside_%s.png"
                        hover_foreground Text("Main Menu", style ="main_menu_imagebutton_text")
                        idle_foreground Text("Main Menu", style ="main_menu_imagebutton_text")
                        action MainMenu()
                        at customzoom

                if renpy.variant("pc"):

                    ## The quit button is banned on iOS and unnecessary on Android and
                    ## Web.
                    imagebutton:
                        auto "gui/button/mainside_%s.png"
                        hover_foreground Text("Quit", style ="main_menu_imagebutton_text")
                        idle_foreground Text("Quit", style ="main_menu_imagebutton_text")
                        action Quit(confirm=not main_menu)
                        at customzoom

################################################################################
## Preferences Screen ##########################################################
################################################################################
style pref_styling_label_text:
    idle_color "#fff"
    color "#fff"
    size 26
    #font "fonts/NEWBOROU.ttf"

style pref_styling_label:
    ypadding 10

style pref_styling_button_text:
    idle_color "#969696"
    hover_color "#fff"
    selected_color "#66a3e0"
    size 18

style pref_styling_button:
    ypadding 10

screen preferences():
    tag menu

    use game_menu_prefs(_("Settings"), scroll="viewport"):
        
        hbox:
            xpos 50
            ypos 30
            vbox:
                vbox:
                    spacing gui.navigation_spacing
                    imagebutton:
                        auto "gui/button/mainside_%s.png"
                        hover_foreground Text("System", style ="main_menu_imagebutton_text")
                        idle_foreground Text("System", style ="main_menu_imagebutton_text")
                        action [ShowMenu("sub_menu_text"), Hide("sub_menu_audio"), Hide("help"), Hide("credits")]
                        at customzoom
                    imagebutton:
                        auto "gui/button/mainside_%s.png"
                        hover_foreground Text("Audio", style ="main_menu_imagebutton_text")
                        idle_foreground Text("Audio", style ="main_menu_imagebutton_text")
                        action [ShowMenu("sub_menu_audio"), Hide("sub_menu_text"), Hide("help"), Hide("credits")]
                        at customzoom
                    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                        ## Help isn't necessary or relevant to mobile devices.
                        imagebutton:
                            auto "gui/button/mainside_%s.png"
                            hover_foreground Text("Help", style ="main_menu_imagebutton_text")
                            idle_foreground Text("Help", style ="main_menu_imagebutton_text")
                            action [ShowMenu("help"), Hide("sub_menu_text"), Hide("sub_menu_audio"), Hide("credits")]
                            at customzoom
                        #textbutton _("Help") action ShowMenu("help")
                    imagebutton:
                        auto "gui/button/mainside_%s.png"
                        hover_foreground Text("Credits", style ="main_menu_imagebutton_text")
                        idle_foreground Text("Credits", style ="main_menu_imagebutton_text")
                        action [ShowMenu("credits"), Hide("sub_menu_text"), Hide("sub_menu_audio"), Hide("help")]
                        at customzoom


transform customzoom:
        zoom 0.8

transform customzoomsmall:
        zoom 0.6

screen sub_menu_text():
    if renpy.get_screen("preferences"):
        vbox:
            xpos 400
            box_wrap True
            yalign 0.5

            if renpy.variant("pc") or renpy.variant("web"):

                hbox:
                    null width 1500

                vbox:
                    #style_prefix "radio"
                    style_prefix "pref_styling"
                    label _("Display")
                    hbox:
                        #textbutton _("Window") action Preference("display", "window")
                        imagebutton:
                            auto "gui/button/blue_%s.png"
                            hover_foreground Text("Window", style ="main_menu_imagebutton_text")
                            idle_foreground Text("Window", style ="main_menu_imagebutton_text")
                            action Preference("display", "window")
                            at customzoomsmall
                        #textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        imagebutton:
                            auto "gui/button/blue_%s.png"
                            hover_foreground Text("Fullscreen", style ="main_menu_imagebutton_text")
                            idle_foreground Text("Fullscreen", style ="main_menu_imagebutton_text")
                            action Preference("display", "fullscreen")
                            at customzoomsmall

                null height (2 * gui.pref_spacing)

                vbox:
                    #style_prefix "check"
                    style_prefix "pref_styling"
                    label _("Skip")
                    hbox:
                        imagebutton:
                            auto "gui/button/blue_%s.png"
                            hover_foreground Text("Unseen Text", style ="main_menu_imagebutton_text")
                            idle_foreground Text("Unseen Text", style ="main_menu_imagebutton_text")
                            action Preference("skip", "toggle")
                            at customzoomsmall
                        imagebutton:
                            auto "gui/button/blue_%s.png"
                            hover_foreground Text("After Choices", style ="main_menu_imagebutton_text")
                            idle_foreground Text("After Choices", style ="main_menu_imagebutton_text")
                            action Preference("after choices", "toggle")
                            at customzoomsmall
                        imagebutton:
                            auto "gui/button/blue_%s.png"
                            hover_foreground Text("Transitions", style ="main_menu_imagebutton_text")
                            idle_foreground Text("Transitions", style ="main_menu_imagebutton_text")
                            action InvertSelected(Preference("transitions", "toggle"))
                            at customzoomsmall
                        #textbutton _("Unseen Text") action Preference("skip", "toggle")
                        #textbutton _("After Choices") action Preference("after choices", "toggle")
                        #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                        null height (2 * gui.pref_spacing)
                #vbox:
                    #style_prefix "check"
                    #label _("Graphic Imagery")
                    #textbutton _("On") action ToggleVariable("show_gross", true_value=True)
                    #textbutton _("Off") action ToggleVariable("show_gross", true_value=False)
                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                    ## added here, to add additional creator-defined preferences.

                vbox:
                    style_prefix "slider"
                    box_wrap True

                    vbox:
                        style_prefix "pref_styling"
                        label _("Text")

                        hbox:
                            #style_prefix "radio"
                            style_prefix "pref_styling"
                            imagebutton:
                                auto "gui/button/blue_%s.png"
                                hover_foreground Text("Speech Pauses", style ="main_menu_imagebutton_text")
                                idle_foreground Text("Speech Pauses", style ="main_menu_imagebutton_text")
                                action ToggleField(persistent,"speech_pauses")
                                at customzoomsmall

                            #WHY IS THIS BEING DUMB???????
                            showif persistent.speech_pauses:
                                label _("{size=14}Dialogue will pause naturally at commas and periods.{/size}"):
                                    yalign 0.5
                                #vbox:
                                    #style_prefix "slider"
                                    #label _("Commas")
                                    #bar value FieldValue(persistent, "speech_pause_comma", step=.05, style=u'slider', min=0.05, max=1.0)
                                    #label _("Sentences")
                                    #bar value FieldValue(persistent, "speech_pause_period", step=.05, style=u'slider', min=0.1, max=2.0)


                    null height (2 * gui.pref_spacing)

                    vbox:
                        style_prefix "bar"
                        label _("Text Speed")
                        null height (1.5 * gui.pref_spacing)
                        bar value Preference("text speed")

                        null height (1.5 * gui.pref_spacing)

                        label _("Auto-Forward Time")
                        bar value Preference("auto-forward time")
    else:
        pass

screen sub_menu_audio():
    if renpy.get_screen("preferences"):
        vbox:
            xpos 400
            box_wrap True
            null height 100


            if config.has_music:
                style_prefix "pref_styling"
                label _("Audio")
                vbox:
                    style_prefix "slider"
                    label _("Music Volume")

                    bar value Preference("music volume")
                        #xsize 500

            if config.has_sound:

                label _("Sound Volume")
                vbox:
                    style_prefix "slider"
                    bar value Preference("sound volume")
                        #xsize 500

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)

            if config.has_voice:
                label _("Voice Volume")

                hbox:
                    bar value Preference("voice volume")

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                style_prefix "pref_styling"
                null height gui.pref_spacing

                imagebutton:
                    auto "gui/button/menu_%s_background.png"
                    hover_foreground Text("Mute All", style ="main_menu_imagebutton_text")
                    idle_foreground Text("Mute All", style ="main_menu_imagebutton_text")
                    action Preference("all mute", "toggle")
                    at customzoom
                    #style "mute_all_button"
    else:
            pass

################################################################################
## PREF MENU STYLES ############################################################
################################################################################
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 450

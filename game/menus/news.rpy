screen gameNews():

    imagebutton:
        auto "newsbutton_%s"
        hover_foreground Text("News", style ="main_menu_imagebutton_text1", color ="#66a3e0")
        idle_foreground Text("News", style ="main_menu_imagebutton_text1")
        activate_sound "audio/sfx_choiceClick.ogg"
        hover_sound None
        action [Hide("gameNews")]

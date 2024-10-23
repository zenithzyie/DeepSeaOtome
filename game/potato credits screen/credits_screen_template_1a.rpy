## 1a: The basic layout template with big credits blocks on each row.
# Each person is supposed to be credited once per row.
# I used 250x250 avatars, but it can be of any size.
# the site icons are 32x32

# Modified About Screen
screen template_1a():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("1a: One column, one list"), scroll="viewport"):

        style_prefix "about"

        # vbox for credits
        vbox:
            text "Credits:" style "about_header" 

            # spacing between each element
            spacing 50

            # Credit block
            hbox:
                add "logo" # zoom 0.5 -> if images are not resized properly you can do it with zoom

                null width 50 # manual horizontal spacing

                vbox:
                    null height 10 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Gaming Variety Potato" style "credits_name"
                    null height 10  # manual vertical spacing
                    text "Art, Story & Programming" style "credits_role"
                    null height 30
                    hbox:
                        add "itch-io"
                        textbutton _("https://gaming-variety-potato.itch.io/") action OpenURL("https://gaming-variety-potato.itch.io/") style "credits_url_button" text_style "credits_url_text"
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text" 

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Name 2" style "credits_name"
                    null height 10
                    text "(Placeholder)" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text" 

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Name 3" style "credits_name"
                    null height 10
                    text "(Placeholder)" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            ## Unrelated to the credit template
            text "Asset Attribution:" style "about_header"

            hbox:
                add "itch-io"
                text "itch.io icon edited from {a=https://iconduck.com/icons/55051/itch-io}Line Awesome{/a}" yalign 1.0

            text "Line Awesome is an Icon Set of 1,544 icons. Each icon is solid, which is useful for changing icon colors. It's been open sourced with the license: Good Boy License. All icons can be used for personal & commercial purposes."

            hbox:
                add "twitter-original"
                text "twitter icon edited from {a=https://iconduck.com/icons/13242/twitter-original}Devicons Set V2{/a}" yalign 1.0

            text "Devicons Set V2 is an Icon Set of 427 icons. It is exclusively made up of color icons. It's been open sourced with the license: MIT License. All icons can be used for personal & commercial purposes."    

            ## Default content that came with Ren'Py's About screen
            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


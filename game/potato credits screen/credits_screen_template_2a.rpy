## 2a: The layout template with two columns for smaller credit blocks
# I used zoom 0.6 on the original image size, so here they're 150x150. But this is because I didn't want to add another image asset.

# Credits Screen
screen template_2a():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        #text "Credits:" style "about_header"
        #null height 50 # manual vertical spacing

        # syntax: grid <amount_columns> <amount_rows>
        # You need to calculate this manually to fill in these <amount_columns> and <amount_rows> values.
        # Unused slots need to be filled with null (see the end of the code, because we got 7 elements while there is space for 8 (=2*4)).
        # vpgrid is also an option over grid depending on preference.
        # NOTE As fas as I know, you can't give fixed coordinates to grid slots, positions are calculated for slots in relation to each other.
        # Such as having long text strings in first column will push the second column more to the right. Play around with xspacing value for the look you want.
        grid 2 7:
            # horizontal spacing
            xspacing 50
            # vertical spacing
            yspacing 50

            # Credit block: ZENITH
            hbox:
                add "logos/logo.png" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Zenith Zyie" style "credits_name_small"
                    null height 10  # manual vertical spacing
                    text "Director, Writing & Coding" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "itch-io"
                        textbutton _("itch.io") action OpenURL("https://zenithzyie.itch.io/") style "credits_url_button" text_style "credits_url_text_small"
                    hbox:
                        #add "twitter-original"
                        textbutton _("Website") action OpenURL("https://zenithzyie.carrd.co/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block
            ## Default content that came with Ren'Py's About screen
            hbox:
                add "gui/window_icon.png" zoom 0.59
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    label "[config.name!t]" style "credits_name_small"
                    null height 10
                    text _("Version [config.version!t]") style "credits_role_small"
                    null height 10
                    hbox:
                        textbutton _("itch.io") action OpenURL("https://zenithzyie.itch.io/hearts-depth") style "credits_url_button" text_style "credits_url_text_small"
                    hbox:
                        textbutton _("Made with Ren'Py") action OpenURL("https://www.renpy.org/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: EM
            hbox:
                add "logos/em logo.png" zoom 0.59
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Em" style "credits_name_small"
                    null height 10  # manual vertical spacing
                    text "Lead Character Art, Writing & Production" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("Instagram") action OpenURL("https://www.instagram.com/e.ggily") style "credits_url_button" text_style "credits_url_text_small"
            # Credit block: ALI
            hbox:
                add "gui/window_icon.png" zoom 0.59
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Alibun" style "credits_name_small"
                    null height 10
                    text "Co-Director, Character Art & Writing" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("itch.io") action OpenURL("https://www.artstation.com/alibunn") style "credits_url_button" text_style "credits_url_text_small"
                    hbox:
                        #add "twitter-original"
                        textbutton _("Artstation") action OpenURL("https://www.artstation.com/alibunn") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: SOJIN
            hbox:
                add "logos/duck logo.png" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Sojin" style "credits_name_small"
                    null height 10
                    text "Environment Art & Character Art" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("Website") action OpenURL("https://sojinkim.myportfolio.com/") style "credits_url_button" text_style "credits_url_text_small"


            # Credit block: ALYSSA
            hbox:
                add "gui/window_icon.png" zoom 0.59
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Alyssa" style "credits_name_small"
                    null height 10
                    text "Writing" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("itch.io") action OpenURL("https://araetzel.itch.io/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: YUJA
            hbox:
                add "gui/window_icon.png" zoom 0.59
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Yuja" style "credits_name_small"
                    null height 10
                    text "Environment Art & UI Design" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("Website") action OpenURL("https://tokipado.com/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: MANGO
            hbox:
                add "logos/mango logo.png" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Mango" style "credits_name_small"
                    null height 10
                    text "Environment Art" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("itch.io") action OpenURL("https://mango-lord.itch.io/") style "credits_url_button" text_style "credits_url_text_small"
                    hbox:
                        #add "twitter-original"
                        textbutton _("Twitter/X") action OpenURL("https://x.com/islandofmangos") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: LAURA
            hbox:
                add "gui/window_icon.png" zoom 0.59
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Laura" style "credits_name_small"
                    null height 10  # manual vertical spacing
                    text "Environment Art" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("Twitter/X") action OpenURL("https://x.com/waweii") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: LU
            hbox:
                add "logos/lu logo.png" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Lu" style "credits_name_small"
                    null height 10
                    text "Coding" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("itch.io") action OpenURL("https://itch.io/profile/flrmstr") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: LEMNISCATE
            hbox:
                add "logos/lem logo.png" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Lemniscate" style "credits_name_small"
                    null height 10
                    text "Editing" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("itch.io") action OpenURL("https://lemniscreate.itch.io/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block: JUSTIN
            hbox:
                add "logos/justin logo.png" zoom 0.59
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Justin" style "credits_name_small"
                    null height 10
                    text "Voice Acting & Editing" style "credits_role_small"
                    null height 10
                    hbox:
                        #add "twitter-original"
                        textbutton _("itch.io") action OpenURL("https://itch.io/profile/vylphix") style "credits_url_button" text_style "credits_url_text_small"

            # fill unused grid spot (when amount is uneven) with null
            null

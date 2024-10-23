## 2a: The layout template with two columns for smaller credit blocks
# I used zoom 0.6 on the original image size, so here they're 150x150. But this is because I didn't want to add another image asset.

# Credits Screen 
screen template_2a():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("2a: Two columns"), scroll="viewport"):

        style_prefix "about"

        text "Credits:" style "about_header" 
        null height 50 # manual vertical spacing

        # syntax: grid <amount_columns> <amount_rows>
        # You need to calculate this manually to fill in these <amount_columns> and <amount_rows> values.
        # Unused slots need to be filled with null (see the end of the code, because we got 7 elements while there is space for 8 (=2*4)).
        # vpgrid is also an option over grid depending on preference.
        # NOTE As fas as I know, you can't give fixed coordinates to grid slots, positions are calculated for slots in relation to each other.
        # Such as having long text strings in first column will push the second column more to the right. Play around with xspacing value for the look you want.
        grid 2 4:            
            # horizontal spacing
            xspacing 100
            # vertical spacing
            yspacing 100

            # Credit block
            hbox:
                add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Gaming Variety Potato" style "credits_name_small"
                    null height 10  # manual vertical spacing
                    text "Art, Story & Programming" style "credits_role_small"
                    null height 10
                    hbox:
                        add "itch-io"
                        textbutton _("https://gaming-variety-potato.itch.io/") action OpenURL("https://gaming-variety-potato.itch.io/") style "credits_url_button" text_style "credits_url_text_small"
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text_small"                    

            # Credit block
            hbox:
                add "logo" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Name 2" style "credits_name_small"
                    null height 10
                    text "(Placeholder)" style "credits_role_small"
                    null height 10
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block
            hbox:
                add "logo" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Name 3" style "credits_name_small"
                    null height 10
                    text "(Placeholder)" style "credits_role_small"
                    null height 10
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block
            hbox:
                add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Name 4" style "credits_name_small"
                    null height 10  # manual vertical spacing
                    text "(Placeholder)" style "credits_role_small"
                    null height 10
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text_small"                          

            # Credit block
            hbox:
                add "logo" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Name 5" style "credits_name_small"
                    null height 10
                    text "(Placeholder)" style "credits_role_small"
                    null height 10
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text_small"

            # Credit block
            hbox:
                add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Name 6" style "credits_name_small"
                    null height 10  # manual vertical spacing
                    text "(Placeholder)" style "credits_role_small"
                    null height 10
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text_small"                          

            # Credit block
            hbox:
                add "logo" zoom 0.6
                null width 25 # manual horizontal spacing
                vbox:
                    null height 5
                    text "Name 7" style "credits_name_small"
                    null height 10
                    text "(Placeholder)" style "credits_role_small"
                    null height 10
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text_small"

            # fill unused grid spot (when amount is uneven) with null
            null

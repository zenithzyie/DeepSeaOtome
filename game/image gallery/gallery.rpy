style prevNext:
    idle_color '#888888'
    hover_color '#66a3e0'
    font "fonts/Philosopher-Regular.ttf"

screen gallery_B():

    tag menu
    $ start = gallery_page * maxperpage
    $ end = len(gallery_items) - 1
    use game_menu("Album"):
        style_prefix "about"

        #grid for images
        hbox:
            box_wrap True
            ypos 10
            xpos -225
            xsize 1150
            ysize 450

            vpgrid:
                cols maxnumy
                yfill True
                xspacing 35
                yspacing 40
                draggable True
                mousewheel True
                scrollbars "vertical"

                #TEXT KEEPS CUTTING OFF ??? i'm going insane.
                for i in range(start, end + 1):
                    $gallery_items[i].refresh_lock()
                    if gallery_items[i].is_locked:
                        #this one is for locked imaged
                        vbox:
                            hbox:
                                #will show "Unlock" + Name of the CG
                                text "Unlock: " + gallery_items[i].name:
                                    style_prefix "name"
                                    xalign 0.5
                            hbox:
                                imagebutton:
                                    idle_foreground "idleLG"
                                    idle gallery_items[i].locked 
                                    hover_foreground "hoverimgLG"
                                    action NullAction()
                                    at imageThumb
                            
                    else:
                        #this one is for unlocked images
                        vbox:
                            hbox:
                                #show name of CG
                                text gallery_items[i].name:
                                    style_prefix "name"
                                    xalign 0.5
                            hbox:
                                imagebutton:
                                    idle_foreground "idleLG"
                                    idle "thumb_" + gallery_items[i].thumbname
                                    hover_foreground "hoverimgLG" 
                                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                                    at imageThumb
                            
                                
                                      

                #required to fill in empty grid items
                for i in range(end - start + 1, maxperpage):
                    null

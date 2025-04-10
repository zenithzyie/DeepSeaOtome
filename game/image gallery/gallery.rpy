style prevNext:
    idle_color '#888888'
    hover_color '#66a3e0'
    font "fonts/Philosopher-Regular.ttf"

screen gallery_A():

    tag menu

    add "gray"

    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)

    #grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
                    at imageThumb
            else:
                imagebutton: 
                    idle gallery_items[i].images
                    style "gallery_button" #delete this line to remove hover
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5
                    at imageThumb

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #grid for info
    grid maxnumx maxnumy:
        pos (gx2, gy2)
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                style_prefix "name"
                spacing maxthumbx - 20
                text gallery_items[i].name
                xysize(sx, sy)
        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #previous, next, and return buttons
    if gallery_page > 0:
        textbutton "{color=#888888}Previous{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.98
            #background "#fff8"
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "{color=#888888}Next{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98
            #background "#fff8"
    textbutton "{color=#888888}Return{/color}":
        action Return() 
        xalign 0.5
        yalign 0.98
        #background "#fff8"

screen gallery_B():

    tag menu
    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)
    use game_menu(_("Gallery"), scroll="viewport"):
        style_prefix "about"

    #grid for images
    grid maxnumx maxnumy:
        pos (gx1, gy1)
        yfill True
        xspacing 25
        yspacing - 160

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
                    at imageThumb
            else:
                imagebutton: 
                    idle gallery_items[i].images
                    hover_foreground gallery_items[i].hoverimg
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5
                    at imageThumb

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #grid for info
    grid maxnumx maxnumy:
        pos (gx2, gy2)
        yfill True
        xspacing 25
        yspacing - 160

        for i in range(start, end + 1):
            hbox:
                style_prefix "name"
                spacing maxthumbx - 20
                xalign 0.0
                yalign 0.1
                text gallery_items[i].name
                xysize(sx, sy)

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #previous and next buttons
    if gallery_page > 0:
        textbutton "Previous" style "prevNext":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.3
            yalign 0.98
            text_style "prevNext"
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "Next" style "prevNext":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98
            text_style "prevNext"
            
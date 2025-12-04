#here are the styles and transforms used in both the replay and gallery screens


# 1280x720 gallery B
define sx = 250
define sy = 181

# 1920x1080 gallery B
#define sx = 450
#define sy = 253

#pos positions pixel close enough!
default gx1 = 120 #1280x720
default gy1 = 50 #1280x720
#default gx1 = 460 #1920x1080
#default gy1 = 30 #1920x1080

style name_text: #text color and outlines please change
    color "#1A2845" #the actual colour
    size 20 # 1280x720
    #size 30 #1920x1080
    font gui.name_text_font

transform imageThumb: #images to thumbnail re-sizer
    size (sx, sy) #for 1920x1080 and 1280x720 DO NOT CHANGE

transform imageMaxSize:
    size (1280, 720) #to resize the big ones

transform cg_fit:
    #this makes sure that images aren't all stretchy, better imageMaxSize
    fit "contain"
    xalign 0.5

transform zoomtest:
    zoom 0.5

transform zoomtest2:
    zoom 1.0

default zoomnum = 1.0
default zoom_max = 2.0
define zoom_min = 1.0

default zoom_current = 1.0

default x_bar = ui.adjustment()
default y_bar = ui.adjustment()

transform cg_zoomable:
    #this makes sure that images aren't all stretchy, better imageMaxSize
    fit "contain"
    #linear zoom_current zoom zoomnum 
    zoom zoomnum 

#the locked image for the galleries
image locked = "images/gallery/thumb_locked.png"


screen gallery_closeup(images): #shows full sized image as a button on top of everything!
    zorder 10
    imagebutton:
        idle ("gui/game_menu.png")
        action Hide("gallery_closeup", dissolve)
        at cg_fit
    viewport id "vp":
            mousewheel True
            draggable True
            xadjustment x_bar
            yadjustment y_bar
            scrollbars  None
            hbox:
                imagebutton:
                    idle images.images
                    action (Hide("gallery_closeup", dissolve))
                    at cg_zoomable

    key "mousedown_4" action (Function(zoom_in), Hide("gallery_closeup", dissolve), Show("gallery_closeup", zoomin, images))
    key "mousedown_5" action (Function(zoom_out), Hide("gallery_closeup", dissolve), Show("gallery_closeup", zoomout, images))

init python:
    maxnumx = 4
    maxnumy = 4
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    global zoomnum
    global zoom_current

    def zoom_in(): 
        if (store.zoomnum < store.zoom_max):
            store.zoom_current = store.zoomnum
            store.zoomnum += 0.1
        elif(store.zoomnum >= store.zoom_max):
            store.zoom_current = store.zoom_max
        

    def zoom_out():
        if (store.zoomnum > zoom_min):
            store.zoom_current = store.zoomnum
            store.zoomnum -= 0.1
        elif(store.zoomnum <= store.zoom_max):
            store.zoom_current = zoom_min

    def reset_zoom():
        global zoomnum
        zoomnum = 1.0

    def set_zoom(sz):
        global zoom_max

        if sz == "wide":
            zoom_max= 2.0
        elif sz == "tall":     
            zoom_max = 4.0
        else :
            zoom_max = 2.0
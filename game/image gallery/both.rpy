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

#the locked image for the galleries
image locked = "images/gallery/thumb_locked.png"

screen gallery_closeup(images): #shows full sized image as a button on top of everything!
    zorder 10
    imagebutton:
        idle images
        action Hide("gallery_closeup", dissolve)
        at cg_fit
        #at imageMaxSize
        #maximum (1280, 720)
        xalign 0.5
        yalign 0.0

init python:
    maxnumx = 4
    maxnumy = 4
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0

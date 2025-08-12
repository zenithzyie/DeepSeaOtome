#here are the styles and transforms used in both the replay and gallery screens

# 1280x720 gallery A
#define sx = 384
#define sy = 216

# 1280x720 gallery B
define sx = 275
define sy = 155

# 1920x1080 gallery A
#define sx = 600
#define sy = 338

# 1920x1080 gallery B
#define sx = 450
#define sy = 253

#pos positions pixel close enough!
default gx1 = 320 #1280x720
default gy1 = 40 #1280x720
#default gx1 = 460 #1920x1080
#default gy1 = 30 #1920x1080

#text
#default gx2 = 25 # gallery_A 1280x720 and 1920x1080
#default gy2 = 10 # gallery_A

default gx2 = 320 # 322 #1280x720 gallery_B
default gy2 = 90 #75  #1280x720 gallery_B

#default gx2 = 460 #1920x1080 gallery_B
#default gy2 = 83 #1920x1080 gallery_B

#style gallery_button: # hover overlay it must be 4 pixels bigger then the images
    #hover_foreground "images/gallery/hover 1284x724.png"
    #hover_foreground "images/gallery/hover 1924x1084.png"

style name_text: #text color and outlines please change
    color "#ffffff"
    #outlines [ (1, "#e9ec09", 0, 0) ]
    size 20 # 1280x720
    #size 30 #1920x1080

transform imageThumb: #images to thumbnail re-sizer
    size (sx, sy) #for 1920x1080 and 1280x720 DO NOT CHANGE

transform imageMaxSize:
    size (1280, 720) #to resize the big ones

#the locked image for the galleries
image locked = "images/gallery/locked.jpg"

screen gallery_closeup(images): #shows full sized image as a button on top of everything!
    zorder 10
    imagebutton:
        idle images
        action Hide("gallery_closeup", dissolve)
        at imageMaxSize
        #maximum (1280, 720)
        xalign 0.5
        yalign 0.98
        background "#fff8"

init python:
    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0

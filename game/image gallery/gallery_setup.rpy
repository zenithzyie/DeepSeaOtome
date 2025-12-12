################################################################################
## Gallery Setup ############################################################
################################################################################
## Setup for list that holds all gallery images.
## Images must be added here first to show up in gallery.rpy.
##
## Also includes references to background images.
################################################################################
init python:

    class GalleryItem:
        def __init__(self, name, images, thumbname, sizing, locked="locked"):
            self.name = name #title of the CG, shown in text
            self.images = images #the image of the CG itself
            self.thumbname = thumbname #the name of the thumbnail after thumb_
            self.sizing = sizing #how big the cg is; "wide" or "tall",
            self.locked = locked
            self.refresh_lock()

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme


    #ALL GALLERY IMAGES HERE
    #Title, cg image (matches gallery images below), thumbnail name, size of cg "wide/tall"
    gallery_items = []
    gallery_items.append(GalleryItem("Train to Aquantis", ["cg_train"], "cg_train", "wide"))
    gallery_items.append(GalleryItem("The Deep Market", ["cg_sushi"] ,"cg_sushi", "wide"))
    gallery_items.append(GalleryItem("Family Portrait", ["cg_familyportrait"], "cg_familyportrait", "wide" ))
    gallery_items.append(GalleryItem("The Curse", ["cg_skyllahands"],"cg_skyllahands" , "wide"))
    gallery_items.append(GalleryItem("The Mermaid", ["cg_mermaidcetus"], "cg_mermaidcetus", "tall" ))
    gallery_items.append(GalleryItem("Transformation", ["cg_mermaidprashadi"], "cg_mermaidprashadi", "tall" ))
    gallery_items.append(GalleryItem("Suspicion", ["cg_thiokabedon"],"cg_thiokabedon", "wide" ))
    gallery_items.append(GalleryItem("The Negotiation", ["cg notyet"], "cg notyet", "wide"))

#gallery idle border?
image idleLG = ("images/gallery/idleLG.png")

#gallery hover images
image hoverimgLG = ("images/gallery/hoverLG.png")

#gallery images
image cg_train = ("images/gallery/cg/cg_train.jpg")
image cg_familyportrait = ("images/gallery/cg/cg_familyportrait.png")
image cg_sushi = ("images/gallery/cg/cg_sushi.jpg")
image cg_skyllahands = ("images/gallery/cg/cg_skyllahands.jpg")
image cg_mermaid_cetus = ("images/gallery/cg/cg_mermaidcetus.jpg")
image cg_mermaid_prashadi = ("images/gallery/cg/cg_mermaidprashadi.jpg")
image cg_thiokabedon = ("images/gallery/cg/cg_thiokabedon.jpg")
image cg notyet = ("images/gallery/cg/cg_skyllahands.png")

#background images
image bg black = ("images/bgs/bg black.jpg")
image bg brickwall = ("images/bgs/bg brickwall.PNG")
image bg calmwave = ("images/bgs/bg calmwave.jpg")
image bg capitalcity = ("images/bgs/bg capitalcity.jpg")
image bg cetus study = ("images/bgs/bg cetus study.jpg")
image bg choppywave = ("images/bgs/bg choppywave.png")
image bg drowning = ("images/bgs/bg drowning.jpg")
image bg gpa = ("images/bgs/bg gpa.jpg")
image bg nice town = ("images/bgs/bg nice town.jpg")
image bg palace guestroom = ("images/bgs/bg palace guestroom.jpg")
image bg palace hallway = ("images/bgs/bg palace hallway.jpg")
image bg port = ("images/bgs/bg port.jpg")
image bg prashadi cave = ("images/bgs/bg prashadi cave.jpg")
image bg sea = ("images/bgs/bg sea.PNG")
image bg shabby market = ("images/bgs/bg shabby market.jpg")
image bg shabby town = ("images/bgs/bg shabby town.jpg")
image bg skylla cave = ("images/bgs/bg skylla cave.png")
image bg throneroom = ("images/bgs/bg throneroom.jpg")
image bg underground market = ("images/bgs/bg underground market.jpg")
image bg white = ("images/bgs/bg white.jpg")

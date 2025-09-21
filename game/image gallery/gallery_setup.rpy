#a very simple gallery

init python:

    class GalleryItem:
        def __init__(self, name, images, thumbname, locked="locked"):
            self.name = name #title of the CG, shown in text
            self.images = images #the image of the CG itself
            self.thumbname = thumbname #the name of the thumbnail after thumb_
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
    #Title, cg image (matches gallery images below), thumbnail name
    gallery_items = []
    gallery_items.append(GalleryItem("Prologue", ["cg train"], "cg_train" ))
    gallery_items.append(GalleryItem("Sushi", ["cg_sushi_unlock"] ,"cg_sushi"))
    gallery_items.append(GalleryItem("Fish", ["cg_skyllahands"],"cg_skyllahands" ))
    gallery_items.append(GalleryItem("Lorem ipsum dolor sit amet", ["cg_skyllahands"],"cg_skyllahands" ))
    gallery_items.append(GalleryItem("Title Here", ["cg_ skyllahands"], "cg_skyllahands" ))
    gallery_items.append(GalleryItem("Fish", ["cg_skyllahands"], "cg_skyllahands" ))
    gallery_items.append(GalleryItem("Fish", ["cg_skyllahands"], "cg_skyllahands" ))
    gallery_items.append(GalleryItem("Fish", ["cg_skyllahands"],"cg_skyllahands" ))
    gallery_items.append(GalleryItem("Fish", ["cg_skyllahands"], "cg_skyllahands" ))
    gallery_items.append(GalleryItem("Fish", ["cg_skyllahands"], "cg_skyllahands" ))
    gallery_items.append(GalleryItem("Prologue", ["cg train"], "cg_train" ))
    gallery_items.append(GalleryItem("Prologue", ["cg train"],"cg_train" ))
    gallery_items.append(GalleryItem("Prologue", ["cg train"], "cg_train" ))  
    gallery_items.append(GalleryItem("Title Here", ["cg_ skyllahands"], "cg_skyllahands" ))
    

#trying to fix border for locked imgs
#it did not work. alas
transform fixlock:
    zoom 0.4

#gallery idle border?
image idleLG = ("images/gallery/idleLG.png")

#gallery hover images
image hoverimgLG = ("images/gallery/hoverLG.png")

#gallery images
image cg train = ("images/cg_train.jpg")
image cg_sushi_unlock = ("images/cg sushi.jpg")
image cg skyllahands = ("images/cg skyllahands.png")

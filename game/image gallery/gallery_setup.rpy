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
    gallery_items.append(GalleryItem("On the Train", ["cg_train"], "cg_train" ))
    gallery_items.append(GalleryItem("Deep Market", ["cg_sushi_unlock"] ,"cg_sushi"))
    gallery_items.append(GalleryItem("Fish", ["cg_skyllahands"],"cg_skyllahands" ))
    gallery_items.append(GalleryItem("Mermaid", ["cg_mermaidcetus"], "cg_mermaidcetus" ))
    gallery_items.append(GalleryItem("Transformation", ["cg_mermaidprashadi"], "cg_mermaidprashadi" ))
    gallery_items.append(GalleryItem("King Regent", ["cg notyet"],"cg notyet" ))
    gallery_items.append(GalleryItem("Negotiation", ["cg notyet"], "cg notyet" ))
    gallery_items.append(GalleryItem("Fish", ["cg notyet"], "cg notyet" ))
    gallery_items.append(GalleryItem("Fish", ["cg notyet"],"cg notyet" ))
    gallery_items.append(GalleryItem("Fish", ["cg notyet"], "cg notyet" ))
    gallery_items.append(GalleryItem("Fish", ["cg notyet"], "cg notyet" ))
    gallery_items.append(GalleryItem("Prologue", ["cg notyet"], "cg notyet" ))
    gallery_items.append(GalleryItem("Prologue", ["cg notyet"],"cg notyet" ))
    gallery_items.append(GalleryItem("Prologue", ["cg notyet"], "cg notyet" ))
    gallery_items.append(GalleryItem("Title Here", ["cg notyet"], "cg notyet" ))

#gallery idle border?
image idleLG = ("images/gallery/idleLG.png")

#gallery hover images
image hoverimgLG = ("images/gallery/hoverLG.png")

#gallery images
image cg_train = ("images/cg_train.jpg")
image cg_sushi_unlock = ("images/cg sushi.jpg")
image cg_skyllahands = ("images/cg_skyllahands.jpg")
image cg_mermaid_cetus = ("images/cg_mermaidcetus.jpg")
image cg_mermaid_prashadi = ("images/cg_mermaidprashadi.jpg")
image cg notyet = ("images/cg skyllahands.png")

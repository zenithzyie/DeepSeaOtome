#a very simple gallery

init python:

    class GalleryItem:
        def __init__(self, name, images, hoverimg, locked="locked"):
            self.name = name
            self.images = images
            self.hoverimg = hoverimg
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

    gallery_items = []
    gallery_items.append(GalleryItem("", ["cg train"],"hoverimgSM" ))
    gallery_items.append(GalleryItem("", ["cg_sushi_unlock"] ,"hoverimgSM"))
    gallery_items.append(GalleryItem("", ["cg skyllahands"],"hoverimgLG" ))



#gallery background
image gray = "#777"

#gallery hover images
image hoverimgSM = ("images/gallery/hover 1284x724.png")
image hoverimgLG = ("images/gallery/hoverLG.png")


#gallery images
image cg train = ("images/cg train.png")
image cg_sushi_unlock = ("images/cg sushi.png")
image cg skyllahands = ("images/cg skyllahands.png")


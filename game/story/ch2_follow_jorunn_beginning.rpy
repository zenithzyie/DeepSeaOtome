

label ch2_follow_jorunn:
    "The mist has dissipated, and all that is left is me and the effects of Prashadi's spell."

    show cg_mermaidprashadi:
        align (0.5, 1.0)
        pos (0.5, 1.26)
        zoom 0.34
    with dissolve
    "The sight of a tail greets me, long and shimmering against the polished throne room floor."

    window auto hide
    show cg_mermaidprashadi:
        linear 6 pos (0.5, 2.64) zoom 0.34
    with Pause(6.10)
    if not renpy.seen_image("cg_mermaidprashadi"):
        show cg_mermaidprashadi:
            pos (0.5, 2.64) zoom 0.34
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        show cg_mermaidprashadi:
            pos (0.5, 2.64) zoom 0.34
    window auto show

    "WOWIE! MERMAID!"
    "this is further test dialogue"


    jump endofdemo

    #SCENE CHANGE - fade to black

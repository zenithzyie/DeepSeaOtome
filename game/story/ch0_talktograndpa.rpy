
label grandpatalk:
    window auto hide
    scene bg gpa:
        fit "contain"
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    show bg gpa:
        fit "contain"
    play music bgm_portTown fadein 3.0 volume 0.4
    stop sound
    stop ambience
    stop ambience2
    "I step through the door and enter the ship's quarters."
    #play ambience "audio/sfx_shipCreaking.ogg" volume 1.0 loop fadein 1.0
    show grandpa happy with dissolve
    g "Har har har...what a sight. Yer really grown up now, ain't ye, [y]?"
    show grandpa neutral with dissolve
    g "And I've missed everythin'."
    y neutral "Not everything. We can make up for the lost time now, right?"
    g "Aye... Truth be told, I wasn't sure I'd ever see ye again."
    g "But now that yer here, pull up a chair and anchor in, little birdie."
    "I sit down at the table and Grandfather joins me."
    "My gaze is quickly drawn to the largest picture on the wall."

    show black:
        alpha 0.5
    if not renpy.seen_image("cg_familyportrait"):
        show cg_familyportrait:
            fit "contain"
            xalign 0.5
        with dissolve
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        show cg_familyportrait:
            fit "contain"
            xalign 0.5
        with dissolve

    ny shocked "Is that Grandfather? He looks so young and happy."
    ny happy "That must be Grandmother and Mother next to him."
    g "Yer so much like her. A fine young woman ye have grown into."
    y "Like Mother?"
    g "Ye have Marie's eyes, aye, but yer a spittin' image of yer grandmother."

    #zoom on grandma

    ny neutral "She had already passed when I was born. I hardly know anything about her."
    ny sad "And ever since Mother and I stopped visiting, Grandfather has been all alone."

    hide cg_familyportrait
    hide black
    with dissolve

    y "Grandfather... What happened between you and Mother? Why was I never allowed to visit again?"
    g "..."
    y "Grandfather?"
    show grandpa happy with dissolve
    g "Why don't I get ye some coffee, little birdie."
    "He moves over to a small kettle brewing on the stove."
    y shocked "Huh? I'd love some, but that's not-"
    g "Yer old enough to have some now. It was yer grandmother's favorite."
    "Is he avoiding the question?"
    y neutral "But I really wanted to ask you-"
    show grandpa neutral with dissolve
    g "...Later, little birdie. I'll tell ye later."
    g "How long are ye stayin' in Aquantis for?"
    y "Well... {w}I didn't give it much thought. I just wanted to come see you."
    g "Aye? Then we have plenty of time."
    g "Here ye are, [y]."
    "He hands me one of the steaming mugs of coffee and sits back down."
    y nervous "But Grandfather-"
    g "Ye will stay, won't ye? It'll be just like when ye was little."
    y shocked "I... {w}Of course. If you'll have me?"
    show grandpa happy with dissolve
    g "There's always room for ye here."

    ny neutral "It looks like I won't be getting anything out of Grandfather today..."

    "Perhaps he just needs time."

    ny happy "Well, I'm not planning on leaving soon. I can wait a little longer for him."

    g "Why don't I make ye some stew for dinner. Yer favorite."
    y veryhappy"That sounds wonderful."

    stop music fadeout 1.0
    stop ambience fadeout 1.0

    jump timeskip1

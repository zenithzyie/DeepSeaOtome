label ch2_followthio:

##This is the beginning of the Throne Room continuation, after June is transformed into a mermaid.

#SCENE CHANGE - FADE INTO MERMAID CG

    show cg_mermaidcetus:
        align (0.5, 1.0)
        pos (0.5, 1.26)
        zoom 0.34
    with dissolve
    "The sight of a tail greets me, long and shimmering against the polished throne room floor."

    window auto hide
    show cg_mermaidcetus:
        linear 6 pos (0.5, 2.64) zoom 0.34
    with Pause(6.10)
    if not renpy.seen_image("cg_mermaidcetus"):
        show cg_mermaidcetus:
            pos (0.5, 2.64) zoom 0.34
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        show cg_mermaidcetus:
            pos (0.5, 2.64) zoom 0.34
    window auto show
    "I stare down at it, confused, before my eyes trace it upward and find that it’s connected to me."

    y "Oh! I'm... a mermaid?"

    "And my voice is back!"

    scene bg throneroom:
        fit "contain"
    $ speaking_char = "Cetus"
    show cetus shocked at cetus_right:
        ypos 60
        xzoom -1
    show thioran shocked at thioran_left
    with dissolve

    c mermaid shocked "So it would seem."

    p "What is this?"

    show cetus neutral with dissolve
    c "It appears her true form has been revealed after lifting the curse."

    c "The little fish you brought home was never a fish at all, Prince Thioran."

    c "Do you still feel drawn to her, as you previously described?"


    show thioran frown with dissolve
    p "...No."

    c "I see. How curious."

    p "This has to be some kind of trick. Did you plan all of this to get inside the castle? Were you sent here as a spy?"

    y "I, ah–"

    c "Save your frustrations, Prince Thioran. She knows she must explain herself."

    "He stares pointedly at me."

    c "What is your name?"

    y neutral "[y]. [y] Finch."

    c "Hmm. Quite an unusual name."

    c "Now then, [y] Finch, how did you come across this curse? And what led to your encounter with the prince?"

    "Maybe if I cooperate, they’ll let me go home?"

    y "Well..."

    "From waking up trapped in a bubble to escaping the siren’s cave, I tell them everything – except for the fact that I'm human."

    ny nervous "I’d better keep that part to myself. I don’t know what they’ll do if they find out what I really am."

    p "A siren..."

    c "Then our suspicions are correct. Another Student has indeed appeared."

    ny neutral "A student? Are they referring to Skylla?"

    p "Damn it. Then this '[y]' is lucky to have made it here alive."

    c "She is quite lucky, indeed. These continuous storms are becoming deadlier, and our people grow weary."

    c "Some have even resorted to theft."

    #(show thio grumpier face)
#    show thioran with dissolve
    p "..."

#    show thioran with dissolve
    c "Therefore, for her safety, the witness will need to remain in the guest wing of the castle."

    y shocked "Pardon?"

    show thioran shocked with dissolve
    p "Uncle Ce- Lord Uncle, are you quite serious?"

    c "Quite so, Prince Thioran. She’s the only one who's seen this siren."

    p "But on the upper floors with us? Is that wise?"

    c "No one will question the appearance of a young lady visiting this time of year."

    c "...So long as she knows to stay quiet."

    ny nervous "I guess he wants to keep my involvement with the siren a secret."

    y neutral "I understand."

    c "Now, might I entrust you with the task of escorting her, Prince Thioran?"

    show thioran frown with dissolve
    p "Right now?"

    p "Should I not also be searching for this siren?"

    #(show Cetus amused)
    show cetus smile with dissolve
    c "You’re not getting out of this so easily, nephew. Besides, the storm outside has yet to settle. It would be foolish of you to venture out unprepared."

    show cetus neutral with dissolve
    c "I’ll look into this matter on my own for now."

    #(cetus closed eyes thio resigned)
    p "...Very well."

    p "Be vigilant, Lord Uncle."

    #(show cetus smiling)
    c "Always, Prince Thioran."

    c "And take care not to drift too far yourself."

    "For just a moment, his eyes meet mine."

    c "I hear humans have been sailing further from their shores as of late."

    play sound "audio/sfx_heavyDoorClose.ogg" fadeout 2.0 volume 0.4
    ny shocked "A chill runs down my spine as the throne room doors close behind us."


#SCENE CHANGE - PALACE HALLWAY
    scene bg palace hallway:
        fit "contain"
    show thioran frown at thioran_center
    with dissolve

    $ speaking_char = "all"
    ny mermaid shocked "The prince stays silent as we swim away, but the uneasy feeling doesn't leave me."

    ny nervous "I can still feel Cetus’s eyes on my back."

    "Could he sense that I’m actually human?"

    y "..."

    p "Keep moving. I don’t have all day."

    y "Yes, of course..."

    ny frustrated "And the prince isn’t really princely at all."

    "No, I’ve got to stay calm. {w} Just keep swimming, [y]."

    scene bg palace hallway:
        fit "contain"
    show thioran frown at thioran_center
    with fade

    "..."
    "..."

    ny mermaid neutral "After several turns, we pass by a hallway with a particularly elegant door."

    "It looks like it could lead to someplace quiet, like a library or an office."

    ny shocked "I wonder if it’s a room used by the royal family?"
    ny neutral "The mysterious room lingers in my mind as we move past it in silence."
    scene bg palace hallway:
        fit "contain"
    show thioran frown at thioran_center
    with fade

    "..."
    "..."

    ny mermaid neutral "There’s a pair of voices talking up ahead."

    "Two servants are hanging up elaborate decorations in the hallway."

    "They don’t seem to notice our approach."

    quietmaid "…and Lord Cetus will be lighting the statue at the festival again this year."

    loudmaid "Of course he will. The prince hasn’t been near it since he was a child. I don’t see that changing anytime soon."

    quietmaid nervous "It’s a shame, isn’t it? If only he were a bit more like his late father."

    loudmaid "Or more like his uncle. He’s the very essence of a noble, even if–"

    p "That’s enough."

    quietmaid "Your Highness!" with vpunch

    #"As they frantically bow, I look over at the Prince and can’t help but shiver at his expression."

    show thioran angry with dissolve
    p shocked "The lips of the palace servants are loose indeed to speak so carelessly of the King Regent."

    loudmaid "Forgive us! We were only just-"

    "The prince shoulders his way past them without a second glance."

    "He’s moving faster than before. I hurry after him as best as I can."

    scene bg palace hallway:
        fit "contain"
    show thioran frown at thioran_center
    with fade

    ny mermaid neutral "..."

    menu:
        "Should I say something...?"
        "\"Is there a festival happening soon?\"":
            p "Of course there is. Do not make a mockery of me."
            y flustered "Oh, right."
            y "I’m sorry. It must have slipped my mind."
            ny nervous "Maybe I shouldn’t have asked."
            "It seems like this was something I should have known already."
        "\"Are you okay?\"":
            show thioran frown
            p "..."
            y sad "Those servants were rather rude."
            p "That’s none of your concern."
            ny nervous "Maybe I shouldn’t have asked."
        "\"...\"":
            ny nervous "...No, I better not."
            "I shouldn’t make the situation any worse."

    ny neutral "The Prince suddenly stops before a closed door."
    p "Your room."
    "I quickly move to open the door."

    "I should go inside. The prince doesn’t seem too happy with me right now."

    y "Thank yo–"

    if not renpy.seen_image("cg_thiokabedon"):
        scene cg_thiokabedon with dissolve:
            fit "contain"
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        scene cg_thiokabedon with dissolve:
            fit "contain"

    "Prince Thioran suddenly leans over me, trapping me between his body and the door."
    "He’s leaning in so close!"

    p "What are you really hiding?"
    p "Whatever trick you’re trying to pull here isn’t going to work on me."


    menu:
        "\"You can trust me.\"":
            p "Do you expect me to believe that? Play me the fool?"
            y "We’re on the same side! I want to be free from the siren too."
            y "I don’t want to hurt anyone. I just want to go home."
            p "..."
            y "I promise, I’m not hiding anything from you."
            "...except for the part that would get me turned into fish food."


        "\"I already told you everything.\"":
            p "Do you expect me to believe that? You already tricked me once."
            y  "I wasn’t trying to trick you-  I was cursed."
            y "And you {i}were{/i} the one who brought me here."
            p "A silver tongue won’t save you. I’ll figure out what you’re planning."
            y "I don’t know what you’re talking about."


    "Prince Thioran scoffs at me."
    p "I’ll be keeping my eye on you, [y] Finch."
    "He opens the door behind me and I fall in with it."
    y "Ah! {w=0.3}{nw}" with screenShake

##SCENE CHANGE - GUEST ROOM

    scene bg palace guestroom:
        fit "contain"
    with fade
    play sound "audio/sfx_stoneDoorClose.ogg" volume 0.5
    "The door closes before I can get another word in."

    ny mermaid shocked "What was that?"

    "He was so much kinder when I was a fish..."
    #show june worried
    ny nervous "Now he doesn’t seem to trust me at all. I’d better be more careful."

    "It’s really starting to sink in that I don’t know anything about this world and its people."

    "Even the architecture of this room looks different from what I'm used to."

    ny sad "...I feel more alone than ever."

    "Am I really a guest here?"

    "I can’t believe a simple boat trip ended up like this. I feel exhausted just thinking about it."

    ny neutral "There’s what appears to be a bed on one side of the room. {w}Maybe I should rest for a bit."

    play sound "audio/sfx_bedFlop.ogg" volume 0.5

    ny shocked "Ack!" with vpunch
    "Did I lay on something?"
    "Looking down, I find a purse attached to my waist."
    ny neutral "Oh, right. This must have been created by the magic spell too. I hadn’t really had the time to think about it."
    "Opening it reveals..."
    show black:
        alpha 0.35
    show camera_mermaid at atcamera:
        zoom 0.18
    with dissolve
    extend " a camera."
    y shocked "Wait, is this...? {w}But how is that possible?"
    "It looks a little different but the weight of it feels familiar in my hands. It’s definitely my camera."
    "It couldn’t work underwater, could it?"
    ny neutral "Well, there’s only one way to find out."
    hide camera_mermaid with dissolve
    menu:
        "Take a picture of..."
        "The lamp?":
            play sound "audio/sfx_cameraShutter.ogg" volume 0.8
            show camera with irisin
            hide camera with dissolve
            show photo_guestroom1:
                zoom 0.09
                subpixel True pos (474, 168)
            with dissolve
            "A photo pops out from the top of the camera."
            y "It’s lit up like a lamp, but surely it can’t be using fire or electricity."
            y "I wonder if it's powered by magic?"
            hide photo_guestroom1 with dissolve


        "The window.":
            play sound "audio/sfx_cameraShutter.ogg" volume 0.8
            show camera with irisin
            hide camera with dissolve
            show photo_guestroom2:
                zoom 0.09
                subpixel True pos (474, 168)
            "A photo pops out from the top of the camera."
            y "The star in the center is so eye-catching."
            y "I remember seeing the same shape earlier too. Does it mean something?"

            hide photo_guestroom2 with dissolve

    show camera_mermaid at atcamera:
        zoom 0.18
    with dissolve
    y shocked "Wow…"
    "It really worked. And the colors don’t even bleed."
    "This is incredible! I never thought I’d be taking photos underwater."
    "I was certain I’d lost my camera for good when I fell overboard. How did it survive, anyway?"

    ny happy "Regardless, I’m glad to see it. I’d better keep it safe."
    hide camera_mermaid with dissolve
    "As I tuck the camera and photo into my bag, I can feel my eyes start to grow heavy."
    "I guess everything is finally catching up to me."

    ny neutral "Well, I’m already on the bed. I can figure out what to do after some rest."
    scene bg black with Dissolve(2.0)
    stop music fadeout 1.0
    "..."

#(transition here for dream)
    play music bgm_skyllaCave volume 0.8
    show bg drowning:
        fit "contain"
    with dissolve
    "..."
    "There’s light above me, but it’s drifting further and further away."
    "..."
    "I try to reach for it, but my body won’t respond."
    "..."
    "What’s happening to me?"

    menu:
        "Something.":
            $ pickedsomething = True
            "I think I came here to do something…"
            "But what..?"
        "Someone.":
            $ pickedsomeone = True
            "I think I came here with someone…"
            "But who?"

    "..."
    "..."
    "..."
    "I open my mouth to call out for help, but saltwater floods my lungs."
    scene bg white with Dissolve(2.0)
    "No! It can’t end like this!{w=1}{nw}"
    stop music fadeout 2.5

#(transition here)
    scene bg palace guestroom:
        fit "contain"
    play music bgm_capital volume 0.8
    ny mermaid shocked "I sit up in bed with a gasp." with vpunch
    "The water flows naturally through me as I catch my breath."
    y "I’m… not drowning."
    if pickedsomething:
        "What was I doing in that dream? It felt way too real."
    if pickedsomeone:
        "Who was I with in that dream? It felt way too real."
    ny nervous "Could it mean anything? I don’t know how long this spell will last, after all."
    "Who’s to say the magic won’t start falling apart?"
    "I have to figure out a way to make it back to the surface as a human before it does."
    "Cetus mentioned something about humans earlier… could that mean he knows what I am?"
    "Either way, with his magic, he might be my only chance at getting out of this mess."
    "I need to go find him."

    "I open the door to swim forward, but a guard suddenly blocks my way."

    guard "For your own safety, please do not wander off."

    y "I need to speak to Cetus- er, Sir Cetus. Have you seen him?"

    guard "{i}Lord Cetus{/i} is in his study, and he’s not to be disturbed."

    y "It’s very urgent. I–"

    guard "I'm under direct orders to not let you leave. Please stay inside your room."

    play sound "audio/sfx_stoneDoorClose.ogg"
    queue sound "audio/sfx_doorLockClick.ogg"
    "I’m forced back inside and the door is quickly shut."
    "The sharp click of a lock soon follows."

#    show June worried
    y "Oh, dear. I don’t like the sound of that…"

    "Do they intend to keep me trapped in this room?"

    "There has to be a way out of here."

    call ch2_castle_escaperoom

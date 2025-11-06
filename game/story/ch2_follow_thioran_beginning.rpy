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

    #zoom 0.25

    "I stare down at it, confused for a moment before my eyes trace it upwards and find it connected to my body."

    y "Oh! I'm a mermaid!"

    "And my voice is back!"

    #(surprised cetus)
    c "So it would seem."

    p "What is this?"

    c "It appears her true form has been revealed after lifting the curse."

    c "The little fish you brought home was never a fish at all, Prince Thioran."

    c "Do you still feel drawn to her, as you previously described?"

    p "...No."

    c "I see. How curious."

    scene bg throneroom:
        fit "contain"
    show thioran frown at Position(xpos=0.45)
    $ speaking_char = "all"
    show cetus neutral at left2:
        xzoom -1
        ypos 70
    show thioran frown at farleft
    with dissolve

    p neutral "This has to be some kind of trick. Who are you? Are you some kind of spy?"

    p "This has to be some kind of trick. Who are you? Are you some kind of spy?"

    p "Did you plan all of this to get inside the castle? What were you hoping to accomplish?"

    y "I, ah–"

    c "Save your frustrations, Prince Thioran. She knows she must explain herself to us."

    "He pointedly stares at me, waiting."

    c "What is your name?"

    y "[y]. [y] Finch."

    c "Hmm. Quite an unusual name."

    c "Now then, [y] Finch, how did you come across this curse? And what led to your encounter with the prince?"

    "I don’t think I can refuse to answer."

    "Maybe if I cooperate, they’ll let me go home?"

    y "Well..."

    "From hearing the siren's voice to escaping her cave, I tell them everything– except for the fact that I'm a human."

    "I’d better keep that part to myself. I don’t know what they’ll do if they find out what I really am."

    p "A siren..."

    c "Then our suspicions are correct. Another Student has indeed appeared."

    "A student? Are they referring to Skylla?"

    p "Damn it. This '[y]' is lucky to have made it here alive."

    c "Lucky indeed. The continuous storms are becoming deadlier, and our people grow weary."

    c "Some of them have even been using the storms as an excuse to steal from others."

    #(show thio grumpier face)
    p "..."

    c "Therefore, for her safety, the witness will need to remain here with us on the upper floors."

    y "Pardon?"

    p "Uncle Ce- Lord Uncle, are you quite serious?"

    c "Quite so, Prince Thioran. She’s the only one who's seen this siren."

    p "But on the guest floor? Is that wise?"

    c "There is no harm in it, so long as she stays quiet."

    "Cetus turns to me."

    c "Do keep in mind that the reason why you’re here matters to no one but us."

    "It seems like he wants to keep my involvement with the siren a secret."

    c "Now, might I entrust you with the escort of our guest?"

    p "Right now?"

    p "Should I not also be searching for this siren?"

    #(show Cetus amused)
    c "You’re not getting out of this so easily, nephew. Besides, the storm outside has yet to settle. It would be foolish of you to venture out unprepared."

    #(cetus closed eyes thio resigned)
    p "...Very well."

    p "Be vigilant, Lord Uncle."

    #(show cetus smiling)
    c "Always, Prince Thioran."

    #hide thio
    c "Oh, and… take care not to drift too far yourself."

    "I can feel his eyes boring into me."

    c "I hear humans have been sailing further from their shores as of late."

    "A chill runs down my spine as the throne room doors close behind us."


#SCENE CHANGE - PALACE HALLWAY
    scene bg palace hallway:
        fit "contain"
    show thioran frown at Position(xpos=0.45)
    with dissolve

    $ speaking_char = "all"
    ny neutral "The Prince stays silent as we swim away."

    "What did the Prince’s Uncle mean by drifting too far? Is this mermaid form temporary?"
    "I can’t help but feel Cetus’ warning was a bit more than just a precaution on exploring."

    "After several turns, we pass by a hallway with a solitary door."

    "It looks like a good spot for someplace quiet, like a library or an office."

    p "Keep moving. I don’t have all day."

    y "Right…"

    "We turn {color=#f2b950}left twice, then right…{/color}"

    "There’s a pair of voices talking up ahead."

    "Two maids are hanging up elaborate decorations in the hallway."

    "They don’t seem to notice our approach."

    quietmaid "…and Lord Cetus will be lighting the statue at the festival again this year."

    loudmaid "Of course he will be. The prince hasn’t been near it since he was a child. I don’t see that changing anytime soon."

    quietmaid "It’s a shame, isn’t it? If only he were a bit more like his late father."

    loudmaid "Or more like his uncle. He’s the very essence of a noble, even if–"

    p "That’s enough."

    quietmaid "Your Highness!"

    "As they frantically bow, I look over at the Prince and can’t help but shiver at his expression."

    p "The lips of the palace maids are loose indeed to speak so carelessly of the King Regent."

    loudmaid "Forgive us! We were only just-"

    "The prince shoulders his way past them without a second glance."

    "Somehow, he’s moving faster than before. I hurry after him as best as I can."

    menu:
        "\"Is there a festival happening soon?\"":
            p "Of course there is. Do not make a mockery of me."
            y flustered "Oh, right."
            y "I’m sorry. It must have slipped my mind."
            "Maybe I shouldn’t have asked."
            "It seems like this was something I should have known already as a mermaid."
        "\"Are you okay?\"":
            show thioran frown
            p "..."
            y "Those servants were rather rude."
            p "That’s none of your concern."
        "...":
            "I shouldn’t make the situation any worse."

    "The Prince suddenly stops before a closed door."
    p "Your room."
    "I open the door to the room and turn to thank him, but the Prince is already swimming away."
    y "Oh…"
    "I’m too exhausted to think much of it."
    "I head into the room, eager for some quiet."

##SCENE CHANGE - GUEST ROOM

    scene bg palace guestroom:
        fit "contain"
    with dissolve
    ny neutral "A large sea glass window reflects the bright water outside."

    "My gaze drifts to the bed in the center of the room."

    "Beddddd"

    "I collapse onto the bed and drift off into a dreamless sleep."

    "Some time later, I wake up."

#(transition here)

    "This room is lovely. I’m already learning more than I ever could about mermaids from the decor alone."

    "Would that I had my camera to capture it…"

    "My hand moves to my side out of habit."

    y "Huh?"

    "There’s a bag hanging there that I hadn’t noticed before. Opening it reveals a camera inside."

    y "Wait, is this...? {w}But how is that possible?"

    "It looks a little different but the weight of it feels familiar in my hands. It’s definitely my camera."

    "It couldn’t possibly work underwater, could it?"

    "Well, there’s only one way to find out..."

    menu:
        "Take a picture of the…"
        "Bed":
            pass

        "Window":
            pass

    "The camera automatically develops a photo, just like always. Somehow, the ink doesn’t bleed."

    y "Wow. That’s incredible."

    "But how did it survive all this water? I was certain I’d lost it when the siren captured me."

    "It seems the longer I stay here the more my questions seem to grow."

    "Earlier, Prince Thioran called him the King Regent, and he’s magic. Send help my sexy boob magic man"

    "If Cetus’ spell really is temporary, I have to find him before I get turned back into a fish again or worse."

    "He could be my only chance at getting out of this mess."

    "I open the door and start to swim forward, but a guard suddenly blocks my way."

    guard "For your own safety, please do not wander off."

    y "I need to speak to Lord Cetus. Have you seen him?"

    guard "Lord Cetus is in his study, and he’s not to be disturbed."

    y "It’s very urgent. I–"

    guard "I'm under direct orders to not let you leave. Please stay inside your room."

    "I’m forced back in, and the door is quickly shut with the click of a lock."

#    show June worried
    y "Oh, dear. I don’t like the sound of that…"

    "Do they intend to keep me trapped in this room?"

    "I guess they mean to keep me under house arrest here as a witness."

    "Still, I have to find a way out of here."

    y "I don’t have a fish brain anymore. Getting out of here can’t be that difficult."

    jump ch2_castle_escaperoom

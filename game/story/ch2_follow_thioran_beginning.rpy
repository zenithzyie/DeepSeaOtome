label ch2_followthio:

##This is the beginning of the Throne Room continuation, after June is transformed into a mermaid.

#SCENE CHANGE - FADE INTO MERMAID CG

    "The sight of a tail greets me, long and shimmering against the polished throne room floor."

    "I stare down at it, confused for a moment before my eyes trace it upwards and find it connected to my body."

    y "Oh! I'm a mermaid!"

    "And my voice is back!"

    #(surprised cetus)
    c "So it would seem."

    p "What is this?"

    c "It appears her true form has been revealed after lifting the curse. The little fish you brought home was never a fish at all, Prince Thioran."

    c "Do you still feel drawn to her, as you previously described?"

    p "...No."

    c "I see. How curious."

    scene bg throneroom:
        fit "contain"
    show prince frown at Position(xpos=0.45)
    $ speaking_char = "all"
    show cetus neutral at left2:
        xzoom -1
        ypos 70
    show prince frown at farleft
    with dissolve

    p neutral "This has to be some kind of trick. Why are you trespassing in our waters?"

    c "Save your frustrations, Prince Thioran. She will tell us what happened."

    "He looks at me expectantly."

    menu:
        "Agree":
            #(+1 Cetus)
            c "YOURE ON MY CLOCK NOW FISH"
        "Request to return home.":
            p "That’s not helpful."
            y "But I don’t know anything about ocean storms."
            c "Answer questions first, go homey later"
            y "I…{w} Alright."
            "Damn I gotta talk I guess :("

    c "What is your name?"

    y "[y]. [y] Finch."

    c "An unusual name."
    c "Now then, [y] Finch, what led to your encounter with the prince? How were you transformed?"

    c "That’s a rather unusual name, is it not?"
    c "Regardless. [y] Finch, what led to your encounter with the prince? How were you transformed?"

    "From hearing the siren's voice to escaping her cave, I tell them everything–except for the fact that I'm a human."

    "The more that they know, the quicker they will be able to do something about it."

    "And the quicker I can hopefully go home."

    p "A siren…"

    c "Then our suspicions are correct. Another Student has indeed appeared."

    "A student? Are they referring to Skylla?"

    p "Damn it. This '[y]' is lucky to have made it here alive."

    c "And some have been using the storms as an excuse to steal from others. If this is all truly caused by a siren, it is our duty to put an end to it."

    #(add bitchiness)
    p "im so fucking mad about my fishies being GONE or LIES"

    c "Indeed. However, we must exercise caution."

    c "The witness will need to remain here (on this floor of the castle with us yaay)."

    y "Pardon?"

    p "Uncle Ce- Lord Uncle, are you quite serious?"

    c "Yes, Prince Thioran. She’s the only one who's seen this siren. We need her close to us for the time being."
    #Alt Option:
    c "I have no reason to jest with you, Prince Thioran. She’s the only one who's seen this siren. We need her close to us for the time being."

    p "But here???this is our floor tf"

    c "She’ll be safer with us in the guest wing than anywhere else"

    c "If word gets out further it’ll be more troublesome."

    "Cetus turns to me."

    c "u stfu too"

    c "Now, might I entrust you with the escort of our guest?"

    c "I believe the (previous guest’s room that is prepared already) will be suitable."

    p "Uncle Ce- Lord Uncle, are you quite serious? A servant could handle this. I am no servant."

    c "Now, might I entrust you with the escort of our guest?"

    p "Right now?"

    p "Should I not also be searching for this siren?"

    c "I'll look into this matter myself. You have a duty to ensure our only witness does not come to harm."

    #(closed eyes thio resignment emote)
    p "...Very well."

    p "Be vigilant, Lord Uncle."

    #(smiling)
    c "Always, Prince Thioran."

    "Just before we leave, Lord Cetus turns back to me."

    c "One final thing: take care not to drift too far."

    c "I cannot help you if you return to your cursed form outside these palace walls."

    "A chill runs down my spine as the throne room doors close behind us."

#SCENE CHANGE - PALACE HALLWAY
    scene bg palace hallway:
        fit "contain"
    show prince frown at Position(xpos=0.45)
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
            show prince frown
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

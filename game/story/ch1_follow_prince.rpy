
#BRANCH - FOLLOW THIORAN
#pro and anti mermaid don't matter here
label ch1_followprince:
    hide screen notify2
    hide jorunn glee with moveoutright
    show thioran at Position(xpos=0.45)
    with move
    $ config.side_image_tag = "june"
    "Perhaps the prince would be kind to someone in need?"
    "Alright, [y]! It's now or never!"
    "With all the might I can muster, I push my way through the current towards him."

    show thioran angry:
        subpixel True
        pos (0.45, 730) zoom 1.0
        linear 0.36 pos (0.38, 1288) zoom 2.0
    with Pause(0.46)
    show thioran angry:
        pos (0.38, 1288) zoom 2.0

    #SCREEN SHAKE

    up "What-" with vpunch
    show thioran shocked with dissolve

    "The prince is rather intimidating up close! He's not going to eat me, is he?"

    y "{i}Blub blub blub!!{/i}"

    "Please help me! If I stay out in this storm I'll die!"

    "If only I could speak real words!"

    "Strangely enough, he pauses as if he can understand what I'm saying."

    guard "Your Highness? Is something the matter?"

    show thioran frown with dissolve
    up "No. It's nothing."

    "With a surprising amount of gentleness, he tucks me close to his body."

    "Is he shielding me from view?"

    up "Let's go."

    "Thank goodness. Looks like I made the right choice after all."

    "The prince swims forward, taking me with him."

    menu:
        "I'm nested in the princely merman's hands..."
        "Look through.":
            $ settleback = False
            "I swim forward to peer through the prince's fingers."
            "It looks like we're swimming deeper into the ocean. Foliage and sand whip past us. He's going quite fast!"

        "Settle back.":
            $ prince_points += 1
            $ settleback = True
            "My exhaustion wins over and I lean back against the merman, desperate for a moment of rest."
            "I must be held somewhere against his chest. I can feel his heartbeat, going strong and steady."
            if promermaid >= antimermaid:
                "It's rather comforting."
            if antimermaid > promermaid:
                "It's oddly comforting."

#SCENE CHANGE - Capital City (zoomed in)
    $ config.side_image_tag = "june"
    scene bg black with dissolve
    "Some time passes, and the prince suddenly stops, jostling me from my thoughts."
    "Is that...light seeping through his fingers?"

    if settleback:
        "Intrigued, I swim a bit closer to get a better look."
    else:
        pass

#zoom broken bc of new bg size
#    window auto hide
#    scene bg_marislumina:
#        xalign 0.5
#        subpixel True
#        zoom 1.05
#        linear 1.75 zoom 1.0
#    with dissolve
#    with Pause(1.75)

    play music bgm_capital volume 0.8
    show bg_marislumina night:
        fit "contain"
    show black:
        alpha 0.2
    ny neutral fish "Are we really at the bottom of the ocean? How can it be so bright here?"

    "How beautiful. This must be where the mermaids live."

    "If only I could capture this sight in a photo! No one on land would ever believe such a place exists down here."

    hide black
    show thioran frown at thioran_center
    show black:
        alpha 0.2
    with dissolve
    up "Go on ahead to make a report on the storm. I shall return to the palace shortly."

    guard "Yes, my prince."

    "The guard bows and swims away."

    "Now that we're alone, the prince relaxes his hands around me."

    up "You're safe now. The storm can't reach us in the city."

    up "How did you end up here? Did you get separated from your school?"

    y "Blub..."

    if promermaid >= antimermaid:
        "Something like that..."
    if antimermaid > promermaid:
        "You have no idea..."
 
    up "I suppose that makes two of us."

    "Can he really understand me?"

    #TESTING WEEEEE
    show thioran frown with dissolve
    $ night = True
    y "Blub...{w}blub?"
    y mermaid shocked "Blub..."
    #hide thioran
    show thioran shocked with dissolve

    menu:
        "Maybe I should try saying something..."
        "Hello? Can you hear me...?":
            y "Blub{w} blub...?"

        "A siren did this to me!":
            y "Blub blub blub!"

        "HELP ME!!!":
            y "BLUB BLUB!!!" with screenShake

    up "Are you sick? Injured?"

    "...Apparently not."

    "The prince inspects me carefully."

    up "Hold still for a moment."

    "He gently pulls something from my fins."

    "Is that...crystal? It must have come from the siren's cave."

    up "..."

    up "What did you run into out there?"

    "The prince begins to move with newfound purpose."

    "The city is bustling, but he avoids the crowds in favor of swimming through a quieter area."

    "All I can do is stay between his hands."

    #fade transition (same scene)

    "Eventually, we arrive at the tallest structure, which must be the castle."

#SCENE CHANGE - Throne Room
    window auto hide
    scene bg throneroom:
        fit "contain"
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    scene bg throneroom:
        fit "contain"
    "Our final destination - a grand throne room."
    "What a sight..."
    "Light is pouring through the open windows."

    $ speaking_char = "all"
    show cetus neutral at cetus_center:
        xzoom -1
    with dissolve
    "A mermaid is waiting on the throne at the end of the room."
    $ speaking_char = "all"
    show cetus neutral at cetus_right:
        xzoom -1
    show thioran frown at thioran_left
    with dissolve

    #this section needs edited

    show cetus shocked with dissolve
    ny neutral fish "He holds himself proudly, but he abandons this as soon as he sees the prince."
    
    ucetus "Prince Thioran! Where have you been?"

    p "Uncle Cetus. It has been a long day. You will have to forgive my impropriety."

    "Uncle? Does this mean that he's royalty too?"

    c "The storm takes both pauper and prince alike. You know this."

    p "...I do."

    "Cetus shakes his head and sighs."

    c "No matter. As long as you're safe."

    c "Now, what troubles you? You look as though you've swallowed an urchin."

    p "It's just-{w}here. I found her near the storm."

    "Gently, he brings me forth, presenting me to his uncle like a treasure he had discovered."

    show cetus neutral with dissolve
    c "Oh...? Find another pet for yourself out there, nephew?"

    c "You know you don't need my permission to keep her."

    "Oh dear. He isn't actually planning to keep me as a pet, is he?"

    p "There's something unusual about this one. I found shards caught in her fins."

    c "Ah, a brave survivor of the storm. How fortunate that you've rescued her."

    p "It wasn't normal debris. I suspect it might have been magical in nature."

    p "And I feel...drawn to her. I can't quite explain it."

    "Drawn to me? huh"

    p "Will you take a look, Uncle?"

    c "Hmm. Very well."

    y "Blub!"

    "June thought here"

    

    $ speaking_char = "Cetus"
    "Cetus slowly approaches me, brows furrowing."
    "It almost feels like he's staring right through me, right at something I can't see."
    c "Hmm?"
    "I feel oddly flustered as he inspects my body."
    "This would be a rather inappropriate gaze if I were still a human."
    c "Let me take a closer look."
    menu:
        "Move forward.":
            #(+1 cetus)
            "I'll do anything if he can help me return to normal!"
            "I swim closer to him, indicating my agreement."

        "Look back.":
            "I glance back up at Prince Thioran. He gives me the slightest of nods."
            show thioran soft with dissolve
            p "Go on, it's alright."
            #(+1 thio)
            "Well, if the prince says it's alright..."
            show thioran frown with dissolve

    "I brace myself as Cetus reaches for me, but his hands are clinical as they brush over my fins."
    c "What an interesting little thing."
    "The prince moves closer to us with a troubled look."
    p "What do you see, Uncle?"
    c "Hmm...She's not from these waters, that I can tell."
    c "More importantly, she's been cursed. By something rather skilled, no less."
    p "Cursed?"
    "That's right! Thank goodness he can tell."
    "If only I hadn't been stupid enough to fall for that sea witch's music..."
    p "Is there anything you can do?"
    c "Though the curse is rather complex, it won't be a match for me."
    c "I shall start unraveling the enchantment. You may wish to swim back, Prince Thioran."
    "Really? Just like that? I'll finally be free from this nightmare!"
    "Cetus's hands begin to glow."
    "His hands move like the conductor of an orchestra, and strings of magic entwine themselves around my body."
    "Wait...{w} what will happen if I turn back into a human underwater?"
    "A tingling feeling runs from my head to my tailfins and for a moment, I feel as though I am being stretched uncomfortably tight."
    y "{i}Blub! Blub!{/i}"
    "No! I'll drown! I don't want to die like this!"
    show thioran shocked with dissolve
    p "Wait a moment, Uncle. There's something wrong."
    play sound "audio/sfx_CetusCastMagic.ogg" volume 0.6
    "The magic crescendos, and the tightness around me grows in kind."
    scene bg black with dissolve
    "I squeeze my eyes shut. All I can do is prepare for the worst."
    "Grandfather...! Hunter!"

    "Then, all at once the discomfort disappears. {w}An odd sort of warmth rushes over me instead, as gentle as silk on my skin."
    "I gasp for breath, relieved to find that I'm not drowning."
    "I begin to instinctively tread water. My legs feel like they are tied together, but they are still managing to keep me from going downward."
    "There is nothing but the sound of flowing water around me."
    "I open my eyes."

    call ch2_followthio from _call_ch2_followthio

    #"The strings have disappeared, and all that is left is me and the effects of Cetus' spell."

    scene bg white with hpunch
    jump endofdemo

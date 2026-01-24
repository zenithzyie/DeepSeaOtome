
#BRANCH - FOLLOW THIORAN
label ch1_followprince:
    $ followprince.grant()
    hide screen notify2
    hide jorunn glee with moveoutright
    show thioran at Position(xpos=0.45)
    with move
    $ config.side_image_tag = "june"
    "Perhaps the prince would be kind to someone in need? I hope this fishy shape I'm in isn't some sort of delicacy..."
    "Alright, [y]! It's now or never!"
    "3...2...1!!"
    y "BLUBBB!!!!" with vpunch
    "With all the might I can muster, I push my way through the current."

    show thioran angry:
        subpixel True
        pos (0.45, 730) zoom 1.0
        linear 0.36 pos (0.38, 1288) zoom 2.0
    with Pause(0.46)
    show thioran angry:
        pos (0.38, 1288) zoom 2.0

    "I can't stop! I crash into the back of the princely merman's head." with vpunch
    #SCREEN SHAKE
    up "!!!"
    up "Who-"
    y "Blub blub!"
    show thioran shocked with dissolve
    up "...?"
    "For a brief moment I think I've made some sort of mistake and that I'll be eaten on the spot."
    "Then, with a surprising amount of gentleness, his hands come up to cup my body."
    guard "Your Highness?"
    y "{i}Blub blub blub!!{/i}"
    "Please help me! If I stay out in this storm I'll die!"
    "If only I could speak real words!"
    "Strangely enough, he pauses as if he can understand what I'm saying."
    guard "Is something the matter? The storm is closing in."
    show thioran frown with dissolve
    up "No. It's nothing."
    "Suddenly he tucks me close to his body, his hands carefully shielding me from view."
    up "Let's go."
    "Thank goodness. Looks like I made the right choice after all."
    "I can feel the merman begin to swim. I'm exhausted but curious about where we're going."

    menu:
        "I'm nested in the princely merman's hands..."
        "Look through.":
            "My curiosity wins over, and I swim forward a little to try to peer through the space between the prince's fingers."
            "It looks as though we're swimming somewhere deeper into the depths of the ocean. Foliage and sand whip past us. We are going quite fast!"
            "His hands continue to shield me as he keeps swimming onward."

        "Settle back.":
            #+1 Thio
            "My exhaustion wins over and I lean back against the merman's skin, desperate for a minute of rest."
            "I must be held somewhere against his chest. I can feel his heartbeat, going strong and steady."
            "It's warm and comforting."
            "The storm rumbles on, and I have no need to fear it any longer."
            "The prince swims on in silence."

    "Left alone with my thoughts, my mind races every which way."
    "Am I the first human to experience the sea like this?"
    "I wish I had my camera. {w}But it wouldn't have survived the plunge..."
    "All those memories made with it must be gone now, lost to me just like my own body."

#SCENE CHANGE - Capital City (zoomed in)
    $ config.side_image_tag = "june"
    scene bg black with dissolve
    "Some time passes, and the prince stops suddenly, jostling me from my thoughts."
    "I notice a multitude of colorful lights seeping through his fingers. Are we really at the bottom of the ocean? How can it be so bright here?"
    "Intrigued, I swim a bit closer to get a better look."
    window auto hide
    scene bg capitalcity:
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)

    play music bgm_capital volume 0.8
    show bg capitalcity
    ny neutral fish "My fish eyes grow even wider as I spot several towering seashell structures and more mermaids than I could ever count."
    "I feel smaller than I already am..."
    "Colorful corals are everywhere, decorating mermaid homes and streetways like the people back home decorate their homes with flowers."
    "Would that I could capture this sight in a photo! No one on land would ever believe such a place exists down here."
    show thioran frown at Position(xpos=0.45) with dissolve
    up "Go on ahead to make a report on the storm. I will return to the palace shortly."
    guard "Yes, my prince."
    "I glimpse the guard that had been following him bow and swim away, leaving me alone with the prince in this strange but beautiful city."
    "He begins moving forward again. Now that we are away from the threat of the storm, it is at a more leisurely pace."
    "I glance up at him, but I notice he is glancing at me as well. Our eyes meet for a brief moment."
    show thioran shocked with dissolve
    up "Is something the matter?"
    "He seems concerned about my well-being, even though we have just met."
    "A truly princely fellow!"
    y "Blub!"
    "I shake myself in response. I'm already quite comfortable."
    "I'm just glad he isn't finding my staring strange."
    show thioran frown with dissolve
    "He nods before returning his gaze back ahead."
    up "We will be at the palace before long. How did you end up so far away? And alone?"
    "Earlier, when I tried speaking to him, he seemed to understand me. Maybe he can speak fish after all?"
    "I'm not really sure how much he can hear, but I'm willing to try telling him my story."
    y "Blub...{w}blub?"
    y "Blub..."
    show thioran shocked with dissolve
    up "What are you..."
    up "I apologize. It appears I can't fully understand your meaning."
    show thioran frown with dissolve
    "I barely notice his hands shift out of the corner of my eyes. One moves closer to me, his fingertips gently brushing against my tailfins."
    "...?"
    up "Hold still. There's something in your..."
    "I feel the tiniest prick and then his hand lifts away from me to examine what he found."
    "It takes me a moment to recognize it myself."
    "It looks like a shard of the glowing stones back from the siren's cave."
    up "This is no ordinary rubble. There's traces of magic all over it...and all over {i}you{/i}."
    "The shard he is holding suddenly crumbles to pieces."
    up "Hmm..."
    "The hands around me shift closer as he swims faster with newfound purpose, gliding through the crowd of mermaids. They bow as he passes by, but he doesn't acknowledge them."
    "All I can do is stay between his hands."
    up "I must take you to my uncle."
    up "Perhaps he can explain this strange connection I feel with you."
    "Does his uncle know more about magic?"
    "...Can he turn me back into a human?"
    "Eventually, we arrive at the grandest structure, which must be the castle."
    "The prince takes me through wide halls, filled with busy servants and expensive decor."

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
    "Our final destination: a grand throne room."
    $ speaking_char = "all"
    show cetus neutral at cetus_center:
        xzoom -1
    with dissolve
    "A merman is waiting on the throne at the far end. Somehow, light is pouring through the open windows, bathing him in an ethereal glow."
    $ speaking_char = "all"
    show cetus neutral at cetus_right:
        xzoom -1
    show thioran frown at thioran_left
    with dissolve

    #this section needs edited

    ny neutral fish "Instead of a single tail like the prince, he has several tentacles like an octopus."
    "He holds himself like a royal."
    show cetus shocked with dissolve
    "But he abandons this as soon as he notices the prince."
    "Concern is wrought all over his face as he rushes forward, and I know this has to be the uncle."
    ucetus "Prince Thioran! Where have you been?"
    ucetus "It's not safe to be out wandering while the sea storms rage on."
    p "Uncle Cetus. It has been a long day. You will have to forgive my impropriety."
    "Oh! The prince is named Thioran?"
    "Thioran and Cetus...such strange names mermaids have."
    "Cetus shakes his head and sighs."
    c "No matter. As long as you're safe."
    c "Now, you look troubled. Whatever is the matter?"
    p "It's just-{w} here. I found her near the storm."
    "Gently, he brings me forth, presenting me to his uncle like a treasure he had discovered."
    show cetus neutral with dissolve
    "Cetus's eyes catch on me, and I freeze at the sudden attention."
    c "Oh? What's this? Find another pet for yourself out there, nephew?"
    c "You know you don't need my permission to keep her."
    p "I've never seen a fish like her, and despite being incapable of speech, I seem to be able to understand her intentions."
    p "I feel this..."
    p  "I feel something drawing me in. I can't quite explain it."
    "...?"
    p "It is rather strange. She appears to be just a normal fish."
    y "Blub!"
    "I definitely am not!"
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
    p "Wait a moment, Uncle! There's something wrong."
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

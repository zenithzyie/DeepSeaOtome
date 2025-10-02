
#BRANCH - FOLLOW THIORAN
label ch1_followprince:
    hide jorunn glee with moveoutright
    show prince at Position(xpos=0.45)
    with move
    $ config.side_image_tag = "june"
    "Perhaps the prince would be kind to someone in need? I hope this fishy shape I'm in isn't some sort of delicacy..."
    "Alright, [y]! It's now or never!"
    "3...2...1!!"
    y neutral fish "BLUBBB!!!!"
    "With all the might I can muster, I push my way through the current, leaving a trail of bubbles behind me."

    show prince angry:
        subpixel True
        pos (0.45, 730) zoom 1.0
        linear 0.36 pos (0.38, 1288) zoom 2.0
    with Pause(0.46)
    show prince angry:
        pos (0.38, 1288) zoom 2.0

    "I can't stop! I crash into the back of the princely merman's head." with vpunch
    #SCREEN SHAKE
    up "!!!"
    up "Who-"
    y "Blub blub!"
    show prince sweat with dissolve
    up "...?"
    "For a brief moment I think I've made some sort of mistake and that I'll be eaten on the spot."
    "Then, with a surprising amount of gentleness, his hands come up to cup my body."
    guard "Your Highness?"
    y "{i}Blub blub blub!!{/i}"
    "Please help me! If I stay out in this storm I'll die!"
    "If only I could speak real words!"
    "Strangely enough, he pauses, as if he can understand what I'm saying."
    guard "Is something the matter? The storm is closing in."
    show prince frown with dissolve
    up "No. It's nothing."
    "Suddenly he tucks me close to his body, his hands carefully shielding me from view."
    up "Let's go."
    "The relief I feel is so strong that I feel my fins go weak. Thank goodness. Looks like I made the right choice after all."
    "I can feel the merman begin to swim. I'm exhausted but curious about where we're going."

    menu:
        "I'm nested in the princely merman's hands..."
        "Look through.":
            "My curiosity wins over, and I swim forward a little to try to peer through the space between the prince's fingers."
            "It looks as though we're swimming somewhere deeper into the depths of the ocean. Foliage and sand whip past us. We are going quite fast!"
            "I can catch glimpses of merpeople appearing to be farmers, tending to their fields of kelp and other sea plants I do not recognize."
            "Some wave to the prince as we pass."
            "Despite this, he keeps swimming, his hands acting as a shield."

        "Settle back.":
            #+1 Thio
            "My exhaustion wins over and I lean back against the merman's skin, desperate for a minute of rest."
            "I must be held somewhere against his chest because from here I can feel his heartbeat, going strong and steady."
            "It's warm and comforting."
            "The storm rumbles on, and I have no need to fear it any longer."
            "The prince swims on in silence."

    "Left alone with my thoughts, my mind races every which way."
    "Am I the first human to experience the sea like this?"
    "I wish I had my camera. {w}But it wouldn't survive the plunge..."
    "All those memories made with it must be gone now, lost to me just like my own body."
    "I hope it somehow escaped my fate."

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
    ny neutral fish "My fish eyes grow even wider as I spot several towering seashell structures and more merfolk than I could ever count."
    "I feel smaller than I already am..."
    "Colorful corals are everywhere, decorating mermaid homes and streetways like the people back home decorate their homes with flowers."
    "Would that I could capture this sight in a photo! No one on land would ever believe such a place exists down here."
    show prince frown at Position(xpos=0.45) with dissolve
    up "Go on ahead to make a report on the storm. I will return to the palace shortly."
    guard "Yes, my prince."
    "I glimpse the guard that had been following him bow and swim away, leaving me alone with a prince in this strange but beautiful city."
    "Away from the threat of the storm, he begins swimming again. This time, it is at a more leisurely pace."
    "I glance up at him, but I notice he is glancing at me as well. Our eyes meet for a brief moment."
    show prince sweat with dissolve
    up "Is something the matter? If you're uncomfortable in my hands, I can try to be less...rough."
    "He seems concerned about my well-being, even though we have just met."
    "A truly princely fellow!"
    y "Blub!"
    "Quickly, I shake myself in protest at the suggestion. He is already very gentle."
    "I'm just glad he isn't finding my staring strange."
    show prince frown with dissolve
    "He nods before returning his gaze back ahead."
    up "We will be at the palace before long. How did you end up so far away? And alone?"
    "Earlier, when I tried speaking to him, he seemed to understand me. Maybe he can speak fish after all?"
    "I'm not really sure how much he can hear, but I'm willing to try telling him my story."
    y "Blub...{w}blub?"
    "From Skylla's cave, to me escaping and seeing him and the thief, I tell him all of it."
    up "What are you..."
    show prince sweat with dissolve
    up "I apologize. It appears I can't fully understand your meaning."
    show prince frown with dissolve
    "I barely notice his hands shift out of the corner of my eyes. One moves closer to me, his fingertips gently brushing against my tailfins."
    "...?"
    up "Hold still. There's something in your..."
    "I feel the tiniest prick and then his hand lifts away from me to examine what he found."
    "It takes me a moment to recognize it myself."
    "It looks like a shard of the glowing stones back from the siren's cave. It must have gotten caught in my fins during my escape. I hadn't even noticed."
    up "This is no ordinary rubble. There's traces of magic all over it...and all over {i}you{/i}."
    "The shard he is holding suddenly crumbles to pieces and a glimmer of freed magic is whisked away by the ocean current."
    up "Hmm..."
    "The hands around me shift closer as he swims faster with newfound purpose, gliding effortlessly through the crowd of merfolk. They bow as he passes by."
    "All I can do is stay between his hands."
    up "I must take you to my uncle."
    up "Perhaps he can explain this strange connection I feel with you."
    "He must be another member of the royal family."
    "Does he know more about magic?"
    "...Can he turn me back into a human?"
    "I suppose all I can do is wait for the prince to take us there."
    "We go through the city quickly, passing all sorts of things I wish I could take a closer look at."
    "Eventually, we arrive at the grandest structure, which must be the palace."
    "The prince takes me through wide halls, servants greeting him as we pass."

    window auto hide
    scene bg throneroom:
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    scene bg throneroom:
        fit "contain"
    "Our final destination: a grand throne room."
    show prince frown at Position(xpos=0.45)
    "There is a merman waiting on the throne at the end. Somehow, light is pouring through the open windows, bathing him in an ethereal glow."
    $ speaking_char = "all"
    show cetus neutral at left2:
        xzoom -1
    show prince frown at farleft
    with dissolve

    ny neutral fish "Instead of a single tail like the prince, he has several tentacles instead, like an octopus."
    "He holds himself like a royal."
    "But he abandons this as soon as he sees the prince, and he quickly rushes forward."
    "Concern is wrought all over his face, and I know this has to be the uncle."
    ucetus "Thioran! Where have you been?"
    ucetus "I've been looking all over for you. It's not safe to be out wandering while the sea storms rage on."
    p "Uncle Cetus. It has been a long day. You will have to forgive my impropriety."
    "Ah! The prince is named Thioran?"
    "Thioran and Cetus...such strange names merpeople have."
    "Cetus shakes his head and sighs."
    c "No matter. As long as you're safe..."
    c "Now, you look troubled. Whatever is the matter?"
    p "It's just-{w} here. I found her near the storm."
    "Gently, he brings me forth, presenting me to his uncle like a treasure he had discovered."
    "Cetus' eyes catch on me, and I freeze at the sudden attention."
    "Any thoughts I may have had halt to a stop."
    c "Oh? What's this? Find another pet for yourself out there, Thioran?"
    c "You know you don't need my permission to keep her."
    p "I wanted to ask you to examine her."
    p "She is rather strange. I've never seen a fish like her, and despite being incapable of speech, I seem to be able to understand her intentions."
    p "I feel this..."
    p  "I feel something drawing me in. I can't quite explain it."
    "...?"
    p "She shouldn't have any arcane connections. She appears to be just a normal fish."
    y "Blub!"
    "I definitely am not!"
    "Cetus begins to approach, brows furrowing."
    "His gaze is piercing."
    "It almost feels like he's staring right through me, right at something I can't see."
    c "Hmm?"
    "I feel oddly flustered as he inspects my body."
    "This would be a rather inappropriate gaze were I still human."
    c "May I touch your fins, little fish?"
    menu:
        "Agree.":
            #(+1 cetus)
            "If he can help me return to normal, I'll do anything!"
            "I swim closer to him, indicating my agreement."

        "Hesitate.":
            "I glance back up at Prince Thioran. He gives me the slightest of nods."
            show prince soft with dissolve
            p "Go on, it's alright."
            #(Thio +1)
            "Well, if the prince says it's alright..."
            show prince frown with dissolve

    "I brace myself as Cetus reaches for me, but his hands are clinical as they brush over my fins."
    c "What an interesting little thing."
    "The prince moves closer to us with a troubled look."
    p "What do you see, Uncle?"
    c "Hmm...well she's not from these waters, that I can tell. However, that's a tale for another time."
    c "More importantly, she's been cursed. By something rather skilled, no less."
    p "Cursed?"
    "That's right! It's a relief that he can tell."
    "If only I hadn't been stupid enough to fall overboard for that sea witch's music."
    p "Is there anything you can do about it?"
    c "Yes. Though the curse is rather complex, it won't be a match for me."
    c "I shall start unraveling the enchantment now. You may want to swim back, Thioran."
    "Really? Just like that? I'll finally be free from this nightmare!"
    "Cetus' hands start to glow as he starts to cast his spell."
    "His hands move like the conductor of an orchestra, and strings of magic entwine themselves around my body."
    "Cetus begins to chant in a language I do not know, his hypnotic voice droning on and drowning out my thoughts."
    "Wait...{w} what will happen to me if I turn back human underwater?"
    "A tingling feeling runs from my head to my tailfins and for a moment, I feel as though I am being stretched uncomfortably tight."
    y "{i}Blub! Blub!{/i}"
    "No..! I'll drown! I don't want to die like this!"
    show prince sweat with dissolve
    p "Wait a moment, Uncle! There's something wrong."
    "But Cetus does not stop his chanting."
    "The magic crescendos, and the tightness around me grows in kind."
    scene bg black with dissolve
    "All I can do is prepare for the worst."
    "Grandpa..! Hunter!"

    #(brief pause)
    #(fade to white)
    #(next update, fade to cg of june)

    "Then, all at once the discomfort disappears. {w}An odd sort of warmth rushes over me instead, as gentle as silk on my skin."
    "I gasp for breath, relieved to find that I'm not drowning."
    "I begin to instinctively tread water. My legs feel like they are tied together, but they are still managing to keep me from going downward."
    "There is nothing but the pleasant sound of flowing water around me."
    c "Welcome back to your body, my dear."
    "I open my eyes."

    #"The strings have disappeared, and all that is left is me and the effects of Cetus' spell."

    scene bg white with hpunch
    jump endofdemo

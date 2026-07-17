
#BRANCH - FOLLOW JORUNN
label ch1_followjorunn:
    $ followthief.grant()
    hide screen notify2
    hide thioran angry with moveoutleft
    show jorunn neutral at Position(xpos=0.52) with move
#potential promermaid count: 2 or 1 or 0
#potential antimermaid count: 2 or 1 or 0
    "The thief seems to know his way around. Maybe he can get me out of this mess."
    "Alright, [y]! It's now or never!"
    "With all the might I can muster, I push my way through the current towards him."

    show jorunn neutral:
        subpixel True
        pos (0.52, 804) zoom 1.0
        ease 0.41 pos (0.50, 1355) zoom 2.04
    with Pause(0.50)
    show jorunn neutral:
        ease 0.41 pos (0.50, 1355) zoom 2.04

    show jorunn hesitant with dissolve
    uj "Huh?"
    y "Blub!!"
    "A deft hand snatches me up."
    show jorunn smile with dissolve
    uj "Oh, well this is new! Never had a fish come up to my net before."
    y "{i}Blub blub blub!!{/i}" with hpunch
    "Wait, hang on now! Please don't eat me!"
    "If only I could speak real words!"
    show jorunn neutral with dissolve
    "He squints at me for a moment."
    uj "Huh? What's this?"
    "His other hand plucks something from my fins."
    "Ouch!"
    show jorunn hesitant with dissolve
    uj "Oh?"
    "It takes me a moment to recognize it myself."
    "Is that...crystal? It must have come from the siren’s cave."
    uj "Weird. This thing stinks of magic."
    uj "Now that I think about it..."
    show jorunn smile with dissolve
    uj "So do you, little fishie!"
    y "Blub!!"
    uj "You're no normal fish, are you?"
    show jorunn hesitant with screenShake
    "It feels like the sea storm is picking up even more!"
    uj "First thing's first, we'd better get out of here."
    "He places me on his shoulder under all his hair. It's surprisingly well covered."
    show jorunn smile with dissolve
    uj "Hang tight, okay? Once we get to the forest, we'll be safe from the worst of it."
    y "Blub...!"
    "He's not going to eat me!"
    "Thank goodness. Looks like I made the right choice after all."

#    window auto hide
#    show black
#    with dissolve
#    pause 0.2
#    hide black
    scene bg jorvillagenearby:
        fit "contain"
    show jorunn neutral
    show jorunn neutral:
        pos (0.50, 1355) zoom 2.04
    with fade
#    window auto show

    ny neutral fish "The thief swims forward at a steady pace, unbothered by the growing sea storm."

    menu:
        "I'm nested in the merman's hair..."
        "Try to look through.":
            $ looked_through = True
            $ jorunn_points += 1
            "My curiosity wins over, and I swim forward to try to peer through his hair."
            "As if realizing my intentions, he angles his shoulders to give me a better view."
            "The foliage is thick here, tall plants towering over the both of us like massive trees."
            "With the storm muffled by the cover of the kelp forest, the swim almost feels...{w} peaceful."
            show jorunn smile with dissolve
            uj "It's pretty out here, don't you think?"
            y "Blub!"
            "I really wish I could take a picture of the ocean."
            uj "If we go a bit further out, you'll see my home."
            uj "But that's not important right now. We gotta get you fixed up first!"

        "Settle back.":
            "My exhaustion wins over and I lean back against the crook of his neck, desperate for a minute of rest."
            "It's surprisingly comfortable here."
            "If it bothers the merman he doesn't say anything about it."
            "..."

    show jorunn happy with dissolve
    j "I'm Jorunn, by the way! {w}Sorry, guess I should've said that earlier."
    if promermaid >= antimermaid:
        "Jorunn...such interesting names mermaids have."
    if antimermaid > promermaid:
        "Jorunn...such strange names mermaids have."
    j "But you can call me Jor. That's what everyone else calls me too."
    j "Hey, you don't happen to have a name yourself, do you?"
    y "Blub!"
    "He's a rather talkative fellow, isn't he!"
    show jorunn neutral with dissolve
    j "Right. Can't talk and all that."
    "He sounds a bit disappointed that I can't reply."
    show jorunn smile with dissolve
    j "Don't worry. Miss Prash will know what to do with you. She's the master when it comes to all this magic stuff."
    j "And you look like magic stuff."
    "Miss Prash...?"
    "Is it possible? Is there another mermaid out there that can turn me human again?"
    show jorunn hesitant with dissolve
    j "Or, uh, unless I'm losing it, and you're just a normal fish."
    j "I hope I'm not just talking to myself right now."
    show jorunn neutral with dissolve
    y "Blub!!!"
    $ speaking_char = "None"
    "Even so, he keeps swimming, content to keep me in his hair for the time being."

#SCENE CHANGE? - Kelp Forest

    show jorunn happy with dissolve
    j "Almost there, little fishie! I hope you've been enjoying the ride so far."
    "With that, he takes us into a cave, leaving the kelp forest behind."
#SCENE CHANGE - fade to black... or maybe it goes suddenly black?
    scene bg black with dissolve
    stop music fadeout 5.0
    y "...!"
    "The deeper we go, the darker it gets."
    "Grandfather told me stories of how dangerous the sea could be at night."
    "Storms would roll in without warning, stealing away the moon and turning everything pitch black."
    "I think this is what he must have meant."
    "I can't see anything in front of me at all."
    "The only signs that I'm alive are my own thoughts, and the feel of Jorunn's steady swimming as he takes us deeper still."
    "It feels like there’s no end to this darkness…"

    menu:
        "I'm sure it will be alright.":
            $ promermaid += 1
            "I came this far already. I can't lose hope here."
            "At the end of his stories, Grandfather always came back home safe."
            "I have to trust that I can do the same."
            "..."
            "Oh! I see something glimmering up ahead!"

        "I regret trusting him.":
            $ antimermaid += 1
            "Maybe I made the wrong decision..."
            "What was I thinking, trusting a mermaid?"
            if antimermaid >= 2:
                "His kind is the reason why I fell off Hunter's boat in the first place."
            "Anything could be in here, and I'm just letting him lead me to my doom."
            "..."
            "Just when I think we're going to be wandering around in this dark void forever, something glimmers in the distance."

    j "And here we are!"

#SCENE CHANGE - Prashadi's Cave
    play music bgm_prashCave

    "...!"

    scene bg_prashadicave:
        fit "contain"
    with fade

    $ config.side_image_tag = "june"
    ny neutral fish "Are those...stars above us?"

    show jorunn happy at jorunn_center with dissolve
    j "Miss Prash! Are you in here?"
    "Sure enough, what looks to be the night sky is shining above us, illuminating the entire cavern in a gentle glow."
    "The sky? How is this even possible? We definitely swam deeper to get here."
    show jorunn hesitant with dissolve
    j "Hello? Miss Prash?"
    j "..."
    j "Prashadi!!" with vpunch
    show jorunn neutral with dissolve
    "I'm not sure what to expect."
    "The mermaids in the Deep Market had long hair and shiny scales."
    "Maybe she will be similar to them?"
    show jorunn at jorunn_right with move
    u "Is that Jorunn I hear?"
    "The voice sounds heart-wrenchingly familiar."
    "A figure swims into view from the darker recesses of the cave."
    $ speaking_char = "all"

    #(a flash of grandpa's sprite here)
    show grandpa neutral at left2
    with dissolve
    pause 0.2
    hide grandpa
    show prashadi neutral at left2
    with fade
    "Grandfather!?"

    gpa "Now here's a face you don't see very often!"
    gpa "What brings you all the way down here, boy?"
    show jorunn happy
    j "Did you miss me? I found something I think you'd like to see."
    j "Take a look, Miss Prash!"
    $ speaking_char = "Prashadi"
    "Jorunn pushes me towards 'Miss Prash', and I can only stare, dumbfounded."
    "That's Grandfather. That's him."
    "What in the world?"
    show jorunn neutral
    j "She had some kind of magic shards stuck in her fins."
    gpa "Well now..."
    "His hands carefully cup my body."

    menu:
        "What is this...?"
        "This can’t be right.":
            "Is this some sort of mermaid magic?"
            "Whatever the reason may be, it's undeniable that this 'Prashadi' has Grandfather's face."

        "Is that actually him?":
            "Has he been living some kind of double life this entire time?"
            "But why would he kill his own kind?"
            "Regardless, it seems he is known as 'Prashadi' here."

    Pr "It appears she's been cursed as well."
    j "She's no normal fish, is she?"
    Pr "Precisely. This one is a human!"
    show jorunn hesitant
    j "What?"
    Pr "Your little friend here used to have legs. And a voice. Possibly even hair."
    Pr "A real human, she was."
    Pr "Before her body was stolen from her."
    "He knows! Just how much can this Prashadi see?"
    "If only I hadn't been stupid enough to fall for that sea witch's music..."
    j "A spell that can turn a human into a fish..."
    j "Why would anyone cast a spell like that?"
    Pr "Why don't we find out?"

    show mist:
        zoom 0.2667
    with dissolve
    "A mist begins to roll in and fill the cavern."

    "Then, a gentle coolness passes over me as it envelops my body."

    "Prashadi’s hands move like they're weaving something together from the water around us."

    "Is he casting a spell?"

    "No...this mermaid can’t possibly be Grandfather!"

    #BLACK SCENE
    scene bg black with fade
    "What’s happening to me?"
    "Grandfather...!"
    "Grandfather...! Hunter!"
    "..."
    Pr "Ah...From the depths, your true form emerges! Well, only partially."
    "I open my eyes."

    call ch2_follow_jorunn from _call_ch2_follow_jorunn

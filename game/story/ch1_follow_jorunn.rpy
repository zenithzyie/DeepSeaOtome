
#BRANCH - FOLLOW JORUNN
label ch1_followjorunn:
    $ followthief.grant()
    hide screen notify2
    hide thioran angry with moveoutleft
    show jorunn
    play music "audio/music_underwater.ogg" volume 1.0 fadeout 1.0
    $ config.side_image_tag = "june"
    "The thief seems to know his way around. Maybe he can get me out of this mess."
    "Alright, [y]! It's now or never!"
    "3...2...1!!"
    y "BLUBBB!!!!" with vpunch
    "With all the might I can muster, I push my way through the current."

    show jorunn glee:
        subpixel True
        pos (0.66, 1080) zoom 1.0
        linear 0.39 pos (0.45, 1914) zoom 2.0
    with Pause(0.39)
    show jorunn glee:
        pos (0.45, 1914) zoom 2.0

    "I can't stop! I crash into the scrappy boy's shoulder." with vpunch
    show jorunn sweat with dissolve
    uj "Huh?"
    y "Blub!!"
    "A deft hand snatches me up."
    show jorunn glee with dissolve
    uj "Oh, well this is new! Never had a fish come up to my net before."
    y "{i}Blub blub blub!!{/i}" with screenShake
    "Wait, hang on now! Please don't eat me!"
    "If only I could speak real words!"
    show jorunn neutral with dissolve
    "He squints at me for a moment."
    uj "Huh? What's this?"
    "His other hand plucks something from my fins."
    "Ouch!"
    "The thief holds whatever he plucked from me close to his face, inspecting it with a rather curious expression."
    uj "...!"
    "It takes me a moment to recognize it myself."
    "It looks like a shard of the glowing stones back from the siren's cave."
    "The shard he is holding suddenly crumbles to pieces."
    uj "Weird. This thing stinks of magic."

    #show jorunn glee:
        #subpixel True
        #pos (0.45, 1914) zoom 2.0
        #linear 0.30 pos (0.45, 2592) zoom 2.75
    #with Pause(0.30)
    #show jorunn glee:
        #subpixel True ypos 2592 zoom 2.75

    uj "Now that I think about it..."
    uj "So do you, little fishie!"
    y "Blub!!"
    uj "You're no normal fish, are you?"

    "A rumble echoes through the water as the currents become stronger." with screenShake
    "It feels like the sea storm is picking up even more!"

    #show jorunn glee:
        #subpixel True
        #pos (0.45, 2592) zoom 2.75
        #linear 0.32 pos (0.5, 1080) zoom 1.0
    #with Pause(0.32)
    #show jorunn glee:
        #pos (0.5, 1080) zoom 1.0

    uj "First thing's first, we'd better get out of here."
    "He places me on his shoulder under all his hair. It's surprisingly well covered."
    uj "Hang tight, okay? Once we get to the forest, we'll be safe from the worst of it."
    y "Blub...!"
    "He's not going to eat me!"
    "Thank goodness. Looks like I made the right choice after all."
    #scene bg sea
    #show kelp
    #show jorunn neutral
    #with dissolve
    hide jorunn with dissolve
    ny neutral fish "The thief swims forward at a steady pace, unbothered by the growing sea storm."

    menu:
        "I'm nested in the merman's hair..."
        "Try to look through.":
            #+1 jor
            "My curiosity wins over, and I swim forward to try to peer through the hair."
            "As if realizing my intentions, he angles his shoulders to give me a better view."
            "The foliage is thick here, tall plants towering over the both of us like massive trees."
            "With the storm muffled by the cover of the kelp forest, the swim almost feels...{w} peaceful."
            show jorunn glee with dissolve
            uj "It's pretty way out here, don't you think?"
            y "Blub!" 
            "I really wish I could take a picture of the ocean."
            uj "If we go a bit further out, you'll see my home."
            uj "But that's not important right now. We gotta get you fixed up first!"

        "Settle back.":
            "My exhaustion wins over and I lean back against the crook of his neck, desperate for a minute of rest."
            "It's surprisingly comfortable here."
            "If it bothers the merman he doesn't say anything about it."
            "..."

    show jorunn glee with dissolve
    j "I'm Jorunn, by the way! {w}Sorry, guess I should've said that earlier."
    "Jorunn...such strange names mermaids have."
    j "But you can call me Jor. That's what everyone else calls me too."
    j "Hey, you don't happen to have a name yourself, do you?"
    y "Blub!"
    "He's a rather talkative fellow, isn't he!"
    show jorunn neutral with dissolve
    j "Right. Can't talk and all that."
    "He sounds a bit disappointed that I can't reply."
    j "Don't worry. Miss Prash will know what to do with you. She's the master when it comes to all this magic stuff."
    j "And you look like magic stuff."
    "Miss Prash...?"
    "Is it possible? Is there another mermaid out there that can turn me human again?"
    show jorunn sweat with dissolve
    j "Or, uh, unless I'm losing it, and you're just a normal fish."
    j "I hope I'm not just talking to myself right now..."
    show jorunn neutral with dissolve
    y "Blub!!!"
    "Even so, he keeps swimming, content to keep me in his hair for the time being."
    "The storm rumbles on, and he quiets down to focus on the journey."
    "Left alone with my thoughts, my mind races every which way."
    "Am I the first human to experience the sea like this?"
    "I wish I had my camera. {w}But it wouldn't have survived the plunge..."
    "All those memories made with it must be gone now, lost to me just like my own body."
    "..."

#SCENE CHANGE? - Kelp Forest

    show jorunn glee with dissolve
    j "Almost there, little fishie! I hope you've been enjoying the ride so far."
    show jorunn neutral with dissolve
    "With that, he takes us into a cave, leaving the kelp forest behind."
#SCENE CHANGE - fade to black... or maybe it goes suddenly black?
    scene bg black with dissolve
    stop music fadeout 5.0
    y "...!"
    "The deeper we go, the darker it gets."
    "Grandfather told me stories of how dangerous it could be when all light leaves the world."
    "Sometimes the storms would roll in at night, stealing away the moon and turning the world pitch black."
    "I think this is what he must have meant."
    "I can't see anything in front of me at all."
    "The only signs that I'm alive are my own thoughts, and the feel of  Jorunn's steady swimming as he takes us deeper still."
    "As the darkness stretches on, I begin to feel anxious."

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
            "What was I thinking, trusting a merman?" 
            #show only if antimermaid:
            "His kind is the reason why I fell off Hunter's boat in the first place."
            
            "Anything could be in here, and I'm just letting him lead me to my doom."
            "Just when I think we're going to be wandering around in this dark void forever, something glimmers in the distance."

    j "And...here we are!"

#SCENE CHANGE - Prashadi's Cave
    play music bgm_prashCave

    "...!"

    scene bg prashadi cave:
        fit "contain"
    with dissolve

    $ config.side_image_tag = "june"
    "Are those...stars above us?"

    show jorunn glee with dissolve
    j "Miss Prash! Are you in here?"
    "Sure enough, what looks to be the night sky is shining above us, illuminating the entire cavern in a gentle glow."
    "The sky? How is this even possible? Does that mean there's air above us too?"
    "But we definitely swam deeper to get here."
    show jorunn sweat with dissolve
    j "Hello? Miss Prash?"
    j "..."
    j "Prashadi!!" with vpunch
    show jorunn neutral with dissolve
    "I'm not sure what to expect."
    "The mermaids in the Deep Market had long hair and shiny scales."
    "Maybe she will be similar to them?"
    show jorunn glee at right2 with move
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

    u "Now here's a face you don't see very often!"
    u "What brings you all the way down here, boy?"
    j "Did you miss me? I found something I think you'd like to see." 
    j "Take a look, Miss Prash!"
   
    "Jorunn pushes me towards 'Miss Prash', and I can only stare, dumbfounded."
    "That's Grandfather. That's him."
    "What in the world?"
    j "She had some kind of magic shards stuck in her fins."
    gpa "Well now..."
    "His hands carefully cup my body."

    #show jorunn neutral with dissolve
    #j "I tried to take them out, but they crumbled really easily..."

    menu:
        "This is..."
        "What kind of trick is this?":
            "Is this some sort of mermaid magic?"
            "Either way, it's undeniable that whoever I'm staring at has Grandfather's face."

        "Is that actually him?":
            "Has he been living some kind of double life this entire time?"
            "But why would he kill his own kind?"

    "Regardless, it seems he is known as Prashadi here."
    Pr "It appears she's been cursed as well."
    j "She's no normal fish, is she?"
    Pr "Precisely. This one is a human!"
    show jorunn sweat with dissolve
    j "What...?"
    Pr "Your little friend here used to have legs. And a voice. Possibly even hair."
    Pr "A real human, she was."
    Pr "Before her body was stolen from her."
    "He knows! Just how much can this Prashadi see?"
    "If only I hadn't been stupid enough to fall for that sea witch's music..."
    j "A spell that can turn a human into a fish..."
    j "Why would anyone cast a spell like that?"
    Pr "Why don't we find out?"

    "A spearkling mist begins to roll in and fill the cavern."
    "The water starts to feel heavy, like it's clinging to my fins as he begins."
    "His hands wave like they're weaving something together from the water around us."
    "It's an entirely foreign movement to me."
    "This merman cannot possibly be Grandfather."
    show mist:
        zoom 0.2667
    with dissolve
    "A strange, sparkling mist begins to envelop me."
    "My fins start to itch and tingle. I begin writhing in the thickening water with discomfort, bubbles spurting all around."
    "Before I can decide if the mist is safe, it gently carries me upward."
    "I'm being pulled towards the surface of the water."
    "The tingling in my fins grows stronger as the mist gets thicker. I can't see anything."
    "My whole fish body feels like it's being pulled apart then put back together in the same instant."
    "I squeeze my eyes shut. All I can do is hope I'm not about to drown."

    #BLACK SCENE
    scene bg black with fade

    "Grandfather...Hunter..."
    "Will they spend the rest of their years never knowing what happened to me after the storm?"
    "My face suddenly breaks the surface of the water, startling me from my thoughts, and I take a big gulp of air."
    "I begin to instinctively tread water. My legs feel like they are tied together, but they are still managing to keep me afloat."
    "All I can hear is the water lapping around my body."
    Pr "Ah...From the depths, your true form emerges! Well, only partially."
    "I open my eyes."

    jump ch2_follow_jorunn

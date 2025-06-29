
#BRANCH - FOLLOW JORUNN
label ch1_followjorunn:
    hide prince angry with moveoutleft
    show jorunn sweat
    play music "audio/music_underwater.ogg" volume 1.0 fadeout 1.0

    "The thief seems to know his way around. Maybe he can get me out of this mess. "
    "It's now or never!"
    "3...2...1!!"
    y "BLUBBB!!!!" with vpunch
    "With all the might I can muster I push my way through the current, leaving a trail of bubbles behind me."

    show jorunn glee:
        subpixel True
        pos (0.66, 1080) zoom 1.0
        linear 0.39 pos (0.45, 1914) zoom 2.0
    with Pause(0.39)
    show jorunn glee:
        pos (0.45, 1914) zoom 2.0

    "I can't stop! I crash into the scrappy boy's shoulder." with vpunch
    uj "Huh?"
    y "Blub!!"
    "Immediately, a deft hand snatches me up."
    uj "Oh, well this is new! Never had a fish come swimming up to my net before."
    "Wait, hang on now! Please don't eat me!"
    y "{i}Blub blub blub!!{/i}"
    "If only I could speak real words!"
    "I wriggle around in an attempt to catch his attention."
    show jorunn neutral with dissolve
    "He holds onto me but moves me around, inspecting me."
    uj "Huh? What's this?"
    "His other hand comes close and plucks something from my fins."
    "Ouch!"
    "The thief holds whatever he plucked from me close to his face, inspecting it with a rather curious expression."
    uj "...!"
    "It takes me a moment to recognize it myself."
    "It looks like a shard of the glowing stones back from the siren's cave. It must have gotten caught in my fins during my escape. I hadn't even noticed."
    "As he crushes the tiny shards between his fingers, thin trails of glowing light flow towards the growing storm."
    uj "Weird. This thing stinks of magic."

    show jorunn glee:
        subpixel True
        pos (0.45, 1914) zoom 2.0
        linear 0.30 pos (0.45, 2592) zoom 2.75
    with Pause(0.30)
    show jorunn glee:
        subpixel True ypos 2592 zoom 2.75

    "Then, gently, with the skill of someone who has handled many fish just like me, he brings me closer to his face."
    uj "Now that I'm looking, so do you, little fishie!"
    y "Blub!!"
    uj "You're no normal fish, are you?"

    "A rumble echoes through the water as the currents become stronger." with screenShake
    "It looks like the seastorm is picking up even more!"

    show jorunn glee:
        subpixel True
        pos (0.45, 2592) zoom 2.75
        linear 0.32 pos (0.5, 1080) zoom 1.0
    with Pause(0.32)
    show jorunn glee:
        pos (0.5, 1080) zoom 1.0

    uj "First thing's first, we'd better get out of here."
    "He places me on his shoulder, right under all his hair. It's surprisingly well covered."
    "The currents seem weaker from here, I feel as if I can stay here without ever coming to harm."
    uj "Hang tight, okay? Once we get home, the forest will cover us from the worst of the storm."
    y "Blub..!"
    "He's not going to eat me!"
    "The relief I feel is so strong that I feel my fins go weak. Thank goodness. Looks like I made the right choice after all."
    scene bg sea
    show kelp
    show jorunn neutral
    with dissolve
    ny neutral fish "The thief swims forward at a steady pace, seemingly unbothered by the growing seastorm."

    menu:
        "I'm nested in the thieving merman's hair..."
        "Try to look through.":
            #+1 jor
            "My curiosity wins over, and I swim forward a little to try to peer through the hair into the sea around us."
            "As if realizing my intentions, he seems to shift, angling me in a way that gives me a better view as he swims.."
            "The foliage is thick here, tall plants towering over the both of us like massive trees."
            "With the storm muffled by the cover of the kelp forest, the world around me feels different. The swim even feels peaceful."
            "Wow..."
            show jorunn glee with dissolve
            uj "It's pretty way out here, don't you think?"
            "I nod, even though he can't see it. I really wish I could take a picture of the ocean from here."
            uj "If we go a bit further out, you'll see my home. But that's not as important right now. We gotta get you fixed up!"

        "Settle back.":
            "My exhaustion wins over and I lean back against the crook of his neck, desperate for a minute of rest."
            "If it bothers the merman he doesn't say anything about it."
            "It's oddly comforting."
            "It feels quite nice to rest against his soft hair."

    show jorunn neutral with dissolve
    "I begin to zone out from exhaustion when he speaks again."
    show jorunn glee with dissolve
    j "I'm Jorunn, by the way! {w}Sorry, guess I should've said that earlier."
    "Jorunn...what strange names merfolk have."
    j "But you can call me Jor. That's what my family calls me too."
    j "Hey, you don't happen to have a name yourself, do you?"
    y "Blub!"
    "He's a rather talkative fellow, isn't he!"
    show jorunn neutral with dissolve
    j "Right. Can't talk and all that."
    "He sounds almost a bit disappointed that I can't reply."
    j "Don't worry. Miss Prash will know what to do with you. She's the master when it comes to all this magic stuff."
    j "And you look like magic stuff."
    "Miss Prash..?"
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
    "I wish I had my camera. {w}But it wouldn't survive the plunge..."
    "All those memories made with it must be gone now, lost to me just like my own body."
    "I hope it somehow escaped my fate..."

#SCENE CHANGE? - Kelp Forest

    "The chatty merman swims onward, and I watch as the kelp forest grows thicker and eventually large rocky formations begin to jut out of the ground."
    show jorunn glee with dissolve
    j "Almost there, little fishie! I hope you've been enjoying the ride so far."
    show jorunn neutral with dissolve
    "With that, he takes us both into one of the holes in the rocks, leading to a cave."
#SCENE CHANGE - fade to black... or maybe it goes suddenly black?
    scene bg black with dissolve
    stop music fadeout 5.0
    ny neutral fish "The deeper we go, the darker it gets."
    "Grandfather told me stories of how dangerous it could be when all light leaves the world."
    "Sometimes the storms would roll in at night, stealing away the moon and turning the world pitch black."
    "I think this is what he must have meant."
    "I can't see anything in front of me at all."
    "The only signs that I'm alive are my own thoughts, and the feel of  Jorunn's steady swimming as he takes us deeper still."
    "What kind of merperson even lives in a place like this?"
    "As the darkness stretches on, I begin to feel anxious."

    menu:
        "I'm sure it will be alright.":
            $ promermaid += 1
            "No... I came this far already. I can't lose hope here."
            "At the end of his stories, Grandpa always came back home safe."
            "I have to trust that I can do the same."

        "I'm regretting trusting him.":
            $ antimermaid += 1
            "Maybe I made the wrong decision following him..."
            "What was I thinking, trusting a merman? His kind is the reason why I fell off Hunter's boat in the first place."
            "Anything could be in here, and I'm just letting him lead me into my doom."

    "Just when I think we're going to be wandering around in this dark void forever, something glimmers in the distance."

#SCENE CHANGE - Prashadi's Cave
    play music bgm_prashCave

    j "And...here we are!"
    "The tight tunnel walls give away into an open clearing."
    "...!"
    scene bg prashadi cave with dissolve:
        zoom 0.2667
    ny neutral fish "It's a large cavern."

    $ config.side_image_tag = "june"

#    show prashadi neutral:
#        zoom 2
#        ypos 2610

#    show prashadi neutral:
#        subpixel True
#        pos (0.5, 1410) zpos 0.0 xzoom 1.0 zoom 1.0
#        linear 3.08 pos (0.5, 1110) zpos 0.0 xzoom 1.0 zoom 0.79

#    show prashadi neutral:
#        pos (0.5, 1110) zpos 0.0 xzoom 1.0 zoom 0.79

    "And are those...stars above us?"
    show jorunn glee with dissolve
    j "Miss Prash! Are you in here?"
    "Sure enough, what looks to be the night sky is shining above us, illuminating the entire cavern in a gentle glow."
    "How is this even possible? The sky? Does that mean there's air above us too?"
    "But we definitely swam deeper down to get here."
    show jorunn sweat with dissolve
    j "Hello? Miss Prash?"
    j "..."
    j "Prashadi!! I'm back!" with vpunch
    show jorunn neutral with dissolve
    "I'm not sure what to expect."
    "I think back to the mermaids in the black market with their long hair and shiny scales."
    "Maybe she will be similar to them?"
    show jorunn glee at right2 with move 
    u "Ah, you've made it back, Jor! Did you find anything good today?"
    "The voice speaks, and it sounds heart-wrenchingly familiar."
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
    j "I found something really interesting! Take a look, Miss Prash!"
    "Jorunn pushes me towards 'Miss Prash', and I can only stare, dumbfounded."
    "That's Grandfather. That's him."
    "But Jorunn is still calling him 'Miss Prash.'"
    "What in the world?"
    j "She had some kind of magic shards stuck in her fins."
    show jorunn neutral with dissolve
    j "I tried to take them out, but they crumbled really easily..."
    gpa "Well now, that is interesting!"

    menu:
        "Grandfather is a mermaid. This is..."
        "Ridiculous. That can't be possible.":
            "But...it's undeniable that whoever I'm seeing now has Grandfather's face."
            "I don't even know what to think."

        "Have I been lied to this whole time?":
            "He hunted mermaids even as he himself was one?"
            "How could this be?"

    "Regardless, it seems he is known as Prashadi here."
    "Grandfather..."
    gpa "It seems like she's been cursed as well."
    j "Who would curse a cute little fish like this?"
    gpa "Not fish. This one used to be human!"
    show jorunn sweat with dissolve
    j "Miss Prash, are you saying...?"
    gpa "Your little friend here used to have legs. And a voice. Possibly, even hair."
    gpa "A real human, she was."
    "Yes, that's right! It's [y], your granddaughter!"
    show jorunn glee with dissolve
    "Jorunn looks at me with sparkling eyes."
    j "Are you able to turn her back?"
    gpa "Let me get a closer look."
    "Prashadi swims closer to me, and I can see more of this figure with Grandfather's face."
    "I stare at him, hoping to somehow get him to recognize me, but he ignores me in favor of making strange hand movements."
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
    "All I can do is hope I'm not about to drown."

    #BLACK SCENE
    scene bg black with fade

    "Grandpa...Hunter..."
    "Will they spend the rest of their years never knowing what happened to me after the storm?"
    "My face suddenly breaks the surface of the water, startling me from my thoughts, and I take a big gulp of air."
    "I begin to instinctively tread water. My legs feel like they are tied together, but they are still managing to keep me afloat."
    "All I can hear is the water lapping around my body."
    Pr "Ah... From the depths, your true form emerges! Well, only partially."
    "I open my eyes."

    #PRASH CAVE

    #"The mist has dissipated, and all that is left is me and the effects of Prashadi's spell."

    #SCENE CHANGE - fade to black

    jump endofdemo

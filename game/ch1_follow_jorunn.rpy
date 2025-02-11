

label ch1_followjorunn:
    #BRANCH - FOLLOW JORUNN
    hide prince angry with moveoutleft

    "The thief seems to know his way around. Maybe he can get me out of this mess. "
    "It's now or never!"
    "3... 2... 1!!"
    y "BLUBBB!!!!" with vpunch
    "With all the might I can muster I push my way through the current, leaving a trail of bubbles behind me."
    show jorunn sweat:
        subpixel True 
        pos (0.6, 790) zoom 1.0 
        linear 0.33 pos (0.5, 1522) zoom 2.5 
    with Pause(0.43)
    show jorunn sweat:
        pos (0.5, 1522) zoom 2.5 
    "I can't stop! I crash into the scrappy boy's shoulder."
    j "Huh?"
    y "Blub!!"
    "Immediately, a deft hand snatches me up."
    show jorunn glee:
        subpixel True 
        ypos 1522 zoom 2.5 
        linear 0.20 ypos 790 zoom 1.0 
    with Pause(0.30)
    show jorunn glee:
        ypos 790 zoom 1.0 
    j "Oh, well this is new! Never had a fish come swimming up to my net before."
    "Wait, hang on now! Please don't eat me!"
    y "Blub blub blub!!"
    "If only I could speak real words!"
    "I wriggle around in an attempt to catch his attention."
    show jorunn neutral
    "He holds onto me but moves me around, like he's appraising what my value at a pawn shop would be."
    j "Huh? What's this?"
    "His other hand comes close and plucks something from my fins."
    y "Blub!"
    "Ouch!"
    "The thief holds whatever he plucked from me close to his face, inspecting it with a rather curious expression."
    j "...!"
    "It takes me a moment to recognize it myself."
    "It looks like a shard of the glowing stones back from the siren's cave. It must have gotten caught in my fins during my escape. I hadn't even noticed."
    "As he crushes the tiny shards between his fingers, thin trails of glowing light flow towards the growing storm."
    j "Weird. This thing stinks of magic."
    show jorunn neutral:
        subpixel True 
        pos (0.5, 790) zoom 1.0 
        linear 0.33 pos (0.45, 1660) zoom 2.5 
    with Pause(0.43)
    show jorunn neutral:
        pos (0.45, 1660) zoom 2.5 

    "Then, gently, with the skill of someone who has handled many fish just like me, he brings me closer to his face."
    j "Now that I'm looking, so do you, little fishie!"
    y "Blub!!"
    j "You're no normal fish, are you?"

#(Screenshake)

    "A rumble echoes through the water as the currents become stronger."
    "It looks like the seastorm is picking up even more!"
    j "First thing's first, we'd better get out of here."
    "He places me on his shoulder, right under all his hair. It's surprisingly well covered."
    "The currents seem weaker from here, I feel as if I can stay here without ever coming to harm."
    j "Hang tight, okay? Once we get home, the forest will cover us from the worst of the storm."
    y "Blub..!"
    "He's not going to eat me!"
    "The relief I feel is so strong that I feel my fins go weak. Thank goodness. Looks like I made the right choice after all."
    "The thief swims forward at a steady pace, seemingly unbothered by the growing seastorm."

    menu:
        "I'm nested in Jorunn's hair..."
        "Try to look through.":
            #+1 jor
            "My curiosity wins over, and I swim forward a little to try to peer through the hair into the sea around us."
            "As if realizing my intentions, he seems to shift, angling me in a way that gives me a better view as he swims.."
            "The foliage is thick here, tall plants towering over the both of us like massive trees."
            "With the storm muffled by the cover of the kelp forest, the world around me feels different. The swim even feels peaceful."
            "Wow..."
            show jorunn glee
            j "It's pretty way out here, don't you think?"
            "I nod, even though he can't see it. I really wish I could take a picture of the ocean from here."
            j "If we go a bit further out, you'll see my home. But that's not as important right now. We gotta get you fixed up!"

        "Lean back.":
            "My exhaustion wins over and I lean back against the crook of his neck, desperate for a minute of rest."
            "If it bothers the merman he doesn't say anything about it."
            "It's oddly comforting."
            "It feels quite nice to rest against his soft hair."

    show jorunn neutral
    "I begin to zone out from exhaustion when he speaks again."
    show jorunn glee
    j "I'm Jorunn, by the way! {w}Sorry, guess I should've said that earlier."
    "Jorunn... what strange names merfolk have."
    j "But you can call me Jor. That's what my family calls me too."
    j "Hey, you don't happen to have a name yourself, do you?"
    y "Blub!"
    "He's a rather talkative fellow, isn't he!"
    show jorunn neutral
    j "Right. Can't talk and all that."
    "He sounds almost a bit disappointed that I can't reply."
    j "Don't worry. Miss Prash will know what to do with you. She's the master when it comes to all this magic stuff."
    j "And you look like magic stuff."
    "Miss Prash..?"
    "Is it possible? Is there another mermaid out there that can turn me human again?"
    j "Or, uh, unless I'm losing it, and you're just a normal fish."
    show jorunn pissed
    j "I hope I'm not just talking to myself right now..."
    show jorunn neutral
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
    show jorunn glee
    j "Almost there, little fishie! I hope you've been enjoying the ride so far."
    show jorunn neutral
    "With that, he takes us both into one of the holes in the rocks, leading to a cave."
#SCENE CHANGE - fade to black... or maybe it goes suddenly black?

    "The deeper we go, the darker it gets."
    "When I was younger, grandfather would tell me stories of his hunting trips out at sea. Of how dangerous it could be when all light left the world. "
    "Sometimes the storms would roll in at night, stealing away the moon and turning the world pitch black."
    "I think this is what he must have meant."
    "I can't see anything in front of me at all."
    "The only signs that I'm alive are my own thoughts, and the feel of  Jor's steady swimming as he takes us deeper still."
    "What kind of merperson even lives in a place like this?"
    "As the darkness stretches on, I begin to feel anxious."

    menu:
        "I'm sure it will be alright.":
            "No... I came this far already. I can't lose hope here."
            "At the end of his stories, Grandpa always came back home safe."
            "I have to trust that I can do the same."

        "I'm regretting trusting him.":
            "Maybe I made the wrong decision following him..."
            "What was I thinking, trusting a merman? His kind is the reason why I fell off Hunter's boat in the first place."
            "Anything could be in here, and I'm just letting him lead me into my doom."
            "Just when I think we're going to be wandering around in this dark void forever, something glimmers in the distance."

    "Just when I think we're going to be wandering around in this dark void forever, something glimmers in the distance."

#SCENE CHANGE - Prashadi's Cave

    j "And... here we are!"
    "The tight tunnel walls give away into an open clearing."
    "...!"
    "It's a large cavern."

    scene testprash:
        zoom 0.2667
    $ config.side_image_tag = "june"
    "hmm"
    show prashadi neutral
    with dissolve
    y neutral fish "Hi grandpa!!!"
    show prashadi neutral:
        zoom 2
        ypos 2610
    "wow"

    show prashadi neutral:
        subpixel True
        pos (0.5, 1410) zpos 0.0 xzoom 1.0 zoom 1.0
        linear 3.08 pos (0.5, 1110) zpos 0.0 xzoom 1.0 zoom 0.79
    with Pause(3.18)
    show prashadi neutral:
        pos (0.5, 1110) zpos 0.0 xzoom 1.0 zoom 0.79

    "YEAH BABY"

    show prashadi neutral:
        ypos 888 xzoom 1.0 zoom 0.61

    "And are those... stars above us?"
    j "Miss Prash! Are you in here?"
    "Sure enough, what looks to be the night sky is shining above us, illuminating the entire cavern in a gentle glow."
    "How is this even possible? The sky? Does that mean there's air above us too?"
    "But we definitely swam deeper down to get here."
    j "Hello? Miss Prash?"
    j "..."
    j "Prashadi!! I'm back!" with vpunch
    "According to Jorunn's description, this Prashadi is a beautiful person."
    "I'm not sure what to expect."
    "I think back to the mermaids in the black market with their long hair and shiny scales."
    "Maybe she will be similar to them?"
    u "Ah, you've made it back, Jor! Did you find anything good today?"
    "The voice speaks, and it sounds heart-wrenchingly familiar."
    "A figure swims into view from the darker recesses of the cave."

    #(a flash of grandpa's sprite here)

    "Grandfather!?"
    j "I found something really interesting! Take a look, Miss Prash!"
    "Jorunn pushes me towards 'Miss Prash', and I can only stare, dumbfounded."
    "That's Grandfather. That's him."
    "But Jorunn is still calling him ‘Miss Prash.'"
    "What in the world?"
    j "She had some kind of magic shards stuck in her fins."
    j "I tried to take them out, but they crumbled really easily..."
    gpa "Well now, that is interesting!"

    menu:
        "Grandfather is a mermaid. This is..."
        "Ridiculous. That can't be possible.":
            "But... it's undeniable that whoever I'm seeing now has Grandfather's face."
            "I don't even know what to think."

        "Have I been lied to this whole time?":
            "He hunted mermaids even as he himself was one?"
            "How is this even possible?"

    "Regardless, it seems he is known as Prashadi here."
    "Grandfather..."
    Pr "It seems like she's been cursed as well."
    j "Who would curse a cute little fish like this?"
    Pr "Not fish. This one used to be human!"
    j "Miss Prash, are you saying...?"
    Pr "Your little friend here used to have legs. And a voice. Possibly, even hair."
    Pr "A real human, she was."
    "Yes, that's right! It's [y], your granddaughter!"
    "Jorunn looks at me with sparkling eyes."
    j "Are you able to turn her back?"
    Pr "Let me get a closer look."
    "Prashadi swims closer to me, and I can see more of this figure with Grandfather's face."
    "I stare at him, hoping to somehow get him to recognize me, but he ignores me in favor of making strange hand movements."
    "The water starts to feel heavy, like it's clinging to my fins as Prashadi begins."
    "His hands wave like they're weaving something together from the water around us."
    "It's an entirely foreign movement to me."
    "This merman cannot possibly be Grandfather."
    "A strange, sparkling mist begins to envelop me."
    "My fins start to itch and tingle. I begin writhing in the thickening water with discomfort, bubbles spurting all around."
    "Before I can decide if the mist is safe, it gently carries me upward."
    "I'm being pulled towards the surface of the water."
    "Wait... I can't breathe out of water like this!"
    "The tingling in my fins grows stronger as the mist gets thicker. I can't see anything."
    "My whole fish body feels like it's being pulled apart then put back together in the same instant."
    "All I can do is squeeze my eyes shut and hope I'm not about to drown."

    #BLACK SCENE

    "Grandpa... Hunter..."
    "Will they spend the rest of their years never knowing what happened to me after the storm?"
    "My face suddenly breaks the surface of the water, startling me from my thoughts, and I take a big gulp of air."
    "I begin to instinctively tread water. My legs feel like they are tied together, but they are still managing to keep me afloat."
    "All I can hear is the water lapping around my body."
    Pr "Ah... From the depths, your true form emerges! Well, only partially."
    "I open my eyes."

    #PRASH CAVE

    "The mist has dissipated, and all that is left is me and the effects of Prashadi's spell."

    #SCENE CHANGE - fade to black

    jump endofdemo

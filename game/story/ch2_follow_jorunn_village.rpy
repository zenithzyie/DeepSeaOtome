label ch2_jorunn_village:
##This is the continuation of Follow Jorunn after leaving Prashadi's cave

    scene bg black:
        fit "contain"
    pause 0.7

    "The tunnels are as dark as my first trip through them. I feel a bit more courageous knowing that I have a plan now."

    "We reach the end of the cave and I can see the light spilling out from the exit."

    #SCENE CHANGE - sea wilderness
    scene bg sea with dissolve
    play music "audio/music_underwater.ogg" volume 1.0 fadeout 1.0

    "It's a relief to be back out into the ocean. The darkness was starting to make me uncomfortable."

    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve

    #hand check
    "I let go of Jorunn's hand and follow him through the water."

    j "I should probably mention that the village doesn't get too many visitors these days. They might have some questions for you."

    y mermaid neutral "Oh, right. What should I say?"

    y nervous "I need to be careful. They can't know I'm human."

    #Anti mermaid:
    if antimermaid >= 1:
        "Who knows what they could do to me?"

    # Pro mermaid:
    if promermaid >= 1:
        "I don't think they'd be too happy about that."

    j "How about this - we could say you're a traveling trader! They used to come by pretty often before the storms got worse."

    y happy "Oh, a trader?"

    y nervous "But...{w} Do I look the part? I don't have anything I could trade."

    j "Just say you lost your goods in the storm, easy. I'll back you up!"

    menu:
        "\"Alright!\"":
            $ jorunn_points += 1
            y "I'll give it my best shot."
            j "That's the spirit!"

        "\"Are you sure?\"":
            y "What if they don't believe me?"
            j "They will! Trust me."

    "We keep swimming until the kelp gives way to a clearing."

    scene bg jorvillage afternoon:
        align (0.5, 1.0)
        pos (0.5, 1.64)
        zoom 0.34
    with dissolve

    window auto hide
    show bg jorvillage afternoon:
        linear 6 pos (0.5, 1.0) zoom 0.34
    with Pause(6.10)

    show bg jorvillage afternoon:
        pos (0.5, 1.0) zoom 0.34

    window auto show

    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve

    #village name needed
    j mermaid neutral "Here we are! Welcome to <village name here>."

    y shocked "Wow...!"

    ny "So this is what Jorunn's village looks like! I've never seen so many mermaids in one place before."

    "Large plant stalks cover the entire area. I wonder if they're protecting us from the storm?"

    if looked_through:
        "Large plant stalks cover the entire area. I wonder if they’re protecting us from the storm?"
        "The structures on them remind me of treehouses. That must be where the mermaids live."
    else:
        "The structures on the plant stalks remind me of treehouses. That must be where the mermaids live."

    ny sad "I wish I could take a picture of it..."

    "One of the villagers near the entrance swims up to us."

    show jorunn glee with dissolve
    j "Hey, mossyhead! It's good to see you. I'm back!"

    moss "Ugh. I told you not to call me that."

    moss "And who's this? Don't tell me you brought back another mouth to feed."

    y happy "It's nice to meet you. I'm [y]."

    j "She'll just be staying the night. Until the storm blows over, y'know."

    moss "What?"

    "His features immediately turn to suspicion."

    moss "You don't look like you're from these waters. What are you doing all the way out here?"

    #CONVINCE THE GUARD PUZZLE START
    menu convincestart:
        ny neutral "What do I tell him?"
        "\"I'm a traveling trader.\"":
            $ traderpick = True
            moss "Trading what? I don't see any wares on you."
            menu trader:
                "\"I just traded everything away.\"": #fail
                    $ failconvince += 1
                    moss "Everything? With whom?"
                    moss "We're the only village around here for days."
                    y "Uh, from further away."
                    "Mr. Mossyhead's frown deepens."
                    ny nervous "Oh dear, I don't think he bought it."
                    jump failedconvincemoss

                "\"I lost my wares in the storm.\"": #success
                    y "The currents took everything away before I could blink."
                    moss "...That so?"
                    j "I couldn't believe it at first either! At least we know you're not the only one who's lost their wares in a storm now, Mossy."
                    moss "Shut up about that, will you? It was one time."
                    j "You should have seen it, [y]!"
                    j "He made a big fuss about how he'd make the best trades, then came back empty-handed after losing everything! Haha."
                    y "Oh no...I guess that makes two of us."
                    moss "Ugh..."
                    jump succeedconvincemoss

                "\"I wanted to travel light.\"": #fail
                    $ failconvince += 1
                    y "A heavy pack would just slow me down."
                    moss "Right. A trader traveling light."
                    moss "How stupid do you think I am?"
                    y nervous "Er..."
                    "That sounded better in my head."
                    jump failedconvincemoss

        "\"I'm visiting from far away.\"":
            moss "How far, exactly?"
            menu faraway:
                "\"From the...mermaid capital?\"": #fail
                    $ failconvince += 1
                    moss "Visiting...{i}here?{/i} {w}   From the capital?"
                    moss "Why would you want to leave right when the festival's about to start?"
                    ny nervous "What festival? I just said the first thing that came to my mind!"
                    y "I guess I really didn't think it through...haha..."
                    moss "Clearly. I've seen children lie better than you."
                    "Well, that's embarrassing."
                    jump failedconvincemoss

                "\"Really really far away.\"": #fail
                    $ failconvince += 1
                    y "You wouldn't have heard of it."
                    moss "Try me."
                    y "But it's like super duper far away. Seriously far away."
                    y "It's like...twenty blue whales and a giant squid length...{w}away?"
                    moss "If you can't give a proper answer, you should just leave."
                    moss "Take your nonsense elsewhere."
                    ny nervous "That could've gone better..."
                    jump failedconvincemoss

                "\"Alaska.\"": #success
                    $ alaskapick = True
                    moss "A'lass Ka? Never heard of it."
                    y "Yes, exactly. It's {i}really{/i} far away."
                    j "Oh, yeah! It's supposed to be way north. You really oughta get out more often."
                    moss "Shut it!"
                    y nervous "I'm sorry to impose..."
                    y "It's just been a really long trip. I don't think I can keep traveling in the storm."
                    j "You're not going to turn her away, are you, Mossy?"
                    moss "..."
                    jump succeedconvincemoss

        "\"No clue. I have amnesia.\"":
            $ amnesiapick = True
            moss "You...what?"
            menu headinjury:
                "\"I just don't remember anything.\"": #fail
                    $ failconvince += 1
                    moss "...?"
                    y "It's true! All of my memories are gone."
                    moss "Do you think I have fish for brains? If you're going to talk nonsense, you can leave."
                    ny nervous "I was so sure that would work!"
                    jump failedconvincemoss

                "\"I hit my head real bad in the storm.\"": #success
                    j "It's true! I found her passed out on a rock."
                    y "I have proof! There's a bump on my head!!"
                    y "Do you want to see it?"
                    moss "I really don't."
                    j "It's a nasty bump! I thought she was dead when I found her!"
                    y sad "Ouch...it hurts just thinking about it."
                    moss "Ugh..."
                    jump succeedconvincemoss

                "\"I'm trying to remember who I was by visiting lots of different places.\"": #fail
                    $ failconvince += 1
                    moss "And you thought a village way out here would help?"
                    y "Maybe I've been here before and I just don't remember!"
                    moss "You haven't."
                    moss "We would remember someone using such a terrible excuse."
                    "That usually goes better in the movies..."
                    jump failedconvincemoss

    # JOR FAIL SAVE

label failedconvincemoss:
    show jorunn neutral with dissolve
    j "Okay, fine. You're right. That isn't why she's here."
    j "The real reason is..."
    show jorunn flustered with dissolve
    "Jorunn suddenly reaches over and grabs my hand."
    j "...[y] and I are lovers!!!" with screenShake
    moss "What?"
    ny flustered "What is he doing??"
    j "We didn't want to cause a fuss or anything, but we've been seeing each other for a while!"
    show jorunn flustered with dissolve
    moss "{i}What?{/i}"
    j "You're not gonna tell anyone, are you Mossy? We're not ready to tell my family yet!"
    moss "I...uh..."
    moss "L-lover or not, I'll kick you out the moment you cause any trouble, you hear?"
    y nervous "Pardon? I won't cause any trouble."
    moss "Damnit...!! Whatever! You owe me for this!"
    "He swims away from us in a hurry."
    "But...isn't he supposed to be watching the gate?"
    "..."
    show jorunn neutral with dissolve
    "Following Jorunn's lead, we swim further into the village."
    j "Whew. Guess you're the type who likes to do things her own way, huh?"

    menu:
        "\"Sorry, I panicked.\"":
            j "Well, it happens to the best of us."
            j "Let's try to work together from now on though, yeah?"
            y "Right..."

        "\"I wasn't sure your idea was going to work.\"":
            j "..."
            j "Let's try to work together from now on, yeah?"
            y "Right..."

    jump jorshouse

    #AFTER SUCCESSFUL CONVO (FINALLY)
label succeedconvincemoss:
    moss "Whatever. Just don't cause any trouble."
    show jorunn glee with dissolve
    j "Yep! Thanks, Mossy!"
    ny happy "I can't believe that worked."
    "Following Jorunn's lead, we swim further into the village."

    # picked Jor's suggestion (Trader)
    if traderpick:
        show jorunn glee with dissolve
        j "Hehe. Nice job, [y]. You've got a knack for this kind of stuff, huh?"
        menu:
            "\"Well, I couldn't have done it without your advice.\"":
                "Jorunn gives me a big wink."

            "\"Haha, maybe I do.\"":
                $ jorunn_points += 2
                y "You could say I was made for the stage!"
                "Jorunn gives me a playful bow."
                j "Our star of the sea! It was an honor to share the stage with you."
                y "Hehe."

    # pass Amnesia check
    if amnesiapick:
        show jorunn glee with dissolve
        j "Well, that's not exactly what I had in mind, but it worked out pretty well!"
        y "Thank you for backing me up, Jorunn."
        j "Sure thing!"
        j "We gotta stick together, yeah?"


    #pass Alaska check
    if alaskapick:
        show jorunn glee with dissolve
        j "Well, that's not exactly what I had in mind, but it worked out pretty well!"
        y "Thank you for backing me up, Jorunn."
        j "Sure thing!"
        j "We gotta stick together, yeah?"
        "..."
        j "So, what is Alaska, anyway?"
        y "Oh, it's a fictional place!"
        y "My grandfather used to tell me stories about it as a child."
        j "Really? The name sounds pretty interesting. Too bad it's not real."

    #SCENE CHANGE - Jorunn's House

label jorshouse:

    scene bg jorbedroom with fade:
        fit "contain"
    "We stop at the entrance to one of the homes."

    show jorunn glee at jorunn_center

    j mermaid neutral "Well, here we are!"

    u "Jor?"

    "A younger mermaid swims up to us from the inside. She looks relieved to see Jorunn."

    u "There you are."

    j "Hey, Unna! I'm back!"

    unna "I wasn't sure if you were going to make it back in time with the storm."

    j "Aw, come on, as if a little current like that could stop me."

    unna "And- oh, hello! Who's this with you?"

    j "This is [y]. Found her all caught up in the storm outside. She'll be staying the night 'til it passes over."

    y happy "It's nice to meet you- Unna, is it?"

    unna "Yeah, you got it! I haven't seen clothes like yours around here before. The storm must have carried you a long way, huh?"

    y "Haha...you could say that. Thank you for having me."

    "She seems much friendlier than Mr. Mossyhead."

    j "Where's Parvy? Have you two eaten yet?"

    unna "Not yet. We were hoping to eat together with you."

    "As if on cue, a small figure swims out of the undergrowth to greet us."

    parvy "...Hi, Jor."

    j "There she is!"

    if childrenplaying:
        # Pro mermaid:
        if promermaid >= 1:
            "I can't help but smile. I've never seen a mermaid so small before."
            "She reminds me of the children I saw in Aquantis."

    "The three of them all look so much alike."

    menu:
        ny neutral "I wonder..."
        "\"Are they your siblings, Jorunn?\"":
            j "Nope, found them in a basket one day when I was out for a swim!"
            y "Oh, really? What a coincidence! They look just like you."
            j "Don't they though? Haha, I'm just kidding. They're my sisters."
            y "Of course."

        "\"Are they your children, Jorunn?\"":
            $ jorunn_points += 1
            j "Hmm? Oh, sure are! Carried them in my belly and everything."
            y shocked  "Really?"
            parvy "Ew! Gross!"
            j "Haha! No, just messing with you. These are my younger siblings."
            y happy "Of course, haha."

    parvy "...what kind of mer are you?"

    "Parvy circles me with a surprising amount of intensity."

    ny nervous "She can't tell I'm not actually a mermaid, can she?"

    y neutral "Oh, well, my name is-"

    parvy "Are you from the capital? Is that the kind of clothes they wear there? I heard they live in houses made from rocks!"

    j "Alright you busybug, let's give our guest some space. She's had a long day."

    parvy "Guh..."

    j "You must be pretty hungry too, huh, [y]? Let's go get some food, yeah?"

    y happy "That sounds wonderful."

    scene bg jorvillage afternoon:
        align (0.5, 1.0)
        pos (0.5, 1.64)
        zoom 0.34
    with dissolve

    "I follow the family upwards towards a platform on top of the homes."

    "Everyone quickly gets to work preparing the fish Jorunn brought back."

    y mermaid neutral "Is there anything I can help with?"

    unna "Ah, don't worry about it, you're our guest! Go ahead and make yourself comfortable, we'll be done soon."

    "Unna hands a basket over to Jorunn, who starts sorting through its contents."

    "It's obvious this is something they've done together many times."

    "..."

    # Pro mermaid:
    if promermaid >= 1:
        "Did the mermaids in the underground market have families like this? Did they eat like this too?"

    #Anti mermaid:
    if antimermaid >= 1:
        "It's curious to see mermaids acting like this. It makes them feel so...human."

    "..."

    parvy "Here."

    "Parvy hands me a bowl. She seems quite intent on sticking by my side."

    y happy "Oh, thank you!"

    j "I'm sure it's not what you're used to, but help yourself to what you want!"

    ny neutral "Right...this is my first meal as a mermaid."

    "Where do I even start? There's a whole spread laid out-leafy greens, some things that look like fruit, and fish."

    ny nervous "Hang on...aren't those the same fish Jorunn stole from the prince?"

    "Oh dear. {w} Well, here goes nothing."

    #show text line is for debugging purposes, but might be useful for the player too
    menu makefood:
        ny happy "What should I add to my bowl?"
        "Leafy Greens":
            $ greens += 1
            $ addfood += 1
            if greens == 1:
                "I add some greens to the bowl. If you look at it from here, it kind of looks like lettuce."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if greens == 2:
                "I add more greens to the bowl. My meal is starting to look like a salad."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if greens == 3:
                "I add even more greens to the bowl. Being surrounded by sea plants must have really made me crave some greens."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                jump makefood

        "Sea Fruit?":
            $ fruit += 1
            $ addfood += 1
            if fruit == 1:
                "I add some blue fruits to the bowl. I bet they'll taste berry good."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fruit == 2:
                "I add another fruit to the bowl. These are smooth and yellow. They'll pear nicely with the blue fruits."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fruit == 3:
                "I add one last kind of fruit to the bowl. My bowl looks grape! Fruitful, even. How very a-peeling."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                jump fooddone

        "Fish":
            $ fish += 1
            $ addfood += 1
            if fish == 1:
                "I add some fish to the bowl. They've been filleted rather neatly."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fish == 2:
                "I add more fish to the bowl. This meal is starting to look rather fishy."
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fish == 3:
                "I finish off the bowl with even more fish. I'm still not sure what kind of fish this is. Oh well!"
                show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                jump fooddone

    label fooddone:

    #Bowl Outcomes

    #One of each
    if greens == 1 and fruit == 1 and fish == 1:
        "This is a nice, well-rounded meal."
        "It seems Unna chose the same as me. I guess she isn't much of a picky eater."

    #Two leafy greens
    if greens == 2:
        "I've made a bowl filled with leafy greens."

    #Three leafy greens
    if greens == 3:
        "There could not be more green in this meal. This is a salad bowl to end all salad bowls."
        "It seems Jorunn chose the same as me. I wonder if he's a picky eater?"

    #Two fruit
    if fruit == 2:
        "I've made a bowl filled with fruit."

    #Three fruit
    if fruit == 3:
        "These fruits are singing a three-part harmony in my mouth!"

    #Two fish
    if fish == 2:
        "I've made a bowl with lots of fish."
        "It seems Parvy chose the same as me. She looks pretty pleased to see my bowl."

    #Three fish
    if fish == 3:
        "The fish fillets are staring at me from inside the bowl."
        "...Why did I add so much fish?"
        show jorunn glee with dissolve
        j "..."

    #No fish
    if fish == 0:
        if greens > fruit:
            $ jorunn_points += 1
            j "Guess you're a fan of greens, huh?"
        if fruit > greens:
            $ jorunn_points += 1
            j "Guess you're a fan of fruits, huh?"

        y "Well...you could say I've had enough fish to last me a lifetime."

        j "Hehe, I don't care for fish either."


    #WRAP MEAL END
    hide text
    "Time passes, and we finish eating."

    y "Thank you for the meal. That was delicious."

    j "Right? Unna is such an amazing cook, aren't you?"

    "He rubs Unna's hair affectionately."

    show unna blushing

    unna "..."



    jump endofdemo

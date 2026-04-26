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

    scene bg jorvillage:
        align (0.5, 1.0)
        pos (0.5, 1.64)
        zoom 0.34
    with dissolve

    window auto hide
    show bg jorvillage:
        linear 6 pos (0.5, 1.0) zoom 0.34
    with Pause(6.10)

    show bg jorvillage:
        pos (0.5, 1.0) zoom 0.34

    window auto show
    "test"
    show jorunn neutral at jorunn_center
    ny mermaid shocked "WOW"

    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve

    #village name needed
    j mermaid neutral "Here we are! Welcome to <village name here>."

    y shocked "Wow...!"

    ny "So this is what Jorunn's village looks like! I've never seen so many mermaids in one place before."

    "Large plant stalks cover the entire area. I wonder if they're protecting us from the storm?"

    "The structures on them remind me of treehouses. That must be where the mermaids live."

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
                set menuset
                "\"I just traded everything away.\"": #fail
                    $ failconvince += 1
                    moss "Everything? With whom?"
                    moss "We're the only village around here for days."
                    y "Uh, from farther away."
                    "Mr. Mossyhead's frown deepens."
                    ny nervous "Oh dear, I don't think he bought it."
                    jump trader

                "\"I lost my wares in the storm.\"": #success
                    y "The currents took everything away before I could blink."
                    moss "...That so?"
                    j "I couldn't believe it at first either! At least we know you're not the only one who's lost their wares in a storm now, Mossy."
                    moss "Shut up about that, will you? It was one time."
                    j "You should have seen it, [y]!"
                    j "He made a big fuss about how he'd make the best trades, then came back empty-handed after losing everything! Haha."
                    y "Oh no...I guess that makes two of us."
                    moss "Ugh..."
                    pass

                "\"I wanted to travel light.\"": #fail
                    $ failconvince += 1
                    y "A heavy pack would just slow me down."
                    moss "Right. A trader traveling light."
                    moss "What stupid do you think I am?"
                    y nervous "Er..."
                    "That sounded better in my head."
                    jump trader

        "\"I'm visiting from far away.\"":
            moss "How far, exactly?"
            menu faraway:
                set menuset
                "\"From the...mermaid capital?\"": #fail
                    $ failconvince += 1
                    moss "Visiting...{i}here?{/i} {w}   From the capital?"
                    moss "Why would you want to leave right when the festival's about to start?"
                    ny nervous "What festival? I just said the first thing that came to my mind!"
                    y "I guess I really didn't think it through...haha..."
                    moss "Clearly. I've seen children lie better than you."
                    "Well, that's embarrassing."
                    jump faraway

                "\"Really really far away.\"": #fail
                    $ failconvince += 1
                    y "You wouldn't have heard of it."
                    moss "Try me."
                    y "But it's like super duper far away. Seriously far away."
                    y "It's like...twenty blue whales and a giant squid length...{w}away?"
                    moss "If you can't give a proper answer, you should just leave."
                    moss "Take your nonsense elsewhere."
                    "That could've gone better..."
                    jump faraway

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
                    pass

        "\"No clue. I have amnesia.\"":
            $ amnesiapick = True
            moss "You...what?"
            menu headinjury:
                set menuset
                "\"I just don't remember anything.\"": #fail
                    $ failconvince += 1
                    moss "...?"
                    y "It's true! All of my memories are gone."
                    moss "Do you think I have fish for brains? If you're going to talk nonsense, you can leave."
                    "I was so sure that would work!"
                    jump headinjury

                "\"I hit my head real bad in the storm.\"": #success
                    j "It's true! I found her passed out on a rock."
                    y "I have proof! There's a bump on my head!!"
                    y "Do you want to see it?"
                    moss "I really don't."
                    j "It's a nasty bump! I thought she was dead when I found her!"
                    y sad "Ouch...it hurts just thinking about it."
                    moss "Ugh..."
                    pass

                "\"I'm trying to remember who I was by visiting lots of different places.\"": #fail
                    $ failconvince += 1
                    moss "And you thought a village way out here would help?"
                    y "Maybe I've been here before and I just don't remember!"
                    moss "You haven't."
                    moss "We would remember someone using such a terrible excuse."
                    "That usually goes better in the movies..."
                    jump headinjury

    # JOR FAIL SAVE
    if failconvince > 1:
        show jorunn neutral with dissolve
        j "Okay, fine. You're right. That isn't why she's here."
        j "The real reason is..."
        "Jorunn suddenly reaches over and grabs my hand."
        j "...[y] and I are lovers!!!" with screenShake
        moss "What?"
        ny shocked "What is he doing??"
        j "We didn't want to cause a fuss or anything, but we've been seeing each other for a while!"
        show jorunn flustered with dissolve
        moss "{i}What?{/i}"
        j "You're not gonna tell anyone, are you Mossy? We're not ready to tell my family yet!"
        moss "I...uh..."
        moss "L-lover or not, I'll kick you out the moment you cause any trouble, you hear?"
        y "Pardon? I won't cause any trouble."
        moss "Damnit...!! Whatever! You owe me for this!"
        "He swims away from us in a hurry."
        "But...isn't he supposed to be watching the gate?"
        "..."
        "Following Jorunn's lead, we swim further into the village."
        pass

    #AFTER SUCCESSFUL CONVO (FINALLY)
    if failconvince < 1:
        moss "Whatever. Just don't cause any trouble."
        j "Yep! Thanks, Mossy!"
        ny happy "I can't believe that worked."
        "Following Jorunn's lead, we swim further into the village."


    # picked Jor's suggestion (Trader)
    if traderpick == True:
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
    if amnesiapick == True:
        show jorunn glee with dissolve
        j "Well, that's not exactly what I had in mind, but it worked out pretty well!"
        y "Thank you for backing me up, Jorunn."
        j "Sure thing!"
        j "We gotta stick together, yeah?"


    #pass Alaska check
    if alaskapick == True:
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

    #fails the check
    #HELP WHAT VARIABLE GOES HERE
        j neutral "Whew. Guess you're the type who likes to do things her own way, huh?"

        menu:
            "\"Sorry, I panicked.\"":
                j "Well, it happens to the best of us."
                j "Let's try to work together from now on though, yeah?"
                y "Right..."

            "\"I wasn't sure your idea was going to work.\"":
                j "..."
                j "Let's try to work together from now on, yeah?"
                y "Right..."

    #SCENE CHANGE - Jorunn's House

    "We stop at the entrance to one of the homes."

    j "Home sweet home heehee."

    y happy "Your home is so pretty."

    "A younger mermaid is arranging items on a shelf nearby. She quickly looks up at our approach."

    u "Jor?"

    j "Hey, Unna! I'm back!"

    unna "Oh! And who's this with you?"

    j "This is [y]. Found her all caught up in the storm outside. She'll be staying the night 'til it passes over."

    y "It's nice to meet you- Unna, is it?"

    unna "You got it! It's nice to meet you too, [y]."

    unna "I'm glad you got out of that storm. They can get really nasty."

    unna "It's not much, but welcome to (JOR VILLAGE)."

    y "Thank you for having me."

    "She seems quite friendly, just like Jorunn. They must be family."

    j "Where's Parvy? We DINNER. NOOWWW."

    "A small figure suddenly shuffles over to us, lingering close to Jorunn."

    u "...hi, Jor."

    "She clings against Jorunn in a tight hug and his face lights up at the sight of her."

    u "I missed you."

    j "Hey there, Parvy! Lookit you!! Did you get taller while I was away?"

    "With everyone together, I realize that Unna and Parvy look strikingly similar to Jorunn."

    menu:
        "\"Are they your siblings?\"":
            j "Nope, they just dyed their hair and painted their tails to look like me!"
            y "Wait, really?"
            j "Haha, I'm just kidding-yeah, they're my sisters!"

        "\"Are they your children?\"":
            j "Hmm? Oh, sure are! Carried them in my belly and everything."
            y shocked  "Really?"
            parvy "Ew! Gross!"
            j "Haha! No, just messing with you. These are my younger siblings." 

    j "Anyways, [y] is gonna stay with us for the night."

    j "She can have my room, and I'll share with Unna and Parvy."

    unna "But your room is-"

    j "It'll be fine. She's a guest, after all."

    unna "...Alright. If you say so."



    jump endofdemo

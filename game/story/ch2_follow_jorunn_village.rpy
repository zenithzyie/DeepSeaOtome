label ch2_jorunn_village:
##This is the continuation of Follow Jorunn after leaving Prashadi's cave

    scene bg sea:
        fit "contain"
    play music "audio/music_underwater.ogg" volume 1.0 fadeout 1.0
    pause 0.7
    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve
    with dissolve

    j mermaid neutral "I should probably mention that the village doesn't get too many visitors these days. They might have some questions for you."

    y "Oh, right. What should I say?"

    y nervous "I need to be careful. They can't know I'm human."

    #Anti mermaid:
    if antimermaid >= 1:
        "Who knows what they could do to me?"

    # Pro mermaid:
    if promermaid >= 1:
        "I don't think they'd be too happy about that."

    j "How about this - we could say you're a traveling trader! They used to come by pretty often before the storms got worse."

    y happy "Oh, a trader? Do you think that would work?"

    y nervous "But...{w} I don't have anything I could trade."

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

    scene bg jorvillage with dissolve:
        fit "contain"
    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve

    j mermaid neutral "Here we are! Welcome to <village name here>."

    y shocked "Wow...!"

    ny "So this is what Jorunn's village looks like! I've never seen so many mermaids in one place before."

    "A few of them pause when they see me. One of the villagers near the entrance swims up to us."

    show jorunn glee with dissolve
    j "Hey, mossyhead! It's good to see you. I'm back!"

    moss "Ugh. I told you not to call me that."

    moss "And who's this? Don't tell me you brought back another mouth to feed."

    y happy "It's nice to meet you. I'm [y]."

    j "She'll just be staying the night. Until the storm blows over, y'know."

    moss "What?"

    moss "You don't look like you're from these waters. What are you doing all the way out here?"

    #CONVINCE THE GUARD PUZZLE START
    menu convincestart:
        "\"I'm a traveling trader.\"":
            $ traderpick = True
            moss "Trading what? I don't see any wares on you."
            menu trader:
                set menuset
                "\"I just traded everything away.\"": #fail
                    $ failconvince += 1
                    moss "Everything? With who?"
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
                    y "Oh no...I guess that makes two of us."
                    moss "*grumble grumble*"
                    "It seems like he bought it, at least."
                    pass

                "\"I wanted to travel light.\"": #fail
                    $ failconvince += 1
                    y "A heavy pack would just slow me down."
                    moss "Right. A trader traveling light."
                    moss "What stupid do you think I am?"
                    y nervous "Er..."
                    jump trader

        "\"I'm visiting from far away.\"":
            moss "How far, exactly?"
            menu faraway:
                set menuset
                "\"From the Capital!\"": #fail
                    $ capitalpick = True
                    $ failconvince += 1
                    moss "Visiting...{i}here?{/i} {w}   From the capital?"
                    moss "Why would you want to leave right when the festival's about to start?"
                    ny nervous "What festival? I just said the first thing that came to my mind!"
                    y "I guess I really didn't think it through...haha..."
                    moss "Clearly. I've seen children lie better than you."
                    jump faraway

                "\"Really far far away.\"": #fail
                    $ failconvince += 1
                    y "But it's like super duper far away. Seriously far away."
                    y "It's like...twenty blue whales and a giant squid length...{w}away?"
                    moss "If you can't give a proper answer, you should just leave."
                    moss "Take your nonsense elsewhere."
                    "Uh oh, he looks like he's one second away from kicking me out."
                    "Well, maybe I need to be more specific."
                    "He sure didn't like that answer. Maybe I accidentally offended him?"
                    jump faraway

                "\"Alaska.\"": #success
                    $ alaskapick = True
                    moss "A'lass Ka? Never heard of it."
                    y "Yeah. Exactly. It's {i}really{/i} far away."
                    j "Oh, I've heard of it before! It's supposed to be way north."
                    j "Some other traders talked about it once! It's way up north. [y] got caught up in the storm on the way there."
                    y "And now I'm trying to get back home somehow."
                    j "Easy peasey once the storm ends!"
                    moss "Whatever. Go have this conversation somewhere else."
                    pass

        "\"No clue. I have amnesia.\"":
            $ amnesiapick = True
            moss "You...what?"
            menu headinjury:
                set menuset
                "\"I don't remember anything.\"": #fail
                    $ failconvince += 1
                    moss "That's too convenient. Come up with a better story next time."
                    y "But it's true! All of my memories are gone."
                    j "She's right! I helped her come up with a fake name and everything."
                    moss "...!"
                    jump headinjury

                "\"I hit my head real bad in the storm.\"": #success
                    j "It's true! I found her passed out on a rock."
                    y "I have proof! There's a bump on my head!!"
                    y "Do you want to see it?"
                    moss "I really don't."
                    y "..."
                    y "Wait, who are you again?"
                    moss "Yeah, you definitely hit your head alright."
                    pass

                "\"I'm trying to remember who I was by visiting lots of different places.\"": #fail
                    $ failconvince += 1
                    moss "And you thought a village way out here would help?"
                    y "This village is open to visitors, right? So I'm gonna visit!"
                    moss "Right..."
                    jump headinjury

    # JOR FAIL SAVE
    if failconvince > 1:
        j "Ok, fine. Everyone, this was all a farce."
        "Jorunn suddenly reaches over and grabs my hand."
        j "...[y] and I are lovers!!!" with screenShake
        moss "What?"
        ny shocked "What is he doing??"
        #jor scream
        show jorunn flustered with dissolve
        j "We didn't want to cause a fuss or anything, but we've been seeing each other for awhile!"
        "The random villager quickly swims away without looking back."
        "Everyone else around us leaves too, whispering amongst themselves."
        "Only one villager is left, staring slack jawed at us."
        u "..."
        pass


    #AFTER SUCCESSFUL CONVO (FINALLY)
    moss "Whatever. Just don't cause any trouble."
    "Grumpypants swims away."

    # picked Jor's suggestion (Trader)
    if traderpick == True:
        show jorunn glee with dissolve
        j "Nice i knew you could pull it off"
        j "Glad u took my suggestion heehee"
        y happy "Ty for the save king appreciate it"
        show jorunn flustered with dissolve
        ny frustrated "Now I just have to remember my story."

    if capitalpick == True:
        show jorunn glee with dissolve
        j "Whew we got away with it. Good job june!"
        y happy "Yay jor praise"
        "Now I just have to remember my story."

    # pass Amnesia check
    if amnesiapick == True:
        show jorunn glee with dissolve
        j "No way! I can't believe you got away with that!"
        y happy "Heehee! It sure is easy to tell the truth."
        j "...Right. Anyway, let's go!"

    #pass Alaska check
    if alaskapick == True:
        show jorunn glee with dissolve
        j "So, where is Alaska, anyway?"
        y "It's a fictional place from the stories my grandfather used to tell me as a child."
        j "You sure are full of surprises."

    #SCENE CHANGE - Jorunn's House

    "I follow Jor through the village to his house."


    jump endofdemo

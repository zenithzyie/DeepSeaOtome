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
        "I don't want to make them uncomfortable."

    j "How about this - we could say you're a traveling trader! They used to come by pretty often before the storms got worse."

    y happy "Do you think that would work?"
    
    y nervous "But...{w} I don't have anything I could trade."

    j "Just say you lost your goods in the storm, easy. I'll back you up!"

    "I can't believe he's acting so confident. Well, hopefully this works!"

    scene bg jorvillage with dissolve:
        fit "contain"
    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve

    j mermaid neutral "Here we are! Welcome to <village name here>."

    y shocked "Wow...!"

    ny "So this is what a mermaid village looks like! I've never seen so many mermaids in one place before."

    ny neutral"A few mermaids pause when they see me. One of the guards at the entrance swims up to us."

    show jorunn sweat
    j "Aw, barnacles. It just had to be this guy on watch duty."

    show jorunn glee
    j "Hey <nickname>! It's good to see you. I'm back!"

    V "Ugh. Don't call me that. I have an actual name."

    V "And who's this, Jor? Don't tell me you brought back another mouth to feed."

    ny nervous "Ack, he's looking at me like I'm going to eat his puppy!"

    y happy "It's nice to meet you. I'm [y]."

    j "She'll just be staying the night. Until the storm blows over, y'know."

    V "What?"

    V "You don't look like you're from these waters. What are you doing all the way out here?"

    #CONVINCE THE GUARD PUZZLE START
    menu convincestart:
        "I'm a traveling trader.":
            $ traderpick = True
            V "Trading what? I don't see any wares on you."
            menu trader:
                set menuset
                "I just traded everything away.": #fail
                    $ failconvince += 1
                    y "Yeah! Turns out everyone really loves discounts."
                    j "Like me!"
                    V "But like...what did you get in return?"
                    y "Er..."
                    j "Customer satisfaction, great reviews...!"
                    y "Exactly. I traded the currency!"
                    V "Hmm."
                    "Oh no, I don't think he bought it."
                    jump trader

                "I lost my wares in the storm": #success
                    V "Is that so? Well, you're not the first one to have that kind of trouble around here."
                    y "Yes. I'm not sure how I'll survive without any supplies."
                    j "Hey, here's an idea! Why don't you stay here with us until the storm passes!"
                    y "Really? That's very kind of you. Who knows, maybe I'll visit here again once I've got stuff to trade with." 
                    V "Hmm..."
                    pass

                "I want to explore the whole ocean!": #fail
                    $ failconvince += 1
                    y "A heavy backpack would just slow me down."
                    V "Right. A trader traveling light."
                    V "What kind of fool do you think I am?"
                    y "Er..."
                    jump trader

        "I'm visiting from far away.":
            V "How far, exactly?"
            menu faraway:
                set menuset
                "From the Capital!": #fail
                    $ capitalpick = True
                    $ failconvince += 1
                    V "Oh neat. Rich as fuck. Why are you here?"
                    y "Is that...not normal?"
                    j "No. It's not..."
                    jump faraway

                "Really far far away. You wouldn't have heard of it.": #fail
                    $ failconvince += 1
                    V "Try me."
                    y "It's like...twenty blue whales and a giant squid length away?"
                    V "What are you even...Restrain this imposter!"
                    jump faraway

                "Alaska": #success
                    $ alaskapick = True
                    V "A'lass Ka? Never heard of her."
                    y "Yeah. Exactly. It's {i}really{/i} far away."
                    j "Some other traders talked about it once! It's way up north. [y] got caught up in the storm on the way there."
                    pass

        "No clue. I have amnesia.":
            $ amnesiapick = True
            V "..."
            menu headinjury:
                set menuset
                "I don't remember anything.": #fail
                    $ failconvince += 1
                    V "That's too convenient. Come up with a better story next time."
                    y "But it's true! All of my memories are gone."
                    j "She's right! I helped her come up with a fake name and everything."
                    V "...!"
                    jump headinjury

                "I hit my head real bad in the storm.": #success
                    j "It's true! I found her passed out on a rock."
                    V "Oh. A head trauma victim. Now this all makes sense."
                    y "I have proof! There's a bump on my head!!"
                    y "You're stupid. I don't remember island i don't care if u don't believe me fuck u"
                    y "Wait, who are you again?"
                    pass
                
                "I'm trying to find out who i was by going around places": #fail
                    $ failconvince += 1
                    V "well it won't help here. We dunno u lady. gtfo"
                    y "aw man"
                    j "wait chill i got this"
                    jump headinjury
                
    # JOR FAIL SAVE
    if failconvince > 0:
        j "Ok fine. Everyone...this was all a farce."
        "Jorunn suddenly reaches over and grabs my hand."
        j "...[y] and I are lovers!!!" with screenShake
        V "WTF"
        "WTF"
        j  "We didn't want to cause a fuss or anything but we've been seeing each other for awhile.!"
        V "Jesus. Okay. fine. Wtf" 
        "Random villager swims away."
        "The rest of the villagers swim away, whispering."
        pass

    
    #AFTER SUCCESSFUL CONVO (FINALLY)
    V "Whatever. Just don't cause any trouble."
    "Grumpypants swims away."

    # picked Jor's suggestion (Trader)
    if traderpick == True:
        j "Nice i knew you could pull it off"
        j "Glad u took my suggestion heehee"
        y "Ty for the save king appreciate it"
        show jorunn flustered with dissolve
        "Now I just have to remember my story."

    if capitalpick == True:
        j "Whew we got away with it. Good job june!"
        y "Yay jor praise"
        "Now I just have to remember my story."

    # pass Amnesia check
    if amnesiapick == True:
        j "holy shit i cant believe you got away with that"
        y "heehee im so good at this"
        j ".............sure."

    #pass Alaska check
    if alaskapick == True:
        j "by the way what is alaska anyway"
        y "oh its the name of a fictional place in a story my grandpapapapa told me as a kid"
        j "sure sounds weird no wonder its not real."

    j "Alrighty time to go home yay"

    #scene change - Jorunn's house


    jump endofdemo
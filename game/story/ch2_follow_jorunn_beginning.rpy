label ch2_follow_jorunn:
##This is the beginning of the Prashadi Cave continuation, after June is transformed into a mermaid.

#SCENE CHANGE - FADE INTO MERMAID CG

    show cg_mermaidprashadi:
        align (0.5, 1.0)
        pos (0.5, 1.26)
        zoom 0.34
    with dissolve
    "The sight of a tail greets me, long and shimmering in the dim cave light."

    window auto hide
    show cg_mermaidprashadi:
        linear 6 pos (0.5, 2.64) zoom 0.34
    with Pause(6.10)
    if not renpy.seen_image("cg_mermaidprashadi"):
        show cg_mermaidprashadi:
            pos (0.5, 2.64) zoom 0.34
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        show cg_mermaidprashadi:
            pos (0.5, 2.64) zoom 0.34
    window auto show

    "I stare down at it, confused, before my eyes trace it upward and find that it's connected to me."

    y "Oh! I'm...a mermaid?"

    "And my voice is back!"

    scene bg prashadi cave:
        fit "contain"
    $ speaking_char = "Prashadi"
    show prashadi neutral at left2
    show jorunn flustered at right2
    with dissolve

    $ followthief.grant()

    Pr mermaid shocked "What a lovely form, is it not?"

    Pr "Now, no need to thank me. I daresay this is one of my finest works yet."

    "My new body is dressed in clothes to match. Were these created during the spell too?"

    menu:
        "They're beautiful.":
            "It reminds me a bit of a bathing suit, but it's unlike anything I've seen before."

        "I'm practically naked!":
            ny flustered "I've never worn such a revealing outfit before!"

    show jorunn flustered at right2 with dissolve
    ny nervous "Joruun stares at me in surprise."

    show jorunn glee with dissolve
    "But when our eyes meet, he quickly schools his expression back into a smile."

    j "It's a good thing I brought you here. To think I almost turned such a pretty girl into dinner!"

    Pr "Now that would have been a great shame indeed!"

    Pr "You did the right thing bringing her to me."

    menu:
        "\"Who are you?\"":
            "You look just like my grandfather. But he's human like me."
            Pr "Oho, is that who you see?"
            Pr "Well, I am certainly old enough to be your grandfather."
            "Right...of course it couldn't be him."

        "\"How did you do that?\"":
            Pr "Oh, you know. With a little bit of this and that."
            Pr "I've picked up a few tricks over the years."
            y "But how is it that you look like my grandfather?"
            Pr "How indeed. A true master never reveals their secrets!"
            y shocked "..."

    Pr "My name is Prashadi, child. Though you can call me whatever you'd like."

    Pr "My magic simply allows you to see the face of whoever is dear to your heart."

    "No wonder Jorunn has been calling Prashadi 'Miss.' He must be seeing a different mermaid."

    y happy "I see. Thank you - both of you - for helping me out."

    y "My name is [y]. As you said, I'm a human."

    "What a relief to be able to introduce myself. I'll never take my voice for granted again!"

    j "So you {i}do{/i} have a name!"

    j "Glad to finally meet you, [y]."

    j "Didn't think you'd be human, though. Must've been a long day, huh?"

    # Pro mermaid:
    if promermaid >= 1:
        y "Tell me about it!"
        "He's still as talkative as ever."
        "I'm glad he doesn't seem to mind that I'm human."

    #Anti mermaid:
    if antimermaid >= 1:
        y "Very long."
        "He's still as talkative as ever."
        "I hope he'll remain friendly."

    y nervous "Everything was going fine until I was lured into the sea by a siren's song."

    y "She's the reason why I got turned into a fish in the first place."

    j "A siren?"

    Pr "How curious...How curious indeed. Do you remember anything else about this siren?"

    "I explain everything in clear detail, right up to the point where Jorunn saved me from the storm."

    y "She called herself Skylla. Is that anyone you might know?"

    Pr "I certainly knew a 'Skylla', but it was many years ago now. And the Skylla I knew was certainly no siren."

    #Anti mermaid
    if antimermaid >= 1:
        #placeholder
        "Of course suspicious people know suspicious people!!!!"

    j "Do you think she could be the same mermaid, Miss Prash?"

    Pr "Hmm..."

    Pr "Whoever she is, she's certainly done a number on our human friend!"

    y "Prashadi, is it possible for you to turn me back into a human? I'm very grateful for your help but...I need to return home."

    Pr "If it were simply a spell, I would have already sent you on your way home."

    Pr "Curses are not so easily undone."

    y frustrated "A curse?"

    Pr "Yes. This form is the best l can do for you right now. Unless it's broken - no matter where you go - the sea will always pull you back."

    "No...there has to be a way, right?"

    ny frustrated "But that would mean...I'll be trapped here forever."

    menu:
        "\"I don't want to be a mermaid forever!\"":
            $ antimermaid += 1
            pass

        "\"But I have family waiting for me.\"":
            $ jorunn_points += 1
            pass

    Pr "It's dangerous, child, to meddle with your curse any further."

    y "What am I going to do...?"

    #AHHHHH moment

    j "Hey, it's alright. We'll figure this out together."

    j "It's dangerous, but not impossible, right?"

    Pr "Now, boy..."

    show jorunn sweat with dissolve
    j "The siren must be the one causing all these storms here."

    #If newsboard
    if seastorm:
        y "There's been storms above water, too."
        "Now that I think about it, those posters in Aquantis had warned about sea storms suddenly appearing."
        "Just how long has this been going on?"

    #If not newsboard
    "I recall how powerful the building storm felt when I was a tiny fish and try not to shudder."
    y "There's been other sea storms before?"
    j "Yeah. For a long time."

    Pr "Sea storms have always been a natural occurrence, but those created from magic have a tendency to be rather...volatile."

    j "If we let things be, it'll be trouble for all of us."

    show jorunn glee with dissolve
    j "Plus it's not every day we get to team up with a human."

    "Jorunn discreetly elbows me."

    menu:
        "\"UM RUDE!\"":
            show jorunn pissed with dissolve
            j "..."
            show jorunn glee with dissolve
            j "Work with me here, [y]. I'm trying to help you out."
            y shocked "You'll really help me?"

        "\"Jor is right.\"":
            #$ jorunn_points += 1
            y veryhappy "We can totally do it! I can't give up yet!"

    
    Pr "Hmm! There appears to be a rather unusual mystery here. And with a human involved..."

    Pr "I'll tell you what! Perhaps I can help you after all!"

    y shocked "What? Really?"

    Pr "Yes. It certainly won't be easy to break a curse this strong though, so I'm afraid you must run some errands for me."

    y "Anything!"

    Pr "I need you to collect a few relics."

    y nervous "Relics...?"

    Pr "Small things, imbued with the power of magic. Though there are very few magic users left, the relics they've created remain. I will need three of them to undo your curse."
    
    y "Three relics...where do I look for them?"

    Pr "..."

    "Prashadi's smile begins to turn slightly crooked."

    Pr "Where indeed! Not to worry. The first one can be found somewhere you know very well."

    j "Huh? Miss Prash? You can't mean-"

    Pr "That's right! It's up on land!"

    y "What?"

    "Up on land? How would I even go get a relic back from there if I'm a mermaid?"

    Pr "Now, now, no need to look so confused! Prashadi's will always has a way."

    Pr "I can cast a temporary spell on you to give you back your legs. It won't last longer than a day, I must warn you. Like I said before, your curse is designed to pull you back to the sea." 

    Pr "Until it's fully broken, you'll always return here."

    y "So I'll have my legs back for a day?"

    Pr "I knew you were a smart little fry."

    "The thought is dizzying. But with it comes a hope that sends my heart beating faster. I could see grandfather and Hunter again. Let them know that I'm alive."

    "But..."

    y "Once I'm up on land, how will I know where the relic is? What does it look like?"

    j "I'll go with you."

    y "...!"

    Pr "Now here's a twist! Are you sure, my boy?"
    
    j "I'm good at sensing magic stuff. If I go with [y], finding these relics should be a piece of fish! Plus, having legs for a day sounds super cool!"

    Pr "Well...it's surely possible."

    menu:
        "\"Thank you.\"":
            y "Thank you...I'd really appreciate that."
            "I feel overwhelming gratitude towards Jorunn. Despite the fact that I've just met him, he seems willing to go up to land with me."
            j "Of course! How could I let my new friend go back up there all alone?"
            "I find myself smiling back at him. His cheer is infectious."

        "\"Why would you help me?\"":
            #$ jorunn_points += 1
            y "Wouldn't it be dangerous to go up on land for you? Why would you want to help me? We've only just met."
            j "Aw, how could I let my new friend go back up there all alone?"
            j "Besides, I have a feeling the siren that came after you is bad news for me too. Whatever she's planning to do with you can't be good."
            "Right. If that witch is plotting something, it can't be good for the mermaids living here either."
            y "I see. I'd be grateful then if you joined me."

    Pr "Then it's settled!"

    "Prashahi's hands clap together."

    Pr "Are you ready?"

    y "Yes!"

    Pr "Wonderful. Now, come back tomorrow!"

    y "..."
    
    y "Pardon?"

    Pr "A spell to give the two of you legs will take some time to prepare. Don't be so greedy! Didn't I even help you get out of that awful fishy body? I do need my rest as well."

    "I feel flustered at being called out like that."

    y "Right. I'm sorry."

    "What am I even supposed to do until tomorrow? It's not as though I have a home underwater to return to."

    j "Why don't you come stay at my village for the night, [y]? We're not the capital city or anything, but it'll beat having to sleep out in the sand."

    y "Oh! If you're sure...Thank you."

    j "Thanks, Miss Prash. We'll see you tomorrow then."

    Pr "Tomorrow, my boy."

    j "Here."

    "Jorunn offers me his hand."

    menu:
        "Take it.":
            #$ jorunn_points += 1
            y "Thank you."
            "I hadn't really noticed it as a fish, but his hand feels surprisingly calloused when it slips around my own."
            j "Sure thing. Hold tight, okay?"

        "Decline.":
            j "You sure? No need to be shy. It's pretty dark out there. We wouldn't want you getting lost."
            y "I'll manage."
            j "If you say so!"

    "I turn back to say farewell to Prashadi a final time, but they are nowhere to be found. The cave is entirely empty, as if no one had been there in the first place."

    "What a strange sort."

    "We swim back through the tunnels. It's just as dark as my first trip through them, but I feel a bit more courageous knowing that I have a plan now."

    #JUMP TO JOR VILLAGE

    jump endofdemo

    #SCENE CHANGE - fade to black

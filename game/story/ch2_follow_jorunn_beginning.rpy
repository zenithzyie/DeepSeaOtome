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

    #June inner thought here?

    menu:
        "\"Who are you?\"":
            "You look just like my grandfather. But he's human like me."
            Pr "Oho, is that who you see?"
            Pr "Well, I am certainly old enough to be your grandfather."
            "Right...of course it couldn't be him."

        "\"How did you do that?\"":
            Pr "I've picked up a few tricks over the years."
            y "And how is it that you look like my grandfather?"
            Pr "How indeed. A true master never reveals their secrets!"
            y shocked "..."

    Pr "My name is Prashadi, child. Though you can call me whatever you'd like."

    Pr "My magic simply allows you to see the face of whoever is dear to your heart."

    "No wonder Jorunn has been calling Prashadi 'Miss.' He must be seeing a different mermaid."

    y happy "I see. Thank you - both of you - for helping me out."

    y "My name is [y]. As you said, I'm a human."

    "What a relief to have my voice back!"

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

    y nervous "It was because of a siren. She's the one who lured me into the sea."

    j "A siren?"

    Pr "How curious...How curious indeed. Do you remember anything else about this siren?"

    "I explain everything in clear detail, right up to the point where Jorunn saved me from the storm."

    y "She called herself Skylla. Is that anyone you might know?"

    Pr "I knew of a 'Skylla', but that was some time ago. And she was certainly no siren."

    j "Do you think she could be the same mermaid, Miss Prash?"

    Pr "Hmm..."

    Pr "Whoever she is, she's certainly done a number on our human friend."

    y "Prashadi, is it possible for you to turn me back into a human?" 

    y "I'm very grateful for all you've done, but...I need to return home."

    Pr "If it were that simple, I would have sent you on your way already."

    Pr "But I'm afraid the curse on you is not so easily undone."

    y shocked "A curse?"

    Pr "Yes. No matter where you go, the sea will always pull you back. Your form now is all I can do for you."

    y "Is there any way to remove it completely?"

    Pr "It's dangerous, child, to meddle with your curse any further."

    j "Dangerous, but not impossible, right?"

    Pr "Now, boy..."

    show jorunn sweat with dissolve
    j "I know you're trying to look out for us, but I don't think whatever the siren is planning will stop with [y]'s curse."

    j "The storms here have been getting worse, haven't they? If we let things be, it'll be trouble for all of us."

    #if newsboard
    if seastorm:
        "Now that I think about it, those posters in Aquantis had warned about storms suddenly appearing."
        "So, they've been affecting the mermaids underwater too..."

    else:
        "Just how long have these storms been going on for?"

    j "Besides, even if it's dangerous, she should get the choice."

    j "It's her life, after all, isn't it?"

    y "Right!"

    y "Even if it means risking my life, I have to get back home."

    Pr "There's worse things out there than dying, girl."

    y "Even so, I want to try."

    Pr "..."

    "They're just like grandfather...stubborness and all."

    j "Prashadi, if you really won't help us, then we'll just have to figure it out ourselves."

    j "You can't stop us from doing that now, can you?"

    show prashadi shocked with dissolve

    Pr "Jorunn. Don't be foolish."
    
    j "Well, you're not giving us much of a choice."

    j "I'll leave it up to you. Whether you want us to be going in unprepared or not."


    j "But I'm not going to be sitting around doing nothing."

    Pr "Of all the times to be so bullheaded..."

    menu:
        y frustrated "..."
        "\"I don't want to be a mermaid for the rest of my life!\"":
            y "Please. I don't belong here."
            pass

        "\"I have family waiting for me.\"":
            y "Please. Wouldn't you want to get back to your family too?"
            pass

    show prashadi neutral with dissolve
    Pr "...Very well."

    show prashadi angry with dissolve
    Pr "But I will not be responsible for your deaths, you hear?"

    j "Course not. We're not dying anytime soon."

    y "You'll help us?"



    if jorright:
        "Jorunn gives me a wink and a big ol thumbs up."

    "I hope this means I'll be home soon if all goes well."
    
    Pr "Don't thank me just yet. It certainly won't be easy to break a curse this strong, so I'm afraid you must run some errands for me."

    y "Anything!"

    show prashadi neutral with dissolve
    Pr "I need the two of you to collect some relics."

    y nervous "Relics...?"

    j "Done!"
    
    y "Like...{w}antiques?"

    #june inner thought
    "I'm picturing a fancy vase imbued with mermaid magic. Somehow I doubt that's what a relic is, though."

    Pr "Small things, imbued with the power of magic. Though there are very few magic users left, the relics they've created remain. I will need three of them to undo your curse."

    menu whatisrelic:
        set menuset
        "I have so many questions..."
        "\"What do they look like?\"":
            Pr "Anything. They can look as different as you can me."
            y "Then how will I know if it's a relic?"
            show jorunn pissed with dissolve
            j "beep beep metal/relic detector."
            show jorunn glee with dissolve
            Pr "...Pretty much like ordinary objects. Magic people left them, very special cool stuff."
            y "How do old mementos carry magic?"
            Pr "What am I, a dictionary? Hakuna matata."
            jump whatisrelic
        "\"How do we find these relics?\"":
            "Prashadi's smile begins to turn slightly crooked."
            Pr "That depends entirely on your luck."
            y nervous "..."
            y "How long could that take? I don't have any time to waste!"
            Pr "They'll come to you. You just gotta keep an eye out."
            jump whatisrelic
        "\"Will this undo my curse?\"":
            Pr "Thats a good ole prashadi secret :)"
            jump whatisrelic
    
    "If these relics are so hard to find, how am I ever supposed to find them? I'm just human!"

    Pr "It's precisely why I think you'll be the best at finding them! Haha"

    y "Oh brother..."

    Pr "Not to worry. The first one can be found somewhere you know very well."



    j "Huh? Miss Prash? You can't mean-"

    Pr "That's right! It's up on land!"

    y "What?"

    "Up on land? How would I even go get a relic back from there if I'm a mermaid?"



    "Come to think of it, how does a mermaid relic end up on land?"

    "...Same way that mermaids end up on land, I suppose."

    Pr "Now, now, no need to look so confused! Prashadi will always have a way."

    Pr "I can cast a temporary spell on you to give you back your legs. You would have three days before you return to the sea."

    y "So I'll have my legs back for a day?"

    Pr "I knew you were a smart little fry."

    "The thought is dizzying. But with it comes a hope that sends my heart beating faster."

    "I could see Grandfather and Hunter again. Let them know that I'm alive."

    "But..."

    "I wouldn't be able to stay with them. I'd only be human for three days."

    y "This...This is a lot. Are you sure you still want to help me, Jorunn?"

    j "Of course I still wanna help you. And how could I pass up the chance at being human? Sounds pretty neat!"


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

    Pr "Ha! You humans are still so impatient! First and foremost, take some time to rest and enjoy being out of that awful fishy body."

    y "Oh. Right. I could do with a good rest."

    Pr "Ah, almost forgot the most important part-Once you're ready, you'll get your legs by breaking the surface at dawn."
    
    Pr "I recommend being close to land when you do. Swimming without a tail is tough work!"

    "Dawn? That feels like a lifetime away! What am I supposed to do until then? Where am I even supposed to sleep?"

    j "Why don't you come stay at my village for the night, [y]?"

    j "We're not the capital city or anything, but it'll beat having to sleep out on the sand."

    y happy "Oh! If you're sure...That would be wonderful."

    j "Here."

    "Jorunn offers me his hand."

    menu:
        "Take it.":
            #$ jorunn_points += 1
            y "Thank you."
            "I hadn't really noticed it as a fish, but his hand feels surprisingly calloused when it slips around my own."
            j "Sure thing. Hold tight, okay?"

        "Decline.":
            j "You sure? No need to be shy. It's pretty dark in those tunnels. We wouldn't want you getting lost."
            y "I'll manage."
            j "If you say so! Just say close, alright?"

    hide prashadi with dissolve
    hide jorunn with dissolve 
    "With that, we start to leave."

    j "Thanks, Miss Prash!"

    Pr "It's still too early to thank me yet, boy..."

    "I turn back to say farewell to Prashadi a final time as well, but they are nowhere to be found."

    ny nervous "The cave is entirely empty, as if no one had been there in the first place."

    "..."

    "What a strange sort."

    #BLACK SCENE
    scene bg black with fade

    "We swim back through the tunnels. It's just as dark as my first trip through them, but I feel a bit more courageous knowing that I have a plan now."

    call ch2_jorunn_village from _call_ch2_jorunn_village
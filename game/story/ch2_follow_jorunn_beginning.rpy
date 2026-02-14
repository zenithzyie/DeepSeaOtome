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
            "I've never worn such a revealing outfit before!"

    show jorunn flustered at right2 with dissolve
    "Joruun stares at me in surprise."

    show jorunn glee with dissolve
    "But when our eyes meet, he quickly schools his expression back into a smile."

    j "It's a good thing I brought you here. To think I almost turned such a pretty girl into dinner!"

    Pr "Now that would have been a great shame indeed!"

    Pr "You did the right thing bringing her to me."

    menu:
        "\"Who are you?\"":
            y "You look just like my grandfather. But he's human like me."
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
    y "Tell me about it!"
    "He's still as talkative as ever."
    "I'm glad he doesn't seem to mind that I'm human."

    #Anti mermaid:
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
    #"Of course suspicious people know suspicious people!!!!"

    j "Do you think she could be the same mermaid, Miss Prash?"

    Pr "Hmm..."

    Pr "Whoever she is, she's certainly done a number on our human friend!"

    y "Prashadi, is it possible for you to turn me back into a human? I'm very grateful for your help but...I need to return home."

    Pr "If it were simply a spell, I would have already sent you on your way home."

    Pr "Curses are not so easily undone."

    y frustrated "A curse?"

    #Pr "Unless it's broken - no matter where you go - the sea will always pull you back.

    "No...there has to be a way, right?"

    ny frustrated "But that would mean...I'll be trapped here forever."

    menu:
        "\"I don't want to be a mermaid forever!\"":
            #+racism
            pass

        "\"But I have family waiting for me.\"":
            #+jor
            pass

    Pr "It's dangerous, child, to meddle with your curse any further."

    #y "Is there really no other way, if it means staying down here forever? I'll have to try something!"

    y "What am I going to do...?"
    #AHHHHH

    j "Hey, it's alright. We'll figure this out together."

    j "Miss Prash, is there really no other way?"

    Pr "You as well, Jorunn?"

    j "The siren must be the one causing all these storms here."
    j "With how powerful the siren is, she must be the one causing all the sea storms."

    j "If we let things be, it'll be trouble for all of us."

    #If not newsboard
    "I recall how powerful the building storm felt when I was a tiny fish and try not to shudder."
    y "There's been other sea storms before?"
    j "Yeah. For a long time."

    #if newsboard
    y "There's been storms above water, too."
    "Now that I think about it, those posters in Aquantis had warned about sea storms suddenly appearing."
    "Just how long has this been going on?"

    Pr "Sea storms have always been a natural occurrence, but those created from magic have a tendency to be rather...volatile."


    jump endofdemo

    #SCENE CHANGE - fade to black

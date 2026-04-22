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

    "It seems that Prashadi is someone who exists outside of the gender we see."

    y happy "So that's how it is...Thank you - both of you - for helping me out."

    y "My name is [y]. As you said, I'm a human."

    "What a relief to have my voice back!"

    j "So you {i}do{/i} have a name!"

    j "Glad to finally meet you, [y]."

    j "Didn't think you'd be human, though. Must've been a long day, huh?"

    # Pro mermaid:
    if promermaid >= antimermaid:
        y "Tell me about it!"
        "He's still as talkative as ever."
        "I'm glad he doesn't seem to mind that I'm human."
    #Anti mermaid:
    elif antimermaid > promermaid:
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

    y nervous "There must be some way to remove it?"

    show prashadi angry with dissolve
    Pr "It's dangerous, child, to meddle with your curse any further."

    j "Dangerous, but not impossible, right?"

    Pr "Now, boy..."

    show jorunn sweat with dissolve
    j "This siren who cursed [y]...she must be the same one who's causing all these storms here, isn't she?"

    Pr "It's likely, yes."

    #if newsboard
    if seastorm:
        "Now that I think about it, those posters in Aquantis had warned about storms suddenly appearing."
        "So, they've been affecting the mermaids underwater too..."

    else:
        "Just how long have these storms been going on for?"

    j "I know you're trying to look out for us, but I don't think whatever she's planning to do with [y] will stop with the curse."

    j "If we let things be, it'll be trouble for all of us."

    j "Besides, even if it's dangerous, she should get the choice."

    j "It's her life, after all, isn't it?"

    y neutral "Right!"

    y "Even if it means risking my life, I have to get back home."

    Pr "There's worse things out there than dying, girl."

    y "Even so, I want to try."

    Pr "..."

    ny frustrated "They're just like grandfather...stubborness and all."

    j "Prashadi, if you really won't help us, then we'll just have to figure it out ourselves."

    j "You can't stop us from doing that now, can you?"

    show prashadi shocked with dissolve

    Pr "Jorunn. Don't be foolish."

    j "Well, you're not giving us much of a choice."

    j "I'll leave it up to you-whether you want us to be going in unprepared or not."

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

    show jorunn glee with dissolve
    j "Course not. I'm not planning on dying anytime soon."

    y happy "Thank you, Prashadi!"

    Pr "Don't thank me just yet. You will need to complete some tasks for me first."

    y "Just tell me what to do."

    Pr "I need the two of you to collect some relics."

    y neutral "Relics? Like...antiques?"

    show jorunn neutral with dissolve
    j "Magic items, basically. They show up in a lot of children's tales."

    menu whatisrelic:
        set menuset
        "I have so many questions..."
        "\"What do they look like?\"":
            $ pr_questions += 1
            show prashadi neutral with dissolve
            Pr "Anything. They can look as different as you and me."
            "A fleeting look of nostalgia passes over Prashadi's face."
            Pr "A scroll, a trident, or perhaps a ring..."
            Pr "Just to name a few, you might say."
            "That isn't very specific, but I think I get the idea."
            jump whatisrelic

        "\"How do we find these relics?\"":
            $ pr_questions += 1
            Pr "As scattered as they are, I can point you in the right direction."
            y "And after that? How will I know when I've found one?"
            Pr "That is where you're fortunate Jorunn has offered his help."
            show jorunn glee with dissolve
            "Jorunn gives me a confident smile."
            j "I've got a good eye for magic!"
            y "Oh! I'll be grateful for your help, then."
            "Now that I think about it, he was able to sense there was something different about me as a fish too."
            "I wonder how he learned to do that. Is it a mermaid thing?"
            jump whatisrelic

        "\"Will these relics undo my curse?\"":
            $ pr_questions += 1
            Pr "They will play a part in it, yes."
            y "Just 'a part'? Is there something else we need to do?"
            Pr "In due time, little fry. Bring me a relic first, then we'll talk."
            menu:
                "\"Alright.\"":
                    "I want to know more, but..."
                    "I'd better not press any further."
                    "I don't want them to change their mind about helping me."
                    jump whatisrelic

                "\"Isn't there anything else you can tell us?\"":
                    $ jorunn_points += 1
                    Pr "I've already warned you that breaking this curse will be no simple matter. Prove to me that you can handle this task."
                    Pr "Only then will I trust you with what comes next."
                    y frustrated  "..."
                    "That seems to be as far as I can push."
                    "It's frustrating, but let's just leave it at this for now."
                    jump whatisrelic
        "That's all." if pr_questions >= 1:
            pass
    y neutral "So, where should we start looking?"

    Pr "Hmm...yes, the closest one will do."

    y "...?"

    Pr "You will find it on land."

    y shocked "Pardon?"

    show jorunn sweat with dissolve
    j "Land? You want us to find a relic up there?"

    Pr "Yes, I will grant you the means to do so."

    y "I thought you said you couldn't break the curse?"

    Pr "This spell will only be an illusion. Your true body will remain as it is."

    Pr "You will not have much time before you will need to return to the sea."

    y sad "Oh."

    "I could see Grandfather and Hunter again...but what would I even say? They're both mermaid hunters."

    "..."

    "Perhaps I could find a way to leave them a letter? Just to let them know I'm alive..."

    show jorunn glee with dissolve
    j "...Well, I can't say I've been up on land before. I guess I'll be in your care, [y]!"

    y happy "Yes, of course."

    "Right. I'm not in this alone. We'll find the relic together."

    menu:
        "\"Thank you for agreeing to help.\"":
            y "I know it must be a lot to go up on land like this."
            j "Course! We'll make the most out of it, yeah?"
            "He doesn't seem nervous at all."
            "I find myself smiling back at him. His cheer is infectious."

        "\"But are you sure you're okay with going up on land?\"":
            $ jorunn_points += 1
            j "Course! Said we'd figure this out together, didn't I?"
            y "Still, we've only just met. You're taking a big risk by going up there."
            j "Well, Guess I am, aren't I? If you treat me to a meal I'll consider us even, hehe."
            y "I think I can work with that."
            "He doesn't look nervous at all. It seems I was worried for nothing."

    show jorunn neutral with dissolve
    j "So, how will the illusion work? Are you going to cast the spell on us now?"

    show prashadi neutral with dissolve
    Pr "...It has been a very long time since I've last done this." 

    "A gentle coolness passes over me as Prashadi casts their spell."

    Pr "When morning comes, swim up to the shore. You'll find yourself able to walk without much trouble at all."

    y "Morning? And not now?"

    show prashadi happy with dissolve
    Pr "You will want the morning sun for what comes after. And I suggest the two of you get some rest until then."

    y flustered "Oh. Right. I could do with a good rest."

    ny nervous "But it's not like I have a place to stay."

    ny "Would either of them let me spend the night? I wouldn't want to impose any more than I already have."

    "Jorunn seems to catch my eye."

    j "...Why don't you stay over at my village for the night, [y]?"

    j "I've gotta pop in before we head out tomorrow, anyways."

    y "That would be wonderful, thank you."

    j "Okay!"

    "Jorunn offers me his hand."

    j "Here. Don't want to lose you on the way back out, yeah?"

    "Right, It was pretty dark on our way in..."

    menu:
        "Take his hand.":
            $ jorunn_points += 1
            y "Alright. I'll follow your lead, then."
            j "Hold tight, okay?"
            j "It'd be terrible to lose such a pretty girl here!"
            "I hadn't really noticed it as a fish, but his hand feels surprisingly calloused when it slips around my own."

        "Decline.":
            y happy "It's alright. I can follow you on my own."
            j "You sure? It's easy to get lost in those tunnels."
            # Pro mermaid:
            if promermaid >= antimermaid:
                y "I'll manage, don't worry."
                j "If you say so! Just stay close, alright?"
            #Anti mermaid:
            if antimermaid > promermaid:
                ny nervous "I feel nervous about holding hands with a mermaid."
                y "I'll manage."

    j  "Thanks, Miss Prash. We'll be back before you know it."

    Pr "It's still too early to thank me yet, boy..."

    Pr "Mind your time wisely on land. The illusion will dissolve once you return to the sea."

    y "We'll be careful!"

    "Prashadi's warning echoes in my mind as I exit the cave with Jorunn."

    hide jorunn with dissolve
    hide prashadi with dissolve

    #BLACK SCENE
    scene bg black with fade

    call ch2_jorunn_village from _call_ch2_jorunn_village

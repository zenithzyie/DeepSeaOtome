label ch2_jorunn_village:
##This is the continuation of Follow Jorunn after leaving Prashadi's cave

    #SCENE CHANGE - sea wilderness
    scene bg sea with dissolve
    play music "audio/music_underwater.ogg" volume 1.0 fadeout 1.0

    $ speaking_char = "Jorunn"
    show jorunn happy with dissolve

    #hand check
    if takehand == True:
        "Once we're out of the darkness, I let go of Jorunn's hand."

    j mermaid neutral "I should probably mention that the village doesn't get too many visitors these days."

    show jorunn neutral with dissolve
    j "They might have some questions for you."

    y "Oh, right. What should I say?"

    ny nervous "I need to be careful. They can't know I'm human."

    # Pro mermaid:
    if promermaid >= antimermaid:
        "I don't think they'd be too happy about that."

    #Anti mermaid:
    if antimermaid > promermaid:
        "Who knows what they could do to me?"

    show jorunn happy with dissolve

    j "How about this - we could say you're a traveling trader!"
    j "They used to come by pretty often before the storms got worse."

    y happy "Oh, a trader?"

    y nervous "But...{w=0.2} Do I look the part? I don't have anything I could trade."

    show jorunn smile with dissolve

    j "Just say you lost your goods in the storm, easy. I'll back you up!"

    menu:
        "\"Alright!\"":
            $ jorunn_points += 1
            y happy "I'll give it my best shot."
            show jorunn happy with dissolve
            j "That's the spirit!"

        "\"Are you sure?\"":
            y nervous "What if they don't believe me?"
            j "They will! Trust me."

    show jorunn smile with dissolve
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
    show jorunn happy with dissolve

    j mermaid neutral "Here we are! Welcome to our village."

    y shocked "Wow...!"

    show jorunn smile with dissolve

    ny "So this is what Jorunn's village looks like! I've never seen so many mermaids in one place before."

    "Large plant stalks cover the entire area. I wonder if they're protecting us from the storm?"

    if looked_through:
        "Large plant stalks cover the entire area. I wonder if they're protecting us from the storm?"
        "The structures on them remind me of treehouses. That must be where the mermaids live."
    else:
        "The structures on the plant stalks remind me of treehouses. That must be where the mermaids live."

    ny sad "I wish I could take a picture of it..."

    "One of the villagers near the entrance swims up to us."

    show jorunn happy at jorunn_right with move
    j "Hey, mossyhead! It's good to see you. I'm back!"

    moss "Ugh. I told you not to call me that."

    moss "And who's this? Don't tell me you brought back another mouth to feed."

    y happy "It's nice to meet you. I'm [y]."

    j "She'll just be staying the night. Until the storm blows over, y'know."

    moss "What?"

    "His face scrunches up a bit."

    moss "You don't look like you're from these waters. What are you doing all the way out here?"
    show jorunn smile with dissolve

    #CONVINCE THE GUARD PUZZLE START
    menu convincestart:
        ny neutral "What do I tell him?"
        "\"I'm a traveling trader.\"":
            $ traderpick = True
            moss "Trading what? I don't see any wares on you."
            menu trader:
                "\"I just traded everything away.\"": #fail
                    show jorunn hesitant with dissolve
                    moss "Everything? With whom?"
                    moss "We're the only village around here for days."
                    y "Uh, from further away."
                    "Mr. Mossyhead's frown deepens."
                    ny nervous "Oh dear, I don't think he bought it."
                    jump failedconvincemoss

                "\"I lost my wares in the storm.\"": #success
                    y sad "The currents took everything away before I could blink."
                    moss "...That so?"
                    show jorunn shocked with dissolve
                    j "I couldn't believe it at first either! At least we know you're not the only one who's lost their wares in a storm now, Mossy."
                    moss "Shut up about that, will you? It was one time."
                    show jorunn happy with dissolve
                    j "You should have seen it, [y]!"
                    j "He made a big fuss about how he'd make the best trades, then came back empty-handed after losing everything! Haha."
                    y shocked "Oh no...I guess that makes two of us."
                    moss "Ugh..."
                    jump succeedconvincemoss

                "\"I wanted to travel light.\"": #fail
                    show jorunn hesitant with dissolve
                    y "A heavy pack would just slow me down."
                    moss "Right. A trader traveling light."
                    moss "How stupid do you think I am?"
                    y nervous "Er..."
                    "That sounded better in my head."
                    jump failedconvincemoss

        "\"I'm visiting from far away.\"":
            show jorunn neutral with dissolve
            moss "How far, exactly?"
            menu faraway:
                "\"From the...mermaid capital?\"": #fail
                    show jorunn hesitant with dissolve
                    moss "Visiting...{i}here?{/i} {w=0.4}From the capital?"
                    moss "Why would you want to leave right when the festival's about to start?"
                    ny nervous "What festival? I just said the first thing that came to my mind!"
                    y "I guess I really didn't think it through...haha..."
                    moss "Clearly. I've seen children lie better than you."
                    "Well, that's embarrassing."
                    jump failedconvincemoss

                "\"Really really far away.\"": #fail
                    show jorunn hesitant with dissolve
                    y "You wouldn't have heard of it."
                    moss "Try me."
                    y "But it's like super duper far away. Seriously far away."
                    y "It's like...twenty blue whales and a giant squid length...{w}away?"
                    moss "If you can't give a proper answer, you should just leave."
                    moss "Take your nonsense elsewhere."
                    ny nervous "That could've gone better..."
                    jump failedconvincemoss

                "\"Kansas.\"": #success
                    $ kansaspick = True
                    moss "Can'zass? Never heard of it."
                    y neutral "Yes, exactly. It's {i}really{/i} far away."
                    show jorunn happy with dissolve
                    j "Oh, yeah! It's supposed to be way north. You really oughta get out more often."
                    moss "Shut it!"
                    y nervous "Look, I'm sorry to impose..."
                    y "It's just been a really long trip. I don't think I can keep traveling in the storm."
                    show jorunn shocked with dissolve
                    j "You're not going to turn her away, are you, Mossy?"
                    moss "..."
                    jump succeedconvincemoss

        "\"No clue. I have amnesia.\"":
            show jorunn neutral with dissolve
            $ amnesiapick = True
            moss "You...what?"
            menu headinjury:
                "\"I just don't remember anything.\"": #fail
                    show jorunn neutral with dissolve
                    moss "...?"
                    y "It's true! All of my memories are gone."
                    moss "Do you think I have fish for brains? If you're going to talk nonsense, you can leave."
                    ny nervous "I was so sure that would work!"
                    jump failedconvincemoss

                "\"I hit my head real bad in the storm.\"": #success
                    show jorunn shocked with dissolve
                    j "It's true! I found her passed out on a rock."
                    y "I have proof! There's a bump on my head!!"
                    y "Do you want to see it?"
                    moss "I really don't."
                    j "It's a nasty bump! I thought she was dead when I found her!"
                    y sad "Ouch...it hurts just thinking about it."
                    moss "Ugh..."
                    jump succeedconvincemoss

                "\"I'm trying to remember who I was by visiting lots of different places.\"": #fail
                    show jorunn hesitant with dissolve
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
    $ datingspeedrun.grant()
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
    show jorunn happy with dissolve
    j "Yep! Thanks, Mossy!"
    ny happy "I can't believe that worked."
    show jorunn happy at jorunn_center with move
    "Following Jorunn's lead, we swim further into the village."

    # picked Jor's suggestion (Trader)
    if traderpick:
        show jorunn happy with dissolve
        j "Hehe. Nice job, [y]. You've got a knack for this kind of stuff, huh?"
        menu:
            "\"Well, I couldn't have done it without your advice.\"":
                "Jorunn gives me a big wink."

            "\"Haha, maybe I do.\"":
                $ jorunn_points += 2
                y veryhappy "You could say I was made for the stage!"
                "Jorunn gives me a playful bow."
                j "Our star of the sea! It was an honor to share the stage with you."
                y "Hehe."

    # pass Amnesia check
    if amnesiapick:
        show jorunn happy with dissolve
        j "Well, that's not exactly what I had in mind, but it worked out pretty well!"
        y "Thank you for backing me up, Jorunn."
        j "Sure thing!"
        show jorunn smile with dissolve
        j "We gotta stick together, yeah?"


    #pass Kansas check
    if kansaspick:
        show jorunn happy with dissolve
        j "Well, that's not exactly what I had in mind, but it worked out pretty well!"
        y happy "Thank you for backing me up, Jorunn."
        j "Sure thing!"
        j "We gotta stick together, yeah?"
        show jorunn smile with dissolve
        "..."
        j "So, what is Kansas, anyway?"
        y "Oh, it's a fictional place!"
        y "My grandfather used to tell me stories about it as a child."
        y "I liked the one about a girl who got swept up in a storm the most."
        "..."
        ny nervous "Now that I think about it, that's kind of what happened to me."
        show jorunn happy with dissolve
        j "Really? You gotta tell me about it sometime."
        y happy "Sure! I'd love to."


    #SCENE CHANGE - Jorunn's House

label jorshouse:
    scene bg jorvillage afternoon with fade:
        align (0.5, 1.0)
        pos (0.5, 1.0)
        zoom 0.34

    "We stop at the entrance to one of the homes."

    show jorunn smile with dissolve
    $ speaking_char = "Jorunn"

    j mermaid neutral "Well, here we are!"

    u "Jor?"

    "A younger mermaid swims up to us from the inside. She looks relieved to see Jorunn."

    show jorunn at jorunn_right with move
    show unna at unna_left with dissolve

    $ speaking_char = "Unna"

    u "You're back!"

    show jorunn happy with dissolve

    j "I am back! Hey, Unna."

    unna "I wasn't sure if you were going to make it back in time with the storm."

    show jorunn smile with dissolve

    j "Aw, come on, as if a little current like that could stop me."

    unna "And- oh, hello! Who's this with you?"

    show jorunn neutral with dissolve

    j "This is [y]. Found her all caught up in the storm outside. She'll be staying the night 'til it passes over."

    y happy "It's nice to meet you- Unna, is it?"

    unna "Yeah, you got it! I haven't seen clothes like yours around here before. The storm must have carried you a long way, huh?"

    y "Haha...you could say that. Thank you for having me."

    "She seems much friendlier than Mr. Mossyhead."

    j "Where's Parvy? Have you two eaten yet?"

    unna "Not yet. We were hoping to eat together with you."

    "As if on cue, a small figure swims out of the undergrowth to greet us."

    show parvy at parvy_center with dissolve

    parvy "...Hi, Jor."

    show jorunn happy with dissolve

    j "There she is!"

    if childrenplaying:
        # Pro mermaid:
        if promermaid >= antimermaid:
            "I can't help but smile. I've never seen a mermaid so small before."
            "She reminds me of the children I saw in Aquantis."

    $ speaking_char = "all"

    "The three of them all look so much alike."

    menu:
        ny neutral "I wonder..."
        "\"Are they your siblings, Jorunn?\"":
            j "Nope, found them in a basket one day when I was out for a swim!"
            y happy "Oh, really? What a coincidence! They look just like you."
            j "Don't they though? Haha, I'm just kidding. They're my sisters."
            y "Of course, haha."

        "\"Are they your children, Jorunn?\"":
            $ jorunn_points += 1
            j "Hmm? Oh, sure are! Carried them in my belly and everything."
            y shocked  "Really?"
            parvy "Ew! Gross!"
            j "Haha! No, just messing with you. These are my younger siblings."
            y happy "Ah, of course."

    parvy "...what kind of mer are you?"

    "Parvy circles me with a surprising amount of intensity."

    ny nervous "Can she tell I'm not a mermaid? Surely not, right?"

    y neutral "Oh, well, my name is-"

    show parvy smile with dissolve

    parvy "Are you from the capital?"
    parvy "Is that the kind of clothes they wear there?"
    show parvy happy with dissolve
    parvy shocked "I heard they live in houses made from rocks!"

    j happy "Alright you busybug, let's give our guest some space. She's had a long day."

    show parvy upset with dissolve

    parvy "Guh..."

    show parvy neutral with dissolve

    j "You must be pretty hungry too, huh, [y]? Let's go get some food, yeah?"

    y happy "That sounds wonderful."


    #SCENE CHANGE - Platform of Home

    scene bg jorvillage afternoon:
        align (0.5, 1.0)
        pos (0.5, 1.0)
        zoom 0.34
    with dissolve

    window auto hide
    show bg jorvillage afternoon:
        linear 3 pos (0.5, 1.64) zoom 0.34
    with Pause(3.10)

    show bg jorvillage afternoon:
        pos (0.5, 1.64) zoom 0.34

    window auto show
    $ speaking_char = "all"
    show jorunn at jorunn_right
    show unna at unna_left
    show parvy at parvy_center
    with dissolve

    ny mermaid neutral "I follow the family upwards towards a platform on top of the homes."

    y "Is there anything I can help with?"

    unna "Ah, don't worry about it, you're our guest! Go ahead and make yourself comfortable, we'll be done soon."

    $ speaking_char = "None"

    "Unna hands a basket over to Jorunn, who starts sorting through its contents."

    "It's obvious this is something they've done together many times."

    "..."

    # Pro mermaid:
    if promermaid >= antimermaid:
        ny nervous "Did the mermaids in the underground market have families like this? Did they eat like this too?"

    #Anti mermaid:
    if antimermaid > promermaid:
        "It's curious to see mermaids acting like this. It makes them feel so...human."

    ny neutral "..."

    parvy "Here."

    "Parvy hands me an empty bowl. She seems quite intent on staying by my side."

    y happy "Thank you."

    "They've made quick work of getting everything ready."

    #no dissolve for smooth transition
    show jorunn happy

    j "I'm sure it's not what you're used to, but help yourself to what you want!"
    $ speaking_char = "none"
    ny neutral "Right...this is my first meal as a mermaid."

    ny shocked "Where do I even start? There's a whole spread laid out - leafy greens, some things that look like fruit, and fish."

    ny nervous "Hang on...aren't those the same fish Jorunn stole from the prince? {w}Oh dear."
    ny neutral "Well, here goes nothing."

    #show text line is for debugging purposes
    $ makingfoodtext = "What should I add to my bowl?"
    menu makefood:
        ny happy "[ makingfoodtext ]"
        "Leafy Greens":
            if addfood == 0:
                $ makingfoodtext = "What else?"
            elif addfood == 1:
                $ makingfoodtext = "And finally..."
            $ greens += 1
            $ addfood += 1
            if greens == 1:
                "I add some greens to the bowl. If you look at it from here, it kind of looks like lettuce."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if greens == 2:
                "I add more greens to the bowl. My meal is starting to look like a salad."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if greens == 3:
                "I add even more greens to the bowl. Being surrounded by sea plants must have really made me crave some greens."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                jump makefood

        "Sea Fruit?":
            if addfood == 0:
                $ makingfoodtext = "What else?"
            elif addfood == 1:
                $ makingfoodtext = "And finally..."
            $ fruit += 1
            $ addfood += 1
            if fruit == 1:
                "I add some blue fruits to the bowl. I bet they'll taste berry good."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fruit == 2:
                "I add another fruit to the bowl. These are smooth and yellow. They'll pear nicely with the blue fruits."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fruit == 3:
                "I add one last kind of fruit to the bowl. My bowl looks grape! Fruitful, even. How very a-peeling."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                jump fooddone
        "Fish":
            if addfood == 0:
                $ makingfoodtext = "What else?"
            elif addfood == 1:
                $ makingfoodtext = "And finally..."
            $ fish += 1
            $ addfood += 1
            if fish == 1:
                "I add some fish to the bowl. They've been filleted rather neatly."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fish == 2:
                "I add more fish to the bowl. This meal is starting to look rather fishy."
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                if addfood == 3:
                    jump fooddone
                else:
                    jump makefood
            if fish == 3:
                "I finish off the bowl with even more fish. I'm still not sure what kind of fish this is. Oh well!"
                #show text "I've added [greens] leafy greens, [fruit] fruit and [fish] fish." at topright
                jump fooddone
    label fooddone:

    #Bowl Outcomes

    #One of each
    if greens == 1 and fruit == 1 and fish == 1:
        "This is a nice, well-rounded meal."
        $ speaking_char = "Unna"
        "It seems Unna chose the same as me. I guess she isn't much of a picky eater either."

    #Two leafy greens
    if greens == 2:
        "I've made a bowl filled with leafy greens."

    #Three leafy greens
    if greens == 3:
        "There could not be more green in this meal. This is a salad bowl to end all salad bowls."
        $ speaking_char = "Jorunn"
        "It seems Jorunn chose the same as me. I wonder if he's a picky eater?"

    #Two fruit
    if fruit == 2:
        "I've made a bowl filled with fruit."

    #Three fruit
    if fruit == 3:
        "There is so much fruit in here. Did I overdo it?"

    #Two fish
    if fish == 2:
        "I've made a bowl with lots of fish."
        $ speaking_char = "Parvy"
        show parvy smile with dissolve
        "It seems Parvy chose the same as me. She looks pretty pleased to see my bowl."

    #Three fish
    if fish == 3:
        "The fish fillets are staring at me from inside the bowl."
        ny shocked "...Why did I add so much fish?"
        show jorunn smile with dissolve
        j "..."

    #No fish
    if fish == 0:
        $ jorunn_points += 1
        j "Not a fan of fish, huh?"

        y "Well...you could say I've had enough fish to last me a lifetime."


    #MEAL END
#    hide text
    ny neutral "I take a bite of the food."

    parvy "How is it? Do you like it?"

    y happy "It's good! Thank you for the meal."

    parvy "What kind of food do you eat where you're from?"

    y "We have something similar."

    show parvy smile with dissolve

    parvy "Are you actually from the capital? Did you get your outfit there?"

    show jorunn neutral
    j "Parvy, all these questions for [y] and none for me, huh? I'm hurt! Don't you wanna know what I've been up to?"

    show parvy neutral
    parvy "I see you all the time!"

    "Jorunn makes an exaggerated motion like he's been struck." with vpunch

    show jorunn shocked with dissolve

    j "Arugh...[y], you've stolen my sister!"

    y veryhappy "Hehe."

    show jorunn smile

    unna happy "You know, Parvy is usually pretty shy. I guess she's taken a liking to you!"

    "My outfit must really stand out...I wonder how far the capital is from the village."

    show parvy smile

    parvy "And what's in your bag, [y]? Do you collect anything?"

    y "My bag?"

    ny shocked "Now that she mentions it, Prashadi's spell did give me a purse. I haven't really had the time to think about it."

    ny happy "Well, let's see!"

    "Opening it reveals..."
    show black:
        alpha 0.35
    show camera_mermaid at atcamera:
        zoom 0.18
    with dissolve

    parvy "What is it?"

    y shocked "It's...my camera."

    "How is this even possible?"

    "It looks a little different, but the weight of it feels familiar in my hands. It's definitely my camera."

    hide camera_mermaid
    hide black
    show parvy shocked
    with dissolve

    parvy "A camera?"

    y "Well, uh..."

    $ speaking_char = "all"

    "They're all staring at me curiously."

    "Would it be okay to tell them? It doesn't look like a normal camera anymore."

    y "It takes pictures. So you can have a physical copy of your memories."

    show parvy smile with dissolve

    parvy "How does it work?"

    y "You just point it at what you want to remember, then..."

    menu:
        "Take a picture of the family.":
            play sound "audio/sfx_cameraShutter.ogg" volume 0.8
            show camera with irisin
            hide camera with dissolve
            show black:
                alpha 0.35
            show photo_black at atphoto
            show parvy shocked
            show jorunn shocked
            with dissolve

    parvy "...!"

    show jorunn smile

    "A photo pops out from the top of the camera."

    y shocked "Wow..."

    "It really worked. And the colors don't even bleed."

    "This is incredible! I never thought I'd be taking photos underwater."

    hide photo_black
    hide black
    with dissolve

    "The three siblings are photographed staring curiously into the camera. Parvy looks especially shocked."

    y happy "Here. What do you think?"

    "I hand the photograph to them."

    show parvy happy with vpunch

    parvy "That's...that's so cool!"

    parvy "Unna, look it's us! We're on a little square!"

    unna "Wow, how did you do that? Is it a magic item?"

    y veryhappy "Haha...something like that."

    y happy "The 'little square' is called a photograph. It's for you! Please keep it."

    unna "Thank you! We'll take good care of it."

    parvy "Look, Jor! Isn't this amazing?"

    j "...It is, isn't it? Don't forget to thank [y] now."

    parvy "Thank you, [y]!"

    "Parvy's eyes are shining. She looks like she has a lot more questions to ask."

    show jorunn neutral

    j "Well, it's getting late, isn't it? Why don't we head inside? You must be exhausted, [y]."

    y "Oh, yes. I think that's a good idea."

    ny neutral "What a strange day this has been. I am rather exhausted."

    show jorunn smile with dissolve

    j "You can hunker down in my room for the night."

    j "Follow me. I'll show you the way."

    unna "I'll clean up here. Parvy, you should head to bed too."

    show parvy upset

    parvy "What? No! I want to help."

    j "Just don't stay up too late, okay? Come on, [y]."

    y happy "Goodnight, everyone!"

    "I wave goodbye to the sisters and follow Jorunn. He takes me to one of the rooms beneath the platform."

    #SCENE CHANGE - Jorunn's Room

    scene bg jorbedroom with dissolve:
        fit "contain"
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    scene bg jorbedroom:
        fit "contain"

    show jorunn neutral
    show jorunn neutral:
        xpos 0.47
        ypos 930
        zoom 1.3
    with dissolve

    j mermaid neutral "It's just in here."

    "Jorunn's room is small but comfortable."

    $ speaking_char = "Jorunn"

    menu:
        ny mermaid neutral "A thought occurs to me, but dare I ask...?"
        "\"Are we...sharing the room?\"":
            "Jorunn suddenly leans in closer, his hair brushing against my face."
            show jorunn neutral:
                ypos 930 zoom 1.3
                ease 0.3 ypos 1152 xpos 0.43 zoom 1.7
            with Pause(0.4)
            show jorunn teasing:
                ypos 1152 xpos 0.43 zoom 1.7
            with dissolve
            j "What, did you want to share?"
            y flustered "I, uh-"
            show jorunn smile:
                ypos 1152 xpos 0.43 zoom 1.7
                ease 0.3 ypos 930 xpos 0.47 zoom 1.3
            with Pause(0.4)
            show jorunn smile:
                ypos 930 xpos 0.47 zoom 1.3

            j "Haha! Just kidding. I'll be sleeping in one of my sister's rooms for the night. You've got this room all to yourself."
            "...He seems to have a teasing streak, doesn't he?"
            show jorunn happy with dissolve
            j neutral "I'm sure you could use some time to yourself. Besides, we'll be seeing each other a lot now anyways."
            y happy "That's true. Thank you, Jorunn."

        "\"Thank you.\"":
            y "I appreciate you letting me stay here."
            pass

    j "Course! Least I can do for my partner in crime."

    show jorunn neutral with dissolve
    j "We have to wake up early, yeah? So get some rest while you can."

    j "I'm going to help clean up. Good night, [y]!"

    hide jorunn with dissolve

    "Jorunn leaves, and I'm alone once more."

    #CHOICE
    menu:
        y mermaid neutral "What should I do?"

        "Go to sleep.":
            pass

        "Look around the room first.":
            $ snoop = True
            "I'm pretty tired, but a quick look around the room couldn't hurt, right?"
            "It's not like it's everyday I get to see what a mermaid's room looks like."
            ny nervous "I hope Jorunn won't mind."
            ny neutral "..."
            y shocked "What's this?"
            "There's a small box tucked away on one of the shelves."

            menu:
                "I wonder what could be inside?"
                "Open the box.":
                    ny neutral "..."
                    "..."
                    ny frustrated "Ugh...The lid's rather stubborn."
                    ny neutral "After a few more tries, the box finally opens."
                    "Inside is…"
                    show black:
                        alpha 0.7
                    show bracelet at atphoto:
                        xpos 470
                        zoom 2
                    with dissolve
                    y "A bracelet?"
                    "Come to think of it, Jorunn and his family were all wearing bracelets. I wonder why this one is hidden away?"
                    y nervous "I'd better put this back..."
                    hide black
                    hide bracelet
                    with dissolve
                "Don't open the box.":
                    y neutral "No, I'd better not."
                    "Even if I'm curious about what's inside, opening it might be going too far."
                    "I put the box back on the shelf."


    ny sad "I can feel my eyes start to grow heavy. I guess everything is finally catching up to me."
    ny neutral "Time to get some rest."
    scene bg black with Dissolve(2.0)
    stop music fadeout 1.0
    "..."

#(transition here for dream)
    play music bgm_skyllaCave volume 0.8
    scene bg underground market:
        fit "contain"
    show black:
        alpha 0.7
    with dissolve
    "..."
    "I'm at that underground market again."
    "..."
    "It feels like something is drawing me in."
    "..."
    "Where do I go?"

    menu:
        "Forward.":
            $ pickedforward = True
            "There's something I need to do here, something very important."
            "But what?"
        "Back.":
            $ pickedback = True
            "I need to go back...there's someone waiting for me."
            "But who?"

    "..."
    "Something is urging me to move faster."
    "..."
    "..."
    "But my legs feel like lead. I'm slowing down."
    "..."
    scene bg black with Dissolve(2.0)
    "No! I need to keep going!{w=1}{nw}"
    stop music fadeout 2.5
    "..."
    j "...!"
    j "[y]...!"

#(transition here)
    scene bg jorbedroom:
        fit "contain"
    play music bgm_capital volume 0.8
    $ config.side_image_tag = "june"
    ny mermaid shocked "I sit up in bed with a gasp." with vpunch

    show jorunn smile
    show jorunn smile:
        xpos 0.47
        ypos 930
        zoom 1.3
    with dissolve
    j "Good morning!"

    y "Ah...Jorunn? Hello."

    "I'm still in Jorunn's room...I must've been dreaming."

    show jorunn hesitant with dissolve
    j "You okay? You were talking in your sleep just now."

    y neutral "Oh, was I? Sorry. I think I was having a strange dream."

    show jorunn neutral with dissolve
    j "Well, with everything that's happening it'd be weirder if they were normal."

    j "You ready to go?"

    "Right. It's time to head ashore. I hope Prashadi keeps their word."

    j "We need to swim quietly so we don't wake up my sisters. Unna's a little prickly in the morning, if you can believe it."

    y "Do your siblings know we're leaving?"

    j "They know, yeah. I'm usually up this early when I head out, so this is nothing new."

    y nervous "Are you sure they'll be alright without saying goodbye?"

    show jorunn smile with dissolve
    j "Unna's good at looking after Parvy. Nothing for you to worry about, [y]."

    "..."

    menu:
        "I could say something..."
        "\"What if this was your last chance to say goodbye?\"":
            show jorunn neutral with dissolve
            y "Not that it is, but...I wish I could have said something more before…"
            "Before I fell into the sea..."
            show jorunn smile with dissolve
            j "It's okay. We will be coming back."
            ny neutral "Jorunn is resolute in his response."
            y "You're right."
            ny happy "No more doubts! We will get that relic, and we will make it back."
        "Don't ask.":
            "No, I'd better not. I don't want to dampen the mood."
            y neutral "I'm ready when you are."
            j "Great. Just follow my lead."

    "I follow Jorunn, swimming as quietly as I can."

#SCENE CHANGE
    scene bg jorvillage morning:
        align (0.5, 1.0)
        pos (0.5, 1.0)
        zoom 0.34
    with fade
    "We continue on through the village. At this hour, it's mostly empty."

    ny mermaid neutral "Mr. Mossyhead must still be asleep. Thank goodness."
    show jorunn smile at jorunn_center with dissolve
    "The villagers that notice us wave at Jorunn and wish him luck."

    "I guess he really does leave like this often."

#SCENE CHANGE

    scene bg sea:
        fit "contain"
    with fade
    "..."

    show jorunn neutral at jorunn_center with dissolve
    ny mermaid neutral "The two of us swim further on. The shore feels so far."

    "..."

    "I can see the outline of metal ships moving above us. We must be getting close to the port."

    j "The surface is busy this morning."

    "If I remember right, there's some isolated beaches further down the shoreline."

    y "We should keep going. I know a good place for us to surface."

    j "You got it!"

    "..."

    scene bg beach:
        fit "contain"
    with fade
    play music "audio/music_underwater.ogg" volume 1.0 fadeout 1.0

    "We arrive on shore at last, and I take in a breath of air."

    ny shocked "Oh! Prashadi’s spell worked! It appears they kept their word."

    "Is this really an illusion? I feel so...normal. Like I never fell off the boat to begin with."

    ny neutral "I lay down on my back to catch my breath, and Jorunn does the same beside me."

    show jorunn neutral with dissolve

    y shocked "...!"

    "Jorunn has changed too. It’s strange to see him with legs."

    y neutral "Jorunn, how are you feeling?"

    show jorunn hesitant

    j "Ah...achoo!" with screenShake

    show jorunn smile

    j "Well, I’ve been warmer that’s for sure."

    y "I could say the same."

    "Prashadi’s spell gave us clothes, but they’ve been soaked through with water."

    y "Don’t worry. We’ll dry off quickly once the sun comes up."

    "It is chillier here than I remember."

    "I think Hunter is the one who showed me this place. This is the same beach we used to play on as children."

    "Did the land ahead of us always feel so vast? How do we even begin searching through all of it?"

    "..."

    y "I don’t suppose you sense any relics nearby here, do you?"

    show jorunn smile with dissolve

    j "Can’t say that I do."

    y "Right, of course."

    ny nervous "There’s no way it would be that simple..."

    show jorunn happy

    j "But you know, when a mer uses a relic, it leaves an impression."

    j "The magic lingers, even if they’re not holding onto it anymore."

    y neutral "Do you think it’ll do the same with humans?"

    show jorunn neutral with dissolve

    j "Well, why don’t we go find out? It might make our search easier."

    y "Let’s check the market, then! I know lots of people go through that area."

    ny nervous "If we can find something there, then maybe we wouldn’t have to head to the eerier market underground."

    j "Let’s get going then. We aren’t far from the city, yeah?"

    y neutral "Right."

    "I quickly rise to my feet. Jorunn watches me and begins to do the same."

    show jorunn hesitant with dissolve

    "He’s moving his legs rather carefully."

    y shocked "Will you be alright to walk?"

    show jorunn smile with dissolve

    j "Well...there’s a first time for everything, right? Don’t worry, I’ll get the hang of it soon enough."

    menu:
        "Offer to help.":
            y neutral "Here, take my hand. I'll help keep you balanced."
            show jorunn teasing with dissolve
            if takehand:
                j "You want to hold my hand again so soon, huh, [y]?"
                y "Huh? I just thought you could use the help!"
            else:
                j "You change your mind about holding my hand, huh, [y]?"
                y "That’s different!"
            show jorunn neutral with dissolve
            "With my help, Jorunn takes a few steps across the sand. He seems to have gotten the hang of it rather quickly."
            y "You’re a natural at this!"
            j "Ah, that’s too bad though. I was hoping to hold your hand a bit longer."

        "Let him be.":
            "Jorunn takes a few slow but steady steps. He seems to get the hang of it rather quickly."
            show jorunn neutral with dissolve
            y happy "You're a natural!"
            show jorunn smile with dissolve
            j "Well, I have a pretty lady to keep up with, don’t I?"

    show jorunn happy with dissolve
    j "Anyway, let’s be off, yeah?"

    y "Before we go...you should know that there are mermaid hunters in the city too."

    j "I can’t say I’m surprised. Don’t worry, we’ll just have to be careful, right?"

    y "Right."

    "...I hope it will be that easy."

    "It’s not just Jorunn who’s a mermaid. I can’t forget that my human body right now is just an illusion too."

    "If we ran into Hunter or Grandfather, I’m still not sure what I would do."

    novisualhunter "...[y]?"

    ny shocked "I know that voice..."

    hide jorunn
    show hunter shocked at hunter_center
    with dissolve

#    ny shocked "I look over to see Hunter standing just a few feet away from me."

    h "You're… {i}alive?{/i}"

    $ finished_demo_jor.grant()

    jump endofdemo


label start:
    $ hunter_points = 0
    $ prince_points = 0
    $ jorunn_points = 0
    $ cetus_points = 0
    $ promermaid = 0
    $ antimermaid = 0

    #lower music when voice line is playing
    default preferences.emphasize_audio = True
    jump get_name

label get_name:
    scene bg black

    show text "My granddaughter.{w}":
        align (0.5,0.5)
    with dissolve
    pause
    show text "It's getting warmer here. Summer already now. {p}You used to love playing by pier here with me as a baby.{p} You remember that, birdie?{w}":
        align (0.5,0.5)
    with dissolve
    pause
    show text "You must be tall enough to go on the boats by yourself now.{w}":
        align (0.5,0.5)
    with dissolve
    pause
    show text "I miss you. I hope to you see again one day.{w}":
        align (0.5,0.5)
    with dissolve
    pause
    hide text with dissolve
    show side june neutral at farleft with dissolve:
        yalign 0.1

label enter_name:
    $player_name = renpy.input("What is your name?", default = "June", length=15)

    $player_name.strip

    if player_name == "":
        $ player_name="June"

    #Name check?
    menu:
        "Is [y] correct?"
        "Yes":
            jump prologue
            hide side june neutral with dissolve

        "No":
            jump enter_name

#PROLOGUE
label prologue:
    #TODO SCENE ?
    scene bg choppywave
    show noise:
        alpha .3
    with dissolve

    play music "audio/music_storm.mp3" volume 0.4
    play sound "audio/sfx_wavesChoppy.ogg" volume 0.6 loop

    $ config.side_image_tag = "june"
    y shocked "It was sunny only moments ago! What is this?"

    show hunter silhouette with dissolve

    u "Blast...I've sailed us right into a sea witch's storm! Hold onto something!"
    "The ship creaks as he tries to turn it back towards the port, but the waves are unrelenting."
    "Something stirs in the back of my memory as I stare down into the waves below."
    "I can see something glowing through the wind and rain."

    #SCREEN SHAKE
    u "[y!u]!" with screenShake
    #u "!!!" with screenShake
    $ config.side_image_tag = "june"
    "I try to reach for it, forgetting myself for just a moment."

    #SFX - SPLASH
    scene bg black with vpunch
    play sound "audio/sfx_splash.flac"

    #SCENE CHANGE - (Underwater / Black)
    stop music
    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "Regret floods my mind, but it's too late."
    "I can feel myself fading..."
    jump get_name

#CHAPTER 1
label chapter1:
    #SCENE = CG (Train)
    scene bg black with dissolve
    play music "audio/music_town.mp3" fadein 1.0

    "Salty air...I remember how I would try to stick out my tongue to taste it."
    if not renpy.seen_image("cg train"):
        scene cg train with dissolve
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        scene cg train with dissolve
    "I was a child the last time I did something as silly as that."
    "It's been at least ten years since I've seen the ocean."
    "I used to visit quite often over the summer as a child. Grandfather would always be so excited to have me over."
    "It's been over ten years since I've last seen him, too."
    "Perhaps it's just because I missed him after being without contact for so long, but..."
    "Now I'm returning to Aquantis again, just to see him."
    "I can't really remember why my mother stopped taking me to see Grandfather."
    "Even though I'm now a grown woman, she refuses to say why."
    "...And Grandfather is the only other one with answers."
    conductor "Please gather all personal belongings, we are arriving at Aquantis Station!"

    "The screeching of the brakes signal the train to a stop."
    #SUBTLE ZOOM IN FROM CENTRE
    window auto hide
    show bg shabby town:
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    show bg shabby town:
        zoom 1.0
    $ config.side_image_tag = "june"
    y neutral "At last. Hello, Aquantis!"
    "As soon as I exit the train car, I let the shutter of my camera go off, taking a picture."

    menu:
        "Take a picture of..."
        "The people outside":
            play sound "audio/sfx_cameraShutter.wav"
            show camera with irisin
            hide camera with dissolve
            y "Let's see how it turned out!"
            # Image of picture here
            y "Everyone's dress is so modern and lightweight."
            y "I'm not Inland anymore, that much is clear."

        "The town around":
            play sound "audio/sfx_cameraShutter.wav"
            show camera with irisin
            hide camera with dissolve
            y "Let's see how it turned out!"
            # Image of picture here
            "A quaint assortment of homes and shops descend down the hill that leads to the harbor."
            y "This part of town has a great view of the sea."

    "The letters Grandfather sent had his address, though it would be helpful to ask for some directions. The harbor city is huge."
    y "Excuse me- sir! Hello?"
    "He ignores me, walking away from the station."
    "I try to ask a few more people, but no one wants to give me the time of day."
    ny huffed "Trying to grab anyone's attention around here seems impossible! They all just ignore me."
    "Were they so unfriendly to people from outside when I was younger? {w}I can't remember."

    #SCENE CHANGE - (Shabbier part of Town)
    scene bg shabby town

    "The further I walk down from the top of the city, the more and more the atmosphere seems to change."
    "Rather than being ignored, it seems I'm attracting an uncomfortable attention."
    "Their gazes feel heavy on me as I walk by."
    "It looks like these parts have fallen into harder times. When I was younger I remember it being more lively and nice, but now, it feels gloomy and unwelcoming."
    badguy "Tch, inlanders. What is someone like her out here for?"
    badguy "Inlander? Oy, you don't see many of them. And she's got a fancy one of those picture devices, that could land us a nice bit of coin, aye?"

    #SPRITE CHANGE (Annoyed Expression)
    $ config.side_image_tag = "june"
    ny huffed "Are they referring to my camera? They're hardly being secretive about wanting to rob me!"
    "I quickly walk away from the men watching me, holding my camera closer."

    #SCENE CHANGE - (Shabby Market [Zoomed In])
    #SUBTLE ZOOM IN FROM CENTRE
    window auto hide
    show bg shabby market:
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    show bg shabby market:
        fit "contain"
    #play sound "audio/sfx_shabbycrowd.mp3" volume 0.5 loop
    #make this a more occasional/easygoing market sfx
    ny neutral "I suddenly find myself at a market."
    "There are so many interesting things to see."
    menu:
        "What catches your eye?"
        "The wooden newsboard":
            $ seastorm = True
            "There's a board filled with notices and posters here."
            "Beware of sudden sea storms..."
            "Deadly storms that strike with no rhyme or reason - use caution when traveling without seasoned sailors."
            # Show propaganda poster here

        "Children playing in the street":
            $ childrenplaying = True
            "The children are playing some kind of game."
            kid "I want to be the mermaid hunter this time!"
            kid "No way, it's my turn!"
            y "How cute."
            kid "I don't wanna be no stinkin' fish! I'ma be a hunter!"
            "I wonder if I ever played something like that when I was young here."

        "The paperboy":
            $ newspaper = True
            paperboy "Extra, extra! Read all about it!"
            "I purchase a copy of the weekly news."
            "Several Fishing Companies Absorbed by Morrowe Family: What Will They Do Now?"
            y "Morrowe...that name sounds familiar."
            y "But where have I heard it from..?"
            "I tuck the newspaper in my coat for later."

    "There seems to be friendlier townsfolk around now that I've reached the market."

    "Where do I start...?"
    menu talktownsfolk:
        set menuset
        "Talk to..."
        "Elderly woman":
            y " Good day to you, ma'am. I apologize for the disruption, but could I trouble you for directions?"
            "The woman turns to me. She has a crazed look on her face."
            woman "Knock knock."
            y "Pardon?"
            woman "Knock knock."
            y "Oh, I know this one. Who's there?"
            "Her glazed eyes stare unblinkingly at me."
            woman "Knock knock."
            "…"
            y "Uh…knock knock?"
            "The woman grins toothily, looking pleased with my response."
            woman "Knock knock!"
            #bolding makes it look weird
            "It doesn't seem like she's trying to tell me a joke at all."
            "I wonder if I should show her the address on the letter."
            "Even so, this is really getting nowhere..."
            "Surely there are others around who can help me find Grandfather?"
            y "Have a good day, ma'am."
            "I quickly walk away from the strange woman, though I can't help but feel like whatever she kept repeating is important somehow."

            jump talktownsfolk

        "Child with toy":
            y "Hey, there! Do you know where I could find this area?"
            "The child is holding a plush octopus tightly. It looks well-loved."
            "I show him the address on the letter, and he glances at it."
            kid "Oh, I know that place!"
            "The child's eyes gleam proudly with excitement and he hugs the octopus toy tighter against his chest."
            kid "That's near the west alley. My mama says I can't play over there."
            kid "She says it's full of bad people."
            "He gives me a look."
            kid "Are you bad people?"
            y "No, I'm just looking for someone who lives here."
            "I smile at him reassuringly."
            y "Thank you for your help."
            "The child nods happily."
            kid "No problem, lady!"
            "He dashes off with a giggle."
            "I have no choice but to find someone else for more information."

            jump talktownsfolk

        "Fishmonger":
            #SPRITE CHANGE (??? Expression)
            ny shocked "I just hope I'm not expected to buy the fish covered in flies."

            #SCENE CHANGE - Shabby Market (fishmonger npc sprite)
            y "Good day to you sir. I'm sorry for disrupting you, but-"
            fishmonger "Bass or tilapia?" with vpunch
            y "Oh- er, well...I'm not looking to buy fish right now. Could you please help me with the directions to-"
            fishmonger "Do I look like a map stand? I sell fish. Ya buy fish, then ya leave, ya get it?"
            y "I will pay you for the help! I'm just looking for this address."
            fishmonger "I ain't gonna be telling any airsick in-landler how to get—"
            "Before he can deny me again, I show him the bottom half of the letter where the address is clearly written."
            "He squints at the paper."
            fishmonger "What did ya say ya name was again?"
            y neutral "It's [y] Finch."
            fishmonger "Finch, ya say..."
            "He scratches his chin and sighs."
            fishmonger "The code for that wall's five, three, four. An' remember to pause in between!"
            fishmonger "That's all I know, and all I'll say."
            "He stares at me with a glimmer of greed in his eyes."
            fishmonger "Payment?"
            "Clearly, the only language merchants speak is money..."
            y "Oh, yes. Thank you so much for the help."
            "That was far from helpful!"
            "But, I leave him a fair amount of coin for his trouble anyway."
            "Perhaps I will have better luck with someone else."

            jump talktownsfolk

    #SCENE CHANGE - Brick Wall
    "It seems I have spoken to everyone I can in the area."

    "According to what I've been told, I need to go to the west alley and knock on the wall."

    "The code was… five, three, four?"

    "That really isn't much to go off of. People have such an odd way of giving directions in Aquantis."

    "Still, it's more than what I started with."

    scene bg brickwall
    $ config.side_image_tag = "june"
    ny neutral "I arrive at the west alleyway. It's a rather nondescript path."
    "Upon reaching the end, I make a left turn down to see a brick wall. It has an odd discolouration unlike the rest."
    "This must be the wall the merchant spoke of. "
    "Well."
    "I stare at the wall for a few moments. This is certainly not something I had planned for this trip."
    "I suppose I'll just have to give it a go."

    menu knocking:
        "What was the code..?"
        "3":
            ny huffed "No, that doesn't seem right..."
            ny neutral "Let me try again."
            jump knocking
        "4":
            ny huffed "No, that doesn't seem right..."
            ny neutral "Let me try again."
            jump knocking
        "5":
            menu:
                "Next was..."
                "3":
                    menu:
                        "And finally..."
                        "3":
                            ny huffed "Was that it? Nothing is happening."
                            ny neutral "Let me try again."
                            jump knocking
                        "4":
                            jump afterknocking
                        "5":
                            ny huffed "Was that it? Nothing is happening."
                            ny neutral "Let me try again."
                            jump knocking
                "4":
                    ny huffed "No, that doesn't seem right..."
                    ny neutral "Let me try again."
                    jump knocking
                "5":
                    ny huffed "No, that doesn't seem right..."
                    ny neutral "Let me try again."
                    jump knocking

    label afterknocking:

    "There is no response at first, but..."
    ny shocked "Suddenly, the wall is pulled back."
    "With cautionary steps, I move closer."
    stop music fadeout 5.0

    #SCENE CHANGE - Black Screen
    scene bg black with slideawayright
    #note: this could be somehting like....better
    "It closes the moment I enter. It must be an ancient elevator, rusted and old."
    #SFX -  Elevator
    play sound "audio/sfx_elevator.wav" volume 0.1
    "The rickety elevator descends down for a while. I start to regret stepping inside - who knows what I would find so far down?"
    "..."
    "..."
    "..."
    #SFX -  Elevator
    play sound "audio/sfx_elevator2.wav" volume 0.1
    "Until it finally comes to a stop, the door opens, and I am greeted with a new world."

    #SCENE CHANGE -  Underground Black Market Faire
    play music bgm_blackMarket volume 0.4
    play sound "audio/sfx_crowd.wav" volume 0.009 loop
    #scene bg underground market with slideawayleft
    #ZOOM IN ON SPECIFIC PARTS WITH FADES TO BLACK
    window auto hide
    show bg underground market:
        subpixel True pos (0.73, 3.89) zoom 2.0
    with dissolve
    with Pause(0.75)
    show bg underground market:
        subpixel True pos (2.11, 2.16) zoom 1.50
    with fade
    with Pause(0.75)
    show bg underground market:
        subpixel True pos (-0.28, 3.43) zoom 2.0
    with fade
    with Pause(0.75)
    #SUBTLE ZOOM IN FROM CENTRE
    show bg underground market:
        fit "contain"
        subpixel True pos (0.0, 1.0) zoom 1.05
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with fade
    with Pause(1.75)
    show bg underground market
    "It's almost like a circus, or a fairground. Many merchants' booths have strange knick-knacks begging to be looked at."
    "It's hard to make out any faces. No one here seems keen to be recognized."
    "My eyes follow every gleaming thing on display."

    y shocked "This is incredible..."
    "As I walked around in awe, my eyes catch on a stand of tropical flowers arranged in a beautiful pattern."
    y "Mother would love to see this..."
    "My hand reaches for my camera once more."

    #this zooms in on him centered
    window auto hide
    show hunter neutral:
        xalign 0.5
        ypos 0.0
        parallel:
            Null(694.0, 699.0)
            'hunter neutral' with dissolve
        parallel:
            zoom 1.0
            linear 0.80 zoom 1.5
    with Pause(0.90)
    show hunter neutral:
        zoom 1.5
        ypos 0.0
    window auto show

    uhunter "Careful where you point that thing. I wouldn’t take your camera out here ‘less you want to leave in a barrel."
    "I freeze as a stranger’s hand reaches over to cover my own ."
    uhunter "Thought I saw a familiar face in the crowd. Didn't know it was you, [y] Finch."
    show hunter neutral:
        xalign 0.5
        ypos 0.0
        ease 0.2 zoom 1
    with vpunch
    ny shocked "I turn to see who the man is behind me. How does he know my name?"
    "I quickly yank my hand away."
    y "Who are you, exactly?"
    uhunter "Bit rude to greet a friend like that, isn't it?"
    "He scoffs and shakes his head."

    #TODO SPRITE CHANGE - Hunter Disappointed
    uhunter "You don't remember your old playmate? I'm hurt! After all these years, I didn't once forget about you."
    y neutral "I haven't been in this part of Aquantis before. You must have me mistaken for someone else."
    uhunter "Ha- this isn't your first time here. Don't appreciate being treated like a stranger, though I s'pose it's been awhile."
    "Bending down to my level, the stranger looks me right in the eyes."
    uhunter "Jogging anything in that noggin? I've grown up a bit since you've last seen this mug...how 'bout it?"
    "He stares at me for a moment before the realization hits."
    uhunter "Ah, that's right."
    #if we go mask route, just pop this back in but it doesn't make sense right now
    #"He pulls down his mask to reveal a handsome and somewhat-familiar face."
    show hunter neutral:
        xalign 0.5
        ypos 0.0
        ease 0.7 zoom 1.5
    pause 0.8
    uhunter "Hunter {w=0.1}Aubrey{w=0.1} Morrowe."
    if newspaper:
        ny shocked "Oh, Morrowe! That means..."
    y neutral "...Hunter?"
    h "That's my name, yes."
    "He looks positively delighted to hear me say his name."
    y "..."
    y shocked "Oh!"
    y neutral "Right, Hammy! You were so different when we were young!"
    "He deflates as soon as I say it."
    h "Ah, you still remember that nickname. Pity..."
    show hunter neutral:
        xalign 0.5
        ypos 0.0
        ease 0.2 zoom 1

    menu:
        "Tease him.":
            $ hunter_points += 1
            y "Well, Hammy, you don't leave my mind that easily!"
            h "Please, really, just Hunter is fine."
            y "But your face is so cute when I say it!"
            h "You..."
            "He looks away from me. I believe he is thoroughly embarrassed now."
            y "Of course, I'll call you Hunter. I'm just having my fun."

        "Let it be.":
            y "But of course, I'll just call you Hunter."

    "We used to play near the beach as children. If there was anyone I'd recall from my time here, it'd be him."
    "We were fast friends, though I can't remember much of what we did together. He was a strange little kid."
    h "At least you do remember me! It's been only about, what...ten years since we've last seen each other?"
    h "I'll be honest, never expected you to come back."
    "I do remember his smile when he was trying to show me shells or bugs he found on the beach."
    "As I look at him now, it seems like the only thing that remains is that smile."
    y "I came to see my grandfather, if you still remember him."
    h "Ah, family visit. Of course I still remember the old man. His hunting company practically owned half the market strip."
    h "Though he went into retirement a few years ago."
    "He tilts his head, gazing at me intently."
    h "Need some help finding your way?"
    y "Well, yes, if you wouldn't mind..."
    h "I'll take you. Just keep your camera out of view."
    h "And stop gawking at things like you've never been here before...People might think you're a spy or somethin'."
    "He unclips his cloak and throws it on top of my head. My nose is filled with the salty smell of the sea."

    #SCENE CHANGE - Black Screen
    scene bg black with screenShake

    h "Just keep it for now."
    y shocked "Hey-!"
    menu:
        "Thanks?":
            $ hunter_points += 1
            h "S'alright."
            h "Should keep you from standin' out too much."
            ny neutral "His cloak is heavy, but it's not a bad weight."
            "Amidst the salt, there's another scent my nose welcomes: a more subtle vanilla."
            "It's far more palatable. Maybe it's from Hunter's detergent?"


        "What's the big idea, man?":
            $ hunter_points -= 1
            h huffed "Sorry 'bout this."
            y "Don't just throw this dirty thing on me!"
            h "It'll help you blend in, yeah? You don't want people gettin' the wrong ideas about you."
            y "I suppose."

    h "Keep your eyes down so people can't clearly see your face...and avoid seeing things you shouldn't be looking at anyways."
    y shocked "Seeing things I shouldn't be..?"
    ny neutral "Things I am forbidden to see...? What could he be talking about?"
    "I feel a pressing need to see them - but a far more pressing urge to stay hidden from the rest of the townsfolk here."
    "I do as he asks, even if his cloak is starting to chafe on my shoulders and crush my hat."

    #SCENE CHANGE - Black Market
    scene bg underground market:
        fit "contain"

    show hunter neutral with dissolve

    "He takes my hand and gives a low hush, leading me through the crowd. I look down at my feet."

    #SFX - CROWD
    play sound "audio/sfx_crowd.wav" volume 0.04 loop fadein 2.5

    "He walks meticulously, carefully weaving through the crowds of people, and I try my best to keep in step with his strides."
    "But then, I see something tantalizingly curious out of the corner of my eye. Without thinking, I glance up."

    #SCENE = CG (Mermaid in Tank [Zoomed])
    scene bg black with dissolve
    show cg sushi:
        subpixel True pos (0,0) zoom 1.0
    with fade
    #show cg sushi with fade:
    #    fit "contain"
    "There is a pale but beautiful face in the dark, behind glass."
    "The further along we walk, the more of her face is revealed."
    "Her body is so human on the top, but her lower half...{w}scales, a tail that flows in the water and reflects off the dim lights around her."
    "A woman...{w}no, a creature that is equal parts human and fish."

    $ config.side_image_tag = "june"

    y neutral "Beautiful..."

    $ config.side_image_tag = "None"

    "Her long brown hair moves in the water just like her tail. She is mouthing something, banging on the glass, but I can't hear a word."
    "Her eyes seem to lock onto mine for a moment."
    "Is she asking for my help?"
    "Suddenly, my view of the rest of the stand is unblocked, and I am able to peek through the empty spot in the crowd. It is a fish hawker's stand."

    #SCENE = CG (Mermaid cut in half)
    stop sound fadeout 3.5
    window auto hide
    show cg sushi:
        subpixel True
        pos (0, 0) xzoom 1.0 zoom 1.0
        ease 3.10 pos (0, 0) xzoom 1.0 zoom 0.3334
    with Pause(3.10)
    show cg sushi:
        fit "contain"
        pos (0, 0) xzoom 1.0 zoom 1.0
    window auto show
    #so you don't unlock it until it zooms out
    if not renpy.seen_image("cg_sushi_unlock"):
        show cg_sushi_unlock
        hide cg_sushi_unlock
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    "Her sign reads 'Catch of the day'. Another mermaid, eerily similar to the face banging on the glass, on a table in front of the tank."
    "Except she is missing her body from the hip below; tail ripe for the taking by rabid customers, piece by piece."
    "As if she was just the catch of the day. Another fish for someone to eat for dinner."
    "I fight down the sudden bile rising up my throat and squeeze Hunter's hand, and he starts to walk faster through the crowd."

    scene bg black with dissolve:
        zoom 2.0
    camera:
        zoom 1.0
    scene bg underground market:
        fit "contain"
    with fade
    show hunter neutral with dissolve
    h "I said keep your eyes down, or people might see your face. You don't want them remembering what you look like."
    $ config.side_image_tag = "june"
    y neutral "I know."
    "I glance back for just a moment before turning back away."
    "The cruel reality of the world. There isn't much I can do about it."
    "To fill the air with something else, I ask Hunter a question."

    play sound "audio/sfx_crowd.wav" volume 0.009 loop fadein 2.5

    menu:
        "Do you hunt now, too?":
            $ hunter_points += 1
            h "Well, yeah, I do. It's the family business, though your family left it to mine."
            h "Your old man always talked about wanting you to come back to join him, but when he announced his retirement, he sold most of it to my mother instead."
            if newspaper:
                "I wonder if that was one of the deals the newspaper was talking about."
            y "I see."
            "I wonder how many mermaids die like that..."
            menu:
                "Thinking about it..."
                "I pity them.":
                    $ promermaid += 1
                    "I would be terrified if I were in their situation."
                    "If I were a mermaid, I would rather die in the sea, at home. Not here..."
                "That's just how it is.":
                    $ antimermaid += 1
                    "Grandfather and Hunter make their living in a world like this."
                    "Either the world floods over completely, or we keep our land safe."
                    "That's the way it is."

        "Have you actually...killed them before?":
            $ promermaid += 1
            h "Why do you sound so horrified? Don't be fooled by their appearances."
            h "I've seen them kill a man in the blink of an eye."
            h "They're monsters using human faces. They don't deserve your pity."
            h "...But yes, I have."
            y "..."

    stop sound fadeout 2.0

    #SCENE CHANGE - Port w/ Boats
    play music bgm_portTown fadein 2.0 volume 0.4
    #SUBTLE ZOOM IN FROM CENTRE
    window auto hide
    scene bg port:
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    show bg port:
        zoom 1.0
    play sound "audio/sfx_wavesCalm.ogg" loop volume 0.1 fadein 1.0
    play sound "audio/sfx_seagulls.ogg" loop volume 0.8 fadein 1.0
    "Once we make it outside the underground and I can finally see the sky again, the sun is already far along on its journey."
    "I hand Hunter his cloak, and he puts it back on."
    y neutral "It's afternoon already?"
    show hunter neutral with dissolve
    h "Wandering does that to ya. When did your train get here?"
    y "Early morning. My legs are aching to sit."
    h "We're almost there. Don't keel over on me, would you?"
    y "I wouldn't dream of it."
    "We're actually at the portside now, the edge of the country. Practically the edge of the world."
    "Ships are anchored near the shore. Fishermen and hunters alike line the dock, carrying supplies to and from the ships."
    "The ships are different than the ones I remember. These are large, made of steel, and produce steam."
    y shocked "Does Grandfather live on one of these ships?"
    show hunter neutral at slightRight with move
    h "The only one not made of steel, that one over there."
    ny neutral "Out on the furthest side of the docks is a large wooden ship. It sticks out compared to the rest, with its clothed sails, and ornate details."
    "It has clearly been maintained with a lot of pride and dedication."
    "I have a faint recollection of Grandfather owning  a boat, of course, but I thought I would remember more than that upon seeing his home."
    show hunter neutral at centre with move
    h "Well, keep moving along already. I thought you'd be more excited to see your Grandpa!"
    y "Hey, don't start shoving me- I appreciate the help, but you really don't have to follow me the whole way there."
    h "I have business with your old man, actually. Running into you was just a coincidence. Let's go!"
    y "Alright, alright, let's go."

    #SCENE CHANGE - Port w/ Boats (ZOOM)
    scene bg port
    "We board a small rowboat to take us there."
    camera:
        ease2 3.36 zoom 1.5
    "Before I know it, we arrive on deck, and Hunter walks towards the entrance of the ship's interior."
    "Ten years apart finally coming to an end. Perhaps my parents estranged us over a misunderstanding, and it will be a simple, happy reunion with no trouble at all."
    "I want to hear his side of it, regardless."
    "I want answers."
    camera:
        ease2 1.0 zoom 1.0
    pause 0.5
    show hunter neutral at right2
    with dissolve
    "Hunter knocks at the entrance of the ship."
    "There's some loud grunting and muffled swearing as the door opens."
    show grandpa neutral at Position(xpos=0.32) with dissolve
    g "I told you people I don't want any-"
    show grandpa surprised with vpunch
    stop music fadeout 1.0
    #SFX - waves (calm)
    "The old man stands frozen before me. He looks as though he's seen a ghost."
    y shocked "Grandfather...?"
    show grandpa happy at jumpin
    g "Oh, bless the stars...you got my letter? You're really here! My dear, sweet [y]!"
    show grandpa happy:
        subpixel True
        zoom 1.0
        linear 0.60 ypos 1.27 zoom 1.5
    with Pause(0.70)
    show grandpa happy:
        ypos 1.27 zoom 1.5
    "Suddenly, I'm caught in his embrace. He may be older, but his strength certainly has not faded." with vpunch
    "I hug him tightly in return. The wave of anxious anticipation I had moments before seems to vanish entirely."
    y neutral "It's been too long, Grandfather!"
    show grandpa happy:
        subpixel True
        ypos 1.27 zoom 1.5
        linear 0.20 ypos 1.0 zoom 1.0
    with Pause(0.20)
    show grandpa happy:
        ypos 1.0 zoom 1.0
    g "Oh, and I see the lad brought you here. Thank you my boy, get in here too!"
    h "Hah? Ey, that's not necessary-"
    g "Just 'cause you're a man now doesn't mean I can't still embarrass you like my own grandchild!"
    show grandpa happy at Position(xpos=0.64) with move
    "Grandfather traps Hunter too. Though Hunter groans, I can't help but laugh." with hpunch
    "Once he has squeezed the daylight out of us, he lets go."
    show grandpa happy at left2 with move:
        ease2 0.3
    g "Oh, just how many years has it been since I've seen the both of you together?"
    g "It's good to see you, little birdie."
    g "How's your mother? She never replies when I write to her."
    g "Nor has she ever let you reply to the letters I've sent you over the years..."
    "My heart sinks."
    y "Mother has been well, as well as Father. But, well..."
    y "She read the letters, but never let me see them. I only recently saw them myself."
    y "She let me keep the gifts you sent, but never the letters..."
    show grandpa neutral with dissolve
    g "Oh, Marie..."
    "He lets out a wistful sigh."
    g "Can't be helped, I s'pose. Come on, then! Let's get you settled in."

    #ADDITIONAL GRANDPA SCENE
    #scene bg gpa:
    #    anchor (24, 6) zoom 0.34
    #"wow"
    #show grandpa happy at left2

    #SCENE CHANGE - Black Screen
    scene bg black
    stop sound fadeout 2.0
    "Time just flies by, and before I know it, it's been a week."
    "Despite my best attempts, Grandfather has not been able to answer my questions."
    "Or rather...he doesn't want to."
    "He's avoiding any talk about my past."

    #SCENE CHANGE - Shabby Market
    scene bg shabby market with dissolve
    play music "audio/music_town.mp3" fadein 1.0
    show grandpa happy at left2 with dissolve

    "Today, Grandfather and I are shopping for the next week's supply of food before he meets a trader in the afternoon."
    show hunter neutral at right2 with dissolve
    "Along with Hunter, who just happened to be free."
    y neutral "...I don't know a thing about shopping for fish."
    h "It's easy enough. Just look at the colorin' and the smell."
    y "Color, I can do that. But I'd rather not have to smell them at all."

    # REMEMBER: variable to check if name is june - little birdie for any name other than june, little bug/junebug for june
    g "There's been worse smells, little birdie."
    show grandpa happy at jumpin
    show grandpa happy:
        ypos 1.0 zoom 1.0
    g "When ye've been on a ship for three days 'n three nights with ten dead mermaids and they're startin' to curdle in the sun, that's when the smell's bad! Har har!" with vpunch
    "I've learned some things from Grandfather in my time here."
    "He's quite proud of his history at sea with the mermaids."
    g "And dont get me started on sirens!"
    g "I only ever saw one in my career, and it damn near got my whole crew!"
    h "Yeah, right, old man. They've been deader longer than you've been alive."
    h "All you ended up with was an overgrown mermaid, not a siren."
    g "Har har har!"
    show grandpa neutral with dissolve
    g "But I s'pose you'll never get to see you a mermaid like that, would you..."
    "He also wishes I could've inherited his love for the hunt."
    y flustered "Sorry, Grandfather..."
    g "Nah, it don't bother me, little birdie. Don't worry about me, I know it ain't everyone's cup o' tea."
    y "It's alright."
    y "Say, Grandfather, when you get the time, can we please talk about that summer..."
    show grandpa surprised with dissolve
    g "[y!c]...right now? I thought ye were done with that business."
    y huffed "Grandfather, please-"
    show grandpa neutral with dissolve
    #ny "Hunter taps Grandfather on the shoulder."
    h "Oy, old man. She's open."
    "Grandfather pulls out his timepiece and flips it open."
    g "Ah, look at the time already. Can't keep 'er waitin'. The ship won't pay for itself!"
    hide grandpa with dissolve
    show hunter neutral at centre with move
    "Grandfather takes his leave. I can tell he's trying to be cheerful, but he still looks dejected."
    y flustered "Grandfather..."
    "Part of me wonders if it's because I keep asking about my past."
    "Out of habit, my hand finds my camera still sitting at my side, waiting."
    y "I wish I could find some way to cheer him up."
    ny huffed "And get him to talk..."
    h "Hmmh?"
    y neutral "Is there anything Grandfather likes that I could get him?"
    h "A present, huh?"
    h "Hmm, I have an idea."
    y "You do?"
    h "The old man'd be ecstatic to hear you go out to see one of his old haunts."
    h "How do you fancy a boat ride?"
    h "I can steer us to the safer part of the sea."
    y "That sounds perfect!"
    y "Oh, thank you, Hunter!"
    y "We're going to make Grandfather's day!"

    #SCENE CHANGE - Sea
    scene bg calmwave with dissolve
    stop music fadeout 1.0
    #SFX - waves (calm)
    play sound "audio/sfx_wavesCalm.ogg" loop volume 0.3

    "We embark on Hunter's fishing vessel, he at the helm and I at the edge of the railing."
    "The sea is calm, and the sun is shining down."

    show hunter neutral with dissolve
    $ config.side_image_tag = "june"
    h "I'm going to steer us towards the calmer places. Might be able to spot a 'maid goin' onto the rocks for a sunbathe."
    y shocked "Mermaids sunbathe? Really?"
    h "Yep. But if they spot my little skiff, the show's over."
    h "There's no safer place than this part o' the sea."
    hide hunter neutral with dissolve
    ny neutral "I keep my camera at the ready, not willing to let any photo opportunities pass me by."
    "My only experiences are with inland animal photography, but surely sea animals are no more difficult than capturing birds on film."
    "I wonder if I'll be able to catch a picture of a mermaid?"
    "The boat travels further out to sea, putting the port behind us."
    "I take the occasional picture of the waves or a seagull, but not much else enters my camera's lens."
    "No mermaids in sight."
    "Some time passes, and Hunter makes light conversation."
    show hunter neutral with dissolve
    h "How are you enjoying the view?"
    ny shocked "I'm about to respond to him, but the ship catches on the waves, and I stumble." with vpunch

    #SCENE CHANGE - view of the sea (stormy)
    play sound "audio/sfx_thunder.ogg" volume 0.9
    scene bg choppywave
    play music "audio/music_storm.mp3" fadein 2.0 volume 0.4
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.4 loop
    show hunter neutral with vpunch
    h "What the damn-"
    "The weather changes nearly in an instant."
    "I can't see a hint of blue in the sky."
    "Our perfect sailing day was covered by clouds of grey."
    y shocked "It was sunny only moments ago! What is this?"
    h "Blast...I've sailed us right into a sea witch's storm! Hold onto something, [y]!"
    if seastorm:
        "I remember reading something about this."
        "If this is a sea witch's storm..."
        "My hair stands on end just thinking about what devastation will ensue."

    hide hunter neutral with vpunch
    "The ship creaks as he tries to turn it back towards the port, but it seems to make no progress at all."
    "The lurching nearly throws me to the floorboards, but I grab the side of the ship just in time to stay upright."
    $ config.side_image_tag = "june"
    y shocked "Ah..."
    #SCREENSHAKE
    "Something stirs in the back of my memory as I stare into the waves. Something is glowing through the wind and rain."  with screenShake

    #TODO FLASHBACK CG for a second of baby prince and june
    y "Who...? This is familiar to me, but...?"
    #SFX - loud crash, screen shake
    play sound "audio/sfx_waveCrash.wav" fadeout 1.0
    show bg choppywave with screenShake
    #SFX - choppy waves
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.6 loop

    show hunter neutral with vpunch
    "The sounds of the waves and the wind make Hunter's words hard to hear."
    h "The waters are getting choppier, stay away from the ledge!"
    y shocked "I'll try! I can hardly stand straight!"
    hide hunter neutral with dissolve
    "He returns back to his position, eyes staying forward as the winds grow stronger."
    ny flustered "I want to listen to him, but in that moment, I imagine Grandfather's face from earlier today."
    show grandpa neutral
    show bg shabby market
    show noise:
        alpha .3
    with dissolve
    g "{i}But I s'pose you'll never get to see a mermaid like that, would you...{/i}"
    hide grandpa
    hide noise
    show bg choppywave
    with dissolve
    "Wouldn't he love to know I was out here where he was? Enjoying the sea and mermaids like he did?"
    "Wouldn't that bring me just that much closer to learning the truth?"
    "Surely he couldn't turn me away, then?"
    menu:
        "..."
        "Listen to Hunter.":
            # +Hunter points
            "I shouldn't take unnecessary risks..."
            "My life isn't worth a photo."
            if seastorm:
                "Especially if they're as deadly as the papers say they are."
            ny neutral "I move closer to where Hunter is, towards the back of the boat."

        "I can't give up on a picture.":
            "I can hardly see out, but I can't give up my quest for a picture."
            if seastorm:
                "Even if this is a sea witch storm, I'm sure we'll probably be fine..!"
            ny neutral "I hold my camera up, making sure my hand is ready to press the trigger once I see a mermaid."
            "The water laps at the edge of the boat ferociously."

    $ config.side_image_tag = "june"
    #SPRITE?
    play sound "audio/sfx_waveCrash.wav" volume 0.06 fadein 1.0
    $ renpy.music.set_volume(0.3, 2, 'music')
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.06 loop
    play sound "audio/sfx_hum.mp3" volume 1.5 fadein 1.0

    u "Come...come with me..."
    y shocked "What...?"
    u "O' ye of land to the queen of sea..."
    "My thoughts are hazy, and my body feels as though I'm floating."
    h "[y], what are you doing?!"
    u "Come with me..."
    u "...to the depths below..."
    "The singing feels as though it is only for my ears to hear alone, the waves calling out for me to sink in."
    "My legs begin to move on their own."
    h "Shit, it's a siren!? [y]!"
    show hunter neutral with vpunch
    "Hunter abandons his position at the helm of the ship and races towards me, but I can't imagine why."
    "An unimportant thought crosses my mind. I've heard of something like this before."
    "In fairy tales...sailors were sung to by the sea, only to be met with death..."
    hide hunter neutral with dissolve
    y "A siren's song."
    "At the edge of the boat now, my eyes look down below for the cause of my affliction, but the darkness below the waves are all I can see, and the voice all I can hear."
    "With all my might I hold tightly to the slippery railing that parts me from the water, and yet my body is going against my will to stay put."
    "I sit atop the ledge."
    "And just for a split moment I think I can hear Hunter calling my name before I take the plunge."
    stop music fadeout 1.0
    #SFX - SPLASH
    scene bg black with hpunch
    play sound "audio/sfx_splash.flac" volume 0.6

    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "The song stops, but my body is numb."
    "Regret floods my mind, but it's too late."
    "I can feel myself fading..."
    "..."
    stop sound fadeout 2.0

    #SCENE CHANGE - Black Screen
    scene bg black
    siren "After all these long years...you've finally returned home to me..."
    "..."
    "...Where am I?"
    play sound "audio/sfx_hum.mp3" volume 1.2 fadein 1.0
    siren "Hmm, hmm, hmm."
    "A strange voice is humming a familiar song."
    stop sound fadeout 1.0
    siren "Ah! You've woken up, little human."
    y "Blub!"
    "....Huh."
    y "Blub blub blub!"
    siren "Or, shall I say, little fish?"
    "Hands, impossibly large and glowing strangely, come down to cradle me."

    if not renpy.seen_image("cg skyllahands"):
        scene cg skyllahands with dissolve:
            zoom 0.343
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        scene cg skyllahands with dissolve:
            zoom 0.343


    #SCENE CHANGE - underwater cave (skylla's)
    play music bgm_skyllaCave volume 0.8
    $ config.side_image_tag = "june"
    "All at once I recognize her, or her voice at least. This is the same siren that caused me to go overboard."
    y fish neutral "BLUB BLUB BLUB!!!"
    siren "Ahaha! Oh, you cute thing. That's no way to speak to a lady!"
    $ config.side_image_tag = "None"
    "Try as I might, none of my words come out right."
    "And I've...{w}been turned into a fish by this siren!?"
    menu:
        "Stay very, very still.":
            $ cetus_points += 1
            $ prince_points -= 1
            "My body freezes up with fear."
            "I don't want to risk angering her."
            "Best to stay still and hope for the best..."

        "Get her!":
            $ prince_points += 1
            $ cetus_points -= 1
            "I try to swim at her, but an invisible wall stops me before I can get close enough to smack her." with vpunch
            "Near-invisible, I should say. The walls are shining."
            "A bubble?"

    scene bg underwater cave:
        zoom 0.5
    show skylla happy
    with dissolve
    $ config.side_image_tag = "june"
    siren neutral fish "Aw. You're hurting my feelings! Aren't you happy to see me?"
    siren "When Skylla calls, little mers are meant to follow."
    "Skylla..? Is that the name of this siren?"
    show skylla neutral:
        yalign 0.1
        ease 0.5 zoom 1.5
    "Suddenly she leans in closer. The look in her beautiful eyes turns dark and ravenous. A cold and instinctive fear shoots through my gut."
    s "There's no need to rush. We have all the time in the world together. And you'll give me what I want."
    show skylla happy:
        yalign 0.1
        ease 0.7 zoom 1
    s "Now, where did I put that pestle?"
    hide skylla neutral with dissolve
    pause 0.5
    "No matter how hard I press my hands - well, fins - against the bubble, I can't push through!"
    "I'm trapped. There's no doubt about it."
    "Am I cursed to stay like this...forever?"
    #stop music fadeout 2.0
    "At the thought, horror rolls through me like a wave. My body is all wrong, somehow warped into the wrong shape."
    "I have no hands to take pictures with.{w} No legs to run back home with.{w} No words to cry out with."
    "Forever? Like this?"
    "Or maybe...{w}am I going to die after being eaten as a special dinner course?"
    "Suddenly the memories of the mermaid market come to mind. Their bodies had been taken apart to become a cheap meal."
    "I am no different from them now.{w} Just as helpless."
    "From the distance I can hear the siren humming to herself as she swims to and fro around the cave."
    s "One piece at a time..."
    "No.{w} No, no, no."
    "Think, [y], think! There has to be a way out of here!"
    "If there's a way to turn a human into a fish, surely there's a way to turn a fish back into human, right?"
    "I glance around the cave I'm in."

    window auto hide
    camera:
        subpixel True
        parallel:
            pos (0, 0)
            linear 0.88 pos (-864, -7)
            linear 0.80 pos (-12, -475)
            linear 0.78 pos (-858, -480)
        parallel:
            zoom 1.0
            linear 0.22 zoom 1.61
    with Pause(2.56)
    camera:
        pos (-858, -480) zoom 1.61
    window auto show

    "It's dark here, hard to see. My new tiny eyes struggle to take in everything all at once."

    window auto hide
    camera:
        subpixel True
        pos (-858, -480)
        linear 0.83 pos (-804, -318)
    with Pause(0.93)
    camera:
        pos (-804, -318)
    window auto show

    "From what I can see there's only a path forward deeper towards the siren's lair. No windows, or whatever the underwater equivalent is."

    window auto hide
    camera:
        subpixel True
        pos (-864, -288) zoom 1.61
        linear 1.32 pos (-108, -102) zoom 2.04
    with Pause(1.42)
    camera:
        pos (-108, -102) zoom 2.04
    window auto show


    "There are what looks like glowing stones on the walls. What are the odds that they could magically explode?"

    window auto hide
    camera:
        subpixel True
        pos (-108, -102) zoom 2.04
        linear 0.40 pos (0, 0) zoom 1.0
    with Pause(0.50)
    camera:
        pos (0, 0) zoom 1.0
    window auto show

    "Come on, [y]! You can do better than this! What else is there?"

    show skylla happy with dissolve
    "Before I can finish the thought, the siren swims back towards me."
    "Her clawed fingers gracefully pop the bubble trapping me, but just as swiftly in that motion her hand clasps around me."
    "My heart begins rushing in my tiny body. She could pop me in an instant as well."
    show skylla:
        yalign 0.1
        ease 0.5 zoom 1.5
    s "Hold still now, cute thing. This won't hurt."
    play sound "audio/sfx_hum.mp3" volume 1.5 fadein 1.0
    "It's a lie. Strange magic begins to glow out of the siren's hands as she softly sings."
    "It's beautiful beyond words, but the moment it starts I start to feel a burning pain spreading across my body."
    s "It's okay! Don't be stubborn now. Come on, it's me!"
    "I can't even scream as I feel something tugging in me, as if the siren is reaching inside of my body and trying to pull me apart."
    show skylla angry
    "The moment I feel like I'm about to snap in two, a sudden blinding light flashes throughout the cave." with flash

    #FLASH EFFECT
    stop sound
    show skylla angry:
        yalign 0.1
        ease 0.02 zoom 1
    "The siren screams as she drops me, falling backwards."
    show skylla surprised
    s "No. No! This- this isn't right."
    "Once I blink the white spots out my vision I look up and find the siren staring at me with a shocked expression on her beautiful face."
    "Her hands are bleeding."
    "We both stare at each other, frozen, before I remember myself and swim away from her, pushing my tiny fins as hard as they can go."
    show skylla angry with vpunch
    s "You little {i}eel!{/i} Get back here!"

    y "Blub blub!!"

    "As if! Who in their right mind would do that!?"
    "Her tentacles try to grasp me, but I'm too small for them to catch."
    s "Fine! Be like that!"
    show skylla angryteeth
    play sound "audio/sfx_hum.mp3" volume 1.5 fadein 1.0
    "She begins humming to herself again, and a bolt of magic shoots out of her hands."
    "I twist away just in time, and the magic misses me and collides with one of the glowing stones on the wall of the cave." with vpunch
    hide skylla with dissolve
    stop sound
    "Time seems to slow down."
    "I hear a whirring coming from the stones like the sound of a shrill kettle, and in the next second the stones explode." with flash
    "The force sends me sprawling backwards in pain, but I don't have time to linger on it because the explosion has created a hole just big enough to squeeze through."
    stop music
    scene bg black

    "I swim as fast as I can. Faster than I've ever ran when I had legs."
    "My heart is thumping madly in my chest as I force my way through the debris. "
    "The sharper pieces scrape and cut through my fins but I barely pay them any mind as I keep swimming.{w} I think that if I had my voice I would be crying."
    "I can hear the siren cursing as I swim away, but eventually it shrinks into a distant shriek as I keep charging forward with all I have."
    "It doesn't matter where I go, just as long as it's far away from that awful witch!"

    scene bg sea with vpunch
    play music "audio/music_underwater.mp3" volume 0.7 fadeout 1.0
    "I stop to catch my breath after what feels like a lifetime."
    $ config.side_image_tag = "june"
    y fish neutral "Blub...blub..."
    "Now that the adrenaline has faded I feel exhausted. My body feels like it's been run over. Everything hurts."

    "Grandfather...Hunter...they must think that I'm dead by now."
    "At the thought of them, I suddenly feel overwhelmingly homesick. I need to tell them I'm alive!"
    "But...{w}how am I supposed to make it back to land?"
    "The only one that might be able to change me back is that siren, but there's no way I can go back there."
    "Before I can dive any further into those thoughts I hear voices approaching from a distance."
    "I quickly dart into some foliage to hide."

    #THIO AND JOR ENTER THE STAGE
    #Voice Lines Start (old, deleted the comments where they were due to script changes)
    show prince angry at farleft
    show jorunn sweat at right2
    show kelp with vpunch
    novisualthio "The further out you swim, the more guilty you are! Those fish belong to the Vanguard."
    novisualthio "Return them now, and your judgment will be fair."
    novisualjor "Well, I am sorry, my prince! But I was hoping I could skip the judgement part entirely!"
    novisualjor "Maybe you could ask your Vanguard to find you something else for your dinner? They could always go pilfer from other villages."

    "A 'prince'?"
    "Curiosity piqued, I lean over as much as I dare to stare at the new arrivals."

    hide kelp with dissolve

    show prince angry at farleft
    show jorunn sweat at right2
    with dissolve

    "Ahead of me, two mer-people are staring each other down."
    "One of them is a young man carrying a large net stuffed full of fish." (cb_name = "Jorunn")
    "The other one has fins unlike any other I've seen, a striking array of blue.{w} He has what looks to be a bodyguard hovering close to his side." (cb_name = "Prince Thioran")

    "Prince...? Bodyguard? Do mermaids really have that kind of thing?"
    up "Are you suggesting that {i}we{/i} sink to {i}your{/i} level?"
    uj "Oh no. No, of course not!"
    show jorunn glee
    uj "...But if the shell fits!"
    up "You thieving little-"

    show prince sweat at jumpin2
    show jorunn sweat at jumpin
    with vpunch

    "Just then, a loud rumble echoes through the area. The waters feel like they're slowly beginning to churn."
    guard "It's another sea storm, Your Highness! We must head back now before it picks up any further."
    show prince angry
    up "Dammit. Why now of all times..!"
    show jorunn glee
    uj "Well, I guess that's my cue! I'll be taking these home then. Goodbye!"
    "The rumble comes again, a bit louder this time. My heart sinks as I realize I might not survive whatever storm is coming." with vpunch
    "Do I approach the prince? Or perhaps the other fellow? Maybe this is dangerous...but they might be my only shot at getting help right now."

    if promermaid >= 1:
        "Anything would be better than returning to the sea witch."
    if antimermaid >= 1:
        "Should I even be trusting any of them? Chasing mermaids is how I became stuck like this."
    "Either way, they're both starting to swim away."

    #Follow Striking Prince
    #Follow Scrappy Boy (can't choose this yet, lol)
    menu:
        "What do I do...?"
        "Follow Striking Prince":
            $ prince_points += 1
            jump ch1_followprince
        "Follow Thieving Merman":
            $ jorunn_points += 1
            jump ch1_followjorunn
        "Find another way" if antimermaid >= 1:
            jump ch1_badend1

label ch1_badend1:

    hide prince angry
    hide jorunn glee
    with dissolve

    "There has to be another way out of this."
    "I can't trust either of them!"
    "Both merpeople swim away, and I'm alone."
    "Sort of..."
    "The other fish are swimming in a frenzy trying to get away from the vortex of water."
    "The seastorm gets louder and louder."
    "What if I hid in the seaweed again?"
    "The seastorm is getting closer with every moment I hesitate."
    "I know! I'll try taking shelter in a nearby rock formation!"
    "The problem is, everything is so far away from me."
    "It'll take far too long to reach shelter."
    "I try swimming anyway, as fast as I can go."
    "The storm roils behind me, and I feel myself being sucked into the whirling water..."
    "It's too late!"
    "The last thing I see before my eyes close forever is something large, crashing right into me."
    scene black with vpunch
    "Ravaged by the sea, I die."
    "BAD END 1."

    jump endofdemo

label endofdemo:
    stop music fadeout 2.0
    scene bg prashadi cave:
        fit "contain"
    show prashadi neutral
    with dissolve

    "..........."

    Pr "Hello there!"
    Pr "You've reached the end of the demo for Heart's Depth!"
    Pr "With this update, we've completely overhauled the game jam demo."
    show prashadi at jumpin
    Pr "From here on, expect updates to come in chapters!"
    Pr "Look forward to seeing the rest of our story, heh heh heh."
    Pr "Thank you so much for playing! Follow our game page for updates."
    Pr "There's so much more to see..."
    hide prashadi
    with dissolve
    play sound "audio/sfx_splash.flac"
    with Pause(1.0)

    #END OF DEMO!!!!!!!

    return

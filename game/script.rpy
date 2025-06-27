
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

    show text "{i}My dear granddaughter...{/i}{w}":
        align (0.5,0.5)
    with dissolve
    pause
    show text "{i}It's getting warmer here. Summer already.{/i}{w}":
        align (0.5,0.5)
    with dissolve
    pause
    show text "{i}You used to love playing by the pier with me as a baby.{p} You remember that, little birdie?{/i}{w}":
        align (0.5,0.5)
    with dissolve
    pause
    show text "{i}I miss you. I hope to you see again one day.{/i}{w}":
        align (0.5,0.5)
    with dissolve
    pause
    show text "{i}Love, Grandfather.{/i}{w}":
        align (0.5,0.5)
    with dissolve
    pause
    hide text with dissolve
    #show side june happy with dissolve: #FOR NEW JUNE SPRITE
    show side june neutral at farleft with dissolve:
        yalign 0.1
        #xzoom -1

label enter_name:
    $player_name = renpy.input("What is your name?", default = "June", length=15)

    $player_name.strip

    if player_name == "":
        $ player_name="June"

    #Name check?
    menu:
        "Is [y] correct?"
        "Yes":
            jump chapter1
            hide side june neutral with dissolve

        "No":
            jump enter_name

#CHAPTER 1
label chapter1:
    #SCENE = CG (Train)
    scene bg black with dissolve
    play music "audio/music_town.ogg" fadein 1.0 volume 0.9 loop
    play sound "audio/sfx_train-loop.ogg" fadein 2.0 volume 0.15 loop

    "Salty air...I remember how I would try to stick out my tongue to taste it."
    if not renpy.seen_image("cg_train"):
        scene cg_train with dissolve:
            fit "contain"
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        scene cg_train with dissolve:
            fit "contain"
    "I was a child the last time I did something as silly as that."
    "It's been at least ten years since I've seen the ocean."
    "I used to visit quite often over the summer as a child. Grandfather would always be so excited to have me over."
    "It's been over ten years since I've last seen him too."
    "Perhaps it's just because I missed him after being without contact for so long, but..."
    "Now I'm returning to Aquantis again, just to see him."
    "I can't really remember why Mother stopped taking me to see Grandfather."
    "Even though I'm a grown woman now, she still refuses to say why."
    "...And Grandfather is the only other one with answers."
    play sound "audio/sfx_steam.mp3" volume 0.3 fadeout 0.5
    conductor "Please gather all personal belongings! We are arriving at Aquantis Station!"
    stop sound fadeout 2.0

    #"The screeching of the brakes signal the train to a stop."
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
    "As soon as I exit the train car, I remove my camera from my purse to take a picture."

    menu:
        "Take a picture of..."
        "The townspeople.":
            play sound "audio/sfx_cameraShutter.wav" volume 0.3
            show camera with irisin
            hide camera with dissolve
            y "Let's see how it turned out!"
            # Image of picture here
            y "Everyone's dress is so lightweight."
            y "I'm not Inland anymore, that much is clear."

        "The seaside town.":
            play sound "audio/sfx_cameraShutter.wav"
            show camera with irisin
            hide camera with dissolve
            y "Let's see how it turned out!"
            # Image of picture here
            "A quaint assortment of homes and shops descend down the hill that leads to the harbor."
            y "This part of town has a great view of the sea."

    "Grandfather's address is on the letter I have, but it would be helpful to ask for some directions. The harbor city is huge."
    y "Excuse me- sir! Hello?"
    "He ignores me and walks away from the station without a glance."
    "I try to ask a few more people for help, but no one wants to even give me the time of day."
    ny huffed "Trying to grab anyone's attention around here is impossible!"
    "Were they always this unfriendly when I was younger? {w}I can't remember."

    #SCENE CHANGE - (Shabbier part of Town)
    #scene bg shabby town

    #june will be frowing a little in her neutral
    ny neutral "The further I walk down from the top of the city, the more the atmosphere seems to change."
    "It looks like these parts have fallen onto harder times. I remember it being a bit more lively."
    "Now, the street feels gloomy and unwelcoming."
    "Rather than being ignored, it seems I'm attracting uncomfortable attention."
    "The people's gazes feel heavy on me as I walk by."
    badguy "Tch, Inlanders. What's someone like her out here for?"
    badguy "Oy, you don't see many of them ‘ere anymore. And she got a fancy lookin' bag on her. That could land us a nice bit of coin, aye?"

    #SPRITE CHANGE (Annoyed Expression)
    $ config.side_image_tag = "june"
    ny huffed "They're hardly being secretive about wanting to rob me!"
    "I quickly walk away from the men watching me, holding my bag closer to my side."

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
    ny neutral "In my rush to escape, I find myself at a market."
    "There's more people here. And more to look at, as well."
    menu:
        "My eyes are drawn to..."
        "The newsboard":
            $ seastorm = True
            "There's a board filled with notices and posters here."
            y "Beware of sudden storms..."
            "Deadly sea storms can strike without rhyme or reason. Use caution when traveling without seasoned sailors."
            #Show propaganda poster here
            t "Those storms aren’t something to mess with. Stay safe if you’re heading out to sea, missy!"
            y "I will. Thank you!"
            "The man walks off and I browse over a few more posters before turning away."

            #needs a few more lines, include a townsperson

        "Children playing in the street":
            $ childrenplaying = True
            "The children are playing some kind of game."
            kid "I want to be the mermaid hunter this time!"
            kid "No way, it's my turn!"
            y "How cute."
            kid "I don't wanna be no stinkin' fish! I'ma be a hunter!"
            "I wonder if I ever played like that as a kid here."

        "The paperboy":
            $ newspaper = True
            paperboy "Extra, extra! Read all about it!"
            "I purchase a copy of the weekly news."
            "Several Fishing Companies Absorbed by Morrowe Family: What Will They Do Now?"
            y "Morrowe...that name sounds familiar."
            y "But where have I heard it from?"
            "I tuck the newspaper in my coat for later."

    "After looking around, it seems like the townsfolk are friendlier here."

    "Perhaps they can help me find Grandfather's address."

    "Where do I start...?"
    menu talktownsfolk:
        set menuset
        "Talk to..."
        "Elderly woman":
            y "Good day to you, ma'am. I apologize for the disruption, but could I trouble you for directions?"
            "The woman turns to me. She has a crazed look on her face."
            woman "Knock knock."
            y "Pardon?"
            woman "Knock knock."
            y "Oh, I know this one. Who's there?"
            "Her glazed eyes stare unblinkingly at me."
            woman "Knock knock."
            y"…"
            y "Uh...knock knock?"
            "The woman grins toothily, looking pleased with my response."
            woman "Gehehehe! The wall!"
            #bolding makes it look weird
            "It doesn't seem like she's trying to tell me a joke at all."
            y "Have a good day, ma'am."
            "I quickly walk away from the strange woman, though I can't help but feel like whatever she kept repeating is important somehow."

            jump talktownsfolk

        "Child with toy":
            y "Hey, there! Do you know where I could find this area?"
            "The child is holding a plush octopus tightly. It looks well-loved."
            "I show him the address on the letter, and he glances at it."
            kid "Oh, I know that place!"
            "His eyes gleam with pride as he hugs the octopus toy tighter against his chest."
            kid "That's near the west alley. My mama says I can't play over there."
            kid "She says it's full of bad people."
            "He gives me a look."
            kid "Are you bad people?"
            y "No, I'm just looking for someone who lives there."
            y "Thank you for your help."
            "The child nods happily."
            kid "No problem, lady!"
            "He dashes off with a giggle."
            "I have no choice but to find someone else for more information."

            jump talktownsfolk

        "Fishmonger":
            #ny shocked "I just hope I'm not expected to buy the fish covered in flies."

            #SCENE CHANGE - Shabby Market (fishmonger npc sprite)
            y neutral "Good day to you sir. I'm sorry for disrupting you, but-"
            fishmonger "Bass or tilapia?" with vpunch
            y shocked "Oh- er, well...I'm not looking to buy fish right now. Could you please help me with the directions to-"
            fishmonger "Do I look like a map stand? I sell fish. Ya buy fish, then ya leave, ya get it?"
            y huffed "I will pay you for the help! I'm just looking for this address."
            fishmonger "I ain't gonna be telling any airsick Inlandler how to get—"
            "Before he can deny me again, I show him the bottom half of the letter where the address is clearly written."
            "He squints at the paper."
            fishmonger "What did ya say ya name was again?"
            y neutral "It's [y] Finch."
            fishmonger "Finch, ya say..."
            "He scratches his chin and sighs."
            fishmonger "The code for that's five, three, four. An' remember to pause in between!"
            fishmonger "That's all I know, and all I'll say."
            "He stares at me with a glimmer of greed in his eyes."
            fishmonger "Payment?"
            "Clearly, the only language merchants speak is money..."
            y "Oh, yes. Thank you so much for the help."
            "That was far from helpful!"
            "But I leave him a fair amount of coin for his trouble anyway."
            #"Perhaps I will have better luck with someone else."

            jump talktownsfolk

    #SCENE CHANGE - Brick Wall
    "It seems I have spoken to everyone I can in the area."

    "According to what I've been told, I need to go to the west alley and knock on the wall."

    "The code was... five, three, four?"

    scene bg brickwall with dissolve
    $ config.side_image_tag = "june"
    ny neutral "I make my way past the market area to a narrow alley."
    "Upon reaching the end of the alley, I turn and come across a strange brick wall. The bricks are discolored and eroded compared to the rest."
    "Well."
    "I stare at the wall for a few moments."
    "This is certainly not something I had planned for this trip, but if it's the only way to get to Grandfather..."
    "I suppose I'll just have to give it a go."

label knocking:
    if knocking >= 3:
        jump knockwhatever
    else:
        jump knockknock

    menu knockknock:
        "What was the code..?"
        "3":
            ny huffed "No, that doesn't seem right..."
            ny neutral "Let me try again."
            $ knocking += 1
            jump knocking
        "4":
            ny huffed "No, that doesn't seem right..."
            ny neutral "Let me try again."
            $ knocking += 1
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
                            $ knocking += 1
                            jump knocking
                        "4":
                            jump afterknocking
                        "5":
                            ny huffed "Was that it? Nothing is happening."
                            ny neutral "Let me try again."
                            $ knocking += 1
                            jump knocking
                "4":
                    ny huffed "No, that doesn't seem right..."
                    ny neutral "Let me try again."
                    $ knocking += 1
                    jump knocking
                "5":
                    ny huffed "No, that doesn't seem right..."
                    ny neutral "Let me try again."
                    $ knocking += 1
                    jump knocking

label knockwhatever:
    "After a few attempts, I'm fairly certain I've forgotten the code."
    y "..."
    "Whatever!"
    "I knock on the wall repeatedly in frustration, with no rhyme or reason!"
    "..."

label afterknocking:
    "There is no response at first, but..."
    stop music fadeout 5.0

    play sound "audio/sfx_brickWallMoving.mp3" volume 0.44
    #SCENE CHANGE - Black Screen
    scene bg black with slideawayright
    ny shocked "The brick wall suddenly pulls back."
    "With cautionary steps, I move inside."
    $ config.side_image_tag = "None"
    #note: this could be somehting like....better
    "A rattling door slides closed the moment I enter."
    "It must be an ancient elevator, rusted and old."
    #SFX -  Elevator
    play sound "audio/sfx_elevator.wav" volume 0.1
    #sounds off
    "The rickety elevator descends down for a while. I start to regret stepping inside - who knows what I will find so far down?"
    "..."
    "..."
    "..."
    #SFX -  Elevator
    play sound "audio/sfx_elevator2.wav" volume 0.1
    "The elevator finally comes to a stop, and the door opens."

    #SCENE CHANGE -  Underground Black Market Faire
    play music bgm_blackMarket volume 0.4
    play sound "audio/sfx_crowd.wav" volume 0.009 loop
    #play sound "audio/sfx_runningSewer.mp3" volume 0.026 loop
    #scene bg underground market with slideawayleft
    #ZOOM IN ON SPECIFIC PARTS WITH FADES TO BLACK
    window auto hide
    show bg underground market:
        subpixel True pos (0.73, 3.89) zoom 2.0
    with dissolve
    with Pause(1.05)
    show bg underground market:
        subpixel True pos (2.11, 2.16) zoom 1.50
    with fade
    with Pause(1.05)
    show bg underground market:
        subpixel True pos (-0.28, 3.43) zoom 2.0
    with fade
    with Pause(1.05)
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
    $ config.side_image_tag = "june"
    "It takes a few seconds for my eyes to adjust to the dim lighting as I step out of the elevator."
    "A strange new world greets me.  Creatures I've never seen before are lined up in tanks or hung out on display."
    "Even the people here are mysterious, their features obscured by masks or dark clothing. No one seems keen on being recognized."
    ny shocked "What is this place?"
    "Why did Grandfather's address lead me here? Was I given the wrong directions?"
    "Not to mention the smell of the sewer is rather unpleasant. It's no wonder everyone has their faces covered."
    ny neutral "Feeling uneasy, I turn to see if I can take the elevator back up, but the door refuses to open."
    "It seems I have no choice but to keep moving. There must be another way out somewhere."
    "As I push through the crowd, I can't help but notice what's on display in the stands."
    "Some of the sea creatures are quite beautiful. These are worth remembering."
    "Surely a picture wouldn't hurt?"
    "I reach for my camera."
    show hunter neutral mask with dissolve
    window auto hide
    show hunter neutral:
        subpixel True
        ypos 1.17 zoom 1.0
        linear 0.80 ypos 1.75 zoom 1.5
    with Pause(0.80)
    with dissolve
    show hunter neutral:
        ypos 1.75 zoom 1.5
    window auto show

    uhunter "Careful where you point that thing. I wouldn't take your camera out here ‘less you want to leave in a barrel."
    "I freeze as a stranger's hand reaches over to cover my own ."
    uhunter "Thought I saw a familiar face in the crowd. Didn't know it was you, [y] Finch."
    show hunter neutral:
        xalign 0.5
        ease 0.2 ypos 1.17 zoom 1
    with vpunch
    ny shocked "I turn to see who the man is behind me. How does he know my name?"
    "I quickly yank my hand away."
    y "Who are you, exactly?"
    show hunter happy with dissolve
    uhunter "Bit rude to greet a friend like that, isn't it?"
    y "A friend?"
    y neutral "I'm sorry sir, you've got the wrong person. I haven't been in this part of Aquantis before."
    show hunter raisedeyebrow with dissolve
    uhunter "Ha- this isn't your first time here. Don't appreciate being treated like a stranger either, though I s'pose it's been awhile."
    "He pulls down his mask to reveal a handsome face."
    #TAKE OFF MASK
    show hunter neutral -mask:
        xalign 0.5
        ease 0.7 ypos 1.75 zoom 1.5
    pause 0.2
    show hunter neutral with dissolve
    uhunter "Hunter. Hunter {w=0.1}Morrowe."
    if newspaper:
        ny shocked "Morrowe? I saw that name in the newspaper earlier, but the man himself looks unfamiliar."
    menu:
        "That doesn't mean anything to me.":
            $ hunter_points -= 1
            y neutral "Is that name supposed to mean anything?"
            y "I told you I don't know who you are."
        "I'm sorry?":
            y neutral "I'm not sure what you mean, sorry."
            y "I don't think I know anyone by that name."

    show hunter flustered with dissolve
    h "Ha... you're really going to make me say it then?"
    h "..."
    h "It's Hammy."
    h "We used to play together as kids."
    "An old memory comes back to me. I used to play with a kid down at the beach."
    "I remember his smile when he was showing me the shells or bugs he found."
    "If there was anyone I'd recall from my time here, it'd be him."
    #show june smile
    y "That's right! Hammy!"
    "His shoulders deflate."
    h "Of all the things you could remember me by, it just had to be that nickname…"

    menu:
        "Tease him.":
            $ hunter_points += 1
            y "Well, Hammy, it's hard to forget a nickname like that!"
            h "Please, really, just Hunter is fine."
            y "But your face is so funny when I say it!"
            h "You..."
            show hunter flustered with dissolve
            "He looks away from me. I believe he is thoroughly embarrassed now."
            y "Of course, I'll call you Hunter. I'm just having my fun."

        "Let it be.":
            y "Of course, I'll just call you Hunter now."
            y "We're not children anymore."

    show hunter happy with dissolve
    h "...Didn't think I'd ever hear you say my name again."
    y "You look so different now!"
    show hunter neutral:
        xalign 0.5
        ease 0.2 ypos 1.17 zoom 1
    h "Well, it's been about, what... ten years or so since we've last seen each other? Would hope I look different."
    h "I'll be honest, never expected you to come back."
    y "I came to see my grandfather, if you still remember him."
    show hunter raisedeyebrow with dissolve
    h "{i}Remember him?{/i} 'Course I remember him. Always grateful for the old man taking care of me all these years."
    h "Figured you'd rather rush off to see him first thing. Didn't think you'd be sneaking ‘round here instead."
    show hunter happy with dissolve
    h "Feeling nostalgic?"

    y "Well... I was following the address on this letter he sent me. The townspeople pointed me here."
    show hunter neutral with dissolve
    "I show him Grandfather's letter."
    h "Looks like it was sent from his old shop down here, but that's been closed since he retired."
    y shocked "Pardon?"
    show hunter happy with dissolve
    h "Heh, lost your way again, [y]? Some things never change."
    y huffed "I'm not that bad with directions! I was misled..."
    show hunter neutral with dissolve
    h "Yeah, yeah. Follow me. I'll take you to the old man's place."
    y shocked "Really? You would do that?"
    h "I got business with him anyways."
    h "Just keep your camera out of view. People might think you're a reporter or something."
    "He throws me his coat."

    #SCENE CHANGE - Black Screen
    play sound "audio/sfx_cloakdrop.mp3"
    scene bg black with screenShake
    "My nose is filled with the salty smell of the sea."
    h "Keep it for now."
    menu:
        "\"Thank you.\"":
            $ hunter_points += 1
            h "Sure."
            h "Should keep you from standing out too much."
            "His coat is heavy, but it's not a bad weight."

        "\"What are you doing?\"":
            $ hunter_points -= 1
            y "Don't just throw this thing on me."
            h "It'll help you blend in, yeah? You don't want people getting the wrong idea."
            y "I suppose..."

    #SCENE CHANGE - Black Market
    scene bg underground market:
        fit "contain"
    $ config.side_image_tag = "june"
    show hunter neutral mask
    with dissolve

    "I slide the coat over my shoulders and Hunter pulls his mask back up."
    "He takes my hand, leading me through the crowd. I try my best to keep in step with his long strides."

    #SFX - CROWD
    play sound "audio/sfx_crowd.wav" volume 0.05 loop fadein 2.5

    "As we're walking, I see something moving out of the corner of my eye."
    "Without thinking, I glance up. "

    #SCENE = CG (Mermaid in Tank [Zoomed])
    scene bg black with dissolve
    show cg sushi:
        subpixel True pos (0,0) zoom 1.0
    with fade
    "There is a pale face behind the glass."
    "The top half of her body looks human, but her lower half ends in a tail."
    "A woman... {w}no - a creature - that is equal parts human and fish."

    $ config.side_image_tag = "june"

    y neutral "Beautiful..."

    $ config.side_image_tag = "None"

    "She is mouthing something and banging urgently on the glass."
    "Her eyes seem to lock onto mine for a moment."
    "Is she asking for my help?"
    "The crowd parts, and I'm able to see the rest of the stand."

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
    $ config.side_image_tag = "None"
    "Another mermaid, similar to the one banging on the glass, is on display in front of the tank."
    "Her tail is ripe for the taking."

    menu:

        "How awful.":
            $ promermaid += 1
            "Though I know they're sea creatures, they still look so human."
            "Did she have any family? Children?"
            "I try to shake off the nausea and squeeze Hunter's hand."
            "He seems to pick up on my uneasiness and walks faster through the crowd."

        "How curious.":
            $ antimermaid += 1
            "A large chunk has been taken from her tail."
            "What are mermaids even used for? Bait? Food?"
            "Hunter must have noticed I was staring for too long. He pulls on my hand and walks faster through the crowd."

    scene bg black with dissolve:
        zoom 2.0
    camera:
        zoom 1.0
    scene bg underground market:
        fit "contain"
    with fade
    show hunter neutral mask with dissolve
    h "Try to keep your eyes down, or people might see your face."
    $ config.side_image_tag = "june"
    y neutral "Sorry. It's just... I haven't seen a mermaid before. It's all a bit surprising."
    h "...Huh. {w}Right."
    h "You get used to seeing them after a while."
    play sound "audio/sfx_crowd.wav" volume 0.009 loop fadein 2.5

    menu:
        "\"Do you hunt them too?\"":
            $ hunter_points += 1
            h "Yeah, I do. Family business, remember?"
            if newspaper:
                y "I thought it was a fishing company?"
                h "On the surface, sure."
                h "We do a lot of fishing. Some of that is mermaids... if you look under the table."
            else:
                y "I don't quite remember much, to be honest."
                h "We do a lot of fishing. Some of that is mermaids... if you look under the table."
        "\"You don't {i}kill{/i} them too... do you?\"":
            $ hunter_points -= 1
            h "I do."
            h "My family does a lot of fishing. Some of that is mermaids... if you look under the table."
            h "Either they die or our sailors do."
            y "..."
            h "Don't be fooled, [y]. They're more dangerous than they look."

    "A lot has changed since I last saw him."
    h "Y'know, the old man used to hunt mermaids, too."
    y shocked "Really? {i}Grandfather{/i} did?"
    h "Yep- the best of us. Then he retired and sold most of his ships to my mother."
    y "I know Grandfather owned a ship, but I don't remember him mentioning anything about mermaids."
    h "You should ask him. He'd tell you all 'bout his time at sea."

    if promermaid >= 1:
        ny flustered "I can't believe Grandfather did something like that."
        "If I were a mermaid, I'd rather meet my end at sea. {w}Not here. {w}Not like this."
        y  "Can we keep moving?"
        y "I don't think I can stand being here any longer."
        "He gives my hand a reassuring squeeze."

    if antimermaid >= 1:
        ny neutral "Grandfather and Hunter make their living in a world like this."
        "That's the way it is. I'd rather the people be safe."
        y "How much further do we have to go?"

    h "Exit's right this way. C'mon, [y]."
    "True to Hunter's word, we soon find our way out."

#need transition here
    stop sound fadeout 2.0

    #SCENE CHANGE - Port w/ Boats
    play music music_town fadein 2.0 volume 0.4
    #SUBTLE ZOOM IN FROM CENTRE
    window auto hide
    scene bg port:
        fit "contain"
        xalign 0.5
        subpixel True
        zoom 1.05
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    show bg port

    play sound "audio/sfx_wavesCalm.ogg" loop volume 0.1 fadein 1.0
    play sound "audio/sfx_seagulls.ogg" loop volume 1 fadein 1.0
    "We make it outside and I can finally see the sky again."

    $ config.side_image_tag = "june"
    y neutral "It's afternoon already?"
    show hunter neutral with dissolve
    h "Wandering does that to you."
    "He pulls the mask off his face and I hand him back his coat."
    h "When did your train get here?"
    y "Early morning. My legs are aching to sit."
    show hunter happy with dissolve
    h  "Don't keel over just yet."
    y "I wouldn't dream of it."
    "We're at the portside now; the edge of the country. The ocean looks so vast and endless."
    "Sailors are carrying supplies to and from the ships at the dock."
    y "Does Grandfather live on one of these?"
    show hunter neutral at farright with move
    h "The ole girl over there, can't miss her."
    "Out on the furthest side of the docks is a large wooden ship. It sticks out compared to the rest, towering proudly over the harbor."
    y "So that's his home..."

    #show hunter neutral at centre with move
    #june sad
    "All these years apart are finally coming to an end."
    "Perhaps my parents estranged us over a misunderstanding, and it will be a simple, happy reunion with no trouble at all."
    "I want to hear his side of it, regardless."
    "We cross the ramp onto Grandfather's ship and approach the closed doors of the Captain's Quarters."
    "Hunter gives a few strong knocks with the back of his hand."
    "..."
    g "Aye, I hear ye-"
    show grandpa neutral at Position(xpos=0.32) with dissolve
    "The door opens and an old man steps out."
    y shocked "Grandfather?"
    show grandpa surprised with vpunch
    stop music fadeout 1.0
    "He staggers back as though he's seen a ghost."
    g "Could it really be...? Little birdie?"
    show grandpa happy at jumpin
    g "Oh, bless the stars... Yer really here! My dear, sweet [y]!"
    #$ config.side_image_tag = "none"
    show grandpa happy:
        subpixel True
        zoom 1.0
        linear 0.60 ypos 1.27 zoom 1.5
    with Pause(0.70)
    show grandpa happy:
        ypos 1.27 zoom 1.5
    "Suddenly, I'm caught in his embrace. He may be older, but his strength certainly has not faded." with vpunch
    "I hug him tightly in return. The anxious anticipation I had moments before seems to vanish entirely."
    play music music_town fadein 2.0 volume 0.4
    y neutral "It's been too long, Grandfather!"
    show grandpa happy:
        subpixel True
        ypos 1.27 zoom 1.5
        linear 0.20 ypos 1.0 zoom 1.0
    with Pause(0.20)
    show grandpa happy:
        ypos 1.0 zoom 1.0
    g "An' I see the lad brought ye here. Thank ye, my boy."
    h "‘Course."
    $ speaking_char = "all"
    show grandpa happy at Position(xpos=0.64) with move
    "Hunter is barely able to respond before Grandfather traps him in his arms too. Hunter groans in response and I can't help but laugh." with vpunch
    "Once Grandfather has squeezed the daylights out of us, he lets go."
    show grandpa happy at left2 with move:
        ease2 0.3
    g "Oh, just how many years has it been since I've seen ye, [y]?"
    show grandpa neutral with dissolve
    g "And yer mother? Is she with ye?"
    y "I'm sorry, Grandfather. It's just me."
    g "Oh, Marie..."
    "He lets out a wistful sigh."
    g "Can't be helped, I s'pose."
    g "Come on in, then. Ye had a long journey, I'm sure."
    h "I'll let you two catch up."
    y "But didn't you say you had business with Grandfather?"
    show hunter happy with dissolve
    h "Heh, I did. Had to deliver a lost package safely to his door."
    #Blushing June Emote here
    y flustered "Oh!"
    y neutral "Thank you, Hunter."

    menu:
        "\"Will I see you again?\"":
            $ hunter_points += 1
            show hunter warmsmile with dissolve
            h "Yeah."
            h "I won't be far."
        "\"Goodbye.\"":
            h "Goodbye, [y]. Don't be a stranger, yeah?"

    show hunter neutral with dissolve
    "He turns to leave, nodding respectfully to Grandfather."
    h "See you 'round, old man."
    g "Thank ye for guidin' her here."
    hide hunter with dissolve
    "Hunter heads out, and Grandfather beckons me inside."
    stop music fadeout 1.0
    jump grandpatalk

label timeskip1:
    #SCENE CHANGE - Black Screen
    scene bg black with dissolve
    stop sound fadeout 2.0
    "Time goes by quickly, and a few days pass just like that."
    "Despite my best attempts, Grandfather has not been able to answer my questions."

    #SCENE CHANGE - Shabby Market
    scene bg shabby market with dissolve
    play music "audio/music_town.mp3" fadein 1.0
    show grandpa neutral at left2 with dissolve
    $ speaking_char = "all"
    "Today, Grandfather and I are going out shopping."

    show hunter neutral at right2 with dissolve
    "Along with Hunter, who just happened to be free."

    y neutral "Thanks for joining us, Hunter."

    show hunter happy with dissolve
    h "Sure. Had some time today."

    y "It's been awhile since I last went shopping for fish."

    show grandpa happy with dissolve
    g "Don't ye worry, little birdie. I know my way around the markets."

    show hunter neutral with dissolve
    h "There any fish you got in mind?"

    y "I have no idea. Whatever tastes good, I suppose."

    g "Ye ain't really tasted fish till yer out at sea. There's all kinds."

    g "O'course some fish bite back. Ye got to watch out for the mermaids out there."

    show grandpa neutral with dissolve
    g "Worst is the sirens."
    y shocked "Sirens?"
    g "Blasted horrible creatures. I only ever saw one in my career, and it damn near got my whole crew!"
    show hunter happy with dissolve
    h "Yeah, right, old man. They've been dead longer than you've been alive."
    h "All you got was a squealing manatee, not a siren."
    show grandpa happy at jumpin
    g "Har har har!"
    show grandpa neutral with dissolve
    g "If only ye'd visited sooner, [y]. Ye could'a seen me in action."
    #june sad instead of flustered
    y flustered "It's unfortunate. I wish I could've spent more time with you."
    "I've learned some things from Grandfather in my time here."
    "He's quite proud of his history at sea."
    g "Ain't got any reason to regret all that. Yer here now, and that's what matters."
    y neutral "Have we ever been out to sea together? I don't recall if we have."
    show grandpa neutral with dissolve
    g "Aye, but never out too deep. The sea's a dangerous place for a wee lass."
    show grandpa happy with dissolve
    g "Shame ye don't remember. I caught ye all kinds of colorful fish."
    "I shouldn't press too hard, but..."
    y "Mother was okay with that?"
    show grandpa surprised with dissolve
    g "[y]...right now? I thought ye were done with that business."
    y "But you still haven't-"
    show grandpa neutral with dissolve
    g "Ah, I've been standin' too long. My back's goin' again."
    g "Go and finish shoppin' without me."
    ny huffed "Oh, not this again!"
    y "Grandfather, {i}please{/i}."
    g "Ye ain't gonna want this old man with his bad back slowin' ye down."
    g "I'll see ye later tonight, aye!"
    hide grandpa with dissolve
    $ speaking_char = "Hunter"
    show hunter at centre with move
    "My questions are once again left unanswered as Grandfather hurries away."
    #show hunter at center with move
    show hunter raisedeyebrow with dissolve
    h "Sure moves fast when he wants to."
    y flustered "Grandfather..."
    "What will it take for him to feel comfortable enough to talk about what happened?"
    "Out of habit, I reach for the camera inside my purse."
    ny neutral "Perhaps there's a way I can prove to him that I'm ready to hear his story."
    show hunter nervous with dissolve
    h "Don't know if I like that look in your eyes. What are you plotting, [y]?"
    y "You have a boat, don't you, Hunter?"
    show hunter neutral with dissolve
    h "Yeah, I got one."
    y "What if you took me out to sea? Further than Grandfather ever took me?"
    y "If I head out far enough, he'll understand that I'm not a child anymore."
    h "Nope."
    y shocked "No? How come?"
    h "If something happens to you, he'll have my hide."
    show hunter happy with dissolve
    h "‘Sides, you don't have the sea legs for it."
    y neutral "We don't have to go out that deep. Just enough to bring him back a photo."

    show hunter raisedeyebrow
    h "..."

    menu:
        "\"Please, Hammy!\"":
            show hunter flustered with dissolve
            h "Ugh."
            #june smile
            y "Come on, you can do a favor for an old friend, right?"
            show hunter happy with dissolve
            h "Stubborn as ever, [y]."

        "\"I would appreciate it.\"":
            #june smile
            y "Old friends help each other out, yes?"
            show hunter raisedeyebrow
            h "Pulling that card, huh?"

    show hunter neutral with dissolve
    h "Fine. Though I'm only taking you through the safest waters."
    #june big happy
    y "Thank you! You won't regret it, Hunter."
    #june happy
    y "It'll be fun. We can pretend to be pirates, just like when we were kids!"
    show hunter happy with dissolve
    h "Sure. But I get to be Captain this time."

    #SCENE CHANGE - Sea
    scene bg calmwave with dissolve
    stop music fadeout 1.0
    #SFX - waves (calm)
    play sound "audio/sfx_wavesCalm.ogg" loop volume 0.3

    "We embark on Hunter's boat."
    "The sea is calm, and the sun is shining down on us."

    #show hunter smile instead
    $ config.side_image_tag = "june"
    show hunter happy with dissolve
    h "Might be able to spot a 'maid going onto the rocks for a sunbathe."
    y shocked "Mermaids sunbathe? Really?"
    show hunter neutral with dissolve
    h "Yep. But if they spot my little skiff, the show's over."
    "I take my camera out of my purse."
    ny neutral "I wonder if I'll be able to catch a picture of a mermaid?"
    "That should be more than enough to impress Grandfather."
    show hunter happy with dissolve
    h "So, you're into photography now?"
    #june big happy
    y "Aye, Captain!"
    h "Heh. Didn't think you'd have the patience for it."
    #june happy
    y "Perhaps not when I was younger, but I really enjoy it now."
    y "It's like making physical copies of memories. Even if you forget something, the photo lasts forever."
    y neutral "Do you keep any records as a mermaid hunter? Photos?"
    show hunter neutral with dissolve
    h "Records, yes. Photos, no."
    h "Don't like being near them any more than we have to."
    y shocked "Oh. They're really that dangerous?"
    h "Yeah. It's the pretty ones you gotta watch out for."
    h "Nothing for you to worry about though. You'll be-"
    h "..."

    show hunter nervous with dissolve
    h "Hang on. Something's not right."
    "I'm about to respond to him, but the ship catches on the waves, and I stumble."

    #SCENE CHANGE - view of the sea (stormy)
    play sound "audio/sfx_thunder.ogg" volume 0.9
    scene bg choppywave
    play music "audio/music_storm.mp3" fadein 2.0 volume 0.4
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.4 loop
    show hunter nervous with vpunch

    "I can't see a hint of blue in the sky."
    y shocked "It was sunny only moments ago! What is this?"
    h "Hold onto something, [y]! This storm's not natural. I'll steer us out of it."

    if seastorm:
        "I remember reading something about storms that appear without warning like this."
        "I should be safe since Hunter is with me, right?"

    hide hunter neutral with vpunch
    "The boat creaks as he tries to turn it back towards the port."
    "The lurching nearly throws me to the floorboards and I have to grab the side of the boat to stay upright."
    $ config.side_image_tag = "june"
    y shocked "Ah...!" with screenShake
    "Something stirs in the back of my memory as I stare into the waves."
    "Is the water... glowing?"

    #TODO FLASHBACK CG for a second of baby prince and june
    #SFX - loud crash, screen shake
    play sound "audio/sfx_waveCrash.wav" fadeout 1.0
    show bg choppywave with screenShake
    #SFX - choppy waves
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.6 loop

    #show hunter neutral with vpunch
    h "Stay away from the edge!"
    y shocked "I'll try! I can hardly stand straight!"
    #hide hunter neutral with dissolve
    ny flustered "I want to listen to him, but in that moment, I recall Grandfather's face from earlier today."
    "I didn't get to take a photo yet to bring back to him."
    menu:
        "..."
        "Listen to Hunter.":
            # +Hunter points
            "I shouldn't take unnecessary risks."
            "My life isn't worth a photo."
            ny neutral "I tuck my camera back into my purse and move away from the edge."

        "I can't give up on a picture.":
            "This should be proof that I can handle whatever Grandfather has to say."
            ny neutral "I hold my camera up, adjusting the shutter speed and exposure to the perfect amount..."


    $ config.side_image_tag = "june"
    #SPRITE?
    play sound "audio/sfx_waveCrash.wav" volume 0.06 fadein 1.0
    $ renpy.music.set_volume(0.3, 2, 'music')
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.06 loop
    play sound "audio/sfx_hum.mp3" volume 1.5 fadein 1.0

    u "Come...come with me..."
    y "What...?"
    u "O' ye of land to the queen of sea..."
    "A haze clouds my thoughts and my legs start to move on their own."
    "I lean over the side of the boat, searching for the source of the singing, but all I can see are the churning waves below."
    h "[y], what are you doing?!"
    u "Come with me..."
    u "...to the depths below..."
    "The alluring voice seems like it's singing for my ears alone."
    show hunter nervous with vpunch
    h "Shit, it's a siren! Cover your ears, [y]!"
    "Hunter abandons his position at the helm and races towards me, but I can't imagine why."
    "My hands tightly grip the slippery rail that's keeping me from falling in, and yet the rest of my body is going against my will to stay put."
    "For a split second, I think I can hear Hunter calling my name before I take the plunge."

    stop music fadeout 1.0
    #SFX - SPLASH
    scene bg drowning:
        fit "contain"
    with hpunch
    play sound "audio/sfx_splash.flac" volume 0.6

    "The light of the surface drifts further and further away as my body sinks deeper into the emptiness."
    "The singing stops, but my body remains numb."
    "I can feel myself fading..."

    stop sound fadeout 2.0

    #SCENE CHANGE - Black Screen
    scene bg black with dissolve
    "..."
    siren "After all these long years... you've finally returned home to me..."
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
        scene cg_skyllahands with dissolve:
            zoom 0.343
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        scene cg_skyllahands with dissolve:
            zoom 0.343


    #SCENE CHANGE - underwater cave (skylla's)
    play music bgm_skyllaCave volume 0.8
    $ config.side_image_tag = "june"
    "All at once I recognize her, or her voice at least. She's the one that caused me to go overboard."
    y fish neutral "BLUB BLUB BLUB!!!"
    siren "Ahaha! Oh, you cute thing. That's no way to speak to a lady!"
    $ config.side_image_tag = "None"
    "Try as I might, none of my words come out right."
    "I've... been turned into a fish by this siren?"
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
            "I try to swim at her, but an invisible wall stops me before I can get close enough." with vpunch
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
    "No matter how hard I press my hands - well, fins - against the bubble, I can't push through."
    "I'm trapped. There's no doubt about it."
    "Am I cursed to stay like this... forever?"
    #stop music fadeout 2.0
    "At the thought, horror rolls through me like a wave. My body is all wrong, somehow warped beyond recognition."
    "I have no hands to take pictures with.{w} No legs to run back home with.{w} No words to cry out with."
    "Forever? Like this?"
    "Or perhaps...{w}am I going to die after being eaten as a special dinner course?"
    "Suddenly the memories of the mermaid market come to mind. Their bodies had been taken apart, all for a cheap meal."
    "I am no different from them now.{w} Just as helpless."
    "From the distance I can hear the siren humming to herself as she swims to and fro around the cave."
    s "One piece at a time..."
    "No.{w} No, no, no."
    "Think, [y], think! There has to be a way out of here!"
    "If there's a way to turn a human into a fish, surely there's a way to turn a fish back into a human, right?"
    "I glance around the cave."

    window auto hide
    camera:
        subpixel True
        parallel:
            ease 0.52 pos (0, 0)
            ease 0.88 pos (-864, -7)
            ease 0.80 pos (-12, -475)
            ease 0.78 pos (-858, -480)
        parallel:
            zoom 1.0
            ease 0.52 zoom 1.61
    with Pause(2.98)
    camera:
        pos (-858, -480) zoom 1.61
    window auto show

    "It's dark, and difficult to see. My new tiny eyes struggle to take in everything all at once."

    window auto hide
    camera:
        subpixel True
        pos (-858, -480)
        linear 0.83 pos (-804, -318)
    with Pause(0.93)
    camera:
        pos (-804, -318)
    window auto show

    "From what I can see, there's only one path forward: deeper into the siren's lair."

    window auto hide
    camera:
        subpixel True
        pos (-804, -318) zoom 1.61
        linear 1.32 pos (-108, -102) zoom 2.04
    with Pause(1.42)
    camera:
        pos (-108, -102) zoom 2.04
    window auto show

    "Glowing stones line the cave walls, but that's not very helpful."

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
    "Her clawed fingers gracefully pop the bubble, and then just as swiftly close around my body."
    "My tiny heart thuds rapidly. She could pop me in an instant as well."
    show skylla:
        yalign 0.1
        ease 0.5 zoom 1.5
    s "Hold still now, cute thing. This won't hurt."
    play sound "audio/sfx_hum.mp3" volume 1.5 fadein 1.0
    "It's a lie. A burning pain spreads across my body as she sings."
    "I can't even scream as I feel something tugging inside me, as if the siren is trying to pull me apart from within."
    s "It's okay! Don't be stubborn now. Come on, it's {i}me!{/i}"
    show skylla angry with dissolve
    "The moment I feel like I'm about to snap in two, a sudden blinding light flashes throughout the cave." with flash

    #FLASH EFFECT
    stop sound
    show skylla angry:
        yalign 0.1
        ease 0.02 zoom 1
    "The siren screams as she drops me and flails backward."
    show skylla surprised with dissolve
    s "No. No! This- this isn't right."
    "Once I blink the white spots out my vision, I look up and find the siren staring at me with a shocked expression on her beautiful face."
    "Her hands are bleeding."
    "We stare at each other, frozen in place."
    "..."
    "But then, I remember myself and swim away from her, pushing my tiny fins as hard as they can go."
    show skylla angry with vpunch
    s "You little {i}eel!{/i} Get back here!"

    y "Blub blub!!"

    "As if! Who in their right mind would do that!?"
    "Her tentacles try to grasp me, but I'm too small for them to catch."
    s "Fine! Be like that!"
    show skylla angryteeth with dissolve
    play sound "audio/sfx_hum.mp3" volume 1.5 fadein 1.0
    "She begins humming to herself again, and a bolt of magic shoots out of her hands."
    "I twist away just in time, and the magic collides with one of the glowing stones on the wall." with vpunch
    hide skylla with dissolve
    stop sound
    "Time seems to slow down."
    "I hear a whirring coming from the stones like the sound of a shrill kettle, and in the next second the stones explode." with flash
    play sound "audio/sfx_glowStoneExplosion.mp3" volume 0.2
    "The force sends me sprawling backwards in pain, but I don't have time to linger on it because the explosion has created a hole just big enough to squeeze through."
    stop music
    scene bg black

    "I swim as fast as I can. Faster than I've ever ran when I had legs."
    "My heart is thumping madly in my chest as I force my way through the debris. "
    "The sharper pieces scrape and cut through my fins, but I barely pay them any mind as I keep charging forward with all I have."
    "I can hear the siren cursing as I swim away."
    "It doesn't matter where I go, just as long as it's far away from that awful witch!"

    scene bg sea with vpunch
    play music "audio/music_underwater.mp3" volume 0.7 fadeout 1.0
    "I stop to catch my breath after what feels like a lifetime."
    $ config.side_image_tag = "june"
    y fish neutral "Blub...{w}blub..."
    "Now that the adrenaline has faded, I feel exhausted. My body feels like it's been run over."
    "Grandfather...{w} Hunter...{w} they must think that I'm dead by now."
    "At the thought of them, I suddenly feel overwhelmingly homesick. I need to tell them I'm alive!"
    "But...{w}how am I supposed to make it back to land?"
    "The only one that might be able to change me back is that siren, but there's no way I can go back there."
    "Before I can dive any further into those thoughts, I hear voices approaching from a distance."
    "I quickly dart into some foliage to hide."

    #THIO AND JOR ENTER THE STAGE
    #Voice Lines Start (old, deleted the comments where they were due to script changes)
    show prince angry at farleft
    show jorunn sweat at right2
    show kelp with vpunch
    novisualthio "The further out you swim, the more guilty you are! Those fish belong to the Capital."
    novisualthio "Return them now, and your judgment will be fair."
    novisualjor "I'm very sorry, {i}my prince{/i}, but I was hoping I could skip the judgment part entirely!"
    novisualjor "Can’t you just ask your servants to find you something else for dinner? I’m sure they have plenty of food to spare."

    "Oh? A 'prince'?"
    "Curiosity piqued, I push a bit further through the foliage to get a better look."

    hide kelp with dissolve

    show prince angry at farleft
    show jorunn sweat at right2
    with dissolve

    $ speaking_char = "all"
    "A pair of merfolk are staring each other down."
    $ speaking_char = "Jorunn"
    "One of them is carrying a large net stuffed full of fish."
    $ speaking_char = "Prince Thioran"
    "The other has fins in a striking shade of blue, unlike anything I've seen.{w} He has what appears to be a guard hovering close to his side."

    $ speaking_char = "all"
    "Prince? Guard? Do mermaids really have those kinds of things?"
    up "Are you suggesting that {i}we{/i} sink to {i}your{/i} level?"
    uj "Oh, no. Of course not!"
    show jorunn glee
    uj "...But if the shell fits!"
    up "You thieving little-"

    show prince sweat at jumpin2
    show jorunn sweat at jumpin
    with vpunch

    "Just then, a loud rumble echoes throughout the area. The waters feel like they're slowly beginning to churn."
    guard "It's another sea storm, Your Highness! We must head back now before it picks up any further."
    show prince angry
    up "Damn it. Why now, of all times..!"
    show jorunn glee
    uj "Well, I guess that's my cue! I'll be taking these home then. Goodbye!"
    "The rumble comes again, a bit louder this time. My heart sinks as I realize I might not survive whatever storm is coming." with vpunch
    "They could be dangerous, like Hunter warned, but they might be my only shot at getting help right now."
    "Do I approach the prince? Or perhaps the other fellow?"

    if promermaid >= 1:
        "Anything would be better than returning to the sea witch."
    if antimermaid >= 1:
        "Should I even be trusting any of them? Chasing mermaids is how I became stuck like this."
    #"Regardless, they're both starting to swim away."

    $ speaking_char = "all"
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
    "I try swimming anyway, moving as fast as I can."
    "The storm roils behind me, and I feel myself being sucked into the whirling water..."
    "It's too late!"
    "The last thing I see before everything goes dark is something large crashing right into me.."
    scene black with vpunch
    "Ravaged by the sea, I die."
    "BAD END 1."

    jump endofdemo

#Change this
label endofdemo:

    "Thank you for playing Heart's Depth! Follow our game page for updates..."

    return
    #past this is unused for now
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

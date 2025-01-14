
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

    show side june neutral at farleft with dissolve:
        yalign 0.1

    #GET PLAYER NAME
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
            jump get_name



#PROLOGUE
label prologue:

    #TODO SCENE ?
    scene bg choppywave with dissolve
    play music "audio/music_storm.mp3" volume 0.4
    play sound "audio/sfx_wavesChoppy.ogg" volume 0.6 loop

    $ config.side_image_tag = "june"
    y shocked "It was sunny only moments ago! What is this?"

    show hunter silhouette with dissolve

    u "Blasted...I've sailed us right into a sea witch's storm! Hold onto something, [y]!"
    "The ship creaks as he tries to turn it back towards the port, but the waves are unrelenting."
    "Something stirs in the back of my memory as I stare down into the waves below."
    "I can see something glowing through the wind and rain."

    #SCREEN SHAKE
    u "[y]!" with screenShake
    $ config.side_image_tag = "june"
    "I try to reach for it, forgetting myself for just a moment."

    #SFX - SPLASH
    scene bg black with vpunch
    play sound "audio/sfx_splash.flac"

    #SCENE CHANGE - (Underwater / Black)
    stop music
    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "The regret floods my mind, but it's too late."
    "I can feel myself fading..."
    jump chapter1

#CHAPTER 1
label chapter1:
    #TODO SCENE = CG (Train)
    scene bg black with dissolve
    play music "audio/music_town.mp3" fadein 1.0

    "Salty air...I remember how I would try to stick out my tongue to taste it."
    scene cg train with dissolve
    "I was a child the last time I did something as silly as that."
    "I can’t wait to see it again, but when I think about the ocean, I can't help but feel like I broke a promise to it."
    "It has been 10 years since I've last seen the ocean. Perhaps it was just because I missed Grandfather after being inland without contact for so long."
    "I only ever got to see him on special holidays in the summer, but now I'm returning to Aquantis again just to see him."
    "I can’t really remember why my mother stopped letting me see Grandfather. She said she had lost trust in him after something that happened to me here when I was a child."
    "Even though I am now grown, she refuses to say what happened."
    conductor "Please gather all personal belongings, we are arriving at Aquantis Station!"

    "The screeching of the brakes signal the train to a stop."
    scene bg shabby town with dissolve

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
            # Camera sfx here
            y "Let's see how it turned out!"
            # Image of picture here
            y "This part of town has a great view of the sea."
            y "It’s hard to believe that the port used to be further down."

    "The letter Grandfather sent me had his address, though it would be helpful to ask for some directions. The harbor city is huge."
    "It's been years since I last set foot here, after all."
    "A quaint assortment of homes and shops descend down the hill that lead to the ports, cramped with new and old parts of the city mixed together."
    y "Excuse me- sir! Hello?"
    "He ignores me, walking quickly away from the station."
    "I try to ask few more people, but not one wants to give me the time of day."
    ny huffed "Trying to grab anyone's attention around here seems impossible! They all just ignore me."
    "Were they so unfriendly to people from outside when I was younger? I can't remember."

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
    "I quietly slip away from the men watching me, heading further down the road."
    "I keep my camera close to my hip, hiding it with my coat to prevent any further unwanted attention."

  #SCENE CHANGE - (Shabby Market [Zoomed In])
    scene bg shabby market with dissolve
    ny neutral "The smell grows worse as I suddenly find myself at a market."
    "There are so many interesting things to see."
    menu:
        "What catches your eye?"
        "The newsboard":
            $ seastorm = True
            "There's a board filled with notices and posters here."
            y "Beware of sea witch storms..."
            # Show propaganda poster here
            "Do your town a favor! Report any mermaid sightings to your local Seahunting Guild."
            "The longer they live, the shorter the land!"
            "A group of people stand just past the newsboard, yelling."
            t "It’s the end of times! Return to fish!"
            "I walk away quickly. Best not to interact with those types."

        "Children playing in the street":
            "The children are playing some kind of game."
            kid "I want to be the mermaid hunter this time!"
            kid "No way, it's my turn!"
            y "How cute."
            kid "I don’t wanna be no stinkin’ fish! I’ma be a hunter!"
            "I wonder if I ever played that kind of game as a kid here."

        "The newspaper":
            $ newspaper = True
            t "Extra, extra! Read all about it!"
            "I purchase a copy of the weekly news,"
            "Several Fishing Companies Absorbed by Morrowe Family: What Will They Do Now?"
            y "Morrowe...that name sounds familiar."
            y "I wonder where I've heard it before?"
            "I tuck the newspaper in my coat for later."

    "The smell of fish, salt, smoke and sewer is strong here. Though despite it, there seemed to be a few friendlier townsfolk around."

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
            y "Oh, I know this one. Who’s there?"
            woman "Knock knock."
            y flustered "Uh...knock knock?"
            "The old woman grins toothily."
            woman "Knock knock."
            y "Have a good day, ma'am."
            "I walk away quickly."
            jump talktownsfolk

        "Child with toy":
            y "Hey, there! Do you know where I could find this area?"
            "The child is holding a plush octopus tightly. It looks well-loved."
            "I show him the address, and he glances at it."
            kid "Oh, I know that place!"
            kid "My mama says I’m not allowed to go to the west alley."
            kid "She says there’s bad people there."
            y shocked "Oh…"
            y neutral "Well, thank you for your help."
            jump talktownsfolk

        "Fishmonger":
            #SPRITE CHANGE (??? Expression)
            ny shocked "I just hope I'm not expected to buy the fish covered in flies."

            #SCENE CHANGE - Shabby Market (fishmonger npc sprite)
            y neutral "Good day to you sir. I'm sorry for disrupting you, but-"
            fishmonger "Bass or Tilapia?"
            y "Oh- er, well...I'm not looking to buy fish right now. Could you please help me with the directions to-"
            fishmonger " Do I look like a map stand? I sell fish. Ye buy fish, then ya leave, ye get it?"
            y "I will pay you for the help! I’m just looking for this address."
            "Before he could deny me once more, I show the bottom half of the letter where the address is clearly written."
            #with suggestions from Tay
            fishmonger "I ain't gonna be telling any airsick in-landler how to get—"
            "He squints at the paper, adjusting his sight to get a better look at it."
            fishmonger "What did you say your name was again?"
            y "It's [player_name] Finch."
            fishmonger "Finch, you say..."
            "He scratches his chin and sighs."
            #moved dialogue around - end of tay suggestions
            fishmonger "....Girlie, do ye know where that is? That's in the Black Market District. Someone like you don't belong there. Hell, even I avoid it."
            "Black Market District..?"
            y "Even so, I have to get there. I’ll pay you if you just point me in the right direction."
            fishmonger "Alrighty, little lady."
            fishmonger "Five hits on the brick. Pause, give three, and pause again to give four."
            fishmonger "That's all I know, and all I’ll say."
            "He looks at me and grins toothily."
            fishmonger "Payment?"
            ny huffed "Clearly, the only language merchants speak is money..."
            y neutral "Oh, yes. Thank you so much for the help."
            "I leave him a fair amount of coin for his trouble."
            jump talktownsfolk

    #SCENE CHANGE - Brick Wall
    scene bg brickwall
    $ config.side_image_tag = "june"
    ny neutral"I arrive at the west alleyway. It's a rather nondescript path."
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
    "..3..4..5…"
    "..1..2..3…"
    "..2..3..4.."
    "There is no response at first, but..."
    ny shocked "Suddenly, the wall is pulled back."
    "With cautionary steps, I push inside, seeing no one is there behind the door."
    stop music fadeout 5.0

    #SCENE CHANGE - Black Screen
    scene bg black with slideawayright
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
    play music "audio/music_blackmarket.mp3"
    play sound "audio/sfx_crowd.wav" volume 0.009 loop
    scene bg underground market with slideawayleft
    "It's almost like a circus, or a fairground. Many merchants' booths have strange knick-knacks begging to be looked at."
    "It's hard to make out any faces. No one here seems keen to be recognized in any fashion; a sea of cloths and rags stare back at me as I exit the elevator."
    "Exotic fruits, animals, books, and so many more things from what must have been lands long gone to the waves are being sold here as rarities."
    "My eyes follow every gleaming thing on display."

    y shocked "This is incredible..."
    "As I walked around in awe, my eyes caught on a stand of tropical flowers arranged in a beautiful pattern."
    y "Mother would love to see this..."
    "My hand reaches for my camera once more."

    show hunter neutral with dissolve

    u "I wouldn't dare to take out that camera here, unless you're planning on joining the fish in the stands."
    "My heart sinks as I stand frozen, feeling a gloved hand on top of my own, stopping me." with vpunch
    u "I thought I saw a familiar face in the crowd. I didn't know it was you, [y] Finch~."
    ny huffed "I turn to see who the hell the man is behind me. How does he know my name?"
    "I slap his hand away from mine and glare at his face." with vpunch
    "I do not recognize him."
    u "It's a bit rude to slap a friend, isn't it?"
    y "Who are you, exactly?"
    "He scoffs and shakes his head." with hpunch

    #TODO SPRITE CHANGE - Hunter Disappointed
    u "You don't remember your old playmate? I'm hurt! After all these years, I didn't once forget about you."
    y neutral "I haven't been in this part of Aquantis before. You must have me mistaken for someone else."
    u "Ha- this isn’t your first time here. Don’t appreciate being treated like a stranger, though I s'pose it's been awhile."
    "Bending down to my level, the stranger looks me right in the eyes."
    u "Jogging anything in that noggin? I’ve grown up a bit since you’ve last seen this mug...how 'bout it?"
    "He stares at me for a moment before the realization hits."
    u "Ah, that's right."
    "He pulls down his mask to reveal a handsome and somewhat-familiar face."
    h "Hunter Aubrey Morrowe."
    if newspaper:
        ny shocked "Oh, Morrowe! That means..."
    y neutral "...Hunter?"
    h "That's my name, yes."
    "He looks positively delighted to hear me say his name."
    y "..."
    y "Oh!"
    y "Right, Hammy! you were so different when we were young!"
    "He deflates as soon as I say it."
    h "Ah, you still remember that nickname. Pity..."

    menu:
        "Tease him.":
            $ hunter_points += 1
            y "Well, Hammy, you don't leave my mind that easily!"
            h "Please, really, just Hunter is fine."
            y "But your face is so cute when I say it!"
            h "You..."
            "He looks away from me. I believe he is thoroughly embarrassed now."
            y "Of course, I'll just call you Hunter. I'm just having my fun."

        "Let it be.":
            y "But of course, I'll just call you Hunter."

    "We used to play near the beach as kids. If there was anyone I'd recall from my time here, it'd be him."
    "We were fast friends, though I can't remember much of what we did together. He was a strange little kid."
    h "At least you remember me! It's been only about, what… ten years since we’ve last seen each other?"
    h "I'll be honest, never expected you to come back."
    "I do remember his smile when he was trying to show me shells or bugs he found on the beach."
    "As I look at him now, it seems like the only thing that remains is that smile."
    y "I came to see my grandfather, if you still remember him."
    h "Ah~ family visit. Of course I still remember the old man. His hunting company practically owned half the market strip."
    h "Though he went into retirement a few years ago."
    "He tilts his head, gazing at me intently."
    h "Need some help finding your way?"
    y "Well, yes, if you wouldn't mind..."
    h "I’ll take you. Just keep your camera out of view."
    h "And stop gawking at things like you’ve never been here before...People might think you’re a spy or somethin'."
    "He unclips his cloak and throws it on top of my head. My nose is assaulted with the salty smell of the sea."

    #SCENE CHANGE - Black Screen
    scene bg black with screenShake

    #SCREEN SHAKE
    y huffed "Hey- don't just throw this dirty thing on me!"
    h "Just keep it for now. Keep your eyes down so people can't clearly see your face...and avoid seeing things you shouldn't be looking at anyways."
    y shocked "Seeing things I shouldn't be..?"
    ny neutral"Things I am forbidden to see...I feel a pressing need to see them - but a far more pressing urge to stay hidden from the rest of the townsfolk here."
    "I do as he asks, even if the cloak starts to chafe on my shoulders and crush my hat."

    #SCENE CHANGE - Black Market
    scene bg underground market

    show hunter neutral with dissolve

    "He takes my hand and gives a low hush, leading me through the crowd. I look down at my feet."

    #SFX - CROWD
    play sound "audio/sfx_crowd.wav" volume 0.04 loop fadein 2.5

    "He walks meticulously, carefully weaving through the crowds of people, and I try my best to keep in step with his strides."
    "But then, I see something tantalizingly curious out of the corner of my eye. Without thinking, I glance up."

    #TODO SCENE = CG (Mermaid in Tank [Zoomed])
    scene bg black with dissolve
    camera:
        zoom 2.1
    show cg sushi with fade
    "There is a pale but beautiful face in the dark, behind glass."
    "The further along we walk, the more of her face is revealed."
    "Her body is so human and serene from the top, but her lower half....scales, a tail that flows in the water and reflects off the dim lights around her."
    "A woman....no, a creature that is equal parts human and fish."

    $ config.side_image_tag = "june"

    y neutral "Beautiful..."

    $ config.side_image_tag = "None"

    "Her long brown hair moves in the water just like her tail. She is mouthing something, banging on the glass, but I can't hear a word."
    "Her eyes seem to lock onto mine for a moment."
    "Is she asking for my help?"
    "Suddenly, my view of the rest of the stand is unblocked, and I am able to peek through the empty spot in the crowd. It is a fish hawker's stand."

    #TODO SCENE = CG (Mermaid cut in half)

    stop sound fadeout 3.5
    window auto hide
    camera:
        subpixel True
        zoom 1.0
        ease2 3.36 zoom 0.5
    show cg sushi:
        subpixel True xzoom 1.0 zoom 2.23
        parallel:
            xpos 1.04
            linear 3.36 xpos 1.1
        parallel:
            ypos 2.02
            linear 3.36 ypos 2.22
    with Pause(3.46)
    camera:
        zoom 0.5
    show cg sushi
    $ config.side_image_tag = "None"
    window auto show

    "Her sign reads 'Catch of the day'. Another mermaid, eerily similar to the face banging on the glass, on a table in front of the tank."
    "Except she is missing her body from the hip below; tail ripe for the taking by rabid customers, piece by piece."
    "As if she was just the catch of the day. Another fish for someone to eat for dinner."
    "I fight down the sudden bile rising up my throat and squeeze Hunter's hand, and he starts to walk faster through the crowd."

    scene bg black with dissolve:
        zoom 2.0
    camera:
        zoom 1.0
    scene bg underground market with fade
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
                "That’s just how it is.":
                    $ antimermaid += 1
                    "Grandpa and Hunter make their living in a world like this."
                    "Either the world floods over completely, or we keep our land safe."
                    "That’s the way it is."

        "Have you actually...killed them before?":
            $ promermaid += 1
            h "Why do you sound so horrified? Don't be fooled by their appearances."
            h "I've seen them kill a man in the blink of an eye."
            h "They're monsters using human faces. They don't deserve your pity."
            h "...But yes, I have."
            y "..."

    stop sound fadeout 2.0

    #SCENE CHANGE - Port w/ Boats
    play music "audio/music_port.mp3" fadein 2.0 volume 0.3
    scene bg port with dissolve
    play sound "audio/sfx_wavesCalm.ogg" loop volume 0.1 fadein 1.0
    play sound "audio/sfx_seagulls.ogg" loop volume 0.8 fadein 1.0
    "Once we make it outside the underground and I can finally see the sky again, the sun is already far along on its journey."
    y neutral "It's afternoon already?"
    show hunter neutral with dissolve
    h "Wandering does that to ya. When did your train get here?"
    y "Early morning. My legs are aching to sit."
    h "We're almost there. Don't keel over on me, would you?"
    y "I wouldn't dream of it."
    "We're actually at the portside now, the edge of the country. Practically the edge of the world."
    "Ships are anchored near the shore. Fishermen and hunters alike line the dock, carrying supplies to and from the ships."
    "They are much different than the ones I remember as a kid. These are large, made of steel, and produce steam."
    y shocked "Does Grandfather live on one of these ships?"
    h "The only one not made of steel, that one over there."
    ny neutral "Out on the furthest side of the docks is a large wooden ship. It sticks out compared to the rest, with its clothed sails, and ornate details."
    "It has clearly been maintained with a lot of pride and dedication."
    "I have a faint recollection of Grandfather owning  a boat, of course, but I thought I would remember more than that upon seeing his home."
    h "Well, keep moving along already. I thought you'd be more excited to see your Grandpa!"
    y "Hey, don’t start shoving me- I appreciate the help, but you really don’t have to follow me the whole way there."
    h "I have business with your old man already, running into you was just a coincidence. Let's go!"
    y "Alright, alright, let's go."

    #TODO SCENE CHANGE - Port w/ Boats (ZOOM)
    scene bg port
    "We board a small rowboat to take us there."
    show hunter neutral with dissolve
    camera:
        ease2 3.36 zoom 1.5
    "Before I know it, we arrive on deck, and Hunter walks towards the entrance of the ship's interior."
    "Ten years apart finally coming to an end. Perhaps my parents estranged us over a misunderstanding, and it will be a simple, happy reunion with no trouble at all."
    "I want to hear his side of it, regardless."
    "I want answers."
    camera:
        ease2 1.0 zoom 1.0
    show hunter neutral at right with move
    "Hunter knocks at the entrance of the ship."
    "There's some loud grunting and muffled swearing as the door opens."
    show grandpa neutral at left with dissolve
    g "I told you people I don't want any-"
    show grandpa surprised with vpunch
    stop music fadeout 1.0
    #SFX - waves (calm)
    "The old man stands frozen before me. He looks as though he's seen a ghost."
    y shocked "Grandfather…?"
    show grandpa happy at jumpin
    g "Oh, bless the stars...you got my letter? you're really here! My dear, sweet [y]!"
    "Suddenly, I'm caught in his embrace. He may be older, but his strength certainly has not faded." with vpunch
    "I hug him tightly in return. The wave of anxious anticipation I had moments before seems to vanish entirely."
    y neutral "It's been too long, Grandfather!"
    g "Oh, and I see the lad brought you here. Thank you my boy, get in here too!"
    h "Hah? Sir, that's not necessary-"
    g "Just 'cause you're a man now doesn't mean I can't still embarrass you like my own grandchild!"
    show grandpa happy at right with move
    "Grandfather traps Hunter too. Though Hunter groans, I can't help but laugh." with hpunch
    "Once he has squeezed the daylight out of us, he lets go."
    show grandpa happy at left with move:
        ease2 0.3
    g "It's been years! Oh, just how many years has it been since  I've seen the both of you together...How many years has it been since I've seen you, [y]."
    g "How's your mother? She never replies when I write to her."
    g "Nor has she ever let you reply to the letters I've sent you over the years."
    "My heart sinks."
    y "Mother has been well, as well as Father. But, well..."
    y "She read the letters, but never let me see them. I only recently saw them myself."
    y "She let me keep the gifts you sent, but never the letters..."
    show grandpa neutral with dissolve
    g "Oh, Marie..."
    "He lets out a wistful sigh."
    g "Can't be helped, I s'pose. Come on, then! Let's get you settled in."

    #SCENE CHANGE - Black Screen
    scene bg black
    stop sound fadeout 2.0
    "Time just flies by, and before I know it, it's been a week."

    #SCENE CHANGE - Shabby Market
    scene bg shabby market with dissolve
    play music "audio/music_town.mp3" fadein 1.0
    show grandpa happy at left with dissolve

    "Today, Grandfather and I are shopping for the next week's supply of food before he meets a trader in the afternoon."
    show hunter neutral at right with dissolve
    "Along with Hunter, who just happened to be free."
    y neutral "...I don't know a thing about shopping for fish."
    h "It's easy enough. Just look at the colorin' and the smell."
    y "Color, I can do that. But I'd rather not have to smell them at all."

    # REMEMBER: variable to check if name is june - little birdie for any name other than june, little bug/junebug for june
    g "There's been worse smells, little bug."
    show grandpa happy at jumpin
    g "When ye've been on a ship for three days 'n three nights with ten dead mermaids and they're startin' to curdle in the sun, that's when the smell's bad! Har har!" with vpunch
    "I've learned some things from Grandpa in my time here."
    "He's quite proud of his history at sea with the mermaids."
    show grandpa neutral at left with dissolve
    g "But I s'pose you'll never get to see that, would you."
    "He also wishes I could've inherited his love for the hunt."
    y flustered "Apologies, Grandfather..."
    g "Nah, it don't bother me, little bug. Don't worry about me, I know it ain't everyone's cup of tea."
    ny neutral "Hunter taps Grandfather on the shoulder."
    h "Mr. Eaton, she's open."
    "Grandfather pulls out his timepiece and flips it open."
    g "Ah, look at the time already. Can't keep 'er waitin'. The ship won't pay for itself!"
    hide grandpa happy at left with dissolve
    show hunter neutral at farright with move
    "Grandfather takes his leave. I can tell he's trying to be cheerful, but he still looks dejected."
    y flustered "Grandfather..."
    "Out of habit, my hand finds my camera still sitting at my side, waiting."
    y "I wish I could find some way to cheer him up."
    h "Hmmh?"
    y neutral "Is there anything Grandfather likes that I could get him?"
    h "A present, huh?"
    h "Hmm, I have an idea."
    y "You do?"
    h "Mr. Eaton'd be ecstatic to hear you go out to see one of his old haunts."
    h "How do you fancy a boat ride?"
    h "I can steer us to the safer part of the sea."
    y "That sounds perfect!"
    y "Oh, thank you, Hunter!"
    y "We're going to make Grandfather's day!"

    #TODO SCENE CHANGE - Sea
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
    "The boat travels further out to sea, putting the port behind us."
    show hunter neutral with dissolve
    h "How are you enjoying the view?"
    ny shocked "I'm about to respond to him, but the ship catches on the waves, and I stumble." with vpunch

    #SCENE CHANGE - view of the sea (stormy)
    scene bg choppywave
    play music "audio/music_storm.mp3" fadein 2.0 volume 0.4
    play sound "audio/sfx_wavesChoppy.ogg" volume 0.4 loop
    show hunter neutral with vpunch
    h "What the damn-"
    "The weather changes nearly in an instant."
    "I can't see a hint of blue in the sky."
    "Our perfect sailing day was covered by clouds of grey."
    y shocked "It was sunny only moments ago! What is this?"
    h "Blasted...I've sailed us right into a sea witch's storm! Hold onto something, [y]!"
    if seastorm:
        "I remember reading something about this."
        "If this is a sea witch’s storm…"
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
    h "The waters are getting choppier, stay away from the ledge!"
    y huffed "Well, obviously! I can hardly stand straight!"
    hide hunter neutral with dissolve
    "He returns back to his position, eyes staying forward as the winds grow stronger."
    "I can hardly see out, but I can't give up my quest for a picture."
    "The sounds of the waves and the wind make Hunter's words hard to hear."
    $ config.side_image_tag = "june"
    "I hold my camera up, making sure my hand is ready to press the trigger once I see a mermaid."
    #SPRITE?

    play sound "audio/sfx_waveCrash.wav" volume 0.06 fadein 1.0
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.06 loop
    play music "audio/music_underwater.mp3" volume 0.2 fadein 1.0

    u "Come...come with me..."
    y shocked "What...?"
    u "O' ye of land to the queen of sea..."
    "My thoughts are hazy, and my body feels as though I'm floating."
    h "[y], what are you doing?!"
    u "Come with me..."
    u "...to the depths below..."
    "The singing feels as though it is only for my ears to hear alone, the waves calling out for me to sink in."
    h "Shit, it's a siren! [y]!"
    show hunter neutral with vpunch
    "Hunter abandons his position at the helm of the ship and races towards me, but I can't imagine why."
    "An unimportant thought crosses my mind. I've heard of something like this before."
    "Sailors being sung to by the sea, only to be met with death..."
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
    "The regret floods my mind, but it's too late."
    "I can feel myself fading..."
    "..."
    stop sound fadeout 2.0

    #SCENE CHANGE - Black Screen
    scene bg black
    play music "audio/music_underwater.mp3" volume 0.7
    siren "After all these long years… you’ve finally returned home to me..."
    "..."
    "...Where am I?"
    siren "Hmm, hmm, hmm."
    "A strange voice is humming a familiar song."
    siren "Ah! you've woken up, little human."
    y "Blub!"
    "....Huh."
    y "Blub blub blub!"
    siren "Or shall I say fish?"
    "Hands, impossibly large and glowing strangely, come down to cradle me."

    #PUT SKYLLA HAND CG HERE

    #SCENE CHANGE - underwater cave (skylla's)
    scene bg underwater cave with dissolve:
        zoom 0.5
    $ config.side_image_tag = "june"
    "All at once I recognize her, or her voice at least. This is the same siren that caused me to go overboard."
    y neutral fish "BLUB BLUB BLUB!!!"
    show skylla neutral with dissolve
    siren "Ahaha! Oh, you cute thing. That's no way to speak as a lady!"
    "Try as I might, none of my words come out right."
    "And I've...{w} been turned into a fish by this siren!?"
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
            "I try to swim at her, but an invisible wall stops me before I can get close enough to smack her."
            "Near-invisible, I should say. The walls are shining."
            "A bubble?"

    siren "Aw. You’re hurting my feelings!{w} Aren’t you happy to see me?{w} When Skylla calls, little mers are meant to follow."
    "Skylla..? Is that the name of this siren?"
    "Suddenly she leans in closer. The look in her beautiful eyes turns dark and ravenous. A cold and instinctive fear shoots through my gut."
    s "There’s no reason to rush. We have all the time in the world together. You'll give me what I want in due time."
    s "Now, where did I put that pestle?"
    hide skylla neutral with dissolve
    "The voice swims away, and I'm left alone to contemplate my new fate."
    "No matter how hard I press my hands - well, fins - against the bubble, I can't push through!"
    "I'm trapped. There's no doubt about it."
    "Am I cursed to stay like this...forever?"
    stop music fadeout 2.0
    "At the thought, horror rolls through me like a wave. My body is all wrong, somehow warped into the wrong shape."
    "I have no hands to take pictures with.{w} No legs to run back home with.{w} No words to cry out with."
    "Forever? Like this?"
    "Or maybe...{w}am I going to die after being eaten as a special dinner course?"
    "Suddenly the memories of the mermaid market come to mind. Their bodies had been taken apart to become a cheap meal."
    "I am no different from them now.{w} Just as helpless."
    "From the distance I can hear the siren humming to herself as she swims to and fro around the cave."
    s "One piece at a time..."
    "No.{w} No, no, no."
    "Think, [player_name], think! There has to be a way out of here!"
    "If there’s a way to turn a human into a fish, surely there’s a way to turn a fish back into human, right?"
    "I glance around the cave I’m in."
    "It’s dark here, hard to see. My new tiny eyes struggle to take in everything all at once."
    "From what I can see there’s only a path forward deeper towards the siren’s lair. No windows, or whatever the underwater equivalent is."
    "There are what looks like glowing stones on the walls. What are the odds that they could magically explode?"
    "Come on, [y]! You can do better than this! What else is there?"

    show skylla neutral with dissolve
    "Before I can finish the thought, the siren swims back towards me."
    "Her clawed fingers gracefully pop the bubble trapping me, but just as swiftly in that motion her hand clasps around me."
    "My heart begins rushing in my tiny body. She could pop me in an instant as well."
    s "Hold still now, cute thing. This won’t hurt."
    "It’s a lie. Strange magic begins to glow out of the siren’s hands as she softly sings."
    "It’s beautiful beyond words, but the moment it starts I start to feel a burning pain spreading across my body."
    s "It’s okay! Don’t be stubborn now. Come on, it's me!"
    "I can't even scream as I feel something tugging in me, as if the siren is reaching inside of my body and trying to pull me apart."
    "The moment I feel like I’m about to snap in two, a sudden blinding light flashes throughout the cave."

    #FLASH EFFECT

    "The siren screams as she drops me, falling backwards."
    s "No. No! This- this isn’t right."
    "Once I blink the white spots out my vision I look up and find the siren staring at me with a shocked expression on her beautiful face."
    "Her hands are bleeding."
    "We both stare at each other, frozen, before I remember myself and swim away from her, pushing my tiny fins as hard as they can go."
    s "You little {i}eel!{/i} Get back here!"

    y "Blub blub!!"

    "As if! Who in their right mind would do that!?"
    "Her tentacles try to grasp me, but I’m too small for them to catch."
    s "Fine! Be like that!"
    "She begins humming to herself again, and a bolt of magic shoots out of her hands."
    "I twist away just in time, and the magic misses me and collides with one of the glowing stones on the wall of the cave."
    "Time seems to slow down."
    "I hear a whirring coming from the stones like the sound of a shrill kettle, and in the next second the stones explode."
    "The force spends me sprawling backwards in pain, but I don’t have time to linger on it because the explosion has created a hole just big enough to squeeze through."

    scene bg black

    "I swim as fast as I can. Faster than I’ve ever ran when I had legs."
    "My heart is thumping madly in my chest as I force my way through the debris. "
    "The sharper pieces scrape and cut through my fins but I barely pay them any mind as I keep swimming.{w} I think that if I had my voice I would be crying."
    "I can hear the siren cursing as I swim away, but eventually it shrinks into a distant shriek as I keep charging forward with all I have."
    "It doesn't matter where I go, just as long as it’s far away from that awful witch!"

    scene bg sea with vpunch

    "I stop to catch my breath after what feels like a lifetime."
    $ config.side_image_tag = "june"
    y fish neutral "Blub…blub…"
    "Now that the adrenaline has faded I feel exhausted. My body feels like it’s been run over. Everything hurts."
    play music "audio/music_underwater.mp3" volume 0.7

    "Grandpa...Hunter...they must think that I’m dead by now."
    "At the thought of them, I suddenly feel overwhelmingly homesick. I need to tell them I'm alive!"
    "But... {w}how am I supposed to make it back to land?"
    "The only one that might be able to change me back is that siren, but there's no way I can go back there."
    "Before I can dive any further into those thoughts I hear voices approaching from a distance."
    "I quickly dart into some foliage to hide."

    #THIO AND JOR ENTER THE STAGE
    #Voice Lines Start (old, deleted the comments where they were due to script changes)
    show kelp with vpunch
    novisualthio "The further out you swim, the more guilty you are! Those fish belong to the Vanguard."
    novisualthio "Return them now, and your judgment will be fair."
    novisualjor "Well I am sorry, my prince! But I was kind of hoping I could skip the judgement part entirely!"
    novisualjor "Maybe you could ask your Vanguard to find you something else for your dinner? They could always go pilfer from other villages."

    "A '{i}prince{/i}'?"
    "Curiosity piqued, I lean over as much as I dare to stare at the new arrivals."

    hide kelp with dissolve

    show prince angry at left
    show jorunn sweat at moreright
    with dissolve

    "Ahead of me, two mer-people are staring each other down."
    "One of them is a young man carrying a large net stuffed full of fish."
    "The other one has fins unlike any other I’ve seen, a striking array of blue.{w} He has what looks to be a bodyguard hovering close to his side."

    "Prince...? Bodyguard? Do mermaids really have that kind of thing?"
    up "Are you suggesting that {i}we{/i} sink to {i}your{/i} level?"
    uj "Oh no. No, of course not!"
    show jorunn glee at moreright
    uj "...But if the shoal fits!"
    up "You thieving little-"

    show prince sweat at left
    show jorunn sweat at moreright
    with vpunch

    "Just then, a loud rumble echoes through the area. The waters feel like they’re slowly beginning to churn."
    guard "It’s another sea storm, Your Highness! We must head back now before it picks up any further."
    show prince angry at left
    up "Dammit. Why now of all times..!"
    show jorunn glee at moreright
    uj "Well I guess that's my cue! I’ll be taking these home then. Goodbye!"
    "The rumble comes again, a bit louder this time. My heart sinks as I realize I might not survive whatever kind of storm is coming." with vpunch
    "Do I approach the prince? Or perhaps the other fellow? Maybe this is dangerous...but they might be my only shot at getting help right now."

    if promermaid >= 1:
        "Anything would be better than returning to the sea witch."
    if antimermaid >= 1:
        "Should I even be trusting any of them? Chasing mermaids is how I became stuck like this."
    "Either way, they're both starting to swim away."

    #Follow Striking Prince
    #Follow Scrappy Boy (can't choose this yet, lol)
    menu:
        "Follow Striking Prince":
            $ prince_points += 1
            jump ch1_followprince

label ch1_followprince:
    #BRANCH - FOLLOW PRINCE
    hide jorunn glee with moveoutright
    "Perhaps the prince would be kind to someone in need? I hope I'm not a species of fish they fight over for eating."
    "All I have to do is just wait for this shark to pass..."
    "3....2...1!!"
    $ config.side_image_tag = "june"
    y neutral fish "BLUBBB!!!!"
    "With all the might I can muster I push my way through the current, leaving a trail of bubbles behind me."
    "It feels like riding a bicycle downhill without any brakes to stop me."
    "I can’t stop, crashing into the back of the striking merman’s head."

    #SCREEN SHAKE
    $ config.side_image_tag = "None"
    # voice "audio/voice/prince/THIODAL-7.wav"
    show prince sweat at furthleft with hpunch
    up "!!!"
    # voice "audio/voice/prince/THIODAL-8.wav"
    show prince angry with hpunch
    up "Who-"
    $ config.side_image_tag = "june"
    y "Please help me!!"
    show prince neutral
    # voice "audio/voice/prince/THIODAL-9.wav"
    up "...?"
    guard "The fish drew their attention!"
    "The sharks hurl towards us in a frenzy, chomping at the water and whatever moves in front of them."
    "I swim as quickly as I can past the striking merman, hoping the sharks haven't caught my scent."
    "I know I've scraped something swimming out of the cave. It's a minor itch, but I can feel the blood seeping from my body as I propel through the water."
    "And if sharks are drawn to blood, it's only a matter of time before I'm done for!"
    "The princely fellow seems to realize this, at least."

    show prince angry at furthleft with dissolve
    # voice "audio/voice/prince/THIODAL-10.wav"
    up "You there! Lead it that way!"
    "I swim in the direction he is pointing, and I notice in horror that he has not followed me there."
    "However, my worry is unwarranted."
    "He must have quickly brandished a weapon between the eyes of the great white, as a cloud of bubbles and a hole in its head are all I can see before it is over."
    "The shark sinks quickly to the ocean floor, pushing up the sand below, blood intermingling with the tide."
    "Surely this dead shark is more tantalizing than my pitiful injury."

    show prince neutral with dissolve
    # voice "audio/voice/prince/THIODAL-11.wav"
    up "Let us away, before the others come."
    $ config.side_image_tag = "june"
    y "....R-Right!"
    "How fearsome his strength must be. He certainly doesn't seem the type."
    "The wave of adrenaline is starting to finally calm down, but I follow him diligently to a safer spot away from the cave and the sharks."
    # voice "audio/voice/prince/THIODAL-12.wav"
    up "Stay still for a moment."
    show prince angry with dissolve
    "His brow furrows as he draws closer to me, his hands hovering my sides, but not quite enclosing my body."
    "A faint glow surrounds me, the scales reforming over in moments."
    show prince neutral with dissolve
    "Almost instantly, I could feel my energy return. I suppose being so small, even a little bit of blood loss could make you quite weak."
    "Was that healing magic? I've only heard of it in books."
    y "Ah, I should--no, wait. I forget myself."
    y "Thank you, sir."
    "Through some miracle, it seems he can understand me."
    # voice "audio/voice/prince/THIODAL-13.wav"
    up "You speak strangely, but that's none of my concern. You're either extremely resilient, or a spy of that Sea Witch."
    y "I'm not a spy! I'm just a resilient type, as you say!"
    "I sincerely hope he believes me, as it's true."
    # voice "audio/voice/prince/THIODAL-14.wav"
    up "I suppose I will believe you for this moment. Your wounds have been taken care of, so please, return to your reefs...safely."
    guard "Prince Thioran!! Are you injured?"
    # voice "audio/voice/prince/THIODAL-15 v2.wav"
    p "Of course not."
    "His vanguard found us, relieved to see their charge unhurt."
    "However, the guards pointed their weapons at me."
    guard "Her kind shouldn't be this deep in the ocean."
    guard "Couldn't this one be a spy?"
    "No, surely they wouldn't just kill me for being strange!!"
    "The Prince seems to think about this for a moment, but he looks too exhausted to give it proper consideration."
    "Yet his glances at me, do they feel familiar? It would be impossible for us to have met before today, yet I get the feeling we have, somehow."
    # voice "audio/voice/prince/THIODAL-16.wav"
    p "It is quite uncommon. Most of her kind wouldn't be able to withstand these depths."
    # voice "audio/voice/prince/THIODAL-17.wav"
    p "However, if she was a spy, I doubt the sharks would have attacked her."
    # voice "audio/voice/prince/THIODAL-18.wav"
    p "I believe she was only swept up in our clash."
    # voice "audio/voice/prince/THIODAL-19.wav"
    p "Regardless, there are other matters we must attend to, and we've already wasted enough time."
    "He turns to address me last."
    # voice "audio/voice/prince/THIODAL-20.wav"
    p "So please, you are free to go. You have my permission."
    "I don't need his blessing- I just need whatever magic power he has to help me turn back to normal!"
    "Clearly he knows a trick or two, especially with those sharks."
    y "If it's alright, I would like to make a request. "
    y "Could you lead me back to...the kingdom? I...have business there."
    show prince soft with dissolve
    "He stares at me for a few moments, with an indeterminable expression on his face."
    # voice "audio/voice/prince/THIODAL-21.wav"
    show prince neutral with dissolve
    p "You may follow us. When we arrive, attend to your business. Any other troubles from then on must be your own."
    y "That's more than enough! Thank you!"
    "That is definitely not enough!!"
    "If I stay, that could be my chance to find some answers to cure my fishy affliction!"
    "I follow the Prince and his guards across the sea, taking in the sights as I pass them."

    "I am behind the Knights that swam in a march, putting distance between me and the prince."
    "I suppose I'm no longer allowed to speak with him."
    "..."
    "Left alone with my thoughts, my mind races every which way."
    "Am I the first human to experience the sea like this?"
    "I wish I had my camera. But it wouldn't survive the plunge."
    "I hope it somehow escaped my fate."
    "Hunter must think the worst outcome for me, falling like I did."
    "And...oh, Grandfather!"
    "He would be devastated to find out I went overboard!"
    "They're going to think I drowned.."
    "I need to return back."

    scene bg sea with dissolve
    "The waters seem to brighten more as we swim, peaks of coral and schools of beautiful fish."
    $ config.side_image_tag = "june"
    ny june neutral fish "We arrive at a place just before a city, where a mesmerizing merman waits."
    c "My lovely nephew! Where have you been?"
    c "I hear news of an attack, and you do not deign to tell me?"
    show prince sweat at right with dissolve
    # show cetus at left with dissolve
    # voice "audio/voice/prince/THIODAL-22.wav"
    p "Cetus. It has been a long day. You will have to forgive my impropriety."
    c "Always so stiff."
    c "I merely jest. I know no trouble would come of an attack on you."
    "The man called Cetus seems familiar as well. The more he speaks, the more I also feel a sense that I have met him before."
    c "Oh? Who's this you have following you like a pet, Thio?"
    "His gaze catches on me, and I want nothing more than to dart behind a rock and hide."
    # voice "audio/voice/prince/THIODAL-23.wav"
    p "I...did not ask for a name. She claims to have business here in the city. By formality, I allowed her to return with me."
    c "I see."
    "Cetus stares at me for a moment before he starts chanting in a low tone. The prince does not pay it any heed."
    # voice "audio/voice/prince/THIODAL-24.wav"
    show prince neutral at right with dissolve
    p "I will return shortly to my duties, Uncle."
    "My body seizes, and I feel drawn towards Cetus." with hpunch
    "The prince does not seem to take notice..."
    "My will is no longer mine, and I am no more than a mere fish lost in the sea."
    "It's just like how I felt when the siren dragged me under."
    "Suddenly, a burst of light breaks my body free from the trance, and I feel my fins begin to change."
    scene bg white with hpunch

    stop music fadeout 2.0
    scene bg black with dissolve

    "..........."

    show jorunn glee with dissolve

    j "Hello there!"
    j "You've reached the end of the demo for Heart's Depth!"
    j "We sincerely look forward to releasing the rest of the story." with vpunch
    show jorunn pissed at moreleft with dissolve
    j "I hope they put me in the next update..."
    show jorunn glee at moreleft with dissolve
    j "Anyway."
    j "Thank you so much for playing! Follow our game page for updates."
    j "We have much, much more to come..."
    play sound "audio/sfx_splash.flac"
    hide jorunn glee with dissolve

    #END OF DEMO!!!!!!!

    return

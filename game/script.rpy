# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define y = Character("[player_name]", image="june")
define ny = Character(None, image="june") # for narration
define g = Character("Grandfather", image="june")
define h = Character("Hunter", image="june")
define s = Character("Skylla", image="june")
define c = Character("Cetus", image="june")
define p = Character("Prince Thioran", image="june")
define j = Character("Jorunn", image="june")
define t = Character("Townsperson", image="june")

define u = Character("???", image="june")
define guard = Character("Guard", image="june")
define up = Character("Striking Prince", image="june")
define uj = Character("Thieving Merman", image="june")

define furthleft = Position(xpos=0.20)
define farleft = Position(xpos=0.25)
define moreleft = Position(xpos=0.35)
define center = Position(xpos=0.45)
define moreright = Position(xpos=0.60)
define farright = Position(xpos=0.70)
define prettyfarright = Position(xpos=0.85)

init python:
    config.side_image_tag = "june"
    #proritize voice as highest volume
    config.emphasize_audio_channels = [ 'voice' ]

# The game starts here.

label start:
    $ hunter_points = 0
    $ prince_points = 0
    $ jorunn_points = 0
    $ cetus_points = 0

    #lower music when voice line is playing
    default preferences.emphasize_audio = True

    # "NARRATION"

    # # If you want to hide the side image
    # $ config.side_image_tag = "None"

    # "This is a narration so the side image shouldn't appear."

    # # ""

    # #this above one makes a blank thing, good for comedic effect?

    # #NEED TO DO THIS EVERY TIME THERES NARRATION W/ NO PROTAG
    # # To unhide the side image
    # $ config.side_image_tag = "june"

    # m neutral "It's so cold"

    jump get_name

label get_name:
    scene bg black

    show side june neutral at farleft with dissolve:
        yalign 0.1

    #GET PLAYER NAME
    $player_name = renpy.input("What is your name?",length=15)
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

    scene onboat with dissolve
    show hunter neutral with dissolve
    $ config.side_image_tag = "june"
    y neutral "It was sunny only moments ago! What is this?"
    "TESTING!!!!"

    #TODO SCENE ?
    scene bg choppywave with dissolve

    play music "audio/sfx_wavesChoppy.ogg" volume 0.6 loop

    $ config.side_image_tag = "june"
    y neutral "It was sunny only moments ago! What is this?"

    $ config.side_image_tag = "None"

    # show hunter at moreright with dissolve

    u "Blasted...I've sailed us right into the sea witch's storm! Hold onto something, [y]!"
    "The ship creaks as he tries to turn it back towards the port, but the waves are unrelenting."
    "Something stirs in the back of my memory as I stare down into the waves below."
    "I can see something glowing through the wind and rain."

    #SCREEN SHAKE
    h "[y]!" with screenShake
    $ config.side_image_tag = "june"
    "I try to reach for it, forgetting myself for just a moment."

    #SFX - SPLASH
    scene bg black with vpunch
    play sound "audio/sfx_splash.flac"

    #SCENE CHANGE - (Underwater / Black)
    stop music
    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "The regret floods my mind, but it's too late."
    "I can feel myself fading...is this really the end...?"
    jump chapter1

#CHAPTER 1
label chapter1:
    #TODO SCENE = CG (Train)
    scene bg shabby town
    play music "music_town.mp3" fadein 1.0

    $ config.side_image_tag = "june"
    "Salty air...I remember how I would try to stick out my tongue to taste it."

    "I was a child the last time I did something as silly as that."
    "I can't wait to see it again, but when I think about the ocean, I can't help but feel  like I broke a promise to it."
    "It has been 10 years since I've last seen the ocean. Perhaps it was just because I missed Grandfather after being inland without contact for so long."
    "I only ever got to see my grandfather on special holidays in the summer, but now I'm returning to Aquantis again just to see him."
    "I can't really remember why my mother stopped letting me see Grandfather. She said she had lost trust in him after something that happened to me here when I was a child."
    "Even though I am now grown, she refuses to say what happened."

    $ config.side_image_tag = "None"
    t "Please gather all personal belongings, we are arriving at Aquantis Station!"

    $ config.side_image_tag = "june"
    y neutral "Oh, we're already here?"

    "The screeching of the brakes signal the train to a stop."
    "From my car seat window, I let the shutter of my camera go off, taking a picture of the people outside."
    "It's been years since I last stepped foot here."
    "The letter Grandfather sent me had his address, though it would be helpful to ask for some directions. The harbor city is huge."
    "Homes and shops descended down the hill that lead to the ports, cramped with new and old parts of the city mixed together."
    y "Excuse me- sir! Hello?"
    "He ignores me, walking quickly away from the station."
    "I try to ask few more people, but not one wants  to give me the time of day."
    "Trying to grab anyone's attention around here seems impossible! They all just ignore me. Were they so unfriendly to people from outside when I was younger? I can't remember."

    #SCENE CHANGE - (Shabbier part of Town)
    scene bg shabby town

    "The further I walk down from the top of the city, the more and more the atmosphere seems to change."
    "Rather than being ignored, it seems I'm attracting an uncomfortable attention."
    "I can feel the eyes of  the people I pass by watching me."
    "It looks like these parts have fallen into harder times. When I was younger I remember it being more lively and nice, but now, I feel as though I should keep my eyes to myself."

    $ config.side_image_tag = "None"
    t "Tch, inlanders. What is someone like her out here for?"
    t "Inlander? Oy, you don't see many of them.. And she's got a fancy one of those picture devices, that could land us a nice bit of coin aye?"

    #SPRITE CHANGE (Annoyed Expression)
    $ config.side_image_tag = "june"
    ny huffed "Are they referring to my camera? They're hardly being secretive about wanting to rob me!"
    "I quietly slip away from the men watching me, heading further down the road."
    "I keep my camera close to my hip, hiding it with my coat to draw away any more notice."

    #SCENE CHANGE - (Shabby Market [Zoomed In])
    scene bg shabby market
    ny neutral "The smell grows worse as I suddenly find myself at a market."
    "The smell of fish, salt, smoke and sewer is strong here. Though despite it, there seemed to be a few friendlier townsfolk around."
    "I approach the friendliest of the bunch. A man mans his fish stand, hawking his catches."

    #SPRITE CHANGE (??? Expression)
    ny shocked "I just hope I'm not expected to buy the fish covered in flies."

    #SCENE CHANGE - Shabby Market (or CG [Merchant at Fish Stand])
    scene bg shabby market
    y neutral "Good day to you sir. I'm sorry for disrupting you, but-"
    t "Bass or Tilapia?"
    y "Oh- er, well...I'm not looking to buy fish right now. Could you please help me with the directions to-"
    t "Does I look like a map stand? I sell fish, ye buy fish, ye leave- ye get it?"
    y "I will pay you for the help! I'm just looking for this address."

    "Before he could deny me once more, I showed the bottom half of the letter where the address was clearly written. He squints at the paper, adjusting his sight to get a better look at it"

    t "...Girlie, do ye know where that is? That's in the Black Market District. Someone like you don't belong there. Hell, even I avoid it."

    "Black Market District..?"
    y "Even so, I have to get there. I'll pay you if you just point me in the right direction."
    "He gave a sigh and pointed forwards to the end of the market square."
    "Truly, the only way to get through to these people is money."
    t "Take a left down that alley, give five knocks on the brick, pause, give three knocks, and pause again to give four."
    t "That'll open the elevator for ya to take ya where you need goin'."
    t "That's all I know, and all I'll say."
    "He looks at me and grins toothily."
    t "Payment?"
    y "Oh, yes. Thank you so much for the help."
    "I leave him a fair amount of coin and follow his instructions to the alleyway."

    #SCENE CHANGE - Brick Wall
    scene bg brickwall
    "Upon reaching the end, I make a left turn down to see a brick wall. It has an odd discolouration unlike the rest."
    "This must be the wall the merchant spoke of. "
    "Well."
    "I stare at the wall for a few moments. This is certainly not something I had planned for this trip."
    "I suppose I'll just have to give it a go."
    "..3..4..5…"
    "..1..2..3…"
    "..2..3..4.."
    "There is no response, but..."
    "Suddenly, the wall was pulled back."
    "With cautionary steps, I pushed inside, seeing no one was there behind the door."
    stop music fadeout 5.0

    #SCENE CHANGE - Black Screen
    scene bg black
    "It closes the moment I enter. It must be an ancient elevator, rusted and old."
    #SFX -  Elevator
    play sound "audio/sfx_elevator.wav"
    "The rickety elevator descends down for a while. I start to regret stepping inside - who knows what I would find so far down?"
    "..."
    "..."
    "..."
    #SFX -  Elevator
    play sound "audio/sfx_elevator2.wav"
    "Until it finally comes to a stop, the door opens, and I am greeted with a new world."

    #SCENE CHANGE -  Underground Black Market Faire
    play music "music_blackmarket.mp3"
    scene bg underground market
    "It's  almost like a circus, or a fairground. Many merchant's booths had strange knick-knacks begging to be looked at."
    "Exotic fruits, animals, books, and so many more things from what must have been lands long gone to the waves being sold here as rarities. "
    "My eyes follow every gleaming thing being displayed."

    y neutral "This is incredible..."
    "As I walked around in awe, my eyes caught on a stand of tropical flowers arranged in a beautiful pattern."
    y "Mother would love to see this..."
    "My hand reaches for my camera once more."
    $ config.side_image_tag = "None"

    show hunter neutral with dissolve

    u "I wouldn't dare to take out that camera here, unless you're planning on joining the fish in the stands."
    "My heart sunk as I stood frozen, feeling a gloved hand on top of my own, stopping me."
    u "I knew I saw a familiar face in the crowd. I knew it was you, [y] Finch~."
    u "I turned to see who the hell the man was behind me. How does he know my name? I slap his hand away from mine and glare at his face."
    "I do not recognize him."
    u "It's a bit rude to slap a friend, isn't it?"
    $ config.side_image_tag = "june"
    y neutral "Who are you, exactly?"
    "He scoffs and shakes his head." with hpunch

    #TODO SPRITE CHANGE - Hunter Disappointed
    u "You don't remember your old playmate? I'm hurt! After all these years, I didn't once forget about you, [y]."
    y "I haven't been in this part of Aquantis before. You must have me mistaken for someone else."
    u "Ha- this isn't your first time here. Don't appreciate being treated like a stranger, though I suppose it's been awhile."
    "Bending down to my level, the stranger looks me right in the eyes."
    u "Jogging anything in that noggin'? I've grown up a bit since you've last seen this mug...how 'bout it?"
    "He stares at me for a moment before the realization hits."
    u "Ah, that's right. Perhaps the name will help."
    h "Hunter Aubrey Morrowe."
    y "...Hunter?"
    h "That's my name, yes."
    "He looks positively delighted to hear me say his name."
    y "..."
    y "Oh!"
    y "Right, Hammy! You were so different when we were young!"
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

        "Drop it.":
            y "But of course, I'll just call you Hunter, now."

    "We used to play near the beach as kids. If there was anyone I'd recall from my time here, it'd be him."
    "We were fast friends, though I can't remember much of what we did together. He was a strange little kid."
    h "At least you remember me! It's been only about, what… ten years since we've last seen each other?"
    h "I'll be honest, never expected you to come back."
    "I do remember his smile when he was trying to show me shells or bugs he found on the beach."
    "As I look at him now, it seems like the only thing that remains is that smile."
    y "I came to see my grandfather, if you still remember him."
    h "Ah~ family visit. Of course I still remember the old man. His hunting company practically owned half the market strip. Though he went into retirement a few years ago."
    h "Need some help finding your way?"
    y "Well, yes, if you wouldn't mind..."
    h "I'll take you. Just keep your camera out of view."
    h "And stop gawking at things like you've never been here before...People might think you're a spy or somethin'."
    "He unclips his cloak and throws it on top of my head. My nose is assaulted with the salty smell of the sea."

    #SCENE CHANGE - Black Screen
    scene bg black

    #SCREEN SHAKE
    y huffed "Hey! don't just throw this dirty thing on me!" with screenShake
    h "Just keep it for now. Keep your eyes down so people can't clearly see your face...and to avoid seeing things you shouldn't be looking at anyways."
    y neutral "Seeing things I shouldn't be..?"
    "Things I am forbidden to see...I feel a pressing need to see them - but a far more pressing urge to stay hidden from the rest of the townsfolk here."
    "I do as he asks, even if the cloak starts to chafe on my shoulders and crush my hat."

    #SCENE CHANGE - Black Market
    scene bg underground market

    show hunter neutral with dissolve

    "He takes my hand and gives a low hush, leading me through the crowd. I look down at my feet."

    #SFX - CROWD
    play sound "audio/sfx_crowd.wav" volume 0.2 loop

    "He walks meticulously, carefully weaving through the crowds of people, and I try my best to keep in step with his strides."
    "But then, I see something tantalizingly curious out of the corner of my eye. Without thinking, I glance up. "

    #TODO SCENE = CG (Mermaid in Tank [Zoomed])
    scene bg underground market with dissolve
    "There is a pale but beautiful face in the dark, behind glass."
    "The further along we walk, the more of her face is revealed."
    "Her body is so human and serene from the top, but her lower half....scales, a tail that flows in the water and reflects off the dim lights around her."
    "A woman....no, a creature that is equal parts human and fish."

    y neutral "Beautiful..."

    #TODO SCENE = CG (Mermaid in Tank [Full])
    scene bg underground market
    "Her long silver hair moves in the water just like her tail. She is mouthing something, banging on the glass, but I can't hear a word."
    "Her eyes seem to lock onto mine for a moment."
    "Is she asking for my help?"
    "Suddenly, my view of the rest of the stand is unblocked, and I am able to peek through the empty spot in the crowd. It's a fish hawker's stand."

    #TODO SCENE = CG (Mermaid cut in half)
    scene bg underground market
    "Her sign reads 'Catch of the day'. Another mermaid, eerily similar to the face banging on the glass, on a table in front of the tank."
    "Except she is missing her body from the hip below; tail being taken by rabid customers, piece by piece."
    "As if she was just the catch of the day. Another fish for someone to eat for dinner."
    "I grip Hunter's hand tighter, and he starts to walk faster through the crowd."
    show hunter neutral with dissolve
    h "I said keep your eyes down, or people might see your face. Believe me, you don't want them remembering who you are."
    $ config.side_image_tag = "june"
    y neutral "I know."
    "I glance back for just a moment before turning back away."
    "The cruel reality of the world. There isn't much I can do about it."
    "To fill the air with something else, I ask Hunter a question."

    menu:
        "Do you hunt now, too? Like your father?":
            $ hunter_points += 1
            h "Well, yeah, I do. It's the family business, though your family left it to mine."
            h "Your old man always talked about wanting you to come back to join him, but when he announced his retirement, he sold most of it to my father instead."
            y "I see..."

        "Have you actually...killed them before?":
            h "Why do you sound so horrified? Fish is fish. Don't be fooled by their appearances."
            h "If anything, they're monsters using human faces. They don't deserve your pity."
            h "...But yes, I have."
            y "..."

    stop sound fadeout 2.0

    #SCENE CHANGE - Port w/ Boats
    play music "music_town.mp3" fadein 1.0
    scene bg port
    "Once we make it outside the underground and I can finally see the sky again, the sun is high in the sky."
    y neutral "It's afternoon already?"
    show hunter neutral with dissolve
    h "Wandering does that to ya. When did your train get here?"
    y "Early morning. My legs are aching to sit."
    h "We're almost there. Don't keel over on me, would you?"
    y "I wouldn't dream of it."
    "We're actually at the portside now, the edge of the country. Practically the edge of the world."
    "Boats lined up, fishermen and hunters alike lining the dock, carrying supplies to and from the ships."
    "They were much different than the ones I had remembered as a kid. These were large, made of steel, and produced steam."
    y "Does Grandfather live on one of these ships?"
    h "The only one still not made of steel, that one over there."
    "Out on the furthest side of the docks was a large wooden ship. It stuck out compared to the rest, with its clothed sails, and ornate details."
    "There was clearly a lot of pride and dedication to the maintenance of it."
    "I had a faint recollection of Grandfather owning a boat, of course, but I thought I would remember more than that upon seeing his home."
    h "Well, keep moving along already. I thought you'd be more excited to see your Grandpa!"
    y "Hey, don't start shoving me- I appreciate the help, but you really don't have to follow me the whole way there."
    h "I have business with your old man already, running into you was just a coincidence. Let's go!"
    y "Alright, alright, let's go."

    #TODO SCENE CHANGE - Port w/ Boats (ZOOM)
    scene bg port
    "We board a small rowboat to take us there."
    show hunter neutral with dissolve
    "Before I know it, we arrive on deck, and Hunter walks towards the entrance of the boat interior."
    "Ten years apart finally coming to an end. Perhaps my parents estranged us over a misunderstanding, and it will be a simple, happy reunion with no trouble at all."
    "I want to hear his side of it, regardless."
    "I want answers."
    show hunter neutral at right with move
    "Hunter knocks at the entrance of the ship."
    "There's some loud grunting and muffled swearing as the door opens."
    show grandpa neutral at left with dissolve
    g "I told you people I don't have any-"
    show grandpa surprised with vpunch
    "The old man stands frozen before me. He looks as though he's seen a ghost."
    y neutral "Grandfather…?"
    show grandpa happy with dissolve
    g "Oh, bless the stars… you got my letter? You're really here! My dear, sweet [y]!"
    "Suddenly, I'm caught in his embrace. He may be older, but his strength certainly has not faded."
    "I hug him tight in return. The wave of anxious anticipation I had moments before seemed to vanish entirely."
    y "It's been too long, Grandfather!"
    g "Oh, and I see the lad brought you here. Thank you my boy, get in here too!"
    h "Hah? Sir, that's not necessary-"
    g "Just 'cause you're a man now doesn't mean I can't still embarrass ye like my own grandchild!"
    show grandpa happy at right with move
    "Grandfather traps Hunter too. Though Hunter groans, I can't help but laugh."
    "Once he has squeezed the daylight out of us, he lets go."
    show grandpa happy at left with move
    g "It's been years! Oh, just how many years has it been since  I've seen the both of ye together.. How many years has it been since I've seen you, [y]."
    g "How's your mother? She never replies when I write to her."
    g "Nor has she ever let you reply to the letters I've sent you over the years."
    "My heart sinks."
    y "Mother has been well, as well as Father. But, well."
    y "She read the letters, but never let me see them. I only recently saw them myself."
    y "She let me keep the gifts you sent, but never the letters..."
    show grandpa neutral with dissolve
    g "Oh, Marie..."
    "He lets out a wistful sigh."
    g "Can't be helped, I s'pose. Come on, then! Let's get you settled in."

    #SCENE CHANGE - Black Screen
    scene bg black
    "Time just flies by, and before I know it, it's been a week."

    #SCENE CHANGE - Shabby Market
    scene bg shabby market

    show grandpa happy at left with dissolve

    "Today, Grandfather and I shop for the next week's supply of food before he meets a trader in the afternoon."
    "Along with Hunter, who just happened to be free."

    show hunter neutral at right with dissolve

    y neutral "...I don't know a thing about shopping for fish."
    h "It's easy enough. Just look at the colorin' and the smell."
    y "Color, I can do that. But I'd rather not have to smell them at all."
    g "There's been worse smells, little bug."
    g "When ye've been on a ship for three days 'n three nights with ten dead mermaids and they're startin' to curdle in the sun, that's when the smell's bad! Har har!"
    "I've learned some things from Grandpa in my time here."
    "He's quite proud of his history at sea with the mermaids"
    show grandpa neutral at left with dissolve
    g "But I s'pose you'll never get to see that, would ye."
    "He also wishes I could've inherited his love for the hunt."
    y "Apologies, Grandfather..."
    g "Nah, it don't bother me, little bug. Don't worry about me, I know it ain't everyone's cup of tea."
    "Hunter taps Grandfather on the shoulder."
    h "Mr. Eaton, Merrill's open."
    "Grandfather pulls out his timepiece and flips it open."
    g "Ah, look at the time already. Can't keep Merrill waitin'. The ship won't pay for itself!"
    hide grandpa happy at left with dissolve
    show hunter neutral at farright with move
    "Grandfather takes his leave. I can tell he's trying to be cheerful, but he still looks dejected."
    y "Grandfather..."
    "Out of habit, my hand finds my camera still sitting at my side, waiting, and I'm struck with a thought."
    y "Hunter."
    h "Hmmh?"
    y "I need your help."
    h "With what?"
    y "We're going to make Grandfather's day!"
    h "What, buy him mermaid nigiri for dinner?"
    y "No! I'm going to take a picture of a live one." with hpunch
    y "Imagine what people would pay for a picture!"
    "Hunter seems to think about it for a moment."
    y "Please?"
    "I put on my best begging expression, and he gives in immediately."
    h "I s'pose inlanders would think they'd be interestin' enough."
    h "Alright, it's a nice day. Let's get him a picture."
    y "Thank you!"

    #TODO SCENE CHANGE - Sea
    scene bg calmwave with dissolve
    stop music fadeout 1.0
    #SFX - waves (calm)
    play sound "audio/sfx_wavesCalm.ogg" loop

    "We embark on Hunter's fishing vessel, he at the helm and I at the edge of the railing."
    "The sea is calm, and the sun is shining down."

    show hunter neutral with dissolve

    h "I'm going to steer us towards the calmer ones. Might be able to spot one goin' onto the rocks for a sunbathe."
    y shocked "Mermaids sunbathe? Really?"
    h "When they feel safe enough to. If they spot my little skiff, the show's over."
    h "Gotta be quick with your pictures."
    y neutral "Of course!"

    hide hunter neutral with dissolve

    "My only experiences are with inland animal photography, I can't imagine it would be harder than capturing birds on film."
    "The boat travels further out to sea, putting the port behind us."
    h "As long as we avoid the hostile ones, we'll be in the clear. Keep an eye out, [y]!"
    "I'm about to respond to him, but the ship catches on the waves, and I stumble."

    #SCENE CHANGE - view of the sea (stormy)
    scene bg choppywave

    show hunter neutral with vpunch
    h "What the damn-"
    "The weather changes nearly in an instant."
    "I can't see a hint of blue in the sky."
    "It's covered by clouds of grey, instead."
    y shocked "It was sunny only moments ago! What is this?"
    h "Blasted...I've sailed us right into the sea witch's storm! Hold onto something, [y]!"
    hide hunter neutral with vpunch
    "The ship creaks as he tries to turn it back towards the port, but it seems to make no progress at all."
    "The lurching nearly throws me to the floorboards, but I grab the mast just in time to stay upright."
    y "Ah..."
    #SCREENSHAKE
    "Something stirs in the back of my memory as I stare into the waves. Something is glowing through the wind and rain."  with screenShake

    #TODO FLASHBACK CG for a second of baby prince and june
    y "Who...? This is familiar to me, but...?"
    #SFX - loud crash, screen shake
    play sound "audio/sfx_waveCrash.wav"
    scene bg choppywave with screenShake
    #SFX - choppy waves
    queue sound "audio/sfx_wavesChoppy.ogg" volume 0.6 loop

    show hunter neutral with vpunch
    h "The waters are getting choppier, stay away from the ledge!"
    y huffed "Well, obviously! I can hardly stand straight!"
    hide hunter neutral with dissolve
    "He returns back to his position, eyes staying forward and ahead as the winds grow stronger."
    "I could hardly see out, but I couldn't give up my quest for a picture."
    "The sounds of the waves and the wind made Hunter's words a bit hard to hear."
    y neutral"I hold my camera up, making sure my hand was ready to press the trigger once I saw a mermaid."
    #SPRITE?
    u "Come...come with me..."
    y shocked "What...?"
    u "O' ye of land to the queen of sea..."
    "My thoughts feel hazy, and my body feels as though I'm floating."
    h "[y], what are you doing?!"
    s "Come to Skylla..."

    "The singing felt as though it was only for my ears to hear alone, the waves calling out to me to sink in."
    h "Shit, it's a siren! [y]!"
    show hunter neutral with vpunch
    "Hunter abandons his position at the helm of the ship and races towards me, but I can't imagine why."
    "An unimportant thought crosses my mind. I've heard of something like this before."
    "Sailors being sung to by the sea to only be met with death..."
    hide hunter neutral with dissolve
    y "A siren's song."
    "At the edge of the boat now, my eyes look down below for the cause of my affliction, But the darkness below the waves are all I can see, and the voice all I could hear."
    "And with all my might I held tightly to the slippery ledge that parted me from the water, and yet my body went against my will to stay."
    "I sit atop the ledge."
    "And just for a split moment I think I can hear Hunter calling my name before I take the plunge."

    #SFX - SPLASH
    scene bg black with hpunch
    play sound "audio/sfx_splash.flac"

    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "The song stops, but my body is numb."
    "The regret floods my mind, but it's too late."
    "I can feel myself fading...is this really the end...?"
    stop sound fadeout 2.0

    #SCENE CHANGE - Black Screen
    scene bg black
    play music "music_underwater.mp3" volume 0.7

    s "Hmm, hmm, hmm."
    s "After all these years, this is where it's been, encased in a protective spell?"
    s "I can't just rip it out either..."
    s "...This is going to take time."
    s "Alas, keeping her alive for now is my only choice."
    s "Why did he ever offer something like this to a human?"
    #SCENE CHANGE - underwater cave (skylla's)
    scene bg underwater cave
    $ config.side_image_tag = "june"
    "..."
    "...Where am I?"
    s "Ah, you've awoken, little human. Or shall I say fish?"
    y neutral fish "Blub!"
    "....Huh."
    y "Blub blub blub!"
    "The strange voice laughs at me, and I recognize it."
    y "BLUB BLUB BLUB!!!"
    $ config.side_image_tag = "None"
    s "That's no way to speak as a lady!"
    "Try as I might, none of my words come out right."
    "I've been turned into a fish by the siren!?"
    menu:
        "Stay still.":
            $ cetus_points += 1
            $ prince_points -= 1
            "I don't want to risk angering her."
            "Best to stay still and hope for the best..."

        "Get her!":
            $ prince_points += 1
            $ cetus_points -= 1
            "I try to swim at her, but an invisible wall stops me before I can get close enough to smack her."
            "Near-invisible, I should say. The walls are shining."
            "A bubble?"

    s "None of that swimming off! Stay put here, dearie, and be good, yes?"
    s "You'll give me what I want in time."
    s "Now, where did I put that pestle?"
    "The voice swims away, and I'm left alone to contemplate my new fate."
    "Pushing my hands, well- fins against the bubble I can hardly push through!"
    "I'm trapped. There's no doubt about it."
    "Am I cursed to stay like this...forever?"
    "Am I going to die being eaten for some fish's dinner, same as the mermaids above?"
    "From the distance through the water I could hear the siren talking to herself, swimming to and fro around the cave."
    s "Extraction of a pearl...extraction..."
    "She comes back over to me, her sharp eyes are stunningly beautiful."
    "Yet I can't help but feel fear as she grabs the bubble, bringing me closer to her face, examining me with a ravenous intent."
    s "Do you humans still practice magic on land?"
    s "Do you even know what it is that you possess?"
    $ config.side_image_tag = "june"
    y "Bl-Blub?"
    $ config.side_image_tag = "None"
    s "No, you seem ignorant. Yet I know it's inside you. I can see it radiating off you."
    s "Faint and hidden, but it's there."
    "What do I possess? What could I even have? And magic practice? I'm not in a fairytale, am I!?"
    s "How did you convince him to give it to you? Bribery?"
    $ config.side_image_tag = "june"
    y "Blub?"
    $ config.side_image_tag = "None"
    "Surely this is a mistake of some sort."
    s "Let's just get started. We have a lot of trial and error ahead of us."
    "Her clawed fingers gracefully pop the bubble, but just as swiftly in that motion her hand clasps around me."
    "My heart was rushing in my tiny body. She could pop me in an instant as well."
    "She drew closer to whatever she was preparing to test on me in the back of the cave before she suddenly paused, listening closely to something as her ears twitched."
    #Voice Lines Start
    voice "audio/voice/prince/THIODAL-1.wav"
    up "The further out you swim, the more guilty that you are! Those fish belong to the vanguard."
    voice "audio/voice/prince/THIODAL-2.wav"
    up "Return them now, and I will not arrest you."
    s "That voice...he's not supposed to be here."
    "She squeezes me painfully in frustration."
    uj "Well, I'm sorry, my liege, but I'm sure you'll find something else out there to eat."
    uj "Perhaps you should ask your guards how they got these fish in the first place? It wasn't very kind or knightly."
    voice "audio/voice/prince/THIODAL-3.wav"
    up "Are you suggesting we stole from {i}you{/i}?"
    voice "audio/voice/prince/THIODAL-4.wav"
    up "If my men have done harm to your village and stolen from you, I will personally take accountability in returning those fish and providing recompense."
    voice "audio/voice/prince/THIODAL-5.wav"
    up "However, the fact of the matter is that you stole from the royal guard!"
    s "I need to chase them away..."
    s "Ah, how about this!"
    s "Heheheh~."
    "She waves out to the voices, whispering in a tongue I can't understand."
    "But her hand's grip slightly loosened, just enough for me to squirm out of her grasp."
    s "You little eel! Get back here!"
    "Quickly zipping across the room, I push my tiny fins as hard as they can go."
    "Her tentacles try to grasp me, but I am too small for them to catch."
    "And just through sheer luck, in front of me in the cave wall is a crack, just small enough for me to fit through!"
    "I can hear the siren cursing behind the wall as I swim away."

    #SCENE CHANGE - sea wilderness
    scene bg sea
    "It doesn't matter where I go, just far away from that witch!"
    "The hole happened to bring me straight in the thick of things outside the cave."
    show prince 4 at left, bob with dissolve
    show jorunn sweat at bob, moreright with dissolve
    guard "Sharks ahead! Get the prince out of here!"
    guard "We've been in the witch's domain for far too long, your Majesty! We must return, now!"
    uj "Sharks? Ah, we are in the witch's country, aren't we?"
    show jorunn glee at bob, moreright with vpunch
    uj "I'll be taking these home then! Goodbye!"
    voice "audio/voice/prince/THIODAL-6.wav"
    show prince 4 at left, bob with hpunch
    up "You damned, fish-grubbing parasite! Grah, fine!"
    "It seems like the two opposing parties are separating, and I need to figure out where to go, now!"
    "Maybe one of them can help me?"
    "Hiding between the broken shells of sea hunterships, I could see the sharks patrolling. Did the siren summon them?"
    "The merman that was surrounded by knights was called a prince, huh?"
    "He sure looked like one, his fins were unlike any other I've seen, a striking array of blue."
    "Do I approach him..? Or do I follow the other fellow? He seems like he might be more willing to help me, like some of the townsfolk I know back home."
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
    "With all the might I could muster I push my way through the current, leaving a trail of bubbles behind me."
    "It felt like riding  a bike downhill, without any brakes to stop me. I couldn't stop before crashing into the back of the striking merman's head."
    #SCREEN SHAKE
    $ config.side_image_tag = "None"
    voice "audio/voice/prince/THIODAL-7.wav"
    show prince 1 at bob, furthleft with hpunch
    up "!!!"
    voice "audio/voice/prince/THIODAL-8.wav"
    show prince 4 at bob with hpunch
    up "Who dares-"
    $ config.side_image_tag = "june"
    y "Please help me!!"
    $ config.side_image_tag = "None"
    show prince 5 
    voice "audio/voice/prince/THIODAL-9.wav"
    up "...?"
    guard "The fish drew their attention!"
    "The sharks hurl toward us in a frenzy, chomping at the water and whatever moves in front of it."
    "I swim as quickly as I can past the striking merman, hoping the sharks have caught my scent."
    "I know I've scraped something swimming out of the cave. It's a minor itch, but I can feel the blood seeping from my body as I propel through the water."
    "And if sharks are drawn to blood, it's only a matter of time before I'm done for!"
    "The princely fellow seemed to realize this, at least."
    show prince 4 at bob, furthleft with dissolve
    voice "audio/voice/prince/THIODAL-10.wav"
    up "You- lead it that way!"
    "Swimming toward where he directs, I swim right past him, watching in horror to see he stays in place!"
    "However, my worry is unwarranted."
    "He must have quickly brandished a weapon with great speed between the eyes of the great white, as a cloud of bubbles and a hole in its head are all I can see before it is over."
    "The shark sinks quickly to the ocean floor, pushing up the floor of the ocean, blood intermingling with the tide."
    "Surely this is more tantalizing than my pitiful injury."
    show prince 5 at bob, with dissolve
    voice "audio/voice/prince/THIODAL-11.wav"
    up "Let us away, before the others come."
    $ config.side_image_tag = "june"
    y "....R-Right!"
    "How fearsome his strength must be. He certainly doesn't seem the type."
    "The wave of adrenaline is starting to finally calm down, but I follow him diligently to a safer spot away from the cave and the sharks."
    voice "audio/voice/prince/THIODAL-12.wav"
    up "Stay still for a moment."
    show prince 4 with dissolve
    "His brow furrows as he draws closer to me, his hands hovering my sides, but not quite enclosing my body."
    "A faint glow surrounds me, the scales reforming over in moments."
    show prince 5 with dissolve
    "Almost instantly, I could feel my energy return. I suppose being so small, even a little bit of blood loss could make you quite weak."
    y "Was that healing magic? I've only heard of it in books."
    y "Ah, I should, no, wait, I forget myself."
    y "Thank you, sir."
    "Through some miracle, it seems he can understand me."
    voice "audio/voice/prince/THIODAL-13.wav"
    up "You speak strangely, but that's none of my concern. You're either extremely resilient, or a spy of that Sea Witch."
    y "I'm not a spy! I'm just a resilient type, as you say!"
    "I sincerely hope he believes me, as it's true."
    voice "audio/voice/prince/THIODAL-14.wav"
    up "...Let's just say that for now. Your wounds have been taken care of, so please, return to your reefs...safely."
    guard "Prince Thioran!! Are you injured?"
    voice "audio/voice/prince/THIODAL-15 v2.wav"
    p "Of course not."
    "His vanguard found us, relieved to see their charge unhurt."
    "However, the guards pointed their weapons at me."
    guard "Isn't it strange for that kind of fish to be at this depth of the ocean?"
    guard "Couldn't this one be a spy?"
    "No, surely they wouldn't just kill me for being strange!!"
    "The Prince thought for a moment, but mostly just looked exhausted and wanted to just end the day."
    voice "audio/voice/prince/THIODAL-16.wav"
    p "It is quite uncommon. Most of her kind wouldn't be able to withstand these depths."
    voice "audio/voice/prince/THIODAL-17.wav"
    p "However, if she was a spy, I doubt the sharks would have attacked her."
    "Yet his glances at me, do they feel familiar? It would be impossible for us to have met before today, yet I get the feeling we have, somehow."
    voice "audio/voice/prince/THIODAL-18.wav"
    p "I believe she was only swept up in our clash."
    voice "audio/voice/prince/THIODAL-19.wav"
    p "Regardless, there are other matters we must attend to, and we've already wasted enough time."
    "He turns to address me last."
    voice "audio/voice/prince/THIODAL-20.wav"
    p "So please, you are free to go. You have my permission."
    "I don't need his blessing- I just need whatever magic power he has to help me turn back to normal!"
    "Clearly he knows a trick or two, especially with those sharks."
    y "If it's alright, I would like to make a request. "
    y "Could you lead me back to...the kingdom? I...have business there."
    show prince 3 with dissolve
    "He stares at me for a few moments, with an indeterminable expression on his face."
    voice "audio/voice/prince/THIODAL-21.wav"
    show prince 5 with dissolve
    p "You may follow us. When we arrive, attend to your business. Any other troubles from then on must be your own."
    y "That's more than enough! Thank you!"
    "That is definitely not enough!!"
    "I must stay with him, if there is even a chance to find some answers to cure my fishy affliction!"
    "I follow the Prince and his guards across the sea, taking in the sights as I pass them."
    "I was behind the Knights that swam in a march, putting distance between me and the prince."
    "I suppose I'm no longer allowed to speak with him."
    "..."
    "Left alone with my thoughts, my mind races every which way."
    "Am I the first human to experience the sea like this?"
    "I wish I had my camera. But it wouldn't survive the plunge."
    "I hope it somehow escaped my fate."
    "Hunter must think the worst outcome for me, falling like I did."
    "Oh, Grandfather..!"
    "He would be devastated to find out I went overboard!"
    "They're going to think I drowned.."
    "I need to return back."
    scene bg sea
    "The waters seem to brighten more as we swim, peaks of coral and schools of beautiful fish."
    "We arrive at a place just before a city, where a mesmerizing merman waits for the prince."
    c "My lovely nephew! Where have you been?"
    c "I hear news of an attack, and you do not deign to tell me?"
    show prince 1 at right, bob with dissolve
    # show cetus at left with dissolve
    voice "audio/voice/prince/THIODAL-22.wav"
    p "Cetus. It has been a long day. You will have to forgive my impropriety."
    c "Always so stiff."
    c "I merely jest. I know no trouble would come of an attack on you."
    "The man called Cetus seems familiar as well. The more he speaks, the more I feel a sense that I have met him before."
    c "Oh? Who's this you have following you like a pet, Thio?"
    "His gaze catches on me, and I want nothing more than to dart behind a rock and hide from it."
    voice "audio/voice/prince/THIODAL-23.wav"
    p "I...did not ask for a name. She claims to have business here in the city. By formality, I allowed her to return with me."
    c "I see..."
    "Cetus stares at me for a moment before he starts chanting in a low tone. The prince does not pay it any heed."
    voice "audio/voice/prince/THIODAL-24.wav"
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

    show jorunn glee at moreleft with dissolve

    j "Hello there!"
    j "You've reached the end of the demo for Heart's Depth!"
    j "Thank you so much for playing! Follow our game page for updates when they come."
    j "We sincerely look forward to releasing the rest of the story." with vpunch
    j "Take care! And stay fishy!"

    play sound "audio/sfx_splash.flac"
    hide jorunn glee with dissolve

    #END OF DEMO!!!!!!!

    return

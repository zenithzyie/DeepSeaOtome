# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define y = Character("[player_name]", image="june")
define g = Character("Grandfather", image="june")
define h = Character("Hunter", image="june")
define s = Character("Skylla", image="june")
define c = Character("Cetus", image="june")
define p = Character("Prince Thioran", image="june")
define j = Character("Jorunn", image="june")
define t = Character("Townsperson", image="june")

define farleft = Position(xpos=0.25)
define moreleft = Position(xpos=0.35)
define center = Position(xpos=0.45)
define moreright = Position(xpos=0.60)
define farright = Position(xpos=0.70)
define prettyfarright = Position(xpos=0.85)

init python:
    config.side_image_tag = "june"

# The game starts here.

label start:

    # "NARRATION"

    # # If you want to hide the side image
    # $ config.side_image_tag = "None"

    # "This is a narration so the side image shouldn't appear."

    # # ""

    # #this above one makes a blank thing, good for comedic effect?

    # #NEED TO DO THIS EVERY TIME THERES NARRATION W/ NO MIN
    # # To unhide the side image
    # $ config.side_image_tag = "june"

    # m neutral "It's so cold"

    jump get_name

label get_name:
    scene bg black
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
        "No":
            jump get_name



#PROLOGUE
label prologue:
    #TODO SCENE ?
    scene bg sea

    $ config.side_image_tag = "june"
    y neutral "It was sunny only moments ago! What is this?"

    $ config.side_image_tag = "None"

    show prince 1 at moreright with dissolve

    show grandpa surprised at moreleft with dissolve

    h "Blasted...I've sailed us right into the sea witch's storm! Hold onto something, [y]!"
    "The ship creaks as he tries to turn it back towards the port, but the waves are unrelenting."
    "Something stirs in the back of my memory as I stare down into the waves below."
    "I can see something glowing through the wind and rain."

    #SCREEN SHAKE
    h "[y]!" with screenShake
    $ config.side_image_tag = "june"
    "I try to reach for it, forgetting myself for just a moment."

    #SFX - SPLASH
    play sound "audio/sfx_splash.flac"

    #SCENE CHANGE - (Underwater / Black)
    scene bg black
    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "I can feel myself fading...is this really the end for me?"

    jump chapter1

#CHAPTER 1
label chapter1:
    #TODO SCENE = CG (Train)
    scene bg shabby town

    $ config.side_image_tag = "june"
    "Salty air...I remember how I would try to stick out my tongue to taste it."
    "I was a child the last time I did something as silly as that."
    "Life was so carefree back then..."
    "I can't wait to see it again, but when I think about the ocean, I can't help feeling like I had broken a promise to it."
    "It has been 10 years since I've  last seen the ocean. Perhaps it was just because I missed Grandfather after being inland without contact for so long."

    "I only ever got to see my grandfather on special holidays in the summer."
    "I can't really remember why my mother stopped letting me see him. She said she had lost trust in him after some incident I had gone through as a child. Even now, she refuses to say what happened."
    "I would ask him, but I would rather just enjoy our time together in peace."

    $ config.side_image_tag = "None"
    t "Please gather all personal belongings, we are arriving at Aquantis station!"

    $ config.side_image_tag = "june"
    y neutral "Oh, we're already here?"

    "Getting up from my seat I gathered my bags from the overhead, taking my camera first."
    "From my car seat window, I let the shutter go off, clicking quickly of the people outside. The screeching of the brakes signalled the train to a stop."
    "The letter Grandfather sent me had his address, though it would be helpful to ask for some directions. The harbor city was huge. From where I stood I could see the entire city and the ocean in the distance."
    "It's been years since I last stepped foot here."
    "Homes and shops descended down the hill that lead to the ports, cramped with new and old parts of the city mixed together."

    y "Excuse me- sir! Hello?"

    "Trying to grab anyone's attention around here seems impossible! They all just ignore me. Were they so unfriendly to people from outside when I was younger? I couldn't remember."

    #SCENE CHANGE - (Shabbier part of Town)
    scene bg shabby town

    "The further I walked down from the top of the city, the more and more the atmosphere seemed to change. I could feel the eyes of  the people I passed by watching me."
    "It looked like these parts have fallen into harder times. When I was younger I remember it being more lively and nice, but now.. I feel as though I should keep my eyes away from the gaze of others."

    $ config.side_image_tag = "None"
    t "Tch, inlanders. What is someone like her out here for?"
    t "Inlander? Oy, you don't see many of them.. And she's got a fancy one of those picture devices, that could land us a nice bit of coin aye?"

    #TODO - SPRITE CHANGE (Annoyed Expression)
    $ config.side_image_tag = "june"
    "Were they referring to my camera? They were hardly being secretive about wanting to rob me!"
    "Slipping away from the men following behind me, I keep my camera close to my hip, hiding it with my coat to draw away any more notice. Was my grandfather truly living in such a hostile area?"

    #SCENE CHANGE - (Shabby Market [Zoomed In])
    scene bg shabby market
    "The smell grew worse as I suddenly found myself at a market, it was the smell of fish, salt, smoke and sewer. Though despite it, there seemed to be a few more normal townsfolk around."
    "I approached the friendliest-looking stand. A man stood there, hawking his catches."

    #TODO - SPRITE CHANGE (??? Expression)
    "A merchant would be far easier to talk to for directions! I just hope I'm not expected to buy the fish covered in flies."

    #SCENE CHANGE - Shabby Market (or CG [Merchant at Fish Stand])
    scene bg shabby market
    y "Good day to you sir. I'm sorry for disrupting you, but-"
    t "Bass or Tilapia?"
    y "Oh- er, well...I'm not looking to buy fish right now. Could you please help me with the directions to-"
    t "Does this look like a map stand? I sell fish, you buy fish, you leave- ye get it?"
    y "I will pay you for the help! I'm just looking for this address."

    "Before he could deny me once more, I showed the bottom half of the letter where the address was clearly written. He squints at the paper, adjusting his sight to get a better look at it"

    t "....Girlie, do ye know where that is? That address is in the Black Market District. Someone like you doesn't belong there. Hell, even I avoid it. It's not exactly a tourist destination."

    "Black Market District..?"
    y "Even so, I have to get there. I'll pay you if you just point me in the right direction."
    "He gave a sigh and pointed forwards to the end of the market square. There was an alleyway that seemed to lead to a wall."
    t "Take a left down that alley, give five knocks on the brick, pause, give three knocks, and pause again to give four.
        Someone will open the elevator for you to take ya where you need going. That's all I know, and all I'll say."
    "He looked at me and grinned toothily."
    t "Payment?"
    y "Oh, yes. Thank you so much for the help."
    "Leaving him a decent amount of coin, I followed his instructions down towards the alleyway."

    #SCENE CHANGE - Brick Wall
    scene bg brickwall
    y "Alright...Grandfather you could have at least explained better how to reach you..living in the Black Market District.. It makes sense considering his job."
    "Upon reaching the end, I made a left turn down to see a brick wall. It had an odd discolouration, and I knew this must be the wall the merchant spoke of."
    "Well."
    "I stared at the wall for a few moments. It was certainly not something I had planned to do on this trip."
    "I suppose I'll just have to give it a go."
    "..3..4..5..."
    "..1..2..3..."
    "..2..3..4..."
    "There was no response, but suddenly the wall was pulled back."
    "With cautionary steps, I pushed inside, seeing no one was there behind the door."

    #SCENE CHANGE - Black Screen
    scene bg black
    "It closed the moment I entered. It must have been an ancient elevator, rusted and old."

    #SFX -  Elevator
    play sound "audio/sfx_elevator.wav"
    "The rickety elevator descends down for a while. I start to regret stepping inside - who knows what I would find so far down? The prospect is terrifying..."
    #SFX -  Elevator
    play sound "audio/sfx_elevator2.wav"
    "Until it finally came to a stop, the door opened, and I was greeted with a new world."

    #SCENE CHANGE -  Underground Black Market Faire
    scene bg underground market
    "It was almost like a circus, or a fairground. Many tent booths were set up and had strange knick knacks begging to be looked at."
    "Exotic fruits, animals, books, and so many more things from what must have been lands long gone to the waves being sold here as rarities. My eyes followed every gleaming thing being displayed."

    y "This is incredible..."
    "As I walked around in awe, my eyes caught on a stand of tropical flowers arranged in a beautiful pattern."
    y "Mother would love to see this..."
    "My hand reached out for my camera."
    #NOTE Are we hiding name until he reveals himself?
    h "I wouldn't dare to take out that camera here, unless you're planning on joining the fish in the sea."
    "My heart sunk as I stood frozen, feeling a gloved hand on top of my own, stopping me."
    h "I knew I saw a familiar face in the crowd. I knew it was you, [y] Finch~."
    "I turned to see who the hell the man was behind me. How did he know my name? Slapping his hand off mine I glared at his face. He wore a mask on his face, but even so - I did not recognize his voice."
    h "It's a bit rude to slap a friend, isn't it?"
    y "Who are you, exactly?"
    "He scoffed and shook his head."

    #TODO SPRITE CHANGE - Hunter Disappointed Mask
    h "You don't remember your old playmate? I'm hurt! After all these years, I didn't once forget about you, [y]."
    y "I haven't been in this part of Aquantis before, so you must have mistaken me for someone else"
    h "Ha- this isn't your first time here. I don't appreciate being treated like a stranger."
    "Bending down to my level, the stranger looked me right in the eyes."
    h "Jogging anything in that noggin'? I've grown up a bit since you've last seen this mug..how about it?"
    "He stared at me for a moment before the realization hit."
    h "Ah, that's right. I still have the mask on."
    "With that, he swiftly removed his mask, and I was faced with someone I hadn't seen in a long time"
    #NOTE Is there a sprite for this ??
    y "...Hunter?"
    h "That's my name, yes"
    "He looked positively delighted to hear me say his name."
    h "You do remember me~! It's been only about, what... ten years since we've last seen each other? I never expected you to return here..."
    "Hunter..."
    "We used to play near the beach as kids. If there was anyone I'd recall besides my grandfather, it'd be Hunter."
    "We were fast friends, though I can't remember much of what we did. Back then, he was a strange, scrawny little kid."
    "But aside from that, I remember his smile when he was trying to show me shells or bugs he found on the beach."
    "As I looked at him now, it seemed like the only thing that remained was that smile."
    y "Yes- you've certainly gotten...taller. But I came to see my grandfather, if you still remember him."
    h "Ah~ family visit.. Of course I still remember the old man. His hunting company practically owns half the market strip. Though he went into retirement a few years ago."
    h "I'm assuming you need some help?"
    y "Well, yes..."
    h "I'll take you to him. Just keep that camera out of view."
    h "Stop gawking at things like you've never been here before...People might think you're a spy or somethin'."
    "He unclipped his cloak and threw it on top of my head. My nose was assaulted with the salty smell of the sea."

    #SCENE CHANGE - Black Screen
    scene bg black

    #SCREEN SHAKE
    y "Gah! Hey- don't just throw this dirty thing on me!" with screenShake
    h "Just keep it for now. Keep your eyes down so people can't clearly see your face...and to avoid seeing things you shouldn't be looking at anyways."
    y " Seeing things I shouldn't be..?"
    "What did he mean by that? Things I shouldn't see...I felt a pressing need to see them - but a far more pressing urge to stay alive"
    "I did as he asked, even if the cloak was starting to chafe on my shoulders and crush my hat."

    #SCENE CHANGE - Black Market
    scene bg underground market

    "He took my hand and gave a low hush, leading me through the crowds of masked men and women. I looked down at my feet, hearing the mumbling roar of chatter."

    #SFX - CROWD
    play sound "audio/sfx_crowd.wav" volume 0.2 loop

    "He walks meticulously, carefully weaving through the crowds of people, and I try my best to keep in step with his strides."
    "But then, I saw something tantalizingly curious out of the corner of my eye. Without thinking, I glanced up"

    #TODO SCENE = CG (Mermaid in Tank [Zoomed])
    scene bg underground market
    "There was a pale but beautiful face in the dark, behind glass."
    "The further along we walked, the more of her face was revealed.
        Her body was so human and serene from the top, but her lower half....scales, a tail that flowed in the water and reflected off the dim lights around her."
    "A creature that was equal parts human and fish."
    y "A mermaid?"

    #TODO SCENE = CG (Mermaid in Tank [Full])
    scene bg underground market
    "She was so beautiful."
    "Long silver hair that moved in the water just like her tail. She was mouthing something, banging on the glass. But not a word could be heard through it. Her eyes seemed to lock onto mine for a moment."
    "Was she asking for my help?"
    "Suddenly, my view of the rest of the stand was unblocked, and I was able to peek through the empty spot in the crowd. It was a fish hawker's stand."

    #TODO SCENE = CG (Mermaid cut in half)
    scene bg underground market
    "Her sign read 'Catch of the day'.
        Another mermaid, eerily similar to the face banging on the glass, was laying on a table in front of the tank.
        Except she was chopped off from the hip below, tail being taken by rabid customers, piece by piece."

    "As if she was just the catch of the day. Another fish for someone to eat for dinner."
    "I gripped Hunter's hand tighter, and he started to walk faster through the crowd."
    h "I said keep your eyes down, or people might see your face. Believe me, you don't want them remembering who you are."
    "I gave a regretful glance back before turning back away. It was the cruel reality of the world, but there wasn't much I could do about it..."

    menu:
        "Do you hunt now, too? Like your father?":
            h "Well.. yeah I do. It's the family business, though your family left it.
                Your old man always talked about wanting you to come back to join him..but when he announced his retirement, he sold some of those assets to my father."
        "Have you actually...killed them before?":
            h "Why do you sound so horrified? Fish is fish. If anything they're monsters using human faces. They don't deserve your pity"

    stop sound fadeout 2.0
    "Once we had made it outside the underground and I could see the sky again, the sun was on its way down. It seems like I'd been there for hours. My legs were aching to sit after being lost all day."

    #SCENE CHANGE - Port w/ Boats
    scene bg port
    "But what surprised me the most was we were actually at the portside now, the edge of the country..practically the edge of the world."
    "Boats were lined up, fishermen and hunters alike lining the dock, carrying supplies to and fro the ships."
    "They were much different than the ones I had remembered as a kid. These were large, made of steel, and produced steam."

    y "Does Grandpa live on one of these ships?"
    h "The only one not made of steel, that one over there."

    "Out on the furthest side of the docks was a large wooden ship. It stuck out compared to the rest, with its clothed sails, and ornate details.
        There was clearly a lot of pride and dedication to the maintenance of it"
    "Was his home always on a boat? It was too fuzzy to remember clearly. I had a faint recollection of a boat, but I thought I would remember more than that upon seeing his home."

    h "Well, keep moving along already. You know that only hunters and fishermen are the only one's really allowed at the docks. Come on."
    y "Hey, don't start shoving me- I appreciate the help, but you don't have to follow me the whole way there."
    h "I have business there already, running into you was just a coincidence. I have to prepare for my next voyage tomorrow anyway."
    y "Fine."

    #TODO SCENE CHANGE - Port w/ Boats (ZOOM)
    scene bg port
    "Stepping closer to the ship, my stomach was turning in knots. Ten years apart finally coming to an end. Perhaps my parents estranged us over a misunderstanding. I want to hear his side of it all."
    "Hunter knocks at the Captain's Quarters of the ship."
    "There was some loud grunting and muffled swearing as the door opened."
    show grandpa neutral at center with dissolve
    g "I told you people I don't want any-"
    show grandpa surprised
    "The old man stood frozen before me. He looked as though he had seen a ghost."
    y "Grandpa...?"
    show grandpa happy
    g "Oh bless the stars... you got my letter? You're really here! My dear, sweet [y]!"
    "Suddenly I was lunged into his embrace. He may have been older, but boy did he sure still had his strength."
    "I hugged him tight, not nearly as hard as he was, but over all the wave anxious anticipation just had  seemed to vanish for that moment."
    g "Oh, and I see the lad brought you here. Thank you my boy, get in here too!"
    h "Heh? That's not necessary-"
    "Grandpa practically grabbed the two of us both into a hug."
    "Once he had squeezed the daylight out of us, he let go."
    g "It's been years!! Oh just how many years have I've seen the both of ye's together.. How many years have it been since I've seen you. How's your mother? She never replies when I write to her.."
    show grandpa neutral
    g "Nor has she ever let you reply to the letters I've sent you over the years."
    "My heart sank."
    y "Mother has been well, as well as Father. But, well.."
    y "She read the letters, but never let me see them. I had only recently seen them myself. She let me keep the gifts you sent, but never the letters..."
    g "Marie..."
    "He let out a wistful sigh."
    g "What's done is done. Come on, then! Let's get you settled in."

    #SCENE CHANGE - Black Screen
    scene bg black
    "Time just flies by, and before I know it, it's been a week."

    #SCENE CHANGE - Shabby Market
    scene bg shabby market

    "Today, Grandfather and I shop for the next week's supply of food before he meets a trader in the afternoon."
    "Along with Hunter, who just happened to be free."
    y "...I don't know a thing about shopping for fish."
    h "It's easy enough. Just look at the colorin' and the smell."
    y "Color, I can do that. But I'd rather not have to smell them at all."
    g "There's been worse smells, little bug."
    g "When ye've been on a ship for three days 'n three nights with ten dead mermaids and they're startin' to curdle in the sun, that's when the smell's bad! Har har!"
    "I've learned some things from Grandpa in my time here."
    "He's quite proud of his history at sea with the mermaids"
    g "But I s'pose you'll never get to see that, would ye."
    "He also wishes I could've inherited his love for the hunt."
    y "Apologies, Grandfather..."
    g "Nah, it don't bother me, little bug. Don't worry about me, I know it ain't everyone's cup of tea."
    "Hunter taps Grandfather on the shoulder."
    h "Mr. Eaton, Merrill's open."
    "Grandfather pulls out his timepiece and flips it open."
    g "Ah, look at the time already. Can't keep Merrill waitin'. The ship won't pay for itself!"
    "Grandfather takes his leave. I can tell he's trying to be cheerful, but he still looks dejected."
    y "Grandfather..."
    "Out of habit, my hand finds my camera still sitting at my side, waiting, and I'm struck with a thought."
    y "Hunter."
    h "Hmmh?"
    y "I need your help"
    h "With what?"
    y "We're going to make Grandfather's day!"
    h "What, buy him mermaid nigiri for dinner?"
    y  "No! I'm going to take a picture of a live one."
    y "Imagine what people would pay for a picture!"
    h "I s'pose inlanders would think they'd be interestin'."
    #Hunter is down bad so he agrees

    #TODO SCENE CHANGE - Sea
    scene bg white
    #TODO SFX - waves (calm)

    #SCENE CHANGE - view of the sea (stormy)
    scene bg white
    y "It was sunny only moments ago! What is this?"
    h "Blasted...I've sailed us right into the sea witch's storm! Hold onto something, June!"
    "The ship creaks as he tries to turn it back towards the port, but it seems to make no progress at all."
    "The lurching nearly throws me to the floorboards, but I grab the mast just in time to stay upright"
    y "Ah..."
    #SCREENSHAKE
    "Something stirs in the back of my memory as I stare into the waves. Something is glowing through the wind and rain."  with screenShake

    #TODO FLASHBACK CG for a second of baby prince and june
    y "Who...? This is familiar to me, but...?"
    #TODO SFX - loud crash, screen shake
    #TODO SFX - choppy waves

    h " The waters are getting choppier, stay away from the ledge!"
    y "Well, obviously! I can hardly stand straight!"
    "He returns back to his position, eyes staying forward and ahead as the winds grow stronger."
    "I could hardly see out, but I couldn't give up my quest for a picture."
    "The sounds of the waves and the wind made Hunter's words a bit hard to hear."
    "I hold my camera up, making sure my hand was ready to press the trigger once I saw a mermaid."
    #SPRITE?
    s "Come...come with me..."
    y "What...?"
    s "O' ye of land to the queen of sea..."
    "My thoughts feel hazy, and my body feels as though I'm floating."
    h "June, what are you doing?!"
    s "Come to Skylla..."

    "The singing felt as though it was only for my ears to hear alone, the waves calling out to me to sink in."
    h "Shit, it's a siren! June!"
    "Hunter abandons his position at the helm of the ship and races towards me, but I can't imagine why."

    "An unimportant thought crosses my mind. I've heard of something like this before."
    "Sailors being sung to by the sea to only be met with death..."
    y "A siren's song." 
    "At the edge of the boat now, my eyes look down below for the cause of my affliction, But the darkness below the waves are  all I can see, and the voice all I could hear."
    "And with all my might I held tightly to the slippery ledge that parted me from the water, and yet my body went against my will to stay put."
    "I sit atop the ledge."
    "And just for a split moment I think I can hear Hunter calling my name before I take the plunge."

    #TODO SPLASH SFX
    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "The song stops, but my body is numb."
    "The regret floods my mind, but it's too late."
    "I can feel myself fading...is this really the end...?"

    #SCENE CHANGE - Black Screen
    scene bg black

    s "Hmm, hmm, hmm."
    s "After all these years, this is where it's been, encased in a protective spell? I can't just rip it out either.."
    s "...This is going to take time. Alas, keeping her alive for now is my only choice."
    s "Why did he ever offer something like this to a human..?"
    #SCENE CHANGE - underwater cave (skylla's)
    scene bg underwater cave
    $ config.side_image_tag = "june"
    "..."
    "...Where am I?"
    s "Ah, you've awoken, little human. Or shall I say fish?"
    y neutral "Blub!"
    "....Huh."
    y "Blub blub blub!"
    "The strange voice laughs at me, and I recognize it."
    y "BLUB BLUB BLUB!!!"
    $ config.side_image_tag = "None"
    s "That's no way to speak as a lady!"
    "Try as I might, none of my words come out right."
    "I've been turned into a fish by the siren!?"
    "I try to swim at her, but an invisible wall stops me before I can get close enough to smack her."
    "Near-invisible, I should say. The walls are shining."
    "A bubble?"
    s "None of that swimming off! Stay put here, dearie, and be good, yes? You'll give me what I want in time."
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
    s "Do you even know what it is that you possess? Do you humans still practice magic on land?"
    $ config.side_image_tag = "june"
    y "Bl-Blub?"
    $ config.side_image_tag = "None"
    s "No, you seem ignorant. Yet I know it's inside you. I can see it radiating off you, faintly hidden, but it's there."
    "What do I possess? What could I even have? And magic practice? I'm not in a fairytale, am I!?"
    s "How did you convince him to give it to you? Bribery?"
    $ config.side_image_tag = "june"
    y "Blub?"
    $ config.side_image_tag = "None"
    "What was she even talking about? I didn't steal anything. Surely this is a mistake."
    s "Let's just get started. We have a lot of trial and error to go through."
    "Her clawed fingers gracefully pop the bubble, but just as swiftly in that motion her hand clasps around me."
    "My heart was rushing in my tiny body. She could pop me in an instant as well."
    "She drew closer to whatever she was preparing to test on me in the back of the cave before she suddenly paused, listening closely to something as her ears twitched."
    p "The further out you swim, the more guilty that you are! Those fish belong to the Vanguard. Return them now, and I will not arrest you."
    s "That voice...he's not supposed to be here."
    "She squeezes me painfully in frustration."
    j "Well, I'm sorry, my liege, but I'm sure you'll find something else out there to eat."
    j "Perhaps you should ask your vanguard how they got these fish in the first place? It wasn't very kind or knightly."
    p "Are you suggesting we stole from {i}you{/i}?"
    p "If my men have done harm to your village and stole from you. I will personally take accountability and return those fish and then some to your village."
    p "However, the fact of the matter is that you stole from the royal guard!"
    s "I need to chase them away...ah, how about this..."
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
    t "Sharks ahead! Get the prince out of here!" 
    t "We've been in the witch's domain for far too long, your Majesty! We must return, now!"
    j "Sharks? Ah, we are in the witch's country, aren't we?"
    j "I'll be taking these home then! Goodbye!"
    p "You damned, fish-grubbing parasite! Grah, fine!"
    "It seems like the two opposing parties are separating, and I need to figure out where to go, now!"
    "Maybe one of them can help me?"
    "Hiding between the broken shells of sea hunterships, I could see the sharks patrolling. Did the siren summon them?"
    "The merman that was surrounded by knights was called a prince huh?"
    "He sure looked like one, his fins were unlike any other I've seen, a striking array of blue."
    "Do I approach him..? Or perhaps the other fellow? He seems like he might be more willing to help me, like some of the townsfolk I know back home."
    "Should I even be trusting any of them? Chasing mermaids is how I became stuck like this."
    "Either way, they're both starting to swim away"

    #Follow Striking Prince
    #Follow Relatable Boy (can't choose this yet, lol)
    menu:
        "Follow Striking Prince":
            jump ch1_followprince


label ch1_followprince:
    #BRANCH - FOLLOW PRINCE
    "Perhaps the prince would be kind to someone in need? I hope I'm not a species of fish they fight over for eating."
    "All I have to do is just wait for this shark to pass..."
    "3....2...1!!"
    $ config.side_image_tag = "june"
    y neutral "BLUBBB!!!!"
    "With all the might I could muster I push my way through the current, leaving a trail of bubbles behind me."
    "It felt like riding  a bike downhill, without any brakes to stop me. I couldn't stop before crashing into the back of the striking merman's head."
    #SCREEN SHAKE
    $ config.side_image_tag = "None"
    show prince 4 at center with dissolve
    p "!!!" with screenShake
    p "Who dares-"
    $ config.side_image_tag = "june"
    y "Please help me!!"
    $ config.side_image_tag = "None"
    show prince 5
    p "...?"
    t "The fish drew their attention!"
    "The sharks hurl toward us in a frenzy, chomping at the water and whatever moves in front of it."
    "I swim as quickly as I can past the striking merman, hoping the sharks have caught my scent."
    "I know I've scraped something swimming out of the cave. It's a minor itch, but I can feel the blood seeping from my body as I propel through the water."
    "And if sharks are drawn to blood, it's only a matter of time before I'm done for!"
    "The princely fellow seemed to realize this, at least."
    show prince 4
    p "You- lead it that way!"
    "Swimming toward where he directs, I swim right past him, watching in horror to see he stays in place!"
    "My worry is unwarranted."
    "He must have quickly brandished a weapon with great speed between the eyes of the great white, as a cloud of bubbles and a hole in its head are all I can see before it is over."
    "The shark sinks quickly to the ocean floor, pushing up the floor of the ocean, blood intermingling with the tide."
    "Surely this is more tantalizing than my pitiful injury."
    show prince 5
    p "Let us away, before the others come."
    $ config.side_image_tag = "june"
    y "....R-Right!"
    "How fearsome his strength must be. He certainly doesn't seem the type."
    "The wave of adrenaline is starting to finally calm down, but I follow him diligently to a safer spot away from the cave and the sharks."
    p "Stay still for a moment." 
    "His brow furrows as he draws closer to me, his hands hovering my sides, but not quite enclosing my body."
    "A faint glow surrounds me, the scales reforming over in moments."
    "Almost instantly, I could feel my energy return. I suppose being so small, even a little bit of blood loss could make you quite weak."
    y "Was that healing magic? I've only heard of it in books."
    y "Ah, I should, no, wait, I forget myself."
    y "Thank you, sir."
    "Through some miracle, it seems he can understand me."
    p "You speak strangely, but it's not as strange as to why you are here. You're either extremely resilient, or a spy of that Sea Witch."
    y "I'm not a spy! I'm just a resilient type, as you say!"
    "I sincerely hope he believes me, as it's true."
    p "...Yeah, for now let's just say that. Well, I helped you, so please return to your reefs now safely."
    t "My lord!! Are you injured?"
    p "Of course not."
    "His vanguard found us, relieved to see their charge unhurt."
    #SOMETHING ELSE HERE IDK IM TIRED
    t "Isn't it strange for that kind of fish to be at this depth of the ocean?"
    "The Prince gave a thought for expression, but mostly just looked exhausted and wanted to just end the day."
    "Yet his glances at me, do they feel familiar? It would be impossible for us to have met before today, yet I get the feeling we have, somehow."
    p "It is quite uncommon. Most of her kind couldn't withstand the depths of the sea. However, if she was a spy, I doubt the sharks would have attacked her."
    p "I believe she was only swept up in our clash."
    p "Regardless, there's other matters we must attend to, and we have wasted enough time already."
    "He turns to address me last."
    p "So please, you are free to go with. You have my permission."
    "I don't need his blessing- I just need whatever magic power he has to help me turn back to normal!"
    "Clearly he knows a trick or two, especially with those sharks."
    y "If it's alright, I would like to make a request. "
    y "Could you lead me back to...the kingdom? I...have business there."
    p "You may follow us. When we arrive, you may attend to your business. Any other troubles from then on must be your own."
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
    "The waters seem to brighten more as we swim, peaks of coral and schools of beautiful fish."
    "We arrive at a place just before a city, where a mesmerizing merman waits for the prince."
    c "My lovely nephew! Where have you been? I hear news of an attack, and you do not deign to tell me?"
    p "Cetus. It has been a long day. You will have to forgive my impropriety."
    c "Always so stiff. I merely jest. I know no trouble would come of an attack on you."
    "The man called Cetus seems familiar as well. The more he speaks, the more I feel a sense that I have met him before."
    c "Oh? Who's this you have following you like a pet, Thio?"
    "His gaze catches on me, and I want nothing more than to dart behind a rock and hide from it."
    p "I...did not ask for a name. They have business here in the city. By formality, I have allowed them to return with me."
    c "I see."
    "Cetus stares at me for a moment before he starts chanting in a low tone. The prince does not pay it any heed."
    p "I will return shortly to my duties, Uncle."
    "My body seizes, and I feel drawn towards Cetus."
    "My will is no longer mine, and I am no more than a mere fish lost in the sea."
    "It's just like how I felt when the siren dragged me under."
    "Suddenly, a burst of light breaks free from my body, and I feel my fins begin to change."

    #SHE TRANSFORMS WOOOO MERMAID JUNE
    p "Wtf?"
    c "Well, this certainly is something, isn't it?"

    #END OF DEMO!!!!!!!
    
    return

#Shake(position, duration, maximum distance)
init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
    #
    #Screenshake variable, to use in script
    $ screenShake = Shake((0, 0, 0, 0), 0.3, dist=20)
#

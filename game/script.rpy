# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define y = Character("[player_name]", image="june")
define g = Character("Grandpa", image="june")
define h = Character("Hunter", image="june")
define s = Character("Skylla", image="june")
define c = Character("Cetus", image="june")
define p = Character("Prince Thioran", image="june")
define t = Character("Townsperson", image="june")

# define m = Character("Min", image="june")
# define j = Character("Jane", image="june")
# define o = Character("October", image="june")

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

    # o "Vee speaking rn"

    # m "You've created a new Ren'Py game."

    # m "Once you add a story, pictures, and music, you can release it to the world!"

    # j "Wait what do you mean this is just a tutorial"

    # $ config.side_image_tag = "None"

    # "It was in fact a tutorial"

    # $ config.side_image_tag = "june"

    # m "Idk man we're just testing it ig"

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
    scene bg bedroom

    $ config.side_image_tag = "june"
    y neutral "It was sunny only moments ago! What is this?"

    $ config.side_image_tag = "None"

    show jane smile with dissolve

    h "Blasted...I've sailed us right into the sea witch's storm! Hold onto something, [y]!" #NOTE USE PLAYER NAME
    "The ship creaks as he tries to turn it back towards the port, but the waves are unrelenting."
    "Something stirs in the back of my memory as I stare down into the waves below."
    "I can see something glowing through the wind and rain."

    #TODO SCREEN SHAKE
    h "[y]!" #NOTE USE PLAYER NAME
    $ config.side_image_tag = "june"
    "I try to reach for it, forgetting myself for just a moment."

    #TODO SFX - SPLASH

    #TODO SCENE CHANGE - (Underwater / Black)
    scene bg black
    "The light of the surface is drifting further and further away. My body is sinking deeper, and the loud sounds from the surface are lost in the waves."
    "I can feel myself fading...is this really the end for me?"

    jump chapter1

#CHAPTER 1
label chapter1:
    #TODO SCENE = CG (Train)
    scene bg bedroom

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
    y "Oh, we're already here?"

    "Getting up from my seat I gathered my bags from the overhead, taking my camera first."
    "From my car seat window, I let the shutter go off, clicking quickly of the people outside. The screeching of the brakes signalled the train to a stop."
    "The letter Grandfather sent me had his address, though it would be helpful to ask for some directions. The harbor city was huge. From where I stood I could see the entire city and the ocean in the distance."
    "It's been years since I last stepped foot here."
    "Homes and shops descended down the hill that lead to the ports, cramped with new and old parts of the city mixed together."

    y "Excuse me- sir! Hello?"

    "Trying to grab anyone's attention around here seems impossible! They all just ignore me. Were they so unfriendly to people from outside when I was younger? I couldn't remember."

    #TODO SCENE CHANGE - (Shabbier part of Town)
    scene shabby town

    "The further I walked down from the top of the city, the more and more the atmosphere seemed to change. I could feel the eyes of  the people I passed by watching me."
    "It looked like these parts have fallen into harder times. When I was younger I remember it being more lively and nice, but now.. I feel as though I should keep my eyes away from the gaze of others."

    $ config.side_image_tag = "None"
    t "Tch, inlanders. What is someone like her out here for?"
    t "Inlander? Oy, you don't see many of them.. And she's got a fancy one of those picture devices, that could land us a nice bit of coin aye?"

    #TODO - SPRITE CHANGE (Annoyed Expression)
    $ config.side_image_tag = "june"
    "Were they referring to my camera? They were hardly being secretive about wanting to rob me!"
    "Slipping away from the men following behind me, I keep my camera close to my hip, hiding it with my coat to draw away any more notice. Was my grandfather truly living in such a hostile area?"

    #TODO SCENE CHANGE - (Shabby Market [Zoomed In])
    "The smell grew worse as I suddenly found myself at a market, it was the smell of fish, salt, smoke and sewer. Though despite it, there seemed to be a few more normal townsfolk around."
    "I approached the friendliest-looking stand. A man stood there, hawking his catches."

    #TODO - SPRITE CHANGE (??? Expression)
    "A merchant would be far easier to talk to for directions! I just hope I'm not expected to buy the fish covered in flies."

    #TODO SCENE = CG (Merchant at Fish Stand)
    #or SCENE CHANGE - Shabby Market
    scene shabby market
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

    #TODO SCENE CHANGE - Brick Wall
    scene bg bedroom
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

    #TODO SCENE CHANGE - Black Screen
    scene bg black
    "It closed the moment I entered. It must have been an ancient elevator, rusted and old."

    #TODO SFX -  Elevator
    "The rickety elevator descends down for a while. I start to regret stepping inside - who knows what I would find so far down? The prospect is terrifying..."
    #TODO SFX -  Elevator
    "Until it finally came to a stop, the door opened, and I was greeted with a new world."

    #TODO SCENE CHANGE -  Underground Black Market Faire
    scene bg bedroom
    "It was almost like a circus, or a fairground. Many tent booths were set up and had strange knick knacks begging to be looked at.
        Exotic fruits, animals, books, and so many more things from what must have been lands long gone to the waves being sold here as rarities. My eyes followed every gleaming thing being displayed."

    y "This is incredible..."
    "As I walked around in awe, my eyes caught on a stand of tropical flowers arranged in a beautiful pattern."
    y "Mother would love to see this..."
    "My hand reached out for my camera."
    #NOTE Are we hiding name until he reveals himself?
    h "I wouldn't dare to take out that camera here, unless you're planning on joining the fish in the sea."
    "My heart sunk as I stood frozen, feeling a gloved hand on top of my own, stopping me."
    h "I knew I saw a familiar face in the crowd. I knew it was you, [y] Finch~." #NOTE USE PLAYER NAME
    "I turned to see who the hell the man was behind me. How did he know my name? Slapping his hand off mine I glared at his face. He wore a mask on his face, but even so - I did not recognize his voice."
    h "It's a bit rude to slap a friend, isn't it?"
    y "Who are you, exactly?"
    "He scoffed and shook his head."

    #TODO SPRITE CHANGE - Hunter Disappointed Mask
    h "You don't remember your old playmate? I'm hurt! After all these years, I didn't once forget about you, [y]." #NOTE USE PLAYER NAME
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

    #TODO SCENE CHANGE - Black Screen
    scene bg black
    #TODO SCREEN SHAKE

    y "Gah! Hey- don't just throw this dirty thing on me!"
    h "Just keep it for now. Keep your eyes down so people can't clearly see your face...and to avoid seeing things you shouldn't be looking at anyways."
    y " Seeing things I shouldn't be..?"
    "What did he mean by that? Things I shouldn't see...I felt a pressing need to see them - but a far more pressing urge to stay alive"
    "I did as he asked, even if the cloak was starting to chafe on my shoulders and crush my hat."

    #TODO SCENE CHANGE - Black Market
    scene bg bedroom

    "He took my hand and gave a low hush, leading me through the crowds of masked men and women. I looked down at my feet, hearing the mumbling roar of chatter."

    #TODO SFX - CROWD

    "He walks meticulously, carefully weaving through the crowds of people, and I try my best to keep in step with his strides."
    "But then, I saw something tantalizingly curious out of the corner of my eye. Without thinking, I glanced up"

    #TODO SCENE = CG (Mermaid in Tank [Zoomed])
    scene bg bedroom
    "There was a pale but beautiful face in the dark, behind glass."
    "The further along we walked, the more of her face was revealed.
        Her body was so human and serene from the top, but her lower half....scales, a tail that flowed in the water and reflected off the dim lights around her."
    "A creature that was equal parts human and fish."
    y "A mermaid?"

    #TODO SCENE = CG (Mermaid in Tank [Full])
    scene bg bedroom
    "She was so beautiful."
    "Long silver hair that moved in the water just like her tail. She was mouthing something, banging on the glass. But not a word could be heard through it. Her eyes seemed to lock onto mine for a moment."
    "Was she asking for my help?"
    "Suddenly, my view of the rest of the stand was unblocked, and I was able to peek through the empty spot in the crowd. It was a fish hawker's stand."

    #TODO SCENE = CG (Mermaid cut in half)
    scene bg bedroom
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

    "Once we had made it outside the underground and I could see the sky again, the sun was on its way down. It seems like I'd been there for hours. My legs were aching to sit after being lost all day."

    #TODO SCENE CHANGE - Port w/ Boats
    scene bg bedroom
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
    scene port
    "Stepping closer to the ship, my stomach was turning in knots. Ten years apart finally coming to an end. Perhaps my parents estranged us over a misunderstanding. I want to hear his side of it all."
    "Hunter knocks at the Captain's Quarters of the ship."
    "There was some loud grunting and muffled swearing as the door opened."
    g "I told you people I don't want any-"
    "The old man stood frozen before me. He looked as though he had seen a ghost."
    y "Grandpa...?"
    g "Oh bless the stars... you got my letter? You're really here! My dear, sweet [y]!" #NOTE USE PLAYER NAME
    "Suddenly I was lunged into his embrace. He may have been older, but boy did he sure still had his strength."
    "I hugged him tight, not nearly as hard as he was, but over all the wave anxious anticipation just had  seemed to vanish for that moment."
    g "Oh, and I see the lad brought you here. Thank you my boy, get in here too!"
    h "Heh? That's not necessary-"
    "Grandpa practically grabbed the two of us both into a hug."
    "Once he had squeezed the daylight out of us, he let go."
    g "It's been years!! Oh just how many years have I've seen the both of ye's together.. How many years have it been since I've seen you. How's your mother? She never replies when I write to her.."
    g "Nor has she ever let you reply to the letters I've sent you over the years."
    "My heart sank."
    y "Mother has been well, as well as Father. But, well.."
    y "She read the letters, but never let me see them. I had only recently seen them myself. She let me keep the gifts you sent, but never the letters..."
    g "Marie..."
    "He let out a wistful sigh."
    g "What's done is done. Come on, then! Let's get you settled in."

    #END FOR NOW


    return

label ch3_office_temple:
##This is the beginning of the Cetus Office continuation, after June visits Cetus.

    $ merjune = True

    scene bg_cetusoffice1:
        fit "contain"
#    show test_firefly at firefly_blink
    show firefly_background_example at firefly_blink
    show firefly_midground_example
    show firefly_foreground_example
    with dissolve

    show cetus neutral at cetus_center:
        ypos 60
    with dissolve

    c mermaid neutral "There's a temple located a short distance away from the city. You can start your search there."

    c "Take my nephew with you. He will know the way."

    y mermaid nervous "Prince Thioran? He, er, doesn't seem to be very fond of me..."

    c "He's not fond of many mers these days."

    c "Still, he is the only one who knows about your involvement with the siren. I'd like it to remain that way."

    c "But I'll warn you to keep our little deal to yourself."

    c "If my nephew learns about your true nature, things will only become more troublesome."

    y "...I understand."

    c "Good."

    y "So...what kind of relic should I be searching for? What does it look like?"

    c "Who's to say? No two relics are the same."

    c "I trust you'll make the most of your judgment."

    #If you didn't break out on first try:
    if failescape > 0:
        c "...However simple it may be."
        y "..."
    #If you broke out first try:
    if failescape == 0:
        c "You're a clever one. I'm sure you will figure it out."

    "How am I meant to find something when I don't even know what it looks like?"

    "...but it's not like I have much of a choice, either."

    c "I'll send Prince Thioran to join you tomorrow. I suggest you get some rest until then."

    "Cetus dismisses me with a wave of his hand."

    y "I will, thank you."

    c "Oh, and [y]? Do try to use the door when you next leave your room."

    c "I'm afraid our windows won't survive another one of your daring escapades."

    y "Ha...haha..."

    "He's not going to let me forget that, is he?"

    #SCENE CHANGE - fade to black

    scene bg black with Dissolve(2.0)
    stop music fadeout 1.0

    "I return to my room to try to get some rest."

    "Sleep doesn't come as easily this time around."

    #play knock sfx
    play sound "audio/sfx_guestDoorKnock.ogg" volume 0.5

    "Just as I start to drift off, a knock at my door wakes me."

    #SCENE CHANGE - CASTLE ROOM

    scene bg palace guestroom:
        fit "contain"
    with dissolve
    $ speaking_char = "Thioran"

    y mermaid shocked "...Just a moment!"

    ny neutral "I swim over to open the door."

    show thioran frown at thioran_center with dissolve

    y mermaid happy "Oh! Good morning, Prince Thioran."

    play music "audio/music/13 Beatiful Reflections.ogg" fadein 1.0 volume 0.8

    p "..."

    ny neutral "The prince looks as though he'd rather be anywhere else..."

    y "I'll be in your care today."

    p "...I told you that I'd be keeping an eye on you. If you try to pull any of your tricks today, I'll know."

    y "I won't cause any trouble, I promise you."

    p "Hmph. Follow me."

    #SCENE CHANGE - UNDERWATER WILDERNESS

    scene bg sea:
        fit "contain"
    with fade
    show thioran frown at thioran_center with dissolve
    $ speaking_char = "Thioran"

    ny mermaid nervous "He leads me out of the city, keeping a quick and determined pace."

#    ny mermaid neutral "..."
#    "..."
#    ny nervous "..."

    "The silence between us is tense and uneasy."

    menu:
        "Is there anything I could say to break the ice?"
        "\"I've never stayed in the capital before.\"":
            y happy "My room is very nice."
            p "You're not visiting for some leisure trip,{i} [y] Finch{/i}. You'd do well to remember that."
            y flustered "Yes, of course. I know..."
            ny nervous "He doesn't have to say my name like it's some kind of curse!"

        "\"Did you sleep well?\"":
            p "..."
            y "Haha...Right, I'm sure you did."
            "I should probably stop talking. He could freeze the ocean over with that glare..."

        "\"...\"":
            "I'd better not. He doesn't really look like he wants to talk."

    "We continue to swim along without a word."

    "Eventually, we arrive at an old building."

    y "Oh, is this it?"

    p "Yes."

    "It reminds me of the drawings of ancient mausoleums in my father's books."

    y "Thank you for guiding me here."

    p "Save your thanks for the King Regent. I am only here to escort you by his will."

    #(tiny text)
    p "{size=*0.8}...Though I doubt we'll find any trace of the siren this close to the city.{/size}"

    "Traces of the siren? So that's what Cetus told him we're looking for..."

    "I hope I can keep up this act while looking for the relic."

    y "Well, I'm sure Lord Cetus has his reasons!"

    "Prince Thioran scoffs and moves toward the door."

    play sound "audio/sfx_heavyDoorClose.ogg" fadeout 2.0 volume 0.5

    "It opens slowly, like it's been sealed shut for a long time, and I follow him inside."

    #SCENE CHANGE - TEMPLE INTERIOR

    scene bg temple:
        fit "contain"
    with dissolve

    y mermaid shocked "Oh, wow...How beautiful."

    ny neutral "This place must have been rather important, once. {w=0.2}But now, all I can feel is a strange and inexplicable sadness."
    "We must be the first visitors in a long time."

    ny nervous "I wish I could take a picture, but I'd better not take my camera out in front of the prince."

    show thioran frown at thioran_center with dissolve
    $ speaking_char = "Thioran"

    p "...Let us get this over with. Don't stray too far."

    y neutral "Right."

    "Let's see... Cetus did tell me the relic could be anything."

label statuepuzzlestart:
    menu:
        ny neutral "[ lookaroundtemple ]"
    #After the first choice "Where should I look next?"
################################################################################################################################################################
        "Study the murals.":
            if mural:
                "Murals are cool!!!!!"
                jump statuepuzzlestart

            else:
                $ mural = True
                $ lookaroundtemplenumber += 1
                if lookaroundtemplenumber >= 1:
                    $ lookaroundtemple = "Where should I look next?"

                "Elaborate murals are all over the temple walls. It looks like they're telling some kind of story."
                y "I wonder what these could be about?"
                p "Can you not tell? They're meant to depict the founding story of Maris Lumina."
                "Maris Lumina? That's the name of the city isn't it? I remember Cetus mentioning it before."
                "I don't think he mentioned anything about the founding story, though..."

            #(Mural) Choice:
                menu:
                    "What should I say?"
                    "Pretend you know what he's talking about.":
                        y "Oh right. Haha, of course. The founding story."
                        "I quickly glance at the walls."
                        y "The one where the...pink...starfish conquered the blue jellyfish land."
                        p "Enough. This isn't the time for your japery."
                        y nervous "..."
                        p"..."
                        p "Are you acting like this because you truly do not know?"
                        y "I'm sorry. I'm from...really far away. I haven't heard about it before."

                    "Just be honest.":
                        y "I'm sorry, I'm afraid I'm not familiar."
                        p "Enough of that."
                        y nervous "..."
                        p "..."
                        p "...You're serious? You truly do not know?"
                        y "I'm from...really far away.  I haven't heard about it before."

                p "Still, how can that be possible?"
                p "Perhaps the encounter with the siren has scrambled your memories."

                p "...Pay attention then. I'll explain it just this once."

                #Show mural CG 1
                p "They say that a very time ago, before life as we know it today, the sea was shrouded in complete darkness."
                p "It was an era where all were ruled by the Great Ones, higher beings that could bend reality to their will."

                #Show mural CG 2
                p "Merkind struggled. Their longing and hope for better days gave life to a being named Lumina."
                p "Lumina was made of light itself, the first to ever exist in the world."
                p "She rallied mers together, to fight against the Great Ones and break away from their rule."

                #Show mural CG 3
                p "Among those who joined her was one named Maris."
                p "They say she was frail but clever, and once snuck close to the Great Ones to observe them."
                p "It was there she learned the secrets of magic, which she brought back with her to teach to those of her village."

                #Show mural CG 4
                p "Together they fought against the Great Ones and won."
                p "But Maris had been struck a fatal blow through the chest, and died."
                p "Lumina was then crowned the first king of all merkind, and Maris's students helped her build the city we know today."

                y "Wow...that's incredible. I had no idea there was a story like that."

                menu:
                    "Could anyone learn magic like Maris did?":
                        #(+1 Cetus)
                        $ cetus_points += 1
                        p "No. Magic died out ages ago. Only a few remain who still practice it, but that."
                        y "I see..."
                        y "Well that's unfortunate."

                    "Is Lumina your ancestor?":
                        #(+1 Thio)
                        $ prince_points += 1
                        p "Yes. It is the duty of her descendants to be the guiding light of the sea."
                        y "A guiding light..."
                        y "That's big shoes to fill.."
                        p "Shoes?"
                        y "ermm its just a saying from my town haha."

                "Everyone up on land would never believe mermaids have a kind of history like this."

                #If Festival Asked is True:
                if askedaboutfestival:
                    p "Yesterday, you had asked if there was a festival coming up."
                    p "I had thought you were mocking me at the time...but yes, it is one to celebrate our founding day."
                    y "So that's what it was?"

                #If Festival Asked is False:
                else:
                    p "It'd do you well to remember it this time. The coming festival is a celebration of our founding day."
                    y shocked "I see."

                y veryhappy "Thank you for explaining it to me, Prince Thioran!"

                p "..."
                jump statuepuzzlestart
################################################################################################################################################################
        "Investigate the statue.":
            $ lookaroundtemplenumber += 1
            if lookaroundtemplenumber >= 1:
                $ lookaroundtemple = "Where should I look next?"

        #If murals is False:
            if mural == False:
                "There's a statue of a beautiful mermaid at the end of the temple. She's looking upwards, as though searching for something out of reach."

        #If murals is True:
            if (mural == True and muralstatuedialogue == False):
                y "This must be Maris! I wonder if there's a statue of Lumina around here too?"
                p "Lumina's statue was built to be in the heart of the city. You won't find it here."
                y "Oh...Is that so?"
                "Come to think of it, I do remember seeing a statue in the city. It was much bigger than this though."
                "I wonder why they didn't build them next to each other? Is it because only Lumina became the king?"
                "Still...It's a bit sad to see that they're separated."
                #makes this only play once if player comes back to it
                $ muralstatuedialogue = True

            #(Statue) Choice:
            menu:
                "I wonder..."
                "Inspect it further.":
            #If no keystone + no mural:
                    if (keystone == False and mural == False and nokeystoneattempt1 == False):
                        "Maybe the relic is hidden somewhere on the statue?"
                        y "Hello? Miss Statue?"
                        "I try knocking on the statue. There's no response from it, but..."
                        p "What are you doing?"
                        y "Oh, nothing! Haha... Just paying my respects."
                        p "By trying to break her? Cease that immediately."
                        "Okay, so that didn't work. Maybe I should go look around some more."
                        #makes this only play once if player comes back to it
                        $ nokeystoneattempt1 = True
                        jump statuepuzzlestart

            #If no keystone + no mural, tried this already:
                    if (keystone == False and mural == False and nokeystoneattempt1 == True):
                        "I still don't know what to do here. Maybe I should go look around some more."
                        jump statuepuzzlestart

            #If no keystone + mural:
                    if (keystone == False and mural == True and nokeystoneattempt2 == False):
                        "Maybe the relic is hidden somewhere on the statue?"
                        "Prince Thioran did say that Maris was struck through the chest. It'd make sense if the relic was hidden in her heart, right?"
                        "I pat down the statue."
                        "There's no response from it, but..."
                        p "What are you doing? Why are you caressing the statue?"
                        y "{i}Huh?{/i}" with screenShake
                        y "Oh no! I was just...just, dusting her off!"
                        p "..."
                        "The prince looks rather perturbed."
                        "I must be missing something. I should go look around some more."
                        #makes this only play once if player comes back to it
                        $ nokeystoneattempt2 = True
                        jump statuepuzzlestart

            #If no keystone + mural, tried this already:
                    if (keystone == False and mural == True and nokeystoneattempt2 == True):
                        p "..."
                        "If I keep poking around Maris's statue without a plan, Prince Thioran will probably start getting suspicious."
                        "I should keep looking..."
                        jump statuepuzzlestart

            #If keystone is True:
                    if keystone == True:
                        "Maybe I could do something with this gem I found?"
            #(Keystone) Choice:
                        menu:
                            "Use the stone on the statue..."

                            "In her eye.":
                                "I hold the stone up and press it against her eye."
                                "..."
                                "It kind of looks like she's wearing an eyepatch."
                                "As pretty as her eyes may have been, I don't think this would quite fit."
                                jump statuepuzzlestart

                            "In her hand.":
                                "I place it in the palm of her outstretched hand."
                                "Won't you accept this, miss?"
                                "Nothing happens."
                                "Hmm. That's not right."
                                jump statuepuzzlestart

            #If murals is True:
                            "In her chest." if mural:
                                "There's a small divot in the statue's chest."
                                "I carefully place the stone inside."
                                jump statuepuzzlefinished

                "Return":
                    "I think I'll look at this later..."
                    jump statuepuzzlestart
################################################################################################################################################################
        "Examine the plants.":
            $ lookaroundtemplenumber += 1
            if lookaroundtemplenumber >= 1:
                $ lookaroundtemple = "Where should I look next?"

            if not lookedatplants:
                "This place really feels unattended. There's vegetation everywhere."
                y "Excuse me, Prince Thioran?"
                p "..."
                "Though he doesn't say anything, he turns to acknowledge me."
                y "Why would such an important place be abandoned?"
                p "This temple used to be part of the festival celebrations, but that practice has long since faded away."
                p "Since then, there's been no need to tend to this place any longer."
                y "That's a shame. It's a beautiful place."
                p "It is..."
                "He gives me a funny look but says nothing else as he turns away."
                "Despite the plants having taken up residence here, the building itself seems to be intact."
                "Oh?"
                $ lookedatplants = True

            #(Plants) Choice:
            menu:
                "Those plants over there look different somehow."
                "Check it out.":
                    $keystone = True
                    "I swim closer to get a better look. This plant is blooming with dozens of pale blue flowers."
                    "I reach out to touch one and notice something nestled beneath all the foliage."
                    "It feels warm to the touch."
                    "I feel oddly drawn to it."
                    "Could this be the relic?"
                    "But why didn't Cetus just get it himself? Maybe there's more to it...{w}I'd better keep looking for now."
                    p "Did you find something?"
                    p "What is that?"
                    y "I think I found some kind of stone."
                    "The prince does not look very impressed."
                    p "This is an old temple. There are many stones here."
                    y "Well...that's true."
                    "Still, it can't hurt to hold onto it."
                    jump statuepuzzlestart

                "Stay here.":
                    "Let me go look at the other things first."
                    "I'll come back to this later."
                    jump statuepuzzlestart

    #When June finishes the puzzle:
label statuepuzzlefinished:
    "The stone fits perfectly."
    "The stone starts glowing, emitting a bright blue light."
    y "Oh!"
    #show prince angry
    p "What are you doing? You can't mess around with magic stuff, it's dangerous."


    jump endofdemo

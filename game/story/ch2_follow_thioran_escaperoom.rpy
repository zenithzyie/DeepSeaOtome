
label ch2_castle_escaperoom:

# to see room at full/proper zooms
#            show bg palace guestroom:
#                subpixel True zoom 0.34

    menu escapebegin:
        ny neutral "What should I do?"
        "Examine the window.":

            show bg palace guestroom:  #zoom in window
                subpixel True
                xpos 0 zoom 1.0
                linear 1.17 xpos -630 ypos -100 zoom 1.49
            with Pause(1.27)
            show bg palace guestroom:
                xpos -630 ypos -100 zoom 1.49

            if not lookedatwindow:
                $ lookedatwindow = True
                "It’s difficult to see through the stained glass. Does it lead outside of the castle?"
                "The window is missing a handle, but there’s a small gap between the glass and the wall."
                "If I had something thin like a letter opener, maybe I could pry it open."
            if lookedatwindow:
                pass

            menu:
                ny neutral "Should I try to open it?"
                "Try to open it.":
                    if hairpin:
                        "The hairpin slips easily into the small gap."
                        "After a fair bit of moving it around, I hear a faint click."
                        play sound "audio/sfx_windowClick.ogg" volume 0.6
                        queue sound "audio/sfx_windowSlideOpen.ogg" volume 0.6
                        ny happy "The window slides open. There’s just enough room for me to swim through."
                        ny veryhappy "Now I just need to find Cetus!"
                        jump escapedroom_tohallway
                    if not hairpin:
                        if punchwindow:
                            "I already tried that. I need something to help me open this window…"
                            jump escapebegin
                        $ failescape += 1
                        $ punchwindow = True
                        play sound "audio/sfx_fistAgainstWindow.ogg"
                        "I lean against the window and push with all my might."
                        "The window doesn’t even budge."
                        ny frustrated "In a surge of desperation, I slam a fist against the glass." with vpunch
                        y shocked "Ouch!"
                        guard "Everything alright in there?"
                        y "Everything’s fine!"
                        ny sad "My hand is rather sore though…"
                        "Sir Guard would probably stop me if I tried to do that again."
                        "I should find a quieter way to open the window."
                        jump escapebegin
                "Not yet...":
                    "I shouldn’t be too reckless. I only have one chance at escaping."
                    show bg palace guestroom: #zoom out window
                        subpixel True
                        pos (-630, -100) zoom 1.49
                        linear 1.17 pos (0, 0) zoom 1.0
                    with Pause(1.27)
                    show bg palace guestroom:
                        pos (0, 0) zoom 1.0
                    jump escapebegin

        "Search the room.":
            window auto hide
            camera:
                subpixel True
                linear 1.0 pos (-50 , -125) zoom 1.35
                linear 1.5 pos (-420 , -125) zoom 1.35
            with Pause(2.5)
            camera:
                pos (-420 , -125) zoom 1.35
            window auto show
            camera:
                subpixel True
                pos (-420 , -125) zoom 1.35
                linear 0.5 pos (0,0) zoom 1.0
            with Pause(0.5)
            camera:
                pos (0,0) zoom 1.0
            menu searchroom:
                ny neutral "Hmm..."
                "Check the mirror.":
                    camera: #zoom in mirror
                        subpixel True
                        xpos 0 zoom 1.0
                        linear 0.88 pos (-800,-550) zoom 2.5
                    with Pause(0.88)
                    camera:
                        pos (-800,-550) zoom 2.5

                    if promermaid > antimermaid:
                        ny shocked "Wow, I look so different!"
                        "The colors and fabrics are pretty, but I miss my coat a bit as well."
                        ny flustered "Without it, I feel a little exposed…"
                        camera: #zoom out mirror
                            subpixel True
                            pos (-800,-550) zoom 2.5 zoom 2.5
                            linear 0.88 pos (0, 0) zoom 1.0
                        with Pause(0.88)
                        camera:
                            pos (0, 0) zoom 1.0
                        jump searchroom

                    if antimermaid > promermaid:
                        ny shocked "I… hardly recognize myself."
                        ny sad "I doubt Hunter or Grandfather would either."
                        camera: #zoom out mirror
                            subpixel True
                            pos (-800,-550) zoom 2.5 zoom 2.5
                            linear 0.88 pos (0, 0) zoom 1.0
                        with Pause(0.88)
                        camera:
                            pos (0, 0) zoom 1.0
                        jump searchroom

                "Check the dresser.":
                    show bg palace guestroom: #zoom in dresser
                        subpixel True
                        xpos 0 zoom 1.0
                        linear 0.97 pos (-1680,-770) zoom 2.35
                    with Pause(0.97)
                    show bg palace guestroom:
                        pos (-1680,-770) zoom 2.35
                    "I open the dresser."
                    if coinpurse and hairpin:
                        "It seems like I've searched through everything here."
                        show bg palace guestroom: #zoom out dresser
                            subpixel True
                            pos (-1680,-770) zoom 2.35
                            linear 0.97 pos (0, 0) zoom 1.0
                        with Pause(0.97)
                        show bg palace guestroom:
                            pos (0, 0) zoom 1.0
                        jump escapebegin
                    menu checkdresser:
                        set menuset
                        "Let's see..."
                        "Letter.":
                            $ letter = True
                            show black:
                                alpha 0.5
                            play sound "audio/sfx_thickPaperRustle.ogg" volume 0.8
                            show text "{i}My Dearest Lord Cetus.{/i}{w}":
                                align (0.5,0.5)
                            with dissolve
                            pause
                            show text "{i}Ever since I glimpsed your elegant complexion at the festival last year,{p}{w}my head has been filled with nothing but thoughts of you.{p}{w}{/i}":
                                align (0.5,0.5)
                            with dissolve
                            pause
                            show text "{i}You shine even brighter than the late king himself.{/i}{w}":
                                align (0.5,0.5)
                            with dissolve
                            pause
                            show text "{i}Your graceful poise, your slender hands, your tender tentacles...{p}{w}It is enough to drive a lady to madness.{/i}{w}":
                                align (0.5,0.5)
                            with dissolve
                            pause
                            hide text
                            hide black
                            with dissolve
                            ny neutral "{i}If you would allow me the opportunity, I could show you where to put all of those tentacles of yours-{/i}"
                            y flustered "Oh!"
                            "The rest of the letter is filled with the fantasies of a young noble woman."
                            play sound "audio/sfx_stoneDrawerClose.ogg" volume 0.8
                            y "I think I’ll leave this here…"
                            jump checkdresser

                        "Hairpin.":
                            $ hairpin = True
                            ny neutral "There’s what appears to be an ornate hairpin resting inside the dresser."
                            y happy "How beautiful. Did it belong to the last person who stayed here?"
                            ny neutral "The pointy end is rather thin. Maybe I can use this for something?"
                            "I'll keep it in my bag for now."
                            jump checkdresser

                        "Small bag.":
                            $ coinpurse = True
                            "I spy a small bag tucked in the back of the drawer."
                            play sound "audio/sfx_coinJingle.ogg"
                            "There’s some gold and silver shells inside. This looks like somebody’s coinpurse."
                            "Do mermaids barter the same way humans do?"
                            "I'll hold onto this for now."
                            ny shocked "I hope the previous guest doesn’t come looking for it…"
                            jump checkdresser

                        "Return." if coinpurse and hairpin:
                            ny neutral"It seems like I've searched through everything here."
                            show bg palace guestroom: #zoom out dresser
                                subpixel True
                                pos (-1680,-770) zoom 2.35
                                linear 0.97 xpos 0 ypos 0 zoom 1.0
                            with Pause(0.97)
                            show bg palace guestroom:
                                pos (0, 0) zoom 1.0
                            jump escapebegin
                "Return.":
                    jump escapebegin

        "Talk to the guard.":
            if bribeguard:
                ny nervous "Er... I really shouldn’t."
                "I think I’ve bothered him enough."

                jump escapebegin
            else:
                if coinpurse:
                    play sound "audio/sfx_coinJingle.ogg"
                    "The coinpurse jingles faintly in my bag."
                    "That fishmonger in Aquantis wasn’t too helpful either until I offered him money."
                    ny frustrated "I have to try everything I can here. It’s the only way to get home."
                    menu:
                        "Bribe the guard.":
                            $ bribeguard = True
                            $ failescape += 1
                            play sound "audio/sfx_guestDoorKnock.ogg"
                            "I knock on the door."
                            y neutral "Excuse me. Sir Guard?"
                            guard "What is it now?"
                            y "Could you please take me to Lord Cetus? I can pay you."
                            play sound "audio/sfx_longerCoinJingle.ogg"
                            ny happy "I jingle the coinpurse in hopes of getting his attention."
                            guard "So desperate as to resort to bribery?"
                            guard "Try that again and your new room might become the castle dungeons."
                            y flustered "S-sorry to bother you!" with vpunch
                            "I swim away from the door."
                            ny sad "That didn’t go as well as I’d hoped."
                            jump escapebegin
                        "Don’t bother.":
                            "This won’t get me anywhere."
                            "I should take a closer look around the room."
                            jump escapebegin

                else:
                    play sound "audio/sfx_guestDoorKnock.ogg"
                    "I knock on the door."
                    y "Excuse me. Sir Guard?"
                    guard "Take some time to rest. Someone will come fetch you when you’re needed."
                    ny frustrated "I’ve already rested plenty!"
                    ny neutral "I guess I'll take a closer look around the room."
                    jump escapebegin


label escapedroom_tohallway:
    scene bg palace hallway:
        fit "contain"
    with fade
    ny mermaid neutral "I find myself in another hallway."
    ny shocked "Huh. I suppose this is better than having to find my way back inside the castle."

    "That guard’s probably just around the corner. I don’t think he’s moved all day."
    "He said that Cetus was in his study."
    ny neutral "I need to find him before Sir Guard realizes I’m gone."
    "But… I have no idea where to start."

    "{i}After several turns, we pass by a hallway with a particularly elegant door.{/i}"
    "{i}It looks like it could lead to someplace quiet, like a library or an office.{/i}"

    "Well, it’s not like I have any other ideas."
    "The way to get back there is very clear in my mind."
    y frustrated "I will {i}not{\i} get lost again."

    ny neutral "..."
    y "...and hang another left here..."
    "..."
    ny shocked "Oh! There’s the decorations the servants were hanging up!"
    ny happy "The door is right here, just like I thought."

    y "..."
    "Here goes nothing..."
    play sound "audio/sfx_guestDoorKnock.ogg"
    "..."
    "..."
    "..."
    ny nervous "There's no response."
    "There’s no guarantee he’ll actually be here, but let’s give it a shot."
    "Taking a deep breath, I open the door."
    call cetus_office

label cetus_office:
    scene bg cetus study:
        fit "contain"
    with dissolve
    "Unlike the rest of the castle, this room is dimly lit."
    show cetus neutral at cetus_center:
        ypos 60
    with dissolve
    y mermaid shocked "Lord Cetus?"
    "Cetus is here! It looks like he’s busy writing something at his desk."
    c " Close the door behind you. It can get rather noisy out there."
    c "Though I’m sure you’ve already seen that firsthand."
    "...At least he’s not sending me away."
    y neutral "I need to speak with you."
    "Cetus pauses a moment before finally putting his work down."
    c "Yes. Quite urgently too, it seems, seeing as you’ve broken out of your room to come all the way here."

    y "I wanted to ask-"
    c "No, not from there."
    y "Pardon?"
    c nervous "Come closer."
    "Cetus beckons me forward with a wave of his hand."
    "I swim cautiously towards his desk."

#    camera:
#        subpixel True
#        xpos 0 zoom 1.0
#        ease 1.00 xpos -192 ypos -60 zoom 1.30
#    with Pause(1.25)
#    camera:
#        xpos -192 ypos -60 zoom 1.30
#
    c "Now then, how did you make it past the guard?"

    menu cetus_ask:
        "\"I was able to slip away.\"":
            "If you break free on the first try +2 cetus (?)"
            c "Clever girl."
            "Somehow, his praise only makes me feel more nervous."
            "Shouldn’t he be upset instead?"

            "If it takes you multiple attempts to break out"
            c "Though not without causing a commotion, I hear."
            "How did he know about that?"
            "If you picked option 2 first"
            show cetus smirk
            c "That wasn’t so bad, was it?"

        "\"I wanted to ask you something.\"":
            #removed after you pick it first
            c "Well now, was this {i}your{/i} office I barged into?"
            c "In that case, there’s plenty of paperwork that needs your attention, {i}my lady.{/i}"
            c "Perhaps I should take my leave before you call the guards to lock me away."
            y "Please don’t call the guards!"
            c "Oh? What was that?"

            jump cetus_ask

    y "Lord Cetus, are you aware of what I really am?"
    c "You are a very long way from your shore, human."
    "...!"
    y "Earlier in the throne room, you acted as if you didn’t know."
    c "And you did as well, did you not? A prudent choice."

    c "Some things are better left unsaid. Particularly in…unfriendly company."
    c "Merfolk are not very fond of your kind."
    y "..."
    "I think of the mermaid in the market again, and shudder."
    "I can only imagine what Prince Thioran would have done."
    c "Yet here you still are, unharmed."

    "He looks at me with interest."
    "Cetus has every reason to threaten me."
    "But it also seems like he’s giving me room to speak."
    "I need to take this chance."

    y "Lord Cetus, how can I become human again?"
    c "Ah, but what use would a human be in the search for a sea witch?"
    c "Allow me to remind you of your situation, [y] Finch: you are our witness first before you are a human."
    c "And shirking your duties as a witness would be quite the offense."
    "Being back on land would make that difficult."
    y "If I help you find her, will you help me return home to my family? To be human again?"
    y "What do I need to do?"
    c "You simply need to stay here until my knights locate the sea witch."
    y "But- that could take weeks! Months, even!"
    "(insert concerned alarm about time, family thinking she’s dead etc)"

    c "I have a duty to my nephew and to my people to fulfill."
    c "Keeping you here is simply part of fulfilling it."
    "He really isn’t budging."
    "I knew it wouldn’t be easy, but… I can’t give up."
    "There must be something I can do to get him to agree."
    "I run my fingers over the purse at my side."

    y "What if I could return the favor?"
    y "If you help me, I could bring you things from the surface."
    c "I have no interest in your human toys."
    y "But we have a lot of wonderful things up there!"
    "I pull out the camera from my purse and present it to him."
    "Hopefully it’ll get his attention. I don’t know how else to bargain with him."
    y "Like this camera, for instance. It lets me keep records of memories that last forever."
    "Cetus focuses on the camera for only a moment before he shakes his head."
    c "There is no memory that can truly last forever, no matter how much you may want it to."
    "He may be right… {w} but that’s not the point right now."
    "I can’t stay here forever!"
    c "Though…"
    c "To think, your precious human toy found its way back to you after being transformed. How very curious."
    "Cetus leans in closer."

    scene cg_cetusoffice:
        fit "contain"
    $ config.side_image_tag = "None"
    y "...!"
    c "I’ll make a different deal with you, [y] Finch, if you wish to gain your legs back."
    y "A different deal?"
    c "Locating the siren is one task, but stopping her is another."
    c "A siren powerful enough to cause these storms won't go down without a fight."

    c "There is a spell that can subdue her, but it will require certain magical artifacts."
    c "With a nudge in the right direction, you should have no trouble finding them."
    y "And this will help me become human again?"
    c "Retrieve them for me and I shall honor our bargain."

    c "That is all your little mortal heart desires, is it not?"
    y "Yes, but…"

    menu:
        "I have so many questions."

        "Don’t you need me to stay here?":
            c "Arrangements will need to be made. You will require an escort, of course."
            c "I certainly can’t have you swimming off before we’ve found the siren."

        "Will it be dangerous?":
            c "Perhaps. It would be no more dangerous than trying to figure it out yourself."
            "Alt Version 1:"
            c "Perhaps. But what is reward without risk?"
            "Alt Version 2:"
            c "Perhaps."

        "Why me?":
            c "Did you not wish for an alternative solution?"
            c "It is simply a task that needs to be done."
            c "Locating magical objects is a task best left to those blessed by luck."

    c "But I suppose if it’s too difficult for you, it cannot be helped."
    y "No. I’ll do it."
    c "In that case, I shall tell you where to begin."

    scene bg black
    "CLIFFHANGER ENDING!!!"

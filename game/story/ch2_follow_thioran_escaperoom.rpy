
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
                "There's no handle on the window, but there’s a small gap between the glass and the wall."
                "If I had something thin, maybe I could pry it open."
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
                        if failescape == 0:
                            $ perfectescaperoom.grant()
                        jump escapedroom_tohallway
                    if not hairpin:
                        if punchwindow:
                            "I already tried that. I need something to help me open this window…"
                            jump escapebegin
                        $ failescape += 1
                        $ punchwindow = True
                        "I lean against the window and push with all my might."
                        "The window doesn’t even budge."
                        play sound "audio/sfx_fistAgainstWindow.ogg"
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
                        ny neutral "Let's see..."
                        "Letter.":
                            $ letter = True
                            show black:
                                alpha 0.7
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
    $ config.side_image_tag = "june"
    ny mermaid neutral "I find myself in another hallway."
    ny shocked "Huh. I suppose this is better than having to find my way back inside the castle."
    ny nervous "That guard’s probably just around the corner. I doubt he’s moved all day."
    "He said that Cetus was in his study. But... I have no idea where to start."
    ny neutral "I need to find him before Sir Guard realizes I’m gone."
    "Hmm..."

    $ speaking_char = "all"
    $ config.side_image_tag = "None"
    show bg palace hallway:
        fit "contain"
    show thioran frown
    show black:
        alpha 0.45
    with fade

    "{i}After several turns, we pass by a hallway with a particularly elegant door.{/i}"
    "{i}It looks like it could lead to someplace quiet, like a library or an office.{/i}"

    hide black
    hide thioran
    with fade

    $ config.side_image_tag = "june"
    ny mermaid neutral "Well, it’s not like I have any other ideas."
    "The way to get back there is very clear in my mind."
    y frustrated "I will {i}not{\i} get lost again."

    #change scenes with each ellipses
    scene bg palace hallway:
        fit "contain"
    with fade
    "..."
    y mermaid neutral "...and hang another left here..."
    scene bg palace hallway:
        fit "contain"
    with fade
    "..."
    ny mermaid shocked "Oh! There’s the decorations the servants were hanging up!"
    ny happy "The door is right here, just like I remembered."

    y "..."
    "Here goes nothing..."
    play sound "audio/sfx_guestDoorKnock.ogg"
    "..."
    "..."
    "..."
    ny nervous "No response."
    "There’s no guarantee he’ll actually be here, but let’s give it a shot."
    "Taking a deep breath, I open the door."

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
    c "Close the door behind you. It can get rather noisy out there."
    c "Though I’m sure you’ve already seen that firsthand."
    play sound "audio/sfx_stoneDoorClose.ogg"
    ny nervous "...At least he’s not sending me away."
    y neutral "I need to speak with you."
    "Cetus pauses a moment before finally putting his work down."
    show cetus displeased with dissolve
    c "Yes. Quite urgently too, it seems, seeing as you’ve broken out of your room to come all the way here."

    y "I wanted to ask-"
    c "No, not from there."
    y shocked "Pardon?"
#    show cetus smirk with dissolve
    c nervous "Come closer."
    "Cetus beckons me forward with a wave of his hand."
    "I swim cautiously towards his desk."

    camera:
        subpixel True
        xpos 0 zoom 1.0
        ease 1.00 xpos -192 ypos -60 zoom 1.30
    with Pause(1.25)
    camera:
        xpos -192 ypos -60 zoom 1.30

    show cetus neutral with dissolve
    c "Now then, how did you make it past the guard?"

    menu cetus_ask:
        set menuset
        ny frustrated "..."
        "\"I was able to slip away.\"":
            y "...Through the window. With a hairpin."
            #"If you break free on the first try +2 cetus (?)"
            if failescape == 0:
                show cetus smirk with dissolve
                c "Clever girl."
                ny nervous "Somehow, his praise only makes me feel more nervous."
                "Shouldn’t he be upset instead?"

            #"If it takes you multiple attempts to break out"
            if failescape > 0:
                c "Though not without causing a commotion, I hear."
                ny shocked "How did he know about that?"
            pass

        "\"I wanted to ask you something.\"":
            #removed after you pick it first
            $ sillyjune = True
            show cetus shocked with dissolve
            c "Well now, was this {i}your{/i} office I barged into?"
            show cetus displeased with dissolve
            c "In that case, there’s plenty of paperwork that needs your attention, {i}my lady.{/i}"
            c "Perhaps I should take my leave before you call the guards to lock me away."
            y shocked "Please don’t call the guards!"
            show cetus smirk with dissolve
            c "Oh? What was that?"
            y "..."
            show cetus neutral with dissolve
            jump cetus_ask

    if sillyjune:
        #"If you picked option 2 first"
        show cetus smirk with dissolve
        c "That wasn’t so bad, was it?"

    show cetus neutral with dissolve
    c "Go on, then. I’ll reward you with my time."

    y "Lord Cetus, you mentioned humans in the throne room earlier."

    show cetus displeased with dissolve
    c "And?"

    y "Well...you were looking at me when you said it."

    y "Did you...mean anything by it?"

    show cetus smirk with dissolve
    c "You’re aiming quite high, little fish."

    c "While I applaud your boldness, you’ll have better luck looking for a partner elsewhere."

    y flustered "{i}Oh!{/i} I didn’t mean it like that!"

    y nervous "It’s just that-"

    show cetus displeased with dissolve
    c "Get to the point."

    "I hope I’m right about this..."

    y frustrated "Do you know...{w}what I really am?"

    c "..."

    ny nervous "...Or not. {w}Did I make a mistake?"

    show cetus neutral with dissolve

    c "Not many have eyes to see what’s right in front of them. But I am not so easily misled."

    c "You’re quite a distance from your shores, {i}human.{/i}"

    y shocked "...!" with vpunch

    y "You didn’t say anything about it before."

    c "And neither did you. A prudent choice."

    c "I’m sure you must have seen for yourself on land - how our kin treat one another."

    #(add flashback image of the mermaid trapped in the glass cage)
    if promermaid > antimermaid:
        y sad "I have..."
    if antimermaid > promermaid:
        y frustrated "I have."

    c "Then I suggest you continue to keep this to yourself. It’ll only get more troublesome if word gets out."

    y nervous "But...for how long? How long is this spell on me going to last?"

    show cetus smirk with dissolve
    c "Did you think my magic to be temporary?"

    show cetus neutral with dissolve
    c "I don’t work in halves."

    "Oh, thank goodness. That’s one less thing to worry about."

    y "Then, will you turn me back into a human after you’ve dealt with the siren?"

    y "So I can return home?"

    c "Return home?"
    show cetus displeased with dissolve

    c "I have been very lenient with you, [y] Finch, but you forget your place."

    c "What comes {i}after{/i} is of no concern to me."

    menu:
        "But…"
        "My family and friends think I’m dead!":
            c sad "A pity."
            pass
        "There are people waiting for me.":
            c frustrated "A pity."
            pass

    "He’s really serious. But… that would mean I’d be stuck like this forever."

    "And what would happen to me once the siren is caught?"

    "I won’t be needed in the castle anymore."

    "No. There must be something I can say to change his mind."

    y "Would you turn me back into a human if I could return the favor?"

    menu changehismind:
        set menuset
        ny nervous "There must be something I can say to change his mind."
        "I could go out and help you hunt the siren!":
            y neutral "I’ve seen her lair, after all."
            y happy "If we work together, I’m sure we’ll have a better chance!"
            show cetus neutral with dissolve
            c "If nothing else, your sheer recklessness should be applauded."
            pass

        "I could bring you back things from the surface.":
            c "I have no interest in your human toys."
            c "And even if I did, why should I believe that you’d keep your word?"
            y shocked "..."
            show cetus neutral with dissolve
            c "Try again."
            jump changehismind

        "Also, just consider: Please!!!":
            y shocked "Lord Cetus, please reconsider! You’d have my gratitude for life."
            c "..."
            y "Please, please, please, please, please, please, please, please, please-{nw}{w=0.1}" with vpunch
            show cetus shocked
            y "Please, please, please, please, please, please, please, please, please-{nw}{w=0.1}"
            y "Please, please, please, please, please, please, please, please, please-{nw}{w=0.1}"
            y "Please...Pretty please..?"
            show cetus displeased with dissolve
            c "................"
            y "Please..."
            c  "Are you quite finished?"
            y sad "...Yes."
            jump changehismind


    c nervous "Do you have any idea what it would take to bring down a siren?"

    c "Maris Lumina may be protected by old magic, but it would not be able to shield us out there."

    c "What do you suppose would happen were we to fight her head-on?"

    y neutral "Couldn’t you fight magic with more magic? Aren’t there other magic users that could help us?"

    show cetus bittersmile with dissolve
    c "Perhaps that would have been possible in another lifetime. {w}But I am all that remains now."

    y sad "...Oh."

    show cetus neutral with dissolve
    c "That is why we must find a different way."

    c "Though the Students may be gone, the relics they’ve left behind remain."

    y neutral "Relics?"

    show cetus smirk with dissolve
    c "Items, imbued with the magic of their creators."

    ny shocked "Cetus suddenly leans in closer."

    if not renpy.seen_image("cg_cetusoffice"):
        scene cg_cetusoffice:
            fit "contain"
        camera:
            xpos 0 ypos 0 zoom 1.0
        with vpunch
        $ renpy.notify("A new CG has been unlocked in the gallery.")
    else:
        scene cg_cetusoffice:
            fit "contain"
        camera:
            xpos 0 ypos 0 zoom 1.0
        with vpunch

    $ config.side_image_tag = "None"
    y "...!"

    c "They may be of use to me, were you to go out and find them."

    y  "If I were to find these relics for you, would you turn me back into a human?"

    c "That will depend on how well you perform."

    "He’s willing to make a deal?"

    y "..."

    "But something doesn’t feel right…"

    y "Why ask me? Why not just send out your guards?"

    c "I don’t believe you're in any position to be questioning me."

    y "Then how can I trust that you’ll keep your word?"

    c "Because you don’t have a choice. I believe your desperation outweighs your uncertainty."

    "Well… he isn’t wrong."

    "This might be my only chance of getting home."

    y "..."

    y "Alright. I’ll do it. It’s a deal."

    c "An excellent choice. Now, here is what you must do…"

    $ finished_demo_thio.grant()

    jump endofdemo

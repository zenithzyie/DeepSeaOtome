
label ch2_castle_escaperoom:

    menu escapebegin:
        "What should I do?"
        "Examine the window.":
            if not lookedatwindow:
                $ lookedatwindow = True
                "There isn’t much of a view from here. This room must be at the back of the palace. The stained glass makes it difficult to see outside."
                "The glass looks thick. It might be difficult to break."
                "It has no handle or latch, but there is a small gap between the glass and the wall."
                "I push with all my might."
                "The window doesn’t even budge."
                "If I had something thin like a lockpick, maybe I could open it."
            if lookedatwindow:
                pass

            menu:
                "Should I try to open it?"
                "Try to open it.":
                    if hairpin:
                        "The hairpin slips easily into the small gap."
                        "After a fair bit of moving it around, I hear a faint click."
                        "The window slides open. There’s just enough room for me to swim through."
                        "Now I just need to find Lord Cetus!"
                        jump escapedroom_tohallway
                    if not hairpin:
                        if punchwindow:
                            "I already tried that. I need something to help me open this window…"
                            jump escapebegin
                        $ failescape += 1
                        $ punchwindow = True
                        "In a surge of desperation, I slam a fist against the glass."
                        "The thunk is loud enough that I soon hear knocking against the door."
                        guard "Everything alright in there?"
                        y "Everything’s fine!"
                        "My hand is rather sore though…"
                        "I’m certain the guard would try to stop me if I make any further noise."
                        "I should find a quieter method to open the window."
                        jump escapebegin
                "Not yet...":
                    "I shouldn’t be too reckless. I only have one chance at escaping."
                    jump escapebegin

        "Search the room.":
            menu searchroom:
                "There’s a small cabinet beside the bed and a mirror on the wall."
                "Check the mirror.":
                    #(show full cg of Mermaid June)?
                    if promermaid > antimermaid:
                        "Wow, I look so different!"
                        "The colors and fabrics are pretty, but I miss my coat a bit as well."
                        "Without it, I feel a little exposed…"
                        jump searchroom
                    if antimermaid > promermaid:
                        "I… hardly recognize myself."
                        "I doubt Hunter or Grandfather would either."
                        jump searchroom

                "Check the dresser.":
                    if coinpurse and hairpin:
                        "It seems like I've searched through everything here."
                        jump escapebegin
                    menu checkdresser:
                        set menuset
                        "Letter.":
                            "{i}My Dearest Lord Cetus. {/i}"
                            "{i}Ever since I glimpsed your elegant complexion at the festival last year, my head has been filled with nothing but thoughts of you. You shine even brighter than the late king himself. Your graceful poise, your slender hands, your tender tentacles…It is enough to drive a lady to madness. If you would allow me the opportunity, I could show you where to put all of those tentacles of yours-{/i}"
                            y flustered "Oh!"
                            "The rest of the letter is filled with the fantasies of a young noble woman."
                            y "I'll just… put this back."
                            jump checkdresser

                        "Hairpin.":
                            $ hairpin = True
                            "There’s what appears to be an ornate hairpin resting inside the dresser."
                            y "How beautiful. Did it belong to the last person who stayed here?"
                            "The pointy end is rather thin. Maybe I can use this for something?"
                            "I'll keep it in my bag for now."
                            jump checkdresser

                        "Small bag.":
                            $ coinpurse = True
                            "I spy a small bag tucked in the back of the drawer."
                            "It clinks faintly and I discover several gold coins inside."
                            "Do they use this as currency?"
                            "I place the coinpurse into my bag. I’m sure I can find a use for this later."
                            jump checkdresser

                        "Return." if coinpurse and hairpin:
                            "It seems like I've searched through everything here."
                            jump escapebegin
                "Return.":
                    jump escapebegin

        "Talk to the guard.":
            "The guard isn’t willing to tell me anything."
            "Should I really be bothering him again?"
            if coinpurse:
                "The coinpurse jingles faintly in my bag."
                "That fishmonger in Aquantis wasn’t too helpful either until I offered him money."
                "I have to try everything I can here. It’s the only way to get home."
                menu:
                    "Bribe the guard.":
                        $ bribeguard = True
                        $ failescape += 1
                        "I knock on the door."
                        y "Excuse me. Sir Guard?"
                        guard "What is it now?"
                        y "Could you please take me to Lord Cetus? I can pay you."
                        "I jingle the coinpurse in hopes of getting his attention."
                        guard "So desperate as to resort to bribery? Try that again and your new room might become the palace dungeons."
                        "My cheeks burn with embarrassment as I swim away from the door."
                        "That didn’t go as well as I’d hoped."
                        jump escapebegin
                    "Don’t bother.":
                        "This still won’t get me anywhere."
                        "I should take a closer look around the room."
                        jump escapebegin

            else:
                "I knock on the door."
                y "Excuse me. Sir Guard?"
                guard "Keep it down in there."
                "This still won’t get me anywhere."
                "I should take a closer look around the room."
                jump escapebegin


label escapedroom_tohallway:
    scene bg cetus study:
        fit "contain"
    with dissolve
    "Woah, Cetus, your office is kinda sexy?"
    show cetus neutral:
        ypos 70
        xpos 170
    c"I know, right? This office is as sexy as me."
    y neutral "Woag. Man boobs."

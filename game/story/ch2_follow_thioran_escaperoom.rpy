
label ch2_castle_escaperoom:

    menu escapebegin:
        "What should I do?"
        "Examine the window.":
            if not lookedatwindow:
                $ lookedatwindow = True
                "It’s difficult to see through the stained glass. Does it lead outside of the castle?"
                "The window is missing a handle, but there’s a small gap between the glass and the wall."
                "I lean against the window and push with all my might."
                "The window doesn’t even budge."
                "If I had something thin like a letter opener, maybe I could pry it open."
            if lookedatwindow:
                pass

            menu:
                "Should I try to open it?"
                "Try to open it.":
                    if hairpin:
                        "The hairpin slips easily into the small gap."
                        "After a fair bit of moving it around, I hear a faint click."
                        play sound "audio/sfx_windowSlideOpen.ogg"
                        "The window slides open. There’s just enough room for me to swim through."
                        "Now I just need to find Lord Cetus!"
                        jump escapedroom_tohallway
                    if not hairpin:
                        if punchwindow:
                            "I already tried that. I need something to help me open this window…"
                            jump escapebegin
                        $ failescape += 1
                        $ punchwindow = True
                        play sound "audio/sfx_fistAgainstWindow.ogg"
                        "In a surge of desperation, I slam a fist against the glass."
                        "Ouch!"
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
            "There’s a dresser beside the bed and a mirror on the wall."
            menu searchroom:
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
                    "I open the dresser."
                    if coinpurse and hairpin:
                        "It seems like I've searched through everything here."
                        jump escapebegin
                    menu checkdresser:
                        set menuset
                        "Letter.":
                            play sound "audio/sfx_thickPaperRustle.ogg" volume 0.8
                            "{i}My Dearest Lord Cetus.{/i}"
                            "{i}Ever since I glimpsed your elegant complexion at the festival last year, my head has been filled with nothing but thoughts of you. You shine even brighter than the late king himself.{/i}"
                            "{i}Your graceful poise, your slender hands, your tender tentacles…It is enough to drive a lady to madness.{/i}"
                            "{i}If you would allow me the opportunity, I could show you where to put all of those tentacles of yours-{/i}"
                            y flustered "Oh!"
                            "The rest of the letter is filled with the fantasies of a young noble woman."
                            play sound "audio/sfx_stoneDrawerClose.ogg" volume 0.8
                            y "I think I’ll leave this here…"
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
                            play sound "audio/sfx_coinJingle.ogg"
                            "It clinks faintly and I discover gold and silver coins inside."
                            "Do they use this as currency?"
                            "I place the coinpurse into my bag."
                            jump checkdresser

                        "Return." if coinpurse and hairpin:
                            "It seems like I've searched through everything here."
                            jump escapebegin
                "Return.":
                    jump escapebegin

        "Talk to the guard.":
            if bribeguard:
                "No...I really shouldn't talk to him again."
                jump escapebegin
            else:
                "The guard isn’t willing to tell me anything."
                "Should I really be bothering him again?"
                if coinpurse:
                    play sound "audio/sfx_coinJingle.ogg"
                    "The coinpurse jingles faintly in my bag."
                    "That fishmonger in Aquantis wasn’t too helpful either until I offered him money."
                    "I have to try everything I can here. It’s the only way to get home."
                    menu:
                        "Bribe the guard.":
                            $ bribeguard = True
                            $ failescape += 1
                            play sound "audio/sfx_guestDoorKnock.ogg"
                            "I knock on the door."
                            y "Excuse me. Sir Guard?"
                            guard "What is it now?"
                            y "Could you please take me to Lord Cetus? I can pay you."
                            play sound "audio/sfx_longerCoinJingle.ogg"
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
                    play sound "audio/sfx_guestDoorKnock.ogg"
                    "I knock on the door."
                    y "Excuse me. Sir Guard?"
                    guard "Keep it down in there."
                    "This still won’t get me anywhere."
                    "I should take a closer look around the room."
                    jump escapebegin


label escapedroom_tohallway:
    scene bg palace hallway:
        fit "contain"
    "I swim outside the window and find myself in an open-windowed hallway."
    "Here goes nothing…"
    #(a pause, knocking sfx.)
    "..."
    "There's no response."
    "Maybe he’s not here? {w}Well, there’s only one way to find out."
    "Taking a deep breath, I open the door."
    call cetus_office

label cetus_office:
    scene bg cetus study:
        fit "contain"
    with dissolve
    "Unlike the rest of the castle, this room is dimly lit."
    show cetus neutral:
        ypos 70
        xpos 50
    "Cetus is behind a desk covered in scrolls. He seems to be immersed in his paperwork."
    y neutral "Lord Cetus?"
    c " Close the door behind you. It can get rather noisy out there."
    c "Though I’m sure you’ve already seen that firsthand."
    y "I need to speak with you."
    "Cetus pauses a moment before finally putting his work down."
    c "Yes. Quite urgently too, it seems, seeing as you’ve broken out of your room to come all the way here."
    "...At least he’s not sending me away."

    y "I wanted to ask-"
    c "No, not from there."
    y "Pardon?"
    c "Come closer."
    "Cetus beckons me forward with a wave of his hand."
    "I swim cautiously towards his desk."

    c "Now then, how did you make it past the guard?"

    menu cetus_ask:
        "I came through the window.":
            y "I was able to get it open."
            "If you break free on the first try +2 cetus (?)"
            c "Clever girl."

            "If it takes you multiple attempts to break out"
            c "Though not without causing a commotion, I hear."

            "If you picked option 2 first"
            c "That wasn’t so bad, was it?"

        "I wanted to ask you something.":
            c "Well now, was this your office I barged into?"
            c "There’s plenty of paperwork that needs your attention, my lady."
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

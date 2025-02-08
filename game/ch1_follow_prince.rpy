# follow branches here

#FOLLOW THIORAN
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
    show prince angry:
        subpixel True 
        pos (0.0, 1.0) zoom 1.0 
        linear 0.33 pos (-0.23, 1.87) zoom 2.0 
    with Pause(0.43)
    show prince angry:
        pos (-0.23, 1.87) zoom 2.0 
    "I can’t stop, crashing into the back of the striking merman’s head."
    #SCREEN SHAKE
    $ config.side_image_tag = "None"
    # voice "audio/voice/prince/THIODAL-7.wav"
    show prince sweat with hpunch
    up "!!!"
    # voice "audio/voice/prince/THIODAL-8.wav"
    show prince angry with hpunch
    up "Who-"
    show prince angry:
        subpixel True 
        pos (-0.23, 1.87) zoom 2.0 
        linear 0.19 pos (0.15, 1.0) zoom 1.0 
    with Pause(0.29)
    show prince angry:
        pos (0.15, 1.0) zoom 1.0 
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

    show prince angry with dissolve
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
    hide prince with dissolve
    "Left alone with my thoughts, my mind races every which way."
    "Am I the first human to experience the sea like this?"
    "I wish I had my camera. But it wouldn't survive the plunge."
    "I hope it somehow escaped my fate."
    "Hunter must think the worst outcome for me, falling like I did."
    "And...oh, Grandfather!"
    "He would be devastated to find out I went overboard!"
    "They're going to think I drowned.."
    "I need to return back."
    "The waters seem to brighten more as we swim, peaks of coral and schools of beautiful fish."
    $ config.side_image_tag = "june"
    window auto hide
    show bg capitalcity:
        xalign 0.5
        subpixel True 
        zoom 1.05 
        linear 1.75 zoom 1.0
    with dissolve
    with Pause(1.75)
    show bg capitalcity:
        zoom 1.0 
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
    jump endofdemo

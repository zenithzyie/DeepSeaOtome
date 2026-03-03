label ch2_jorunn_village:
##This is the continuation of Follow Jorunn after leaving Prashadi's cave

    scene bg sea:
        fit "contain"
    play music "audio/music_underwater.ogg" volume 1.0 fadeout 1.0
    pause 0.7
    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve
    with dissolve

    j mermaid neutral "I should probably mention that the village doesn't get too many visitors these days. They might have some questions for you."

    y "Oh, right. What should I say?"
 
    y nervous "I need to be careful. They can't know I'm human."
    
    #Anti mermaid:
    if antimermaid >= 1:
        "Who knows what they could do to me?"
    
    # Pro mermaid:
    if promermaid >= 1:
        "I don't want to make them uncomfortable."

    j "How about this - we could say you're a traveling trader! They used to come by pretty often before the storms got worse."

    y happy "Do you think that would work?"
    
    y nervous "But...{w} I don't have anything I could trade."

    j "Just say you lost your goods in the storm, easy. I'll back you up!"

    "I can't believe he's acting so confident. Well, hopefully this works!"

    scene bg jorvillage with dissolve:
        fit "contain"
    $ speaking_char = "Jorunn"
    show jorunn glee with dissolve

    j mermaid neutral "Here we are! Welcome to <village name here>."

    y shocked "Wow...!"

    ny neutral "So this is what a mermaid village looks like! I've never seen so many mermaids in one place before."

    "A few mermaids pause when they see me. One of the guards at the entrance swims up to us."

    show jorunn sweat
    j "Aw, barnacles. It just had to be this guy on watch duty."

    show jorunn glee
    j "Hey <nickname>! It's good to see you. I'm back!"

    V "Ugh. Don't call me that. I have an actual name."

    V "And who's this, Jor? Don't tell me you brought back another mouth to feed."

    ny nervous "Ack, he's looking at me like I'm going to eat his puppy!"

    y happy "It's nice to meet you. I'm [y]."

    j "She'll just be staying the night. Until the storm blows over, y'know."

    V "What?"

    V "You don't look like you're from these waters. What are you doing all the way out here?"

    #Choice things go here







    #jump endofdemo
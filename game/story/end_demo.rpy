#Change this
label endofdemo:
    scene bg black
    with dissolve
    show chibi_merjune:
        fit "contain"
        pos (185, 116)
        zoom 0.6
    show text "Thank you for playing the demo for {p}Heart's Depth!{w}":
        align (0.5,0.5)
    with dissolve
    pause

    hide chibi_merjune
    hide text
    with dissolve
    pause

    show chibi_thio:
        fit "contain"
        pos (125, 116)
        zoom 0.6
    show text "Follow {a=https://zenithzyie.itch.io/hearts-depth}{color=#97c9e6}our game page{/color}{/a}{p}for news on updates...{w}":
        align (0.5,0.5)
    with dissolve
    pause
    
    hide chibi_thio
    hide text
    with dissolve
    pause

    $ MainMenu(confirm=False)()
    return

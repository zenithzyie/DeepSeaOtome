#Change this
label endofdemo:
    scene bg black
    with dissolve
    show chibi_hunter:
        fit "contain"
        pos (720, 130)
        zoom 0.6
    show chibi_jor:
        fit "contain"
        pos (155, 136)
        zoom 0.55
    show text "Thank you for playing the demo for {p}Heart's Depth!{w}":
        align (0.5,0.5)
    with dissolve
    show ctc_pos

    pause

    hide chibi_hunter
    hide chibi_jor
    hide text
    with dissolve
    show chibi_cetus:
        fit "contain"
        pos (680, 130)
        zoom 0.6
        xzoom -1
    show chibi_thio:
        fit "contain"
        pos (125, 116)
        zoom 0.6
    show text "Follow {a=https://zenithzyie.itch.io/hearts-depth}{color=#97c9e6}our game page{/color}{/a} for news{p}on the full release...{w}":
        align (0.5,0.5)
    with dissolve
    pause

    $ MainMenu(confirm=False)()
    return

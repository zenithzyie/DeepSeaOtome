# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Min", image="june")
define j = Character("Jane", image="june")
define o = Character("October", image="june")

init python:
    config.side_image_tag = "june"

# The game starts here.

label gamestart:

    scene bg bedroom

    show jane smile

    "NARRATION"

    # If you want to hide the side image
    $ config.side_image_tag = "None"

    "This is a narration so the side image shouldn't appear."

    # ""

    #this above one makes a blank thing, good for comedic effect?

    #NEED TO DO THIS EVERY TIME THERES NARRATION W/ NO MIN
    # To unhide the side image
    $ config.side_image_tag = "min"

    m neutral "It's so cold"

    o "Vee speaking rn"

    m "You've created a new Ren'Py game."

    m "Once you add a story, pictures, and music, you can release it to the world!"

    j "Wait what do you mean this is just a tutorial"

    $ config.side_image_tag = "None"

    "It was in fact a tutorial"

    $ config.side_image_tag = "min"

    m "Idk man we're just testing it ig"

    return

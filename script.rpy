# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define a = Character("Mia")
define b = Character("James")

# Variables to reach the endings.
default mia_affection = 0
default mia_make_up = 0
default james_affection = 0
default james_make_up = 0
default mia_dislike = -3
default james_dislike = -3
default escape_loop = False
default loops = -1


# The game starts here.

label start:

    # Prologue goes here
    m "Hi"

    # Goes on until MC realises she's in a loop.
    # Choices matter from here.

    jump main_game

label main_game:
    $ loops += 1



label cafe:
    menu :
        "Who should I meet now?"
        "Mia":
            jump mia_problem
        "Choice 2":
            jump james_problem
        
        
label mia_problem:
    a "Hi Miku."
    menu:
        a "You might be wondering about what happened to us."
        "Yes":
            $ mia_affection += 1
            a "Well here's the thing...."

        "No":
            $ mia_dislike += 1
            a "Oh... I see...."
            a "Well why are you here then"



label james_problem:

    return




label looping_evaluation:
    if escape_loop == True:
        jump ending_evaluation
    else:
        $ default mia_affection = 0
        $ default mia_make_up = 0
        $ default james_affection = 0
        $ default james_make_up = 0
        $ default mia_dislike = -3
        $ default james_dislike = -3
        jump main_game


label ending_evaluation:

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define a = Character("Mia")
define b = Character("James")

# Variables to reach the endings.
default mia_affection = -1 # Negative value
default mia_make_up = 0
default james_affection = -1 # Negative value
default james_make_up = 0
default escape_loop = False
default mia_cafe = False
default james_cafe = False
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

    m "They have already started arguing but it's just background noise to me now."
    menu:
        "Confront Mia and James":
            $ mia_affection -= 1
            $ james_affection += 1

            jump confrontation

        "Ignore them":
            $ mia_affection += 1
            # Text goes here
            jump cafe

label confrontation:
    # Text goes here

    jump cafe

label cafe:
    menu :
        "Who should I meet now?"
        "Mia":
            $ mia_affection += 1
            jump mia_problem
        "James":
            $ james_affection += 1
            jump james_problem
        
        
label mia_problem:
    a "Hi Miku."
    menu:
        a "You might be wondering about what happened to us."
        "Yes":
            $ mia_affection += 1
            a "Well here's the thing...."

            jump game_Stop_temp

            # Text



        "No":
            $ mia_affection -= 1
            a "Oh... I see...."
            a "Well why are you here then"

            jump game_Stop_temp

label james_problem:
    b "Oh Miku..."
    b "What brings you here?"


    return


label game_Stop_temp:
    return

label looping_evaluation:
    if escape_loop == True:
        jump ending_evaluation
    else:
        $ mia_affection = 0
        $ mia_make_up = 0
        $ james_affection = 0
        $ james_make_up = 0
        $ mia_dislike = -3
        $ james_dislike = -3
        jump main_game


label ending_evaluation:

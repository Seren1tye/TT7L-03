# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = character('Sery', color="#7F00FF")


# The game starts here.

label start:
    #Displaying text and character dialogue
    "During an uneventful night."
    a "Hello!"
    a "I did this so I can try out RenPy for the first time"
    

label sprites:
    #Showing the character model and swapping expressions.
    a "Wait where is my portrait?"
    show zeil smile
    a "Oh thats how I look!"
    show zeil annoyed
    a "Thought I looked different but it doesn't matter anyways"
    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('Sery', color="#7F00FF")
define b = Character('Sery clone', color="#87CEEB")


# The game starts here.

label start:
    #Displaying text and character dialogue
    "During an uneventful night."
    a "Hello!"
    a "I did this so I can try out RenPy for the first time"
    

label sprites:
    #Showing an image on screen and swapping sprites.
    a "Wait where is my portrait?"
    show zeil smile
    a "Oh thats how I look!"
    show zeil annoyed
    a "Thought I looked different but it doesn't matter anyways"
    hide zeil annoyed
    show zeil smile
    a "Hmm..."
    a "I wonder if I can clone myself?"
    # Adding another sprite in a scene.
    show zeil shocked at left
    show extra normal at right
    a "Whoa...."
    b "I can clone myself??"
    b "Wait this isn't a perfect clone! What a sham...."
    a "Ok how do I undo this?"
    # Removing a sprite from a scene.
    hide extra normal
    a "Ah, thats how I do it."

    return

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

label background:
    show zeil annoyed
    a "This black void is so boring. Can I be somewhere else instead?"
    # Adding a background to the scene.
    scene bg classroom
    show zeil angry
    a "Wait are we at schooL????"
    show zeil bored
    a "Better than the black void at least."
    show bg gym
    show zeil shocked
    a "Huh we're at the gym?"
    a "We're switching locations FAST."
    show zeil smug
    # Use \"text\" to show quotation marks
    a "Heh you're using a lot of \"show\" lines."
    a "Betcha can't use \"scene\" instead hehehe."

    scene bg classroom
    with dissolve
    a "Hey!!!!!"
    show zeil annoyed
    with fade
    a "That's rude you know! {size=-10}Although I was kinda asking for it.....{/size}"

label bgm:
    show zeil normal
    a "..."
    show zeil bored
    a "..."
    show zeil annoyed
    a "..."
    show zeil angry
    a "Are you really gonna let me suffer in silence!"
    a "At least put some background music!"
    # Play background music
    play music "audio/bgm_basketball.mp3" fadein 1.0
    show zeil annoyed
    a "I don't like this music."
    a "Play something else."
    a "Also reduce the volume it's waaaaaaaaaay too loud."
    stop music
    play music "audio/Persona 5 Royal - Mementos Upper Area__735000_4822273.ogg" volume 0.25
    a "That's better"

label sfx:
    play audio "sfx_bell.mp3"
    show zeil shocked
    a "Oh the bell rang!"

label choices:
    show zeil sad
    a "Looks like our time is up..."
    show zeil 
    a "Did you enjoy our time together{size=-5}and learn something?{/size}?"
# System to choose options
menu:
    "Yes":
        jump choices_a

    "No":
        jump choices_b

label choices_a:
    show zeil laugh
    a "I'm glad that we had fun!"
    show zeil smile2
    a "Sure I have inconsistent characterization but that shouldn't matter!"
    a "This is just following a tutorial and taking extreme liberties after all."
    jump ending_a

label choices_b:
    show zeil normal
    a "...."
    jump ending_b

label ending_a:
    show zeil smile
    a "Good luck on creating the actual novel!"
    show zeil smile2
    a "Anything is possible especially since you have the Internet at your disposal!"
    show zeil sad
    a "This is goodbye then (and not an excuse to use all the character sprites)"
    show zeil smile
    a "Goodbye"
    return
    
label ending_b:
    show zeil angry
    a "What do you mean no????!!!"
    a "Wow thanks soooooo much for nothing!"
    show zeil sad
    a "I'd be crying right now but I don't have a crying sprite so this will have to do"
    show zeil angry
    a "You suck"
    return


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define a = Character("Mia")
define b = Character("James")
define s = Character("Sarah")

# Persistent values for the ending tracker (and best ending)
# default persistent.mia_end = False
# default persistent.james_end = False
# default persistent.bad_end = False
# default persistent.best_end = False
# default persistent.secret_end = False
# default persistent.end_got = False

# Variables used in the game.
default mia_affection = 0 
default james_affection = 0 
default make_up = 0
default mia_cafe = False
default james_cafe = False
default loops = -1
default confront = False
default breakup = False
default best_end = 0
default breaking_up = False

# Defining images
image a1 = "Mia 1.png"
image a2 = "Mia 2.png"
image a3 = "Mia 3.png"
image a4 = "Mia 4.png"
image a5 = "Mia 5.png"
image a6 = "Mia 6.png"
image a7 = "Mia 7.png"
image a8 = "Mia 8.png"
image a9 = "Mia 9.png"
image a10 = "Mia A.png"
image a11 = "Mia B.png"

image b1 = "James 1.png"
image b2 = "James 2.png"
image b3 = "James 3.png"
image b4 = "James 4.png"
image b5 = "James 5.png"
image b6 = "James 6.png"
image b7 = "James 7.png"
image b8 = "James 8.png"

image school = "bg school.jpg"
image room = "room.png"
image schoolout = "school_out.jpg"
image park = "park.jpg"
image cafe = "cafe.png"
image school2 = "jamescafe.jpg"
# The game starts here.

label start:
    jump prologue

label intermission:
    scene room with Fade(0.5,0.3,0.5)
    "I return back to my room."
    "It's been quite a long day, hopefully this never-ending day finally comes to an end."
    "I lie in bed staring at the ceiling, hoping for weariness to take me over."
    jump loop_checker

# For the Secret Ending
label loop_checker:
    if loops == 10:  # If the game loops 10 times, it will unlock a secret ending
        $ loops = 0
        $ persistent.end = True
        jump Secret_Ending
    else:
        jump best_or_bad_end

label best_or_bad_end:
    if best_end >= 3:
        $ persistent.best_end = True
        jump Best_Ending
    elif breaking_up:
        $ persistent.bad_end = True
        jump Bad_Ending
    else:
        jump ending_checker

# Calculate the affection to jump into different ending
label ending_checker:
    if mia_affection < 3 and james_affection < 3:
        $ loops += 1
        jump main_gameplay  # if Mia and James affection didn't hit the requirement, the game will loop again
    elif mia_affection > james_affection:
        $ persistent.mia_end = True
        $ persistent.end = True
        jump Mia_Ending  # If Mia affection is higher than James, it jumps into Mia's Ending
    else:
        $ persistent.james_end = True
        $ persistent.end = True
        jump James_Ending  # If James affection is higher than Mia, it jumps into James's Ending



# Dev ending chooser for testing
label ending_chooser:
    m "Choose an ending."
    menu:
        "Best Ending" if persistent.mia_end and persistent.james_end:
                $ persistent.best_end = True 

        "Mia's Ending":
            $ persistent.mia_end = True
            $ persistent.end = True
            return
        "James's Ending":
            $ persistent.james_end = True
            $ persistent.end = True
            return
        "Bad Ending":
            $ persistent.bad_end = True
            $ persistent.end = True
            return
        "Secret Ending":
            $ persistent.secret_end = True
            $ persistent.end = True
            return
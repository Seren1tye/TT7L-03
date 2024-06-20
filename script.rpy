
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define a = Character("Mia")
define b = Character("James")

# Persistent values for the ending tracker (and best ending)
# default persistent.mia_end = False
# default persistent.james_end = False
# default persistent.bad_end = False
# default persistent.best_end = False
# default persistent.secret_end = False
# default persistent.end_got = False

# Variables used in the game.
default approach = False
default mia_affection = -1 # Temp value
default mia_make_up = 0
default james_affection = -1 # Temp value
default james_make_up = 0
default escape_loop = False
default mia_cafe = False
default james_cafe = False
default mia_outside = False
default james_outside = False
default loops = -1
default confront = False
default leave_alone = False
default breakup = False
default making_up = False

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
image school out = "school_out.jpg"
# The game starts here.

label start:
    jump prologue



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

# label cafe:
#     menu :
#         "Who should I meet now?"
#         "Mia":
#             $ mia_affection += 1
#             $ mia_cafe = True
#             jump mia_problem
#         "James":
#             $ james_affection += 1
#             $ james_cafe = True
#             jump james_problem
        
        
# label mia_problem:
#     a "Hi Miku."
#     menu:
#         a "You might be wondering about what happened to us."
#         "Yes":
#             $ mia_affection += 1
#             a "Well here's the thing...."

#             jump game_Stop_temp

#             # Text



#         "No":
#             $ mia_affection -= 1
#             a "Oh... I see...."
#             a "Well why are you here then"

#             jump game_Stop_temp

# label james_problem:
#     b "Oh Miku..."
#     b "What brings you here?"

# label after_school:
#     "Who should I meet now?"
#         "Mia":
#             $ mia_affection += 1
#             jump mia_after_school
#         "James":
#             $ james_affection += 1
#             jump james_after_school

# label mia_after_school:
#     if mia_cafe == True:
#         mia_affection += 2
#     jump mia_after_school_dialogue

# label james_after_school:
#     if james_cafe == True:
#         james_affection += 2
#     jump james_after_school_dialogue

# label mia_after_school_dialogue:
#     # Text
#     "Should I?"
#     menu:
#         "Invite Mia to hang out outside school":
#             $ mia_outside == True
#             $ mia_affection += 1
#         "Leave her alone":
#             jump game_Stop_temp


# label james_after_school_dialogue:
#     # Text
#     "Should I?"
#     menu:
#         "Invite James to hang out outside school":
#             $ james_outside == True
#             $ james_affection += 1
#         "Leave him alone":
#             jump game_Stop_temp

# label game_Stop_temp:
#     return

# label looping_evaluation:
#     if escape_loop == True:
#         jump ending_evaluation
#     else:
#         $ mia_affection = 0
#         $ mia_make_up = 0
#         $ james_affection = 0
#         $ james_make_up = 0
#         $ mia_dislike = -3
#         $ james_dislike = -3
#         jump main_game


# label ending_evaluation:

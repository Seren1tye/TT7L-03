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

# List for obtainable endings
define persistent.ends = [
    {"name": "Best Ending", "desc": "Mia and James made up and their relationship is going better than ever.", 
    "unlocked": False},
    {"name": "Mia Ending", "desc": "Mia broke up with James but it looks like she's eyeing on someone else.", 
    "unlocked": False},
    {"name": "James Ending", "desc": "James broke up with Mia and decided to pursue a relationship with you instead.", 
    "unlocked": False},
    {"name": "James Ending", "desc": "James broke up with Mia and decided to pursue a relationship with you instead.", 
    "unlocked": False},
    {"name": "Bad Ending", "desc": "James broke up with Mia and decided to pursue a relationship with you instead.", 
    "unlocked": False}, 
    {"name": "Secret Ending", "desc": "You looped one too many times and you lost your mind.", 
    "unlocked": False}
    
]

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


# The game starts here.

label start:
    jump prologue

label main_game:

# Dev ending chooser for testing
label ending_chooser:
    m "Choose an ending."
    menu:
        "Mia's Ending":
            $ persistent.ends[1]["unlocked"] = True
            return
        "James's Ending":
            $ persistent.ends[2]["unlocked"] = True
            return
        "Bad Ending":
            $ persistent.ends[3]["unlocked"] = True
            return
        "Secret Ending":
            $ persistent.ends[4]["unlocked"] = True
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

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define a = Character("Mia")
define b = Character("James")

# Variables to reach the endings.
default approach = False
default mia_affection = -1 # Negative value
default mia_make_up = 0
default james_affection = -1 # Negative value
default james_make_up = 0
default escape_loop = False
default mia_cafe = False
default james_cafe = False
default mia_outside = False
default james_outside = False
default loops = -1


# The game starts here.

label start:

    # bedroom bg image
    # Alarm sfx
    # Stop alarm sfx
    # Replay alarm sfx
    "...."
    m "....What time is it...."
    "I pick up my phone on my bedside table."
    "It reads Friday, 13th September 2024, 6:47 am."
    "I rose up from my bed immediately"
    m "Oh no! I'm late for school!"
    "I gotta rush to reach school on time."
    "I quickly get out of bed and scramble to get ready for school."

    # Classroom bg
    # Bell sfx
    m "{i}Phew{/i}"
    "I audibly sigh as I manage to make it to school in time."
    # Stomach grumbling sfx
    "I had to skip breakfast in order to not be late."
    "Sorry stomach"
    # Show Mia and James on screen.
    # Angry expressions
    "Oh it's Mia and James."
    "They're fighting again." 
    "It's been about a week since  they've been fighting with each other."
    "They would argue loudly and give each other the silent treatment randomly."
    "Of course, our class has to witness their quarrels."
    "Like how we witnessed them enter a relationship together after months 
    of intense “will they won't they” moments."
    "I'm kind of curious about what they are fighting about."

    # Choice to get more dialogue options.
    menu:
        "Approach them":
            $ approach == True
            jump explaination_prologue

        "Leave them be":
            "I don't think I have the right to interfere with them."
            "I'll just leave them be."
            "I look around and see all of my classmates staring at them arguing."
            "The class couple is attracting a lot of attention that they're 
            probably not aware off."
            "Classmate" "Guys! The teacher is coming!"
            "Both of them immediately stopped arguing."
            "I guess the threat of disciplinary action can make them shut up if nothing else can."
            "Mia looked embarrased once she saw everyone looking at her."
            "We all looked towards to our teacher as she entered our class."
            jump cafe_prologue


label explaination_prologue:
    "As I approach Mia and James, I see them give glares that could kill each other."
    "I'm scared to approach them now but I've already made up my mind so I might as 
    well commit to it."
    m "Hey guys, is there anything going on betwe-"
    "Mia glares at me, cutting me off."
    a "Go away, it's none of your business."
    a "Look at what you've done! You've made someone else interfere in our problems!"
    b "My fault? I'm sorry for being extremely loud, grabbing everyone's attention. 
    Oh wait. That's you. And you're supposed to be the quiet one."
    a "Can't you ever take responsibility for once! 
    You juuust love to blame me for everything!"
    b "Well it wasn't my idea to ignore the person I'm dating messages and calls!"
    b "Which just so happens to be the same person that sits next to you in school."
    b "Really smart move there."
    # Show Mia flustered
    a "We-well.."
    a "I at least don't do ridiculous stuff like what you always do!"
    a "Is singing loudly in a mall a good idea when we're on a date together?"
    a "My younger brother is more mature than you."
    a "He's 10."
    b "Hey! That's just how I roll! At least it's part of me."
    b "Speaking of maturity, as if you're any better."
    b "I don't treat any minor inconvenience like the world is going to end."
    a "Oh my god you are so insufferable if you think that's a \“minor inconvenience\”."
    m "Hey guys, you both should stop arguing now."
    "They ignore me as they continue arguing to themselves."
    "Random classmate" "Guys! The teacher is coming!"
    "Both of them immediately stopped arguing."
    "I guess the threat of disciplinary action can shut them up if nothing else can."
    "Mia looks around and sees a lot of people staring at them."
    "She sinks down to her chair trying to cover herself from the stares while 
    James gives a sheepish look and sits down on his seat."
    "I rush towards my seat before the class started so I wouldn't 
    be scolded by the teacher."
    jump cafe_prologue

label cafe_prologue:
    # cafeteria bg
    # Bell sfx
    "Finally it's recess time."
    "I can finally satiate my hunger."
    "As I sit down with my group of friends to eat 
    I feel someone tapping on my shoulder."
    "???" "Hey Miku?"
    "I look behind me and see Mia."
    "She looks troubled."
    a "Do you mind if I talk to you for a while?"
    "Sorry hunger but curiosity has won me over."
    "I excuse myself from my friends and head
    to a more quiet corner in the cafeteria."
    m "So what do you want to talk about?"
    a "Well as you already know…me and James have been fighting a lot recently."
    if approach == True:
        a "....Im sorry about lashing out earlier."
        a "I was so angry that I accidentally yelled at you."
        "She's self aware? That's a first."
        m "It's fine no offense taken."
    m "Anyways what happened between you two?"
    a "Well as you know James is very immature."
    m "It feels like he hasn't matured ever since he was like 9 years old."
    a "Hahaha..."
    a "It usually pisses me off a lot but recently 
    I feel like it's gotten even more irritating."
    m "I wonder how you haven't exploded yet."
    a "Hey what is that supposed to mean?"
    "Mia sighs to herself."
    a "a"
    a "{size=-7}Okay calm down Amelia.{/size}"
    a "I know he's been quite childish always and while it annoys me a lot."
    a "I could tolerate it."
    a "{size=-15}I also find it hot.{/size}"
    m "Hmm? What did you say?"
    # Mia blushes here.
    a "N-nothing!"
    a "But like I've said I feel that he's more irritating now."

    menu:
        "Well, did you talk to him about it?":
            a "..."
            a "No...."
            a "I don't know how to bring it up with him."
            a "We do argue from time to time but this is the 
            first time we've ever argued this much."
        "Since when did you start to feel it's more irritating?":
            a "Last week I think?"
            a "I'm not sure..."
    return


    # Goes on until MC realises she's in a loop.
    # Choices matter from here.

    #jump main_game
label temp:
    "The same thing happens every day."
    "I go to school."
    "Mia and James argue."
    "I leave them alone."
    "They stop before class starts."
    "The day restarts."
    "I go to school."
    "Mia and James argue."
    "I talk to them."
    "They stop before class starts."
    "The day restarts."
    "I don't go to school."
    "The day restarts."
    "My mind thinks of a movie I watched a while ago."
    "Groundhog Day."
    "The protagonist, Phil, is stuck in a time loop 
    and has to repeat the same day over and over again."
    "He broke free after changing something in his life."
    "I must be in the same situation."
    "But it feels like no matter what I do I can't escape the time loop."
    "Unless..."
    # Mia and James appear on screen.
    "My only way to escape is by stopping them from arguing."
    "At least I hope that's the case."
    "There's only one way to find out."


label main_game:
    $ loops += 1
    # Set this to play on the first gameplay loop
    # Alarm sfx
    # Stop alarm sfx
    "The day looped again."
    "It's time to try out my theory."
    "If they stop arguing then I can move on to the next day."
    "I don't even know how many times I've done this routine."
    "I hope I don't ever lose track of myself."

    # Put the message for consecutive loops here by using an elif statement.

    # Class bgm
    # Class bg
    "I reach school early."
    "There's not many people in class right now."
    "I can see a few bags left alone on their seats."
    "Guess their owners must be somewhere else."
    "Less distractions at least."
    "If my theory is true then I could make them reconcile together."
    "I could also break them up."
    "That's on the table but I'm not sure if I want to do it."
    "Well it is AN option."
    "I glance up at the clock."
    "7:12am"
    "I look towards the class entrance and see Mia entering class."
    "It's almost time for them to start arguing."
    "As soon as James enters the classroom, Mia will give him a death stare."
    "He'll go to his seat and argue with Mia."
    "I've seen it a few times already."
    "Their argument gets boring to listen to after a while."
    b "Hey Mia!"
    b "Why haven't you responded to my text messages?"
    a "Oh you wanna know why?"
    a "Well it's because of what you did!"
    "Oh boy they're arguing again."
    menu:
        "Step into their argument":
            $ mia_affection -= 1
            $ james_affection += 1

            jump confrontation

        "Leave them alone":
            "I don't think I should get involved in their argument."
            "It's going to stop later anyways."
            "As they argue I think about how to get them to make-up."
            "I could make them meet together somewhere and talk it out."
            "But I have to convince them to meet up somewhere."
            "Random classmate" "Guys! The teacher is coming!"
            "Mia and James stop arguing with each other."
            "Mia looks around and sees a lot of people staring at them."
            "She sinks down to her chair trying to cover herself from the stares while 
            James gives a sheepish look and sits down on his seat."
            "Time to listen to the same class again."
            jump cafe

label confrontation:
    b "How would I know what I did if you wouldn't tell me?"
    a "Well do you wanna know?"
    a "Is singing loudly in a mall a good idea when we're on a date together?"
    a "My younger brother is more matur-"
    m "Guys you should stop arguing with each other."
    a "Go away, it's none of your business."
    a "Look at what you've done! 
    You've made someone else interfere in our problems!"
    b "My fault? I'm sorry for being extremely loud, grabbing everyone's attention. 
    Oh wait. That's you. And you're supposed to be the quiet one."
    "Gotta love lover quarrels."
    
    # Minigame goes here

    # If player suceeds in the minigame.
    $ mia_affection += 1
    $ james_affection += 1
    $ mia_make_up += 1
    $ james_make_up += 1

    a "Can't you ever take responsibility for once! 
    You juuust love to blame me for everything!"
    m "Guys!"
    "I raise my voice to catch their attention."
    "It worked as they stopped arguing momentarily to look at me."
    "Mia gives a sharp glare to me."
    a "What is it?"
    m "Please stop arguing."
    m "Everybody in class is looking at you."
    "They both take a look at their surroundings and 
    see everyone in class staring at them."
    "There's also people from other classes staring at them."
    "I don't think they've noticed them though."
    # Show Mia being embarrased
    a "A: A-a..."
    "Mia sinks to her seat looking extremely embarrassed."
    "James looks around sheepishly before sitting down on his seat as well."
    "It's better for it to happen now than later."
    "I decide to head back to my seat while Mia is recovering from her embarrassment."
    "Random classmate" "Guys! The teacher is coming!"
    "Time to listen to the same class again."

    # If the player fails
    m "Guys, you should stop arg-"
    "Mia glares at me, cutting me off."
    a "Go away, it's none of your business."
    a "Look at what you've done! You've made someone else interfere in our problems!"
    b "My fault? I'm sorry for being extremely loud, grabbing everyone's attention.
    Oh wait. That's you. And you're supposed to be the quiet one."
    a "Can't you ever take responsibility for once!
    You juuust love to blame me for everything!"
    "{i}Sigh.{/i}"
    "They aren't listening."
    "There's no point in me interrupting them now."
    "I head back to my seat while they still argue among themselves."
    "I can try again when I loop back to today."
    "Random classmate" "Guys! The teacher is coming!"
    "Mia and James stop arguing with each other."
    "Mia looks around and sees a lot of people staring at them."
    "She sinks down to her chair trying to cover herself from the stares while 
    James gives a sheepish look and sits down on his seat."
    "Time to listen to the same class again."



    # Text goes here

    jump cafe

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

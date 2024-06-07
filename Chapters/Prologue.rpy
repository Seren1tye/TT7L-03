label prologue:
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
scene bg classroom


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
        call explaination_prologue
        jump cafe_prologue

    "Leave them be":
        call left_alone

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
        # Add something here so skip is disabled temporarily
        m "b"
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
            jump main_game0
        "Since when did you start to feel it's more irritating?":
            a "Last week I think?"
            a "I'm not sure..."
            jump main_game0

label explaination_prologue:
    $ approach = True
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
    return

label left_alone:
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
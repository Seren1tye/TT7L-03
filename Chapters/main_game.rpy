label main_game0:
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
    jump main_gameplay

label main_gameplay:
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
    # Temporary
    menu:
        "Succeed":
            call succeed1
        "Fail":
            call failure1
    # Text goes here

    jump cafe


label succeed1:
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

label failure1:
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


label cafe:
    jump ending_chooser
    return
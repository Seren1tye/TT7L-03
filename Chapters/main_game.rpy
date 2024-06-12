label main_game0:
    "As I lie in bed, I begin to ponder over what has been happening these past few days."
    "Days? Or Day? I don't know how to describe this."
    "What is going on?"
    "Whenever I go to sleep I relive the same day."
    "13th September, Friday 13th. Of course this happens on Friday the Thirteenth."
    "I go to school, listen to Mia and James argue about the same thing, I go home, fall asleep, and wake up to relive the same day."
    "I don't get it, why am I reliving the same day?"
    "Whenever the clock strikes 12 am the day rewinds itself."
    "I tried to stay awake past 12 but I always faint afterwards and when I wake up the day is still 13th September."
    "Is this some sort of time loop?"
    "...."
    "Hold on..."
    "Am I stuck in a time loop?"
    "I don't really believe in supernatural occurrences but what else can explain what is happening to me?"
    "Some random person decided to loop this specific day for their own amusement?"
    "That's a stupid thought."
    "However the reason I'm in a time loop may be because of those two."
    # Show Mia and James on the screen
    "Mia and James."
    "I have a feeling that I'm stuck in this loop because of those two."
    "I have a feeling that the only way I can escape this time loop is if I help them with their relationship, no matter what."
    "Maybe I'll have to break them up or bring them together, who knows what works, I just gotta hope that I don't lose my mind in the process."
    "It's been about 10 times since I've relived the same day over and over again."
    "I grab my phone on the bedside to check the time."
    "23:57"
    "3 more minutes until the day loops."
    "There's no point in staying awake any longer. It's time to go to bed."
    "I stare at my ceiling waiting for 3 minutes to pass."
    "What can I even do to help their relationship? Is this even related to their relationship? What if I'm overlooking something else?"
    "Doubt clouds my mind as I lie in bed, waiting for the clock to reach 12 am."
    "...."
    jump main_gameplay

label main_gameplay:
    # game loops here
    # Set this to play on the first gameplay loop
    # Alarm sfx
    # Stop alarm sfx
    # if 1st loop
    "I rise up from my bed and stare at my phone."
    "I stare at my phone and as if on cue, my alarm starts to ring."
    "It's time to try out my theory."
    "If they stop arguing then I can move on to the next day."
    "I don't even know how many times I've done this routine."
    "I hope I don't ever lose track of myself."
    "I get out of my bed to turn off my alarm and head to the toilet to prepare for school."
    "The splash of cold water hits my skin as I think about what to do."

    # after 1st loop
    # "I rise up from my bed and stare at my phone."
    # "I stare at my phone and as if on cue, my alarm starts to ring."
    # "{It's the {loop} time since I decided to help with Mia and James's relationship.}"
    # "I get out of my bed to turn off my alarm and head to the toilet to prepare for school."
    # "The splash of cold water hits my skin as I think about what to do."

    #transition
    # Class bgm
    # Class bg
    "I stare at my classroom's entrance, waiting for the two celebrities to enter the classroom."
    "As my classmates slowly trickle in the classroom, I glance up to the clock hanging on the wall above the whiteboard."
    "It reads “7:12 am”."
    "In about a minute Mia and her posse would come in from another class and gather near the whiteboard to gossip."
    "And James will enter soon and argue with Mia when he locks eyes with her."
    "I see Mia and her posse enter the class and gather at the blackboard."
    "Girl A" "OMG Mia! You should tell us!"
    "Sarah" "Yeah we're starving for tea over here! Tell us what happened!!"
    "Girl C" "Girl you can't just argue with your boyfriend and NOT expect us to ask."
    "Mia swatted her friends away like they're annoying flies but it's proven to be ineffective as they swarm her again."
    a "Oh my god it's none of your business."
    "I tune out from their conversation. It becomes boring to listen to after hearing it after the fourth time."
    "Their gossip session comes to a halt after a strong voice cuts through the class."
    b "Mia!"
    "James steps inside the classroom and glares at Mia."
    "His friends who have been talking with him stare at Mia from the entrance."
    b "Why haven't you returned my texts and calls?"
    a "You know what you did in the first place!"
    b "Well how would I know when you wont even tell me?"
    "Once again they've started to argue in front of the whole class."
    "A crowd is forming around them, watching them argue."
    "There's even people from other classes watching them argue."
    $ renpy.force_autosave(take_screenshot=True)
    menu:
        "What should I do?"
        "Step into to break their fighting":
            # Mia affection increases
            # James affection increases
            # James makes up increases
            jump confrontation

        "Leave them alone":
            $ leave_alone = True
            # Mia affection increases
            # Mia makes up increases
            "I decide to leave the two lovebirds alone."
            "Their argument will come to a halt soon and continue at the cafeteria later anyways."
            "Love knows no bounds I guess."
            "I wonder if they actually love each other in the first place."
            "Well I've never been in a relationship so I don't know how they work."
            "I know nothing about romance aside from romance movies and anime and I'm pretty sure they're not accurate to real life."
            "I watch my classmates surround them listening to their argument."
            "Sarah" "Heh"
            "Sarah" "This might be good for me."
            "One of Mia's friends sits at her table beside me."
            "Her name is Sarah."
            "We do interact with each other sometimes so we aren't complete strangers but we aren't exactly friends either."
            "We're more like acquaintances."
            "I look towards my right and see her slumped over her chair."
            "She's looking straight at them instead of me."
            "Sarah" "I just want to know what's happening with them so I can get together with James."
            "Sarah" "Ah James....when you eventually dump Mia we can finally get together. Like we were meant to be...."
            "Sarah" "If only you weren't with Mia."
            "I can understand what she's saying now since I've heard her mumble to herself a few times already."
            "What a nice friend she is."
            "I guess she doesn't know that Mia and Mia are friends."
            "Random Classmate" "Guys! Miss Low is arriving!"
            "Everybody immediately rushed back to their seats. Mia and James aren't the only ones who fear our teacher's wrath."
            "The students outside of our class who were listening to the argument are long gone."
            "As footsteps approach our class, I begin to prepare listening to classes I've heard a bunch of times already."
            jump cafeteria

label confrontation:
    $ confront = True
    "Begrudgingly, I decide to approach them to break up their fighting."
    "I push past some of my classmates as I approach the arguing couple."
    m "Hey you two should stop arguing."
    "Mia shoots me a glare."
    a "Stay out of this will you."
    b "What did I even do? Is it because of our last date?"
    a "Obviously! That was the worst date I've EVER been on!"
    b "Oh come on it wasn't that bad-"
    m "Guys!"
    "I raise my voice to catch their attention and it worked."
    "Mia and James turn around to look at me."
    m "You should stop arguing before the teacher catches you."
    "Class is going to start soon after all."
    "They immediately stopped arguing. The threat of disciplinary action manages to scare them."
    "I don't blame them. Our chemistry teacher is the head of discipline and she doesn't tolerate their relationship during school times despite the principal's approval."
    "Random Classmate" "Guys! Miss Low is arriving!"
    "Everybody immediately rushed back to their seats. Mia and James aren't the only ones who fear our teacher's wrath."
    "The students outside of our class who were listening to the argument are long gone."
    "As footsteps approach our class, I begin to prepare listening to classes I've heard a bunch of times already."
    jump cafeteria


    
    # school bell sfx
    # cafeteria bg

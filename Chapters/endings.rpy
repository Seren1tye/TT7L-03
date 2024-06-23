label Best_Ending:
    $ persistent.best_end = True
    stop music
    scene room with Fade(0.5,0.3,0.5)
    "I return back to my room."
    "It's been quite a long day, hopefully this never-ending day finally comes to an end."
    "I lie in bed staring at the ceiling, hoping for weariness to take me over."
    play music "sfx_alarm.mp3"
    "I groggily get out of bed."
    "I haven't felt this tired when I wake up in a while."
    stop music
    "I check my phone on the side of my bed."
    "06:32"
    "13th September 2024"
    "Wait a minute."
    "It's Friday the 13th. The day after 12th September."
    "I feel tears dropping down my face. I'm finally free from the time loop."
    "I sit in bed for a moment, just taking in the fact that I can finally move on."
    "I glance at my phone again."
    "06:55"
    "Oh no I'll be late for class!"
    "I jumped out of my bed and rushed to the toilet to get ready for school."

    scene school with Fade(0.5,0.3,0.5)
    play audio "sfx_bell.mp3"
    play music "bgm_school.mp3" volume 0.75 fadein 0.5
    "Phew. I made it to school in time."
    "I haven't been late to school ever since the early days of me being stuck in the time loop."
    "Days? Hours? Times? I don't know and I don't have to care about it anymore."
    show a10 with dissolve:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    show b7 at left with dissolve:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    "I look at Mia and James's table and see the both of them being happy with each other."
    "Guess they finally reconciled after yesterday."
    stop music fadeout 0.5
    hide a10 with dissolve
    hide b7 with dissolve
    play music "bgm_argue.mp3" fadein 0.5 volume 0.75
    s "No this can't be! Why are they together!"
    "I look to the side and see Sarah fuming mad."
    "She looks directly towards me."
    s "Hatsune Miku! What did you do!"
    m "What do you mean?"
    s "Ugh! You screwed over everything! My only chance of getting together with James is gone!"
    s "The magic rock I used to keep them in a time loop until I found a way to break them up is destroyed! And somehow you're unaffected."
    m "Wait what???"
    "I was stuck in a time loop because of petty jealousy?"
    s "Doesn't matter I'll never show up again."
    "Sarah then disappeared."
    stop music fadeout 0.5
    "That's weird."
    play music "bgm_school.mp3" volume 0.75 fadein 0.5
    "Random Classmate" "Guys! Ms Ho is arriving!"
    "Ah Physics class."
    "I'd never admit this last time but after spending who knows how long learning Chemistry and Maths over and over again, Physics is a nice change of pace."
    "The rest of the day went smoothly. Nothing much happened."
    "As for Sarah, it seems like nobody knew she existed. Everybody claims that there's nobody that sat to my left for this entire year."
    "That hurts but at least I'm out of the cursed loop."
    scene schoolout with Fade(0.5,0.3,0.5)
    play audio "sfx_bell.mp3" volume 0.75
    "As I leave school I hear someone calling my name."
    a "Miku!"
    show a10 with dissolve:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25 
    "Mia rushes towards me alongside James."
    show b7 at left with dissolve:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    hide a10
    show a7 :
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25 
    a "I'd like to say thanks for bringing us back together yesterday. We really appreciate it."
    hide b7
    show b5 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "Yeah without you intervening who knows what could have happened."
    m "Aw guys it's nothing."
    hide a7
    show a6 :
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25 
    a "Well we're going on a date this Sunday. You wanna come with?"
    "Third wheeling a couple? Sounds like it's gonna be boring."
    hide b5
    show b4 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    m "To where?"
    b "There's an amusement park that recently opened and we thought about going there."
    "On second thought that sounds fun."
    m "Sounds fun I'm in."
    hide a6
    show a7 :
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25 
    a "Yeah!"
    hide b4
    show b5 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "Cool."
    m "Well I'll see you on Sunday. Bye guys."
    "I leave the school compound, heading straight back home."
    stop music fadeout 0.5 
    scene room with Fade(0.5,0.3,0.5)
    "It's Sunday, the day of me joining Mia and James to the amusement park."
    scene bs
    "I head out of my room in order to face the future head on."
    return

label Mia_Ending:
    play music "sfx_alarm.mp3"
    "I groggily get out of bed."
    "I haven't felt this tired when I wake up in a while."
    stop music
    "I check my phone on the side of my bed."
    "06:32"
    "13th September 2024"
    "Wait a minute."
    "It's Friday the 13th. The day after 12th September."
    "I feel tears dropping down my face. I'm finally free from the time loop."
    "I sit in bed for a moment, just taking in the fact that I can finally move on."
    "I glance at my phone again."
    "06:55"
    "Oh no I'll be late for class!"
    "I jumped out of my bed and rushed to the toilet to get ready for school."
    scene school with Fade(0.5,0.3,0.5)
    play audio "sfx_bell.mp3"
    play music "bgm_school.mp3" volume 0.75 fadein 0.5
    "Phew. I made it to school in time."
    "I haven't been late to school ever since the early days of me being stuck in the time loop."
    "Days? Hours? Times? I don't know and I don't have to care about it anymore."
    show a2 with dissolve:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    show b6 at left with dissolve:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    "I look at Mia and James's table and see that they both are sitting down at their respective seats."
    "James is talking to Mia but she has a disinterested look in her face."
    "I can barely hear what they are talking about from where I'm sitting."
    b "Mia I'm sorry for what I did. Please forgive me."
    a "We'll talk about it later."
    hide a2
    show a10:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    "She flashes James a smile and looks straight forward."
    hide a10
    show a2:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    "James tried to talk to Mia but quickly recognised his attempts were futile as she was ignoring him."
    "Did Mia actually go through with the idea of breaking up with James?"
    "After seeing Mia break down yesterday after regretting failing to keep in contact with me, she said that she's going to break up with James."
    "It must have been a hasty emotional decision at that time but there's no way she actually is going through with this idea."
    "Random Classmate" "Guys! Ms Ho is arriving!"
    "Ah Physics class."
    "I'd never admit this last time but after spending who knows how long learning Chemistry and Maths over and over again, Physics is a nice change of pace."
    stop music fadeout 0.5
    play audio "sfx_bell.mp3"
    scene cafe with Fade(0.5,0.3,0.5)
    "It's recess time."
    play audio "bgm_cafe.mp3"
    "Due to rushing towards school, I didn't get the chance to pack food from home to eat."
    "I was too busy savouring the present."
    $ food = renpy.random.choice([' a plate of noodles', 'a plate of fried rice', 'burger'])
    "I head to a stall and order a [food]."
    "I get to buy whatever I want as I don't have to spend time with Mia or James in order to escape the time loop."
    "I sit down a few tables away from where Mia and James usually sit, just so I can confirm that I've finally escaped from the time loop."
    "As I savoured my food, I felt someone tapping my shoulder."
    stop music fadeout 0.5
    play music "bgm_mia.mp3"
    show a6 at center with dissolve:
        xpos 0.5095 ypos 1.02
        xzoom 1.25 yzoom 1.25
    "I turn around and see Mia. Again."
    m "Mia? What is it?"
    a "Miku....can you come to the school exterior later when school ends?"
    m "What for?"
    a "Well, you'll see later."
    hide a6 with dissolve
    stop music fadeout 0.5
    "Mia then left the cafeteria."
    "Well this was unexpected. If anything goes wrong I'll just loop back again."
    play music "bgm_argue.mp3" fadein 0.5 volume 0.75
    "Wait a minute."
    "What if this is just another time loop I'm stuck in?"
    "Oh no. Please don't make that be the case."
    "I try to push these thoughts out of my head and focus on my food. After all, what proof is there that I'm stuck in a time loop."
    "Then again there isn't any proof that I was stuck in a time loop beforehand except my own perspective. From other people's point of view it's just a regular day for them."
    stop music
    play audio "sfx_bell.mp3"
    "The sound of the school bell ringing disrupts my thoughts."
    "I head back to the classroom to not be late for classes."
    scene bg school with Fade(0.5,0.3,0.5)
    play audio "sfx_bell.mp3"
    "Finally school is over for the day."
    "I couldn't pay attention in class. My mind is preoccupied with the feeling that this is still a time loop."
    scene cafe with pixellate
    show a6 at center with dissolve:
        xpos 0.5095 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "Miku....can you come to the school exterior later when school ends?"
    m "What for?"
    a "Well, you'll see later."
    scene school with pixellate
    "I should meet up with Mia after school."
    scene school_out with Fade(0.5,0.3,0.5)
    "I head to the school exterior. Mia did ask me to come here. But what for exactly?"
    "I noticed a group of people in a circle. Curious to know why, I went to the circle to find out what is going on."
    play music "bgm_argue.mp3"
    "To my surprise, Mia and James are in the middle of the circle."
    show a4 with dissolve:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    show b8 at left with dissolve:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    a "James, I'm breaking up with you."
    b "....what."
    hide a4
    show a5:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "I've been doing some thinking, and I decided that we should break up."
    "Tears stream down Mia's face. It's obvious that it's tough for Mia to do this."
    a "I'm sorry for doing this to you James."
    b "Mia, wait!"
    "James grabs Mia's hand."
    b "Please! Don't go! At least tell me what I did wrong!"
    "Mia stays silent for a while before finally uttering something."
    "James lets go of Mia's hand."
    "Nobody in the crowd could hear it. Fair since it seems really private."
    "Shame that there's a crowd."
    "Speaking of the crowd, the crowd goes livid. They didn't expect to see someone breaking up."
    "James just looks shocked. It doesn't help that there's a crowd that's witnessing this."
    hide b8
    show b6 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    hide b6 with easeoutleft
    "James then dashes through the crowd, looking pretty hurt."
    stop music fadeout 0.5
    "The crowd slowly starts to disperse, leaving only me and Mia."
    play music "bgm_mia.mp3"
    hide a5
    show a4:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "Ah Miku! You're here!"
    "Mia rushed towards me."
    a "Well originally I wanted only you to see what's happening. Shame that a group has formed though."
    "She looks a bit guilty of what happened."
    m "What did you say to James?"
    hide a4
    show a5:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "Well, I told him that we're breaking up and that I've fallen for someone else instead."
    m "Wait, that's why you went through with breaking up with him? Who are you interested in?"
    "Mia came close to me and whispered something into my ear."
    hide a5
    show a4:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "You know them very well."
    "I move away from Mia out of shock."
    "I'm confused. I don't really know a lot of people so who is she referring to?"
    a "Anyways I'mma go now. See you soon."
    hide a4 with easeoutright
    "Mia leaves the school."
    stop music fadeout 0.5
    "I just stood there in confusion."
    play music "bgm_badend.mp3"
    "I hear someone approaching me and I come face to face with Sarah,one of Mia's new friends, and the person who sits next to me in class."
    s "Hehehehe."
    s "Good job. Now what's rightfully mine is now available."
    s "You did good Hatsune Miku. You're now free."
    m "Wait, Sarah! What do you mean?"
    "I try to call out to her but she had already left the scene."
    "What did she mean by what she said? What is even going on."
    "I decide to go back home. There's not much for me to do now."
    stop music fadeout 0.5
    scene room with Fade(0.5,0.3,0.5)
    "It's almost midnight."
    "I lie in bed just thinking about what went on."
    "I also can't stop thinking about if I'm still stuck in a time loop."
    "I can't sleep due to being very restless."
    "I look at my phone to check the time."
    "23:59"
    "1 more minute until I'll find out."
    "Bracing to fall unconscious, I lie still in bed."
    "...."
    "...."
    "I'm still awake."
    "I look at my phone."
    "00:04"
    "15 September 2024."
    "In disbelief I look at my phone again."
    "The same thing is shown on the screen."
    "I did it."
    "I finally left this cursed time loop."
    "I can feel myself crying."

    scene room with Fade(0.5,0.3,0.5)
    play music "bgm_mia.mp3"
    "The next thing I know, I wake up in my bed, sunlight coming out from the windows."
    "I look at my phone and see that I've gotten text messages from none other than Mia."
    a "hey miku!"
    a "do you wanna date tmr?"
    a "*hang out"
    a 'i meant hang out'
    "I put my phone away and contemplate what is going on."
    "I can finally live life normally and I'm friends with Mia again."
    "Things are finally looking up."

    scene room with Fade(0.5,0.3,0.5)
    "The next day arrived."
    "I get dressed to hang out with Mia."
    "Or more accurately, my date."
    "I'm not so sure."
    scene bs
    "I head out of my room in order to face the future head on."
    return

label James_Ending:
    play music "sfx_alarm.mp3"
    "I groggily get out of bed."
    "I haven't felt this tired when I wake up in a while."
    stop music
    "I check my phone on the side of my bed."
    "06:32"
    "13th September 2024"
    "Wait a minute."
    "It's Friday the 13th. The day after 12th September."
    "I feel tears dropping down my face. I'm finally free from the time loop."
    "I sit in bed for a moment, just taking in the fact that I can finally move on."
    "I glance at my phone again."
    "06:55"
    "Oh no I'll be late for class!"
    "I jumped out of my bed and rushed to the toilet to get ready for school."
    scene school with Fade(0.5,0.3,0.5)
    play audio "sfx_bell.mp3"
    play music "bgm_school.mp3" volume 0.75 fadein 0.5
    "Phew. I made it to school in time."
    "I haven't been late to school ever since the early days of me being stuck in the time loop."
    "Days? Hours? Times? I don't know and I don't have to care about it anymore."
    show a9 with dissolve:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    "I look at Mia and James's table and see only Mia is at her seat. James is nowhere to be seen."
    "After a while, James suddenly burst into the classroom."
    show b3 at left with easeinleft:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "Mia! I'm gonna change seats."
    hide a9
    show a11:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "W-what? What do you mean?"
    b "I said that I'm changing seats."
    hide a11
    show a1:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "You can't do that! Besides, the teachers won't let you."
    hide b3
    show b7 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "I already asked for permission. And our class teacher let me."
    hide a1
    show a11:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "You what???"
    "James pointed to the person sitting beside me."
    b "You! Swap places with me!"
    "The person sitting there stuttered nervously before bringing his belongings to James's table."
    "James heads on over to where that guy was originally."
    hide a11 with dissolve
    show b7 at center with easeinright:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "Mia could only stare in disbelief on what's happening."
    hide b7
    show b5 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Hey Miku!"
    "James is beaming at me. Is he thinking about his crush on me?"
    hide b5
    show b8 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "Random Classmate" "Guys! Ms Ho is arriving!"
    "Ah Physics class."
    "I'd never admit this last time but after spending who knows how long learning Chemistry and Maths over and over again, Physics is a nice change of pace."
    stop music fadeout 0.5
    play audio "sfx_bell.mp3"
    scene cafe with Fade(0.5,0.3,0.5)
    "It's recess time."
    play music "bgm_cafe.mp3"
    "Due to rushing towards school, I didn't get the chance to pack food from home to eat."
    "I was too busy savouring the present."
    $ food = renpy.random.choice([' a plate of noodles', 'a plate of fried rice', 'burger'])
    "I head to a stall and order a [food]."
    "I get to buy whatever I want as I don't have to spend time with Mia or James in order to escape the time loop."
    "I sit down a few tables away from where Mia and James usually sit, just so I can confirm that I've finally escaped from the time loop."
    "As I savoured my food, I felt someone tapping my shoulder."
    stop music fadeout 0.5
    play music "bgm_james.mp3"
    show b4 at center with dissolve:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "I turn around and see James"
    m "James? What is it?"
    b "Hey Miku, can you come to the school exterior after school ends?"
    m "What for?"
    b "Well, you'll see later."
    hide b4 with dissolve
    stop music fadeout 0.5
    "Mia then left the cafeteria."
    "Well this was unexpected. If anything goes wrong I'll just loop back again."
    play music "bgm_argue.mp3" fadein 0.5 volume 0.75
    "Wait a minute."
    "What if this is just another time loop I'm stuck in?"
    "Oh no. Please don't make that be the case."
    "I try to push these thoughts out of my head and focus on my food. After all, what proof is there that I'm stuck in a time loop."
    "Then again there isn't any proof that I was stuck in a time loop beforehand except my own perspective. From other people's point of view it's just a regular day for them."
    stop music
    play audio "sfx_bell.mp3"
    "The sound of the school bell ringing disrupts my thoughts."
    "I head back to the classroom to not be late for classes."
    scene bg school with Fade(0.5,0.3,0.5)
    play audio "sfx_bell.mp3"
    "Finally school is over for the day."
    "I couldn't pay attention in class. My mind is preoccupied with the feeling that this is still a time loop."
    scene cafe with pixellate
    show b4 at center with dissolve:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Hey Miku, can you come to the school exterior after school ends?"
    m "What for?"
    b "Well, you'll see later."
    scene school with pixellate
    "I should meet up with James after school."
    scene school_out with Fade(0.5,0.3,0.5)
    "I head to the school exterior. James did ask me to come here. But what for exactly?"
    "I noticed a group of people in a circle. Curious to know why, I went to the circle to find out what is going on."
    play music "bgm_argue.mp3"
    "To my surprise, Mia and James are in the middle of the circle."
    show a11 with dissolve:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    show b6 at left with dissolve:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "Mia, I wanna break up with you."
    a "James? What are you talking about?"
    b "Like I said, I wanna break up with you."
    hide a11
    show a4:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    a "Wh-why?"
    hide b6
    show b4 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "Well, I fell in love with someone else. "
    hide a4
    show a5:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    "The crowd goes livid. They didn't expect to see someone breaking up. Much less James having a crush on someone else."
    "Mia looks very hurt. Doesn't help that there's a crowd watching this."
    hide a5 with easeoutright
    "Mia rushes away, crying."
    stop music fadeout 0.5
    "The crowd slowly starts to disperse, leaving only me and James."
    play music "bgm_james.mp3"
    hide b4
    show b6 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15 
    b "Miku,you're here."
    "James walked over towards me."
    b "Shame there was a group earlier, I wanted you to be the only spectator."
    "He looks a bit guilty of what happened."
    m "It's because you like me huh."
    b "Yeah."
    hide b6
    show b4 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "Miku, what do you think of me?"
    "This thought has plagued me since the first time I heard him say it and I finally know the answer."
    m "I like you James I really do."
    hide b4
    show b5 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    "James was ecstatic."
    b "Oh wow, I'm glad."
    b "So shall we go on a date on Sunday?"
    "I can't tell him that I might be stuck in a loop."
    m "Yeah alright then."
    b "Alright!"
    "James grasps my hands."
    hide b5
    show b7 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    b "You have no idea what this means to me."
    "James lets go and waves towards me."
    b "Bye Mia! See you on Sunday!"
    hide b7 with easeoutleft
    "James leaves the school."
    stop music fadeout 0.5
    "I just stood there in surprise."
    play music "bgm_badend.mp3"
    "I hear someone approaching me and I come face to face with Sarah,one of Mia's new friends, and the person who sits next to me in class."
    "She has a furious look on her face."
    s "This can't be happening. Nonononono."
    s "He was supposed to be with me! Not you!"
    s "All that effort just for nothing!"
    s "Hatsune Miku! Don't relax just yet. I'll get you someday."
    m "Wait, Sarah! What do you mean?"
    "I try to call out to her but she had already left the scene."
    "What did she mean by what she said? What is even going on."
    "I decide to go back home. There's not much for me to do now."
    stop music fadeout 0.5
    scene room with Fade(0.5,0.3,0.5)
    "It's almost midnight."
    "I lie in bed just thinking about what went on."
    "I also can't stop thinking about if I'm still stuck in a time loop."
    "I can't sleep due to being very restless."
    "I look at my phone to check the time."
    "23:59"
    "1 more minute until I'll find out."
    "Bracing to fall unconscious, I lie still in bed."
    "...."
    "...."
    "I'm still awake."
    "I look at my phone."
    "00:04"
    "15 September 2024."
    "In disbelief I look at my phone again."
    "The same thing is shown on the screen."
    "I did it."
    "I finally left this cursed time loop."
    "I can feel myself crying."

    scene room with Fade(0.5,0.3,0.5)
    play music "bgm_james.mp3"
    "The next thing I know, I wake up in my bed, sunlight coming out from the windows."
    "I look at my phone and see someone calling me. The caller id is unknown."
    "I pick up the phone and hear James talking on the other side of the phone."
    b "Hey Miku!"
    b "Well, this is Miku, right?"
    m "Yeah it's Miku."
    b "Ah great, I just wanted to call you so I can confirm this is your number."
    "James promptly hung up the phone."
    "I'd usually be annoyed at this but not today."
    "I put my phone away and contemplate what is going on."
    "I can finally live life normally and I'm dating James."
    "Things are finally looking up."

    scene room with Fade(0.5,0.3,0.5)
    "The next day arrived."
    "I get dressed for my date with James."
    scene bs
    "I head out of my room in order to face the future head on."
    return

label Bad_Ending:
    play music "sfx_alarm.mp3"
    "I groggily get out of bed."
    "I haven't felt this tired when I wake up in a while."
    stop music
    "I check my phone on the side of my bed."
    "06:32"
    "13th September 2024"
    "Wait a minute."
    "It's Friday the 13th. The day after 12th September."
    "I feel tears dropping down my face. I'm finally free from the time loop."
    "I sit in bed for a moment, just taking in the fact that I can finally move on."
    "I glance at my phone again."
    "06:55"
    "Oh no I'll be late for class!"
    "I jumped out of my bed and rushed to the toilet to get ready for school."

    scene school with Fade(0.5,0.3,0.5)
    play audio "sfx_bell.mp3"
    play music "bgm_school.mp3" volume 0.75 fadein 0.5
    "Phew. I made it to school in time."
    "I haven't been late to school ever since the early days of me being stuck in the time loop."
    "Days? Hours? Times? I don't know and I don't have to care about it anymore."
    show a8 with dissolve:
        xpos 0.55 ypos 0.21
        xzoom 1.25 yzoom 1.25
    "I look at Mia and James's table and see only Mia is at her seat. James is nowhere to be seen."
    "After a while, James enters the classroom without any fanfare."
    show b6 at left with easeinleft:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    "He goes to his seat to take his belongings and goes to another person's seat."
    hide b6 with easeoutleft
    "Looks like he's swapping places."
    hide a8 with dissolve
    stop music fadeout 0.5
    "Did they actually break up?"
    play music "bgm_ultrabad.mp3" volume 0.75 fadein 0.5
    "I hear Sarah laughing beside me."
    s "Hehehehehehe."
    s "Thanks to you, I can get together with James."
    s "Thank you, Hatsune Miku."
    m "Sarah what are you saying?" 
    "Sarah ignored me. No matter what she never paid any attention to me."   
    "Random Classmate" "Guys! Ms Ho is arriving!"
    "Ah Physics class."
    "I'd never admit this last time but after spending who knows how long learning Chemistry and Maths over and over again, Physics is a nice change of pace."
    scene cafe with Fade(0.5,0.3,0.5)
    "It's recess and Mia and James are at separate tables."
    "I approach Mia."
    show a2 at center with dissolve:
        xpos 0.5095 ypos 1.02
        xzoom 1.25 yzoom 1.25
    m "Hey Mia."
    "Mia gives me the cold shoulder. She ignores anything I try to say to her."
    hide a2 with dissolve
    show b3 at center with dissolve:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "I go over to James and he too, ignores whatever I say to him."
    "What is going on?"
    "Why is everyone ignoring me?"
    "I try to ask people around me but they ignore me."
    "Is this the price of what happens to those who meddle in others affairs?"
    "Distraught, I dashed out of school."
    scene bs
    "Looks like this is my life now."
    "A life of emptiness."
    return

label Secret_Ending:
    stop music
    scene bs
    "Master" "What are you doing Miku?"
    scene ws
    "My eyes are covered in darkness before blinding lights shine through my eyes."
    m "Well your game sucks so I was wondering if there's anything worthwhile in it."
    "Master gave a chuckle."
    "Master" "Well looks like it's back to the drawing board for me."
    m "Please make it good, I can't have my name, Hatsune Miku tarnished by this junk."
    "Master" "Hahaha. Alright Miku."
    return
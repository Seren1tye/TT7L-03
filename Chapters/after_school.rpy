label after_school:
    scene school with Fade(0.5,0.3,0.5)
    "Finally school is over for the day."
    "Until I wake up again and relive this day again."
    "I really need to find a way to escape this loop."
    "I don't want to relive this day over and over again."
    "I pack up my belongings and head out to the school exit."
    scene schoolout with Fade(0.5,0.3,0.5)
    "I find a shaded area and stay under it for a while."
    "I want to talk to either James or Mia to try to fix their relationship."
    "After what seems like an eternity, Mia comes out from the entrance."
    "James comes out from the entrance shortly afterwards."
    "They didn't acknowledge each other's presence. Looks like they haven't talked after their fight in the cafeteria."
    menu:
        "Who do I talk to?"

        "Mia":
            # mia affection increases
            $ mia_affection += 1
            jump Mia

        "James":
            # james affection increases
            $ james_affection += 1
            jump James
        
        "Both" if persistent.mia_end and persistent.james_end:
            # best end
            $ best_end += 1
            jump best_end_convo

        

label Mia:
    show a8 at center with dissolve:
        xpos 0.507 ypos 1.02
        xzoom 1.25 yzoom 1.25
    "I approach Mia."
    "She isn't with her posse. Guess she didn't want to talk to them right now."
    "Makes it easier to approach her."
    if mia_cafe == False:
        m "Hey Mia."
        a "Oh it's you."
        hide a8
        show a10 at center:
            ypos 1.03
            xzoom 1.25 yzoom 1.25
        "Mia flashes me a bright smile."
        a "Hi Miku, what do you need?"
        menu:
            "How's things going with you and James?":
                hide a10
                show a3 at center:
                    ypos 1.02
                    xzoom 1.25 yzoom 1.25
                a "Uh….what do you mean? Are you living in your own world?"
                a "You did see us argue earlier didn't you?"
                m "Well yeah but I wanna know what happened."
                m "Aren't we friends? Don't friends tell each other what happens?"
                if james_cafe == True:
                    "I cringed internally at what I said. Can't believe I quoted James out of all people."
                hide a3
                show a2 at center:
                    xpos 0.5 ypos 1.05
                    xzoom 1.25 yzoom 1.25
                "Mia let out a sigh. She looks irritated."
                "It's none of your business so piss off!"
                "Mia turned around and promptly stomped out of school."
                hide a2 with dissolve
                "Looks like I can't ask her that directly."
                # jump to part where the game loops
                jump intermission
                
    else:

        if breakup == True:
            "Mia has a melancholic expression on her face. Maybe it's because I suggested that she break up with James?"
        m "Hey Mia."
        hide a8
        show a10 at center:
            ypos 1.03
            xzoom 1.25 yzoom 1.25
        "Mia flashes me a bright smile."
        a "Oh. Hey Mia. What do you need?"
        # Route branches based on what was done in cafe.
        if mia_cafe == True:
            m "Well have you thought about what I said just now?"
            a "I have."
            if making_up == True:
                hide a10
                show a8 at center:
                    xpos 0.507 ypos 1.02
                    xzoom 1.25 yzoom 1.25
                a "I've been thinking about how to make up with him."
                a "Can you help me Miku?"
                a "I really don't know how."
                a "Besides, it's James's fault. He's the one who made me mad."
                m "Well you can start by not blaming him for everything."
            
            if breakup == True:
                hide a10
                show a8 at center:
                    xpos 0.507 ypos 1.02
                    xzoom 1.25 yzoom 1.25
                a "I've been thinking about if it's worth it to break up with James."
                a "Can you help me Miku?"
                a "I'm not sure if it's a good idea in the first place."
                m "Well you can start by telling me why you even want to break up in the first place."

            a "...."
            hide a8
            show a7 at center:
                xpos 0.5 ypos 1.03
                xzoom 1.25 yzoom 1.25
            a "Do you want to go somewhere together?"
            "I took this opportunity to tease Mia."
            hide a7
            show a11 at center:
                xpos 0.494 ypos 1.03
                xzoom 1.25 yzoom 1.25
            m "This is unexpected. Don't tell me you're cheating on James with me."
            "This caught Mia off guard."
            hide a11
            show a6 at center:
                xpos 0.5 ypos 1.04
                xzoom 1.25 yzoom 1.25
            a "Y-you idiot!"
            a "Ugh, why am I surrounded by idiots everywhere!"
            "I laughed quietly."
            "Mia gets really flustered when I pull off snarky comments. It's funny to do that to her once in a while."
            "Especially since we haven't talked much recently."
            hide a6
            show a9 at center:
                xpos 0.494 ypos 1.04
                xzoom 1.25 yzoom 1.25
            a "{i}sigh{/i}"
            a "Alright let's go somewhere."
            hide a9
            show a7 at center:
                xpos 0.5 ypos 1.03
                xzoom 1.25 yzoom 1.25
            a "Hmmm....how about the park? Does that sound good?"
            a "I'd be down to that."
            # clap sfx
            "Mia clasps her hands together loudly."
            "Alright to the park we go then!"
            hide a7 with easeoutleft
            "Mia swiftly walks to the school exit while I try to follow her from behind."
            m "Wait hold on!"
            jump mia_walk

label mia_walk:
    scene park with Fade(0.5,0.3,0.5)
    show a10 at center:
        ypos 1.03
        xzoom 1.25 yzoom 1.25
    "After a 10 minute walk we finally arrived at a nearby park."
    "This is usually a hangout spot for couples or families on the weekends."
    "Seeing as school just ended around half an hour ago, there aren't a lot of people here other than highschool couples."
    "Personally I don't see the appeal of going to a park for a date, especially after school."
    "Then again, I'm not in a relationship so what do I know? Who knows, I might think going to the park with my S/O is the best thing ever if I have one."
    a "It's been a while since we hung out together. School has been hellish especially after the principal himself made me the model student for academics."
    hide a10
    show a9 at center:
        xpos 0.494 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "It's torture being the best student in the school."
    hide a9
    show a10 at center:
        ypos 1.03
        xzoom 1.25 yzoom 1.25
    a "It's nice to hang out with someone I'm old friends with."
    a "With that said, it's nice to hang out with someone that I've been friends with for a while now. It feels more nostalgic, like the world hasn't completely changed."

    menu:
        "What's going on with you and James?":
            # lead up to bad end.
            jump mia_convo1
        "Then why did you ignore me?":
            # mia affection increases
            $ mia_affection += 1
            jump mia_convo2

label James:
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    "I approach James."
    "He's talking loudly with his group of friends."
    "Sounds like they're talking about sports. Not that I care."
    b "Did you see the goal I made earlier? That's why I'm the be-"

    if james_cafe == False:
        m "Hey James!"
        hide b5
        show b2 at center:
            xpos 0.492 ypos 1.04
            xzoom 1.15 yzoom 1.15
        "James stopped talking with his friends and looked at me."
        "He looked irritated after I interrupted him."
        b "Miku, arentcha? What do you want?"
        m "Well I wanna know what happened between you and Mia."
        hide b2
        show b5 at center:
            ypos 1.04
            xzoom 1.15 yzoom 1.15
        "James let out a hearty laugh, followed by his friends."
        b "Aren't you friends with Mia? Why don't ya ask her instead?"
        m "Well we're not that close."
        hide b5
        show b7 at center:
            xpos 0.505 ypos 1.04
            xzoom 1.15 yzoom 1.15
        b "Don't friends talk to each other about stuff? You should know since you're friends."
        m "As I've said we aren't that clos-"
        b "Just ask Mia since you two are friends and all."
        "It's not like being friends since we were children makes me eligible to ask her on her relationship problems."
        "Guy 1" "Oooh do you think she wants to take James for herself?"
        "Guy 2" "Hahaha she wants to take away James from Mia. That reminds me of an anime I wat-"
        "Guy 3" "Shut it Alex! Nobody wants to hear about whatever you watched."
        "I shut them a glare and they promptly stopped gossiping about me."
        hide b7
        show b3 at center:
            xpos 0.505 ypos 1.04
            xzoom 1.15 yzoom 1.15
        b "Anyways I actually have stuff to do."
        b "Cya! Wouldn't wanna be ya!"
        hide b3 with easeoutleft
        m "But wait she didn-"
        "It was too late as he dashed past me with his friends following along."
        m "Wait James!"
        "He ignored me as he exited the school grounds."
        "Maybe I can talk with Mia instead?"
        "I look around for Mia but can't find her. Guess she went back home already."
        "Bummer."
        "Looks like there's no reason for me to stay in school. Time to go back home."
        jump intermission

    else:
        m "Hey James!"
        hide b5
        show b8 at center:
            xpos 0.486 ypos 1.04
            xzoom 1.15 yzoom 1.15
        "James stopped talking with his friends and looked at me."
        "He had a surprised expression on his face."
        b "Miku? What do ya want?"
        m "Didn't you say that you wanna talk to me later during recess?"
        hide b8
        show b2 at center:
            xpos 0.492 ypos 1.04
            xzoom 1.15 yzoom 1.15
        b "I did?"
        "James thought for a second before he finally spoke up."
        hide b2
        show b4 at center:
            xpos 0.49 ypos 1.04
            xzoom 1.15 yzoom 1.15
        b "Oh yeah I did say that. Didn't know you'd actually come looking for me."
        "Guy 1" "Oooh what's going on?"
        "Guy 3" "Are they dating behind Mia's back? Is this why she's arguing with James?"
        "I paid no attention to the boys bickering."
        m "So when are we gonna talk about Mia?"
        b "Uhhhh...."
        "James looked back to his friends for support but they said nothing."
        m "And preferably one-on-one. I don't want any third party members to listen in."
        "Guy 2" "Aren't you a third party as well? Since you're Mia's friend and all-"
        "I shot him a glare that could kill. He took the message and stopped talking."
        b "How....about a park nearby? We can discuss Mia there."
        m "Alright sure lead the way."
        "James turned around to his group of friends one more time."
        hide b4
        show b1 at center:
                xpos 0.495 ypos 1.04
                xzoom 1.15 yzoom 1.15
        b "Do NOT talk about this to anyone you hear?"
        b "Or else you'll never be invited to gaming nights anymore."
        b "Oh and also you'll break the bro code."
        "His friends nod solemnly. Guess the threat of breaking the 'bro code' is a serious offence."
        hide b1
        show b4 at center:
            xpos 0.49 ypos 1.04
            xzoom 1.15 yzoom 1.15
        b "Alright Mia, follow me."
        hide b4 with easeoutleft
        "James rushed out of the school compound."
        m "Wait hold on!"
        scene park with Fade(0.5,0.3,0.5)
        show b7 at center:
            xpos 0.505 ypos 1.04
            xzoom 1.15 yzoom 1.15
        "After a 10 minute walk we finally arrived at a nearby park."
        "This is usually a hangout spot for couples or families on the weekends."
        "Seeing as school just ended around half an hour ago, there aren't a lot of people here other than highschool couples."
        "Personally I don't see the appeal of going to a park for a date, especially after school."
        "Then again, I'm not in a relationship so what do I know? Who knows, I might think going to the park with my S/O is the best thing ever if I have one."
        "Wait a minute. I'm at the park that's famous for being a dating hotspot with THE most famous guy in my school that's dating THE most famous girl in my school."
        "This is not gonna look good for either of us."
        b "So what do you want to know about me and Mia? She never told you huh?"
        menu:
            "We aren't that close":
                # james affection increases
                $ james_affection += 1
                jump james_convo1
            "Why are you two arguing?":
                jump james_convo2

label james_convo1:
    m "As I've said about a million times, we aren't that close. You should get that drilled into your thick skull."
    hide b7
    show b3 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Yeah yeah I know. You keep repeating that. I'm curious about why exactly."
    m "Well I dunno, we just grew apart I guess."
    hide b3
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    "James let out a loud laugh attracting nearby onlookers."
    "I cover my face in embarrassment."
    m "Did you really have to laugh that loud???"
    b "Hahahah…don't you two still text each other? Last I remembered you sent her a reel about some singer, what's her name?"
    b "Ah yea, Kagerman Ren or something like that."
    "This caught me off-guard. That was around 2 months ago when we did talk to each other."
    hide b5
    show b7 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    m "H-how did you know?"
    b "I've seen her texts before."
    m "That was about 2 months ago. How did you even remember that?"
    b "Your chats with her are pinned to the top of her chat messages. Well after her family and me at least."
    "I am dumb-founded. James knew?"
    m "She hasn't texted me in a while! Isn't that proof that we haven't talked in a while?"
    hide b7
    show b3 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Hmmm...."
    "James looks lost in thought. I've never seen him think that deeply since year 6 in primary school during a maths test."
    hide b3
    show b6 at center:
        xpos 0.506 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Maybe she's embarrassed by you. After all, ever since she was chosen as the model student for academics, she was a popular sensation."
    b "And that talking to you would ruin her reputation so she slowly stopped talking to you until you both stopped talking."
    "That's unusually deep for James. I never knew he had a more serious side to him."
    m "That's....unusually deep for you James."
    hide b6
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    "This time, instead of a hearty laugh, James let off a slight chuckle."
    b "Heh…the 'me' everyone usually sees is just an act after all. Can't have the model student for extra-curriculars to seem smart."
    m "Then why'd you keep doing poorly in tests then?"
    hide b5
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Ah....that's because I'm not that good at studying."
    hide b4
    show b7 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "But after being with Mia my grades shot up! I'm no longer getting single digits!"
    "It's better than nothing at least."
    m "Wait, let's rewind for a second. If she didn't want to talk to me then why is my chats with her pinned to the top?"
    hide b7
    show b6 at center:
        xpos 0.506 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "James stayed silent before finally speaking up."
    b "Maybe it's because she's regretting cutting you off from her life? I'm not so sure I never really bothered to ask her about this."
    m "Huh...."
    m "I didn't know she still wants to talk to me to this day."
    "After thinking for a moment, I feel anger burning within me."
    m "If she didn't want to talk to me then why did she pin our chats to the top?"
    m "If she really wanted to still be friends then why didn't she continue messaging me?"
    m "Why did she have to slowly stop talking before going radio silence?"
    "I can feel tears running down my cheeks. I know I'm crying in front of a guy I haven't really talked to much but at this point I could care less."
    m "Why did she...."
    hide b6
    show b7 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "While I was crying, I felt a hand on my shoulder."
    b "Hey Miku...."
    "I look up amidst sobs and see James with a soft smile on his face."
    b "Everything will be alright. It's fine to feel hurt."
    "I continue to cry. Tears gradually stopped falling down my face and eventually my cries became sobs."
    hide b7
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "I wish I knew why she didn't want to talk to you. Alas I don't know the reason why and Mia won't tell me."
    "James lets off a slight chuckle."
    b "Truth to be told Miku, I had a crush on you during primary school."
    "Wait what?"
    "I looked up to James in surprise, not believing what I was hearing."
    m "Wh-what did you say?"
    b "Heh, guess I said that out too loud didn't I?"
    b "Well I had a crush on you in primary school. I remember that we were classmates in Year 6 and after laying my eyes on you, my heart skipped a beat."
    hide b4
    show b7 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Guess it somehow persisted until now haha."
    hide b7
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "I'm speechless. I really don't know what to say."
    "I've never been in a situation where someone confesses their feelings towards me."
    "Much less someone who's in a committed relationship with someone I used to be close with."
    "This is an interesting situation to be in say the least."
    m "What about Mia? Does she know?"
    hide b4
    show b3 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "No she doesn't and she doesn't have to know."
    hide b3
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Miku, I want to know. What do you think about me?"
    "I stay silent. I'm unsure of what I feel towards him."
    "I used to think that he's just an idiot this whole time but he's surprisingly serious despite the persona he shows off."
    "A part of me is arguing that this is wrong."
    "Mia is my friend and this is an act of betrayal."
    "Another part of me argues that this doesn't matter and that Mia should die in a ditch for all that I care."
    "After all, she did stop talking to me due to embarrassment."
    "I look at James, he looks like he's expecting an answer from me."
    m "I'm....not sure."
    b "Haha, it's alright."
    hide b4
    show b8 at center:
        xpos 0.486 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "James glances at his watch."
    b "Oh shoot I have to go now! Don't wanna be late."
    m "Late for what?"
    b "Personal stuff."
    hide b8
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Welp see ya in class tomorrow, Mia."
    m "Ah goodbye."
    hide b5 with easeoutleft
    "James heads off from the park."
    "I'm still recovering from the bombshell that was dropped on me."
    "James had a crush on me? Did he ever love Mia then? How did he hold on to this crush for this long?"
    "I decided to go back home as I don't feel like staying in the park any longer."
    jump intermission

label james_convo2:
    hide b7
    show b8 at center:
        xpos 0.486 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Looks like you really don't know huh."
    hide b8
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Well me and Mia are arguing cause she couldn't handle me."
    "There's absolutely no way that is the reason why."
    m "There's gotta be something more than that."
    hide b5
    show b7 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Like what exactly?"
    m "Well this is the first time you two argued for this long. Most of the time your so-called “arguments” last at most a day and they're usually over petty matters."
    m "An argument that lasts for this long means that something must have happened between you two."
    hide b7
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    "James let out a loud laugh attracting nearby onlookers."
    "I cover my face in embarrassment."
    m "Did you really have to laugh that loud???"
    hide b5
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Well ya got me there."
    b "Yeah something did happen between us."
    "I'm curious about what happened. Resolving it might be the key to escaping this time loop."
    m "Well tell me what happened!"
    hide b4
    show b3 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Alright fine. You being Mia's friend might help me."
    hide b3
    show b6 at center:
        xpos 0.506 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "As you know, I'm not exactly all that good in academics."
    b "I somehow barely passed my tests and even then it's with Mia helping me a lot."
    b "The only thing that I'm good at are sports."
    b "However, I've been feeling that sports is the only thing that I'm ever gonna be good at."
    b "I can barely do maths, sciences confuse me to no end and history is very confusing."
    b "The only subjects I'm good at are the language subjects and even then it'd be pretty hard to fail in those."
    b "I just feel like I'm kinda insignificant compared to Mia. She's this academic weapon while I'm just a lowly student that's only good at kicking a ball around a field."
    "I'm rendered speechless. I didn't know that James had this side of him."
    m "Wow uh....didn't know you had this side to you, James."
    hide b6
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    "He let out a small chuckle, a stark contrast to his loud laugh earlier."
    b "Heh....I don't really show this side of me to anyone."
    hide b5
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "{size=-15}It also doesn't help that I have a crush on you.{/size}"
    m "What was that?"
    b "Hmm? Did I say anything?"
    "I swear I heard James say something."
    "Did he say he has a crush on me? I must be hearing things"
    "I brush those thoughts aside and focus on James now."
    m "Well did you ever talk to Mia about these feelings?"
    hide b4
    show b6 at center:
        xpos 0.506 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "That's the thing, I didn't."
    b "And when she tries to ask what's happening, I panic and push her away."
    b "It's probably because she's always so overdramatic that I push her away all the time. I'm not really sure."
    b "I don't really know what to do."
    
    menu:
        "I don't know what to do either":
            # leads to a loop
            "James had a dejected look on his face before quickly covering it up with a smile."
            hide b6 
            show b7 at center:
                xpos 0.505 ypos 1.04
                xzoom 1.15 yzoom 1.15
            b "Heheh....it's alright. I didn't expect much anyways."
            b "Well I guess you two really haven't talked to each other in a while huh. Your texts do help prove it."
            m "Wh-what do you mean 'my texts do help prove it'?"
            hide b7
            show b4 at center:
                xpos 0.49 ypos 1.04
                xzoom 1.15 yzoom 1.15
            b "Well I did look at Mia's texts before and saw that you messaged her about something 2 months ago and Mia didn't respond."
            hide b4
            show b7 at center:
                xpos 0.505 ypos 1.04
                xzoom 1.15 yzoom 1.15
            b "Anyways Imma go now. I just remembered I had to do something urgent."
            m "Ah okay then."
            hide b7
            show b5 at center:
                ypos 1.04
                xzoom 1.15 yzoom 1.15
            b "Well, see ya."
            hide b5 with easeoutleft
            "James heads off from the park."
            "This was certainly interesting. I sit down on a nearby bench to collect my thoughts."
            "What could I have said to help James?"
            "Would this help escape the time loop?"
            "Some time has passed and I'm still sitting on the bench, looking at couples hanging out in the park."
            "It's awkward being in a park alone surrounded by couples so I decided to leave the park and return home."
            jump intermission
            # loop
        "What about breaking up with her?":
            # james affection increases
            $ james_affection += 1
            jump james_convo3

label james_convo3:
    hide b6
    show b8 at center:
        xpos 0.486 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "James gives me a dumbfounded look."
    b "What do you mean by breaking up with her?"
    m "Okay hear about what I have to say first."
    m "It's no secret that Mia is over dramatic. It's her main personality trait."
    m " If you were to tell her about how you feel then she might overreact. It'll eventually slip and the whole school will know about this. It's not worth it."
    "I'm overexaggerating a lot but I'm trying to get a point across. Besides, it might be better off for them in the long run."
    hide b8
    show b1 at center:
        xpos 0.495 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Miku, I think you're the one being overdramatic instead."
    b "What's the chances of that happening anyways?"
    m "You can't deny that it's a possibility."
    hide b1
    show b6 at center:
        xpos 0.506 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "James fell silent."
    m "Anyways it's best to think this through."
    b "Miku, can I ask you a question?"
    m "Sure what is it?"
    b "Are you doing this because Mia stopped talking to you?"
    "Wait a minute. How did he know about that?"
    m "Wait, how did you know about that?"
    hide b6
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "I've seen your messages on her phone before. Well in the menu at least I never opened the chat and read your messages."
    "Truth to be told, I'm pretty indifferent towards Mia now."
    "I don't have anything to gain or lose if Mia and James break up."
    "Aside from escaping the time loop at least."
    "It's not like Mia will suddenly come back to being friends with me again when she breaks up with James. Not to mention I'd probably won't be friends with her again."
    "Oh well it doesn't matter."
    hide b4
    show b6 at center:
        xpos 0.506 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Breaking up with Mia huh....I'll do it."
    m "Wait what? You're gonna do it?"
    hide b6
    show b2 at center:
        xpos 0.492 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Yeah, after all, she hasn't even fully explained why she's mad at me."
    b "If this is a sign for things to come then I don't wanna be with her anymore."
    m "Aren't you rushing things way too fast?"
    hide b2
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Truth to be told, I had the thought to break up with her."
    b "I remember someone suggesting that I should break up with her before. Strangely enough I don't remember who exactly."
    "James glanced at his watch."
    hide b4
    show b7 at center:
        xpos 0.505 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Welp I gotta go now."
    b "I got some personal stuff to do."
    hide b7
    show b5 at center:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "See ya, Miku."
    b "Oh and one more thing."
    hide b5
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "I have a crush on you Miku. Always had one and probably will always have one."
    "I was stunned. James had a crush on me?"
    hide b4 with easeoutleft
    "Before I could respond, he left the park."
    "This is insane."
    "I tried to gather my thoughts but I ended up failing."
    "I decide to go back home as I want to think about this in private."
    jump intermission

label mia_convo1:
    hide a10
    show a6 at center:
        xpos 0.5 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "O-oh getting straight to the point I see."
    a "Well...."
    a "You know how earlier I said that James is really immature?"
    hide a6
    show a9 at center:
        xpos 0.494 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "Well, that isn't the whole picture."
    a "Recently he's becoming more different."
    m "Different? What do you mean by that?"
    hide a9
    show a3 at center:
        ypos 1.02
        zoom 1.25 yzoom 1. 
    a "He's....acting different, like he's frustrated about something."
    a "And if I try to ask about it he ignores the question."
    hide a3
    show a8 at center:
        xpos 0.507 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "I don't know what's going on with him."

    menu:
        "Have you tried to sit down with him?":
            jump mia_convo15
        
        "Is he cheating on you?":
            jump mia_convo3
            

label mia_convo2:
    # mia affection increases
    $ mia_affection += 1
    hide a10
    show a4 at center:
        xpos 0.502 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "I...."
    "Mia fell silent."
    m 'Mia. Why did you ignore me for these past few months?'
    "She didn't respond."
    m "Mia?"
    hide a4
    show a5 at center:
        xpos 0.495 ypos 1.03
        xzoom 1.25 yzoom 1.25
    "I hear sobbing coming from Mia."
    a "I'm sorry...."
    a "I'm so sorry...."
    "Mia looks up to me with tears in her eyes."
    a "I'm sorry for ignoring you Miku."
    a "It's just that-that-"
    "What excuse is she going to make up now?"
    a "Ever since I became the model student for academics, I've been surrounded by people 24/7."
    a "And some of the people had an issue with me hanging out with you."
    a "So I had to slowly cut you off."
    a "I'm sorry."
    "I didn't expect this to happen."
    "What should I do?"
    
    menu:
        "Forgive her":
            # mia affection increases
            $ mia_affection += 1
            hide a5
            show a11 at center:
                xpos 0.5034 ypos 1.02
                xzoom 1.25 yzoom 1.25
            a "You forgive me? Even after what I did to you?"
            m "What you did sucks but it's reasonable. After all you are very weak to peer pressure."
            hide a11
            show a5 at center:
                xpos 0.495 ypos 1.03
                xzoom 1.25 yzoom 1.25
            a "Heheh...."
            m "Friends?"
            a "Fr-friends."
            "We embraced each other in a hug."
            hide a5
            show a4 at center:
                xpos 0.502 ypos 1.02
                xzoom 1.25 yzoom 1.25
            a "I've decided to break up with James."
            m "Wait what? Why?"
            a "We aren't a good couple, and also I have feelings for someone else."
            a "No point in staying a relationship that I don't love."
            "She hugs me tighter."
            "We remain in an embrace for a while until Mia lets go."
            hide a4
            show a10 at center:
                ypos 1.03
                xzoom 1.25 yzoom 1.25
            a "Well, I should go now."
            a "Thanks Hatsune Miku."
            hide a10 with easeoutleft
            "Mia leaves the park."
            "Seeing as there's no reason for me to stay any longer I decide to head back home."
            jump intermission

        "Don't forgive her":
            a "Hahahaha....what was I thinking?"
            a "Of course you won't forgive me. I did destroy our friendship because I thought it was uncool."
            hide a5
            show a4 at center:
                xpos 0.502 ypos 1.02
                xzoom 1.25 yzoom 1.25
            a "Well I'm sorry for wasting your time."
            a "Bye."
            hide a4 with easeoutleft
            "Mia leaves the park."
            "Seeing as there's no reason for me to stay any longer I decide to head back home."
            jump intermission


label mia_convo3:
    hide a8
    show a1 at center:
        xpos 0.485 ypos 1.03
        xzoom 1.25 yzoom 1.25
    a "Miku? What are you talking about?"
    a "Him cheating on me? Really?"
    m "Well it's just that it looks like he's showing signs of him cheating. So I assumed that he must be cheating on you with someone else."
    hide a1
    show a2 at center:
        xpos 0.501 ypos 1.028
        xzoom 1.25 yzoom 1.25
    "Mia gives me a sharp glare."
    hide a2
    show a1 at center:
        xpos 0.485 ypos 1.03
        xzoom 1.25 yzoom 1.25
    a "You watch too much anime. There's NO way he's cheating on me. I even read his texts!"
    m "Well is he spending much time with you?"
    hide a1
    show a8 at center:
        xpos 0.507 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "Not recently...."
    m "Then that means that he might be cheating on you."
    hide a8
    show a1 at center:
        xpos 0.485 ypos 1.03
        xzoom 1.25 yzoom 1.25
    a "Wait a minute, how would you know if he is cheating on me? You were never in a relationship ever last I checked."
    m "Uh....I have my sources."
    a "Yeah right."
    hide a1
    show a4 at center:
        xpos 0.502 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "Well this went nowhere."
    a "Well I guess there's no reason for me to be here anymore."
    a "Bye Miku...."
    hide a4 with easeoutleft
    "Mia heads out of the park."
    "Seeing as I don't have any reason to stay here, I leave the park as well."
    jump intermission



label mia_convo15:
    hide a8
    show a9 at center:
        xpos 0.494 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "Well....not really."
    a "We did go on a date last week before we started to argue."
    hide a9
    show a8 at center:
        xpos 0.507 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "The way he acted then really ticked me off."
    m "Didn't he book a reservation at Burger King or something like that?"
    hide a8
    show a11 at center:
        xpos 0.5034 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "Wait, how did you know that?"
    m "Well....you two were arguing pretty loudly during recess."
    hide a11
    show a6 at center:
        xpos 0.5 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "Oh my god, as if my reputation couldn't get any more worse."
    "Mia covers her face in her hands in embarrassment. Guess clarity finally hit her head on."

    menu:
        "Hey it's not all that bad! You'll be even more popular now!":
            # mia affection decreases
            $ mia_affection -= 1
            hide a6
            show a1 at center:
                xpos 0.485 ypos 1.03
                xzoom 1.25 yzoom 1.25
            a "Ohmygod Miku please stop joking! This is serious!"
            m "Sorry. It was a bad time to joke."
            "Not like she has the right to complain since she stopped talking to me."

        "These things happen. It's alright.":
            hide a6
            show a8 at center:
                xpos 0.507 ypos 1.02
                xzoom 1.25 yzoom 1.25
            a "That doesn't change the fact that it happened."
            a "Everyone's gonna make fun of me."
            m "Hey that's not true! In fact everyone is curious about what happened!"
            hide a8
            show a9 at center:
                xpos 0.494 ypos 1.04
                xzoom 1.25 yzoom 1.25
            a "And how would you know that?"
            a "I'm sorry to say this but you don't really talk to many people. How would you know what they're thinking about?"
            m "H-hey! What's that supposed to mean!"
            a "My point is that what do you know about what others think when you don't really talk to others?"
            "The audacity."


    m "...."
    m "We lost track of what we're originally talking about."
    hide a1
    show a9 at center:
        xpos 0.494 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "Ah yeah, about me and James...."
    "Silence falls between us."
    hide a9
    show a6 at center:
        xpos 0.5 ypos 1.04
        xzoom 1.25 yzoom 1.25
    "It's starting to feel awkward now so I decided to break the silence to make it less awkward."
    m "So...."
    m "What happened next?"
    hide a6
    show a9 at center:
        xpos 0.494 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "Well I'd say it's less of 'what happened next' and more of 'what happened before'."
    a "After the Burger King incident I felt that something snapped within me."
    a "I felt that all of his immature actions went from annoying but endearing to irritating."
    a "So that's how we argued and argued and argued."
    m "Well this is the first time it lasted for weeks so it's quite a surprise."
    m "It has never happened before."
    hide a9
    show a8 at center:
        xpos 0.507 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "I guess it's more of small things that kept piling up into a bigger issue."
    a "Instead of it being a single massive issue."
    a "I just don't know what to do...."

    menu:
        "I don't know what to do as well":
            hide a8
            show a4 at center:
                xpos 0.502 ypos 1.02
                xzoom 1.25 yzoom 1.25
            a "Ah...."
            "Mia looks dejected. Looks like she didn't get the answer that she expected."
            a "Well I guess there's no reason for me to be here anymore."
            a "Bye Miku...."
            hide a4 with easeoutleft
            "Mia heads out of the park."
            "Seeing as I don't have any reason to stay here, I leave the park as well."
            jump intermission

        "Break up with him":
            $ breaking_up = True
            hide a8
            show a2 at center:
                xpos 0.501 ypos 1.028
                xzoom 1.25 yzoom 1.25
            a "Hmmm...."
            a "It may be for the best for both of us."
            hide a2
            show a5 at center:
                xpos 0.495 ypos 1.03
                xzoom 1.25 yzoom 1.25
            a "He's not a good partner for me."
            m "Are you sure that you're not reaching too fast?"
            a "Well, I got a voice that tells me that I should break up with James. Strangely enough I don't remember who but the voice sounds familiar."
            "That's weird. It's probably nothing."
            a "Well I guess there's no reason for me to be here anymore."
            a "Bye Miku...."
            hide a5 with easeoutleft
            "Mia heads out of the park."
            "Seeing as I don't have any reason to stay here, I leave the park as well."
            jump intermission



label best_end_convo:
    "I finally got to talk to both Mia and James during recess. This should make them more willing to talk to me."
    "However they won't be talking to me, instead they'll be talking to each other."
    "I decided to meet Mia first since she usually exits the school first."
    show a8 at center with dissolve:
        xpos 0.507 ypos 1.02
        xzoom 1.25 yzoom 1.25  
    "The moment Mia exits the school, I immediately approach her."
    m "Hey Mia."
    hide a8
    show a10 at center:
        ypos 1.03
        xzoom 1.25 yzoom 1.25
    a "Oh. Hey Miku. What do you need?"
    m "Well have you thought about what I said just now?"
    hide a10
    show a8 at center:
        xpos 0.507 ypos 1.02
        xzoom 1.25 yzoom 1.25 
    a 'I did.'            
    a "I've been thinking about how to make up with him."
    a "Can you help me Miku?"
    a "I really don't know how."
    a "Besides, it's James's fault. He's the one who made me mad."
    m "Well you can start by not blaming him for everything."
    hide a8
    show a6 at center:
        xpos 0.5 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "...."
    m "Hey Mia, do you want to go somewhere to talk?"
    hide a6
    show a11 at center:
        xpos 0.494 ypos 1.03
        xzoom 1.25 yzoom 1.25
    a "O-oh! Okay Miku. But where to?"
    m "We can go to the nearby park. Y'know, the one where couples go."
    hide a11
    show a6 at center:
        xpos 0.5 ypos 1.04
        xzoom 1.25 yzoom 1.25
    a "O-oh."
    "Mia looks a bit embarrassed."
    m "But I'm sorry to do this but can you go there first? I'll meet you up soon but you gotta trust me."
    m "Just wait for around 5 minutes."
    a "Oh okay then Miku. I guess I'll see you there."
    hide a6 with easeoutleft
    "Mia leaves the school compound, hopefully going to the park like I suggested."
    "I then turn my focus to James. He isn't out yet so I have to wait for a while."
    "After about 10 minutes, I see James exiting the school."
    show b5 at center with dissolve:
        ypos 1.04
        xzoom 1.15 yzoom 1.15
    "He's talking loudly with his group of friends."
    b "Did you see the goal I made earlier? That's why I'm the be-"
    m "Hey James!"
    hide b5
    show b8 at center:
        xpos 0.486 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "James stopped talking with his friends and looked at me."
    "He had a surprised expression on his face."
    b "Miku? What do ya want?"
    m "Didn't you say that you wanna talk to me later during recess?"
    hide b8
    show b2 at center:
        xpos 0.492 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "I did?"
    "James thought for a second before he finally spoke up."
    hide b2
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    b "Oh yeah I did but I didn't expect you to actually meet-"
    hide b4
    show b8 at center:
        xpos 0.486 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "I grabbed James's hand. There's no time I can't afford to make Mia wait."
    m "There's no time we gotta go!"
    b "Wait go wher-"
    "I whisked James along before he could continue."
    "I can hear his friends' confusion but I can't afford to care."
    b "Miku, where are we going??"
    m "The park."
    scene park with Fade(0.5,0.3,0.5)
    show b4 at center:
        xpos 0.49 ypos 1.04
        xzoom 1.15 yzoom 1.15
    "We finally arrived at the park after rushing to it."
    "I look around to try to find Mia. I finally spotted her after looking around a bit."
    "I point to the direction Mia is in."
    m "Hey James can you go over there for a while? I need to grab something real quick so you can chill over there."
    b "Wait Miku what is this for?"
    m "Trust me it's important. Now go!"
    hide b4 with easeoutright
    "James heads to the location I pointed towards. It's working."
    scene park with fade
    "I take a long route to where they are in order to avoid getting detected."
    "I hide behind the bushes and hear them arguing."
    show a1:
        xpos 0.53 ypos 0.21
        xzoom 1.25 yzoom 1.25
    show b1 at left:
        xpos 0.2 ypos 1.1
        xzoom 1.15 yzoom 1.15
    a "James? Why are you here?"
    b "Mia brought me here!"
    a "What is she up to? Anyways, what do you want to do?"
    "They're arguing."

    menu:
        "Step in":
            # best end
            $ best_end += 1
            m "Guys stop arguing! I was the one who brought you guys together."
            hide a1
            hide b1
            show a11:
                xpos 0.55 ypos 0.21
                xzoom 1.25 yzoom 1.25
            show b8 at left:
                xpos 0.2 ypos 1.1
                xzoom 1.15 yzoom 1.15
            a "Miku? You were there the whole time?"
            m "Well I just arrived there but I overheard your argument."
            m "I brought you guys here together because I want you guys to make up."
            hide a11
            show a1:
                xpos 0.53 ypos 0.21
                xzoom 1.25 yzoom 1.25
            a "Well why do you care?"
            hide b8
            show b1 at left:
                xpos 0.2 ypos 1.1
                xzoom 1.15 yzoom 1.15
            b "Yeah what stake do you have in our argument."
            "Well their relationship status is dependent on me escaping this time loop but I can't tell them that."
            m "Mia, even though we aren't as close as we used to be, I still can't bear to see you two argue for this long without making up."
            m "You guys are arguing for so long to the point that everyone is wondering if anything is alright."
            m "I hope that you guys can make up."
            m "Mia, aren't you mad at James for not opening up?"
            hide a1
            show a6:
                xpos 0.56 ypos 0.21
                xzoom 1.25 yzoom 1.25
            m "And James, don't you have something that you want to say to Mia?"
            hide b1
            show b4 at left:
                xpos 0.19 ypos 1.1
                xzoom 1.15 yzoom 1.15
            "Mia and James" "Wait what??" 
            "Mia and James" "How did you know that?"
            m "It's tough to explain but you guys have told me about it but you both probably don't remember."
            m "Anyways please do make up."
            a "...."
            b "...."
            hide a6
            show a4:
                xpos 0.55 ypos 0.21
                xzoom 1.25 yzoom 1.25
            a "I'm sorry James."
            a "I wanted to know why you were acting differently so I kept pestering you. I guess you were frustrated about that huh."
            hide b4
            show b6 at left:
                xpos 0.2 ypos 1.1
                xzoom 1.15 yzoom 1.15
            b "Mia....I'm sorry for not telling you how I really feel."
            b "The truth is, I feel like I'm way out of your league."
            b "After all, I'm only good at sports while you're good at academics."
            hide a4
            show a5:
                xpos 0.53 ypos 0.21
                xzoom 1.25 yzoom 1.25
            a "Hey that's not true! I appreciate you!"
            a "And I'm sorry for acting melodramatic sometimes."
            b "I'm sorry for acting very childish towards you."
            a "Wanna make up?"
            hide b6
            show b4 at left:
                xpos 0.19 ypos 1.1
                xzoom 1.15 yzoom 1.15
            b "Sure."
            "Mia and James embrace themselves in a hug."
            "Looks like I can quietly leave them."
            "I slip away from the park without disturbing them."
            jump intermission
        
        "Leave out of it":
            "I decided to stay put."
            "Me interrupting them may make it worse."
            a "Ohmygod I wish you weren't so insufferable childish!"
            b "I wish you weren't this annoying to deal with!"
            a "Me? Annoying? Oh boy, have you ever looked at a mirror?"
            a "Or even better, look at a dictionary for the definition of annoying?"
            b "Do I treat everything like it's the end of the world?"
            a "Ohmygod."
            b "Well I'm breaking up with you!"
            hide a1
            show a11:
                xpos 0.55 ypos 0.21
                xzoom 1.25 yzoom 1.25
            a "W-what."
            b "It's obvious that we'll be unhappy if we continue on like this."
            hide b1
            show b6 at left:
                xpos 0.2 ypos 1.1
                xzoom 1.15 yzoom 1.15
            b "We need to break up."
            a "J-james wait pleas-"
            b "I'm sorry Mia."
            hide b6 with easeoutleft
            "I hear footsteps walking."
            hide a11
            show a5:
                xpos 0.53 ypos 0.21
                xzoom 1.25 yzoom 1.25
            "Looks like James is serious about breaking up."
            "I can hear sobbing. Sounds like Mia."
            "I quietly leave the park to avoid alerting Mia of my presence."
            jump intermission
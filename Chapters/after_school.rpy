label after_school:
    # classroom bg
    "Finally school is over for the day."
    "Until I wake up again and relive this day again."
    "I really need to find a way to escape this loop."
    "I don't want to relive this day over and over again."
    "I pack up my belongings and head out to the school exit."
    # transition
    # outside school bg
    "I find a shaded area and stay under it for a while."
    "I want to talk to either James or Mia to try to fix their relationship."
    "After what seems like an eternity, Mia comes out from the entrance."
    "James comes out from the entrance shortly afterwards."
    "They didn't acknowledge each other's presence. Looks like they haven't talked after their fight in the cafeteria."
    menu:
        "Who do I talk to?"

        "Mia":
            # mia affection increases
            jump Mia


        "James":
            # james affection increases
            jump James

        

label Mia:
    "I approach Mia."
    "She isn't with her posse. Guess she didn't want to talk to them right now."
    "Makes it easier to approach her."
    if mia_cafe == False:
        m "Hey Mia."
        a "Oh it's you."
        "Mia flashes me a bright smile."
        a "Hi Miku, what do you need?"
        menu:
            "How's things going with you and James?":
                a "Uh….what do you mean? Are you living in your own world?"
                a "You did see us argue earlier didn't you?"
                m "Well yeah but I wanna know what happened."
                m "Aren't we friends? Don't friends tell each other what happens?"
                if james_cafe == True:
                    "I cringed internally at what I said. Can't believe I quoted James out of all people."
                "Mia let out a sigh. She looks irritated."
                "It's none of your business so piss off!"
                "Mia turned around and promptly stomped out of school."
                "Looks like I can't ask her that directly."
                return
                # jump to part where the game loops
    else:

        if breakup == True:
            "Mia has a melancholic expression on her face. Maybe it's because I suggested that she break up with James?"
        m "Hey Mia."
        a "Oh. Hey Mia. What do you need?"
        # Route branches based on what was done in cafe.
        if mia_cafe == True:
            m "Well have you thought about what I said just now?"
            a "I have."
            if making_up == True:
                a "I've been thinking about how to make up with him."
                a "Can you help me Miku?"
                a "I really don't know how."
                a "Besides, it's James's fault. He's the one who made me mad."
                m "Well you can start by not blaming him for everything."
            
            if breakup == True:
                a "I've been thinking about if it's worth it to break up with James."
                a "Can you help me Miku?"
                a "I'm not sure if it's a good idea in the first place."
                m "Well you can start by telling me why you even want to break up in the first place."

            a "...."
            a "Do you want to go somewhere together?"
            "I took this opportunity to tease Mia."
            m "This is unexpected. Don't tell me you're cheating on James with me."
            "This caught Mia off guard."
            a "Y-you idiot!"
            a "Ugh, why am I surrounded by idiots everywhere!"
            "I laughed quietly."
            "Mia gets really flustered when I pull off snarky comments. It's funny to do that to her once in a while."
            "Especially since we haven't talked much recently."
            a "{i}sigh{/i}"
            a "Alright let's go somewhere."
            a "Hmmm…how about the park? Does that sound good?"
            a "I'd be down to that."
            "Mia clasps her hands together loudly."
            "Alright to the park we go then!"
            "Mia swiftly walks to the school exit while I try to follow her from behind."
            m "Wait hold on!"
            jump mia_walk

label mia_walk:
    # park bg

    "After a 10 minute walk we finally arrived at a nearby park."
    "This is usually a hangout spot for couples or families on the weekends."
    "Seeing as school just ended around half an hour ago, there aren't a lot of people here other than highschool couples."
    "Personally I don't see the appeal of going to a park for a date, especially after school."
    "Then again, I'm not in a relationship so what do I know? Who knows, I might think going to the park with my S/O is the best thing ever if I have one."
    a "It's been a while since we hung out together. School has been hellish especially after the principal himself made me the model student for academics."
    a "It's torture being the best student in the school."
    a "It's nice to hang out with someone I'm old friends with."
    a "With that said, it's nice to hang out with someone that I've been friends with for a while now. It feels more nostalgic, like the world hasn't completely changed."

    menu:
        "What's going on with you and James?":
            # mia make up increases
            # lead up to bad end.
            jump mia_convo1
        "Then why did you ignore me?":
            # mia affection increases
            # lead up to mia end
            jump mia_convo2

label James:
    "I approach James."
    "He's talking loudly with his group of friends."
    "Sounds like they're talking about sports. Not that I care."
    b "Did you see the goal I made earlier? That's why I'm the be-"

    if james_cafe == False:
        m "Hey James!"
        "James stopped talking with his friends and looked at me."
        "He looked irritated after I interrupted him."
        b "Miku, arentcha? What do you want?"
        m "Well I wanna know what happened between you and Mia."
        "James let out a hearty laugh, followed by his friends."
        b "Aren't you friends with Mia? Why don't ya ask her instead?"
        m "Well we're not that close."
        b "Don't friends talk to each other about stuff? You should know since you're friends."
        m "As I've said we aren't that clos-"
        b "Just ask Mia since you two are friends and all."
        "It's not like being friends since we were children makes me eligible to ask her on her relationship problems."
        "Guy 1" "Oooh do you think she wants to take James for herself?"
        "Guy 2" "Hahaha she wants to take away James from Mia. That reminds me of an anime I wat-"
        "Guy 3" "Shut it Alex! Nobody wants to hear about whatever you watched."
        "I shut them a glare and they promptly stopped gossiping about me."
        b "Anyways I actually have stuff to do."
        b "Cya! Wouldn't wanna be ya!"
        m "But wait she didn-"
        "It was too late as he dashed past me with his friends following along."
        m "Wait James!"
        "He ignored me as he exited the school grounds."
        "Maybe I can talk with Mia instead?"
        "I look around for Mia but can't find her. Guess she went back home already."
        "Bummer."
        "Looks like there's no reason for me to stay in school. Time to go back home."

    else:
        m "Hey James!"
        "James stopped talking with his friends and looked at me."
        "He had a surprised expression on his face."
        b "Miku? What do ya want?"
        m "Didn't you say that you wanna talk to me later during recess?"
        b "I did?"
        "James thought for a second before he finally spoke up."
        b "Oh yeah you did. Didn't know you'd actually look for me."
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
        b "Do NOT talk about this to anyone you hear?"
        b "Or else you'll never be invited to gaming nights anymore."
        b "Oh and also you'll break the bro code."
        "His friends nod solemnly. Guess the threat of breaking the ‘bro code' is a serious offence."
        b "Alright Mia, follow me."
        "James rushed out of the school compound."
        m "Wait hold on!"
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
                jump james_convo1
            "Why are you two arguing?":
                # james make up increases
                jump james_convo2

label james_convo1:
    m " As I've said about a million times, we aren't that close. You should get that drilled into your thick skull."
    b "Yeah yeah I know. You keep repeating that. I'm curious about why exactly."
    m "Well I dunno, we just grew apart I guess."
    "James let out a loud laugh attracting nearby onlookers."
    "I cover my face in embarrassment."
    m "Did you really have to laugh that loud???"
    b "Hahahah…don't you two still text each other? Last I remembered you sent her a reel about some singer, what's her name?"
    b "Ah yea, Kagerman Ren or something like that."
    "This caught me off-guard. That was around 2 months ago when we did talk to each other."
    m "H-how did you know?"
    b "I've seen her texts before."
    m "That was about 2 months ago. How did you even remember that?"
    b "Your chats with her are pinned to the top of her chat messages. Well after her family and me at least."
    "I am dumb-founded. James knew?"
    m "She hasn't texted me in a while! Isn't that proof that we haven't talked in a while?"
    b "Hmmm...."
    "James looks lost in thought. I've never seen him think that deeply since year 6 in primary school during a maths test."
    b "Maybe she's embarrassed by you. After all, ever since she was chosen as the model student for academics, she was a popular sensation."
    b "And that talking to you would ruin her reputation so she slowly stopped talking to you until you both stopped talking."
    "That's unusually deep for James. I never knew he had a more serious side to him."
    m "That's….unusually deep for you James."
    "This time, instead of a hearty laugh, James let off a slight chuckle."
    b "Heh…the ‘me' everyone usually sees is just an act after all. Can't have the model student for extra-curriculars to seem smart."
    m "Then why'd you keep doing poorly in tests then?"
    b "Ah....that's because I'm not that good at studying."
    b "But after being with Mia my grades shot up! I'm no longer getting single digits!"
    "It's better than nothing at least."
    m "Wait, let's rewind for a second. If she didn't want to talk to me then why is my chats with her pinned to the top?"
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
    "While I was crying, I felt a hand on my shoulder."
    b "Hey Miku...."
    "I look up amidst sobs and see James with a soft smile on his face."
    b "Everything will be alright. It's fine to feel hurt."
    "I continue to cry. Tears gradually stopped falling down my face and eventually my cries became sobs."
    b "I wish I knew why she didn't want to talk to you. Alas I don't know the reason why and Mia won't tell me."
    "James lets off a slight chuckle."
    b "Truth to be told Miku, I had a crush on you during primary school."
    "Wait what?"
    "I looked up to James in surprise, not believing what I was hearing."
    m "Wh-what did you say?"
    b "Heh, guess I said that out too loud didn't I?"
    b "Well I had a crush on you in primary school. I remember that we were classmates in Year 6 and after laying my eyes on you, my heart skipped a beat."
    b "Guess it somehow persisted until now haha."
    "I'm speechless. I really don't know what to say."
    "I've never been in a situation where someone confesses their feelings towards me."
    "Much less someone who's in a committed relationship with someone I used to be close with."
    "This is an interesting situation to be in say the least."
    m "What about Mia? Does she know?"
    b "No she doesn't and she doesn't have to know."
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
    "James glances at his watch."
    b "Oh shoot I have to go now! Don't wanna be late."
    m "Late for what?"
    b "Personal stuff."
    b "Welp see ya in class tomorrow, Mia."
    m "Ah goodbye."
    "James heads off from the park."
    "I'm still recovering from the bombshell that was dropped on me."
    "James had a crush on me? Did he ever love Mia then? How did he hold on to this crush for this long?"
    "I decided to go back home as I don't feel like staying in the park any longer."

label james_convo2:
    b "Looks like you really don't know huh."
    b "Well me and Mia are arguing cause she couldn't handle me."
    "There's absolutely no way that is the reason why."
    m "There's gotta be something more than that."
    b "Like what exactly?"
    "Well this is the first time you two argued for this long. Most of the time your so-called “arguments” last at most a day and they're usually over petty matters."
    "An argument that lasts for this long means that something must have happened between you two."
    "James let out a loud laugh attracting nearby onlookers."
    "I cover my face in embarrassment."
    m "Did you really have to laugh that loud???"
    b "Well ya got me there."
    b "Yeah something did happen between us."
    "I'm curious about what happened. Resolving it might be the key to escaping this time loop."
    m "Well tell me what happened!"
    b "Alright fine. You being Mia's friend might help me."
    b "As you know, I'm not exactly all that good in academics."
    b "I somehow barely passed my tests and even then it's with Mia helping me a lot."
    b "The only thing that I'm good at are sports."
    b "However, I've been feeling that sports is the only thing that I'm ever gonna be good at."
    b "I can barely do maths, sciences confuse me to no end and history is very confusing."
    b "The only subjects I'm good at are the language subjects and even then it'd be pretty hard to fail in those."
    b "I just feel like I'm kinda insignificant compared to Mia. She's this academic weapon while I'm just a lowly student that's only good at kicking a ball around a field."
    "I'm rendered speechless. I didn't know that James had this side of him."
    m "Wow uh…didn't know you had this side to you, James."
    "He let out a small chuckle, a stark contrast to his loud laugh earlier."
    b "Heh....I don't really show this side of me to anyone."
    b "{size=-15}It also doesn't help that I have a crush on you.{/size}"
    m "What was that?"
    b "Hmm? Did I say anything?"
    "I swear I heard James say something."
    "Did he say he has a crush on me? I must be hearing things"
    "I brush those thoughts aside and focus on James now."
    m "Well did you ever talk to Mia about these feelings?"
    b "That's the thing, I didn't."
    b "And when she tries to ask what's happening, I panic and push her away."
    b "It's probably because she's always so overdramatic that I push her away all the time. I'm not really sure."
    b "I don't really know what to do."
    
    menu:
        "Best end":
            # best ending
            # obtainable if James and Mia's endings are obtained
            jump best_end_convo
        "I don't know what to do either":
            # leads to a loop
            'a'
            return
            # loop
        "What about breaking up with her?":
            # james affection increases
            jump james_convo3

label james_convo3:
    'a'
    return

label mia_convo1:
    a "O-oh getting straight to the point I see."
    a "Well...."
    a "You know how earlier I said that James is really immature?"
    a "Well, that isn’t the whole picture."
    a "Recently he’s becoming more different."
    m "Different? What do you mean by that?"
    a "He’s....acting different, like he’s frustrated about something."
    a "And if I try to ask about it he ignores the question."
    a "I don’t know what’s going on with him."

    menu:
        "Have you tried to sit down with him?":
            a "Well....not really."
            a "We did go on a date last week before we started to argue."
            a "The way he acted then really ticked me off."
            m "Didn’t he book a reservation at Burger King or something like that?"
            a "Wait, how did you know that?"
            m "Well....you two were arguing pretty loudly during recess."
            a "Oh my god, as if my reputation couldn’t get any more worse."
            "Mia covers her face in her hands in embarrassment. Guess clarity finally hit her head on."

            menu:
                "Hey it’s not all that bad! You’ll be even more popular now!":
                    # mia affection decreases
                    call mia_joke
                "These things happen. It’s alright.":
                    call mia_unjoke


    m "...."
    m "We lost track of what we’re originally talking about."
    a "Ah yeah, about me and James...."
    "Silence falls between us."
    "It’s starting to feel awkward now so I decided to break the silence to make it less awkward."
    m "So...."
    m "What happened next?"
    a "Well I’d say it’s less of ‘what happened next’ and more of ‘what happened before’."
    a "After the Burger King incident I felt that something snapped within me."
    a "I felt that all of his immature actions went from annoying but endearing to irritating."
    a "So that’s how we argued and argued and argued."
    m "Well this is the first time it lasted for weeks so it’s quite a surprise."
    m "It has never happened before."

label mia_convo2:
    'a'

label mia_joke:
    a "Ohmygod Miku please stop joking! This is serious!"
    m "Sorry. It was a bad time to joke."
    "Not like she has the right to complain since she stopped talking to me."

label mia_unjoke:
    a "That doesn’t change the fact that it happened."
    a "Everyone’s gonna make fun of me."
    m "Hey that’s not true! In fact everyone is curious about what happened!"
    a "And how would you know that?"
    a " I’m sorry to say this but you don’t really talk to many people. How would you know what they’re thinking about?"
    m 'H-hey! What’s that supposed to mean!'
    a "My point is that what do you know about what others think when you don’t really talk to others?"
    "The audacity."

label best_end_convo:
    'a'
    return
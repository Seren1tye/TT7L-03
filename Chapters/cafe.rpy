label cafeteria:
    scene cafe with Fade(1.0, 1.0, 1.0)
    "It's time for recess."
    "Mia and James are going to argue soon."
    "There's no use trying to interrupt them then so I might as well wait until they finish arguing."
    "I'll have to find somewhere to sit so that I can talk to either Mia or James once they finish arguing."
    "I didn't bother packing food from home to eat for recess."
    "I'm too lazy to make a new dish for recess after the fourth or fifth loop."
    "It's too much effort."
    $ food = renpy.random.choice(['sandwich', 'wrap', 'packet of nuggets', 'packet of fries'])
    "I head to the stalls and order a [food] from the western stall."
    "I'm not really that hungry to eat something heavier."
    "As I headed towards the cafeteria tables, I could hear the ever-so familiar argument by none other than the star couple."
    a "Why are you so insufferable? I asked you a simple question and you decide to twist it into fourteen different ones."
    b "How is it my fault? You're the one who can't word it simply. Always using words that confuse me and then blame me when I don't understand what you meant in the first place."
    show a1 at right:
        ypos 1.05
    show b1 at right:
        xpos 0.7 ypos 1.05
        xzoom 0.9 yzoom 0.9
    a "Can't you just take responsibility for once. You juuust love to blame me for everything in your life!"
    b "Well it wasn't my idea in the first place to ignore the messages and calls from the person you're dating!"
    "They're arguing again."
    menu:
        "Where should I sit?"
        "Sit at the table near Mia and James":
            # mia affection increases
            $ mia_cafe = True
            jump cafe_table
        "Go to a quiet corner":
            jump corner
        "Wander around the school":
            # james affection increases
            jump wander
        

label cafe_table:
    scene cafe with dissolve
    "I decided to sit 4 tables away from them."
    "Mia approaches me whenever I sit here."
    "I tuned out to their argument, it became white noise a while ago."
    "As I was busy eating my [food] I felt someone tapping on my shoulder."
    show a8 at center with dissolve:
        ypos 1.015
    "It's Mia."
    hide a8
    show a9 at center:
        xpos 0.4999 ypos 1.02
    a "Hey Miku? Can I sit here?"
    m "Sure, go ahead."
    show a9 at center:
        xpos 0.4999 ypos 1.02
        xzoom 1.25 yzoom 1.25
    "Mia sat next to me. She had a solemn expression on her face."
    a "Heh....it's been a while since we talked like this."
    a "A heart-to-heart conversation."
    "Technically we talked like this somewhat recently but I stayed silent."
    "In her perspective we don't really talk all too often while I've seen her talk about this issue a few times at this point."
    if confront == True:
        # mia affection increases
        hide a9
        show a8 at center:
            xpos 0.507 ypos 1.02
            xzoom 1.25 yzoom 1.25
        a "I'm sorry about lashing out earlier."
        a "I was so caught in the moment that I accidentally yelled at you."
        m "It's fine no offence taken."
    m "Anyways what happened between you two?"
    hide a8
    show a9 at center:
        xpos 0.4999 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "Well as you know James is very immature."
    m "It feels like he's a 9 year old at heart."
    hide a9
    show a10 at center:
        ypos 1.03
        xzoom 1.27 yzoom 1.27
    a "Hahaha...."
    hide a10
    show a9 at center:
        xpos 0.4999 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "It usually pisses me off a lot but recently I feel like it's even more irritating."
    a "I know he's been quite childish always and while it annoys me a lot."
    a "I could tolerate it."
    hide a9
    show a6 at center:
        xpos 0.5095 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "{size=-10}I also find it hot.{/size}"
    hide a6
    show a9 at center:
        xpos 0.4999 ypos 1.02
        xzoom 1.25 yzoom 1.25
    a "But like I've said I feel that he's more irritating now."
    a "I don't know what to do."
    
    menu:
        "Have you considered making up with him?":
            $ making_up = True
            # mia affection increases
            # mia makes up increases
            hide a9
            show a3 at center:
                ypos 1.02
                xzoom 1.25 yzoom 1.25
            a "...."
            a "Yes, I have...."
            a "But I don't...."
            hide a3
            show a6 at center:
                xpos 0.5095 ypos 1.02
                xzoom 1.25 yzoom 1.25
            "Mia looks away."
            a "Nevermind...."
            m "What is it?"
            a "No-nothing!"
            a "Ugh why would I have to apologise? He's the one who started this,not me."
            m "I never said anything about apologising?"
            hide a6
            show a11 at center:
                xpos 0.5034 ypos 1.02
                xzoom 1.25 yzoom 1.25
            a "Eh?"
            hide a11
            show a6 at center:
                xpos 0.5095 ypos 1.02
                xzoom 1.25 yzoom 1.25
            "Mia turned red as a tomato."
            a "I....I...."
            a "This is the worst day of my life."
            "I gave a slight chuckle."
            m "Well you should try to resolve your issues with him."
            m "After all, isn't love about giving it your all to the person you love?"
            m " And that means by making up with him, you're showing him that you're giving him your all."
            "Truth to be told, I have no idea what I'm saying."
            "I'm just basing things off from a romance anime I once watched."
            "Mia doesn't need to know that though."
            a "I-I'll keep that in mind."
            # bell sfx
            hide a6
            show a11 at center:
                xpos 0.5034 ypos 1.02
                xzoom 1.25 yzoom 1.25
            "Looks like recess is over now. Better head back to class."
            m "I'll see you in class Mia."
            a "Oh....alright then."
            "She rises up from the table and walks briskly to the entrance."
            show a11 at offscreenright with easeinright
            "I follow suit in order to not be late for class."
            jump after_school
        "Have you considered breaking up with him?":
            $ breakup = True
            # mia affection increases
            a "...."
            a "Wait what????"
            m "Well it's obvious that you both aren't made for each other."
            m "After all you two have been arguing with each other for about a week now. Maybe even more."
            m "Don't you think it's gone on long enough?"
            "I hate to do this but after seeing them argue after this long I don't think they exactly have a healthy relationship."
            "Besides, it looks like it wouldn't work out for them in the long run."
            a "Miku, what are you saying???"
            a "I can't break up with him! I still love him! Love him lots and lots! I'd literally die if I broke up with him."
            m "Are you really sure that you love him?"
            m "After all it's been a week since you two started arguing. If you really loved him you would have made up by now."
            a "I...."
            "Mia fell silent."
            m "Well I'm just saying what I think. It's up to you if you want to listen to me."
            # bell sfx
            "Looks like recess is over now. Better head back to class."
            m "Well I'll see you in class Mia."
            "Mia didn't respond. Looks like she's pondering on what I said to her."
            "I head back towards the classroom so I won't be late to class."
            jump after_school


label corner:
    scene cafe with dissolve 
    "I decided to go somewhere quieter."
    "I find a relatively quiet corner and sit down there."
    "There's only 3 students around and they're a few tables away from where I'm sitting."
    "Recess did just start recently so the cafeteria isn't crowded yet."
    "Maybe James will come here after he finishes arguing with Mia?"
    "Come to think of it, I never saw where he went after they argued."
    "I never really paid attention to where he went off too afterwards."
    "As I ate my [food] in silence, people started to fill up the empty seats."
    "I haven't seen either Mia or James head towards this corner."
    # bell sfx
    "Looks like recess is over."
    "Neither James nor Mia came here."
    "Looks like I have to find another spot to find either one of them."
    "I head back towards the classroom so I won't be late to class."
    jump after_school

label wander:
    "I decided to wander around the school compound."
    scene school2 with dissolve
    "Well wherever that I can wander during recess time."
    "There isn't much space to wander around anyways."
    "I don't want the school prefects to report me on trespassing to Miss Low."
    "???" "Hey Miku!"
    "I hear someone call my name so I turn around and promptly see one of my friends."
    m "Oh hey Sab what are you doing?"
    "Sab" "I'm doing fine. How about you?"
    show b3 at left:
        ypos 1.05
        xzoom 0.8 yzoom 0.8
    "As I was talking to my friend, I saw James exit the cafeteria."
    hide b3 with dissolve
    m "Sorry Sab I gotta go!"
    "Sab" "Wait Miku-"
    "I left my friend behind as I trailed James."
    scene school2
    "He was heading towards the men's restroom."
    "I decided to wait outside since I obviously can't enter."
    "I look around me and see people giving me weird looks."
    "Oh wait. I'm a girl waiting directly outside the men's restroom."
    "Frantically, I left the area trying to not look like I'm a pervert. Hopefully nobody reports me as one to the prefects."
    show b6 at center with dissolve:
        ypos 1.05
    b "I wish I knew what went wrong."
    "I hear James speak as he exits the restroom."
    "I turn around and see him lost in thought. Looks like he was talking to himself."
    "He turned to my direction and started walking before he noticed me."
    m "Ah!"
    hide b6
    show b8 at center:
        xpos 0.486 ypos 1.05
    "James was shocked."
    b "Aren't you Mia?"
    b "What are you doing here?"
    m "Nothing I swear!!"
    "I frantically wave my hands to hide the embarrassment."
    hide b8
    show b2 at center:
        xpos 0.489 ypos 1.05
    b "Well in case you couldn't read this is the BOYS RESTROOM."
    m "Yeah I can read. I'm actually surprised that you can even read."
    b "Hey! Reading isn't hard! Besides I'm 17."
    menu:
        "You're 17? I thought you were 6.":
            hide b2
            show b1 at center:
                xpos 0.489 ypos 1.05
            "Guess this must have ticked James off as he was mad as a hornet's nest"
            b "I know you're Mia's friend and all that but c'mon!"
            b "Do you trade insults with each other?"
            m 'You overestimate how close we actually are.'
            b "You're going behind my back with my girl?"
            m "What?? No, what made you think of that?"
            b "Well you said that I overestimated how close you two are so I thought you were dating Mia."
            "I let out a sigh. He's good at sports and only sports. Intelligence isn't exactly one of his strengths."
            m "Anyways...."
        "....":
            hide b2
            show b3 at center:
                xpos 0.499 ypos 1.058
            b "Hmm."
            b "Well if you have nothing to say then I'll be going now."
            m "Ah wait!"
            hide b3
            show b8 at center:
                xpos 0.486 ypos 1.05
            "James looks back with a puzzled look."
            b "Hmm? What is it?"
        
    m "What were you talking about just now?"
    hide b1
    show b8 at center:
        xpos 0.486 ypos 1.05
    b "W-what do you mean?"
    m "You said you wondered what went wrong."
    hide b8
    show b4 at center:
        xpos 0.486 ypos 1.05
    b "No I didn't."
    m "Yes you did."
    b "Oh yeah? What's your proof."

    menu:
        "I literally heard you say it out loud.":
            # james affection increases
            $ james_cafe = True
            hide b4
            show b6 at center:
                ypos 1.05
            b "Damn it."
            b "Well ya got me. We have relationship issues. That's what you wanted to know right? Well there ya go."
            "Very descriptive. He never fails to piss me off."
            m "Well there's gotta be more than that."
            m "Give me the deets."
            hide b6
            show b2 at center:
                xpos 0.489 ypos 1.05
            "I cringed so hard at that sentence."
            b "Never say that again. You sound like a middle-aged woman trying to sound ‘hip and cool' with the kids."
            b "What makes me think I can trust you with this? You won't tell Mia won't you?"
            m "Why will I ever need to tell her this?"
            hide b2
            show b4 at center:
                xpos 0.486 ypos 1.05
            b "Because....I don't know you're friends. Don't friends tell each other everything in their lives or whatever is it you girls do?"
            m "Again, you’re thinking too highly of our friendship. We aren’t even that close nowadays. You should learn more about friendships."
            hide b6
            show b2 at center:
                xpos 0.489 ypos 1.05
            b "Says the one who usually sits alone every time."
            "Fair point but this guy really gets on my nerves."
            m "At least I'm not-"
            # bell sfx
            hide b2
            show b8 at center:
                xpos 0.486 ypos 1.05
            b "Well looks like recess is over. See ya wouldn't wanna be ya!"
            scene school2
            show b8 at center:
                xpos 0.486 ypos 1.05
            show b8 at offscreenright with easeinright
            "James dashed off in a hurry."
            m "Hey!"
            "I rushed back towards the classroom so I won't be late to class."
            jump after_school
        
        "I made it up":
            b "Well I thought so."
            b "You should get your head checked."
            b "Cya wouldn't wanna be ya!"
            "James dashed off to the distance."
            m "Hey!"
            "It's too late as he's too far away to hear me."
            "I decide to loiter around waiting for the bell to ring as I have nothing to do. It's not like I have enough time to talk to Mia anyways."
            # Bell sfx
            "Looks like recess is over."
            "I head back towards the classroom so I won't be late to class."
            jump after_school
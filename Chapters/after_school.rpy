label after_school:
    # classroom bg
    "Finally school is over for the day."
    "Until I wake up again and relive this day again."
    "I really need to find a way to escape this loop."
    "I don’t want to relive this day over and over again."
    "I pack up my belongings and head out to the school exit."
    # transition
    # outside school bg
    "I find a shaded area and stay under it for a while."
    "I want to talk to either James or Mia to try to fix their relationship."
    "After what seems like an eternity, Mia comes out from the entrance."
    "James comes out from the entrance shortly afterwards."
    "They didn’t acknowledge each other’s presence. Looks like they haven’t talked after their fight in the cafeteria."
    menu:
        "Who do I talk to?"

        "Mia":
            jump Mia


        "James":
            jump James

        

label Mia:
    "I approach Mia."
    "She isn’t with her posse. Guess she didn’t want to talk to them right now."
    "Makes it easier to approach her."
    if breakup == True:
        "Mia has a melancholic expression on her face. Maybe it’s because I suggested that she break up with James?"
    m "Hey Mia."
    a "Oh. Hey Mia. What do you need?"
    # Route branches based on what was done in cafe.
    if mia_cafe == True:
        m "Well have you thought about what I said just now?"
        a "I have."
        if making_up == True:
            a "I’ve been thinking about how to make up with him."
            a "Can you help me Miku?"
            a "I really don’t know how."
            a "Besides, it's James’s fault. He’s the one who made me mad."
            m "Well you can start by not blaming him for everything."
        
        if breakup == True:
            a "I’ve been thinking about if it’s worth it to break up with James."
            a "Can you help me Miku?"
            a "I’m not sure if it’s a good idea in the first place."
            m "Well you can start by telling me why you even want to break up in the first place."

        a "...."
        a "Do you want to go somewhere together?"
        menu:
            "Yes":
                jump mia_walk


label James:
    'a'





label mia_walk:
    a "Hmmm how about the park? Does that sound good?"
    m "Alright sure."
    m "Although you’re ignoring what I sai-"
    "Mia clasps her hands together loudly, interrupting me."
    a "Alright to the park we go then!"
    "Mia swiftly walks to the school exit while I try to follow her from behind."
    m "Wait hold on!"

    # park bg

    "After a 10 minute walk"
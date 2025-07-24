label chapter_0_tsukuneDrive:
    play music "music/scene4.ogg"
    scene bg_car_passenger

    tsukune "Thanks for driving me home. It's much more convenient than getting a cab."

    alex "And you know for a fact that someone didn't vomit where you're sitting!"

    tsukune "Wait, huh?"

    alex "{i}Shit, I think I said something weird!{/i}" with hpunch

    alex "O-oh, it's just- You know how sometimes people throw up in taxis because someone get super drunk?"
    alex "Well, I don't drive anyone around, so this car is cleaner than clean!"

    #show tsukune laugh
    tsukune "Oh, that makes sense! You're totally right, it'd suck to sit around vomit stains."

    alex "See, you get me! This is why you're cool."

    menu:
        "What should I talk about?"

        "Check in with Tsukune":
            jump drive_conversation_tsukuneTherapy

        "Talk about your new neighbor":
            jump drive_conversation_claudiaMoveIn
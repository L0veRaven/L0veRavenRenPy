label chapter_0_tsukuneDrive:
    play music "music/scene4.ogg"
    pause 1.0
    play sound "sfx/carDoor_close.mp3"
    pause 1.0
    play sound "sfx/carDrive_start.mp3"
    pause 4.0
    scene bg_car_passenger with Dissolve(2.0)

    tsukune "Thanks for driving me home. It's much more convenient than taking the bus."

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
            jump chapter_0_tsukuneTherapy

        "Talk about your new neighbor":
            jump chapter_0_conversationClaudia
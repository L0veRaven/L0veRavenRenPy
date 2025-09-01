label c0_tsukuneTherapy:
    $ lovePoints_Tsukune+=20
    ##Increase Tsukune love points by 20

    alex "So Tsukune, I'm gonna be real for a second. How are you doing lately? Like, how are you {b}{i}actually{/b}{/i} doing?"

    hide tsukune_neutral
    show tsukune_blush:
        xpos 0.65
    tsukune "Oh... damn, it's been a while since someone checked in with me... That's nice of you."

    hide tsukune_blush
    show tsukune_neutral:
        xpos 0.65
    tsukune "But I've really been doing well. Actually, I think I've been doing a {i}{b}lot{/b}{/i} better lately. I'm not even sure if people can even tell, but I can definitely feel it."

    alex "What do you mean?"

    hide tsukune_neutral
    show tsukune_blush:
        xpos 0.65
    tsukune "Well... Geez it's kind of embarassing to admit it, but I've finally started seeing a therapist."

    hide tsukune_blush
    show tsukune_neutral:
        xpos 0.65
    tsukune "I know it's not for everybody, but I've been more level-headed. Normally it's super easy for me to get stuck into self-loathing loops in my head."

    # hide tsukune_neutral
    ## TODO: show tsukune_smile
    tsukune "Now, I'm showing a lot more compassion to myself."

    ## [Question 1] Tsukune Therapy
    menu:
        "That sounds like bullshit.":
            jump c0_tsukuneTherapy_a

        "I'm glad it's working out for you!":
            jump c0_tsukuneTherapy_b

        "Do you think I need therapy?":
            jump c0_tsukuneTherapy_c
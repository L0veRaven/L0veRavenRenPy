label chapter_0_tsukuneTherapy:
    $ lovePoints_Tsukune+=20 #Increase Tsukune love points by 20

    alex "So Tsukune, I'm gonna be real for a second. How are you doing lately? Like, how are you {b}{i}actually{/b}{/i} doing?"

    tsukune "Oh... damn, it's been a while since someone checked in with me... That's nice of you."
    tsukune "But I've really been doing well. Actually, I think I've been doing a {i}{b}lot{/b}{/i} better lately. I'm not even sure if people can even tell, but I can definitely feel it."

    alex "What do you mean?"

    tsukune """
    Well... Geez it's kind of embarassing to admit it, but I've finally started seeing a therapist.

    I know it's not for everybody, but I've been more level-headed. Normally it's super easy for me to get stuck into self-loathing loops in my head.

    Now, I'm showing a lot more compassion to myself.
    """

    ## [Question 1] Tsukune Therapy
    menu:
        "That sounds like bullshit.":
            jump chapter_0_tsukuneTherapy_a

        "I'm glad it's working out for you!":
            jump chapter_0_tsukuneTherapy_b

        "Do you think I need therapy?":
            jump chapter_0_tsukuneTherapy_c
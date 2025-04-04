label journal_1_1:

    scene black with Dissolve(2.0)

    "{i}I never knew that feeling love could be... so...{/i}"

    "{sc=5}{b}{i}I n t o x i c a t i n g .{/i}{/b}{/sc}"

    "{i}Maybe journaling will help ease my mind...{/i}"
    
    play music "audio/music/scene5.ogg"

    scene bg_work_desk with Dissolve(2.0)

    $ persistent.quickmenu_a = False
    $ persistent.quickmenu_b = True
    $ persistent.quick_menu_display = False

    journal """
    It's been a month since I've started journaling and I think I'm coming to terms with some of my feelings.{nw}
    
    It's hard trying to understand them to be honest, but one thing's been stuck on my mind for a couple of days now.{nw}

    I have a neighbor. Her name is Claudia, and she is... so hard to describe. I mean, she's perfect to me, but there's not a way to really explain it.{w=0.5}
    """
    
    nvl clear

    ## Choice: Hard or Easy mode
    menu:
        "Claudia moved in a week ago... (Hard)":
            jump journal_1a

        "I've known Claudia for a while... (Easy)":
            jump journal_1b

label journal_1a:
    ## Claudia Love: +10
    $ current_love_Claudia+=10

    ## Game Mode: Hard
    $ persistent.hard_mode = True
    $ persistent.easy_mode = False

    journal """
    To be fair, she's only been living at my apartment complex for a week.{w=0.5}
    
    {clear}

    But... whenever I get a glimpse of her, my heart pounds in a way I've never felt before.{w=0.5}
    """

    nvl clear
    
    jump journal_1_2

label journal_1b:
    ## Game Mode: Easy
    $ persistent.hard_mode = False
    $ persistent.easy_mode = True

    journal """
    She's been living at my apartment complex for a while now. I'm on good terms with her. We're more like acquaintances, but it's better than nothing.{nw}

    If only you could feel how she makes my heart race whenever I see her.{w=0.5}
    """

    nvl clear
    
    jump journal_1_2

label journal_1_2:

    scene bg_claudia_trash_0 with fade

    scene bg_claudia_trash_1 with Dissolve(1.0)

    scene bg_claudia_trash_1_zoom with Dissolve(1.0)

    journal """
    I've been taking pictures because it's so hard to take my eyes off her. It's far less creepy to look at photos of her rather than staring at her in public.{nw}

    I'll tape them in this journal so they aren't loose and get scratched up, but if you were a person, I feel like you'd appreciate her beauty, too.{nw}

    It's more than her looks, though. Her mannerisms... The way she tucks her hair behind her ear... The way she ties up her hair...{w=0.5}
    """

    nvl clear

    scene bg_claudia_apartment_curtains_closed with Dissolve(2.0)

    journal """
    I hate to admit that I've been trying to get photos of her during her more... private moments. It's hard to resist the temptation. That's not to say I haven't tried.{nw}

    It's so hard to get a moment like that. With her curtains open, she never shows anything private. She values her privacy, but where does that leave me?{nw}
    
    I may be overreacting, but to see someone in their most vulnerable state... It's such a high honor.{w=0.5}

    {clear}
    
    If I'm able to see her in one of those moments before I'm lucky enough to hopefully experience the real deal...{w=0.5}
    """

    nvl clear

    scene black with Dissolve(2.0)
    
    stop music

    you "Then I can prepare for when it {sc=3}{b}D O E S{/b}{/sc} happen."

    jump chapter_0_1
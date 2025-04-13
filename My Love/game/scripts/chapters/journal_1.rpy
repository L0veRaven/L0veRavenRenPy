label journal_1_1:

    scene black with Dissolve(2.0)

    "{i}I never knew that feeling love could be... so...{/i}"

    "{sc=5}{b}{i}I n t o x i c a t i n g . . .{/i}{/b}{/sc}"

    "{i}Maybe journaling will help ease my mind...{/i}"
    
    play music "audio/music/scene5.ogg"

    scene bg_work_desk with Dissolve(2.0)

    $ persistent.quickmenu_a = False
    $ persistent.quickmenu_b = True
    $ persistent.quick_menu_display = True

    journal """
    June 12th, 20XX\n{nw}
    
    It's so hard to get any work done right now. It honestly bugs me that I can't focus on anything other than my neighbor, Claudia. She can't get out of my head, but I don't exactly want her to.{nw}

    I've been working with my therapist on learning to identify my feelings. It's honestly very difficult for me to know what I feel because of how bad my depression is. It clouds my mind and makes it harder to navigate my life.{w=0.5}

    {clear}
    
    Somehow, even though I've been struggling with this for years, Claudia managed to give me feelings so clear that I'd be a fool to not know what it is:{w=0.5}
    
    Love{w=0.5}
    """
    
    nvl clear

    ## Choice: Hard or Easy mode
    menu:
        "Claudia moved in a week ago... (Hard)":
            jump journal_1a

        "I've known Claudia for a while already... (Easy)":
            jump journal_1b

label journal_1a:
    ## Game Mode: Hard

    journal """
    She hasn't lived here for long. I think it's only been about a week since she moved in, but even then, she is so mesmerizing!{w=0.5}

    Every time I get a glimpse of her, my heart pounds in a way I've never felt before, especially so soon after meeting someone.{w=0.5}
    """

    nvl clear
    
    jump journal_1_2

## Game Mode: Easy
label journal_1b:
    ## Claudia Love: Add 25 points
    $ current_love_Claudia+=25

    journal """
    She's been living at my apartment complex for a while now. We're on good terms with each other, which makes talking to her a lot easier. Sure, we're more like acquaintances, but it's still enough to make me fall for her.{nw}

    Every time I get a glimpse of her, my heart pounds in a way I've never felt before, especially so soon after meeting someone.{w=0.5}
    """

    nvl clear
    
    jump journal_1_2

label journal_1_2:

    scene bg_claudia_trash_0 with fade

    scene bg_claudia_trash_1 with Dissolve(1.0)

    scene bg_claudia_trash_1_zoom with Dissolve(1.0)

    journal """
    I've been taking pictures of her whenever I get the chance. It's nice to keep photos of the things I care about. Besides, it's far less weird to look at photos of her rather than staring at her in public.{nw}

    I took a couple of photos while she was taking out trash today. She sure did seem tired. It's probably because she was working late last night, poor thing.{nw}

    It's more than her looks, though. Her mannerisms... The way she tucks her hair behind her ear... The way she ties up her hair... Even the way she talks is {i}magnetizing{/i}.{w=0.5}
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
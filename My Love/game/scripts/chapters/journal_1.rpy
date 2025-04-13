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

    scene bg_claudia_trash_0 with Dissolve(1.0)

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
    I want to know what her daily routine is like. Unfortunately, it's not that easy. She lives directly next to me, so I can't really take photos when I'm so close.{nw}

    It'd also be really weird if I just sat outside her apartment, waiting for her to leave or to see who comes by to visit. Sure, I can peek through the blinds or look through my open window, but I'd probably look very suspicious doing that.{nw}
    
    I'm ashamed to admit that I'm too nervous to approach her. It would be much easier to talk to her rather than doing complicated bullshit to learn more about her.{w=0.5}
    """

    nvl clear

    scene black with Dissolve(2.0)
    
    stop music

    you "Hopefully... I can finally get to know her more."

    jump chapter_0_1
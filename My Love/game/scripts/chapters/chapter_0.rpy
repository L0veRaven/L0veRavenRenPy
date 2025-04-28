## [START] Journal Entry: Alex - Intro
label chapter_0_start:
    scene black with Pause(2.0)

    claudiaUnknown "Thanks for helping me move everything in Toby, I appreciate it so much!"

    play sound "sfx/sfx-door-lock2.mp3"

    pause 2.0

    $ persistent.quick_menu_display = True
    show claudia neutral with Dissolve (1.0)

    pause 1.0

    alex """
    {i}I never knew that feeling love could be... so...{/i}

    {sc=3}{b}{i}I n t o x i c a t i n g . . .{/i}{/b}{/sc}
    """

    hide claudia neutral with Dissolve (1.0)

    pause 1.0

    alex "{i}Maybe journaling will help ease my mind...{/i}"
    
    play music "audio/music/scene5.ogg"

    scene bg_work_desk with Dissolve(2.0)

    alexJournal """
    June 12th, 20XX{nw}
    
    \nIt sucks being at work. It's not the work that's even challenging. My brain 
    just won't shut up about Claudia, my neighbor. It's not that I don't want to 
    acknowledge that she exists, but I have work to do!{nw}

    \nMaybe I should think about this from a different angle...{nw}

    \nI've been working on learning to identify my feelings, and that's really hard 
    when you have depression. The way that my depression clouds my mind and emotions, 
    it makes it so much harder to know what I'm feeling, or even how to go about my life.{w=0.5}
    """

    nvl clear

    alexJournal """
    It's not just about my depression, though. Claudia genuinely takes up so much of my mind.{nw}

    \nOddly enough, even though I've been struggling with this for years, Claudia managed to 
    give me feelings so clear that I'd be a fool to not know what it is:{nw}
    
    \n{sc=2}Love{/sc}
    
    \nClaudia hasn't lived here long. I think it's only been about a week since she 
    moved in? I know many people would say \"It's too soon for you to fall in love!\" 
    but I don't think they know how mesmerizing she is!{nw}
    
    \nEvery time I get a glimpse of her, my heart pounds in a way I've {sc=2}never{/sc} felt 
    before...{w=0.5}
    """

    nvl clear

    scene bg_claudia_polaroids_desk with Dissolve(1.0)
    with Pause(0.5)

    alexJournal """
    I've been taking pictures of her whenever I get the chance. It's nice to keep photos 
    of the things I care about. Besides, it's far less weird to look at photos of her 
    rather than staring at her in public.{nw}

    \nI took a couple of photos while she was taking out trash today. She sure did seem 
    tired. It's probably because she was working late last night, poor thing.{nw}

    \nIt's more than her looks, though. Her mannerisms... The way she tucks her hair behind 
    her ear... The way she ties up her hair... Even the way she talks is {sc=2}magnetizing{/sc}.{w=0.5}
    """

    nvl clear

    scene bg_claudia_apartment_curtains_closed with Dissolve(2.0)

    alexJournal """
    I want to know what her daily routine is like. Unfortunately, it's not that easy. 
    She lives directly next to me, so I can't really take photos when I'm so close.{nw}

    \nIt'd also be really weird if I just sat outside her apartment, waiting for her to leave 
    or to see who comes by to visit. Sure, I can peek through the blinds or look through my 
    open window, but I'd probably look very suspicious doing that.{nw}
    
    \nI'm ashamed to admit that I'm too nervous to approach her. It would be much easier to 
    talk to her rather than doing complicated bullshit to learn more about her.{w=0.5}
    """

    nvl clear

    scene black with Dissolve(2.0)
    
    stop music

    alex "I swear... I need to be with her {sc=3}{b}s o . . . b a d . . .{/b}{/sc}"

    jump label chapter_0_meetTsukune
    
## Office: Meeting Tsukune
label chapter_0_meetTsukune:
    play music "audio/music/scene3.ogg"

    scene bg_office with Dissolve(2.0)

    tsukuneUnknown "Hey Alex!"

    show tsukune neutral:
        xpos 1.0 #Start off-screen to the right
        ease 0.75 xpos 0.0 ypos 0.0 #Ease -> center to Y axis
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up

    tsukune "What're you working on there?"

    alex "O-oh, nothing much. I'm just... journaling a little bit." with hpunch

    show tsukune neutral:
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up
        
    tsukune "\*chuckles\* I mean, what else are you gonna do during downtime?"

    show tsukune neutral:
        ease 1.0 xpos 0.15 #Slide to the right

    tsukune "Now that I think about it, I need to check in with Ash about the 
    spreadsheet xe was supposed to send in..."

    alex "Right..."

    show tsukune neutral:
        ease 0.5 xpos 0.0 #Slide to center

    tsukune "Oh, when we get off work, I wanna tell you about someone I met."

    alex "Someone you met?"

    show tsukune neutral:
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up

    tsukune "Yeah! See, I met a girl at this coffee shop the other day."

    show tsukune blush:
        ease 1.0 xpos 0.05 #Slide to the right

    tsukune "To be honest, she's kinda cute. I was lucky enough to get her socials."

    alex "Geez, I wish I was lucky enough to get that from my crush..."

    show tsukune neutral:
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up
    
    tsukune "Don't worry. I'm sure you'll get there soon enough."

    show tsukune neutral:
        ease 1.0 xpos 0.1 #Slide to the right
    
    tsukune "Anyways, I gotta get back to work. Talk more later!"

    show tsukune neutral:
        ease 1.0 xpos 1.0 #Slide off-screen to the right

    hide tsukune with dissolve

    alex "The closest I get with my crush is talking to her since she's my neighbor..."

    alex "Oh well, back to work."

    scene black with fade

    ## TODO: play sound typing

    alex "Oh, it's time to clock out."

    ## TODO: play sound car-door-close

    jump chapter_0_tsukuneDrive

## START: Tsukune Drive
label chapter_0_tsukuneDrive:
    scene bg_car_passenger with fade

    tsukune "Thanks for driving me, again."

    alex "It's no problem. Besides, I drive past your place on the way home, so it's not 
    like it takes any time away from me."

    tsukune "I guess you're right. It just sucks to have my car in the shop for over a week. 
    They said it'd only be a few days."

    alex "Have they called yet about what's going on with it?"

    tsukune "The shop called during my lunch break. I should be able to pick it up tomorrow, hopefully."

    scene bg_car_driver with dissolve

    ## Tsukune opens up about therapy
    tsukune "You know, I think I've noticed something about myself. I think I've been doing a lot better lately. I'm not even sure if people can even tell, but I can definitely feel it."

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

## [Answer 1a] Therapy is bullshit
label chapter_0_tsukuneTherapy_a:
    alex ""

    tsukune ""

    alex ""

    jump chapter_0_tsukuneDrive_claudiaTalk

## [Answer 1b] Happy for Tsukune
label chapter_0_tsukuneTherapy_b:
    alex ""
    
    tsukune ""
    
    alex ""

    jump chapter_0_tsukuneDrive_claudiaTalk

## [Answer 1c] Alex needs therapy
label chapter_0_tsukuneTherapy_c:
    alex ""
    
    tsukune ""
    
    alex ""

    jump chapter_0_tsukuneDrive_claudiaTalk

## START: Tsukune Drive - Claudia Talk
label chapter_0_tsukuneDrive_claudiaTalk:
    tsukune "So, remember the girl I was telling you about earlier?"

    alex "The coffee shop girl?"

    tsukune "Her name is Claudia. She's really nice."

    alex "{i}Claudia... No, there's no way that he's talking about the same Claudia...{/i}"

    alex "{i}... Right?{/i}"

    tsukune "She's really pretty and I figured that we could start off with just talking."

    alex "Do you have a picture of her?"

    scene bg_car_passenger with dissolve

    tsukune "I do! Let me go ahead and grab a picture from her blog."

    alex "{i}Wait, she has a blog?! Why didn't I know about this?{/i}"

    tsukune "Alright, I've got it here!"

    scene bg_claudia_coffee_art with dissolve

    tsukune "She mainly shows off her coffee art skills. She was really proud of this one!"

    alex "{i}I see... Being a barista seems to be a hobby for her.{/i}"

    $ persistent.journal_unlock = True
    
    $ persistent.claudia_hobby_barista = True
    $ renpy.notify("You have information about Claudia.")

    $ persistent.journal_unlock = False
    scene bg_claudia_selfie_behind with dissolve

    tsukune "She's kinda athletic from what I can tell."

    alex "{i}Well I already knew that about her.{/i}"

    alex "{i}Then again, this might not be the same Claudia.{/i}"

    alex "{i}Wait!{/i}"

    scene bg_claudia_selfie_behind_zoom with dissolve

    alex "{i}That tattoo! That's definitely my neighbor!{/i}"

    scene bg_claudia_selfie_smile with dissolve

    tsukune "And then here's what she looks like."

    alex "Oh... Wow, she looks amazing."

    ## [Question 2] Interest In Claudia
    menu:
        alex "{i}Wait a second...{/i}"

        "Ask how interested Tsukune is in her.":
            jump chapter_0_claudiaInterest_a

        "I thought you were gay":
            jump chapter_0_claudiaInterest_b

        "Crash the car.":
            jump chapter_0_claudiaInterest_c

## [Answer 2a] Gauging Interest
label chapter_0_claudiaInterest_a:

    alex "So... how interested are you in her?"

    tsukune """
    I mean, I'm interested, but I'm not exactly committed to anything huge like 
    marriage already. I just met her, after all.

    I kinda go by the philosophy that if you haven't known someone for at least 
    two weeks, you won't really know if there's actual interest there, you know?
    """

    alex "{i}That's good to know.{/i}"

    $ persistent.tsukune_claudia_interest = True

    $ renpy.notify("You have information about Tsukune.")

    alex "Oh, here's your place."

    scene bg_tsukune_apartment_parking_lot with dissolve

    show tsukune neutral

    tsukune "Thanks again for dropping me off. I appreciate you."

    alex "It's no problem. See you later."

    hide tsukune with dissolve

    scene black with fade

    jump chapter_0_tsukuneDrive_end

## [Answer 2b] r u gey
label chapter_0_claudiaInterest_b:
    tsukune "I wonder why everyone thinks I'm gay? But no, I'm actually pan. Labels feel kinda weird anyways."

    menu:
        "Ask how interested Tsukune is in her.":
            jump chapter_0_claudiaInterest_a

        "Crash the car.":
            jump chapter_0_claudiaInterest_c

## [Answer 2c] Crash the car
label chapter_0_claudiaInterest_c:
    stop music

    scene bg_car_driver with dissolve

    alex "Screw you, I won't let you have her!"

    tsukune "Wait, what're you talking about."

    scene bg_speedometer_high with dissolve

    tsukune "STOP. {b}STOP!{/b}"

    scene black with fade

    return

## START: Drop off Tsukune
label chapter_0_tsukuneDrive_end:

    scene bg_you_apartment_living_room with fade

    alex "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"
    
    scene bg_sidewalk

    stop music

    jump chapter_0_end

label chapter_0_end:
    scene bg_you_apartment_living_room

    alex "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"

    jump chapter_1_part_1
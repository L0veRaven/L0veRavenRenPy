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
    
label chapter_0_1:
    play music "audio/music/scene3.ogg"

    scene bg_office with Dissolve(2.0)

    $ persistent.quick_menu_display = True

    tsukune "Hey Alex!"

    show tsukune neutral:
        xpos 1.0 #Start off-screen to the right
        ease 0.75 xpos 0.0 ypos 0.0 #Ease -> center to Y axis
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up

    tsukune "What're you working on there?"

    you "O-oh, nothing much. I'm just... journaling a little bit." with hpunch

    show tsukune neutral:
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up
        
    tsukune "\*chuckles\* I mean, what else are you gonna do during downtime?"

    show tsukune neutral:
        ease 1.0 xpos 0.15 #Slide to the right

    tsukune "Now that I think about it, I need to check in with Ash about the spreadsheet xe was supposed to send in..."

    you "Right..."

    show tsukune neutral:
        ease 0.5 xpos 0.0 #Slide to center

    tsukune "Oh, when we get off work, I wanna tell you about someone I met."

    you "Someone you met?"

    show tsukune neutral:
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up

    tsukune "Yeah! See, I met a girl at this coffee shop the other day."

    show tsukune blush:
        ease 1.0 xpos 0.05 #Slide to the right

    tsukune "To be honest, she's kinda cute. I was lucky enough to get her contact info."

    you "Geez, I wish I was lucky enough to get that from my crush..."

    show tsukune neutral:
        ease 0.5 ypos 0.05 #Ease -> slight dip down
        ease 1.0 ypos 0.0 #Ease -> slight bounce back up
    
    tsukune "Don't worry. I'm sure you'll get there soon enough."
    
    tsukune "Anyways, I gotta get back to work. Talk more later!"

    show tsukune neutral:
        ease 1.0 xpos 1.0 #Slide off-screen to the right

    hide tsukune with dissolve

    you "The closest I get with my crush is talking to her since she's my neighbor..."

    you "Oh well, back to work."

    scene black with fade

    ## TODO: play sound typing

    you "Oh, it's time to clock out."

    ## TODO: play sound car-door-close

    scene bg_car_passenger with fade

    tsukune "Thanks for driving me, again."

    you "It's no problem. Besides, I drive past your place on the way home, so it's not like it takes any time away from me."

    tsukune "I guess you're right."

    scene bg_car_driver with dissolve

    tsukune "So, remember the girl I was telling you about earlier?"

    you "Yeah, the coffee shop girl."

    tsukune "Her name is Claudia. She's really nice."

    you "{i}Claudia... No, there's no way that he's talking about the same Claudia...{/i}"

    you "{i}... Right?{/i}"

    tsukune "She's really pretty and I figured that we could start off with just talking."

    you "Do you have a picture of her?"

    scene bg_car_passenger with dissolve

    tsukune "I do! Let me go ahead and grab a picture from her blog."

    you "{i}Wait, she has a blog?! Why didn't I know about this?{/i}"

    tsukune "Alright, I've got it here!"

    scene bg_claudia_coffee_art with dissolve

    tsukune "She mainly shows off her coffee art skills. She was really proud of this one!"

    you "{i}I see... Being a barista seems to be a hobby for her.{/i}"

    $ persistent.journal_unlock = True
    
    $ persistent.claudia_hobby_barista = True
    $ renpy.notify("You wrote info about Claudia in your notebook.")

    scene bg_claudia_selfie_behind with dissolve

    tsukune "She's kinda athletic from what I can tell."

    you "{i}Well I already knew that about her.{/i}"

    you "{i}Then again, this might not be the same Claudia.{/i}"

    you "{i}Wait!{/i}"

    scene bg_claudia_selfie_behind_zoom with dissolve

    you "{i}That tattoo! That's definitely my neighbor!{/i}"

    scene bg_claudia_selfie_smile with dissolve

    tsukune "And then here's what she looks like."

    you "Oh... Wow, she looks amazing."

    $ persistent.journal_unlock = False

menu:

    you "{i}I can't let him talk to her...{/i}"

    "Ask how interested Tsukune is in her.":
        jump chapter_0_question_1a

    "Crash the car.":
        jump chapter_0_question_1b

label chapter_0_question_1a:

    you "So... how interested are you in her?"

    tsukune "I mean, I'm interested, but I'm not exactly committed to anything huge like marriage already. I just met her, after all."

    tsukune "I kinda go by the philosophy that if you haven't known someone for at least two weeks, you won't really know if there's actual interest there, you know?"

    you "{i}That's good to know.{/i}"

    $ persistent.tsukune_claudia_interest = True
    $ persistent.calendar_unlock = True
    $ renpy.notify("You wrote info about tsukune in your notebook.")

    you "Oh, here's your place."

    scene bg_tsukune_apartment_parking_lot with dissolve

    show tsukune neutral

    tsukune "Thanks again for dropping me off. I appreciate you."

    you "It's no problem. See you later."

    hide tsukune with dissolve

    scene black with fade

    jump chapter_0_2

label chapter_0_question_1b:
    stop music

    scene bg_car_driver with dissolve

    you "Screw you, I won't let you have her!"

    tsukune "Wait, what're you talking about."

    scene bg_speedometer_high with dissolve

    tsukune "STOP. {b}STOP!{/b}"

    scene black with fade

    return

label chapter_0_2:

    scene bg_you_apartment_living_room with fade

    you "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"
    
    scene bg_sidewalk

    stop music

    jump chapter_0_end

label chapter_0_end:
    scene bg_you_apartment_living_room

    you "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"

    jump chapter_1_part_1
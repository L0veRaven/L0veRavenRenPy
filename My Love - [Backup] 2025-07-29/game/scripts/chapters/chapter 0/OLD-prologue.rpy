## START: Tsukune Drive - Claudia Talk
label wip_tsukuneDrive_claudiaTalk:
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
    
    $ persistent.claudiaNotes_barista = True
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
            jump wip_claudiaInterest_a

        "I thought you were gay":
            jump wip_claudiaInterest_b

        "Crash the car.":
            jump wip_claudiaInterest_c

## [Answer 2a] Gauging Interest
label wip_claudiaInterest_a:
    alex "So... how interested are you in her?"

    tsukune """
    I mean, I'm interested, but I'm not exactly committed to anything huge like 
    marriage already. I just met her, after all.

    I kinda go by the philosophy that if you haven't known someone for at least 
    two weeks, you won't really know if there's actual interest there, you know?
    """

    alex "{i}That's good to know.{/i}"

    $ persistent.loveMeter = True

    $ renpy.notify("You have information about Tsukune.")

    jump wip_tsukuneDrive_end

## [Answer 2b] r u gey
label wip_claudiaInterest_b:
    tsukune "I wonder why everyone thinks I'm gay? But no, I'm actually pan. Labels feel kinda weird anyways."

    menu:
        "Ask how interested Tsukune is in her.":
            jump wip_claudiaInterest_a

        "Crash the car.":
            jump wip_claudiaInterest_c

## [Answer 2c] Crash the car
label wip_claudiaInterest_c:
    stop music

    scene bg_car_driver with dissolve

    alex "Screw you, I won't let you have her!"

    tsukune "Wait, what're you talking about."

    scene bg_speedometer_high with dissolve

    tsukune "STOP. {b}STOP!{/b}"

    scene black with fade

    return
    





#################################################################
## Journal Entry Example
#################################################################

#label wip:
#    scene black with fade
#
#    alexJournal """
#    June 12th{nw}
#    
#    \nIt sucks being at work. It's not the work that's even challenging. My brain just won't shut up about Claudia, my neighbor. It's not that I don't want to acknowledge that she exists, but I have work to do!{nw}
#
#    \nMaybe I should think about this from a different angle...{nw}
#
#    \nI've been working on learning to identify my feelings, and that's really hard when you have depression. The way that my depression clouds my mind and emotions, it makes it so much harder to know what I'm feeling, or even how to go about my life.{w=0.5}
#    """
#    play sound "sfx/paper-flip.ogg"
#    nvl clear
#
#    alexJournal """
#    It's not just about my depression, though. Claudia genuinely takes up so much of my mind.{nw}
#
#    \nOddly enough, even though I've been struggling with this for years, Claudia managed to give me feelings so clear that I'd be a fool to not know what it is:{nw}
#    
#    \n{sc=2}Love{/sc}
#    
#    \nClaudia hasn't lived here long. I think it's only been about a week since she moved in? I know many people would say \"It's too soon for you to fall in love!\" but I don't think they know how mesmerizing she is!{nw}
#    
#    \nEvery time I get a glimpse of her, my heart pounds in a way I've {sc=2}never{/sc} felt before...{w=0.5}
#    """
#
#    play sound "sfx/paper-flip.ogg"
#    nvl clear
#
#    scene bg_claudia_polaroids_desk with Dissolve(1.0)
#    with Pause(0.5)
#
#    alexJournal """
#    I've been taking pictures of her whenever I get the chance. It's nice to keep photos of the things I care about. Besides, it's far less weird to look at photos of her rather than staring at her in public.{nw}
#
#    \nI took a couple of photos while she was taking out trash today. She sure did seem tired. It's probably because she was working late last night, poor thing.{nw}
#
#    \nIt's more than her looks, though. Her mannerisms... The way she tucks her hair behind her ear... The way she ties up her hair... Even the way she talks is {sc=2}magnetizing{/sc}.{w=0.5}
#    """
#
#    play sound "sfx/paper-flip.ogg"
#    nvl clear
#
#    scene bg_claudia_apartment_curtains_closed with Dissolve(2.0)
#
#    alexJournal """
#    I want to know what her daily routine is like. Unfortunately, it's not that easy. She lives directly next to me, so I can't really take photos when I'm so close.{nw}
#
#    \nIt'd also be really weird if I just sat outside her apartment, waiting for her to leave or to see who comes by to visit. Sure, I can peek through the blinds or look through my open window, but I'd probably look very suspicious doing that.{nw}
#    
#    \nI'm ashamed to admit that I'm too nervous to approach her. It would be much easier to talk to her rather than doing complicated bullshit to learn more about her.{w=0.5}
#    """
#
#    play sound "sfx/paper-flip.ogg"
#    nvl clear
#
#    scene black with Dissolve(2.0)
#    
#    stop music
#
#    alex "I swear... I need to be with her {sc=3}{b}s o . . . b a d . . .{/b}{/sc}"
#
#    jump wip_meetTsukune

## TODO: Talk with Claudia after getting home from work
label prologue_conversation_ClaudiaApartments:
    
    
#################################################################
## Office: Meeting Tsukune
#################################################################
#    show tsukune neutral:
#        xpos 1.0 #Start off-screen to the right
#        ease 0.75 xpos 0.0 ypos 0.0 #Ease -> center to Y axis
#        ease 0.5 ypos 0.05 #Ease -> slight dip down
#        ease 1.0 ypos 0.0 #Ease -> slight bounce back up    
#################################################################
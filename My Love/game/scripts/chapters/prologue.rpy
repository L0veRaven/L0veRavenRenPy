label prologue_start:
    #########################################
    ## Meeting Claudia
    #########################################

    play music "sfx/outdoors_day.mp3"
    scene bg_apartment_outside with Dissolve (2.0)

    voice "voice-lines/claudia-1.mp3"

    show claudia_smilewave:
        xpos 1.0 #Start off-screen to the right
        ease 3.0 xpos 0.65 #Ease -> center to Y axis
    claudiaUnknown "Thanks for helping me move everything in Toby, I appreciate it so much!"

    hide claudia_smilewave
    show claudia_neutral:
        xpos 0.65
        ease 1.0 xpos 0.6

    $ persistent.quick_menu_display = True
    claudiaUnknown "Alright, time to unpack-"

    play sound "sfx/door_lock.mp3"
    pause 1.0
    
    show alex_neutral:
        xpos -600
        ease 1.0 xpos 0.02
    alex "U-uh, hey there!"

    claudiaUnknown "Oh, hi! I just moved in. It looks like you'll be my next door neighbor!"

    alex "Really? Damn, that unit's been empty for a solid year."

    claudiaUnknown "Sounds like I'll be the one to change things up here! You've lived here for a while?"

    alex "Yeah, I've been here for about three years."

    claudiaUnknown "... There aren't roaches here, right?"

    alex "Oh, no! They have pest control come out here every week, so we don't have any pests like that around here."

    claudiaUnknown "That's a relief! My last place had a {i}{b}super{/b}{/i} bad infestation. You can thank the hoarder neighbors for that."

    claudia "I'm Claudia by the way."

    alex "I'm Alex! It's nice to have someone new around here."

    claudia "I bet! Anyways, I'd better start unpacking. I'll see you around."

    hide claudia_neutral
    alex "See you later!"

    scene black with fade
    play sound "sfx/carDoor_close.mp3"
    pause 1.0
    
    scene bg_car_driver with fade
    pause 1.0

    alex "... See you later?"
    alex "It was nice of her to think of me like that"
    alex "Well, she {i}{b}is{/i}{/b} my neighbor... but she seems really nice and beautiful."
    alex "I wonder..."

    #play sound "sfx/wristwatch_alarm.mp3"
    alex "Oh shit, I need to leave for work!"

    play sound "sfx/key_jingle.mp3"
    pause 2.0
    play sound "sfx/carDrive_start.mp3"
    pause 2.0

    scene black with fade

    pause 1.0

    alex "{i}That girl... Claudia...{/i}"

    alex "{i}There's something about her that's really sticking out to me...{/i}"
    
    alex "Maybe I should try journaling."

    pause 1.0

    #########################################
    ## Journal
    #########################################
    jump prologue_journalAlex_1

label prologue_journalAlex_1:
    play music "audio/music/scene5.ogg"
    scene bg_work_desk with Dissolve(2.0)

    alexJournal "June 12\n"

    alexJournal "Journaling still feels very strange to me. It's like I'm talking to the void... but there's nothing else I can do right now. I'm at work, so I can't really call anyone, not that there's anyone for me to talk to.\n"

    alexJournal "There's a new person that moved into the vacant apartment next to me. Her name is Claudia and there's something that sticks out about her. I haven't been able to stop thinking about her, but that's not normal for me. At all.\n"

    alexJournal "I don't really talk to people much except for Tsukune and Ash, but they're coworkers. Does that even count?"

    play sound "sfx/paper-flip.ogg"
    nvl clear

    alexJournal "Maybe it's because Claudia is new, but I really want to keep talking to her. She's really pretty and seems nice...\n"

    alexJournal "Wait... is this what having a crush feels like?"

    stop music
    #play sound "sfx/footsteps1.ogg"
    nvl clear

    alex "{i}Shit, someone's coming.{/i}"

label prologue_meetTsukune:
    play sound "sfx/paper-flip.ogg"

    play music "audio/music/scene3.ogg"

    scene bg_office

    show tsukune neutral
    tsukuneUnknown "Hey, Alex! How're you doing?"

    alex "Hey Tsukune, I'm good! Nothing crazy's going on."

    tsukune "My car is still in the shop right now. It sucks! They said it'll be done by Wednesday though."

    alex "What's the car in the shop for again?"

    tsukune "The AC compressor seized up and completely snapped the serpentine belt. You should've seen the smoke come out of the air vents when that happened!"

    alex "What's taking them so long? It's been a week already."

    tsukune "They're waiting on the replacement AC compressor to get delivered. Gotta love having an older car and waiting longer for the parts for the come in."

    alex "You know, I don't have a problem with driving you home until the car's repaired."

    tsukune "Really? That's awesome, I appreciate it! It's honestly kind of embarassing to ask other people to help me out."

    alex "It's not a problem for me! Your place is on my way home, so it's not really inconveniencing me."

    tsukune "You're a great friend, Alex. I mean it."
    tsukune "Damn, I gotta get back to work. I'll talk to you later!"
    hide tsukune neutral

    alex "I guess I should get back to work too."

    scene black with fade
    stop music

    #play sound "sfx/watch-beep.mp3"
    alex "Oh, it's time to go!"

    jump prologue_tsukuneDrive

label prologue_tsukuneDrive:
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

label drive_conversation_tsukuneTherapy:
    $ lovePoints_Tsukune+=20 #Increase Tsukune love points by 20

    alex "So Tsukune, Imma be real for a second. How are you doing lately? Like, how are you actually doing?"

    tsukune "Oh... damn, it's been a while since someone checked in on me... That's nice of you."
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
            jump drive_conversation_tsukuneTherapy_a

        "I'm glad it's working out for you!":
            jump drive_conversation_tsukuneTherapy_b

        "Do you think I need therapy?":
            jump drive_conversation_tsukuneTherapy_c

#    jump chapter_1_start
## [Answer 1a] Therapy is bullshit
label drive_conversation_tsukuneTherapy_a:
    alex "I don't see the point in therapy. I doesn't even {i}{b}really{/b}{/i} help you."

    tsukune "What do you mean?"

    alex "Therapists basically have {i}{b}you{/b}{/i} try to figure everything out by yourself?"

    tsukune "Not exactly. At least for me, my therapist offers suggestions, but ultimately leaves decisions up to me."

    alex "That's my point."

    tsukune "Well, it {i}{b}is{/b}{/i} my life, so she can't make me do anything, even if she wanted to."

    alex "So therapy is where you go to get suggestions?"

    tsukune "She also walks me through different coping skills. It's much better than me smoking cigarettes like before."

    $ renpy.notify("You have information about Tsukune.")
    $ persistent.tsukuneNotes_cigaretteAddiction = True
    alex "She helped you quit smoking?"

    tsukune "No, I quit before I started getting therapy. If anything, therapy is helping me stay away from cigarettes."

    alex "Really?"

    tsukune "It might be hard to believe, but learning how to manage my stress and triggers makes me less likely to want to smoke. Cigarettes honestly made my issues worse."

    alex "I guess therapy {i}{b}is{/b}{/i} pretty helpful after all."

    tsukune "It really is, for me at least."

    jump prologue_conversation_ClaudiaApartments

## [Answer 1b] Happy for Tsukune
label drive_conversation_tsukuneTherapy_b:
    alex "That sounds great! It can be pretty difficult for people to start therapy."
    
    tsukune "It really can! I only finally started therapy once I noticed I was going to relapse on smoking cigarettes again."
    
    $ renpy.notify("You have information about Tsukune.")
    $ persistent.tsukuneNotes_cigaretteAddiction = True
    alex "You used to smoke?"

    tsukune "Yup, but I quit before I started working at this company. It honestly sucks to have people side-eyeing you and talking shit for having an addiction."

    alex "Were your old coworkers mad about it?"

    tsukune "They really were, but they thought I couldn't hear them. They always changed topics when I made my presence known during those conversations."

    alex "That must really suck. At least you're not dealing with that here, right?"

    tsukune "Exactly, it's why I really like working here."

    jump wip_tsukuneDrive_claudiaTalk

## [Answer 1c] Alex needs therapy
label drive_conversation_tsukuneTherapy_c:
    alex "I know this is kind of weird to ask, but do you think {i}{b}I{/b}{/i} need therapy?"
    
    tsukune "Well, I don't think it's my place to say. Even though {i}{b}I{/b}{/i} think everyone would benefit from seeing a therapist, that doesn't mean it'll work for everyone."

    alex "I guess you're right... If you don't mind me asking, why did you decide to see a therapist?"

    tsukune "Oh, well my reason was because I was getting close to relapsing on smoking cigarettes. I used to smoke four per day!"
    
    $ renpy.notify("You have information about Tsukune.")
    $ persistent.tsukuneNotes_cigaretteAddiction = True
    alex "... Four packs a day?!"

    tsukune "Woah, not {i}{b}that{/b}{/i} many. Just four cigarettes per day."

    alex "Is that a lot?"

    tsukune "Any amount of cigarettes is too much, realistically."

    alex "That's a good point. I think I could qualify for therapy. I know that I have depression, but I'm not sure how a therapist would fix that."

    tsukune "Well, it's not the therapist's job to fix your problems necessarily. They provide you with the tools to heal yourself emotionally and work through your issues."

    alex "It sounds like I'd be doing all the work, right?"

    tsukune "They help you through the process, so you're not just raw dogging everything."

    $ persistent.alexChoice_therapy
    alex "I'll consider it. I just hope it doesn't change my schedule too much."

    tsukune "I think you should do therapy when you feel ready for it. It only works if you {i}{b}really{/b}{/i} want the help."

    jump wip_tsukuneDrive_claudiaTalk

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

    $ persistent.relationshipMeter = True

    $ renpy.notify("You have information about Tsukune.")

    alex "Oh, here's your place."

    scene bg_tsukune_apartment_parking_lot with dissolve

    show tsukune neutral

    tsukune "Thanks again for dropping me off. I appreciate you."

    alex "It's no problem. See you later."

    hide tsukune with dissolve

    scene black with fade

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
    























label wip:
    scene black with fade

    alexJournal """
    June 12th{nw}
    
    \nIt sucks being at work. It's not the work that's even challenging. My brain just won't shut up about Claudia, my neighbor. It's not that I don't want to acknowledge that she exists, but I have work to do!{nw}

    \nMaybe I should think about this from a different angle...{nw}

    \nI've been working on learning to identify my feelings, and that's really hard when you have depression. The way that my depression clouds my mind and emotions, it makes it so much harder to know what I'm feeling, or even how to go about my life.{w=0.5}
    """
    play sound "sfx/paper-flip.ogg"
    nvl clear

    alexJournal """
    It's not just about my depression, though. Claudia genuinely takes up so much of my mind.{nw}

    \nOddly enough, even though I've been struggling with this for years, Claudia managed to give me feelings so clear that I'd be a fool to not know what it is:{nw}
    
    \n{sc=2}Love{/sc}
    
    \nClaudia hasn't lived here long. I think it's only been about a week since she moved in? I know many people would say \"It's too soon for you to fall in love!\" but I don't think they know how mesmerizing she is!{nw}
    
    \nEvery time I get a glimpse of her, my heart pounds in a way I've {sc=2}never{/sc} felt before...{w=0.5}
    """

    play sound "sfx/paper-flip.ogg"
    nvl clear

    scene bg_claudia_polaroids_desk with Dissolve(1.0)
    with Pause(0.5)

    alexJournal """
    I've been taking pictures of her whenever I get the chance. It's nice to keep photos of the things I care about. Besides, it's far less weird to look at photos of her rather than staring at her in public.{nw}

    \nI took a couple of photos while she was taking out trash today. She sure did seem tired. It's probably because she was working late last night, poor thing.{nw}

    \nIt's more than her looks, though. Her mannerisms... The way she tucks her hair behind her ear... The way she ties up her hair... Even the way she talks is {sc=2}magnetizing{/sc}.{w=0.5}
    """

    play sound "sfx/paper-flip.ogg"
    nvl clear

    scene bg_claudia_apartment_curtains_closed with Dissolve(2.0)

    alexJournal """
    I want to know what her daily routine is like. Unfortunately, it's not that easy. She lives directly next to me, so I can't really take photos when I'm so close.{nw}

    \nIt'd also be really weird if I just sat outside her apartment, waiting for her to leave or to see who comes by to visit. Sure, I can peek through the blinds or look through my open window, but I'd probably look very suspicious doing that.{nw}
    
    \nI'm ashamed to admit that I'm too nervous to approach her. It would be much easier to talk to her rather than doing complicated bullshit to learn more about her.{w=0.5}
    """

    play sound "sfx/paper-flip.ogg"
    nvl clear

    scene black with Dissolve(2.0)
    
    stop music

    alex "I swear... I need to be with her {sc=3}{b}s o . . . b a d . . .{/b}{/sc}"

    jump wip_meetTsukune

## TODO: Talk with Claudia after getting home from work
label prologue_conversation_ClaudiaApartments:
    scene bg_you_apartment_living_room with fade

    alex "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"
    
    scene bg_sidewalk

    stop music

    jump chapter_1_start
    
#################################################################
## Office: Meeting Tsukune
#################################################################
#    show tsukune neutral:
#        xpos 1.0 #Start off-screen to the right
#        ease 0.75 xpos 0.0 ypos 0.0 #Ease -> center to Y axis
#        ease 0.5 ypos 0.05 #Ease -> slight dip down
#        ease 1.0 ypos 0.0 #Ease -> slight bounce back up    
#################################################################
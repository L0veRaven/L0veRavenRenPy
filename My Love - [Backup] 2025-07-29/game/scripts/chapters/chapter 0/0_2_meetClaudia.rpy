#########################################
## Meeting Claudia
#########################################

label c0_meetClaudia:
    play music "sfx/outdoors_day.mp3"
    scene bg_apartment_outside with Dissolve(3.0)

    voice "voice-lines/claudia-1.mp3"
    show claudia_smilewave:
        xpos 1.0 #Start off-screen to the right
        ease 3.0 xpos 0.65 #Ease -> center to Y axis
    claudiaUnknown "Thanks for helping me move everything in Toby, I appreciate it so much!"

    hide claudia_smilewave
    show claudia_neutral:
        xpos 0.65
        ease 1.0 xpos 0.6

    claudiaUnknown "Alright, time to unpack all those boxes."

    play sound "sfx/door_lock.mp3"
    pause 1.0
    
    show alex_neutral:
        xpos -600
        ease 2.0 xpos 0.02

    alex "..."
    
    show alex_neutral:
        ease 0.2 xpos -0.09

    alex "O-oh, hey there!"

    show claudia_neutral:
        ease 1.2 xpos 0.58
    claudiaUnknown "Oh, hey there! I didn't mean to startle you. I just moved my things in. Were my friend and I too loud?"

    show alex_neutral:
        ease 1 xpos 0.12
    alex "Really? Damn, that unit's been empty for a solid year. No worries about the noise though. You gotta do what you gotta do, right?"

    claudiaUnknown "I'm glad that you understand at least. If this unit has been empty for a whole year, I better get to deep-cleaning the place soon. I can't stand when grime builds up."

    alex "Hah, I get what you mean. It's a struggle out here."

    claudiaUnknown "Hah... Yeah, it is..." # Claudia has hygiene OCD
    
    claudiaUnknown "So... you've lived here for a while?"

    alex "Yeah, I've been here for about three years."

    claudiaUnknown "... There aren't roaches here, right?"

    alex "Oh, no! They have pest control come out here every week, so we don't have any pests like that around here."

    claudiaUnknown "That's a relief! The place I had before the one I just moved from used to have a {i}{b}super{/b}{/i} bad infestation. You can thank the hoarder neighbors for that."

    claudia "I'm Claudia by the way."

    alex "I'm Alex! It's nice to have someone new around here!"

    claudia "I bet it is! Anyways, I'd better start unpacking and cleaning. I'll see you later!"

    hide claudia_neutral with Dissolve(1.0)
    alex "See you later!"

    scene black with Dissolve(1.0)
    play sound "sfx/carDoor_close.mp3"
    pause 2.0
    
    scene bg_car_driver with Dissolve(1.0)
    pause 1.0

    "{i}\"... See you later?\"{/i} That's really nice. I didn't think that I'd get along with someone new like that."
    "I felt pretty awkward when talking to her though. Claudia... right?"
    "It's good to know that she's interested in getting to know me more. I think it'd do me some good to make friends with someone new."
    
    play sound "sfx/digital-watch-alarm-81203.mp3"
    alex "Oh shit, I need to leave for work!"

    play sound "sfx/key_jingle.mp3"
    pause 2.0
    play sound "sfx/carDrive_start.mp3"
    pause 2.0

    scene black with fade

    pause 1.0

    "That woman... Claudia..."

    "There's something about her that's really sticking out to me..."
    
    alex "Maybe I should try journaling about it... That might help me get it off my mind."

    pause 1.0

    #########################################
    ## Journal
    #########################################
    jump c0_journal2
    
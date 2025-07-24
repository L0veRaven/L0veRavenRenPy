label chapter_0_meetClaudia:
    play music "sfx/outdoors_day.mp3"
    scene bg_apartment_outside with Dissolve (3.0)

    voice "voice-lines/claudia-1.mp3"
    show claudia_smilewave:
        xpos 1.0 #Start off-screen to the right
        ease 3.0 xpos 0.65 #Ease -> center to Y axis
    claudiaUnknown "Thanks for helping me move everything in Toby, I appreciate it so much!"

    hide claudia_smilewave
    show claudia_neutral:
        xpos 0.65
        ease 1.0 xpos 0.6

    claudiaUnknown "Alright, time to unpack this shit."

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
        ease 1 xpos 0.15
    alex "Really? Damn, that unit's been empty for a solid year."
    alex "No worries about the noise though. You gotta do what you gotta do, right?"

    claudiaUnknown "I'm glad that you understand at least. So... you've lived here for a while?"

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
    jump chapter_0_journal2
    
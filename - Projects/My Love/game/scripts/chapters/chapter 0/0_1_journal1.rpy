label c0_journal1:
    scene black with Dissolve(2.0)
    pause 2.0
    scene bg_alex_apartment_living_room with Dissolve(2.0)
    pause (2.0)
    $ persistent.quick_menu_display = True
    
    play sound scribble
    alexJournal "June 12, 2023 7:32 AM"

    play sound scribble
    alexJournal "This is the third month of me journaling daily to see how good it benefits me."
    
    play sound scribble
    alexJournal "I've slowly gotten over my weird feelings about writing in this as if I were talking to a person."
    
    play sound scribble
    alexJournal "It makes sense why some people recommended that on those posts online."
    
    play sound scribble
    alexJournal "It's about feeling heard."

    play sound scribble
    alexJournal "I noticed a difference since I've started journaling."
    
    play sound scribble
    alexJournal "It's not a huge change, but it's nice to start learning how to identify the emotions I'm feeling."

    play sound scribble
    alexJournal "I know it seems weird to not know how to describe my feelings, but I wasn't raised to really get in touch with my emotions."
    
    play sound scribble
    alexJournal "In fact, feeling emotions was basically treated as a sin."

    nvl clear
    pause 1.0
    #play sound "muffled speech"
    #play sound "noise"
    play sound carDoorClose
    pause 2.0

    stop music

    alex "{i}What's going on outside?{/i}"
    #play sound footssteps1

    jump c0_meetClaudia
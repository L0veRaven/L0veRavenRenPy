label c0_journal1:
    scene black with Dissolve(2.0)
    pause 2.0
    scene bg_alex_apartment_living_room with Dissolve(2.0)
    pause (2.0)
    $ persistent.quick_menu_display = True
    play sound "audio/sfx/scribble.mp3"
    alexJournal "June 12, 2023 7:32 AM"

    play sound "audio/sfx/scribble.mp3"
    alexJournal "This is the third month of me journaling daily to see how good it benefits me.{w}
    I've slowly gotten over my weird feelings about writing in this as if I were talking to a person.{w}
    It makes sense why some people recommended that on those posts online. It's about feeling heard.{w}"

    play sound "audio/sfx/scribble.mp3"
    alexJournal "I noticed a pretty big difference since I've started journaling.{w} It's not a huge change, but it's nice to start learning how to identify the emotions I'm feeling.{w}"

    play sound "audio/sfx/scribble.mp3"
    alexJournal "I know it seems weird to not know how to describe my feelings, but I wasn't raised to really get in touch with my emotions.{w}"
    
    play sound "audio/sfx/scribble.mp3"
    alexJournal "In fact, feeling emotions was basically treated as a sin.{w}"

    nvl clear

    pause 1.0
    #play sound "muffled speech"
    #play sound "noise"
    play sound "sfx/carDoor_close.mp3"
    pause 2.0

    stop music

    alex "{i}What's going on outside?{/i}{w}"
    #play sound "sfx/footsteps1.ogg"

    jump c0_meetClaudia
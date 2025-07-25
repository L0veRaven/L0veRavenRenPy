label chapter_0_journal1:
    scene black
    pause 2.0
    $ persistent.quick_menu_display = True
    play sound "audio/sfx/paper-flip.ogg"
    "June 12, 2023 7:32 AM"

    play sound "audio/sfx/paper-flip.ogg"
    "It's me, Alex. This is day three of me journaling daily to see how good it benefits me... or something? It feels weird talking to a book. It's not like you're talking back to me."

    play sound "audio/sfx/paper-flip.ogg"
    "I guess I've noticed a bit of a difference since I've started journaling. It's not a super huge change, but it's nice to start learning how to identify the emotions I'm feeling."

    play sound "audio/sfx/paper-flip.ogg"
    "I know it seems weird to not know how to describe my feelings, but I wasn't raised to really get in touch with my emotions."
    
    play sound "audio/sfx/paper-flip.ogg"
    "In fact, feeling emotions was basically treated as a sin."

    pause 1.0
    #play sound "muffled speech"
    #play sound "noise"
    play sound "sfx/carDoor_close.mp3"
    pause 2.0

    stop music

    alex "{i}What's going on outside?{/i}"
    #play sound "sfx/footsteps1.ogg"

    jump chapter_0_meetClaudia
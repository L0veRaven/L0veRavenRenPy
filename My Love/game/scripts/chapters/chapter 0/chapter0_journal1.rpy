label chapter_0_journal1:
    scene black
    pause 2.0
    play sound "audio/sfx/paper-flip.ogg"
    "June 12, 202X 7:32 AM"

    $ persistent.quick_menu_display = True
    play sound "audio/sfx/paper-flip.ogg"
    "It's me, Alex. This is day three of me journaling daily to see how good it benefits me... or something? It feels weird talking to a book. It's not like you're talking back to me."

    stop music
    #play sound "sfx/footsteps1.ogg"

    alex "{i}What's going on outside?{/i}"

    jump chapter_0_meetClaudia
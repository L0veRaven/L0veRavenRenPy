label chapter_1_start:
    play music "audio/music/triangle-elevator.mp3"

    scene bg_you_apartment_living_room with fade

    tsukune "We're gonna do a presentation night!"

    claudia "I came up with the idea during my lunch break at work 🥳"
    
    claudia "My presentation is going to be about Russian Blue cats!"

    tsukune "Mine is gonna be about the song Emma Was My Best Friend by The Serial Killers. It's pretty interesting when you learn more about it."

    alex "{i}Maybe I have a chance at impressing Claudia with what I decide to do tonight.{/i}"

    stop music

    menu:
        "Talk about coffee grounds":
            jump route_coffeePresentation

        "Talk about pandas and their environmental impact":
            jump route_pandaPresentation

label route_coffeePresentation:
    jump chapter_2_start

label route_pandaPresentation:
    jump chapter_2_start
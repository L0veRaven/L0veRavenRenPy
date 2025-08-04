label c0_tsukuneDrive_end:
    alex "Oh, here's your place."

    scene bg_tsukune_apartment_parking_lot with Dissolve(1.0)

    play sound "sfx/carDoor_open.mp3"
    show tsukune_neutral with Dissolve(0.4)
    tsukune "Thanks again for dropping me off. I owe you one!"

    alex "It's no problem. See you later!"

    tsukune "Wait, did you want to go to the gym with Ash and I later? It'll be Ash's first time back in a while back in the gym."

    alex "I would, but I've actually got some stuff on my mind right now. Maybe next time?"

    tsukune "No big deal, and hey, whatever's on your mind hopefully isn't gonna be the end of the world."

    menu:
        "Should I be a little dramatic?"
        
        "Be a little dramatic":
            jump c0_dramaticReaction

        "Be normal and leave":
            jump c0_normalReaction

label c0_dramaticReaction:
    stop music fadeout 1.0
    alex "Wait... I think I feel something..."

    tsukune "Huh? What is it?"

    "I make obviously fake gagging noises and lightly grab my throat."

    alex "I'm dying!" with hpunch

    "I playfully go limp. Thank heavens the car is already in park."

    tsukune "Bwahahaha! Good one Alex! I'll see you tomorrow or if you decide to game."

    alex "Later dude!"

    jump c0_alexApartment_livingRoom

label c0_normalReaction:
    jump c0_alexApartment_livingRoom
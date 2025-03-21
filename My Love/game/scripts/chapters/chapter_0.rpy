label chapter_0_1:
    play music "audio/music/scene3.ogg"

    scene bg_office with Dissolve(2.0)

    $ persistent.quick_menu_display = True

    tsukune "Hey..."

    show tsukune neutral

    tsukune "What're you working on there?"

    you "O-oh, nothing much. I'm just journaling a little bit." with hpunch

    tsukune "\*chuckles\* What else are you gonna do during downtime, right?"

    you "Right..."

    tsukune "Oh, when we get off work, I wanna tell you about someone I met."

    you "Someone you met?"

    tsukune "Yeah! See, I met a girl at this coffee shop the other day."

    show tsukune blush

    tsukune "To be honest, she's kinda cute. I was lucky enough to get her contact info."

    you "Geez, I wish I was lucky enough to get that from my crush..."

    show tsukune neutral
    
    tsukune "Don't worry. I'm sure you'll get there soon enough."
    
    tsukune "Anyways, I gotta get back to work. Talk more later!"

    hide tsukune with dissolve

    you "The closest I get with my crush is talking to her since she's my neighbor..."

    you "Oh well, back to work."

    scene black with fade

    you "Oh, it's time to clock out."

    scene bg_car_passenger with fade

    tsukune "Thanks for driving me, again."

    you "It's no problem. Besides, I drive past your place on the way home, so it's not like it takes any time away from me."

    tsukune "I guess you're right."

    scene bg_car_driver with dissolve

    tsukune "So, remember the girl I was telling you about earlier?"

    you "Yeah, the coffee shop girl."

    tsukune "Her name is Claudia. She's really nice."

    you "{i}Claudia... No, there's no way that he's talking about the same Claudia...{/i}"

    you "{i}... Right?{/i}"

    tsukune "She's really pretty and I figured that we could start off with just talking."

    you "Do you have a picture of her?"

    scene bg_car_passenger with dissolve

    tsukune "I do! Let me go ahead and grab a picture from her blog."

    you "{i}Wait, she has a blog?! Why didn't I know about this?{/i}"

    tsukune "Alright, I've got it here!"

    scene bg_claudia_coffee_art with dissolve

    tsukune "She mainly shows off her coffee art skills. She was really proud of this one!"

    you "{i}I see... Being a barista seems to be a hobby for her.{/i}"

    $ persistent.journal_unlock = True
    
    $ persistent.claudia_hobby_barista = True
    $ renpy.notify("You wrote info about Claudia in your notebook.")

    scene bg_claudia_selfie_behind with dissolve

    tsukune "She's kinda athletic from what I can tell."

    you "{i}Well I already knew that about her.{/i}"

    you "{i}Then again, this might not be the same Claudia.{/i}"

    you "{i}Wait!{/i}"

    scene bg_claudia_selfie_behind_zoom with dissolve

    you "{i}That tattoo! That's definitely my neighbor!{/i}"

    scene bg_claudia_selfie_smile with dissolve

    tsukune "And then here's what she looks like."

    you "Oh... Wow, she looks amazing."

    $ persistent.journal_unlock = False

menu:

    you "{i}I can't let him talk to her...{/i}"

    "Ask how interested Tsukune is in her.":
        jump chapter_0_question_1a

    "Crash the car.":
        jump chapter_0_question_1b

label chapter_0_question_1a:

    you "So... how interested are you in her?"

    tsukune "I mean, I'm interested, but I'm not exactly committed to anything huge like marriage already. I just met her, after all."

    tsukune "I kinda go by the philosophy that if you haven't known someone for at least two weeks, you won't really know if there's actual interest there, you know?"

    you "{i}That's good to know.{/i}"

    $ persistent.tsukune_claudia_interest = True
    $ persistent.calendar_unlock = True
    $ renpy.notify("You wrote info about tsukune in your notebook.")

    you "Oh, here's your place."

    scene bg_tsukune_apartment_parking_lot with dissolve

    show tsukune neutral

    tsukune "Thanks again for dropping me off. I appreciate you."

    you "It's no problem. See you later."

    hide tsukune with dissolve

    scene black with fade

    jump chapter_0_2

label chapter_0_question_1b:
    stop music

    scene bg_car_driver with dissolve

    you "Screw you, I won't let you have her!"

    tsukune "Wait, what're you talking about."

    scene bg_speedometer_high with dissolve

    tsukune "STOP. {b}STOP!{/b}"

    scene black with fade

    return

label chapter_0_2:

    scene bg_you_apartment_living_room with fade

    you "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"
    
    scene bg_sidewalk

    stop music

    jump chapter_0_end

label chapter_0_end:
    scene bg_you_apartment_living_room

    you "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"

    jump chapter_1_part_1
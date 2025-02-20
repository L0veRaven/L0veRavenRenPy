label chapter_0_part_1:
    
    play music "blurred.mp3"

    scene bg_office with fade

    junetenth """
    Claudia... I wish you knew how much I care about you. You're so kind... So beautiful... It hurts to see you show that same kindness to other people. It should be just me and you.{w=0.5}

    No... It NEEDS to be just me and you.{w=0.5}
    """

    nvl clear

    taro "Hey..."

    show taro neutral

    taro "What're you working on there?"

    you "O-oh, nothing much. I'm just journaling a little bit."

    taro "\*chuckles\* What else are you gonna do during downtime, right?"

    you "Right..."

    taro "Oh, when we get off work, I wanna tell you about someone I met."

    you "Someone you met?"

    taro "Yeah! See, I met a girl at this coffee shop the other day."

    show taro blush

    taro "To be honest, she's kinda cute. I was lucky enough to get her contact info."

    you "Geez, I wish I was lucky enough to get that from my crush..."

    show taro neutral
    
    taro "Don't worry. I'm sure you'll get there soon enough."

    taro "Anyways, I gotta get back to work. Talk more later!"

    hide taro with dissolve

    you "The closest I get with my crush is talking to her since she's my neighbor..."

    you "Oh well, back to work."

    scene black with fade

    you "Oh, it's time to clock out."

    scene bg_car_passenger with fade

    taro "Thanks for driving me, again."

    you "It's no problem. Besides, I drive past your place on the way home, so it's not like it takes any time away from me."

    taro "I guess you're right."

    scene bg_car_driver with dissolve

    taro "So, remember the girl I was telling you about earlier?"

    you "Yeah, the coffee shop girl."

    taro "Her name is Claudia. She's really nice."

    you "{i}Claudia... No, there's no way that he's talking about the same Claudia...{/i}"

    you "{i}... Right?{/i}"

    taro "She's really pretty and I figured that we could start off with just talking."

    you "Do you have a picture of her?"

    scene bg_car_passenger with dissolve

    taro "I do! Let me go ahead and grab a picture from her blog."

    you "{i}Wait, she has a blog?! Why didn't I know about this?{/i}"

    taro "Alright, I've got it here!"

    scene bg_claudia_coffee_art with dissolve

    taro "She mainly shows off her coffee art skills. She was really proud of this one!"

    you "{i}I see... Being a barista seems to be a hobby for her.{/i}"

    $ persistent.claudia_hobby_barista = True
    $ renpy.notify("You wrote info about Claudia in your notebook.")

    scene bg_claudia_selfie_behind with dissolve

    taro "She's kinda athletic from what I can tell."

    you "{i}Well I already knew that about her.{/i}"

    you "{i}Then again, this might not be the same Claudia.{/i}"

    you "{i}Wait!{/i}"

    scene bg_claudia_selfie_behind_zoom with dissolve

    you "{i}That tattoo! That's definitely my neighbor!{/i}"

    scene bg_claudia_selfie_smile with dissolve

    taro "And then here's what she looks like."

    you "Oh... Wow, she looks amazing."

menu:

    you "{i}I can't let him talk to her...{/i}"

    "Ask how interested Taro is in her.":
        jump chapter_0_question_1a

    "Crash the car.":
        jump chapter_0_question_1b

label chapter_0_question_1a:

    you "So... how interested are you in her?"

    taro "I mean, I'm interested, but I'm not exactly committed to anything huge like marriage already. I just met her, after all."

    taro "I kinda go by the philosophy that if you haven't known someone for at least two weeks, you won't really know if there's actual interest there, you know?"

    you "{i}That's good to know.{/i}"

    $ persistent.taro_claudia_interest = True
    $ persistent.calendar_unlock = True
    $ renpy.notify("You wrote info about Taro in your notebook.")

    you "Oh, here's your place."

    scene bg_taro_apartment_parking_lot with dissolve

    show taro neutral

    taro "Thanks again for dropping me off. I appreciate you."

    you "It's no problem. See you later."

    hide taro with dissolve

    scene black with fade

    jump chapter_0_part_2

label chapter_0_question_1b:
    stop music

    scene bg_car_driver with dissolve

    you "Screw you, I won't let you have her!"

    taro "Wait, what're you talking about."

    scene bg_speedometer_high with dissolve

    taro "STOP. {b}STOP!{/b}"

    scene black with fade

    return

label chapter_0_part_2:

    scene bg_you_apartment_living_room with fade

    you "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"
    
    scene bg_sidewalk

    stop music

    jump chapter_0_end

label chapter_0_end:
    scene bg_you_apartment_living_room

    you "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!"

    jump chapter_1_part_1
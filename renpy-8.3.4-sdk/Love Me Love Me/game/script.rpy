# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define claudia = Character('Claudia', color="#000000")

define taro = Character('Taro', color="#000000")

define witness = Character('Witness', color="#000000")

define fade = Fade(0.5, 2.0, 0.5)

define you = Character('You', color="#000000", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf")

define nvl_junetenth = Character('June 10th', color="#000000", who_color="#000000", what_color="#000000", kind=nvl, ctc="ctc_arrow", ctc_position="fixed", ctc_pause="ctc_arrow", ctc_timedpause="ctc_arrow", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf", who_size=50, what_size=50)

## Click To Continue
## Button that fades in and out to indicate the player needs to click to progress.

image ctc_arrow:
    "gui/button/right_arrow.png"
    yalign 0.925 xalign 0.81
    linear 0.3 alpha 1.0
    pause 2.0
    linear 0.3 alpha 0.0
    pause 0.2
    repeat

# The game starts here.

label start:

    stop music

    jump chapter_0_part_1

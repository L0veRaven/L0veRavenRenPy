# The script of the game goes in this file.

## VFX ==================================================================
##
## Altered visual effects

define fade = Fade(0.5, 2.0, 0.5)


## Characters ============================================================
##
## Declare characters used by this game. The color argument colorizes the
## name of the character.

define claudia = Character('Claudia', color="#000000")

define taro = Character('Taro', color="#000000")

define witness = Character('Witness', color="#000000")

define you = Character('You', color="#000000", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf")

define junetenth = Character('June 10th', color="#000000", who_color="#000000", what_color="#000000", kind=nvl, ctc="ctc_arrow", ctc_position="fixed", ctc_pause="ctc_arrow", ctc_timedpause="ctc_arrow", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf", who_size=50, what_size=50)


## Click To Continue ==============================================================
##
## Button that fades in and out to indicate the player needs to click to progress.

image ctc_arrow:
    "gui/button/right_arrow.png"
    yalign 0.98 xalign 0.99
    linear 0.3 alpha 1.0
    pause 2.0
    linear 0.3 alpha 0.0
    pause 0.2
    repeat
        
screen say(who, what):
    on "show" action SetVariable("nvl_showing", False)

screen nvl(dialogue, items=None):
    on "show" action SetVariable("nvl_showing", True)


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if renpy.get_mode() == "nvl":
        ## Reverse Dialogue/Nvl Button
        imagebutton:
            auto "gui/button/left_arrow_%s.png"
            xpos 5
            ypos 700
            focus_mask True
            action Rollback()
        
        ## History Button
        imagebutton:
            auto "gui/button/history_%s.png"
            xpos 150
            ypos 700
            focus_mask True
            action ShowMenu('history')
        
        ## Skip Button
        imagebutton:
            auto "gui/button/double_arrow_right_%s.png"
            xpos 300
            ypos 700
            focus_mask True
            action Skip() alternate Skip(fast=True, confirm=True)
        
        ## Save Button
        imagebutton:
            auto "gui/button/save_%s.png"
            xpos 1500
            ypos 700
            focus_mask True
            action ShowMenu('save')
        
        ## Auto Progress Button
        imagebutton:
            auto "gui/button/auto_%s.png"
            xpos 450
            ypos 700
            focus_mask True
            action Preference("auto-forward", "toggle")
        
        ## Quick Save Button
        imagebutton:
            auto "gui/button/quick_save_%s.png"
            xpos 1650
            ypos 700
            focus_mask True
            action QuickSave()

        ## Quick Load Button
        imagebutton:
            auto "gui/button/quick_load_%s.png"
            xpos 1800
            ypos 700
            focus_mask True
            action QuickLoad()
        
        ## Title Screen Button
        imagebutton:
            auto "gui/button/home_%s.png"
            xpos 1800
            ypos 20
            focus_mask True
            action MainMenu()
    else:
        ## Reverse Dialogue/Nvl Button
        imagebutton:
            auto "gui/button/left_arrow_%s.png"
            xpos 5
            ypos 700
            focus_mask True
            action Rollback()
        
        ## History Button
        imagebutton:
            auto "gui/button/history_%s.png"
            xpos 150
            ypos 700
            focus_mask True
            action ShowMenu('history')
        
        ## Skip Button
        imagebutton:
            auto "gui/button/double_arrow_right_%s.png"
            xpos 300
            ypos 700
            focus_mask True
            action Skip() alternate Skip(fast=True, confirm=True)
        
        ## Save Button
        imagebutton:
            auto "gui/button/save_%s.png"
            xpos 1500
            ypos 700
            focus_mask True
            action ShowMenu('save')
        
        ## Auto Progress Button
        imagebutton:
            auto "gui/button/auto_%s.png"
            xpos 450
            ypos 700
            focus_mask True
            action Preference("auto-forward", "toggle")
        
        ## Quick Save Button
        imagebutton:
            auto "gui/button/quick_save_%s.png"
            xpos 1650
            ypos 700
            focus_mask True
            action QuickSave()

        ## Quick Load Button
        imagebutton:
            auto "gui/button/quick_load_%s.png"
            xpos 1800
            ypos 700
            focus_mask True
            action QuickLoad()
        
        ## Title Screen Button
        imagebutton:
            auto "gui/button/home_%s.png"
            xpos 1800
            ypos 20
            focus_mask True
            action MainMenu()

# The game starts here.

label start:

    stop music

    jump chapter_0_part_1
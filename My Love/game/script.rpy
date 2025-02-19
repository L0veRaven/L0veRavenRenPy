# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

## Click To Continue
## Button that fades in and out to indicate the player needs to click to progress.

image ctc_arrow:
    "gui/button/right_arrow.png"
    yalign 0.98 xalign 0.99
    linear 0.3 alpha 1.0
    pause 2.0
    linear 0.3 alpha 0.0
    pause 0.2
    repeat


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.

init python:
    config.overlay_screens.append("quick_menu")

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if renpy.get_mode() == "nvl":
        ## Reverse Dialogue/Nvl Button
        imagebutton:
            auto "gui/button/hover_idle/left_arrow_%s.png"
            xpos 10
            ypos 20
            focus_mask True
            action Rollback()
        
        ## History Button
        imagebutton:
            auto "gui/button/hover_idle/history_%s.png"
            xpos 15
            ypos 150
            focus_mask True
            action ShowMenu('history')
        
        ## Skip Button
        imagebutton:
            auto "gui/button/hover_idle/fast_forward_%s.png"
            xpos 15
            ypos 280
            focus_mask True
            action Skip() alternate Skip(fast=True, confirm=True)
        
        ## Auto Progress Button
        imagebutton:
            auto "gui/button/hover_idle/auto_%s.png"
            xpos 15
            ypos 415
            focus_mask True
            action Preference("auto-forward", "toggle")
        
        ## Save Button
        imagebutton:
            auto "gui/button/hover_idle/save_%s.png"
            xpos 1800
            ypos 600
            focus_mask True
            action ShowMenu('save')
        
        ## Quick Save Button
        imagebutton:
            auto "gui/button/hover_idle/quick_save_%s.png"
            xpos 1800
            ypos 475
            focus_mask True
            action QuickSave()

        ## Quick Load Button
        imagebutton:
            auto "gui/button/hover_idle/quick_load_%s.png"
            xpos 1800
            ypos 350
            focus_mask True
            action QuickLoad()
        
        ## Title Screen Button
        imagebutton:
            auto "gui/button/hover_idle/home_%s.png"
            xpos 1800
            ypos 20
            focus_mask True
            action MainMenu()
        
        ## Settings Button
        imagebutton:
            auto "gui/button/hover_idle/journal_%s.png"
            xpos 1800
            ypos 150
            focus_mask True
            action ShowMenu('preferences')
    else:
        ## Reverse Dialogue/Nvl Button
        imagebutton:
            auto "gui/button/hover_idle/left_arrow_%s.png"
            xpos 5
            ypos 700
            focus_mask True
            action Rollback()
        
        ## History Button
        imagebutton:
            auto "gui/button/hover_idle/history_%s.png"
            xpos 135
            ypos 700
            focus_mask True
            action ShowMenu('history')
        
        ## Skip Button
        imagebutton:
            auto "gui/button/hover_idle/fast_forward_%s.png"
            xpos 275
            ypos 700
            focus_mask True
            action Skip() alternate Skip(fast=True, confirm=True)
        
        ## Auto Progress Button
        imagebutton:
            auto "gui/button/hover_idle/auto_%s.png"
            xpos 400
            ypos 700
            focus_mask True
            action Preference("auto-forward", "toggle")
        
        ## Save Button
        imagebutton:
            auto "gui/button/hover_idle/save_%s.png"
            xpos 1550
            ypos 700
            focus_mask True
            action ShowMenu('save')
        
        ## Quick Save Button
        imagebutton:
            auto "gui/button/hover_idle/quick_save_%s.png"
            xpos 1675
            ypos 700
            focus_mask True
            action QuickSave()

        ## Quick Load Button
        imagebutton:
            auto "gui/button/hover_idle/quick_load_%s.png"
            xpos 1800
            ypos 700
            focus_mask True
            action QuickLoad()

        ## Settings Button
        imagebutton:
            auto "gui/button/hover_idle/journal_%s.png"
            xpos 1800
            ypos 150
            focus_mask True
            action ShowMenu('preferences')
        
        ## Title Screen Button
        imagebutton:
            auto "gui/button/hover_idle/home_%s.png"
            xpos 1800
            ypos 20
            focus_mask True
            action MainMenu()


## Love Meter ################################################
## Relationship levels in visual form

init python:
    max_love=100
    current_love_Claudia=0
    current_love_Taro=50
    show_stats=False
   
    def stats_overlay():
        if show_stats:
            ui.frame()
            ui.vbox()
            ui.text("Claudia")
            ui.bar(max_love,current_love_Claudia, xmaximum=150)

            ui.text("Taro")
            ui.bar(max_love,current_love_Taro, xmaximum=150)

            ui.close()
                       
    config.overlay_functions.append(stats_overlay)


# The game starts here.

label start:

    $ show_stats=True
    
    "Game start"

    $ current_love_Claudia+=10

    "Increase Olivia love point"

    $ current_love_Taro-=10

    "Decrease McKenzie love point"
    
    $ show_stats=False

    stop music

    jump chapter_0_part_1
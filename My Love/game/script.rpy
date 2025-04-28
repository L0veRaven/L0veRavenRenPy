# The script of the game goes in this file.

init offset = -1

## Click To Continue
## Button that fades in and out to indicate the player needs to click to progress.

#image ctc_arrow:
#    "gui/button/right_arrow.png"
#    yalign 0.98 xalign 0.99
#    linear 0.3 alpha 1.0
#    pause 2.0
#    linear 0.3 alpha 0.0
#    pause 0.2
#    repeat


define config.window_auto_hide = [ "scene", "menu", "pause", "hide" ]

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
##
## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.

init python:
    config.overlay_screens.append("quick_menu")

#######################################################################
## Love Meter #########################################################
##
## Relationship levels in visual form

init python:
    max_love=100
    current_love_Claudia=0
    current_love_Tsukune=25
    Tsukune_Claudia_interest=False
   
    def stats_overlay():
        if Tsukune_Claudia_interest:
            ui.frame()
            ui.vbox()
            ui.text("Claudia")
            ui.bar(max_love,current_love_Claudia, xmaximum=150)

            ui.text("Tsukune")
            ui.bar(max_love,current_love_tsukune, xmaximum=150)

            ui.close()

    config.overlay_functions.append(stats_overlay)

    ######################################
    ## In-Game Use

    #$ Tsukune_Claudia_interest=True
        ## Show love bars
    #$ Tsukune_Claudia_interest=False
        ## Hide love bars

    #$ current_love_Claudia+=10
        ## Increase Claudia's love points
    #$ current_love_Tsukune-=10
        ## Decrease Tsukune's love points
#######################################################################




#######################################################################
## GAME START #########################################################
##

label start:
    stop music fadeout 1.0

    window auto
    
    $ persistent.quick_menu_display = False

    jump chapter_0_start
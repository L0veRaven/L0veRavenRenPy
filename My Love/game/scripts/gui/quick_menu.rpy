## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 200

    fixed:
        imagebutton auto "gui/button/hover_idle/left_arrow_%s.png" action Rollback() style style.guiBack

        imagebutton auto "gui/button/hover_idle/history_%s.png" action ShowMenu('history') style style.guiHistory

        imagebutton auto "gui/button/hover_idle/fast_forward_%s.png" action Skip() alternate Skip(fast=True, confirm=True) style style.guiSkip

        imagebutton auto "gui/button/hover_idle/auto_%s.png" action Preference("auto-forward", "toggle") style style.guiAuto

        imagebutton auto "gui/button/hover_idle/save_%s.png" action ShowMenu('save') style style.guiSave

        imagebutton auto "gui/button/hover_idle/quick_save_%s.png" action QuickSave() style style.guiQuickSave

        imagebutton auto "gui/button/hover_idle/quick_load_%s.png" action QuickLoad() style style.guiQuickLoad

        imagebutton auto "gui/button/hover_idle/settings_%s.png" action ShowMenu('settings') style style.guiSettings


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style guiBack:
    xpos 5
    ypos 15

style guiHistory:
    xpos 5
    ypos 15

style guiSkip:
    xpos 5
    ypos 15

style guiAuto:
    xpos 5
    ypos 15

style guiSave:
    xpos 5
    ypos 15

style guiQuickSave:
    xpos 5
    ypos 15

style guiQuickLoad:
    xpos 5
    ypos 15

style guiSettings:
    xpos 5
    ypos 15

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 200

    fixed:
        if persistent.cutscene_off:
            imagebutton auto "gui/button/hover_idle/left_arrow_%s.png":
                style style.guiBack
                action Rollback()

            imagebutton auto "gui/button/hover_idle/history_%s.png":
                style style.guiHistory
                action ShowMenu('history')

            imagebutton auto "gui/button/hover_idle/fast_forward_%s.png":
                style style.guiSkip
                action Skip() alternate Skip(fast=True, confirm=True)

            imagebutton auto "gui/button/hover_idle/auto_%s.png":
                style style.guiAuto
                action Preference("auto-forward", "toggle")

            imagebutton auto "gui/button/hover_idle/save_%s.png":
                style style.guiSave
                action ShowMenu('save')

            imagebutton auto "gui/button/hover_idle/quick_save_%s.png":
                style style.guiQuickSave
                action QuickSave()

            imagebutton auto "gui/button/hover_idle/quick_load_%s.png":
                style style.guiQuickLoad
                action QuickLoad()

            imagebutton auto "gui/button/hover_idle/settings_%s.png":
                style style.guiSettings
                action ShowMenu('preferences')

            if persistent.journal_unlock:
                imagebutton auto "gui/button/hover_idle/journal_%s.png":
                    style style.guiJournal
                    action ShowMenu('InGameMenu')

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
            
            if persistent.journal_unlock:
                ## Game Menu Button
                imagebutton:
                    auto "gui/button/hover_idle/journal_%s.png"
                    xpos 1800
                    ypos 150
                    focus_mask True
                    action ShowMenu('InGameMenu')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style guiBack:
    xpos 320
    ypos 990

style guiHistory:
    xpos 55
    ypos 700

style guiSkip:
    xpos 160
    ypos 700

style guiAuto:
    xpos 255
    ypos 700

style guiSave:
    xpos 1590
    ypos 700

style guiQuickSave:
    xpos 1700
    ypos 700

style guiQuickLoad:
    xpos 1800
    ypos 700

style guiSettings:
    xpos 1800
    ypos 15

style guiJournal:
    xpos 1800
    ypos 150

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
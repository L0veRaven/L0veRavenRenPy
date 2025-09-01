#######################################################################
## Quick Menu
#######################################################################
## Main buttons when in-game:
## Rewind, Skip, Save, Settings
#######################################################################

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 200

    fixed:
        if persistent.quick_menu_display:
            vbox:
                yalign 1.0
                xalign 0.0
                spacing 50

                ## Rewind
                imagebutton:
                    auto "gui/button/hover_idle/left_arrow_%s.png"
                    focus_mask True
                    xpos 50
                    action Rollback()

                imagebutton:
                    auto "gui/button/hover_idle/fast_forward_%s.png"
                    focus_mask True
                    xpos 50
                    action Skip() alternate Skip(fast=True, confirm=True)

            vbox:
                yalign 1.0
                xalign 1.0
                spacing 50

                imagebutton:
                    auto "gui/button/hover_idle/save_%s.png"
                    focus_mask True
                    xpos -50
                    action ShowMenu('save')

                imagebutton:
                    auto "gui/button/hover_idle/ib_settings_%s.png"
                    focus_mask True
                    xpos -50
                    action ShowMenu('preferences')

            #hbox:
            #    style_prefix "quick"
            #
            #    xalign 0.5
            #    yalign 1.0
            #    spacing 50

                #imagebutton:
                #    auto "gui/button/hover_idle/history_%s.png"
                #    focus_mask True
                #    action ShowMenu('history')

                #textbutton _("Auto"):
                #    action Preference("auto-forward", "toggle")

                #textbutton _("Q.Save"):
                #    action QuickSave()

                #textbutton _("Q.Load"):
                #    action QuickLoad()



## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True
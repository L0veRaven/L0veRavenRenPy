## Navigation #########################################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 0
define gui.navigation_ypos = 40

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 10

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

#define gui.navigation_button_width = 250

screen navigation():
    
    hbox:
        style_prefix "navigation"

        xalign 0.5
        ypos 125
        spacing 100

        if not main_menu:
            imagebutton:
                auto "gui/button/hover_idle/save_%s.png"
                focus_mask True
                action ShowMenu("save")

        imagebutton:
            auto "gui/button/hover_idle/small_load_%s.png"
            focus_mask True
            action ShowMenu("load")

        imagebutton:
            auto "gui/button/hover_idle/small_settings_%s.png"
            focus_mask True
            action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            imagebutton:
                auto "gui/button/hover_idle/small_home_%s.png"
                focus_mask True
                action MainMenu()

        imagebutton:
            auto "gui/button/hover_idle/small_credits_%s.png"
            focus_mask True
            action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            imagebutton:
                auto "gui/button/hover_idle/small_help_%s.png"
                focus_mask True
                action ShowMenu("help")

        if renpy.variant("pc"):
            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton:
                auto "gui/button/hover_idle/small_close_%s.png"
                focus_mask True
                action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")
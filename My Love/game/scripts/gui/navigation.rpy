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

        xpos gui.navigation_xpos
        ypos gui.navigation_ypos

        spacing gui.navigation_spacing

        textbutton _("History") action ShowMenu("history")

        textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            imagebutton:
                auto "gui/button/hover_idle/home_%s.png"
                focus_mask True
                action MainMenu()


        textbutton _("Credits") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")
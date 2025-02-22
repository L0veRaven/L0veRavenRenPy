## Navigation screen ###########################################################
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

screen navigation_title():

    fixed:

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help"):
                xpos 440
                ypos 195
                action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit"):
                xpos 1410
                ypos 203
                action Quit(confirm=not main_menu)

        textbutton _("Start"):
            xpos 700
            ypos 665
            action Start()

        textbutton _("Load"):
            xpos 1125
            ypos 663
            action ShowMenu("load")

        textbutton _("Settings"):
            xpos 685
            ypos 807
            action ShowMenu("preferences")

        textbutton _("Credits"):
            xpos 1110
            ypos 810
            action ShowMenu("about")

style navigation_title_button is gui_button
style navigation_title_button_text is gui_button_text

style navigation_title_button:
    size_group "navigation"
    properties gui.button_properties("navigation_title_button")

style navigation_title_button_text:
    properties gui.text_properties("navigation_title_button")










screen navigation():

    hbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        ypos gui.navigation_ypos

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

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
## Navigation ONLY for the Title Screen

screen title_screen_nav():

    fixed:
        $ tooltip = GetTooltip()
        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ## Help isn't necessary or relevant to mobile devices.

            #TODO: Make tooltip hover for "Help" button
            fixed:
                imagebutton:
                    auto "gui/button/hover_idle/settings_%s.png"
                    xpos 440
                    ypos 500
                    focus_mask True
                    action ShowMenu("help")
                    tooltip "Settings"

                if tooltip:
                    text "[tooltip]":
                        xpos 400
                        ypos 600
                        size 70

            #TODO: Remove textbutton "Help" when imagebutton is complete
            textbutton _("Help"):
                xpos 440
                ypos 195
                text_style "navigationTitleTextButton"
                action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.

            #TODO: Make imagebutton tooltip hover for "Quit"

            #TODO: Remove textbutton "Quit" when imagebutton is complete
            textbutton _("Quit"):
                xpos 1410
                ypos 203
                text_style "navigationTitleTextButton"
                action Quit(confirm=not main_menu)

        #TODO: Make imagebutton tooltip hover for "Start"
        #TODO: Remove textbutton "Start" when imagebutton is complete
        textbutton _("Start"):
            xpos 700
            ypos 665
            text_style "navigationTitleTextButton"
            action Start()

        #TODO: Make imagebutton tooltip hover for "Load"
        #TODO: Remove textbutton "Load" when imagebutton is complete
        textbutton _("Load"):
            xpos 1125
            ypos 663
            text_style "navigationTitleTextButton"
            action ShowMenu("load")

        #TODO: Make imagebutton tooltip hover for "Settings"
        #TODO: Remove textbutton "Settings" when imagebutton is complete
        textbutton _("Settings"):
            xpos 685
            ypos 807
            text_style "navigationTitleTextButton"
            action ShowMenu("preferences")

        #TODO: Make imagebutton tooltip hover for "Credits"
        #TODO: Remove textbutton "Credits" when imagebutton is complete
        textbutton _("Credits"):
            xpos 1110
            ypos 810
            text_style "navigationTitleTextButton"
            action ShowMenu("about")
        

style navigationTitleTextButton:
    size 50
    color '#000000'
    hover_color '#575757'
    selected_color '#000000'
    insensitive_color '#4242427f'
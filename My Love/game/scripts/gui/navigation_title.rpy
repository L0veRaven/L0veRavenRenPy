## Navigation ONLY for the Title Screen

screen navigation_title():

    fixed:

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help"):
                xpos 440
                ypos 195
                text_style "navigationTitleTextButton"
                action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit"):
                xpos 1410
                ypos 203
                text_style "navigationTitleTextButton"
                action Quit(confirm=not main_menu)

        textbutton _("Start"):
            xpos 700
            ypos 665
            text_style "navigationTitleTextButton"
            action Start()

        textbutton _("Load"):
            xpos 1125
            ypos 663
            text_style "navigationTitleTextButton"
            action ShowMenu("load")

        textbutton _("Settings"):
            xpos 685
            ypos 807
            text_style "navigationTitleTextButton"
            action ShowMenu("preferences")

        textbutton _("Credits"):
            xpos 1110
            ypos 810
            text_style "navigationTitleTextButton"
            action ShowMenu("about")

style navigationTitleTextButton:
    size 70
    color '#000000'
    hover_color '#575757'
    selected_color '#000000'
    insensitive_color '#4242427f'
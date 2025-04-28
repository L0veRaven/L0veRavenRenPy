## Navigation - Title Screen #############################

screen title_screen_nav():

    $ tooltip = GetTooltip()

    fixed:

        hbox:
            xalign 0.5
            ypos 750

            spacing 220

            imagebutton:
                auto "gui/button/hover_idle/ib_start_%s.png"
                focus_mask True
                action Start()

            imagebutton:
                auto "gui/button/hover_idle/ib_load_%s.png"
                focus_mask True
                action ShowMenu("load")

            imagebutton:
                auto "gui/button/hover_idle/ib_credits_%s.png"
                focus_mask True
                action ShowMenu("about")

            imagebutton:
                auto "gui/button/hover_idle/ib_settings_%s.png"
                focus_mask True
                action ShowMenu("preferences")

        hbox:
            xalign 0.5
            ypos 125
            spacing 980

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                imagebutton:
                    auto "gui/button/hover_idle/ib_help_%s.png"
                    focus_mask True
                    action ShowMenu("help")
        
            if renpy.variant("pc"): ## Quit button useless on iOS, Android, and Web.
                imagebutton:
                    auto "gui/button/hover_idle/ib_close_%s.png"
                    focus_mask True
                    action Quit(confirm=not main_menu)

        fixed:
            text _("{font=you_font.ttf}My Love"):
                style "titleText"

style titleText:
    xalign 0.5
    ypos 350
    size 150
    color '#000000'
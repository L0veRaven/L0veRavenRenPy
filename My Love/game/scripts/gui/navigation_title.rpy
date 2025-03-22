init python:
    ibStart = False
    ibLoad = False
    ibCredits = False
    ibSettings = False
    ibHelp = False
    ibClose = False

transform fade_inout_2s:
        pause 2
        ease 1 alpha 0.0
        pause 2
        ease 1 alpha 1.0
        repeat

transform fade_inout_4s:
        alpha 0.0
        pause 2
        ease 1 alpha 1.0
        pause 2
        ease 1 alpha 0.0
        repeat

## Navigation ONLY for the Title Screen

screen title_screen_nav():

    $ tooltip = GetTooltip()

    #TODO: Make imagebutton tooltip hover for "Start"
    fixed:

        hbox:
            xalign 0.5
            ypos 750

            spacing 100

            vbox:
                imagebutton:
                    auto "gui/button/hover_idle/ib_start_%s.png"
                    focus_mask True
                    tooltip "Start"
                    hovered ToggleVariable("ibStart", True) #Shows Start() [tooltip] on hover
                    unhovered ToggleVariable("ibStart", False) #Hides Start() [tooltip] on unhover
                    action Start()
                
                if ibStart:
                    text tooltip:
                        style "navigationTitleTextButton"
                        color '#000000'

            vbox:
                #TODO: Make imagebutton tooltip hover for "Load"
                #TODO: Remove textbutton "Load" when imagebutton is complete
                imagebutton:
                    auto "gui/button/hover_idle/ib_load_%s.png"
                    focus_mask True
                    tooltip "Load"
                    hovered ToggleVariable("ibLoad", True) #Shows ShowMenu("load") [tooltip] on hover
                    unhovered ToggleVariable("ibLoad", False) #Hides ShowMenu("load") [tooltip] on unhover
                    action ShowMenu("load")
                
                if ibLoad:
                    text tooltip:
                        style "navigationTitleTextButton"
                        color '#000000'

            vbox:
                imagebutton:
                    auto "gui/button/hover_idle/ib_settings_%s.png"
                    focus_mask True
                    tooltip "Credits"
                    hovered ToggleVariable("ibCredits", True) #Shows ShowMenu("about") [tooltip] on hover
                    unhovered ToggleVariable("ibCredits", False) #Hides ShowMenu("about") [tooltip] on unhover
                    action ShowMenu("about")
                
                if ibCredits:
                    text tooltip:
                        style "navigationTitleTextButton"
                        color '#000000'

            vbox:
                #TODO: Make text hover for "Settings" button
                imagebutton:
                    auto "gui/button/hover_idle/ib_settings_%s.png"
                    focus_mask True
                    tooltip "Settings" #Tooltip text
                    hovered ToggleVariable("ibSettings", True) #Shows ShowMenu("preferences") [tooltip] on hover
                    unhovered ToggleVariable("ibSettings", False) #Shows ShowMenu("preferences") [tooltip] on unhover
                    action ShowMenu("preferences")
                
                if ibSettings:
                    text tooltip:
                        style "navigationTitleTextButton"
                        color '#000000'

        hbox:
            xalign 0.5
            ypos 125
            spacing 975

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                vbox:
                    #TODO: Remove textbutton "Help" when imagebutton is complete
                    imagebutton:
                        auto "gui/button/hover_idle/ib_help_%s.png"
                        focus_mask True
                        tooltip "Help"
                        hovered ToggleVariable("ibHelp", True) #Shows ShowMenu("help") [tooltip] on hover
                        unhovered ToggleVariable("ibHelp", False) #Hides ShowMenu("help") [tooltip] on unhover
                        action ShowMenu("help")
                        
                    if ibHelp:
                        text tooltip:
                            style "navigationTitleTextButton"
                            color '#000000'
        
            if renpy.variant("pc"): ## Quit button useless on iOS, Android, and Web.
                vbox:
                    #TODO: Make text hover for "Exit" button
                    imagebutton:
                        auto "gui/button/hover_idle/ib_close_%s.png"
                        focus_mask True
                        tooltip "Quit" #Tooltip text
                        hovered ToggleVariable("ibClose", True) #Shows ShowMenu("preferences") [tooltip] on hover
                        unhovered ToggleVariable("ibClose", False) #Shows ShowMenu("preferences") [tooltip] on unhover
                        action Quit(confirm=not main_menu)
                    
                    if ibClose:
                        text tooltip:
                            style "navigationTitleTextButton"
                            color '#000000'

        text _("{font=you_font.ttf}My Love") at fade_inout_2s:
            style "titleText"

        text _("{font=claudia_font.ttf}My Love") at fade_inout_4s:
            style "titleText"

        #text _("{font=tsukune_font.ttf}My Love"):
            #style "titleText"
        

style navigationTitleTextButton:
    xalign 0.5
    ypos -70
    size 50
    color '#000000'
    hover_color '#575757'
    selected_color '#000000'
    insensitive_color '#4242427f'

style titleText:
    xalign 0.5
    ypos 350
    size 150
    color '#000000'
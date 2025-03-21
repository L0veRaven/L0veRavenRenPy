init python:
    ibStart = False
    ibSettings = False
    ibClose = False

## Navigation ONLY for the Title Screen

screen title_screen_nav():

    $ tooltip = GetTooltip()

    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        fixed:
            #TODO: Remove textbutton "Help" when imagebutton is complete
            textbutton _("Help"):
                xpos 440
                ypos 195
                text_style "navigationTitleTextButton"
                action ShowMenu("help")


    #TODO: Make imagebutton tooltip hover for "Start"
    fixed:
        xpos 275
        ypos 750

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
                    xalign 0.5
                    ypos -80
                    textalign 0.5
                    color '#000000'

    #TODO: Make imagebutton tooltip hover for "Load"
    #TODO: Remove textbutton "Load" when imagebutton is complete
    textbutton _("Load"):
        xpos 1125
        ypos 663
        text_style "navigationTitleTextButton"
        action ShowMenu("load")

    #TODO: Make imagebutton tooltip hover for "Credits"
    #TODO: Remove textbutton "Credits" when imagebutton is complete
    textbutton _("Credits"):
        xpos 1110
        ypos 810
        text_style "navigationTitleTextButton"
        action ShowMenu("about")
    
    fixed:
        xpos 1440
        ypos 750

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
                    xalign 0.5
                    ypos -80
                    style "navigationTitleTextButton"
                    color '#000000'
    
    if renpy.variant("pc"):

        ## The quit button is banned on iOS and unnecessary on Android and
        ## Web.
        fixed:
            xpos 1440
            ypos 125

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
                        xalign 0.5
                        ypos -80
                        style "navigationTitleTextButton"
                        color '#000000'
        

style navigationTitleTextButton:
    size 50
    color '#000000'
    hover_color '#575757'
    selected_color '#000000'
    insensitive_color '#4242427f'
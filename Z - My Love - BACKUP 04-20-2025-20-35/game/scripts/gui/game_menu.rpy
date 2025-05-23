## Game Menu - Title ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

## Accessible:
    ## Title Menu: Load/Settings/Credits/Help
    ## In-game: Right-click

#TODO: "screen game_menu" use imagebuttons instead of textbuttons
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

    frame:
        style "game_menu_content_frame"

        if scroll == "viewport":

            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    spacing spacing

                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                cols 1
                yinitial yinitial

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                spacing spacing

                transclude

        else:

            transclude

    use navigation

    #textbutton _("Return"):
    #    style "return_button"
    #
    #    action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

## Position of game menu content
style game_menu_content_frame:
    left_margin 300
    top_margin 250
    bottom_margin 100

## Width of game menu content
style game_menu_viewport:
    xsize 1325

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

## Spacing of scrollbar
style game_menu_side:
    spacing 0

style return_button:
    xpos gui.navigation_xpos
    yalign 0.0

## Game Menu - In-Game ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen InGameMenu(scroll=True):

    tag menu

    style_prefix "InGameMenu"

    add "gui/overlay/game_menu.png"

    frame:
        style "InGameMenu_content_frame"

        if scroll == "viewport":

            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    spacing spacing

                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                cols 1
                yinitial yinitial

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                spacing spacing

                transclude

        else:

            transclude

    use navigation

    #textbutton _("Return"):
    #    style "return_button"
    #
    #    action Return()


style InGameMenu_outer_frame is empty
style InGameMenu_navigation_frame is empty
style InGameMenu_content_frame is empty
style InGameMenu_viewport is gui_viewport
style InGameMenu_side is gui_side
style InGameMenu_scrollbar is gui_vscrollbar

style InGameMenu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

## Position of game menu content
style InGameMenu_content_frame:
    left_margin 725
    top_margin 130
    bottom_margin 100

## Width of game menu content
style InGameMenu_viewport:
    xsize 600

style InGameMenu_vscrollbar:
    unscrollable gui.unscrollable

## Spacing of scrollbar
style InGameMenu_side:
    spacing 0
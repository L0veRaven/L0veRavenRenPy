## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about_audio = _p("""
Title\n
{a=https://ko-fi.com/s/ab76dd25a9}{i}Blurred{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 0\n
scene5 by KADOKAWA's {a=https://www.rpgmakerweb.com/products/rpg-maker-mz}RPG Maker MZ{/a}\n
{a=https://ko-fi.com/s/f0e8490a78}{i}Shiny{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 1\n
{a=https://ko-fi.com/s/38443fd4f1}{i}Triangle Elevator{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 2\n
{a=https://ko-fi.com/s/045759065c}{i}People Factory{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 3\n
{a=https://ko-fi.com/s/9244c061a3}{i}Strawberry Blossoms{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 4\n
{a=https://ko-fi.com/s/c58a72ebbf}{i}Karmic Blunder{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 5\n
{a=https://ko-fi.com/s/894338d609}{i}Contact Glow{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 6\n
{a=https://ko-fi.com/s/91c0372829}{i}Polar Float{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}\n

Chapter 7\n
{a=https://ko-fi.com/s/1896a262c9}{i}Swim On, Little One{/i}{/a} by {a=https://x.com/SquaLLio777}SquaLLio{/a}
""")

define gui.about_plugins = _p("""
{a=https://wattson.itch.io/}{b}Wattson{/b}{/a} ~ {a=https://wattson.itch.io/kinetic-text-tags}{i}Kinetic Text Tags{/i}{/a}
""")

define gui.about_software = _p("""
{a=https://procreate.com/}Procreate{/a}

{a=https://procreate.com/}Krita{/a}

{a=https://code.visualstudio.com/}Visual Studio Code{/a}

{a=https://www.live2d.com/en/}Live2D Cubism{/a}

{a=https://www.audacityteam.org/}Audacity{/a}\n

And a special thanks to

{a=https://www.renpy.org/}Ren'Py{/a}
""")

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:
            #label "[config.name!t]" xalign 0.5
            #text _("Version [config.version!t]\n") xalign 0.5

            text _("Developed by {a=https://www.l0veraven.com}L0veRaven{/a}\n") xalign 0.5
            text _("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") xalign 0.5
            text _("{u}Audio Credits{/u}\n") xalign 0.5
            text "[gui.about_audio!t]\n" xalign 0.5
            text _("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") xalign 0.5
            text _("{u}Plugin Credits{/u}\n") xalign 0.5
            text "[gui.about_plugins!t]\n" xalign 0.5
            text _("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") xalign 0.5
            text _("{u}Software Used{/u}\n") xalign 0.5
            text "[gui.about_software!t]\n" xalign 0.5
            text _("{image=gui/renpy_credit_icon.png}{alt}RenPy logo{/alt}\n") xalign 0.5


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style about_text:
    textalign 0.5
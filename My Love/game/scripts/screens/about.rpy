## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about_audio = _p("""
{a=https://x.com/SquaLLio777}{b}SquaLLio{/b}{/a}

{a=https://ko-fi.com/s/ab76dd25a9}{i}Blurry{/i}{/a} - Title\n
{a=https://ko-fi.com/s/f0e8490a78}{i}Shiny{/i}{/a} - Chapter 0\n
{a=https://ko-fi.com/s/38443fd4f1}{i}Triangle Elevator{/i}{/a} - source\n
{a=https://ko-fi.com/s/045759065c}{i}People Factory{/i}{/a} - source\n
{a=https://ko-fi.com/s/9244c061a3}{i}Strawberry Blossoms{/i}{/a} - source\n
{a=https://ko-fi.com/s/c58a72ebbf}{i}Karmic Blunder{/i}{/a} - source\n
{a=https://ko-fi.com/s/894338d609}{i}Contact Glow{/i}{/a} - source\n
{a=https://ko-fi.com/s/91c0372829}{i}Polar Float{/i}{/a} - source\n
{a=https://ko-fi.com/s/1896a262c9}{i}Swim On, Little One{/i}{/a} - source

{b}KADOKAWA{/b}

{a=https://www.rpgmakerweb.com/products/rpg-maker-mz}RPG Maker MZ{/a}'s audio assets
""")

define gui.about_software = _p("""
{a=https://procreate.com/}Procreate{/a}

{a=https://procreate.com/}Krita{/a}

{a=https://code.visualstudio.com/}Visual Studio Code{/a}

{a=https://www.live2d.com/en/}Live2D Cubism{/a}

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
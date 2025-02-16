## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
"Love Me Love Me" was developed by L0veRaven.

This project wouldn't be possible without using resources from other creatives.

========= Audio Credits =========

{a="https://x.com/SquaLLio777"}SquaLLio{/a}

{a="https://ko-fi.com/s/f0e8490a78"}"Shiny"{/a}, 
{a="https://ko-fi.com/s/ab76dd25a9"}"Blurry"{/a}, 
{a="https://ko-fi.com/s/38443fd4f1"}"Triangle Elevator"{/a}, 
{a="https://ko-fi.com/s/045759065c"}"People Factory"{/a}, 
{a="https://ko-fi.com/s/9244c061a3"}"Strawberry Blossoms"{/a}, 
{a="https://ko-fi.com/s/c58a72ebbf"}"Karmic Blunder"{/a}, 
{a="https://ko-fi.com/s/894338d609"}"Contact Glow"{/a}, 
{a="https://ko-fi.com/s/91c0372829"}"Polar Float"{/a}, 
{a="https://ko-fi.com/s/1896a262c9"}"Swim On, Little One"{/a}


KADOKAWA

- {a="https://www.rpgmakerweb.com/products/rpg-maker-mz"}RPG Maker MZ's{/a} audio assets


========= Art Software =========

{a="https://procreate.com/"}Procreate{/a} (12.99 USD)

{a="https://procreate.com/"}Krita{/a} (Free)

{a="https://code.visualstudio.com/"}Visual Studio Code{/a} (Free)


========= Hardware =========

iPad 10

Windows 10

Windows 11


========= Animation Software =========

{a=https://www.live2d.com/en/}Live2D Cubism{/a} Pro Version (14.99 USD/month)


========= Game Engine =========

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
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]" xalign 0.5

            text _("Version [config.version!t]\n") xalign 0.5

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]"
                xalign 0.5

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].") xalign 0.5


style about_label is gui_label
style about_label_text is gui_label_text

style about_text is gui_text:
    text_align 0.5

style about_label_text:
    size gui.label_text_size
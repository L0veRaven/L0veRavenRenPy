init offset = -1











style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb_offset 18
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    left_gutter 18

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if csbox:
            background None

        if who is not None and not csbox:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        if csbox:
            text what id "what" font "HELVETICA_LT_NARROW.ttf" color "#f7dd74" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] size 42 xmaximum 950 xoffset 230 yoffset 50
        else:
            text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init python:
    config.character_id_prefixes.append('namebox')


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing -5












screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "choice"
    add Solid("#000000") at translucent(1.0)
    add "gui/choice_window.png"
    vbox:
        xpos 703
        yalign 0.46
        spacing 30

        for i in items:
            textbutton i.caption action [Play("sfx","audio/PhoneSelect.mp3"),i.action]

transform translucent(t):
    alpha 0.0
    linear t alpha 0.6




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")






screen quick_menu():


    zorder 100

    if quick_menu:

        vbox:
            style_prefix "quick"
            spacing -5

        imagebutton:
            idle "gui/back_pills_vert.png"
            action Function(renpy.rollback, force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=False)
            xalign 0.086
            yalign 0.995

        imagebutton:
            idle "gui/pause_phone.png"
            action ShowMenu()
            xalign 0.964
            yalign 0.979








init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button:
    xalign 1.0

style quick_button_text is button_text

style quick_button_text:
    xalign 1.0
    size 50
    color '#000000'
    hover_color '#555555'
    insensitive_color 'FF0000'











screen newgame_hover_bar():

    add "gui/menu 2/hover_bar.png" at from_left(428, 0.0)
    add "gui/menu 2/newgame2_ro.png"

screen continue_hover_bar():

    add "gui/menu 2/hover_bar.png" at from_left(528, -0.03)
    add "gui/menu 2/continue2_ro.png"

screen option_hover_bar():

    add "gui/menu 2/hover_bar.png" at from_left(628, -0.075)
    add "gui/menu 2/options2_ro.png"

screen about_hover_bar():

    add "gui/menu 2/hover_bar.png" at from_left(728, -0.14)
    add "gui/menu 2/about2_ro.png"

transform from_left(posy, x):
    subpixel True xalign -1.0 yanchor 0.5 ypos posy
    linear 0.14 xalign x
    on hide:
        linear 0.48 xalign -1.0

screen navigation():

    style_prefix "navigation"

    imagebutton:
        idle "gui/menu 2/newgame2.png"
        hover "gui/menu 2/newgame2_ro.png"
        xpos 0
        ypos 0
        activate_sound "audio/MainMenuPress.mp3"
        hover_sound "audio/MainMenuRollover.mp3"
        action Hide("newgame_hover_bar"), SetField(persistent, "new_ending", False), Start()

    imagebutton:
        idle "gui/menu 2/continue2.png"
        hover "gui/menu 2/continue2_ro.png"
        xpos 0
        ypos 0
        activate_sound "audio/MainMenuPress.mp3"
        hover_sound "audio/MainMenuRollover.mp3"
        action SetField(persistent, "new_ending", False), ShowMenu("load")

    imagebutton:
        idle "gui/menu 2/options2.png"
        hover "gui/menu 2/options2_ro.png"
        xpos 0
        ypos 0
        activate_sound "audio/MainMenuPress.mp3"
        hover_sound "audio/MainMenuRollover.mp3"
        action SetField(persistent, "new_ending", False), ShowMenu("preferences")

    imagebutton:
        idle "gui/menu 2/about2.png"
        hover "gui/menu 2/about2_ro.png"
        xpos 0
        ypos 0
        activate_sound "audio/MainMenuPress.mp3"
        hover_sound "audio/MainMenuRollover.mp3"
        action SetField(persistent, "new_ending", False), ShowMenu("about")

    imagebutton:
        idle "gui/menu 2/exit2.png"
        hover "gui/menu 2/exit2_ro.png"
        xpos 0
        ypos 0
        activate_sound "audio/MainMenuPress.mp3"
        hover_sound "audio/MainMenuRollover.mp3"
        action SetField(persistent, "new_ending", False), Quit()

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

transform main_logo_transform:
    xalign .7 yalign 0.3 size (580.0*1.2,395.0*1.2) xanchor .5 yanchor .5
    block:
        easein 0.35 size (580.0*1.3, 395.0*1.3)
        linear 1.5 size (580.0*1.2,395.0*1.2)
        repeat







image main_menu_bg = Movie(play = "gui/menu 2/BG living.webm", start_image = "gui/menu 2/menu_bg.png")
image sparkle = DynamicDisplayable(auto_forward_image, images=["SparkleSequence/Sparkles_000" + str(i).zfill(2) + ".png" for i in range(60)])

screen sparkle(x, y):
    zorder 10
    add "sparkle" xpos x - 102 ypos y - 132 at fade_in_out

screen main_menu_bg():
    zorder 1

    add "main_menu_bg"

screen main_menu():
    on "show":
        action Function(renpy.music.stop, channel="vo", fadeout=0.5), Show("main_menu_bg")
    on "replace":
        action Function(renpy.music.stop, channel="vo", fadeout=0.5), Show("main_menu_bg")


    zorder 15 tag menu

    style_prefix "main_menu"

    default buttons = [
        ["newgame2", Start(), 520, 140],
        ["continue2", ShowMenu("load"), 1000, 140],
        ["about2", ShowMenu("about"), 300, 480],
        ["options2", ShowMenu("preferences"), 1250, 480],
        ["exit2", Quit(), 790, 850],
    ]

    if not renpy.get_screen("ending_tracker_screen") and not renpy.get_screen("ending_tracker_hide_screen"):
        imagebutton:
            idle "gui/ending_tracker/text_access.png"

            action Play("sound", "audio/Phone_slide.mp3"), Show("ending_tracker_screen"), With(None)
            xalign 0.96
            yalign 0.925

            at idle_rotate

    add "gui/ClassOf09logo.png" xalign 0.5 yalign 0.5 at zoom_pulse

    for i, a, x, y in buttons:
        imagebutton:
            idle "gui/menu 2/" + i + ".png"
            hover "gui/menu 2/" + i + "_ro.png"

            hovered Show("sparkle", x=x, y=y, _tag="sparkle_{}_{}".format(x, y))
            unhovered Hide("sparkle_{}_{}".format(x, y))

            action SetField(persistent, "new_ending", False), Hide("sparkle_{}_{}".format(x, y)), a, Hide("main_menu_bg")
            xpos x
            ypos y

            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"

            at jitter

    if persistent.new_ending:
        on "show":
            action Play("sound", "audio/NewTextAlert.mp3")
        add "new_message_animation"

transform fade_in_out():
    alpha 0.0
    on show:
        linear 0.2 alpha 1.0
    on hide:
        linear 1 alpha 0.0

transform zoom_pulse():
    zoom 0.16
    linear 0.2 zoom 0.165
    linear 2 zoom 0.16
    linear 0.2 zoom 0.17
    linear 2 zoom 0.16
    linear 0.18 zoom 0.18
    linear 2.4 zoom 0.16
    repeat

transform jitter():
    on idle:
        xoffset 0
        yoffset 0

    on hover:
        parallel:
            linear 0.02 xoffset 1
            linear 0.04 xoffset -1
            linear 0.02 xoffset 0
        parallel:
            linear 0.02 yoffset 1
            linear 0.04 yoffset -1
            linear 0.02 yoffset 0

        repeat

transform idle_rotate:
    rotate 0
    linear 1.0 rotate 3
    linear 1.0 rotate 0
    linear 1.0 rotate 3
    linear 1.0 rotate 0
    repeat

image new_message_animation:
    "NewMessageSequence/NewMessage_0001.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0002.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0003.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0004.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0005.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0006.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0007.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0008.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0009.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0010.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0011.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0012.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0013.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0014.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0015.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0016.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0017.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0018.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0019.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0020.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0021.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0022.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0023.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0024.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0025.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0026.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0027.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0028.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0029.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0030.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0031.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0032.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0033.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0034.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0035.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0036.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0037.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0038.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0039.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0040.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0041.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0042.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0043.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0044.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0045.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0046.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0047.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0048.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0049.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0050.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0051.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0052.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0053.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0054.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0055.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0056.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0057.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0058.png"
    pause 0.041
    "NewMessageSequence/NewMessage_0059.png"
    pause 0.041
    Solid("#00000000")


style alt_menu_frame is empty
style alt_menu_vbox is vbox
style alt_menu_text is gui_text
style alt_menu_label is gui_label
style alt_menu_label_text:
    color '#FFFFFF'

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_button_text:
    size 60

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











transform fade_in(t):
    alpha 0.0
    linear t alpha 1.0

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add "main_menu_bg"
    add "gui/menu 2/menu_backtray.png" at fade_in(0.5):
        alpha 0.65

    frame:
        style "game_menu_outer_frame"
        at fade_in(0.8)

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial

                    side_yfill True

                    has vbox
                    xsize 700
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    edgescroll True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude
            else:
                transclude

    textbutton _("RETURN") text_font "FUTURA.TTF" text_size 120 text_idle_color "#ffffff" text_hover_color "#34bffa":
        action Return()

        xalign 0.025
        yalign 0.95

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 15
    right_padding 60

style game_menu_navigation_frame:
    xsize 500
    yfill True

style game_menu_content_frame:
    left_margin 300
    right_margin 420
    top_margin 20

style game_menu_viewport:
    xsize 1700

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









screen aboutmenu():
    tag menu





    use game_menu(_("About"), scroll="viewport"):
        frame:
            vbox:

                xalign .5
                yalign .5
                spacing 45

        style_prefix "about"
        hbox:
            xsize 200
            ysize 400
            ypos 40
            spacing 20
            textbutton _("ABOUT"):
                text_idle_color "#ffffff"
                text_hover_color "#2cabf5"
                text_selected_color "#AAAAAA"
                action ShowMenu("about")

            textbutton _("ACTORS"):
                text_idle_color "#ffffff"
                text_hover_color "#2cabf5"
                text_selected_color "#AAAAAA"
                action ShowMenu("actors")

            textbutton _("ARTISTS"):
                text_idle_color "#ffffff"
                text_hover_color "#2cabf5"
                text_selected_color "#AAAAAA"
                action ShowMenu("artists")


        viewport:
            scrollbars "vertical" style_prefix "vbar"
            mousewheel True
            draggable True
            xsize 1100
            ypos -263
            side_yfill True
            has vbox
            transclude

style vbar_vscrollbar:
    xpos 10

screen about():
    tag menu
    style_prefix "about"

    use aboutmenu():
        vbox:
            text _("\nThis video game is entirely based on real events, encounters, and personalities. \n \nAny content viewed as offensive is a reflection of American culture and not endorsed by Class of '09 or it's staff.\n\n\nApparently all characters depicted are over 18.\n\n\nAny products, brand names, logos, and any other proprietary designations mentioned in this video game are the property of their respective owners. The inclusion of these items is for illustrative purposes only and does not imply endorsement or affiliation with the owners. The use of any trademarks, service marks, or trade names strictly pertains to cultural reference within the context of historical fiction and does not suggest sponsorship or approval by the trademark owner.\n\n\nThis program contains free software licensed under a number of licenses, including the GNU Lesser General Public License. A complete list of software is available at {a=http://www.renpy.org/doc/html/license.html}http://www.renpy.org/doc/html/license.html{/a}\n\n\n") outlines []

screen actors():
    tag menu
    use aboutmenu():
        hbox:
            spacing 55
            ypos -20
            xpos 5
            vbox:
                style_prefix "actor"
                text actor_credits outlines []
            vbox:
                style_prefix "char"
                text char_credits outlines []

define actor_credits = _("""
Kayli Mills
Elsie Lovelock
Max Field


Katy Johnson
Valerie Rose
Anne Yatco
Don McDonald
Kira Buckland
Tom Schalk
Chris McCullough
Lyle Rath
Josh Tomar
Sarah Ruth Thomas
Corinne Sudberg
Tiana Camacho
Michael Potok
Connor Quinn
Jas Patrick
Joe Boisits
Dreux Ferrano Jr
Anna Kingsley
Gary Scales

Belsheber Rusape
Erin Nicole Lundquist
Bryson Baugus
Haley Parsley
Anna Kingsley
Brandon Winckler
Lizzy Hofe
Michaela Laws
Krystal LaPorte

""")

define char_credits = _("""
JECKA
NICOLE
KYLAR
CRISPIN
JEFFERY
KELLY
EMILY
MS. AMES
JECKA'S DAD
ARI
COUNSELOR
MR. KATZ
MR. BURLEDAY
MALL COP
PRINCIPAL LYNN
KAREN
MEGAN
HUNTER
COP
MR. LORRE
TRODY
COACH COLBY
JECKA'S MOM
METRO

ADD'L STUDENTS










""")

define artist_credits = _("""

{size=24}PUBLISHED BY{/size}
Wrath Club

{size=24}WRITTEN & DIRECTED BY{/size}
SBN3

{size=24}CG ARTISTS{/size}
P-San
Kohaku
NTDanny
The0ne-u-lost
JokobArt

{size=24}SPRITE ARTISTS{/size}
Danny Espinoza
Smex
Dalmax
Rayleigh Scale

{size=24}BG ARTISTS{/size}
OZK
Hauptmannartwork

{size=24}SCORED BY{/size}
Aaron Monroe
Cozine
Hoobastankonia

{size=24}VFX{/size}
Shawn Smith

{size=24}PROGRAMMER{/size}
Dipesh Aggarwal

""")

screen artists():
    tag menu
    style_prefix "artist"
    use aboutmenu():
        hbox:
            ypos -80
            xpos 110
            text artist_credits outlines []




define gui.about = ""

style artist_text:
    size 40
    color '#FFF'
    text_align .5
    outlines [(1, "#000", 0, 0)]
    kerning 1

style about_hbox:
    top_margin 50
    bottom_margin 25

style about_label:
    size 100

style about_label_text:
    size 100

style about_button:
    size 100

style about_button_text:
    size 60
    color '#000000'

style about_label_text:
    size 100

style char_text:
    color '#FFF'
    size 28
    text_align 0.0
    outlines [(1, "#000", 0, 0)]
    kerning 1

style char_hbox:
    top_margin 30

style actor_text:
    color '#FFF'
    size 28
    text_align 1.0
    outlines [(1, "#000", 0, 0)]
    kerning 1

style about_text:
    size 30
    color '#FFF'
    outlines [(1, "#000", 0, 0)]
    kerning 1










screen pause_save():
    tag menu


    use pause_file_slots(_("Save"))

screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:




            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                yalign 0.0
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.2

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                            color "#ffffff"

                        text FileSaveName(slot):
                            style "slot_name_text"
                            color "#ffffff"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.72

                spacing gui.page_spacing

                imagebutton:
                    idle "gui/arrowleft.png"
                    hover "gui/arrowleft.png"
                    action FilePagePrevious()
                    ypos 0.1


                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto"):
                        text_idle_color "#ffffff"
                        text_hover_color "#2cabf5"
                        text_selected_color "#AAAAAA"

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick"):
                        text_idle_color "#ffffff"
                        text_hover_color "#2cabf5"
                        text_selected_color "#AAAAAA"


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page):
                        text_idle_color "#ffffff"
                        text_hover_color "#2cabf5"
                        text_selected_color "#AAAAAA"

                imagebutton:
                    idle "gui/arrowright.png"
                    hover "gui/arrowright.png"
                    action FilePageNext()
                    ypos 0.1


screen pause_file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto saves"), quick=_("Quick saves"))

    add "gui/nvl.png"


    fixed:


        order_reverse True


        button:
            style "page_label"

            key_events True
            xalign 0.5
            yalign 0.0
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value


        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.2

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)


        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 0.75

            spacing gui.page_spacing

            imagebutton:
                idle "gui/arrowleft.png"
                hover "gui/arrowleft.png"
                action FilePagePrevious()


            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto"):
                    text_idle_color "#ffffff"
                    text_hover_color "#2cabf5"
                    text_selected_color "#AAAAAA"

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick"):
                    text_idle_color "#ffffff"
                    text_hover_color "#2cabf5"
                    text_selected_color "#AAAAAA"


            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            imagebutton:
                idle "gui/arrowright.png"
                hover "gui/arrowright.png"
                action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences():
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")




            null height (4 * gui.pref_spacing)

            vbox:
                style_prefix "slider"
                box_wrap True

                vbox:


                    if config.has_sound:

                        label _("{color=#ffffff}Scene Volume{/color}")

                        vbox:
                            bar value Preference("music volume")

                        label _("{color=#ffffff}UI Volume{/color}")

                        vbox:
                            bar value Preference("sound volume")


screen pause_prefs():
    tag menu


    add "gui/nvl.png"
    style_prefix "alt_menu"

    vbox:

        xalign 0.5
        yalign 0.5

        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):

                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")





        null height (4 * gui.pref_spacing)

        vbox:
            style_prefix "slider"
            box_wrap True

            vbox:
                if config.has_sound:

                    label _("Scene Volume")
                    vbox:
                        bar value Preference("music volume")

                    label _("UI Volume")
                    vbox:
                        bar value Preference("sound volume")

                    textbutton _("Return") action Return()


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    color "#ffffff"

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    idle_color "#ffffff"
    hover_color "#2cabf5"
    selected_color "#AAAAAA"

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")
    idle_color "#ffffff"
    hover_color "#2cabf5"
    selected_color "#AAAAAA"

style slider_vbox:
    xsize 675







screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Sure") action yes_action
            textbutton _("Sorry, I'll keep playing.") action no_action



    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        vbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"


style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

init python:
    import datetime

screen search_engine_screen():
    frame:
        xysize (1336, 751)
        align (0.5, 0.5)
        background "laptopsearch/laptopshell.png"

        add "laptopsearch/laptopscreen.png"
        imagebutton:
            idle Solid("#00000000", xysize=(104, 20))
            hover "laptopsearch/laptopsearchrollover.png"

            focus_mask None

            hovered Play("sound", "audio/MainMenuRollover.mp3")

            action [Play("sound", "audio/PhoneSelect.mp3"), Jump("scene_0086")]
            xpos 556
            ypos 285
        add "laptopsearch/laptopscreenoverlay.png"

screen ending_tracker_screen():

    modal True
    zorder 150

    default endings_name = {
        '0030': '703-425-2981     ',
        '0040': '703-960-1431    ',
        '0056': '202-347-4800    ',
        '0081': '703-352-0990    ',
        '0098': 'nicole              ',
    }
    default endings_details = {
        '0030': 'Greetings my queen',
        '0040': ' right number?',
        '0056': 'this is W',
        '0081': 'can you cover',
        '0098': 'why why why why...',
    }
    default ending_text = {
        '0030': 'hewwo dere i saw your FM wisting and wanted to see if I could come to your house to be stepped on by your cute little piggies. My parents named me Frederick but you can call me Freddy Footins! I am 34 years young and have been with the FeetMeet community for about 5 years now. Someone on the forums snapped a pic of your feet without your permission and I pleasured myself to it roughly 9 times.\nWith that icebreaker out of the way, i have saved up about 300 dollars with my SSI checks and would like to hire your services. Unsure if you do any of the more erotic foot sessions but just in case let me list you some more of my fetishes:\n\n-feet (free space lol)\n-choking\n-food play\n-facesitting\n-Mommy incest\n-sister incest\n-twincest\n-simulated kidnapping\n-women wearing the Taco Bell uniform\n-you pretending to be Mexican but then saying you are white after I point out how hot it is that you are Mexican\n-covering my rent this month\n-that last one wasnt a kink but would be pretty cool if you did that\n\nAlso I am not a rapist by definition (looked it up) so no need to google anything about me.\nP.S. havent seen your face yet but if you look roughly 12 i am SO going to try moving out of my parents house down the line one day maybe to date you!\n',
        '0040': 'Hi I\'m not sure if I have the right person but this is Jeffery\'s mother.\n\nWas just texting to thank you for finding his body and alerting the authorities when you did. Unfortunately they were too late but you can\'t blame yourself for that.\nA part of me is devastated but another part of me is relieved, which is horrible to say... Jeffery has never quite fit in with the other children, never had the best grades, and maybe this was the only avenue for him sadly enough. Every day I wondered in the back of my head if I had failed as a mother by raising someone so awkward. By middle school I eventually gave up on him to compartmentalize my insecurities as a parent, letting him play with toys and masturbate to what I assume is animated pornography that I found on his computer.\nI worried he would be hopelessly going through adulthood so this might have been the best outcome for him. He would tell me he was going to work on video games for a job when he was an adult, then it was comic books, then it was making YouTube reviews of action figures. All these things he said he wanted to do and never pursued... my fear was he just wanted to be a child playing with toys forever.\nMy son\'s suicide is bittersweet, on one hand he is gone but on the other he realized himself that life wouldn\'t work out and ended things before they got worse. I KNEW there was a smart boy somewhere inside of Jeffery.\nI also know we have never spoken before but I needed to tell someone who would not have any pre-conceived notions about my pain...and can understand my blunt honesty now.\n\nWhen Jeffery was alive I was insecure. Now that he\'s gone I can feel free.\n\n',
        '0056': 'Heyo this George W Bush from the America White House!\nNot sure if those lesser camel jockeys let you have a phone as a slave but I personally wanted to let you know that Obama has sent a presidential pardon message to the Taliban to let you out. The Taliban ignores most of my messages and will make a grainy VHS tape telling me MacDonalds is the anti-christ or buddha or whatever the hell brown people worship but you get the idea. American girls like you have a bright future and we need to perserve that in ensuring all men are created equal in this race for equal opportunity.\n\n\nP.S. Kanye was right ; )\n',
        '0081': 'This is Ron Stumpford of Dominos Fairfax texting about the tragic passing of Ari. Now that shes dead we dont really have anyone to do deliveries on NFL Thursdays anymore so can you cover for her? We dont care that you killed her drunk driving we just gotta move orders here. Between you and me I am glad you killed her cause I asked her out on a date and she made up some fake excuse that she was gay FUCK THAT BITCH!\nBut please come down and cover for her because the selfish bitch was too inconsiderate to have someone cover for her in the event she died on the job. I told her parents that and they made it out like IM the bad guy.\n\nIf you cant drive for us would you at least have any naked pictures of her or anything? Im trying not to leave this deal empty handed here. Not even her parents had naked pictures of her to send me like what a rip off!',
        '0098': 'why cant u help me',
        '0000': 'Thank you for playing the Class of \'09 visual novel series to completion!\n\nThis project set out to bring real, relatable experiences back into the current lexicon of entertainment through the medium of comedy. Originally it was thought a bunch of people in their early 30s would play these games for a laugh but it turned out people who were barely alive for 2009 gravitated towards it in larger numbers.\n\nMany of the social issues featured in this game were not exclusive to the late 2000s and the teenage portion of our fans lead me to believe times haven\'t changed...\nI also learned that 2-line throwaway jokes qualify as lore for people who need employment.\n\nThrough these games, presenting the dynamic reality I had witnessed came second to only writing dialogue which would entertain a wide array of people.\n\nFrom FPS streamer fratboy assholes who love Kylar to purple-haired gender neutral girls who love Ari... Class of \'09 has succeeded in being a crossroads of internet culture (regardless of whether those two parties are even aware the other side plays the game).\nThis was not by accident, this is just what happens when you aren\'t afraid to exit your comfort zone and explore other circles, other cultures, and most importantly other levels of hardship.\n\nReprestation in media is important, however mainstream media cannot represent those they are disconnected from. If you\'re suicidal, homeless, bulimic, addicted, a sex worker, or in an abusive relationship, Class of \'09 is not shock humor to you. It merely displays a reality the comfortable can\'t comprehend.\n\nI cannot necessarily write how real which stories were or were not, but I can guarantee the answers will surprise you. Lives had been lost and many futures were squandered along the journey which influenced the stories in these games. Those who experienced some events of Class of \'09 in their own lives would understand. Your funny stories and your sad stories are all you need to create media that resonates.\n\n\nNow while the game contained a plethora of anti-pedophilia messagery you just can\'t avoid psychos who latch onto media just because it\'s popular. I would just like to warn our fans that child predators who infiltrated the Class of \'09 fanbase have been using the following phrases to secretly identify each other:\n\n"the writing in Class of \'09 isnt very good"\n"I hate SBN3"\n"I hate Wrath Club"\n"Class of \'09 was good by mistake"\n"I love Class of \'09 but hate the creator"\n"No! The game just made that up!"\n\nMake sure to report anyone using this or similar secret pedo rhetoric to your local authorities.\n\nThank you.\n\n-SBN3 a.k.a. God\n\n'
    }
    default selected_text = ""
    default show_popup = not persistent.seen_tip

    dismiss action [Play("sound", "audio/Phone_close.mp3"), Hide("ending_tracker_screen"), Show("ending_tracker_hide_screen")]

    key "K_ESCAPE" action If(selected_text, true=SetScreenVariable("selected_text", ""), false=[Play("s_sound", "audio/Phone_close.mp3"), Hide("ending_tracker_screen"), Show("ending_tracker_hide_screen")])
    key "K_BACKSPACE" action If(selected_text, true=SetScreenVariable("selected_text", ""), false=[Play("s_sound", "audio/Phone_close.mp3"), Hide("ending_tracker_screen")])

    add "gui/ending_tracker/ending_tracker_pda.png" at ending_tracker_pda

    fixed:
        at ending_tracker_screen

        add "gui/ending_tracker/base_screen.png"

        text "{}/5".format(len(persistent.endings)) font "joystix monospace.ttf" size 50 color "#ffffff" xpos 848 ypos 134
        if len(persistent.endings) == 5:
            text "3/3" font "joystix monospace.ttf" size 48 color "#ffffff" xpos 1070 ypos 134
        elif len(persistent.endings) == 4:
            text "2/3" font "joystix monospace.ttf" size 48 color "#ffffff" xpos 1070 ypos 134
        elif len(persistent.endings) == 2:
            text "1/3" font "joystix monospace.ttf" size 48 color "#ffffff" xpos 1070 ypos 134
        else:
            textbutton _("0/3") text_font "joystix monospace.ttf" text_size 48 text_color "#ffffff":
                hovered SetScreenVariable("show_popup", True)
                action NullAction()
                padding (0, 0, 0, 0)
                xpos 1070
                ypos 134



        if not selected_text:
            viewport:
                id "messages"
                xysize (750, 615)
                xpos 606
                ypos 266
                draggable True
                mousewheel True

                if selected_text:
                    text ending_text[selected_text] font "texting2007.ttf" size 30 color "#000000"
                else:
                    vbox:

                        if persistent.seen_last_video_message:
                            button:
                                xysize (644, 50)
                                xpos 30

                                hover_background "gui/ending_tracker/highlight_bar.png"

                                text "SBN3               Thanks for playing! " font "texting2007.ttf" size 30 color "#000000" yalign 0.5 xpos 25 yoffset 5:
                                    hover_color "#ffffff"

                                action Play("sound", "audio/Phone_button.mp3"), SetScreenVariable("selected_text", "0000"), SetScreenVariable("adj.value", 0.0)

                        for index, ending in enumerate(persistent.endings[::-1]):
                            $ ending = ending.split("_")[1]
                            $ detail = endings_details[ending]
                            $ end_l = len(persistent.endings)

                            if end_l == 5 and index == 0:
                                button:
                                    xysize (644, 50)
                                    xpos 30

                                    hover_background "gui/ending_tracker/highlight_bar.png"

                                    text "UNKNOWN          VIDEO: IT ENDS WITH YOU" font "texting2007.ttf" size 30 color "#000000" yalign 0.5 xpos 25 yoffset 5:
                                        hover_color "#ffffff"

                                    action Start("scene_S0999")

                            if (end_l == 4 and index == 0) or (end_l == 5 and index == 1):
                                button:
                                    xysize (644, 50)
                                    xpos 30

                                    hover_background "gui/ending_tracker/highlight_bar.png"

                                    text "UNKNOWN          VIDEO: STOP PLAYING" font "texting2007.ttf" size 30 color "#000000" yalign 0.5 xpos 25 yoffset 5:
                                        hover_color "#ffffff"

                                    action Start("scene_S0998")

                            if (end_l == 2 and index == 0) or (end_l == 3 and index == 1) or( end_l == 4 and index == 2) or (end_l == 5 and index == 3):
                                button:
                                    xysize (644, 50)
                                    xpos 30

                                    hover_background "gui/ending_tracker/highlight_bar.png"

                                    text "UNKNOWN          VIDEO: WE'RE WATCHING" font "texting2007.ttf" size 30 color "#000000" yalign 0.5 xpos 25 yoffset 5:
                                        hover_color "#ffffff"

                                    action Start("scene_S0997")

                            button:
                                xysize (644, 50)
                                xpos 30

                                hover_background "gui/ending_tracker/highlight_bar.png"

                                text "{}{}".format(endings_name[ending], detail) font "texting2007.ttf" size 30 color "#000000" yalign 0.5 xpos 25 yoffset 5:
                                    hover_color "#ffffff"

                                action Play("sound", "audio/Phone_button.mp3"), SetScreenVariable("selected_text", ending), SetScreenVariable("adj.value", 0.0)

            vbar value YScrollValue("messages"):
                xpos 1285
                ypos 220
                ysize 670
                xsize 40
                base_bar Solid("#00000000")
                thumb "gui/ending_tracker/texting_scrollbar.png"

        else:
            viewport:
                id "message_detail"
                xysize (610, 635)
                xpos 656
                ypos 266
                draggable True
                mousewheel True

                text ending_text[selected_text] font "texting2007.ttf" size 30 color "#000000"

            vbar value YScrollValue("message_detail"):
                xpos 1285
                ypos 220
                ysize 670
                xsize 40
                base_bar Solid("#00000000")
                thumb "gui/ending_tracker/texting_scrollbar.png"

        imagebutton:
            idle "gui/ending_tracker/texting_back.png"
            hover "gui/ending_tracker/texting_back.png"

            action If(selected_text, true=[Play("sound", "audio/Phone_button.mp3"), SetScreenVariable("selected_text", "")], false=[Play("s_sound", "audio/Phone_close.mp3"), Hide("ending_tracker_screen"), Show("ending_tracker_hide_screen")])
            xpos 664
            ypos 907

        add "gui/ending_tracker/screen_overlay.png"
        add "gui/ending_tracker/faceplate.png"

        if show_popup:
            button:
                xysize (447, 380)
                background "gui/ending_tracker/confirm_bubble.png"

                action NullAction()
                xpos 1180
                ypos 105

                textbutton _("WHATEVER"):
                    text_font "LeagueGothic-Regular.otf"
                    text_size 37
                    text_idle_color "#ff7cc0"
                    text_hover_color "#ffffff"
                    action SetScreenVariable("show_popup", False), SetField(persistent, "seen_tip", True)
                    xpos 200
                    ypos 300

screen ending_tracker_hide_screen():
    zorder 150

    timer 0.50 action Hide("ending_tracker_hide_screen")
    frame:
        at ending_tracker_close

        background None
        xysize (1, 1)

screen movie_playback_screen(m, t):
    modal True
    zorder 155

    on "show":
        action PauseAudio("music", value=True), Function(print, "qwerty")
    on "hide":
        action PauseAudio("music", value=False), Function(print, "asdfgh")

    timer t action Hide("movie_playback_screen")
    dismiss action Hide("movie_playback_screen")

    add Movie(play=m):
        xysize (1920, 1080)

transform ending_tracker_screen:
    on show:
        alpha 0.0
        pause 0.48
        alpha 1.0

transform ending_tracker_pda():
    subpixel True

    on show:
        "gui/ending_tracker/flipanimation/ph01.png"
        zoom 0.4040
        xalign 0.95
        yalign 0.9
        "gui/ending_tracker/flipanimation/ph02.png"
        parallel:
            linear 0.44 zoom 2.8
        parallel:
            pause 0.08
            "gui/ending_tracker/flipanimation/ph03.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph04.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph05.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph06.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph07.png"
            pause 0.08
        parallel:
            linear 0.25 xalign 0.55
        parallel:
            linear 0.25 yalign 0.11

transform ending_tracker_close():
    subpixel True
    xalign 0.55
    yalign 0.11
    zoom 2.8

    on show:
        parallel:
            pause 0.25
            linear 0.25 xalign 0.94
        parallel:
            pause 0.25
            linear 0.25 yalign 0.925
        parallel:
            linear 0.50 zoom 0.35
        parallel:
            "gui/ending_tracker/flipanimation/ph07.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph06.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph05.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph04.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph03.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph02.png"
            pause 0.08
            "gui/ending_tracker/flipanimation/ph01.png"
            pause 0.08
            Null()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

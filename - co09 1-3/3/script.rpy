define beginMarker = "0.0"
define sceneAudio = ""
define endMarker = "0.0"
define waitTime = "0.0"
define drift = 0.0
define waitTag = ""
define line = ""
define tolerance = 0.5
define pad = .05
define playback_paused = False
define paused_position = 0.0
define current_line = ""
define current_character = None
define line_time_remaining = 0.0
define pause_start = 0.0
define pause_duration = 0.0
define config.main_menu_music = "audio/menu_piano.mp3"

default csbox = False
default persistent.seen_last_video_message = False

image smoke:
    "smokeloop/Comp 1_00001.png"
    pause 0.08
    "smokeloop/Comp 1_00003.png"
    pause 0.08
    "smokeloop/Comp 1_00005.png"
    pause 0.08
    "smokeloop/Comp 1_00007.png"
    pause 0.08
    "smokeloop/Comp 1_00009.png"
    pause 0.08
    "smokeloop/Comp 1_00011.png"
    pause 0.08
    "smokeloop/Comp 1_00013.png"
    pause 0.08
    "smokeloop/Comp 1_00015.png"
    pause 0.08
    "smokeloop/Comp 1_00017.png"
    pause 0.08
    "smokeloop/Comp 1_00019.png"
    pause 0.08
    "smokeloop/Comp 1_00021.png"
    pause 0.08
    "smokeloop/Comp 1_00023.png"
    pause 0.08
    "smokeloop/Comp 1_00025.png"
    pause 0.08
    "smokeloop/Comp 1_00027.png"
    pause 0.08
    "smokeloop/Comp 1_00029.png"
    pause 0.08
    "smokeloop/Comp 1_00031.png"
    pause 0.08
    "smokeloop/Comp 1_00033.png"
    pause 0.08
    "smokeloop/Comp 1_00035.png"
    pause 0.08
    "smokeloop/Comp 1_00037.png"
    pause 0.08
    "smokeloop/Comp 1_00039.png"
    pause 0.08
    "smokeloop/Comp 1_00041.png"
    pause 0.08
    "smokeloop/Comp 1_00043.png"
    pause 0.08
    "smokeloop/Comp 1_00045.png"
    pause 0.08
    "smokeloop/Comp 1_00047.png"
    pause 0.08
    "smokeloop/Comp 1_00049.png"
    pause 0.08
    "smokeloop/Comp 1_00051.png"
    pause 0.08
    "smokeloop/Comp 1_00053.png"
    pause 0.08
    "smokeloop/Comp 1_00055.png"
    pause 0.08
    "smokeloop/Comp 1_00057.png"
    pause 0.08
    "smokeloop/Comp 1_00059.png"
    pause 0.08
    "smokeloop/Comp 1_00061.png"
    pause 0.08
    "smokeloop/Comp 1_00063.png"
    pause 0.08
    "smokeloop/Comp 1_00065.png"
    pause 0.08
    "smokeloop/Comp 1_00067.png"
    pause 0.08
    "smokeloop/Comp 1_00069.png"
    pause 0.08
    "smokeloop/Comp 1_00071.png"
    pause 0.08
    "smokeloop/Comp 1_00073.png"
    pause 0.08
    "smokeloop/Comp 1_00075.png"
    pause 0.08
    "smokeloop/Comp 1_00077.png"
    pause 0.08
    "smokeloop/Comp 1_00079.png"
    pause 0.08
    "smokeloop/Comp 1_00081.png"
    pause 0.08
    "smokeloop/Comp 1_00083.png"
    pause 0.08
    "smokeloop/Comp 1_00085.png"
    pause 0.08
    "smokeloop/Comp 1_00087.png"
    pause 0.08
    "smokeloop/Comp 1_00089.png"
    pause 0.08
    "smokeloop/Comp 1_00091.png"
    pause 0.08
    "smokeloop/Comp 1_00093.png"
    pause 0.08
    "smokeloop/Comp 1_00095.png"
    pause 0.08
    "smokeloop/Comp 1_00097.png"
    pause 0.08
    "smokeloop/Comp 1_00099.png"
    pause 0.08
    "smokeloop/Comp 1_00101.png"
    pause 0.08
    "smokeloop/Comp 1_00103.png"
    pause 0.08
    "smokeloop/Comp 1_00105.png"
    pause 0.08
    "smokeloop/Comp 1_00107.png"
    pause 0.08
    "smokeloop/Comp 1_00109.png"
    pause 0.08
    "smokeloop/Comp 1_00111.png"
    pause 0.08
    "smokeloop/Comp 1_00113.png"
    pause 0.08
    "smokeloop/Comp 1_00115.png"
    pause 0.08
    "smokeloop/Comp 1_00117.png"
    pause 0.08
    "smokeloop/Comp 1_00119.png"
    pause 0.08
    "smokeloop/Comp 1_00121.png"
    pause 0.08
    "smokeloop/Comp 1_00123.png"
    pause 0.08
    "smokeloop/Comp 1_00125.png"
    pause 0.08
    "smokeloop/Comp 1_00127.png"
    pause 0.08
    "smokeloop/Comp 1_00129.png"
    pause 0.08
    "smokeloop/Comp 1_00131.png"
    pause 0.08
    "smokeloop/Comp 1_00133.png"
    pause 0.08
    "smokeloop/Comp 1_00135.png"
    pause 0.08
    "smokeloop/Comp 1_00137.png"
    pause 0.08
    "smokeloop/Comp 1_00139.png"
    pause 0.08
    "smokeloop/Comp 1_00141.png"
    pause 0.08
    "smokeloop/Comp 1_00143.png"
    pause 0.08
    "smokeloop/Comp 1_00145.png"
    pause 0.08
    "smokeloop/Comp 1_00147.png"
    pause 0.08
    "smokeloop/Comp 1_00149.png"
    pause 0.08
    "smokeloop/Comp 1_00151.png"
    pause 0.08
    "smokeloop/Comp 1_00153.png"
    pause 0.08
    "smokeloop/Comp 1_00155.png"
    pause 0.08
    "smokeloop/Comp 1_00157.png"
    pause 0.08
    "smokeloop/Comp 1_00159.png"
    pause 0.08
    "smokeloop/Comp 1_00161.png"
    pause 0.08
    "smokeloop/Comp 1_00163.png"
    pause 0.08
    "smokeloop/Comp 1_00165.png"
    pause 0.08
    "smokeloop/Comp 1_00167.png"
    pause 0.08
    "smokeloop/Comp 1_00169.png"
    pause 0.08
    "smokeloop/Comp 1_00171.png"
    pause 0.08
    "smokeloop/Comp 1_00173.png"
    pause 0.08
    "smokeloop/Comp 1_00175.png"
    pause 0.08
    "smokeloop/Comp 1_00177.png"
    pause 0.08
    "smokeloop/Comp 1_00179.png"
    pause 0.08
    "smokeloop/Comp 1_00181.png"
    pause 0.08
    "smokeloop/Comp 1_00183.png"
    pause 0.08
    "smokeloop/Comp 1_00185.png"
    pause 0.08
    "smokeloop/Comp 1_00187.png"
    pause 0.08
    "smokeloop/Comp 1_00189.png"
    pause 0.08
    "smokeloop/Comp 1_00191.png"
    pause 0.08
    "smokeloop/Comp 1_00193.png"
    pause 0.08
    "smokeloop/Comp 1_00195.png"
    pause 0.08
    "smokeloop/Comp 1_00197.png"
    pause 0.08
    "smokeloop/Comp 1_00199.png"
    pause 0.08
    "smokeloop/Comp 1_00201.png"
    pause 0.08
    "smokeloop/Comp 1_00203.png"
    pause 0.08
    "smokeloop/Comp 1_00205.png"
    pause 0.08
    "smokeloop/Comp 1_00207.png"
    pause 0.08
    "smokeloop/Comp 1_00209.png"
    pause 0.08
    "smokeloop/Comp 1_00211.png"
    pause 0.08
    "smokeloop/Comp 1_00213.png"
    pause 0.08
    "smokeloop/Comp 1_00215.png"
    pause 0.08
    "smokeloop/Comp 1_00217.png"
    pause 0.08
    "smokeloop/Comp 1_00219.png"
    pause 0.08
    "smokeloop/Comp 1_00221.png"
    pause 0.08
    "smokeloop/Comp 1_00223.png"
    pause 0.08
    "smokeloop/Comp 1_00225.png"
    pause 0.08
    "smokeloop/Comp 1_00227.png"
    pause 0.08
    "smokeloop/Comp 1_00229.png"
    pause 0.08
    "smokeloop/Comp 1_00231.png"
    pause 0.08
    "smokeloop/Comp 1_00233.png"
    pause 0.08
    "smokeloop/Comp 1_00235.png"
    pause 0.08
    "smokeloop/Comp 1_00237.png"
    pause 0.08
    "smokeloop/Comp 1_00239.png"
    pause 0.08
    repeat

image shadow:
    "shadowloop/shadow_0000.png"
    pause 0.1
    "shadowloop/shadow_0001.png"
    pause 0.1
    "shadowloop/shadow_0002.png"
    pause 0.1
    "shadowloop/shadow_0003.png"
    pause 0.1
    "shadowloop/shadow_0004.png"
    pause 0.1
    "shadowloop/shadow_0005.png"
    pause 0.1
    "shadowloop/shadow_0006.png"
    pause 0.1
    "shadowloop/shadow_0007.png"
    pause 0.1
    "shadowloop/shadow_0008.png"
    pause 0.1
    "shadowloop/shadow_0009.png"
    pause 0.1
    repeat


label splashscreen:
    $ renpy.movie_cutscene('wcsplash.webm')
    $ renpy.movie_cutscene('logosplash.webm')
    return

init python:
    import time
    if not persistent.start_label_jump:
        persistent.start_label_jump = "scene_S0001A"

    def auto_forward_image(st, at, images, interval=0.03, total_frames=60):
        current_frame = int((st / interval)) % total_frames
        return images[current_frame], interval

    def jump_start_label(labels):
        _value = persistent.start_label_jump
        
        if persistent.start_label_jump == labels[0]:
            persistent.start_label_jump = labels[1]
        
        elif persistent.start_label_jump == labels[1]:
            persistent.start_label_jump = labels[2]
        
        elif persistent.start_label_jump == labels[2]:
            persistent.start_label_jump = labels[3]
        
        elif persistent.start_label_jump == labels[3]:
            persistent.start_label_jump = labels[4]
        
        elif persistent.start_label_jump == labels[4]:
            persistent.start_label_jump = labels[0]
        
        return _value

    renpy.music.register_channel("ambient", "music", loop=True, tight=True)
    renpy.music.register_channel("vo", "music", loop=False, tight=True)
    renpy.music.register_channel("sfx", "music", loop=False, tight=True)
    renpy.music.register_channel("s_sound", "temp", loop=False, tight=True)

    def afterLoad():
        renpy.pause(1.0)


    config.after_load_callbacks = [afterLoad]
    preferences.show_empty_window = True

    if not persistent.endings:
        persistent.endings = []
        persistent.new_ending = False

    def isclose(a, b, tolerance):
        return abs(a-b) < tolerance

    def seekvoice(event, interact=True, **kwargs):
        global beginMarker, tolerance, drift
        if event == 'begin':
            pos = renpy.music.get_pos('vo')
            if pos is None:
                pos = float(beginMarker)
                drift = 0.0
                renpy.music.play("<from " + beginMarker + ">" + sceneAudio,'vo')
                return
            drift = pos - float(beginMarker)
            if not isclose(pos, float(beginMarker), tolerance):
                renpy.music.play("<from " + beginMarker + ">" + sceneAudio,'vo')

    def setWait(begin, end):
        global beginMarker, endMarker, waitTime, waitTag, sceneAudio, current_line, drift
        beginMarker = str(begin)
        endMarker = str(end)
        waitTime = str((end - begin) - drift if drift >= 0 else (end - begin))
        waitTag = '{p=' + waitTime + '}{nw}'


    def setVoiceTrack(name):
        global sceneAudio, beginMarker, endMarker, waitTime
        sceneAudio = name
        beginMarker = "0.0"
        endMarker = "0.0"
        waitTime = "0.0"
        drift = 0.0
        renpy.music.play(sceneAudio,'vo')
        renpy.music.set_pause(False, channel='vo')

    def killAudio():
        renpy.music.set_pause(True, channel='vo')
        renpy.music.set_pause(True, channel='ambient')

    def speak(c, line, resume=False):
        global pause_duration, waitTag, current_line, current_character, line_time_remaining
        current_line = line
        current_character = c
        if not resume:
            renpy.pause(0.0)
            renpy.checkpoint(renpy.say(c, line + waitTag))
        else:
            pause_duration = 0
            line_time_remaining = 0
            renpy.say(c.name, line)
        
        if line_time_remaining > 0.0:
            p = line_time_remaining
            
            line_time_remaining = 0
            current_line = current_line.split("{p")[0]
            if pause_duration >= p:
                speak(c, current_line + '{p=' + str(p) + '}{nw}', True)
            else:
                speak(c, current_line + '{p=' + str(pause_duration) + '}{nw}', True)



    def game_unpause():
        global pause_duration
        if pause_duration > 0:
            pause_duration += time.time() - pause_start
        else:
            pause_duration = time.time() - pause_start
        renpy.return_statement()

    def ending_reached(ending):
        import os
        import shutil
        ending_map = {
            '0039': 'shut up about this bitch4.txt',
            '0063': 'they just dont get it and never will.txt',
            '0074': 'attention5is6privilege7.txt',
            '0091': 'sdgsdg6sadhgdszfbadfb6adzfghzdfh6.txt',
            '0103': 'victims 2006 breed 2008 victims i want to kill myself look at me.txt',
            '0105': 'theanswerismaybejaajajajjajajaja.txt',
            '0121': 'priorirties in the year of our lord 2007.txt',
            '0126': 'she will never know who and its not fine.txt',
            '0127': 'i am the ball the ball the ball.txt',
            '0144': '3y3roll hardddddddddd.txt',
            '0145': 'po551b1t135.txt',
            '0153': 'dont do not look dont look at me i dont want it.txt',
            '0161': 'what about me, what ABOUT me 2010.txt',
            '0169': 'so close yet so 4375457far.txt',
            '0173': 'happy659087i5607905.txt',
        }
        desktop_path = os.path.expanduser("~/Desktop/")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(renpy.loader.transfn('endings/completed.txt'), 'r') as fp:
            endings = fp.read().splitlines()
            if ending not in endings:
                shutil.copy(renpy.loader.transfn('endings/' + ending_map[ending]), desktop_path)
        
        with open(renpy.loader.transfn('endings/completed.txt'), 'a') as fp:
            fp.writelines(["\n" + ending])

    def game_pause():
        global paused_position, endMarker, line_time_remaining, pause_start
        renpy.music.set_pause(True, channel='vo')
        renpy.music.set_pause(True, channel='ambient')
        pause_start = time.time()
        paused_position = renpy.music.get_pos('vo')
        line_time_remaining = float(endMarker) - paused_position if paused_position is not None else 0

init:

    $ config.enter_transition = None
    image black = Solid((0, 0, 0, 255))

transform transform_logo:
    alpha 0 xalign 1.2 yalign 0.2 size (700.0,395.0) subpixel True
    easein 1.0 alpha 1 xalign 0.88

screen pause_menu():
    tag menu

    on "show":
        action Function(game_pause)

    key "K_ESCAPE" action Function(game_unpause)
    key "mouseup_3" action Function(game_unpause)
    key "K_MENU" action Function(game_unpause)


    add "gui/nvl.png"
    style_prefix "main_menu"

    zorder 100

    hbox:
        frame:
            style "main_menu"

    add "gui/ClassOf09logo.png" at transform_logo

    vbox:

        xalign 0.5
        yalign 0.5


        textbutton _("Resume"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action Function(game_unpause)
        textbutton _("Options"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action ShowMenu('pause_prefs')
        textbutton _("Save"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action ShowMenu('pause_save')

        textbutton _("Main Menu"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action [Stop("vo"),Stop("ambient"),MainMenu()]

style pause_menu_button_text:
    size 200




screen disable_Controls():
    tag menu
    zorder 0

    key "mouseup_1" action NullAction()
    key "mouseup_2" action NullAction()
    key "mouseup_3" action NullAction()
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    style_prefix "skip"

    vbox:
        spacing -5

        xalign 0.98
        yalign .98

        textbutton "Skip" action [Jump (jump_start_label(["scene_S0001A", "scene_S0001B", "scene_S0001C", "scene_S0001D", "scene_S0001E"])), Hide("disable_Controls")]


screen disable_controls_for_ending():
    tag menu
    zorder 0
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()

    key "K_UP" action NullAction()
    key "K_DOWN" action NullAction()
    key "K_LEFT" action NullAction()
    key "K_RIGHT" action NullAction()
    key "K_SPACE" action NullAction()

    key "a" action NullAction()
    key "b" action NullAction()
    key "c" action NullAction()
    key "d" action NullAction()
    key "e" action NullAction()
    key "f" action NullAction()
    key "g" action NullAction()
    key "h" action NullAction()
    key "i" action NullAction()
    key "j" action NullAction()
    key "k" action NullAction()
    key "l" action NullAction()
    key "m" action NullAction()
    key "n" action NullAction()
    key "o" action NullAction()
    key "p" action NullAction()
    key "q" action NullAction()
    key "r" action NullAction()
    key "s" action NullAction()
    key "t" action NullAction()
    key "u" action NullAction()
    key "v" action NullAction()
    key "w" action NullAction()
    key "x" action NullAction()
    key "y" action NullAction()
    key "z" action NullAction()

    key "0" action NullAction()
    key "1" action NullAction()
    key "2" action NullAction()
    key "3" action NullAction()
    key "4" action NullAction()
    key "5" action NullAction()
    key "6" action NullAction()
    key "7" action NullAction()
    key "8" action NullAction()
    key "9" action NullAction()


define NICOLE = Character("Nicole", callback=seekvoice)
define KYLAR = Character("Kylar", callback=seekvoice)
define ARI = Character("Ari", callback=seekvoice)
define CRISPIN = Character("Crispin", callback=seekvoice)
define TRODY = Character("Trody", callback=seekvoice)
define JEFFERY = Character("Jeffery", callback=seekvoice)
define BURLEDAY = Character("Mr. Burleday", callback=seekvoice)
define JECKA = Character("Jecka", callback=seekvoice)
define BROTHER = Character("Gamer Brother", callback=seekvoice)
define COP = Character("Cop", callback=seekvoice)
define MALLCOP = Character("Mall Cop", callback=seekvoice)
define COACH = Character("Coach Colby", callback=seekvoice)
define KYLE = Character("Kyle", callback=seekvoice)
define EMILY = Character("Emily", callback=seekvoice)
define LYNN = Character("Principal Lynn", callback=seekvoice)
define HUNTER = Character("Hunter", callback=seekvoice)
define MEGAN = Character("Megan", callback=seekvoice)
define COUNSELOR = Character("Counselor", callback=seekvoice)
define KATZ = Character("Mr. Katz", callback=seekvoice)
define KAREN = Character("Karen", callback=seekvoice)
define KELLY = Character("Kelly", callback=seekvoice)
define CAMRY = Character("Camry Driver", callback=seekvoice)
define LORRE = Character("Mr. Lorre", callback=seekvoice)
define AMES = Character("Ms. Ames", callback=seekvoice)
define NICOLE_JECKA = Character("Nicole & Jecka", callback=seekvoice)
define DAD = Character("Dad", callback=seekvoice)
define FOOTFREAK = Character("Crusty Cormac", callback=seekvoice)
define JECKAEMILY = Character("Jecka & Emily", callback=seekvoice)
define PHONE = Character("Jecka's Mom", callback=seekvoice)
define JECKASMOM = Character("Phone", callback=seekvoice)
define METRO = Character("Metro Speaker", callback=seekvoice)
define SHADOW = Character("The Hatman", callback=seekvoice)
define none = Character("none", callback=seekvoice)


transform leftstage:
    xalign -0.11

transform leftmidstage:
    xalign 0.14

transform leftcenterstage:
    xalign 0.37

transform centerstage:
    xalign 0.5

transform rightcenterstage:
    xalign 0.63

transform rightmidstage:
    xalign 0.88

transform rightstage:
    xalign 1.12

transform off_right:
    xalign 1.4

transform off_farright:
    xalign 1.6

transform off_left:
    xalign -0.4

transform off_farleft:
    xalign -0.73

image opening cutscene = Movie(play="opening.webm")

label start:
    stop music fadeout 0.8
    $ quick_menu = False
    $ _game_menu_screen = "pause_menu"
    pause (2.3)
    show black
    show opening cutscene
    show screen disable_Controls
    $ renpy.pause(48, hard=True)

    $ renpy.jump(jump_start_label(["scene_S0001A", "scene_S0001B", "scene_S0001C", "scene_S0001D", "scene_S0001E"]))

label scene_S0001A:
    hide screen disable_Controls
    show black onlayer screens with Pause(1):
        alpha 1.0
    $ setVoiceTrack("audio/Scenes/0001A.mp3")
    $ quick_menu = True
    $ csbox = True
    scene cut0001a
    play ambient "audio/Ambience/Bedroom_Day_Ambience.mp3" fadein 1.6
    $ setWait(0.043,1.67)
    $ speak(JECKA, "...")

    show black onlayer screens:
        alpha 1.0
        linear 2 alpha 0.0

    $ setWait(1.67,4.965)
    $ speak(JECKA, "Am I gonna be waking up early for the rest of my life?")
    $ setWait(4.965,8.51)
    $ speak(JECKA, "How is someone who wants to do this well adjusted?")
    $ setWait(8.51,12.263)
    $ speak(JECKA, "If I was a suicide hotline operator I'd just tell 'em to go for it.")
    $ setWait(12.263,16.726)
    $ speak(JECKA, "I'd be like \"your therapist is a therapist, you think they got life figured out?\"")
    $ setWait(16.726,19.688)
    $ speak(JECKA, "Dumb shit, what was this morning again?")
    stop ambient fadeout 2
    menu:
        "HOME START":
            jump scene_S0002
        "SCHOOL START":

            jump scene_S0057

label scene_S0001B:
    hide screen disable_Controls
    show black onlayer screens with Pause(1):
        alpha 1.0
    $ setVoiceTrack("audio/Scenes/0001B.mp3")
    $ quick_menu = True
    $ csbox = True
    scene cut0001b
    play ambient "audio/Ambience/Bedroom_Day_Ambience.mp3" fadein 1.6
    $ setWait(0.079,4.208)
    $ speak(JECKA, "...")
    $ setWait(4.208,8.087)
    $ speak(JECKA, "Who the fuck invented alarm clocks??")
    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.0
    $ setWait(8.087,12.049)
    scene cut0001a
    $ speak(JECKA, "Probably some ugly white guy who gives nicknames to all the cashiers at Kohl's...")
    $ setWait(12.049,15.845)
    $ speak(JECKA, "\"Hey Smiles, working the register Thursdays, huh?\"")
    scene cut0001c
    $ setWait(15.845,17.889)
    $ speak(JECKA, "Oh wait what do I have today?")
    stop ambient fadeout 2    

    menu:
        "HOME START":
            jump scene_S0002
        "SCHOOL START":

            jump scene_S0057

label scene_S0001C:
    hide screen disable_Controls
    show black onlayer screens with Pause(1):
        alpha 1.0
    $ setVoiceTrack("audio/Scenes/0001C.mp3")
    $ quick_menu = True
    $ csbox = True
    scene cut0001a
    play ambient "audio/Ambience/Bedroom_Day_Ambience.mp3" fadein 1.6
    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.0
    $ setWait(0.415,3.543)
    $ speak(JECKA, "Am I already awake? This sucks.")
    $ setWait(3.543,8.84)
    $ speak(JECKA, "It's like percocet just makes you stronger and immune to more percocet.")
    scene cut0001c
    $ setWait(8.84,12.636)
    $ speak(JECKA, "I want adderall... and a cigarette...")
    scene cut0001a
    $ setWait(12.636,15.472)
    $ speak(JECKA, "I want a cigarette and adderall.")
    $ setWait(15.472,17.891)
    $ speak(JECKA, "What was I even supposed to do this week?")
    stop ambient fadeout 2

    menu:
        "HOME START":
            jump scene_S0002
        "SCHOOL START":

            jump scene_S0057

label scene_S0001D:
    hide screen disable_Controls
    show black onlayer screens with Pause(1):
        alpha 1.0
    $ setVoiceTrack("audio/Scenes/0001D.mp3")
    $ quick_menu = True
    $ csbox = True
    scene black
    play ambient "audio/Ambience/Bedroom_Day_Ambience.mp3" fadein 1.6
    $ setWait(1.089,8.221)
    $ speak(JECKASMOM, "...")
    scene cut0001b
    $ setWait(8.221,9.89)
    $ speak(DAD, "Shut up!! Shut the fuck up!!")

    $ setWait(9.89,11.475)
    $ speak(JECKASMOM, "Ugh! No! Go away!")
    show black onlayer screens:
        alpha 1.0
        linear 0.3 alpha 0.0
    $ setWait(11.475,12.601)
    $ speak(JECKA, "This fuckin' early?")
    $ setWait(12.601,14.811)
    $ speak(DAD, "Do you see this god damn credit card bill!?")
    scene cut0001a
    $ setWait(14.811,16.98)
    $ speak(JECKASMOM, "I told you I didn't go there it's somebody else--")
    $ setWait(16.98,18.482)
    $ speak(DAD, "Oh who!? Who is it!?")
    $ setWait(18.482,19.357)
    $ speak(JECKASMOM, "I don't know!")
    $ setWait(19.357,21.318)
    $ speak(DAD, "Are you seeing Raoul again?")
    $ setWait(21.318,21.985)
    $ speak(JECKASMOM, "No!")
    $ setWait(21.985,25.572)
    $ speak(DAD, "I knew it! You're a whore! A whore!!")
    $ setWait(25.572,26.573)
    $ speak(JECKASMOM, "Shut the fuck up!!")
    $ setWait(26.573,29.91)
    $ speak(DAD, "Give ya a high-speed backslap!!")
    scene cut0001c
    $ setWait(29.91,30.994)
    $ speak(JECKA, "Whoa.")
    $ setWait(30.994,33.33)
    $ speak(JECKASMOM, "Aghhhh! I hate you!!")
    scene cut0001a
    $ setWait(33.33,39.294)
    $ speak(JECKA, "Just gonna let this one blow over.")
    $ setWait(39.294,41.296)
    $ speak(JECKA, "What did I have to do today?")
    stop ambient fadeout 6

    menu:
        "HOME START":
            jump scene_S0002
        "SCHOOL START":

            jump scene_S0057

label scene_S0001E:
    hide screen disable_Controls
    show black onlayer screens with Pause(1):
        alpha 1.0
    $ setVoiceTrack("audio/Scenes/0001E.mp3")
    $ quick_menu = True
    $ csbox = True
    scene cut0001b
    play ambient "audio/Ambience/Bedroom_Day_Ambience.mp3" fadein 1.6
    $ setWait(0.668,9.051)
    $ speak(JECKA, "...")
    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.0
    $ setWait(9.051,12.513)
    $ speak(JECKA, "Bitch why the fuck are you calling me at 7AM?")
    $ setWait(12.513,13.556)
    $ speak(JECKA, "What do you want?")
    $ setWait(13.556,17.852)
    $ speak(NICOLE, "Hey I'm in the kitchen at McDonald's, where do they keep the patties again? I'm trying to steal some.")
    scene cut0001a
    $ setWait(17.852,19.603)
    $ speak(JECKA, "Like burger patties?")
    $ setWait(19.603,20.98)
    $ speak(NICOLE, "Yeah they're like nowhere.")
    scene cut0001b
    $ setWait(20.98,23.566)
    $ speak(JECKA, "It's 7AM they're serving breakfast!")
    $ setWait(23.566,25.025)
    $ speak(NICOLE, "They still do that?")
    scene cut0001a
    $ setWait(25.025,26.36)
    $ speak(JECKA, "Uh yeah?")
    $ setWait(26.36,29.363)
    $ speak(NICOLE, "Oh that explains why there's eggs everywhere, I thought it was French week.")
    scene cut0001b
    $ setWait(29.363,31.073)
    $ speak(JECKA, "Are you actually fucking stupid?")
    $ setWait(31.073,36.162)
    $ speak(NICOLE, "Dude I don't know I haven't been awake earlier than noon since like 9/11 happened.")
    scene cut0001a
    $ setWait(36.162,39.123)
    $ speak(JECKA, "Well... Okay are you going home now?")
    $ setWait(39.123,41.792)
    $ speak(NICOLE, "I guess that depends, what're you doing today?")
    stop ambient fadeout 2

    menu:
        "HOME START":
            jump scene_S0002
        "SCHOOL START":

            jump scene_S0057

label scene_S0002:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    show title_june2009 onlayer screens
    scene onlayer master
    show black
    show house jecka day with Pause(2.955):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.955 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0002.mp3")
    play ambient "audio/Ambience/House_Ambience_2.mp3"
    scene livingroom jecka
    show dad polo smile:
        leftmidstage
        xzoom -1

    show jecka pj:
        off_right
        linear 3 rightmidstage
    $ csbox = False
    show title_june2009 onlayer screens:
        alpha 1.0
        linear 2 alpha 0.0
    $ setWait(2.955,4.873)
    $ speak(DAD, "Morning, sweetheart.")
    $ setWait(4.873,6.625)
    $ speak(JECKA, "Yeah uh...")
    hide title_june2009 onlayer screens
    $ setWait(6.625,10.379)
    $ speak(JECKA, "Dad why were all the family photos with Mom shattered on the Bathroom floor?")
    show dad polo caring:
        leftmidstage
        xzoom -1
    $ setWait(10.379,12.798)
    $ speak(DAD, "Just- Just don't worry about it, I'll clean it up later.")
    show jecka pj angry:
        rightmidstage
    $ setWait(12.798,17.386)
    $ speak(JECKA, "Why don't you clean it up now, Dad? Before I step in it and turn into a Ripley's episode??")
    $ setWait(17.386,20.055)
    $ speak(DAD, "Okay, okay, I'll get the vacuum.")
    show jecka pj:
        rightmidstage
    $ setWait(20.055,21.557)
    $ speak(JECKA, "But yeah where's Mom?")
    $ setWait(21.557,24.435)
    $ speak(DAD, "Jessica, there's no easy way to say this-")
    show jecka pj surprised:
        rightmidstage
        linear 0.25 rightcenterstage
    $ setWait(24.435,25.519)
    $ speak(JECKA, "Did Mom get kidnapped??")
    show dad polo:
        leftmidstage
    $ setWait(25.519,27.73)
    $ speak(DAD, "What- Now don't be ridiculous.")
    show jecka pj:
        rightcenterstage
    $ setWait(27.73,31.692)
    $ speak(JECKA, "Oh I guess you're right. The news thinks women are worthless once they turn 30 anyway.")
    show dad polo upset:
        leftmidstage
        xzoom -1
    $ setWait(31.692,33.444)
    $ speak(DAD, "Well Jesus Christ they're not wrong.")
    show jecka pj angry:
        rightcenterstage
    $ setWait(33.444,34.278)
    $ speak(JECKA, "What??")
    show dad polo:
        leftmidstage
        xzoom -1
    $ setWait(34.278,38.115)
    $ speak(DAD, "Honey, your Mother and I are getting a divorce.")
    show jecka pj surprised:
        rightcenterstage
    $ setWait(38.115,41.577)
    $ speak(JECKA, "A... Are you positive?")
    $ setWait(41.577,42.202)
    $ speak(DAD, "For what?")
    show jecka pj:
        rightcenterstage
    $ setWait(42.202,45.706)
    $ speak(JECKA, "N-no I mean... Are you sure?")
    $ setWait(45.706,54.757)
    $ speak(DAD, "Look I don't mean to bring all this on you at once but I think the last fight we had was pretty much the straw that broke the camel's back.")
    $ setWait(54.757,59.887)
    $ speak(DAD, "She's left to go live with your grandmother until we figure out who keeps what.")
    show jecka pj sad:
        rightcenterstage
    $ setWait(59.887,61.805)
    $ speak(JECKA, "Holy shit...")
    show dad polo caring:
        leftmidstage
        xzoom -1
    $ setWait(61.805,65.017)
    $ speak(DAD, "I-If you need any family counseling we--")
    show jecka pj smile:
        rightcenterstage
    $ setWait(65.017,67.227)
    $ speak(JECKA, "This shit's gonna be awesome!")
    show dad polo:
        leftmidstage
        xzoom -1
    $ setWait(67.227,68.145)
    $ speak(DAD, "How?")
    $ setWait(68.145,73.192)
    $ speak(JECKA, "Two birthdays, two Christmases, too many excuses to get really cute emo tattoos.")
    show dad polo caring:
        leftmidstage
        xzoom -1
    $ setWait(73.192,76.82)
    $ speak(DAD, "Dear I'm not sure if you should look at this as a good thing.")
    show jecka pj:
        rightcenterstage
    $ setWait(76.82,79.865)
    $ speak(JECKA, "It's not like somebody died or whatever, she's just living somewhere else.")
    show dad polo:
        leftmidstage
        xzoom -1
    $ setWait(79.865,83.41)
    $ speak(DAD, "And would you want to live with her and your grandma?")
    show jecka pj angry:
        rightcenterstage
    $ setWait(83.41,88.248)
    $ speak(JECKA, "Dad, fuck no, grandma's like the biggest bitch on Earth. Besides, all my friends are here.")
    $ setWait(88.248,95.464)
    $ speak(DAD, "Well alright, but just so you know, now that she's gone there's gonna have to be a few changes around here.")
    $ setWait(95.464,96.882)
    $ speak(JECKA, "Changes like what?")
    $ setWait(96.882,105.849)
    $ speak(DAD, "Since her income no longer contributes to the household, paying for your college is turning out to be a little more challenging than I predicted.")
    show jecka pj:
        rightcenterstage
    $ setWait(105.849,107.267)
    $ speak(JECKA, "So what're you saying?")
    $ setWait(107.267,111.772)
    $ speak(DAD, "I'm saying you're gonna have to get a job if you wanna continue to live here.")
    show jecka pj surprised:
        rightcenterstage
    $ setWait(111.772,112.94)
    $ speak(JECKA, "Dad, what the fuck.")
    $ setWait(112.94,116.235)
    $ speak(DAD, "I know, I know, I said you wouldn't need to but--")
    show jecka pj angry:
        rightcenterstage
    $ setWait(116.235,118.695)
    $ speak(JECKA, "She's the one divorcing you, don't take it out on me!")
    $ setWait(118.695,120.1)
    $ speak(DAD, "I swear if you don't...")
    show dad polo yell:
        leftmidstage
        xzoom -1

    show jecka pj surprised:
        rightcenterstage
    $ setWait(120.1,123.992)
    $ speak(DAD, "...shut the fuck up I will throw your ass out on the street!!")
    show jecka pj sad:
        rightcenterstage

    show dad polo angry:
        leftmidstage
        xzoom -1
    $ setWait(123.992,125.077)
    $ speak(JECKA, "O-Okay, dad.")

    $ setWait(125.077,128.956)
    $ speak(DAD, "How bout I knock a tooth out every time you act like your bitch whore mother!?")
    show dad polo yell:
        leftmidstage
        xzoom -1
    $ setWait(128.956,131.667)
    $ speak(DAD, "Think I give a fuck we paid for braces!?")
    $ setWait(131.667,133.46)
    $ speak(JECKA, "Alright fine I'll get a job! Shit!")
    show dad polo angry:
        leftmidstage
        xzoom -1
        linear 0.3 leftcenterstage
    $ setWait(133.46,134.67)
    $ speak(DAD, "Still gonna be a bitch!?")
    show jecka pj surprised:
        rightcenterstage
        linear 0.25 rightmidstage
    $ setWait(134.67,136.421)
    $ speak(JECKA, "No no! I'll be good!")
    $ setWait(136.421,139.842)
    $ speak(DAD, "Good, cause if you're not I will smack your makeup off!")
    $ setWait(139.842,144.555)
    $ speak(DAD, "Now get your ass out there and find a job or your mattress is going in the backyard!")
    show jecka pj sad:
        rightmidstage
    $ setWait(144.555,146.473)
    $ speak(JECKA, "Okay just stop yelling!")
    show dad polo upset:
        leftcenterstage
        xzoom -1
    $ setWait(146.473,151.854)
    $ speak(DAD, "Good. Cause the last thing we want is you ending up like your freeloading whore of a mother.")
    show jecka pj:
        rightmidstage
    $ setWait(151.854,154.148)
    $ speak(JECKA, "I thought she had a job-- Yeah we don't want that.")
    show dad polo smile:
        leftcenterstage
        xzoom -1
    $ setWait(154.148,164.158)
    $ speak(DAD, "I'm sorry I yelled sweetheart but now that you're 18 and Mom's not around anymore, the parenting's gonna be a little different from now on.")
    $ setWait(164.158,166.91)
    $ speak(DAD, "Who's Daddy's girl?")
    show jecka pj sad:
        rightmidstage
    $ setWait(166.91,168.412)
    $ speak(JECKA, "..I am...")
    show dad polo smile:
        leftcenterstage
        xzoom -1
        pause 1.8
        xzoom 1
        linear 1.8 off_left
    $ setWait(168.412,172.916)
    $ speak(DAD, "Good.")
    $ setWait(172.916,178.797)
    $ speak(DAD, "Hello? ..Hey Craig, yeah I'd love to donate to that underprivileged youth program.")
    show jecka pj angry:
        xzoom -1
        rightmidstage
        linear 2.2 off_right

    $ setWait(178.797,181.717)
    $ speak(JECKA, "\"He donates to charity, how could he abuse his daughter?\"")
    stop ambient fadeout 1.8

    jump scene_S0003

label scene_S0003:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0003.mp3")
    scene mall int
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1

    show jecka sc1:
        rightcenterstage

    show nicole sc1:
        leftcenterstage

    $ setWait(0.119,1.245)
    $ speak(NICOLE, "And he's not bluffing?")
    show jecka sc1 angry:
        rightcenterstage

    $ setWait(1.245,6.667)
    $ speak(JECKA, "Do you think I wanna find out? I'm just gonna get my horrible job to appease him until I go to college in September.")
    $ setWait(6.667,10.754)
    $ speak(NICOLE, "But Ulta's not hiring, Journey's isn't hiring, not even Popeyes is hiring.")
    $ setWait(10.754,14.3)
    $ speak(JECKA, "How does a restaurant where everyone looks miserable not have a huge turnover rate?")
    $ setWait(14.3,15.301)
    $ speak(NICOLE, "Cause the recession.")

    show jecka sc1:
        rightcenterstage

    $ setWait(15.301,16.969)
    $ speak(JECKA, "What even is the recession?")
    $ setWait(16.969,20.639)
    $ speak(NICOLE, "I don't know but it's a thing you can blame shit on, the recession's pretty cool actually.")
    show jecka sc1 smile:
        rightcenterstage
    $ setWait(20.639,22.182)
    $ speak(JECKA, "Yeah I'm broke cause the recession.")
    show nicole sc1 smile:
        leftcenterstage

    $ setWait(22.182,25.019)
    $ speak(NICOLE, "Yeah can't have dinner with your vegan parents, recession.")
    show jecka sc1:
        rightcenterstage

    $ setWait(25.019,26.604)
    $ speak(JECKA, "I wish that worked on my Dad.")
    $ setWait(26.604,29.607)
    $ speak(NICOLE, "And your Dad wishes you worked, cruel irony.")
    show jeffery work smile:
        off_right
        linear 1.3 rightmidstage

    show jecka sc1:
        rightcenterstage
        pause 0.7
        xzoom -1

    $ setWait(29.607,32.359)
    $ speak(JEFFERY, "Oh hey guys, fancy seeing you here.")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(32.359,33.986)
    $ speak(NICOLE, "What the fuck do you want?")

    show jecka sc1 angry:
        rightcenterstage
        xzoom -1

    $ setWait(33.986,35.446)
    $ speak(JECKA, "Yeah we're busy, Jeffery.")
    show jeffery work:
        rightmidstage

    $ setWait(35.446,37.823)
    $ speak(JEFFERY, "Busy applying for jobs I take it?")
    $ setWait(37.823,38.824)
    $ speak(NICOLE, "Are you stalking her?")
    show jeffery work angry:
        rightmidstage

    $ setWait(38.824,44.872)
    $ speak(JEFFERY, "What the- No! I saw you were running around with a bunch of application papers on my way to work is all.")
    show jecka sc1:
        rightcenterstage
        xzoom -1
    $ setWait(44.872,45.748)
    $ speak(JECKA, "\"Work is all\"")
    show nicole sc1:
        leftcenterstage
    $ setWait(45.748,47.666)
    $ speak(NICOLE, "What do you mean \"work\", you have a job?")
    show jeffery work smile:
        rightmidstage

    $ setWait(47.666,55.215)
    $ speak(JEFFERY, "That's right! I got a job at the bookstore since I spent so much time reading the manga there.")
    $ setWait(55.215,59.553)
    $ speak(JECKA, "...Every time you talk I really wonder how you could possibly have legal sex.")
    show jeffery work:
        rightmidstage
    $ setWait(59.553,69.104)
    $ speak(JEFFERY, "Eh so what, after graduation I realized that sex is kinda overrated. I'm into plenty of other stuff beyond girls and their high standards.")
    $ setWait(69.104,70.272)
    $ speak(NICOLE, "Is bathing a standard?")
    show jecka sc1 flirt:
        rightcenterstage
        xzoom -1
    $ setWait(70.272,76.07)
    $ speak(JECKA, "Y'know Jeffery, some girls would lower their standards if you could get them hired at the bookstore you're working at.")
    show jeffery work:
        rightmidstage

    $ setWait(76.07,79.323)
    $ speak(JEFFERY, "Sorry but no can do, recession and all.")

    show jecka sc1:
        rightcenterstage
        xzoom -1

    $ setWait(79.323,80.366)
    $ speak(NICOLE, "Bitch don't lie to us.")
    show jeffery work angry:
        rightmidstage

    $ setWait(80.366,82.91)
    $ speak(JEFFERY, "You think I can just give you handouts cause you're a girl?")
    show jecka sc1 angry:
        rightcenterstage
        xzoom -1
    $ setWait(82.91,86.038)
    $ speak(JECKA, "Obvi! The workforce is biased against women, help us out.")
    show jecka sc1:
        rightcenterstage
        xzoom -1
    $ setWait(86.038,88.457)
    $ speak(NICOLE, "Help her out, I don't want no bitchass job.")
    $ setWait(88.457,95.589)
    $ speak(JEFFERY, "You girls always pull that feminism card. Sorry but your damsel in distress act ain't workin' here, toots!")

    show jeffery work angry:
        rightmidstage
        xzoom -1
        pause 1.35
        linear 1 off_right

    $ setWait(95.589,99.468)
    $ speak(JEFFERY, "Oh I'm gonna be late! Women...")

    hide jeffery work

    $ setWait(99.468,103.472)
    $ speak(NICOLE, "I think all the not fucking women is turning into not liking women.")
    show jecka sc1:
        xzoom 1
        rightcenterstage

    $ setWait(103.472,105.432)
    $ speak(JECKA, "Do you think he should turn gay?")
    $ setWait(105.432,106.934)
    $ speak(NICOLE, "I don't think it works like that.")
    $ setWait(106.934,110.312)
    $ speak(JECKA, "Okay well Hot Topic's next on the list, could I turn gay working there?")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(110.312,112.856)
    $ speak(NICOLE, "You can't just magically turn gay, this isn't Degrassi.")
    show jecka sc1 angry:
        rightcenterstage
        xzoom 1

    $ setWait(112.856,114.525)
    $ speak(JECKA, "Why are you so against turning gay?")
    $ setWait(114.525,120.239)
    $ speak(NICOLE, "Cause if you think you turned gay there's some weird Christian guy who thinks he can electrocute you into turning back.")
    show jecka sc1 sad:
        rightcenterstage
    $ setWait(120.239,121.407)
    $ speak(JECKA, "People think that?")
    show nicole sc1:
        leftcenterstage
    $ setWait(121.407,125.744)
    $ speak(NICOLE, "Yeah but only a small number with lots of money and political power so don't worry about it.")
    show jecka sc1:
        rightcenterstage

    $ setWait(125.744,126.662)
    $ speak(JECKA, "Cool.")
    show jecka sc1 smile:
        rightcenterstage
        linear 2.5 off_left

    show nicole sc1:
        leftcenterstage
        pause 1.1
        xzoom -1
        linear 2.2 off_left
    $ setWait(126.662,129.373)
    $ speak(JECKA, "Yeah let's see if I can find a goth work girlfriend.")
    stop ambient fadeout 1.5

    jump scene_S0004

label scene_S0004:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0004.mp3")
    scene hot topic

    play ambient "audio/Ambience/HotTopic_Ambience.mp3" fadein 1

    show jecka sc1:
        off_right
        linear 1 rightcenterstage

    show nicole sc1:
        off_right
        xzoom -1
        pause 0.5
        linear 0.7 rightmidstage

    $ setWait(0.123,2.5)
    $ speak(NICOLE, "You ever feel like this place isn't hardcore enough?")

    show jecka sc1:
        rightcenterstage
        xzoom -1

    $ setWait(2.5,4.043)
    $ speak(JECKA, "What like all the Disney stuff?")
    $ setWait(4.043,5.962)
    $ speak(NICOLE, "No it's just missing something.")
    show nicole sc1 smile:
        rightmidstage
        xzoom -1

    $ setWait(5.962,11.426)
    $ speak(NICOLE, "Like if I ran this place the TVs would have videos of guys getting decapitated with a Hello Kitty watermark in the corner.")
    show jecka sc1 smile:
        rightcenterstage
        xzoom -1
    $ setWait(11.426,14.554)
    $ speak(JECKA, "That'd be cool, you should apply for manager here.")
    show nicole sc1:
        rightmidstage
        xzoom -1

    $ setWait(14.554,17.265)
    $ speak(NICOLE, "Do you realize the type of people you gotta deal with working here?")

    show kylar sc1 smile:
        xzoom -1
        off_left
        linear 0.75 leftmidstage

    show jecka sc1:
        rightcenterstage
        pause 0.5
        xzoom 1

    $ setWait(17.265,18.641)
    $ speak(KYLAR, "What's up, bitches?")

    show jecka sc1 angry:
        rightcenterstage
        xzoom 1


    $ setWait(18.641,19.934)
    $ speak(JECKA, "What the fuck do you want?")
    $ setWait(19.934,22.979)
    $ speak(NICOLE, "Yeah and we don't go to school with you anymore so you can't just come up to us.")
    show kylar sc1 angry:
        leftmidstage
        xzoom -1
    $ setWait(22.979,26.774)
    $ speak(KYLAR, "Well no if anything I can do what I want since you don't have the principal to squeal to.")
    $ setWait(26.774,30.028)
    $ speak(JECKA, "This isn't school it's real life, we'll just tell the police!")
    $ setWait(30.028,30.862)
    $ speak(KYLAR, "No you won't.")
    $ setWait(30.862,31.863)
    $ speak(NICOLE, "How do you know?")
    $ setWait(31.863,35.074)
    $ speak(KYLAR, "Don't like 50 percent of women not even report crimes or whatever?")
    $ setWait(35.074,35.992)
    $ speak(JECKA, "Yeah so?")

    show kylar sc1 smile:
        leftmidstage
        xzoom -1
        pause 1.2
        linear 1.2 off_right

    show jecka sc1 angry:
        rightcenterstage
        pause 1.75
        xzoom -1


    show nicole sc1:
        rightmidstage
        pause 2
        xzoom 1

    $ setWait(35.992,39.454)
    $ speak(KYLAR, "So if I punch you in the neck, flip a coin, bitch.")
    $ setWait(39.454,41.706)
    $ speak(NICOLE, "And he's off to his dad's dealership.")
    show emily sc1 upset:
        off_left
        xzoom -1
        linear 2 leftcenterstage

    show jecka sc1:
        rightcenterstage
        xzoom -1
        pause 0.38
        xzoom 1

    show nicole sc1:
        rightmidstage
        xzoom 1
        pause 0.5
        xzoom -1

    $ setWait(41.706,43.333)
    $ speak(EMILY, "What're you posers doing here?")
    show nicole sc1 angry:
        rightmidstage
        xzoom -1
    $ setWait(43.333,46.252)
    $ speak(NICOLE, "You go to Hot Topic alone and you're calling us posers?")
    show jecka sc1 angry:
        rightcenterstage
        xzoom 1
    $ setWait(46.252,49.881)
    $ speak(JECKA, "Yeah we're not here cause we like it I'm just trying to get a job. Do you work here?")
    $ setWait(49.881,50.798)
    show emily sc1:
        leftcenterstage
    $ speak(EMILY, "No.")

    show jecka sc1:
        rightcenterstage

    show nicole sc1:
        rightmidstage
        xzoom -1

    $ setWait(50.798,51.633)
    $ speak(JECKA, "Are you sure?")
    $ setWait(51.633,56.22)
    $ speak(EMILY, "I work at the Chrome Diner not this weirdo hangout for girls who clap when they see pandas.")
    $ setWait(56.22,61.059)
    $ speak(JECKA, "But if we're the only ones in here who does work here? How'd you buy that All Time Low cereal?")
    $ setWait(61.059,65.98)
    $ speak(EMILY, "These All Time O's? I'm just stealing 'em. But why do you need a job? I thought your parents had money.")
    $ setWait(65.98,69.692)
    $ speak(JECKA, "My parents are getting divorced and some other shit, but yeah I really gotta work.")
    $ setWait(69.692,71.361)
    $ speak(EMILY, "Strip club in Crystal City's hiring.")
    show jecka sc1 angry:
        rightcenterstage

    $ setWait(71.361,72.278)
    $ speak(JECKA, "Ew fuck that.")
    $ setWait(72.278,73.071)
    $ speak(NICOLE, "What's it pay?")
    $ setWait(73.071,73.655)
    $ speak(EMILY, "Tips.")
    show nicole sc1 angry:
        rightmidstage
        xzoom -1
    $ setWait(73.655,74.614)
    $ speak(NICOLE, "Yeah ew fuck that.")
    $ setWait(74.614,79.369)
    $ speak(JECKA, "I didn't bust my ass in high school to sell my body to guys who look like Super Mario without the costume.")
    show emily sc1 smile:
        leftcenterstage
        xzoom -1
        pause 1.3
        linear 1.7 off_right

    show nicole sc1:
        rightmidstage

    $ setWait(79.369,83.289)
    $ speak(EMILY, "Yeah we'll see... Lemme know if you wanna wait tables.")
    show jecka sc1 sad:
        rightcenterstage
        xzoom 1
        linear 0.3 centerstage
        xzoom -1
    $ setWait(83.289,85.124)
    $ speak(JECKA, "I can do better than waiter, right?")
    show nicole sc1 angry:
        rightmidstage
        xzoom -1

    $ setWait(85.124,86.793)
    $ speak(NICOLE, "Bitch you can't even wait for popcorn.")
    show jecka sc1 angry:
        centerstage
        xzoom -1
    $ setWait(86.793,88.836)
    $ speak(JECKA, "I told you I like it medium-well!")
    stop ambient fadeout 1.5
    jump scene_S0005

label scene_S0005:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0005.mp3")
    scene fye
    play ambient "audio/Ambience/FYE_Ambience.mp3" fadein 1

    show jecka sc1:
        leftcenterstage
        xzoom -1

    show kelly fye:
        rightcenterstage

    $ setWait(0.077,4.039)
    $ speak(KELLY, "But yeah Jecka, I'm super stoked that you wanna work at FYE with me.")
    show coach 1:
        off_right
        linear 2 rightstage
    $ setWait(4.039,5.207)
    $ speak(JECKA, "You think I wanna work?")
    show kelly fye:
        rightcenterstage
        xzoom -1
        pause 0.5
        xzoom 1
    $ setWait(5.207,6.249)
    $ speak(KELLY, "Oh customer, hold on-")
    show coach 1:
        rightstage

    show kelly fye:
        rightcenterstage
        xzoom -1
        linear 0.3 rightmidstage

    $ setWait(6.249,10.295)
    $ speak(KELLY, "Welcome to FYE, I'm Kelly! How can I help you today.")

    show coach 1 smile:
        rightstage

    $ setWait(10.295,16.134)
    $ speak(COACH, "Uh yeah honey you don't have some of that \"mild style\" do ya?")
    show kelly fye sad:
        rightmidstage
        xzoom -1

    $ setWait(16.134,19.054)
    $ speak(KELLY, "I'm sorry mild.. What? Is that a band?")
    show coach 1:
        rightstage

    $ setWait(19.054,25.143)
    $ speak(COACH, "No it's not a band I-it's that mild mild mild y'know what I mean?")
    $ setWait(25.143,29.272)
    $ speak(KELLY, "Sir, this isn't a Popeyes, but maybe they could help you out.")
    show jecka sc1 angry:
        xzoom -1
        leftcenterstage

    $ setWait(29.272,31.733)
    $ speak(JECKA, "Yeah with everything but a god damn motherfucking job.")
    show jecka sc1:
        xzoom -1
        leftcenterstage

    show coach 1 angry:
        rightstage
        xzoom -1
        linear 1.6 off_right

    $ setWait(31.733,35.362)
    $ speak(COACH, "Got the dumbest bitches on Earth working here nowadays...")
    $ setWait(35.362,36.53)
    $ speak(JECKA, "What was that all about?")
    show kelly fye:
        rightmidstage
        xzoom 1
        linear 0.7 rightcenterstage

    $ setWait(36.53,39.741)
    $ speak(KELLY, "Sometimes old people use retail to be recreationally angry.")
    $ setWait(39.741,41.702)
    $ speak(JECKA, "Well damn now I really don't wanna work here.")
    $ setWait(41.702,44.955)
    $ speak(KELLY, "No no it's cool, that was like once in a blue moon.")
    $ setWait(44.955,46.873)
    $ speak(JECKA, "What're the rest of the customers like?")
    show crispin sc1 smile:
        off_right
        linear 1.2 rightmidstage

    show kelly fye:
        rightcenterstage
        pause 0.4
        xzoom -1
    $ setWait(46.873,52.462)
    $ speak(CRISPIN, "Oh hey guys what's going on? Did you hear the new Devin Townsend album? He's like the drummer from The Who.")
    hide jecka sc1
    show jecka sc1 angry onlayer screens:
        leftcenterstage
        xzoom -1
        linear 1.3 off_right

    $ setWait(52.462,54.256)
    $ speak(JECKA, "Fuck no not workin' here!")
    stop ambient fadeout 1.5

    jump scene_S0006

label scene_S0006:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka day with Pause(2.508):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.508 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0006.mp3")
    scene livingroom jecka
    play ambient "audio/Ambience/House_Ambience_2.mp3"

    show dad buttonup:
        centerstage
        linear 2.3 xalign -0.2

    $ setWait(2.508,5.01)
    $ speak(DAD, "...")
    show dad buttonup smile:
        xalign -0.2
        linear 2 centerstage

    show nicole sc2:
        off_left
        pause 1.5
        linear 2 leftmidstage
    $ setWait(5.01,8.305)
    $ speak(DAD, "Oh hello uh, Nicole right?")
    $ setWait(8.305,10.266)
    $ speak(NICOLE, "Yeah, where's Jecka?")
    show dad buttonup:
        centerstage
    $ setWait(10.266,17.273)
    $ speak(DAD, "Jessica right, she's just up in her room applying for jobs over the phone but she'll only be a few more minutes.")
    show nicole sc2:
        leftmidstage
    $ setWait(17.273,19.608)
    $ speak(NICOLE, "Cool...")
    $ setWait(19.608,26.573)
    $ speak(DAD, "But uh, we can talk while she's busy. How ya doin'? How ya doin' today?")
    $ setWait(26.573,28.158)
    $ speak(NICOLE, "Yeah.")
    show dad buttonup smile:
        centerstage
    $ setWait(28.158,30.452)
    $ speak(DAD, "You guys got anything planned?")
    $ setWait(30.452,34.665)
    $ speak(NICOLE, "Um, we're gonna go to Claire's and trick 12 year olds into getting their eyelids pierced.")
    show dad buttonup:
        centerstage
    $ setWait(34.665,39.92)
    $ speak(DAD, "Oh Claire's yeah I've been there a few times.")
    $ setWait(39.92,41.088)
    $ speak(NICOLE, "...For what?")
    show dad buttonup smile:
        centerstage

    $ setWait(41.088,47.428)
    $ speak(DAD, "Oh just uh browsing. By the looks of things you're using their accessories really well.")
    $ setWait(47.428,50.514)
    $ speak(NICOLE, "Yeah I guess I would if I actually shopped there.")
    $ setWait(50.514,54.56)
    $ speak(NICOLE, "Too bad I'm not some sugar-free vanilla bitch who thinks Katherine Heigl is funny.")
    show dad buttonup:
        centerstage

    $ setWait(54.56,59.732)
    $ speak(DAD, "Oh right yeah, no I uh... So where do you shop?")
    $ setWait(59.732,62.067)
    $ speak(NICOLE, "It's pretty indie, you probably haven't heard of it.")
    show dad buttonup smile:
        centerstage
    $ setWait(62.067,64.987)
    $ speak(DAD, "Try me, I used to be in that scene.")
    $ setWait(64.987,66.155)
    $ speak(NICOLE, "What scene?")
    $ setWait(66.155,68.991)
    $ speak(DAD, "Uh, y'know the scene.")
    $ setWait(68.991,69.908)
    $ speak(NICOLE, "Sure.")
    $ setWait(69.908,75.956)
    $ speak(DAD, "No but, yeah Jessica never told me much about you. Especially not how beautiful you are.")
    $ setWait(75.956,79.001)
    $ speak(NICOLE, "Yeah I'm kinda perfect like that, she's probably jealous.")
    $ setWait(79.001,83.047)
    $ speak(DAD, "Y'know before her mother my last girlfriend was a brunette too actually.")
    $ setWait(83.047,85.883)
    $ speak(NICOLE, "Really? Cool yeah that's normal to tell me.")
    $ setWait(85.883,90.888)
    $ speak(DAD, "By the way I just got these Blue Oyster Cult tickets if you're ever interested.")
    $ setWait(90.888,92.306)
    $ speak(NICOLE, "Sorry I'm not religious.")
    show dad buttonup caring:
        centerstage

    $ setWait(92.306,94.725)
    $ speak(DAD, "No no, Blue Oyster Cult, they're a band.")
    $ setWait(94.725,95.976)
    $ speak(NICOLE, "Aren't most cults banned?")
    $ setWait(95.976,97.603)
    $ speak(DAD, "No a rock band.")
    $ setWait(97.603,100.105)
    $ speak(NICOLE, "Ohhhh... Never heard of 'em.")
    show dad buttonup smile:
        centerstage
    $ setWait(100.105,101.774)
    $ speak(DAD, "So who do you like?")
    show nicole sc2:
        leftmidstage
        pause 0.5
        linear 1.2 rightmidstage
    $ setWait(101.774,103.233)
    $ speak(NICOLE, "Nobody- I'm gonna go up now.")
    show dad buttonup caring:
        centerstage
        xzoom -1
    $ setWait(103.233,104.818)
    $ speak(DAD, "Wait but I don't think she's done yet.")
    show nicole sc2 angry:
        rightmidstage
        xzoom -1
        pause 4.1
        xzoom 1
        linear 1.65 off_right

    $ setWait(104.818,110.783)
    $ speak(NICOLE, "Well it felt like an eternity talking to you so if this bitch doesn't have a job by now I'm pretty sure you failed as a parent.")
    stop ambient fadeout 1.5
    jump scene_S0007

label scene_S0007:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0007.mp3")
    scene bedroom jecka day
    play ambient "audio/Ambience/Bedroom_Day_Ambience.mp3" fadein 1
    show jecka pj smile:
        xzoom -1
        rightstage

    $ setWait(0.083,4.379)
    $ speak(JECKA, "Okay thanks for the job, and yeah bring your adderall Monday.")
    show nicole sc2 surprised:
        off_left
        linear 1 leftcenterstage
    $ setWait(4.379,5.964)
    $ speak(NICOLE, "What kinda job did you get?")
    show jecka pj smile:
        rightstage
        xzoom 1
        linear 0.6 rightmidstage
    $ setWait(5.964,8.758)
    $ speak(JECKA, "Oh Emily just got me a job waiting tables with her.")
    show nicole sc2:
        leftcenterstage

    $ setWait(8.758,11.428)
    $ speak(NICOLE, "How does buying a girl's adderall turn into employment?")
    $ setWait(11.428,14.681)
    $ speak(JECKA, "Buying drugs can make you like the most connected person in town.")
    $ setWait(14.681,16.683)
    $ speak(NICOLE, "I guess I would know that if I didn't always steal them.")
    show jecka pj:
        rightmidstage
        xzoom 1
    $ setWait(16.683,20.812)
    $ speak(JECKA, "Yeah it's a great way to meet friends you'll immediately cut off once you get your life together.")
    $ setWait(20.812,26.735)
    $ speak(NICOLE, "Wow working in a diner, that's like the start of a Hillary Duff movie where she finds out her Dad has a blood diamond mine.")
    $ setWait(26.735,27.777)
    $ speak(JECKA, "Did you just get here?")
    $ setWait(27.777,30.989)
    $ speak(NICOLE, "No your Dad made me wait downstairs, he kept trying to talk to me.")
    show jecka pj sad:
        rightmidstage
    $ setWait(30.989,33.7)
    $ speak(JECKA, "Oh.. well how'd that go?")
    show nicole sc2:
        xzoom -1
    $ setWait(33.7,36.62)
    $ speak(NICOLE, "How would I word this...")
    show nicole sc2:
        xzoom 1
    $ setWait(36.62,38.497)
    $ speak(NICOLE, "Your dad really wants to fuck me.")
    show jecka pj surprised:
        rightmidstage
    $ setWait(38.497,39.539)
    $ speak(JECKA, "Wha- No way.")
    $ setWait(39.539,40.248)
    $ speak(NICOLE, "Yeah way.")
    show jecka pj angry:
        rightmidstage
    $ setWait(40.248,41.666)
    $ speak(JECKA, "My Dad would never do that.")
    $ setWait(41.666,43.877)
    $ speak(NICOLE, "Never? Or never want to?")
    show jecka pj angry:
        rightmidstage
        linear 0.4 rightcenterstage
    $ setWait(43.877,45.003)
    $ speak(JECKA, "But how do you know?")
    $ setWait(45.003,46.296)
    $ speak(NICOLE, "Why don't you just believe me?")
    show jecka pj sad:
        rightcenterstage
    $ setWait(46.296,49.132)
    $ speak(JECKA, "Cause I don't believe my Dad would just go up to you like \"Let's fuck\"!")
    show nicole sc2 angry:
        leftcenterstage
    $ setWait(49.132,52.844)
    $ speak(NICOLE, "No they never do it like that, I can just tell. He was way too interested.")
    $ setWait(52.844,53.845)
    $ speak(JECKA, "Interested how?")
    show nicole sc2:
        leftcenterstage
    $ setWait(53.845,55.096)
    $ speak(NICOLE, "He told me I'm beautiful.")
    $ setWait(55.096,56.348)
    $ speak(JECKA, "What if he's just being nice?")
    $ setWait(56.348,58.433)
    $ speak(NICOLE, "He asked me where I shop for accessories.")
    $ setWait(58.433,60.185)
    $ speak(JECKA, "He's just looking around for my birthday.")
    show nicole sc2 angry:
        leftcenterstage
    $ setWait(60.185,61.811)
    $ speak(NICOLE, "Bitch that's 10 months from now.")
    show jecka pj:
        rightcenterstage
        pause 0.7
        xzoom -1
        linear 3 rightstage

    show nicole sc2:
        leftcenterstage
    $ setWait(61.811,66.274)
    $ speak(JECKA, "Alright fine but if that's all you have I don't think that's enough to go off of.")
    $ setWait(66.274,69.653)
    $ speak(NICOLE, "His last girlfriend was a brunette.")
    show jecka pj surprised:
        rightstage
        xzoom 1
        linear 0.6 rightcenterstage
    $ setWait(69.653,70.987)
    $ speak(JECKA, "His what?")
    show nicole sc2 angry:
        leftcenterstage
    $ setWait(70.987,75.492)
    $ speak(NICOLE, "He told me his last girlfriend was a brunette.")
    show jecka pj sad:
        rightcenterstage

    $ setWait(75.492,78.453)
    $ speak(JECKA, "Uh... Nicole...")
    show nicole sc2:
        leftcenterstage

    $ setWait(78.453,79.371)
    $ speak(NICOLE, "Yeah?")
    $ setWait(79.371,81.498)
    $ speak(JECKA, "My Dad wants to fuck you.")
    $ setWait(81.498,82.123)
    $ speak(NICOLE, "I know.")
    show jecka pj sad:
        rightcenterstage
        xzoom -1
        linear 0.25 rightmidstage
        pause 0.6
        xzoom 1
        linear 0.2 rightcenterstage

    $ setWait(82.123,83.875)
    $ speak(JECKA, "I'm gonna kill myself! Help me kill myself!")
    $ setWait(83.875,86.211)
    $ speak(NICOLE, "Well that wouldn't be technically killing yourself, now would it?")
    show jecka pj sad:
        rightcenterstage
        xzoom 1
    $ setWait(86.211,88.421)
    $ speak(JECKA, "I can't go through with it alone, I'm too scared!")
    show nicole sc2 smile:
        leftcenterstage

    $ setWait(88.421,90.515)
    $ speak(NICOLE, "Work that job for a month, you'll get there.")
    stop ambient fadeout 1.5
    jump scene_S0008

label scene_S0008:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show diner ext with Pause(2.789):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.789 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0008.mp3")
    play ambient "audio/Ambience/Diner_Ambience.mp3"
    scene diner int
    show jecka sc3:
        leftmidstage
        xzoom -1

    show emily sc2:
        centerstage

    $ setWait(2.789,5.333)
    $ speak(EMILY, "Yeah so uh any questions?")
    $ setWait(5.333,7.251)
    $ speak(JECKA, "Can your boyfriend get ketamine too?")
    $ setWait(7.251,8.544)
    $ speak(EMILY, "About the job?")
    $ setWait(8.544,11.672)
    $ speak(JECKA, "Oh um, don't you have to wear a uniform?")
    show emily sc2 angry:
        centerstage

    $ setWait(11.672,15.927)
    $ speak(EMILY, "We make 2 dollars an hour and the rest is in tips, I'm not wearing some ugly ass uniform.")
    $ setWait(15.927,17.804)
    $ speak(JECKA, "Yeah I guess we gotta look our best then.")
    show emily sc2:
        centerstage

    $ setWait(17.804,22.433)
    $ speak(EMILY, "Besides, the manager likes it. I'm pretty sure he dates a different waitress every month anyway.")
    $ setWait(22.433,24.977)
    $ speak(JECKA, "Is that why he wanted a picture before hiring me??")
    $ setWait(24.977,27.98)
    $ speak(EMILY, "Yeah. It's basically the Playboy Mansion with more calories.")
    show jecka sc3 angry:
        leftmidstage
        xzoom -1
    $ setWait(27.98,30.65)
    $ speak(JECKA, "More like the Playboy motorhome, we're not getting paid shit!")
    $ setWait(30.65,33.402)
    $ speak(EMILY, "Oh he actually gives a bonus if you wear open-toe shoes.")
    $ setWait(33.402,34.529)
    $ speak(JECKA, "Fuckin' why?")
    show emily sc2 upset:
        centerstage
    $ setWait(34.529,38.574)
    $ speak(EMILY, "I don't know he's 5-foot-4 and Turkish, you think he's gonna act normal?")
    show jecka sc3 sad:
        leftmidstage
        xzoom -1
    $ setWait(38.574,40.868)
    $ speak(JECKA, "I guess it's worth the bonus...")
    show jecka sc3:
        leftmidstage

    $ setWait(40.868,43.454)
    $ speak(JECKA, "And your boyfriend's just okay with all this?")

    show emily sc2:
        centerstage

    $ setWait(43.454,44.497)
    $ speak(EMILY, "Which one?")
    $ setWait(44.497,48.251)
    $ speak(JECKA, "The... Never mind. At least I'm not a whore.")
    $ setWait(48.251,49.919)
    $ speak(EMILY, "Why do you gotta work so much again?")
    $ setWait(49.919,52.922)
    $ speak(JECKA, "My Dad's forcing me to help out with the bills until college.")
    $ setWait(52.922,54.257)
    $ speak(EMILY, "Dude fuck your bitchass dad.")
    $ setWait(54.257,55.55)
    $ speak(JECKA, "I know right?")
    show emily sc2:
        centerstage
        pause 3.7
        xzoom -1
        linear 2.5 off_right

    $ setWait(55.55,61.138)
    $ speak(EMILY, "Okay well I gotta refill this old guys coffee before he starts telling me how service was better in the 60's.")
    stop ambient fadeout 1.5
    jump scene_S0009

label scene_S0009:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show bookstore ext with Pause(2.838):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.838 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0009.mp3")
    scene bookstore
    play ambient "audio/Ambience/Library_Ambience.mp3"
    show jecka sc4 smile:
        leftcenterstage
        xzoom -1

    show nicole sc3:
        rightcenterstage
        xzoom -1

    $ setWait(2.838,5.257)
    $ speak(JECKA, "Why doesn't everyone buy CDs at the bookstore?")
    $ setWait(5.257,8.385)
    $ speak(NICOLE, "Cause who the fuck buys CDs in general, what is it 2004?")

    show jecka sc4 angry:
        leftcenterstage
        xzoom -1

    $ setWait(8.385,12.431)
    $ speak(JECKA, "You don't always get locked out of your iTunes account from your exboyfriend hacking into it!")
    $ setWait(12.431,16.435)
    $ speak(NICOLE, "Wow computer literacy is the single most weaponized thing against women.")
    $ setWait(16.435,20.939)
    $ speak(JECKA, "Exactly, the CDs can't trick me into clicking on malware that calls me gay.")
    $ setWait(20.939,22.149)
    $ speak(NICOLE, "But yeah what'd you even get?")
    show jecka sc4:
        leftcenterstage
        xzoom -1
    $ setWait(22.149,25.527)
    $ speak(JECKA, "I got the entire discography of Beanie Sigel.")
    $ setWait(25.527,27.738)
    $ speak(NICOLE, "So what like 3 CDs?")
    show jecka sc4 smile:
        leftcenterstage
        xzoom -1
    $ setWait(27.738,33.41)
    $ speak(JECKA, "Yeah, plus this cute little chemistry set in the kid's section. You can make Pop Rocks but shittier.")
    $ setWait(33.41,35.412)
    $ speak(NICOLE, "Weren't your paychecks supposed to help out your Dad?")
    show jecka sc4:
        leftcenterstage
        xzoom -1
    $ setWait(35.412,37.581)
    $ speak(JECKA, "Whatever there should be enough left over.")
    $ setWait(37.581,39.792)
    $ speak(NICOLE, "Or you could buy me shoes at Journey's instead.")
    $ setWait(39.792,42.961)
    $ speak(JECKA, "Actually sure. But will you be my girlfriend after?")
    show nicole sc3 smile:
        rightcenterstage
        xzoom -1

    $ setWait(42.961,43.545)
    $ speak(NICOLE, "Nope.")

    show jecka sc4 smile:
        leftcenterstage
        xzoom -1

    $ setWait(43.545,46.298)
    $ speak(JECKA, "Ugh you were just using me the whole time, you're a whore!")
    show jecka sc4:
        leftcenterstage
        xzoom -1
        pause 0.65
        xzoom 1

    show nicole sc3:
        rightcenterstage
        xzoom -1

    show jeffery work:
        off_left
        xzoom -1
        linear 1.4 leftmidstage



    $ setWait(46.298,48.425)
    $ speak(JEFFERY, "Yep I've been there before.")
    $ setWait(48.425,49.551)
    $ speak(NICOLE, "Why are you stalking us?")
    $ setWait(49.551,52.137)
    $ speak(JEFFERY, "What do you mean? I work here!")
    $ setWait(52.137,54.598)
    $ speak(JECKA, "Oh cool, well...")
    $ setWait(54.598,55.474)
    $ speak(JECKA, "...fuck off.")
    show jeffery work angry:
        leftmidstage
        xzoom -1

    $ setWait(55.474,60.02)
    $ speak(JEFFERY, "One day you girls won't be so lucky and are gonna have to face life how it really is.")
    $ setWait(60.02,62.481)
    $ speak(NICOLE, "Is getting sexually assaulted every week lucky?")
    $ setWait(62.481,65.734)
    $ speak(JEFFERY, "Be grateful somebody even wants you in the first place.")
    $ setWait(65.734,67.444)
    $ speak(NICOLE, "Ohhhh I wanna kill you.")
    show jecka sc4 angry:
        leftcenterstage
        xzoom 1
    $ setWait(67.444,70.823)
    $ speak(JECKA, "Ring us up before I beat your before-photo lookin' ass into dust.")
    show jeffery work:
        leftmidstage
        xzoom -1
    $ setWait(70.823,74.868)
    $ speak(JEFFERY, "Alright fine. But wait, you don't have any books?")
    $ setWait(74.868,77.204)
    $ speak(JECKA, "Why the fuck does that matter? Ring me up!")
    $ setWait(77.204,83.335)
    $ speak(JEFFERY, "Books are the best part of this place. You can read about trains, or anime, or podiatry, or fantasy.")
    show nicole sc3 angry:
        rightcenterstage
        xzoom -1
    $ setWait(83.335,86.338)
    $ speak(NICOLE, "Who fuckin' cares about fantasy? I got my own problems, dude.")
    $ setWait(86.338,89.383)
    $ speak(JEFFERY, "Are you telling me you didn't like Harry Potter?")
    show nicole sc3:
        rightcenterstage
        xzoom -1

    show jecka sc4 angry:
        leftcenterstage
        xzoom 1

    $ setWait(89.383,91.552)
    $ speak(NICOLE, "Didn't like? I didn't fuckin' read it.")
    $ setWait(91.552,92.553)
    $ speak(JEFFERY, "Oh dear.")
    $ setWait(92.553,95.764)
    $ speak(JECKA, "Is that why you wear those stupid glasses? Cause of Harry Potter?")
    $ setWait(95.764,100.477)
    $ speak(JEFFERY, "No- Maybe- Harry Potter is just so relatable, how can you not like it?")
    $ setWait(100.477,103.897)
    $ speak(NICOLE, "Dude bitches don't give head or pussy or anything in it, they just care about school.")
    $ setWait(103.897,106.65)
    $ speak(JECKA, "Yeah we see why you find it relatable, no one fucks in it.")
    show jeffery work angry:
        leftmidstage
        xzoom -1
    $ setWait(106.65,110.779)
    $ speak(JEFFERY, "That is not the point, ugh just follow me to the register...")
    show jeffery work angry:
        leftmidstage
        xzoom 1
        linear 1.5 off_left
    $ setWait(110.779,113.073)
    $ speak(JEFFERY, "...Over-socialized women.")
    show jecka sc4:
        leftcenterstage
        linear 2.5 off_farleft

    show nicole sc3:
        rightcenterstage
        xzoom -1
        linear 2.5 off_left
    $ setWait(113.073,115.242)
    $ speak(NICOLE, "We're gonna make pretty lampshades.")
    stop ambient fadeout 1.5
    jump scene_S0010

label scene_S0010:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0010.mp3")
    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene parkinglot
    show jecka sc5 smoke:
        rightcenterstage

    show emily sc3:
        leftcenterstage
        xzoom -1

    $ setWait(0.126,3.338)
    $ speak(JECKA, "I wish there was something more relaxing than cigarettes.")
    $ setWait(3.338,4.255)
    $ speak(EMILY, "Death.")
    $ setWait(4.255,7.842)
    $ speak(JECKA, "Yeah, by the way where'd you get your purple jeans? I want some.")
    $ setWait(7.842,10.845)
    $ speak(EMILY, "Shop in Georgetown, they were like 200 dollars.")
    $ setWait(10.845,13.681)
    $ speak(JECKA, "How do you blow 200 on jeans when we're getting paid the same?")
    $ setWait(13.681,15.475)
    $ speak(EMILY, "You think this is my only job?")
    $ setWait(15.475,20.23)
    $ speak(JECKA, "Wow I can barely do this job. I don't why but I feel like we're too pretty to work.")

    show emily sc3 smile:
        leftcenterstage
        xzoom -1

    $ setWait(20.23,24.484)
    $ speak(EMILY, "What do they say... If you love what you do you'll never work a day in your life.")
    $ setWait(24.484,25.902)
    $ speak(JECKA, "Cool so what do you do?")
    show emily sc3:
        leftcenterstage
        xzoom -1

    $ setWait(25.902,29.113)
    $ speak(EMILY, "I sell cough medicine to middleschoolers and tell them it's heroin.")
    $ setWait(29.113,30.657)
    $ speak(JECKA, "Fuck now I want a side-job.")
    show emily sc3 angry:
        leftcenterstage
        xzoom -1
    $ setWait(30.657,34.911)
    $ speak(EMILY, "You gotta get this job under control first, manager keeps bitching about you coming in late.")
    $ setWait(34.911,36.329)
    $ speak(JECKA, "You come in late with me.")
    show emily sc3:
        leftcenterstage
        xzoom -1
    $ setWait(36.329,41.584)
    $ speak(EMILY, "Yeah but I don't really give a shit if I get fired, new boyfriend, lots of money, bought me these pants actually.")
    $ setWait(41.584,43.711)
    $ speak(JECKA, "I thought you got 'em with your side-job money.")
    show emily sc3 smile:
        leftcenterstage
        xzoom -1
    $ setWait(43.711,46.965)
    $ speak(EMILY, "No I just changed the subject so I'd look cool and independent.")
    $ setWait(46.965,49.175)
    $ speak(JECKA, "Oh so who's your new guy?")
    show emily sc3:
        leftcenterstage
        xzoom -1
    $ setWait(49.175,53.846)
    $ speak(EMILY, "He's older but not like totally lame, like he's actually really fucking cool for an old guy.")
    $ setWait(53.846,55.515)
    $ speak(JECKA, "Is he actually rich?")
    $ setWait(55.515,58.142)
    $ speak(EMILY, "I mean I work here so rich to me.")
    $ setWait(58.142,61.062)
    $ speak(JECKA, "Yeah I guess, how much has he spent on you?")
    $ setWait(61.062,63.314)
    $ speak(EMILY, "Lost count, easily a thousand.")
    $ setWait(63.314,65.441)
    $ speak(JECKA, "Cool it sounds like he really likes you.")
    $ setWait(65.441,67.277)
    $ speak(EMILY, "Cause he spends money on me?")
    $ setWait(67.277,70.822)
    $ speak(JECKA, "Well it's not like men can communicate so that's kinda all we have to go off of.")
    show emily sc3 upset:
        leftcenterstage
        xzoom -1
    $ setWait(70.822,75.493)
    $ speak(EMILY, "How do you say that about men after gushing over Ryan Sheckler for like 50 hours?")
    $ setWait(75.493,76.244)
    $ speak(JECKA, "So?")
    $ setWait(76.244,77.412)
    $ speak(EMILY, "So he's a man.")
    $ setWait(77.412,81.291)
    $ speak(JECKA, "Ryan Sheckler's more than a man, he's a man with a gold medal at the X-Games.")
    $ setWait(81.291,86.17)
    $ speak(JECKA, "Any time he comes into town I flip out, he'll be my favorite forever and ever.")
    $ setWait(86.17,90.216)
    $ speak(EMILY, "But Life Of Ryan is like the worst show on TV...")
    $ setWait(90.216,92.135)
    $ speak(JECKA, "No it isn't, anime exists.")
    stop ambient fadeout 1.5
    jump scene_S0011

label scene_S0011:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0011.mp3")
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1
    scene mall int
    show jecka sc6 smile:
        leftstage
        xzoom -1
        linear 2 leftcenterstage


    $ setWait(0.085,2.588)
    $ speak(JECKA, "I wanna one-up this bitch with purple shorts.")

    $ setWait(2.588,5.591)
    $ speak(JECKA, "Like if Daisy Duke got her laundry mixed up with Grimace.")
    show jeffery sc1 smile:
        off_right
        linear 1.4 rightcenterstage

    show jecka sc6:
        leftcenterstage
        xzoom -1
    $ setWait(5.591,11.096)
    $ speak(JEFFERY, "Grimace? Are you keeping up with the Wacky Adventures of Ronald McDonald canon too?")
    $ setWait(11.096,12.806)
    $ speak(JECKA, "Wh... What?")
    $ setWait(12.806,20.856)
    $ speak(JEFFERY, "The Ronald McDonald cartoon? It was made by the same studio that gave us Rugrats and The Wild Thornberrys.")
    show jecka sc6 sad:
        leftcenterstage
        xzoom -1

    show jeffery sc1:
        rightcenterstage

    $ setWait(20.856,24.026)
    $ speak(JECKA, "Jeffery, please don't rape any women, they've had enough.")

    show jecka sc6:
        leftcenterstage
        xzoom -1
    $ setWait(24.026,27.446)
    $ speak(JEFFERY, "Wha- Hey I wouldn't want that to happen to any woman...")
    $ setWait(27.446,29.281)
    $ speak(JEFFERY, "Provided she's not mean to people.")
    $ setWait(29.281,29.99)
    $ speak(JECKA, "Wow.")
    $ setWait(29.99,30.95)
    $ speak(JEFFERY, "What's wrong?")
    show jecka sc6:
        leftcenterstage
        xzoom -1
        pause 1.3
        xzoom 1
        linear 1.1 leftstage

    $ setWait(30.95,33.16)
    $ speak(JECKA, "Nothing fixable, so I gotta go now.")
    show jeffery sc1:
        rightcenterstage
        linear 0.4 centerstage

    $ setWait(33.16,36.705)
    $ speak(JEFFERY, "Wait but, could I talk about something with you?")
    show jecka sc6 angry:
        xzoom -1
        leftstage
        linear 0.8 leftmidstage
    $ setWait(36.705,38.499)
    $ speak(JECKA, "Talk about what?")
    show jeffery sc1 blush:
        centerstage
    $ setWait(38.499,40.125)
    $ speak(JEFFERY, "About us?")
    show jecka sc6:
        leftmidstage
        xzoom -1
    $ setWait(40.125,44.004)
    $ speak(JECKA, "Well I need funny stories for Kelly's party this weekend so sure.")
    show jeffery sc1:
        centerstage
    $ setWait(44.004,50.594)
    $ speak(JEFFERY, "Okay, I just wanted to apologize and explain why things were so awkward between us in high school.")
    $ setWait(50.594,52.012)
    $ speak(JECKA, "Us or everyone you meet?")

    $ setWait(52.012,56.85)
    $ speak(JEFFERY, "But now that we're graduated I guess it won't hurt to come clean with this...")
    show jeffery sc1 blush:
        centerstage
    $ setWait(56.85,62.189)
    $ speak(JEFFERY, "I've always sort of been a secret admirer of yours.")
    show jecka sc6:
        xzoom -1
        leftmidstage
        pause 1.6
        xzoom 1
        linear 0.8 leftstage
    $ setWait(62.189,64.608)
    $ speak(JECKA, "Okay well hey I gotta go to work now.")
    $ setWait(64.608,71.574)
    $ speak(JEFFERY, "No, no I'm serious! I like your hair, and your face, and some other things too but I don't wanna be inappropriate.")
    show jecka sc6:
        leftstage
        xzoom -1
        linear 0.7 leftmidstage
    $ setWait(71.574,75.953)
    $ speak(JECKA, "No go ahead and tell me while I dial 911 for an unrelated reason.")
    $ setWait(75.953,78.789)
    $ speak(JEFFERY, "Well if you want me to...")
    $ setWait(78.789,82.793)
    $ speak(JEFFERY, "I always like how your jeans fit your body...")
    $ setWait(82.793,86.755)
    $ speak(JEFFERY, "...And I like that your feet are really small and cute.")
    show jecka sc6 sad:
        leftmidstage
        xzoom -1
    $ setWait(86.755,87.965)
    $ speak(JECKA, "Did you say feet?")
    $ setWait(87.965,93.887)
    $ speak(JEFFERY, "Yeah I just like to- Oh- Open-toe shoes! Are you wearing those for a special occasion?")
    show jecka sc6:
        leftmidstage
        xzoom -1
    $ setWait(93.887,95.472)
    $ speak(JECKA, "No they're just for work.")
    show jeffery sc1 smile:
        centerstage
    $ setWait(95.472,99.268)
    $ speak(JEFFERY, "But yeah I just love a cute pair of feet.")
    $ setWait(99.268,102.479)
    $ speak(JECKA, "So you don't like ass or titties or any of that? Just the feet?")
    $ setWait(102.479,104.189)
    $ speak(JEFFERY, "Well primarily the feet.")
    show trody sc1:
        off_left
        xzoom -1
        linear 1.2 leftstage
    $ setWait(104.189,105.649)
    $ speak(TRODY, "Oh hey Jecka what's up?")
    show jecka sc6 sad:
        leftmidstage
        xzoom 1

    show jeffery sc1:
        centerstage

    $ setWait(105.649,106.734)
    $ speak(JECKA, "Please don't get near this.")
    show trody sc1:
        xzoom 1
        leftstage
        linear 0.66 off_left
    $ setWait(106.734,107.818)
    $ speak(TRODY, "Oh okay.")
    $ setWait(107.818,110.404)
    $ speak(JEFFERY, "So you ever step on anybody with those?")
    show jecka sc6 sad:
        leftmidstage
        xzoom -1

    $ setWait(110.404,111.905)
    $ speak(JECKA, "With my feet? No.")
    $ setWait(111.905,116.41)
    $ speak(JEFFERY, "Oh well if you need a hundred dollars I could pay you to step on me.")
    $ setWait(116.41,118.787)
    $ speak(JECKA, "Step on you? Why would you pay for that?")
    $ setWait(118.787,122.75)
    $ speak(JEFFERY, "I don't know I just like it, it feels good to me.")
    $ setWait(122.75,125.294)
    $ speak(JECKA, "Hundred dollar- Fuckin'- Jeffery I'm gonna be late for work.")
    $ setWait(125.294,126.503)
    $ speak(JEFFERY, "What about 200?")
    show jecka sc6 surprised:
        leftmidstage
        xzoom -1

    $ setWait(126.503,128.881)
    $ speak(JECKA, "200?? To step on you?")

    show jeffery sc1 smile:
        centerstage

    $ setWait(128.881,134.887)
    $ speak(JEFFERY, "Well provided your shoes are off, of course. We can do it in a family-sized restroom here in the mall.")
    show jecka sc6 sad:
        leftmidstage
        xzoom -1

    $ setWait(134.887,138.182)
    $ speak(JECKA, "Fuck that's like twice what I'm making at work today...")
    menu:
        "$200 IS $200":
            jump scene_S0012
        "HE NEEDS TO BE NORMAL":

            jump scene_S0041

label scene_S0012:
    $ setVoiceTrack("audio/Scenes/0012.mp3")
    scene mall int
    show jecka sc6:
        leftmidstage
        xzoom -1

    show jeffery sc1:
        centerstage
    $ setWait(0.043,4.839)
    $ speak(JECKA, "Okay fine where do we do it? I think Old Navy's nearby we could try the lady's section.")
    $ setWait(4.839,6.549)
    $ speak(JEFFERY, "Old Navy, why there?")
    $ setWait(6.549,12.388)
    $ speak(JECKA, "Cause the two bitches who shop at Old Navy are either too ugly to be judgmental or no bitches at all.")
    $ setWait(12.388,15.433)
    $ speak(JEFFERY, "I think a private restroom in the mall might be better.")
    $ setWait(15.433,17.894)
    $ speak(JECKA, "Okay let's do it in the bathroom at Crate & Barrel.")
    $ setWait(17.894,22.941)
    $ speak(JEFFERY, "Um actually, if I could suggest the lady's room at Starbucks.")
    $ setWait(22.941,24.609)
    $ speak(JECKA, "...You just had that one ready.")

    show jeffery sc1 smile:
        centerstage

    $ setWait(24.609,31.366)
    $ speak(JEFFERY, "Yeah I've done this a few times before at the mall with other girls and the Starbucks restroom is pretty much a foot favorite.")
    $ setWait(31.366,32.2)
    $ speak(JECKA, "Why?")
    $ setWait(32.2,41.209)
    $ speak(JEFFERY, "Oh lots of space, pretty quiet and secluded, and the tiles are really smooth and soft so they don't rough up those cute little feet of yours.")
    $ setWait(41.209,44.212)
    $ speak(JECKA, "And you're not gonna murder me once we're in there?")
    show jeffery sc1:
        centerstage

    $ setWait(44.212,48.299)
    $ speak(JEFFERY, "Of course not! I wanna take care of your feet, not hurt them.")
    $ setWait(48.299,49.634)
    $ speak(JECKA, "But the rest of me's expendable.")
    $ setWait(49.634,51.511)
    $ speak(JEFFERY, "So yeah c'mon let's go to Starbucks.")
    $ setWait(51.511,53.179)
    $ speak(JECKA, "Are you gonna buy me coffee first?")

    show jeffery sc1 smile:
        centerstage

    $ setWait(53.179,56.182)
    $ speak(JEFFERY, "I think there's more than enough room in the budget for that.")
    $ setWait(56.182,60.562)
    $ speak(JECKA, "And is that coming out of my payment or is it coffee in addition to the 200?")
    $ setWait(60.562,66.609)
    $ speak(JEFFERY, "For you, coffee plus the 200. I wanna make sure you're taken care of since you haven't done this before.")
    $ setWait(66.609,69.862)
    $ speak(JECKA, "Wow I wish men I actually consider sexually told me that.")
    $ setWait(69.862,73.866)
    $ speak(JEFFERY, "Who knows? Foot services are a great way to start relationships.")
    $ setWait(73.866,76.995)
    $ speak(JECKA, "Jeffery, I wouldn't even consider you for a friendship.")
    show jeffery sc1:
        centerstage

    $ setWait(76.995,79.205)
    $ speak(JEFFERY, "But... But why?")
    $ setWait(79.205,82.041)
    $ speak(JECKA, "Don't take this the wrong way but...")
    $ setWait(82.041,84.627)
    $ speak(JECKA, "...You look like you'd fuck your pets.")
    $ setWait(84.627,85.878)
    $ speak(JEFFERY, "I...")
    $ setWait(85.878,86.921)
    $ speak(JEFFERY, "...would never.")
    $ setWait(86.921,89.966)
    $ speak(JECKA, "Okay don't worry about it, am I gonna step on you or what?")
    show jeffery sc1 smile:
        centerstage

    $ setWait(89.966,92.76)
    $ speak(JEFFERY, "The most amazing words a woman can say.")
    show jecka sc6 angry:
        leftmidstage
        xzoom -1
    $ setWait(92.76,93.595)
    $ speak(JECKA, "God dammit.")
    $ setWait(93.595,102.353)
    $ speak(JEFFERY, "It's somewhat ironic that your face and your feet are on opposite parts of your body when they're by far your cutest features.")
    show jecka sc6:
        leftmidstage
        xzoom -1
    $ setWait(102.353,104.814)
    $ speak(JECKA, "...Is that supposed to turn me on? I don't get it.")
    $ setWait(104.814,107.15)
    $ speak(JEFFERY, "No but maybe this will...")
    $ setWait(107.15,111.237)
    $ speak(JEFFERY, "I think you're prettier than most of my favorite anime crushes.")
    $ setWait(111.237,115.033)
    $ speak(JECKA, "\"Most of\". As in there's still literal drawings that rank ahead of me.")
    show jeffery sc1 smile:
        centerstage
        xzoom -1
        linear 2.8 off_right
    $ setWait(115.033,118.119)
    $ speak(JEFFERY, "C'mon let's go to Starbucks and buy you that coffee.")
    show jecka sc6 sad:
        leftmidstage
        xzoom -1
        linear 4 off_right

    $ setWait(118.119,122.489)
    $ speak(JECKA, "The only circumstance where a white girl isn't happy to hear that.")
    stop ambient fadeout 1.5
    jump scene_S0013

label scene_S0013:
    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.6 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.4 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0013.mp3")
    play ambient "audio/Ambience/Restroom_Ambience.mp3" fadein 1
    scene cut0013a
    $ csbox = True
    $ setWait(0.082,3.794)
    $ speak(JEFFERY, "Mmm they feel like fleshy playdough.")
    scene cut0013b
    $ setWait(3.794,5.838)
    $ speak(JECKA, "Uh huh.")
    $ setWait(5.838,11.385)
    $ speak(JEFFERY, "I like a girl that takes good care of her feet, yours are so nice and soft.")
    scene cut0013c
    $ setWait(11.385,12.177)
    $ speak(JECKA, "Oh yeah?")
    $ setWait(12.177,17.891)
    $ speak(JEFFERY, "I just wanna carry you everywhere so you never need to rough these up a day in your life.")
    scene cut0013a
    $ setWait(17.891,20.644)
    $ speak(JECKA, "Kinda like I'm not a person? Yeah cool.")
    $ setWait(20.644,24.439)
    $ speak(JEFFERY, "Also, would you mind if I complimented the rest of your body?")
    scene cut0013d
    $ setWait(24.439,25.732)
    $ speak(JECKA, "Jeffery, no!")
    $ setWait(25.732,30.32)
    $ speak(JEFFERY, "Okay cause from this angle you look very sexually tall.")
    $ setWait(30.32,31.738)
    $ speak(JECKA, "What the fuck did I just tell you?")
    $ setWait(31.738,34.199)
    $ speak(JEFFERY, "I asked you if you'd mind and you said no.")
    $ setWait(34.199,36.243)
    $ speak(JECKA, "No I meant \"No don't do that\".")
    $ setWait(36.243,38.161)
    $ speak(JEFFERY, "Oh sorry then.")
    scene cut0013a
    $ setWait(38.161,40.455)
    $ speak(JECKA, "No apology will erase this trauma.")
    $ setWait(40.455,44.251)
    $ speak(JEFFERY, "I'll just resume snuggling my cheeks up to these cute little toes.")
    $ setWait(44.251,47.504)
    $ speak(JECKA, "It's only been like 90 seconds and I already wanna kill myself.")
    $ setWait(47.504,51.341)
    $ speak(JEFFERY, "Kill yourself? But these size 6 feet are so cute.")
    scene cut0013c
    $ setWait(51.341,52.175)
    $ speak(JECKA, "Size 7.")
    $ setWait(52.175,54.97)
    $ speak(JEFFERY, "Are you sure? They feel like a size 6.")
    scene cut0013d
    $ setWait(54.97,56.597)
    $ speak(JECKA, "I think I'd be the expert here.")
    $ setWait(56.597,62.394)
    $ speak(JEFFERY, "Okay you're right, mmm. Mmm softer than cotton candy.")
    $ setWait(62.394,63.77)
    $ speak(JECKA, "Okay time's up, Jeffery.")
    $ setWait(63.77,66.94)
    $ speak(JEFFERY, "Just five more minutes before I exit the gates of heaven?")
    $ setWait(66.94,70.277)
    $ speak(JECKA, "You're gonna enter the gates of hell if you don't get the fuck off my feet.")
    scene cut0013f
    $ setWait(70.277,71.486)
    $ speak(MEGAN, "Are you done in there??")
    $ setWait(71.486,73.28)
    $ speak(JEFFERY, "We're busy!")
    scene cut0013e
    $ setWait(73.28,75.782)
    $ speak(JECKA, "That was unsettlingly aggressive.")
    $ setWait(75.782,79.786)
    $ speak(JEFFERY, "Me and the community just wanna enjoy feet and no one gets it.")
    scene cut0013c
    $ setWait(79.786,80.913)
    $ speak(JECKA, "A community?")
    $ setWait(80.913,86.418)
    $ speak(JEFFERY, "Yeah we all talk online, just likeminded fellas who'd love feet like yours.")
    $ setWait(86.418,91.173)
    $ speak(JECKA, "Y'know the internet also has likeminded fellas who molest kids, is that okay too?")
    $ setWait(91.173,96.053)
    $ speak(JEFFERY, "Mmm- What was that? I was just nuzzling my nose between these adorable toes.")
    $ setWait(96.053,98.055)
    $ speak(JECKA, "Never mind, that answered my question.")
    $ setWait(98.055,103.226)
    $ speak(JEFFERY, "But if you'd like any more work like this I could post a recommendation on our online forum.")
    $ setWait(103.226,104.186)
    $ speak(JECKA, "What forum?")
    $ setWait(104.186,106.104)
    $ speak(JEFFERY, "FeetMeet.com")
    scene cut0013e
    $ setWait(106.104,107.773)
    $ speak(JECKA, "It had to rhyme...")
    stop ambient fadeout 1.5
    jump scene_S0014

label scene_S0014:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0014.mp3")
    play ambient "audio/Ambience/Diner_Ambience.mp3" fadein 1
    $ csbox = False
    scene diner int
    show jecka sc6 sad:
        off_left
        xzoom -1
        linear 1.2 leftcenterstage

    $ setWait(0.043,2.754)
    $ speak(JECKA, "Never doing that again. God I hope I'm not too late.")
    show emily sc4 angry:
        off_right
        linear 1.5 rightcenterstage

    $ setWait(2.754,4.006)
    $ speak(EMILY, "Where the fuck were you!?")
    show jecka sc6 surprised:
        leftcenterstage
        xzoom -1
    $ setWait(4.006,4.715)
    $ speak(JECKA, "Customers!")
    $ setWait(4.715,7.593)
    $ speak(EMILY, "They're already upset cause we can't keep up with the lunch rush!")
    show jecka sc6 sad:
        leftcenterstage
        xzoom -1
    $ setWait(7.593,10.512)
    $ speak(JECKA, "Sorry yeah I got my foot caught on a...")
    $ setWait(10.512,12.347)
    $ speak(EMILY, "Bitch no one cares about your foot!")
    show jecka sc6:
        leftcenterstage
        xzoom -1
    $ setWait(12.347,13.724)
    $ speak(JECKA, "Well at least one person.")
    $ setWait(13.724,16.602)
    $ speak(EMILY, "This is the fourth time you were late so manager said you're fired.")
    show jecka sc6 angry:
        leftcenterstage
        xzoom -1
    $ setWait(16.602,17.811)
    $ speak(JECKA, "What!? Come on!")
    show emily sc4:
        rightcenterstage

    $ setWait(17.811,19.104)
    $ speak(EMILY, "Take it up with him, dude.")
    $ setWait(19.104,22.441)
    $ speak(JECKA, "I don't wanna talk to him, he always puts his hand on my hip to console me.")
    $ setWait(22.441,24.651)
    $ speak(EMILY, "Well he can't reach your shoulder, he's' 5'4.")
    show jecka sc6 sad:
        leftcenterstage
        xzoom -1
    $ setWait(24.651,26.945)
    $ speak(JECKA, "Can you just tell him I was robbed or whatever?")
    $ setWait(26.945,30.782)
    $ speak(EMILY, "I would but I'd rather steal a ten minute break by throwing up in the bathroom.")
    $ setWait(30.782,33.035)
    $ speak(JECKA, "Ugh that sounds really good right now.")
    show emily sc4 smile:
        rightcenterstage
        linear 2 off_left

    $ setWait(33.035,34.87)
    $ speak(EMILY, "Good luck.")
    show jecka sc6 sad:
        xzoom 1
        leftcenterstage

    $ setWait(34.87,37.289)
    $ speak(JECKA, "Christ, how am I gonna pay these bills now?")
    show jecka sc6:
        xzoom 1
        leftcenterstage
        pause 0.5
        xzoom -1

    show crispin sc2 smile:
        off_right
        linear 2 rightcenterstage

    $ setWait(37.289,41.126)
    $ speak(CRISPIN, "Oh hey didn't know you worked here. That's pretty cool, I should come here more often.")
    show jecka sc6 angry:
        leftcenterstage
        xzoom -1
        pause 1.4
        xzoom 1
        linear 1.8 off_left

    show crispin sc2:
        rightcenterstage


    $ setWait(41.126,44.046)
    $ speak(JECKA, "Fuck off! Die! Kill! Your! Self!")
    stop ambient fadeout 1.5

    jump scene_S0015

label scene_S0015:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka night with Pause(2.546):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.546 zoom 1.04 truecenter
    $ setVoiceTrack("audio/Scenes/0015.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene livingroom jecka
    show dad undershirt angry:
        leftmidstage
        xzoom 1
    $ setWait(2.546,6.425)
    $ speak(DAD, "God I just wanna call this bitch and threaten her but- why is the service down?")
    show dad undershirt upset:
        leftmidstage
        xzoom -1
        linear 1 centerstage

    $ setWait(6.425,7.76)
    $ speak(DAD, "Jessica!")
    show jecka pj:
        off_right
        linear 1 rightstage

    $ setWait(7.76,8.969)
    $ speak(JECKA, "Dad, I'm busy!")
    $ setWait(8.969,9.845)
    $ speak(DAD, "With what?")
    $ setWait(9.845,13.724)
    $ speak(JECKA, "I'm online cramming a bunch of votes for what the new Apple Jacks flavor should be.")
    $ setWait(13.724,19.772)
    $ speak(DAD, "Internet but no phone... Did you pay the phone bill? That became one of your responsibilities.")
    $ setWait(19.772,22.358)
    $ speak(JECKA, "Um like maybe I don't know.")
    $ setWait(22.358,23.817)
    $ speak(DAD, "Why didn't you?")
    $ setWait(23.817,27.154)
    $ speak(JECKA, "Uh well, money's kinda tight right now.")
    $ setWait(27.154,30.282)
    $ speak(DAD, "You're still going to that job, right?")
    $ setWait(30.282,31.367)
    $ speak(JECKA, "Basically.")
    $ setWait(31.367,33.869)
    $ speak(DAD, "And you're managing your income wisely?")
    show dad undershirt angry:
        centerstage
        xzoom -1

    $ setWait(33.869,36.914)
    $ speak(DAD, "Unlike your whore fucking mother!?")
    show jecka pj sad:
        rightstage

    $ setWait(36.914,39.959)
    $ speak(JECKA, "Wh... What was the first part? A lot just happened there.")

    show dad undershirt:
        centerstage
        xzoom -1

    $ setWait(39.959,43.629)
    $ speak(DAD, "Honey, what's wrong at work? They're paying you your hours, right?")

    show jecka pj:
        rightstage

    $ setWait(43.629,47.758)
    $ speak(JECKA, "Basically but there's this stupid tipping rule and tips are entirely subjective so--")
    $ setWait(47.758,52.638)
    $ speak(DAD, "Whoa now it sounds like you might be making excuses for poor performance on the job.")
    show jecka pj angry:
        rightstage

    $ setWait(52.638,54.265)
    $ speak(JECKA, "Okay just fuckin' take their side.")
    $ setWait(54.265,59.853)
    $ speak(DAD, "See when I was your age even the jobs at the very bottom were taken far more seriously.")
    $ setWait(59.853,60.938)
    $ speak(JECKA, "I wonder why.")
    $ setWait(60.938,68.946)
    $ speak(DAD, "Because back then people cared about contributing to a community. Remember those 4 months after 9/11? How together we were?")
    show dad undershirt smile:
        centerstage
        xzoom -1

    $ setWait(68.946,74.285)
    $ speak(DAD, "That might be the last time we'll ever see this country just get along.")
    $ setWait(74.285,78.872)
    $ speak(JECKA, "Dad you were pulling Arab guys out of cabs and beating the shit out of them, how is that getting along?")
    show dad undershirt:
        centerstage
        xzoom -1

    $ setWait(78.872,84.044)
    $ speak(DAD, "We were having fun- so okay, let me give you a few tips on how I worked at a diner back then.")
    $ setWait(84.044,85.087)
    $ speak(JECKA, "Yeah alright.")
    $ setWait(85.087,91.093)
    $ speak(DAD, "First off, work can be tough but you need to always remember to be smiling and friendly.")
    show dad undershirt smile:
        centerstage
        xzoom -1

    $ setWait(91.093,98.6)
    $ speak(DAD, "You never know what sort of day the customer was having, so whether it be their struggles or insecurities, meet them with kindness.")
    show jecka pj:
        rightstage

    $ setWait(98.6,100.352)
    $ speak(JECKA, "This is already way too hard.")
    $ setWait(100.352,108.944)
    $ speak(DAD, "Step two, small talk. It's the key to opening a real connection between you and the customer. If you can open that, they'll open their wallet for tips.")
    $ setWait(108.944,109.486)
    $ speak(JECKA, "No they won't--")
    $ setWait(109.486,121.165)
    $ speak(DAD, "And lastly, the old adage: the customer's always right. If there's ever a point of disagreement, do you what you can to make it right.")
    $ setWait(121.165,124.501)
    $ speak(JECKA, "Got it. So if they say slavery should come back just go with it?")

    show dad undershirt upset:
        centerstage
        xzoom -1

    $ setWait(124.501,126.628)
    $ speak(DAD, "Just grit your teeth and move along.")
    show jecka pj smile:
        rightstage

    $ setWait(126.628,129.34)
    $ speak(JECKA, "I guess we're really lucky the president doesn't work at a Diner.")
    show dad undershirt caring:
        centerstage
        xzoom -1
    $ setWait(129.34,135.763)
    $ speak(DAD, "Truthfully honey, I don't wanna put too much pressure on you. You don't have to be perfect, just...")
    $ setWait(135.763,138.223)
    $ speak(DAD, "...don't end up a worthless whore like your mother.")
    show jecka pj angry:
        rightstage
        pause 1.2
        xzoom -1
        linear 1.3 off_right
    $ setWait(138.223,140.684)
    $ speak(JECKA, "Wow with that reassurance how could I fail?")
    show dad undershirt smile:
        centerstage
        xzoom -1
    $ setWait(140.684,143.103)
    $ speak(DAD, "That's the spirit, Jessica.")
    stop ambient fadeout 1.5
    jump scene_S0016

label scene_S0016:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0016.mp3")
    scene mall int
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1

    show nicole sc4 angry:
        rightmidstage
        xzoom -1
        linear 2.6 leftcenterstage
        xzoom 1

    show jecka sc7:
        off_right
        linear 2.75 rightcenterstage

    $ setWait(0.043,3.296)
    $ speak(NICOLE, "We've been to this mall ten times, I don't think you're gonna find a job here.")
    show jecka sc7 sad:
        rightcenterstage

    $ setWait(3.296,5.423)
    $ speak(JECKA, "It's been a week, someone had to quit, right?")
    $ setWait(5.423,9.427)
    $ speak(NICOLE, "You went to PacSun, every girl wants to work there. It's like you're not even trying to get hired.")
    show jecka sc7:
        rightcenterstage


    $ setWait(9.427,11.846)
    $ speak(JECKA, "That was just one place, I got a bunch more on the list.")

    show nicole sc4:
        leftcenterstage

    $ setWait(11.846,15.809)
    $ speak(NICOLE, "I guess it's just more places I can steal shit while you distract them with begging for employment.")
    $ setWait(15.809,18.186)
    $ speak(JECKA, "Oh yeah, what'd you get from Circuit City?")
    $ setWait(18.186,19.354)
    $ speak(NICOLE, "You mean Best Buy?")
    $ setWait(19.354,21.564)
    $ speak(JECKA, "Yeah what'd you get from different colored Circuit City?")
    $ setWait(21.564,24.442)
    $ speak(NICOLE, "I stole a demo iPod, just ripped it off the stand.")
    $ setWait(24.442,26.194)
    $ speak(JECKA, "That should go for something on eBay.")
    $ setWait(26.194,28.988)
    $ speak(NICOLE, "Sure-- Wait. What if that's your job?")
    $ setWait(28.988,30.198)
    $ speak(JECKA, "Working for eBay?")
    $ setWait(30.198,32.575)
    $ speak(NICOLE, "Fuck no- stealing shit and selling it on eBay.")
    $ setWait(32.575,34.119)
    $ speak(JECKA, "Could that really be consistent?")
    $ setWait(34.119,37.58)
    $ speak(NICOLE, "Dude totally. Your margins would be infinite cause you're not paying for anything.")
    show jecka sc7 sad:
        rightcenterstage
    $ setWait(37.58,39.707)
    $ speak(JECKA, "I don't know that sounds like a lot of work.")
    show nicole sc4 angry:
        leftcenterstage
    $ setWait(39.707,46.131)
    $ speak(NICOLE, "Fuckin' everything you've applied for sounds like a lot of work. Rainforest Cafe? Baby-talking kids while their dad stares at your tits?")

    show jecka sc7:
        rightcenterstage

    $ setWait(46.131,51.761)
    $ speak(JECKA, "Yeah but that's all work where I can turn my brain off. If I fuck it up I can just get another job with no consequences.")
    show nicole sc4:
        leftcenterstage

    $ setWait(51.761,54.013)
    $ speak(NICOLE, "Oh my god, where are you applying next?")

    $ setWait(54.013,57.976)
    $ speak(JECKA, "Oh uh... like... Maytag?")
    $ setWait(57.976,62.48)
    $ speak(NICOLE, "I don't think I could fit a washer/drier in my back pocket. I'll be at the food court while you do that.")
    show jecka sc7 smile:
        rightcenterstage

    $ setWait(62.48,64.441)
    $ speak(JECKA, "Yeah good luck on your free samples rounds.")
    show nicole sc4 smile:
        leftcenterstage
        linear 3 off_right

    $ setWait(64.441,68.069)
    $ speak(NICOLE, "Fuck that Asian-meat-on-a-toothpick shit, I'm gettin' Popeyes.")

    show jecka sc7 smile:
        rightcenterstage
        linear 3.5 off_left

    $ setWait(68.069,71.823)
    $ speak(JECKA, "Opioids and Popeyes? Now that's watching your figure.")
    scene mall int 2
    show kyle sc1:
        leftmidstage
        xzoom -1

    show jecka sc7 smile:
        off_right
        linear 2 rightmidstage
    $ setWait(71.823,74.534)
    $ speak(KYLE, "Hey uh... Jecka?")
    show jecka sc7:
        rightmidstage

    $ setWait(74.534,76.619)
    $ speak(JECKA, "Yeah hey...")
    $ setWait(76.619,79.289)
    $ speak(KYLE, "So um...")
    show kyle sc1:
        leftmidstage
        xzoom -1
        linear 1.6 centerstage

    $ setWait(79.289,81.416)
    $ speak(KYLE, "Where do you wanna go to step on me?")
    $ setWait(81.416,84.085)
    $ speak(JECKA, "Before we get to that, you got the money?")
    show kyle sc1 sad:
        centerstage
        xzoom -1

    $ setWait(84.085,87.088)
    $ speak(KYLE, "Of course, 200 in cash just like you said.")
    $ setWait(87.088,90.175)
    $ speak(JECKA, "Alright cool. Starbucks restroom?")
    show kyle sc1:
        centerstage
        xzoom -1

    $ setWait(90.175,94.512)
    $ speak(KYLE, "Uh, actually I'd prefer the bathroom at LensCrafters.")
    show jecka sc7 angry:
        rightmidstage

    $ setWait(94.512,96.014)
    $ speak(JECKA, "Literally why?")
    $ setWait(96.014,100.977)
    $ speak(KYLE, "Just super quaint. The floor has a pretty nice tactile stick when you lift your feet off it too.")
    $ setWait(100.977,104.397)
    $ speak(JECKA, "Yeah but I can't buy a drink at LensCrafters, now can I?")
    $ setWait(104.397,106.941)
    $ speak(KYLE, "Oh you're right, you're right. After you.")
    stop ambient fadeout 1.5
    jump scene_S0017

label scene_S0017:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Restroom_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0017.mp3")
    scene cut0017a
    $ setWait(0.085,6.133)
    $ speak(KYLE, "So yeah this is just amazing timing for everything that's happened to me today.")
    scene cut0017b
    $ setWait(6.133,8.51)
    $ speak(JECKA, "Why are you telling me like I care?")
    $ setWait(8.51,12.055)
    $ speak(KYLE, "Oh... Sorry...")
    scene cut0017a
    $ setWait(12.055,14.307)
    $ speak(JECKA, "The customer...")
    scene cut0017b
    $ setWait(14.307,17.936)
    $ speak(JECKA, "But so, what did your Dad say to you?")
    $ setWait(17.936,21.815)
    $ speak(KYLE, "He was just teasing me for being some loser who can't meet girls.")
    $ setWait(21.815,24.86)
    $ speak(JECKA, "Oh yeah dads can be really mean sometimes.")
    $ setWait(24.86,27.279)
    $ speak(KYLE, "I guess he's right though.")
    scene cut0017c
    $ setWait(27.279,31.324)
    $ speak(JECKA, "Uh no way. You're meeting a girl right now, aren't you?")
    $ setWait(31.324,35.412)
    $ speak(KYLE, "Yeah but I need to pay for it, kinda doesn't count.")
    $ setWait(35.412,38.665)
    $ speak(JECKA, "It totally counts, I mean it counts to me- shit.")
    $ setWait(38.665,41.752)
    $ speak(KYLE, "Thanks, never really looked at it like that.")
    scene cut0017b
    $ setWait(41.752,44.88)
    $ speak(JECKA, "Totally, so...")
    $ setWait(44.88,47.007)
    $ speak(JECKA, "...How'd you get into feet?")
    $ setWait(47.007,53.764)
    $ speak(KYLE, "Oh well it all started after I saw Kicking & Screaming with Will Ferrell.")
    $ setWait(53.764,54.765)
    $ speak(JECKA, "Really?")
    $ setWait(54.765,59.144)
    $ speak(KYLE, "Yeah, but that wasn't all of it, just how it started.")
    $ setWait(59.144,61.229)
    $ speak(JECKA, "And how'd it end here?")
    $ setWait(61.229,67.652)
    $ speak(KYLE, "After high school all my friends moved away to college so I didn't really have much else to do.")
    $ setWait(67.652,73.241)
    $ speak(JECKA, "Agreed, having girls step on you sounds like literally the only option.")
    $ setWait(73.241,77.579)
    $ speak(KYLE, "Feeling your awesome size 6 feet really replaces the void though.")
    $ setWait(77.579,78.58)
    $ speak(JECKA, "Size 7.")
    $ setWait(78.58,81.166)
    $ speak(KYLE, "Are you sure? They seem like a 6.")
    scene cut0017c
    $ setWait(81.166,84.419)
    $ speak(JECKA, "Oh uh um... Maybe you're right.")
    $ setWait(84.419,86.588)
    $ speak(KYLE, "Yeah I'm pretty experienced in this.")
    $ setWait(86.588,91.259)
    $ speak(JECKA, "Yeah so you're always right. I just hope my next client's as experienced as you.")
    $ setWait(91.259,96.431)
    $ speak(KYLE, "Aw thanks, can I take you to buy shoes after this?")
    scene cut0017d
    $ setWait(96.431,98.35)
    $ speak(JECKA, "Shoes for me? Sure.")
    $ setWait(98.35,103.98)
    $ speak(KYLE, "Yeah and if I pay you an extra 20 can we hold hands while you look?")
    scene cut0017b
    $ setWait(103.98,105.482)
    $ speak(JECKA, "In public? No.")
    stop ambient fadeout 1.5
    jump scene_S0018

label scene_S0018:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0018.mp3")
    play ambient "audio/Ambience/CornerStore_Ambience.mp3" fadein 1
    scene department store
    show jecka sc8 smile:
        rightmidstage

    show nicole sc5:
        rightcenterstage

    $ setWait(0.168,2.546)
    $ speak(JECKA, "These are like perfect coke hangover glasses.")
    $ setWait(2.546,3.922)
    $ speak(NICOLE, "Bitch you never even done coke.")
    $ setWait(3.922,7.092)
    $ speak(JECKA, "Yeah I did, remember how wild I got at Kelly's last spring?")
    $ setWait(7.092,8.927)
    $ speak(NICOLE, "No you seemed pretty much regular.")
    $ setWait(8.927,11.68)
    $ speak(JECKA, "That's cause I took muscle relaxers right after, duh.")
    $ setWait(11.68,14.766)
    $ speak(NICOLE, "Who the hell did you have to fuck to get cocaine and muscle relaxers?")
    $ setWait(14.766,16.268)
    $ speak(JECKA, "Shut up I'm buying these.")
    $ setWait(16.268,18.019)
    $ speak(NICOLE, "But they're like 300 dollars.")
    $ setWait(18.019,20.146)
    $ speak(JECKA, "I told you I got a job again, I have money.")
    $ setWait(20.146,22.19)
    $ speak(NICOLE, "Did you cave and start stripping at that place?")
    show jecka sc8 sad:
        rightmidstage

    $ setWait(22.19,25.861)
    $ speak(JECKA, "What?? No! That's so beneath me I'd never do anything like that.")
    $ setWait(25.861,26.862)
    $ speak(NICOLE, "Then where?")
    show jecka sc8:
        rightmidstage

    $ setWait(26.862,31.491)
    $ speak(JECKA, "Oh I work at um... The anime store in Fair Oaks.")
    $ setWait(31.491,32.534)
    $ speak(NICOLE, "Are you serious?")
    $ setWait(32.534,36.121)
    $ speak(JECKA, "Yeah, it was the only place that hired me. You can go there and ask them.")
    $ setWait(36.121,39.624)
    $ speak(NICOLE, "I'll never step foot in a fuckin' anime store so I'll take your word for it.")
    show jecka sc8 smile:
        rightmidstage

    $ setWait(39.624,43.128)
    $ speak(JECKA, "Cool, with this cashflow I'll never have to be sober again.")
    $ setWait(43.128,44.212)
    $ speak(NICOLE, "Dude I wish.")
    $ setWait(44.212,47.215)
    $ speak(JECKA, "I wanna party hard every night and die before I'm 21.")
    $ setWait(47.215,53.305)
    $ speak(NICOLE, "Yeah once you're legal getting drunk isn't even cool anymore. You just look like some dumpy idiot who's depressed about working in an office.")
    $ setWait(53.305,58.476)
    $ speak(JECKA, "Exactly! I wanna die young and leave a body so hot everyone in the morgue gets fired for touching it.")
    show nicole sc5 angry:
        rightcenterstage

    $ setWait(58.476,61.396)
    $ speak(NICOLE, "Bitch no you don't, you're going to college for a job and everything.")
    $ setWait(61.396,63.189)
    $ speak(JECKA, "Everybody needs a backup plan.")
    show jecka sc8 smile:
        rightmidstage
        xzoom -1
        linear 2 off_right

    show nicole sc5:
        rightcenterstage
        pause 1
        linear 2.2 off_right

    $ setWait(63.189,64.9)
    $ speak(JECKA, "Fuck it I'm walking out with these.")
    stop ambient fadeout 1.5
    jump scene_S0019

label scene_S0019:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0019.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3" fadein 1
    scene livingroom jecka

    show dad undershirt angry:
        leftmidstage



    $ setWait(0.125,4.129)
    $ speak(DAD, "I guess Pizza Hut comes with free heart palpitations now.")
    show jecka pj angry:
        off_right
        linear 2 rightcenterstage

    $ setWait(4.129,8.3)
    $ speak(JECKA, "Dad why did you eat both pizzas when I just wanted one slice of one of them?")
    show dad undershirt smile:
        leftmidstage
        xzoom -1
        linear 0.6 leftcenterstage

    $ setWait(8.3,9.51)
    $ speak(DAD, "Oh Jessica!")

    show jecka pj sad:
        rightcenterstage
        linear 0.3 rightstage

    $ setWait(9.51,10.135)
    $ speak(JECKA, "Don't hit me!")
    $ setWait(10.135,13.931)
    $ speak(DAD, "Oh no, no. I just wanted to know your secret.")
    $ setWait(13.931,16.683)
    $ speak(JECKA, "What secret? I don't know what you're talking about.")
    $ setWait(16.683,19.853)
    $ speak(DAD, "Secret for how you're doing so well at this job.")
    $ setWait(19.853,20.854)
    $ speak(JECKA, "What do you mean?")
    $ setWait(20.854,26.527)
    $ speak(DAD, "You've been paying off the bills ahead of time, it's honestly astounding for an 18 year old.")
    show jecka pj:
        rightstage
        linear 1.2 rightcenterstage

    $ setWait(26.527,29.363)
    $ speak(JECKA, "Oh yeah, I'm just working hard, dad.")
    $ setWait(29.363,34.034)
    $ speak(DAD, "Not just hard but well, very well. Don't tell me... The 3 steps?")
    $ setWait(34.034,35.869)
    $ speak(JECKA, "I think I've done a little more than 3.")
    $ setWait(35.869,41.917)
    $ speak(DAD, "Above and beyond, great to hear it. You've done this house and my heart very proud.")
    show jecka pj sad:
        rightcenterstage
    $ setWait(41.917,43.085)
    $ speak(JECKA, "Your heart?")
    show jecka pj surprised:
        rightcenterstage
        linear 0.3 rightstage

    $ setWait(43.085,44.211)
    $ speak(JECKA, "Are you gonna molest me?")
    show dad undershirt upset:
        xzoom -1
        leftcenterstage

    $ setWait(44.211,53.011)
    $ speak(DAD, "Of course not, medically speaking. Doctor said to avoid any and all stress to prevent cardiac arrest. I'm at that age y'know.")
    show jecka pj:
        rightstage

    $ setWait(53.011,55.305)
    $ speak(JECKA, "Oh yeah, well good luck with that.")

    show dad undershirt smile:
        leftcenterstage
        xzoom -1

    $ setWait(55.305,64.189)
    $ speak(DAD, "I don't think it's so much luck as it is you. As long as you stay on this new productive path I'll be okay. No pressure, sweetie.")
    $ setWait(64.189,68.36)
    $ speak(JECKA, "Thanks dad, so I'm just gonna reorder another pizza.")
    $ setWait(68.36,70.946)
    $ speak(DAD, "Oh before you do, could you get the cable bill?")
    $ setWait(70.946,74.158)
    $ speak(JECKA, "But I wasn't even supposed to pay that one. Don't we have internet?")

    show dad undershirt:
        leftcenterstage
        xzoom -1

    $ setWait(74.158,77.536)
    $ speak(DAD, "I need you to chip in since I upgraded to get the Food Network.")
    $ setWait(77.536,79.496)
    $ speak(JECKA, "What do you need the Food Network for?")
    $ setWait(79.496,87.713)
    $ speak(DAD, "Well I figured it was time to learn a few recipes since your truckstop turnstile whore of a mother won't be cooking for us anymore.")
    show jecka pj:
        rightstage
        linear 1.2 rightcenterstage
    $ setWait(87.713,89.59)
    $ speak(JECKA, "Dad, do you really have to call her that?")
    $ setWait(89.59,90.007)
    $ speak(DAD, "Don't fucking talk back to me, I'll smack the shit out of you!!")

    show dad undershirt yell:
        leftcenterstage
        xzoom -1

    $ setWait(90.007,92.968)
    $ speak(DAD, "Don't fucking talk back to me, I'll smack the shit out of you!!")
    show jecka pj surprised:
        rightcenterstage
        linear 0.25 rightstage


    show dad undershirt angry:
        leftcenterstage
        xzoom -1

    $ setWait(92.968,94.845)
    $ speak(JECKA, "Okay! Okay! I'm sorry I'll pay it!")
    show dad undershirt angry:
        leftcenterstage
        xzoom 1
        linear 1 leftmidstage

    $ setWait(94.845,97.723)
    $ speak(DAD, "Ugh! I can't believe you'd do this to your own father.")
    show jecka pj sad:
        rightstage
        linear 0.4 rightmidstage

    $ setWait(97.723,98.348)
    $ speak(JECKA, "Do what!?")
    show dad undershirt angry:
        leftmidstage
        xzoom -1
    $ setWait(98.348,101.226)
    $ speak(DAD, "Causing me chest pains! Are you trying to kill me??")
    show jecka pj sad:
        rightmidstage
        pause 2.45
        xzoom -1

    $ setWait(101.226,106.815)
    $ speak(JECKA, "No I'm sorry! I'll buy the Food Network just don't hit me!")
    show dad undershirt smile:
        leftmidstage
        xzoom -1
        pause 1.1
        linear 2 off_right

    $ setWait(106.815,110.871)
    $ speak(DAD, "That's nice, dear. Have fun at work tomorrow.")
    stop ambient fadeout 1.5
    jump scene_S0020

label scene_S0020:
    show black onlayer screens with Pause(1.7):
        alpha 0.0
        linear 1.7 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show mart ext with Pause(2.922):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.922 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0020.mp3")
    play ambient "audio/Ambience/Mart_Ambience.mp3"
    scene kmart
    show nicole sc6 smile:
        leftcenterstage

    show jecka sc9:
        rightcenterstage

    $ setWait(2.922,7.26)
    $ speak(NICOLE, "It's kinda cool how you could just shit on the floor at K-Mart and there'd be no change in aesthetic.")

    show jecka sc9 angry:
        rightcenterstage

    $ setWait(7.26,8.511)
    $ speak(JECKA, "Fuck you, I love K-Mart.")

    show nicole sc6:
        leftcenterstage

    $ setWait(8.511,10.18)
    $ speak(NICOLE, "I do too, it was a compliment.")

    show jecka sc9:
        rightcenterstage

    $ setWait(10.18,13.933)
    $ speak(JECKA, "It's the only place where I can buy all the stuffed animals and shitty T-shirts I want.")
    $ setWait(13.933,17.02)
    $ speak(NICOLE, "Yeah but you went all out today, you picked out a whole cart's worth of shit.")
    $ setWait(17.02,21.941)
    $ speak(JECKA, "Cause half the shirts I'm gonna cut little designs in and the other half I'm gonna take sharpie and draw my own stuff.")
    $ setWait(21.941,23.026)
    $ speak(NICOLE, "Stuff like what?")

    show jecka sc9 smile:
        rightcenterstage

    $ setWait(23.026,27.197)
    $ speak(JECKA, "I don't know like a smiley face but the line for the mouth just says \"DEAD COP\".")
    $ setWait(27.197,34.204)
    $ speak(NICOLE, "Or no it could be like \"DEAD COP\" with a heart around it so cool people think you're punk and old people think you care about 9/11.")

    show jecka sc9:
        rightcenterstage


    $ setWait(34.204,38.917)
    $ speak(JECKA, "Ugh if I do a heart I'm gonna need the pink sharpie. I'll just go back and get the 48 pack.")
    $ setWait(38.917,39.918)
    $ speak(NICOLE, "Can you afford that?")
    $ setWait(39.918,41.336)
    $ speak(JECKA, "Bitch yeah I can afford that.")
    $ setWait(41.336,43.546)
    $ speak(NICOLE, "What is this anime place paying you?")
    $ setWait(43.546,45.131)
    $ speak(JECKA, "What anime place?")
    show nicole sc6 angry:
        leftcenterstage

    $ setWait(45.131,46.591)
    $ speak(NICOLE, "The one you work at?")

    show jecka sc9 sad:
        rightcenterstage

    $ setWait(46.591,50.136)
    $ speak(JECKA, "Oh yeah right um... They pay me okay.")
    $ setWait(50.136,51.429)
    $ speak(NICOLE, "Are you blowing your manager?")
    $ setWait(51.429,52.138)
    $ speak(JECKA, "No!")
    $ setWait(52.138,56.559)
    $ speak(NICOLE, "Then who's your sugar daddy cause there's no way some shitty retail job is paying this much.")
    $ setWait(56.559,59.896)
    $ speak(JECKA, "It's just... I'm just.. good with my money!")
    show jecka sc9 sad:
        rightcenterstage
        xzoom -1

    $ setWait(59.896,61.356)
    $ speak(JECKA, "Hold on I got a text.")
    $ setWait(61.356,65.485)
    $ speak(NICOLE, "You gotta be fucking the ugliest rich guy in the universe if you can't even tell me.")

    show jecka sc9 angry:
        rightcenterstage
        xzoom -1

    $ setWait(65.485,66.653)
    $ speak(JECKA, "Shut up, hold on.")
    show nicole sc6:
        leftcenterstage

    $ setWait(66.653,68.363)
    $ speak(NICOLE, "Is it the Asian guy from American Idol?")
    show jecka sc9 angry:
        rightcenterstage
        xzoom 1
    $ setWait(68.363,69.697)
    $ speak(JECKA, "Can you take a walk or something?")
    show nicole sc6 angry:
        leftcenterstage
        pause 0.3
        linear 0.2 xalign 0.53
        xzoom -1
        linear 0.3 leftmidstage

    $ setWait(69.697,70.15)
    $ speak(NICOLE, "How bout I take your phone, bitch.")
    show jecka sc9 surprised:
        rightcenterstage
        xzoom 1
        linear 0.08 xalign .64
        linear 0.08 xalign .62
        linear 0.08 rightcenterstage
    $ setWait(70.15,71.157)
    $ speak(NICOLE, "How bout I take your phone, bitch.")

    $ setWait(71.157,72.951)
    $ speak(JECKA, "Uh-- What the fuck! Give it back!")
    show nicole sc6:
        leftmidstage
        xzoom 1
    $ setWait(72.951,74.869)
    $ speak(NICOLE, "Who's \"Foot Loser 1\"?")
    show jecka sc9 angry:
        rightcenterstage
        xzoom 1
    $ setWait(74.869,76.121)
    $ speak(JECKA, "Nobody.")
    show text_footloser1 onlayer screens
    $ setWait(76.121,80.333)
    $ speak(NICOLE, "\"Can I pay extra for pink toenail polish?\".. \"$100\"...")

    show text_footloser1 onlayer screens:
        alpha 1.0
        pause 2
        alpha 0.0

    $ setWait(80.333,84.504)
    $ speak(NICOLE, "Why are you so defensive over a pedicure-- Wait how do you charge them a hundred dollars?")
    show jecka sc9 sad:
        rightcenterstage

    hide text_footloser1 onlayer screens
    $ setWait(84.504,86.965)
    $ speak(JECKA, "Okay so it's complicated.")
    $ setWait(86.965,90.468)
    $ speak(NICOLE, "Are you a foot model? Jecka, you know what The Nanny said about foot models.")
    $ setWait(90.468,91.469)
    $ speak(JECKA, "The Nanny?")
    $ setWait(91.469,93.888)
    $ speak(NICOLE, "Yeah The Nanny with Fran Dress shirt.")
    $ setWait(93.888,98.268)
    $ speak(JECKA, "No- Nicole I'm not a foot model... Scroll up.")
    show text_footloser2 onlayer screens
    $ setWait(98.268,103.565)
    $ speak(NICOLE, "\"Could you do a house call to step on me, I'm really lonely and Mom can't drive me.\".. \"50 extra.\"")
    show nicole sc6 surprised:
        leftmidstage
    $ setWait(103.565,105.942)
    $ speak(NICOLE, "What is this?")
    hide text_footloser2 onlayer screens
    $ setWait(105.942,113.074)
    $ speak(JECKA, "Uh... Guys pay me money to take my shoes off and step on them...")
    $ setWait(113.074,114.701)
    $ speak(NICOLE, "Why?")
    $ setWait(114.701,115.702)
    $ speak(JECKA, "I don't know.")

    show nicole sc6:
        leftmidstage
        linear 2 leftcenterstage
    $ setWait(115.702,118.163)
    $ speak(NICOLE, "Are they like grapes, you gotta turn 'em into wine?")
    $ setWait(118.163,122.375)
    $ speak(JECKA, "No they like it cause they're submissive or whatever.")
    $ setWait(122.375,129.382)
    $ speak(NICOLE, "O-Okay so because they're sub-- that.. they give you hundreds of dollars to just put your feet on them?")
    $ setWait(129.382,130.592)
    $ speak(JECKA, "Basically.")
    $ setWait(130.592,133.386)
    $ speak(NICOLE, "And you don't have to take your clothes off, suck dick, anything?")
    $ setWait(133.386,135.471)
    $ speak(JECKA, "Not so far.")
    show nicole sc6 surprised:
        leftcenterstage
    $ setWait(135.471,137.056)
    $ speak(NICOLE, "Dude...")
    show nicole sc6 smile:
        leftcenterstage

    $ setWait(137.056,139.142)
    $ speak(NICOLE, "...That sounds awesome, lemme go with you!")
    show jecka sc9 surprised:
        rightcenterstage

    $ setWait(139.142,140.101)
    $ speak(JECKA, "For real?")
    $ setWait(140.101,143.104)
    $ speak(NICOLE, "Money for some loser to just feel my feet? Hell yeah.")
    show jecka sc9:
        rightcenterstage

    $ setWait(143.104,145.315)
    $ speak(JECKA, "Like you actually wanna go do one with me?")
    $ setWait(145.315,147.609)
    $ speak(NICOLE, "Yeah, you're doing it tonight, right? Lemme plus-one.")
    $ setWait(147.609,148.526)
    $ speak(JECKA, "Just for free?")
    $ setWait(148.526,150.737)
    $ speak(NICOLE, "Fuck no, I want that foot money too.")
    show jecka sc9 sad:
        rightcenterstage


    $ setWait(150.737,154.449)
    $ speak(JECKA, "Yeah but... sharpies...")

    show nicole sc6 angry:
        leftcenterstage

    $ setWait(154.449,156.242)
    $ speak(NICOLE, "Bitch don't be greedy, c'mon.")

    menu:
        "DON'T SPLIT THE REVENUE":
            jump scene_S0021
        "SHARE THE TRAUMA":

            jump scene_S0031

label scene_S0021:
    $ setVoiceTrack("audio/Scenes/0021.mp3")
    scene kmart
    show jecka sc9 sad:
        rightcenterstage

    show nicole sc6 angry:
        leftcenterstage

    $ setWait(0.08,5.586)
    $ speak(JECKA, "Nicole, I like, really need the money. Cause like my Dad and everything.")
    $ setWait(5.586,6.712)
    $ speak(NICOLE, "So what?")
    $ setWait(6.712,9.047)
    $ speak(JECKA, "So I can't let you go with me.")
    $ setWait(9.047,10.34)
    $ speak(NICOLE, "Just give me like 20 percent.")
    $ setWait(10.34,11.717)
    $ speak(JECKA, "I need that 20 percent.")
    $ setWait(11.717,14.845)
    $ speak(NICOLE, "You're so lame! When we were in high school you would've totally done it with me.")
    $ setWait(14.845,20.851)
    $ speak(JECKA, "Yeah but in high school my parents weren't divorced and making me do shit. I gotta pay for internet, clothes, power, the Food Network.")
    $ setWait(20.851,21.81)
    $ speak(NICOLE, "Gay, whatever.")
    show jecka sc9 angry:
        rightcenterstage
    $ setWait(21.81,22.644)
    $ speak(JECKA, "What's gay?")
    $ setWait(22.644,23.312)
    $ speak(NICOLE, "You.")
    $ setWait(23.312,25.814)
    $ speak(JECKA, "Nicole you didn't even know this existed 5 minutes ago!")
    $ setWait(25.814,29.276)
    $ speak(NICOLE, "No you're right, have fun stepping on some loser while he jacks off to you.")
    $ setWait(29.276,30.527)
    $ speak(JECKA, "It's not like that, Nicole.")
    $ setWait(30.527,32.821)
    $ speak(NICOLE, "Then what the fuck is it like?")

    show jecka sc9 sad:
        rightcenterstage

    $ setWait(32.821,37.909)
    $ speak(JECKA, "They know it's weird and everything but.. They can't help it, they just like it...")
    $ setWait(37.909,42.372)
    $ speak(JECKA, "...And they give me a lot of money to do it so that's what I like about it.")
    $ setWait(42.372,48.837)
    $ speak(NICOLE, "When has a man ever liked anything that weird without some sexual gratification?")
    $ setWait(48.837,50.213)
    $ speak(JECKA, "I'm sure there's some guys.")
    $ setWait(50.213,60.349)
    $ speak(NICOLE, "There's none. Cause no guy on planet earth is gonna pay for physical contact with a pretty girl without beating his shit raw as soon as she walks out the door.")
    $ setWait(60.349,63.685)
    $ speak(JECKA, "I can't control what they do after-- even if they do, like what's it matter?")
    show nicole sc6 surprised:
        leftcenterstage

    $ setWait(63.685,67.564)
    $ speak(NICOLE, "Wow you don't even care anymore. That money must be good I should get into this on my own.")
    show jecka sc9 angry:
        rightcenterstage
    $ setWait(67.564,69.274)
    $ speak(JECKA, "Care about fuckin' what anymore?")
    show nicole sc6 angry:
        leftcenterstage
    $ setWait(69.274,71.61)
    $ speak(NICOLE, "Care about being a whore.")

    show jecka sc9 sad:
        rightcenterstage

    $ setWait(71.61,72.819)
    $ speak(JECKA, "...N-no.")
    $ setWait(72.819,82.412)
    $ speak(NICOLE, "Yeah. Cause last I checked selling your body so a guy can get off makes you a trashy, half-finished tattoo sleeve, dimple pierced, fucking whore.")
    $ setWait(82.412,84.748)
    $ speak(JECKA, "N- Well-- So what?")
    show nicole sc6:
        leftcenterstage

    $ setWait(84.748,86.583)
    $ speak(NICOLE, "Do whatever you want, just a word.")

    show jecka sc9 angry:
        rightcenterstage

    $ setWait(86.583,89.836)
    $ speak(JECKA, "How bout you show some respect, Nicole. Cause I'm not a whore.")
    $ setWait(89.836,91.463)
    $ speak(JECKA, "I'm a sex worker!")
    show nicole sc6 angry:
        leftcenterstage

    $ setWait(91.463,93.09)
    $ speak(NICOLE, "Oh don't throw that government shit at me.")
    $ setWait(93.09,97.636)
    $ speak(JECKA, "I can use my body however I want, if that makes me a sex worker then I don't care.")
    $ setWait(97.636,100.055)
    $ speak(NICOLE, "Bitch you need to have sex to be a sex worker.")
    $ setWait(100.055,101.223)
    $ speak(JECKA, "Then what am I?")
    $ setWait(101.223,102.724)
    $ speak(NICOLE, "You're a human petting zoo.")
    $ setWait(102.724,105.602)
    $ speak(JECKA, "Ugh whatever! I don't need to take this I'm going to work!")
    $ setWait(105.602,106.937)
    $ speak(NICOLE, "What about your K-Mart cart?")
    $ setWait(106.937,112.025)
    $ speak(JECKA, "My job you have zero respect for could pay for all of this at a way fancier place...")
    show jecka sc9 angry:
        rightcenterstage
        xzoom -1
        linear 2 off_right
    $ setWait(112.025,113.402)
    $ speak(JECKA, "I'm going to Kohl's!")
    stop ambient fadeout 1.5
    jump scene_S0022

label scene_S0022:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jeffery day with Pause(2.924):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.924 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0022.mp3")
    play ambient "audio/Ambience/House_Ambience.mp3"
    $ csbox = True
    scene cut0022b
    $ setWait(2.924,6.928)
    $ speak(JEFFERY, "Mmm... I love these supple feet.")
    $ setWait(6.928,10.264)
    $ speak(JEFFERY, "You picked out really pretty nail polish today.")
    scene cut0022a
    $ setWait(10.264,12.808)
    $ speak(JECKA, "Oh uh, thanks.")
    $ setWait(12.808,17.855)
    $ speak(JEFFERY, "Girl's feet always feel good but it's even better when they're as pretty as yours.")
    scene cut0022b
    $ setWait(17.855,21.275)
    $ speak(JECKA, "Wow yeah, cool.")
    $ setWait(21.275,22.61)
    $ speak(JEFFERY, "Do you lactate?")
    scene cut0022c
    $ setWait(22.61,23.611)
    $ speak(JECKA, "Do I what?")
    $ setWait(23.611,27.865)
    $ speak(JEFFERY, "Y'know, lactate? Where milk comes out of your beautiful breasts.")
    scene cut0022e
    $ setWait(27.865,32.912)
    $ speak(JECKA, "Um, definitely not. I'm pretty sure you have to like have a baby to do that.")
    $ setWait(32.912,34.997)
    $ speak(JEFFERY, "Ohhh you're right.")
    $ setWait(34.997,38.876)
    $ speak(JEFFERY, "Well I hope you can be impregnated by an alpha male of your choosing.")
    scene cut0022c
    $ setWait(38.876,41.629)
    $ speak(JECKA, "Jeffery don't say that to girls, not even ugly ones.")
    $ setWait(41.629,46.425)
    $ speak(JEFFERY, "Sorry I know it's just you'd make such a cute mommy- mwah mwah mwah")
    scene cut0022d
    $ setWait(46.425,48.219)
    $ speak(JECKA, "Hey, hey, kissing's extra!")
    $ setWait(48.219,49.345)
    $ speak(JEFFERY, "Mwah-- how much extra??")
    $ setWait(49.345,50.262)
    $ speak(JECKA, "250!")
    $ setWait(50.262,53.14)
    $ speak(JEFFERY, "Ugh.. Maybe next week then.")
    scene cut0022e
    $ setWait(53.14,56.644)
    $ speak(JECKA, "You're such a fucking-- ...Yeah next week.")
    $ setWait(56.644,59.772)
    $ speak(JEFFERY, "Um, could you put one of your socks back on?")
    scene cut0022c
    $ setWait(59.772,61.649)
    $ speak(JECKA, "I thought you guys liked bare feet.")
    $ setWait(61.649,66.862)
    $ speak(JEFFERY, "We do, but sometimes a socked foot can be as cute as a bare foot.")
    scene cut0022a
    $ setWait(66.862,67.863)
    $ speak(JECKA, "Socks is extra.")
    $ setWait(67.863,69.615)
    $ speak(JEFFERY, "I thought bare feet were extra?")
    scene cut0022e
    $ setWait(69.615,72.034)
    $ speak(JECKA, "Anything that inconveniences me is extra.")
    $ setWait(72.034,74.245)
    $ speak(JEFFERY, "Oh alright...")
    $ setWait(74.245,76.288)
    $ speak(JEFFERY, "...You were my first kiss by the way.")
    $ setWait(76.288,79.041)
    $ speak(JECKA, "I've literally never kissed you and never will.")
    scene cut0022b
    $ setWait(79.041,80.251)
    $ speak(JECKA, "For under 10,000 dollars.")
    $ setWait(80.251,83.504)
    $ speak(JEFFERY, "No I meant just now, with your feet.")
    scene cut0022f
    $ setWait(83.504,86.549)
    $ speak(JECKA, "Oh yeah, that's pretty fuckin' sad.")
    $ setWait(86.549,88.968)
    $ speak(JEFFERY, "Could I tell you something really personal?")
    scene cut0022e
    $ setWait(88.968,94.724)
    $ speak(JECKA, "Well you kiss my feet and wanna suck milk out of my titties, not sure how much more personal we could get here.")
    $ setWait(94.724,97.685)
    $ speak(JEFFERY, "I... I'm in love with you.")
    scene cut0022a
    $ setWait(97.685,98.811)
    $ speak(JECKA, "I know...")
    $ setWait(98.811,104.775)
    $ speak(JEFFERY, "It's really hard but I try my best to avoid thinking about you while I...")
    $ setWait(104.775,106.861)
    $ speak(JEFFERY, "...use my hand.")
    scene cut0022b
    $ setWait(106.861,109.864)
    $ speak(JECKA, "I'm disappointed but not surprised.")
    $ setWait(109.864,111.824)
    $ speak(JEFFERY, "Is that extra too?")
    scene cut0022a
    $ setWait(111.824,113.534)
    $ speak(JECKA, "Is what extra?")
    $ setWait(113.534,118.372)
    $ speak(JEFFERY, "Thinking about you while I... Enjoy myself?")
    scene cut0022e
    $ setWait(118.372,120.499)
    $ speak(JECKA, "How would I even enforce that?")
    $ setWait(120.499,124.045)
    $ speak(JEFFERY, "The honor system, I swear I won't do it without paying you after.")
    scene cut0022f
    $ setWait(124.045,126.756)
    $ speak(JECKA, "Seriously? How's 50 bucks a load sound?")
    $ setWait(126.756,130.593)
    $ speak(JEFFERY, "It's a little steep but.. You're more than worth it.")
    scene cut0022a
    $ setWait(130.593,134.346)
    $ speak(JECKA, "Cool yeah just PayPal me, I got the text updates on my phone.")
    $ setWait(134.346,138.851)
    $ speak(JEFFERY, "Of course, you deserve it. You deserve every boy's money, Mommy.")
    $ setWait(138.851,141.479)
    $ speak(JEFFERY, "Now lemme dig into these feet some more- Mmm...")
    scene cut0022b
    $ setWait(141.479,143.939)
    $ speak(JECKA, "Just make sure you keep that job at the bookstore...")
    stop ambient fadeout 1.5
    jump scene_S0023

label scene_S0023:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0023.mp3")
    $ csbox = False
    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.1
    scene porch_jecka
    show jecka sc9 sad:
        off_right
        linear 3.6 leftmidstage

    $ setWait(0.037,3.374)
    $ speak(JECKA, "I just wanna watch wheelchair crash videos and fall asleep.")
    show burleday 1 smile:
        off_right
        linear 0.3 rightstage

    $ setWait(3.374,4.5)
    $ speak(BURLEDAY, "Hey! Hey...")
    show jecka sc9 surprised:
        leftmidstage
        linear 0.1 xalign .12
        linear 0.1 xalign .16
        linear 0.1 xalign .12
        xzoom -1
        linear 0.08 leftmidstage
    $ setWait(4.5,5.376)
    $ speak(JECKA, "Ho- What the fuck!")
    show burleday 1:
        rightstage
        linear 2 rightmidstage

    $ setWait(5.376,8.546)
    $ speak(BURLEDAY, "Wait no- uh Jecka, right?")
    show jecka sc9 angry:
        xzoom -1
        leftmidstage

    $ setWait(8.546,10.423)
    $ speak(JECKA, "Yeah what are you doing here??")
    $ setWait(10.423,16.721)
    $ speak(BURLEDAY, "I-I know this might be an odd time but were you the same Jecka on the forums?")
    $ setWait(16.721,18.264)
    $ speak(JECKA, "Forums? What?")
    $ setWait(18.264,19.598)
    $ speak(BURLEDAY, "Yeah the forums.")
    $ setWait(19.598,21.1)
    $ speak(JECKA, "Fuckin' what forums?")
    $ setWait(21.1,23.728)
    $ speak(BURLEDAY, "FeetMeet.com!")
    show jecka sc9 surprised:
        xzoom -1
        leftmidstage

    $ setWait(23.728,25.062)
    $ speak(JECKA, "...Wait so.")
    $ setWait(25.062,28.232)
    $ speak(BURLEDAY, "You're still doing the foot services, right?")
    $ setWait(28.232,29.483)
    $ speak(JECKA, "How'd you get my address?")
    $ setWait(29.483,34.071)
    $ speak(BURLEDAY, "Well your number was in the listing I just used the internet to trace it back here.")
    $ setWait(34.071,35.823)
    $ speak(JECKA, "Oh god...")
    $ setWait(35.823,38.993)
    $ speak(BURLEDAY, "But yeah how much to kiss your toes? $200 like the stepping?")
    show jecka sc9 angry:
        xzoom -1
        leftmidstage

    $ setWait(38.993,40.661)
    $ speak(JECKA, "Are you actually crazy!?")
    $ setWait(40.661,42.288)
    $ speak(BURLEDAY, "Ah sorry was that a lowball?")
    $ setWait(42.288,46)
    $ speak(JECKA, "No- You're in front of my house at midnight and 200's way too low!")
    $ setWait(46,47.668)
    $ speak(BURLEDAY, "Eh it was worth a shot.")
    $ setWait(47.668,49.67)
    $ speak(JECKA, "Get the fuck out of here before I call the cops!")
    $ setWait(49.67,51.714)
    $ speak(BURLEDAY, "O-Okay okay fine!")
    $ setWait(51.714,52.715)
    $ speak(BURLEDAY, "$300.")
    $ setWait(52.715,54.091)
    $ speak(JECKA, "What? No- Leave!")
    $ setWait(54.091,56.218)
    $ speak(BURLEDAY, "Okay 400, 400 to kiss your toes?")
    $ setWait(56.218,58.304)
    $ speak(JECKA, "I'm not haggling! Just go home!")
    $ setWait(58.304,60.598)
    $ speak(BURLEDAY, "Okay screw it- 800, final offer.")
    show jecka sc9 sad:
        leftmidstage
        xzoom -1
        pause 1.15
        xzoom 1

    $ setWait(60.598,62.85)
    $ speak(JECKA, "Eight? No- ugh...")
    show jecka sc9 sad:
        leftmidstage
        xzoom -1
    $ setWait(62.85,63.809)
    $ speak(JECKA, "...For how long?")
    $ setWait(63.809,64.56)
    $ speak(BURLEDAY, "Half hour.")

    show jecka sc9 angry:
        leftmidstage
        xzoom -1

    $ setWait(64.56,65.394)
    $ speak(JECKA, "20 minutes.")

    show burleday 1 smile:
        rightmidstage

    $ setWait(65.394,67.646)
    $ speak(BURLEDAY, "Okay fine, can we do it inside your house?")
    $ setWait(67.646,69.106)
    $ speak(JECKA, "Fuck no, where's your car?")
    show burleday 1 smile:
        rightmidstage
        pause 0.7
        xzoom -1
        pause 1.7
        xzoom 1
    $ setWait(69.106,74.195)
    $ speak(BURLEDAY, "Oh it's that Chevy Caprice over there, LTZ.")
    show jecka sc9 angry:
        leftmidstage
        xzoom -1
        linear 1.3 centerstage

    $ setWait(74.195,76.113)
    $ speak(JECKA, "Whatever the hell that means, let's go.")
    $ setWait(76.113,78.991)
    $ speak(BURLEDAY, "Wait, can I throw in an extra hundred for you to roleplay?")
    $ setWait(78.991,80.618)
    $ speak(JECKA, "Roleplay what?")
    $ setWait(80.618,87.208)
    $ speak(BURLEDAY, "Remember the girl in the 1984 Apple commercial that throws the hammer through the screen?")
    show jecka sc9:
        xzoom -1
        centerstage

    $ setWait(87.208,90.294)
    $ speak(JECKA, "Uh.. maybe it was on Family Guy once.")
    $ setWait(90.294,91.67)
    $ speak(BURLEDAY, "Can you be her?")
    $ setWait(91.67,94.673)
    $ speak(JECKA, "How would you work that into what.. we're doing.")
    $ setWait(94.673,100.054)
    $ speak(BURLEDAY, "Oh y'know like I'm thanking you for throwing the hammer. Is that weird?")
    $ setWait(100.054,101.305)
    $ speak(JECKA, "What do you think?")
    $ setWait(101.305,105.392)
    $ speak(BURLEDAY, "Different. Think Different, you remember that? Were you alive for that?")
    $ setWait(105.392,109.605)
    $ speak(JECKA, "If I said no would you feel like a pedophile or keep going through with this?")
    show burleday 1:
        rightmidstage
        pause 2.8
        xzoom -1
        linear 1.4 off_right

    show jecka sc9:
        centerstage
        xzoom -1
        pause 3.4
        linear 2.4 off_right

    $ setWait(109.605,114.485)
    $ speak(BURLEDAY, "Let's uh... Let's get in the LTZ.")
    stop ambient fadeout 2
    jump scene_S0024

label scene_S0024:
    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.8 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show bookstore ext with Pause(2.883):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.883 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0024.mp3")
    scene bookstore
    play ambient "audio/Ambience/Library_Ambience.mp3"
    show ari sc1:
        off_right
        linear 4 leftcenterstage
        xzoom -1

    show jecka sc10:
        off_farright
        linear 4.15 rightcenterstage

    $ setWait(2.883,7.763)
    $ speak(ARI, "But yeah I'm surprised you called, I thought you'd only hang out with Nicole after we graduated.")
    $ setWait(7.763,10.307)
    $ speak(JECKA, "Uh it's complicated.")
    $ setWait(10.307,12.059)
    $ speak(ARI, "Complicated how?")
    $ setWait(12.059,14.144)
    $ speak(JECKA, "Like the Avril Lavigne song.")
    $ setWait(14.144,15.395)
    $ speak(ARI, "So you were dating?")

    $ setWait(15.395,18.69)
    $ speak(JECKA, "No like the song's called-- whatever.")
    show ari sc1 shy:
        leftcenterstage
        xzoom -1

    $ setWait(18.69,20.818)
    $ speak(ARI, "Is this technically dating?")
    $ setWait(20.818,23.862)
    $ speak(JECKA, "I don't know, what's the difference between dating and hanging out?")
    $ setWait(23.862,26.615)
    $ speak(ARI, "Like uh... like kissing?")
    $ setWait(26.615,27.783)
    $ speak(JECKA, "Do you wanna kiss me?")
    $ setWait(27.783,30.035)
    $ speak(ARI, "Absolutely fucking kinda.")
    $ setWait(30.035,31.286)
    $ speak(JECKA, "Tell me I'm pretty first.")
    show ari sc1:
        leftcenterstage
        xzoom -1

    $ setWait(31.286,32.162)
    $ speak(ARI, "You're pretty.")
    show jecka sc10 angry:
        rightcenterstage

    $ setWait(32.162,34.498)
    $ speak(JECKA, "What's pretty about me?")
    show ari sc1 shy:
        leftcenterstage
        xzoom -1
    $ setWait(34.498,39.753)
    $ speak(ARI, "Um, how you're never able to wash your body glitter all the way off.")
    show jecka sc10 smile:
        rightcenterstage
        pause 0.65
        linear 1 centerstage
    $ setWait(39.753,41.255)
    $ speak(JECKA, "Okay slut, kiss me.")
    hide jecka sc10 smile
    hide ari sc1 shy
    $ csbox = True
    scene cut0024a
    $ setWait(41.255,42.923)
    $ speak(JECKA, "Mwwwwah.")
    scene cut0024b
    $ setWait(42.923,45.175)
    $ speak(ARI, "Why'd you take a picture of us with your phone?")
    $ setWait(45.175,47.302)
    $ speak(JECKA, "I'm gonna send this to guys I like.")
    $ setWait(47.302,52.641)
    $ speak(ARI, "Oh... So I heard you got fired from the chrome diner.")
    $ setWait(52.641,55.144)
    $ speak(JECKA, "Yeah but it's cool, my new job's way better.")
    $ setWait(55.144,56.687)
    $ speak(ARI, "Where do you work now?")
    scene cut0024c
    $ setWait(56.687,59.481)
    $ speak(JECKA, "Oh... Uh...")
    $ setWait(59.481,60.691)
    $ speak(JECKA, "Foot Locker?")
    $ setWait(60.691,64.194)
    $ speak(ARI, "Really? I work at Finish Line, how's Foot Locker though?")
    $ setWait(64.194,71.201)
    $ speak(JECKA, "Shit um, the customers just love shoes and socks and.. Feet.")
    $ setWait(71.201,74.413)
    $ speak(ARI, "Yeah, Finish Line's easier to work at cause customers don't come in.")
    $ setWait(74.413,77.291)
    $ speak(JECKA, "I'm pretty sure my customers come after.")
    $ setWait(77.291,79.626)
    $ speak(ARI, "Come.. After.. What?")
    $ setWait(79.626,82.671)
    $ speak(JECKA, "O-Oh like- come after the new Jordans drop.")
    $ setWait(82.671,87.384)
    $ speak(ARI, "Yeah that's the only time my store's busy. Do they get really mean at you on release days?")
    $ setWait(87.384,89.219)
    $ speak(JECKA, "Uh well...")
    show text_jefferypay
    $ setWait(89.219,91.054)
    $ speak(JECKA, "...")
    $ setWait(91.054,94.016)
    $ speak(JECKA, "No they're kinda always in love with me.")
    hide text_jefferypay
    $ setWait(94.016,95.225)
    $ speak(ARI, "In love with you?")
    $ setWait(95.225,99.104)
    $ speak(JECKA, "Oh I just meant they're really nice to me, but it gets creepy sometimes.")
    $ setWait(99.104,104.902)
    $ speak(ARI, "Could be worse, all my co-workers are like homophobic Christian whatever. Is Foot Locker like that too?")
    $ setWait(104.902,105.944)
    $ speak(JECKA, "Wouldn't surprise me.")
    $ setWait(105.944,108.53)
    $ speak(ARI, "You too? Oh my god, we should quit!")
    $ setWait(108.53,110.866)
    $ speak(JECKA, "You can quit, I kinda need this money though.")
    $ setWait(110.866,113.577)
    $ speak(ARI, "Should gay people really put up with this just for the money?")
    $ setWait(113.577,115.245)
    $ speak(JECKA, "I'm not the right person to ask.")
    $ setWait(115.245,115.996)
    $ speak(ARI, "Why not?")
    $ setWait(115.996,120.25)
    $ speak(JECKA, "Cause Ari you're like actually gay, I'm attention-seeking gay at best.")
    $ setWait(120.25,121.752)
    $ speak(ARI, "Is it really that different?")
    $ setWait(121.752,128.967)
    $ speak(JECKA, "Well if they're homophobic at my job I'll live. If they're homophobic at yours you have to pretend 24/7. So you tell me.")
    $ setWait(128.967,131.678)
    $ speak(ARI, "You're saying you don't think about killing yourself every day?")
    $ setWait(131.678,134.64)
    $ speak(JECKA, "I only think about killing myself when Chipotle gets my order wrong.")
    $ setWait(134.64,137.267)
    $ speak(ARI, "They make it in front of you, how do they get it wrong?")
    $ setWait(137.267,138.977)
    $ speak(JECKA, "Oh my god exactly!")
    stop ambient fadeout 1.5
    jump scene_S0025

label scene_S0025:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0025.mp3")
    $ csbox = False
    play ambient "audio/Ambience/HardwareStore_Ambience.mp3" fadein 1
    scene hardwarestore
    show jecka sc11:
        xzoom -1
        leftstage
    $ setWait(0.035,3.998)
    $ speak(JECKA, "Okay what'll get the stench of thousand-island and blood off my feet.")
    $ setWait(3.998,6.584)
    $ speak(JECKA, "Which of these are gonna make it burn? Should I want it to burn?")
    show kylar sc2 smile:
        xzoom -1
        off_left
        linear 1.2 leftstage
    $ setWait(6.584,7.209)
    $ speak(KYLAR, "Oh hey.")
    show jecka sc11 surprised:
        xzoom 1
        leftstage
        linear 0.4 rightcenterstage
    $ setWait(7.209,8.961)
    $ speak(JECKA, "Whoa shit! What?")
    show kylar sc2:
        leftstage
        xzoom -1
        linear 1 leftmidstage

    $ setWait(8.961,11.881)
    $ speak(KYLAR, "The fuck's the matter with you? You just realize Obama's black?")
    show jecka sc11 sad:
        rightcenterstage
        xzoom 1

    $ setWait(11.881,18.721)
    $ speak(JECKA, "Wow that was racist, no it's just uh.. work. I have like a hard trigger response when men talk to me now.")
    $ setWait(18.721,19.93)
    $ speak(KYLAR, "What are you a stripper?")
    show jecka sc11 angry:
        rightcenterstage
    $ setWait(19.93,20.681)
    $ speak(JECKA, "No!")
    $ setWait(20.681,22.516)
    $ speak(KYLAR, "Oh, at least you got that going for ya.")
    $ setWait(22.516,23.976)
    $ speak(JECKA, "What's that supposed to mean?")
    $ setWait(23.976,25.352)
    $ speak(KYLAR, "At least you're not a whore.")
    show text_jefferypay onlayer screens
    $ setWait(25.352,26.228)
    $ speak(JECKA, "...")
    hide text_jefferypay onlayer screens
    show jecka sc11 angry:
        rightcenterstage
    $ setWait(26.228,31.15)
    $ speak(JECKA, "Do you not like whores? Can't afford 'em after you blew your money on Muscle Milk and Carey Hart tickets??")
    show kylar sc2 angry:
        leftmidstage

    $ setWait(31.15,35.821)
    $ speak(KYLAR, "Dude I only saw him at like 3 motocross tours. And I don't pay for bitches, I'm above that.")
    $ setWait(35.821,37.198)
    $ speak(JECKA, "Oh Mister Morality?")
    $ setWait(37.198,39.909)
    $ speak(KYLAR, "More moral than you, ya fuckin' dimestore dipshit.")
    $ setWait(39.909,44.038)
    $ speak(JECKA, "Is that why you fuck girls while they're unconscious? You're a regular Mr. Rogers.")
    $ setWait(44.038,45.873)
    $ speak(KYLAR, "What are you even talking about?")
    $ setWait(45.873,48)
    $ speak(JECKA, "What everyone else at school was talking about.")
    $ setWait(48,50.795)
    $ speak(KYLAR, "Bro you are going full fuckin' titsa-phrenic right now!")
    $ setWait(50.795,53.839)
    $ speak(JECKA, "Sorry if I think paying for pussy's better than stealing it!")
    $ setWait(53.839,56.842)
    $ speak(KYLAR, "Is this a wall of PMS? What're you even trying to say??")
    $ setWait(56.842,60.304)
    $ speak(JECKA, "I'm saying you look, sound, and spend your money like a rapist.")
    $ setWait(60.304,62.807)
    $ speak(KYLAR, "What's with all these false accusations? Go away!")
    $ setWait(62.807,65.684)
    $ speak(JECKA, "They're not false, they're accusations on layaway!")
    show kylar sc2 angry:
        leftmidstage
        xzoom -1
        pause 1.2
        xzoom 1
        linear 2 off_left

    $ setWait(65.684,69.772)
    $ speak(KYLAR, "Aw whatever! I'm gonna go beat up a deaf person.")
    $ setWait(69.772,72.149)
    show text_jefferypay onlayer screens
    $ speak(JECKA, "...")
    hide text_jefferypay onlayer screens
    show jecka sc11 sad:
        rightcenterstage

    $ setWait(72.149,74.026)
    $ speak(JECKA, "I need some help...")
    stop ambient fadeout 1.5
    jump scene_S0026

label scene_S0026:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0026.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 1
    show ames 1:
        rightmidstage

    show jecka sc12:
        leftstage
        xzoom -1
        linear 3 centerstage

    $ setWait(0.041,2.668)
    $ speak(AMES, "So what brings you to community youth counseling?")
    $ setWait(2.668,4.92)
    $ speak(JECKA, "Honestly what hasn't brought me here.")
    $ setWait(4.92,6.839)
    $ speak(AMES, "Well we need to start somewhere.")
    show jecka sc12 sad:
        xzoom -1
        centerstage
    $ setWait(6.839,8.883)
    $ speak(JECKA, "Actually, how much does this cost?")
    show ames 1 smile:
        rightmidstage

    $ setWait(8.883,11.844)
    $ speak(AMES, "Nothing at all, it's covered by the county.")
    $ setWait(11.844,14.472)
    $ speak(JECKA, "Oh okay...")
    $ setWait(14.472,18.476)
    $ speak(JECKA, "...And if I need a hug, are hugs extra?")
    show ames 1:
        rightmidstage

    $ setWait(18.476,22.063)
    $ speak(AMES, "Extra what? As in charging for a hug? No.")
    $ setWait(22.063,26.067)
    $ speak(JECKA, "Oh right, yeah.. Okay let's start.")
    $ setWait(26.067,28.819)
    $ speak(AMES, "So how's everything going at home?")
    show jecka sc12:
        xzoom -1
        centerstage
    $ setWait(28.819,31.906)
    $ speak(JECKA, "Uh my parents got divorced like a month ago.")
    $ setWait(31.906,33.991)
    $ speak(AMES, "Divorce can be very hard.")
    $ setWait(33.991,38.537)
    $ speak(JECKA, "Well no I'm white I'll get over it, but it's just my Dad mainly.")
    $ setWait(38.537,40.081)
    $ speak(AMES, "Is he taking it really hard?")
    show jecka sc12 sad:
        xzoom -1
        centerstage
    $ setWait(40.081,44.126)
    $ speak(JECKA, "He's taking it out on me. I get threatened every day of my life.")
    $ setWait(44.126,48.506)
    $ speak(AMES, "Threatened how exactly? If you don't mind sharing.")
    $ setWait(48.506,54.929)
    $ speak(JECKA, "He said he'll smack the pretty off my face and sell me to Borneo for a sack of rice.")
    $ setWait(54.929,57.223)
    $ speak(AMES, "Aw that's a very 70's threat.")
    $ setWait(57.223,65.731)
    $ speak(JECKA, "Yeah and so I need to help out with the bills or.. He's gonna get mad and have a heart attack from some chronic heart thing he's got.")
    $ setWait(65.731,71.112)
    $ speak(AMES, "I see... Anything else with him? Other concerns?")
    show jecka sc12:
        xzoom -1
        centerstage
    $ setWait(71.112,72.905)
    $ speak(JECKA, "He always wants to fuck my friends.")
    show ames 1 sad:
        rightmidstage

    $ setWait(72.905,74.115)
    $ speak(AMES, "H-He what?")
    $ setWait(74.115,85)
    $ speak(JECKA, "Well I'm basically kinda gorgeous so naturally my friends would be too, but he's not related to them so it's a green light in his mind.")
    $ setWait(85,89.171)
    $ speak(AMES, "But your father doesn't want... With you, right?")
    $ setWait(89.171,94.385)
    $ speak(JECKA, "No no my Dad doesn't wanna fuck me. He doesn't even like hugging me, so.. silver-lining.")
    show ames 1:
        rightmidstage

    $ setWait(94.385,100.307)
    $ speak(AMES, "Right, so then it seems the issues at home are stemming mainly from the bills?")
    $ setWait(100.307,102.059)
    $ speak(JECKA, "Yeah I guess you could say that.")
    $ setWait(102.059,105.354)
    $ speak(AMES, "Have you taken any steps toward a job? Had a job?")
    $ setWait(105.354,110.276)
    $ speak(JECKA, "Right so, first I got a job at the diner. My friend put in a good word for me.")
    $ setWait(110.276,113.404)
    $ speak(AMES, "That's good, anything else about this friend?")
    $ setWait(113.404,119.493)
    $ speak(JECKA, "Uh I guess she's not actually actually my friend. She's super fucked up on drugs, but she's cool though.")
    $ setWait(119.493,122.163)
    $ speak(AMES, "And are you on drugs at all?")
    show jecka sc12 smile:
        xzoom -1
        centerstage
    $ setWait(122.163,124.623)
    $ speak(JECKA, "Heh, are we on the floor?")
    $ setWait(124.623,129.003)
    $ speak(AMES, "Now I'd take it the diner didn't work out? What was next?")
    show jecka sc12:
        xzoom -1
        centerstage
    $ setWait(129.003,137.553)
    $ speak(JECKA, "Yeah so it didn't work out because I was discovering my new job, which made me late for the first job.")
    $ setWait(137.553,139.68)
    $ speak(AMES, "Do you like your new job?")
    $ setWait(139.68,142.975)
    $ speak(JECKA, "Um... I like the pay.")
    $ setWait(142.975,144.81)
    $ speak(AMES, "And what is it?")
    $ setWait(144.81,147.73)
    $ speak(JECKA, "Like... What do I do for it?")
    $ setWait(147.73,148.939)
    $ speak(AMES, "Uh huh.")
    show jecka sc12 sad:
        xzoom -1
        centerstage
    $ setWait(148.939,153.569)
    $ speak(JECKA, "And you can't.. tell anybody about what I do, right?")
    $ setWait(153.569,160.743)
    $ speak(AMES, "It's sanctioned therapy, everything here is confidential. So what do you do for this job?")
    $ setWait(160.743,166.29)
    $ speak(JECKA, "I-I let guys touch my feet for money.")
    $ setWait(166.29,167.666)
    $ speak(AMES, "Excuse me?")
    $ setWait(167.666,175.216)
    $ speak(JECKA, "N-no it's like... They give me a lot of money to stand on them, and kiss my toes, and be nice when I talk to them!")
    $ setWait(175.216,176.634)
    $ speak(AMES, "A-alright.")
    $ setWait(176.634,181.555)
    $ speak(JECKA, "At first I only did it a little but then they just kept coming and coming and coming, not on me but to me--")
    $ setWait(181.555,189.313)
    $ speak(JECKA, "Like one guy just gives me 50 dollars every time he jerks off to me! And they all have my number and know where I live and just keep offering me more and more money to where I can't say no!")
    show ames 1 sad:
        rightmidstage
    $ setWait(189.313,190.898)
    $ speak(AMES, "Why can't you say no??")
    $ setWait(190.898,195.11)
    $ speak(JECKA, "Cause the money was so good, I got used to spending, and all the bills my Dad needs me to pay!")
    $ setWait(195.11,199.281)
    $ speak(JECKA, "And if I don't make enough money it's gonna stress him out, and the stress'll give 'em a heart attack and die...")
    $ setWait(199.281,208.999)
    $ speak(JECKA, "...and if he dies I won't afford the mortgage and I'm gonna end up living on the street withdrawing from adderall while losers suck on my toes!!")
    $ setWait(208.999,213.087)
    $ speak(AMES, "I can see why it'd be hard to talk about this with someone.")
    $ setWait(213.087,219.593)
    $ speak(JECKA, "Nobody wants me for me! Not even my best friend wants me cause I'm a foot whore!")
    $ setWait(219.593,223.389)
    $ speak(AMES, "This... Certainly seems like a lot.")
    show ames 1:
        rightmidstage

    $ setWait(223.389,229.144)
    $ speak(AMES, "How much are these men paying you to make it so necessary to stay?")
    $ setWait(229.144,231.772)
    $ speak(JECKA, "It starts at like $200.")
    $ setWait(231.772,237.57)
    $ speak(AMES, "No I meant for a regular job to not be an option, what's the monthly income?")
    $ setWait(237.57,240.03)
    $ speak(JECKA, "Oh probably like...")
    $ setWait(240.03,242.408)
    $ speak(JECKA, "Like 6 or 7 thousand a month.")
    show ames 1 angry:
        rightmidstage
    $ setWait(242.408,243.242)
    $ speak(AMES, "What??")
    $ setWait(243.242,244.285)
    $ speak(JECKA, "Is that bad?")

    $ setWait(244.285,247.621)
    $ speak(AMES, "That's twice what I get paid! Why'd you come to free counseling??")
    $ setWait(247.621,250.04)
    $ speak(JECKA, "Cause I didn't know where else to turn--")
    $ setWait(250.04,252.334)
    $ speak(AMES, "Oh shut the fuck up, you could afford to pay it!")
    show ames 1 angry:
        rightmidstage
        linear 3 off_left

    show jecka sc12 sad:
        centerstage
        xzoom -1
        pause 1.9
        xzoom 1
    $ setWait(252.334,256.88)
    $ speak(AMES, "This session is over. 80,000 a year, unbelievable.")
    $ setWait(256.88,259.55)
    $ speak(JECKA, "But... But...")
    show jecka sc12 sad:
        xzoom 1
        centerstage
        linear 5 leftstage

    $ setWait(259.55,263.512)
    $ speak(JECKA, "He makes me pay for the Food Network.")
    stop ambient fadeout 1.5
    jump scene_S0027

label scene_S0027:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0027.mp3")
    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene porch_jecka
    show jecka sc12 sad:
        off_right
        linear 3.8 leftcenterstage

    $ setWait(0.076,3.496)
    $ speak(JECKA, "I want an eating disorder to die hotter.")
    show text_fanclub onlayer screens
    $ setWait(3.496,8.376)
    $ speak(JECKA, "Ryan's gonna be in town? I guess that's cool...")
    hide text_fanclub onlayer screens
    $ setWait(8.376,10.17)
    $ speak(JECKA, "...Fuck it, who cares anymore?")
    show kyle sc1:
        off_right
        pause 1
        linear 0.7 rightcenterstage
    $ setWait(10.17,11.171)
    $ speak(KYLE, "Hey hey wait!")
    show jecka sc12 surprised:
        leftcenterstage
        linear 0.1 xalign 0.35
        linear 0.1 xalign 0.39
        linear 0.1 xalign 0.35
        xzoom -1
        linear 0.07 leftcenterstage

    $ setWait(11.171,12.255)
    $ speak(JECKA, "Oh what the fuck??")
    $ setWait(12.255,16.092)
    $ speak(KYLE, "Hey Jecka, could you come with me to the Caribou Coffee ladies room?")

    show jecka sc12 angry:
        leftcenterstage
        xzoom -1

    $ setWait(16.092,18.762)
    $ speak(JECKA, "Kyle go the fuck home! It's 11 at night!")
    $ setWait(18.762,21.973)
    $ speak(KYLE, "Oh yeah I guess Adult Swim just started...")
    $ setWait(21.973,25.477)
    $ speak(KYLE, "You wanna let me inside to watch Adult Swim with you?")
    $ setWait(25.477,29.773)
    $ speak(JECKA, "Sorry I have better things to do than watching snarky text play over hip-hop for white guys.")
    show burleday 1 smile:
        off_right
        linear 0.7 rightmidstage
    $ setWait(29.773,32.734)
    $ speak(BURLEDAY, "Aw great you're still out here! Nice shoes by the way.")
    show kyle sc1 sad:
        rightcenterstage
        xzoom -1
    $ setWait(32.734,35.07)
    $ speak(KYLE, "Mr. Burleday, you know about Jecka too?")
    $ setWait(35.07,37.739)
    $ speak(BURLEDAY, "Any dedicated FeetMeeter knows Jecka.")
    $ setWait(37.739,42.452)
    $ speak(BURLEDAY, "So uh, you remember the wife in the Sears air conditioning commercial?")
    $ setWait(42.452,43.036)
    $ speak(JECKA, "No!!")
    show kyle sc1 angry:
        rightcenterstage
        xzoom -1

    $ setWait(43.036,44.579)
    $ speak(KYLE, "Hey don't upset her like that.")
    show burleday 1 sad:
        rightmidstage
    $ setWait(44.579,46.998)
    $ speak(BURLEDAY, "Oh no no I didn't mean any offense by it.")
    $ setWait(46.998,49)
    $ speak(KYLE, "Just read the room better next time.")
    $ setWait(49,50.877)
    $ speak(JECKA, "What fuckin' room, we're outside.")
    show lorre 1:
        xzoom -1
        off_left
        linear 0.7 leftmidstage

    $ setWait(50.877,51.711)
    $ speak(LORRE, "It's now or never!")
    show jecka sc12 surprised:
        leftcenterstage
        xzoom 1

    show kyle sc1:
        rightcenterstage
        xzoom 1

    show burleday 1:
        rightmidstage
        xzoom 1
    $ setWait(51.711,52.17)
    $ speak(JECKA, "Wha??")
    $ setWait(52.17,56.007)
    $ speak(LORRE, "Hey heard great things about you, how much to step on me? Is it still 200?")
    show jecka sc12 angry:
        leftcenterstage
        xzoom 1
    $ setWait(56.007,57.467)
    $ speak(JECKA, "Fuck off go away!")
    show kyle sc1 angry:
        rightcenterstage

    $ setWait(57.467,60.387)
    $ speak(KYLE, "Show some respect, creep! At least offer 250.")
    show jeffery sc2 smile:
        off_right
        linear 0.5 rightstage

    $ setWait(60.387,63.098)
    $ speak(JEFFERY, "Oh hey, Jecka! Glad I found ya out here.")
    show jecka sc12 sad:
        leftcenterstage
        xzoom -1
    $ setWait(63.098,66.351)
    $ speak(JECKA, "What could you possibly want-- actually don't tell me.")
    $ setWait(66.351,73.733)
    $ speak(JEFFERY, "I forgot the password to my Paypal account so I came to hand deliver the money in cash for our.. remote-arrangement.")
    show jecka sc12:
        leftcenterstage
        xzoom -1
    $ setWait(73.733,77.404)
    $ speak(JECKA, "\"Came to hand\"-- Wait there's 200 here, I thought it was 50 a pop?")
    show jeffery sc2 blush:
        rightstage

    $ setWait(77.404,78.905)
    $ speak(JEFFERY, "Yeah um...")
    $ setWait(78.905,80.865)
    $ speak(JEFFERY, "I did it four times today.")
    $ setWait(80.865,86.579)
    $ speak(JEFFERY, "Miss Teen USA was on and Miss Washington looked a lot like you-- but you're still prettier, don't worry.")

    show kyle sc1:
        rightcenterstage
        xzoom -1

    $ setWait(86.579,88.206)
    $ speak(KYLE, "Remote arrangement?")
    show jeffery sc2:
        rightstage
    $ setWait(88.206,94.17)
    $ speak(JEFFERY, "Oh see whenever I relieve myself thinking about Jecka I have to pay her $50.")
    show kyle sc1 sad:
        rightcenterstage
        xzoom -1
        pause 0.5
        xzoom 1

    $ setWait(94.17,97.048)
    $ speak(KYLE, "Really? I didn't know we had to do that, I'm sorry.")
    $ setWait(97.048,98.216)
    $ speak(JECKA, "I am too now.")
    show kyle sc1 smile:
        rightcenterstage
        pause 0.6
        xzoom -1
        linear 3 off_right

    $ setWait(98.216,101.094)
    $ speak(KYLE, "Lemme go to the ATM and get you $1400 dollars.")
    show jecka sc12:
        leftcenterstage
        xzoom -1
    $ setWait(101.094,103.388)
    $ speak(JECKA, "Uh- Alright.")
    show jecka sc12 surprised:
        leftcenterstage
        pause 0.3
        xzoom 1
    $ setWait(103.388,105.015)
    $ speak(LORRE, "So 250 then?")
    show burleday 1 angry:
        rightmidstage
        linear 1 rightcenterstage

    show jecka sc12 surprised:
        leftcenterstage
        pause 0.3
        xzoom -1

    $ setWait(105.015,106.85)
    $ speak(BURLEDAY, "I was here first! 300!")
    show lorre 1 yell:
        xzoom -1
        leftmidstage

    show jecka sc12 surprised:
        leftcenterstage
        pause 0.3
        xzoom 1

    $ setWait(106.85,108.476)
    $ speak(LORRE, "I hid in the bushes first!")
    show jeffery sc2 angry:
        rightstage
        linear 1 rightmidstage

    show jecka sc12 surprised:
        leftcenterstage
        pause 0.3
        xzoom -1

    $ setWait(108.476,109.853)
    $ speak(JEFFERY, "I was in love with her first!!")

    show jecka sc12 angry:
        leftcenterstage
        xzoom 1
        linear 0.8 off_left

    show lorre 1 freakout:
        leftmidstage
        pause 0.7
        xzoom 1
    $ setWait(109.853,112.981)
    $ speak(JECKA, "Aw fuck just go away!!")
    show jeffery sc2 angry:
        rightmidstage
        linear 3 leftcenterstage


    $ setWait(112.981,114.816)
    $ speak(JEFFERY, "Oh look what you did to her...")
    stop ambient fadeout 1.5
    jump scene_S0028

label scene_S0028:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.3
    $ setVoiceTrack("audio/Scenes/0028.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3" fadein 1
    scene livingroom jecka night

    show jecka sc12 sad:
        xzoom -1
        off_left
        linear 2 leftcenterstage

    $ setWait(0.082,2.918)
    $ speak(JECKA, "Okay I gotta call the police for real this time.")
    show jecka sc12 angry:
        leftcenterstage
        xzoom -1

    $ setWait(2.918,4.753)
    $ speak(JECKA, "Wait- shit my phone's dead!")
    show jecka sc12 sad:
        leftcenterstage
        xzoom -1
        linear 3 rightcenterstage
    $ setWait(4.753,7.548)
    $ speak(JECKA, "Where's the cordless? Dad!?")
    $ setWait(7.548,11.927)
    $ speak(DAD, "Ohhhhh... Mmmmmm...")
    show jecka sc12 sad:
        rightcenterstage
        xzoom -1
        pause 1.3 xzoom 1

    $ setWait(11.927,14.429)
    $ speak(JECKA, "No... Did he see the crowd outside?")
    $ setWait(14.429,18.1)
    $ speak(DAD, "Uggghhhh...")
    show jecka sc12 surprised:
        rightcenterstage

    $ setWait(18.1,19.685)
    $ speak(JECKA, "They gave him a heart attack...")
    show jecka sc12 sad:
        xzoom -1
        rightcenterstage
        pause 1.1
        linear 1 off_right

    $ setWait(19.685,21.271)
    $ speak(JECKA, "Dad!? Dad it's gonna be okay!!")
    stop ambient fadeout 1.5
    jump scene_S0029

label scene_S0029:
    show black onlayer screens with Pause(3):
        alpha 0.2
        linear 1.7 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0029.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3" fadein 1.4
    $ csbox = True

    scene cut0029a
    $ setWait(0.124,3.169)
    $ speak(DAD, "Ooohhh...")
    $ setWait(3.169,5.838)
    $ speak(JECKA, "I'm coming in, don't freak out.")
    $ setWait(5.838,6.798)
    $ speak(DAD, "Agh...")
    scene cut0029b
    $ setWait(6.798,9.759)
    $ speak(JECKA, "Dad are you...")
    $ setWait(9.759,10.593)
    $ speak(JECKA, "Wait...")
    scene cut0029c
    $ setWait(10.593,11.594)
    $ speak(JECKA, "Nicole??")
    $ setWait(11.594,14.138)
    $ speak(NICOLE, "Oh no, she caught us.")
    $ setWait(14.138,16.265)
    $ speak(JECKA, "Why the fuck are your toes in his mouth!")
    $ setWait(16.265,17.809)
    $ speak(NICOLE, "Don't act like you don't know.")
    $ setWait(17.809,19.143)
    $ speak(DAD, "Sweetheart, I can explain-")
    scene cut0029d
    $ setWait(19.143,21.896)
    $ speak(NICOLE, "Shut your flavored seltzer ass up and feel those feet.")
    $ setWait(21.896,22.814)
    $ speak(DAD, "Oh god...")
    $ setWait(22.814,26.025)
    $ speak(JECKA, "Nicole, with my Dad?? What the fuck is wrong with you!?")
    scene cut0029c
    $ setWait(26.025,28.361)
    $ speak(NICOLE, "I'm just a broke bitch with no limits.")
    $ setWait(28.361,30.613)
    $ speak(JECKA, "I'm gonna fucking... Ugh...")
    scene cut0029d
    $ setWait(30.613,35.118)
    $ speak(NICOLE, "What?? I needed the money, wasn't that your excuse?")
    scene cut0029e
    stop ambient fadeout 3
    $ setWait(35.118,37.903)
    $ speak(JECKA, "I'm so fuckin' done with this...")
    jump end_S0030

label end_S0030:

    show black onlayer screens with Pause(3.4):
        alpha 0.0
        linear 2.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    scene black

    if "end_0030" not in persistent.endings:
        $ persistent.endings.append("end_0030")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    $ renpy.movie_cutscene("cs0030.webm")

    return

label scene_S0031:
    $ setVoiceTrack("audio/Scenes/0031.mp3")
    scene kmart
    show jecka sc9 angry:
        rightcenterstage

    show nicole sc6 smile:
        leftcenterstage

    $ setWait(0.08,2.165)
    $ speak(JECKA, "Alright fine just don't fuck it up for me!")
    $ setWait(2.165,5.502)
    $ speak(NICOLE, "No totally, I won't fuck it down or left either, don't worry.")
    show jecka sc9:
        rightcenterstage

    $ setWait(5.502,6.544)
    $ speak(JECKA, "What about right?")
    $ setWait(6.544,8.505)
    $ speak(NICOLE, "I always fuck it right.")
    $ setWait(8.505,12.926)
    $ speak(JECKA, "Cool, so we gotta be there before 8pm so let's just check out and head straight there.")
    show nicole sc6 surprised:
        leftcenterstage

    $ setWait(12.926,15.178)
    $ speak(NICOLE, "Wait but there's no like directions or anything?")
    $ setWait(15.178,16.596)
    $ speak(JECKA, "I got GPS in my car.")
    show nicole sc6 angry:
        leftcenterstage

    $ setWait(16.596,19.432)
    $ speak(NICOLE, "No I mean directions for stepping on people?")
    $ setWait(19.432,24.979)
    $ speak(JECKA, "Oh I mean it's pretty self-explanatory, they just press their face against your feet.")
    show nicole sc6:
        leftcenterstage

    $ setWait(24.979,26.356)
    $ speak(NICOLE, "Do they beat off while you're there?")
    $ setWait(26.356,29.818)
    $ speak(JECKA, "No that's way extra, like a thousand dollars extra.")
    show nicole sc6 surprised:
        leftcenterstage

    $ setWait(29.818,33.697)
    $ speak(NICOLE, "A thousand bucks? You could have actual sex with a ho for less than a thousand.")
    show jecka sc9 angry:
        rightcenterstage

    $ setWait(33.697,37.575)
    $ speak(JECKA, "Nicole, we are thin, white, and pretty. Everything we do comes with a premium.")
    show nicole sc6 smile:
        leftcenterstage

    $ setWait(37.575,39.077)
    $ speak(NICOLE, "And we ain't talkin' saltines.")
    show jecka sc9:
        rightcenterstage

    $ setWait(39.077,41.121)
    $ speak(JECKA, "But yeah the guy we're gonna see is just Jeffery.")
    show nicole sc6 angry:
        leftcenterstage

    $ setWait(41.121,43.79)
    $ speak(NICOLE, "Ew! Why would you let him whore your feet out? Find someone cuter.")
    show jecka sc9 angry:
        rightcenterstage

    $ setWait(43.79,48.42)
    $ speak(JECKA, "That's not how it works! If they pay enough you just do it, it's not like dating where you can be picky.")
    show nicole sc6:
        leftcenterstage
    $ setWait(48.42,52.173)
    $ speak(NICOLE, "I guess if we're going together it's not so bad. We can make fun of him and stuff.")
    $ setWait(52.173,55.135)
    $ speak(JECKA, "No you can't really do that either cause then he won't wanna hire me again.")
    $ setWait(55.135,57.929)
    $ speak(NICOLE, "Yeah I guess feet fucking comes with a lot of insecurity.")
    $ setWait(57.929,60.849)
    $ speak(JECKA, "It's not feet fucking you just play footsie with his face.")
    $ setWait(60.849,63.309)
    $ speak(NICOLE, "Man my therapist is gonna have a field day with this.")
    show jecka sc9 sad:
        rightcenterstage
        pause 2
        linear 0.2 centerstage
        linear 0.3 rightcenterstage

    $ setWait(63.309,65.603)
    $ speak(JECKA, "Oh and you're gonna wanna take a few of these.")
    $ setWait(65.603,66.479)
    $ speak(NICOLE, "Is that xanax?")
    show jecka sc9:
        rightcenterstage

    $ setWait(66.479,72.485)
    $ speak(JECKA, "Yeah I need it for like every client or my feet are shaking. I just told the doctor I'm afraid of heights and he wrote me a whole bottle.")
    $ setWait(72.485,74.821)
    $ speak(JECKA, "I got name brand from the pharmacist too.")
    $ setWait(74.821,76.114)
    $ speak(NICOLE, "Is name brand really good?")
    show jecka sc9 smile:
        rightcenterstage
    $ setWait(76.114,77.949)
    $ speak(JECKA, "It's not just good...")
    $ setWait(77.949,80.41)
    $ speak(JECKA, "...It's on its best behavior.")
    stop ambient fadeout 1.5
    jump scene_S0032

label scene_S0032:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jeffery day with Pause(2.708):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.708 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0032.mp3")
    play ambient "audio/Ambience/House_Ambience.mp3"
    scene cut0032a
    $ setWait(2.708,8.506)
    $ speak(JEFFERY, "Ohhhh you girls spoil me so good, I knew things would get better after high school.")
    $ setWait(8.506,12.676)
    $ speak(JECKA, "Jeffery, just focus on feet, not the society around them okay?")
    $ setWait(12.676,14.804)
    $ speak(JEFFERY, "Yes ma'am- Mmmmmm.")
    $ setWait(14.804,16.305)
    $ speak(NICOLE, "Ew I can feel his mouth vibrate.")
    scene cut0032b
    $ setWait(16.305,17.181)
    $ speak(JECKA, "Shhh!")
    scene cut0032c
    $ setWait(17.181,19.391)
    $ speak(NICOLE, "Every woman on his wall is a cartoon.")
    $ setWait(19.391,21.644)
    $ speak(JECKA, "Yeah he pays us to do this, what'd you expect?")
    $ setWait(21.644,24.438)
    $ speak(JEFFERY, "I can't decide who's feet are more cute!")
    scene cut0032a
    $ setWait(24.438,26.273)
    $ speak(JECKA, "Oh uh, thanks.")
    $ setWait(26.273,30.82)
    $ speak(NICOLE, "Yeah it's not like they're essential for human function or anything, every part of a woman is just for your entertainment.")
    scene cut0032b
    $ setWait(30.82,31.487)
    $ speak(JECKA, "Nicole.")
    $ setWait(31.487,33.447)
    $ speak(JEFFERY, "Oh did I say something wrong?")
    scene cut0032a
    $ setWait(33.447,36.075)
    $ speak(NICOLE, "Nothing you'll ever correct in your lifetime, don't worry about it.")
    $ setWait(36.075,38.661)
    $ speak(JECKA, "Yeah we're judgment-free girls.")
    $ setWait(38.661,39.954)
    $ speak(NICOLE, "Enjoy those feet, piggy.")
    scene cut0032c
    $ setWait(39.954,40.538)
    $ speak(JECKA, "Nicole!")
    $ setWait(40.538,41.747)
    $ speak(NICOLE, "What? I think he likes it.")
    $ setWait(41.747,44.75)
    $ speak(JEFFERY, "Mmmmm... I'm Mommy's piggy...")
    scene cut0032d
    $ setWait(44.75,46.001)
    $ speak(JECKA, "Oh, gross.")
    $ setWait(46.001,50.005)
    $ speak(NICOLE, "His standards are so low he thinks any interaction from a girl is affection.")
    $ setWait(50.005,52.967)
    $ speak(NICOLE, "You like that you video game shirt wearing loser?")
    $ setWait(52.967,55.553)
    $ speak(JEFFERY, "I love it... Mmm...")
    scene cut0032a
    $ setWait(55.553,58.305)
    $ speak(JECKA, "She just wants you to be better Jeffery, don't worry.")
    $ setWait(58.305,61.183)
    $ speak(NICOLE, "Yeah as in you better not think we're equal, bitch.")
    $ setWait(61.183,65.062)
    $ speak(JEFFERY, "I know, you two will always be my first priority.")
    $ setWait(65.062,71.11)
    $ speak(NICOLE, "Uh huh, cause what's the point in actually dating girls? You're just gonna come crawling back to anime women and feet.")
    $ setWait(71.11,71.986)
    $ speak(JEFFERY, "You're right.")
    $ setWait(71.986,80.202)
    $ speak(NICOLE, "And you'll tell everyone in the world that relationships are overrated, but the truth is you're just a lonely little foot loser.")
    $ setWait(80.202,81.704)
    $ speak(JECKA, "Uh but in a good way!")
    $ setWait(81.704,85.165)
    $ speak(NICOLE, "In a \"cartoon women on your walls guarantee you'll die alone\" way.")
    $ setWait(85.165,87.334)
    $ speak(JEFFERY, "Mmm good thing I got you guys.")
    $ setWait(87.334,91.714)
    $ speak(NICOLE, "And if you wanna keep us, you're gonna take us to Olive Garden and pay for everything.")
    $ setWait(91.714,93.424)
    $ speak(JEFFERY, "Aw sweet like a date?")
    $ setWait(93.424,100.389)
    $ speak(NICOLE, "Fuck no. We're gonna sit at our own table and you're gonna pay for our meal while you sit alone at the bar. Understand?")
    $ setWait(100.389,101.891)
    $ speak(JEFFERY, "Why would I do that?")
    $ setWait(101.891,108.606)
    $ speak(NICOLE, "Cause you're a little board game enthusiast bitch who knows you'll never have sex with us, so spending money on us is the next best thing.")
    $ setWait(108.606,113.986)
    $ speak(JEFFERY, "Ugh it sounds so comforting when you say it, like you know my place in the world.")
    $ setWait(113.986,117.656)
    $ speak(NICOLE, "Mhmm, and that place is right under our feet like a bug.")
    $ setWait(117.656,121.785)
    $ speak(NICOLE, "A little pornographic Japanese video game playing bug.")
    scene cut0032b
    $ setWait(121.785,122.953)
    $ speak(JECKA, "They have porn video games?")
    $ setWait(122.953,128.25)
    $ speak(JEFFERY, "But my Mom's gonna get mad at me for spending so much of my money in one day.")
    scene cut0032a
    $ setWait(128.25,130.419)
    $ speak(JECKA, "I mean you don't have to care what she thinks.")
    $ setWait(130.419,132.671)
    $ speak(NICOLE, "Yeah who would you rather fuck, us or your mom?")
    $ setWait(132.671,133.964)
    $ speak(JEFFERY, "Mmmmmm...")
    $ setWait(133.964,135.257)
    $ speak(JEFFERY, "Tough choice...")
    scene cut0032d
    $ setWait(135.257,136.8)
    $ speak(JECKA, "Why is that a tough choice?")
    $ setWait(136.8,141.013)
    $ speak(JEFFERY, "FeetMeet.com has a mommy-play board and... ugh...")
    $ setWait(141.013,142.264)
    $ speak(JECKA, "She said your mom.")
    $ setWait(142.264,145.559)
    $ speak(NICOLE, "Hey, your mom, my mom, we're all mom, let's get some Olive Garden.")
    $ setWait(145.559,149.021)
    $ speak(JEFFERY, "Okay just 5 more minutes with your feet, Mommy.")
    $ setWait(149.021,151.565)
    $ speak(JECKA, "Ohhh now he's calling us that...")
    stop ambient fadeout 1.5
    jump scene_S0033

label scene_S0033:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show olive garden ext with Pause(2.588):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.588 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0033.mp3")
    scene olive garden door
    $ csbox = False

    show jecka sc9:
        leftmidstage
        xzoom -1

    show nicole sc6:
        leftcenterstage
        xzoom -1


    $ setWait(2.588,4.423)
    $ speak(JECKA, "Why'd we come here on a Friday evening?")
    $ setWait(4.423,7.593)
    $ speak(NICOLE, "Yeah it's packed with families thinking you need to dress up to go here.")
    $ setWait(7.593,9.554)
    $ speak(JECKA, "A 20 minute wait. Unbelievable.")
    $ setWait(9.554,12.473)
    $ speak(NICOLE, "Yeah and it was 25 before we flirted with the host.")
    $ setWait(12.473,15.101)
    $ speak(JECKA, "Like our affection combined is only worth 5 minutes?")
    show jeffery sc2:
        off_right
        linear 2.4 rightmidstage

    $ setWait(15.101,18.479)
    $ speak(JEFFERY, "Yeah I think you guys are way cuter and nicer than 5 minutes.")
    show nicole sc6:
        leftcenterstage
        xzoom 1

    $ setWait(18.479,20.314)
    $ speak(NICOLE, "Jeffery don't while we're in public with you.")
    $ setWait(20.314,23.818)
    $ speak(JECKA, "I swear to god, unlimited soup and salad is not worth this hassle.")
    show nicole sc6:
        leftcenterstage
        xzoom -1
    $ setWait(23.818,24.944)
    $ speak(NICOLE, "What about the breadsticks?")
    show jecka sc9 angry:
        leftmidstage
        xzoom -1
    $ setWait(24.944,27.738)
    $ speak(JECKA, "Fuck the breadsticks! They don't even crunch when you bite into them.")
    $ setWait(27.738,32.243)
    $ speak(NICOLE, "Yeah just another chain restaurant bested by the Red Lobster cheesy biscuits.")
    show jecka sc9:
        leftmidstage
        xzoom -1
    $ setWait(32.243,33.536)
    $ speak(JECKA, "You wanna go there instead?")
    $ setWait(33.536,36.539)
    $ speak(NICOLE, "Maybe, but first I just wanna stick it to Olive Garden.")
    $ setWait(36.539,37.54)
    $ speak(JECKA, "Yeah I feel that.")
    $ setWait(37.54,39.041)
    $ speak(NICOLE, "I'm gonna break one of their windows.")
    show jecka sc9 sad:
        leftmidstage
        xzoom -1

    $ setWait(39.041,40.835)
    $ speak(JECKA, "But you're gonna get caught on their cameras.")
    $ setWait(40.835,42.169)
    $ speak(NICOLE, "Yeah you're right...")
    show nicole sc6 smile:
        leftcenterstage
        xzoom 1

    show jecka sc9:
        leftmidstage
        xzoom -1

    $ setWait(42.169,44.63)
    $ speak(NICOLE, "...Jeffery could you break one of their windows for us?")
    $ setWait(44.63,47.008)
    $ speak(JEFFERY, "But... But I might get in trouble!")
    $ setWait(47.008,48.009)
    $ speak(JECKA, "Oh come on, Jeffery.")
    show nicole sc6 flirt:
        leftcenterstage
        linear 2 rightcenterstage
    $ setWait(48.009,50.761)
    $ speak(NICOLE, "Yeah Jeffery don't you wanna make us happy?")
    show jeffery sc2 blush:
        rightmidstage
    $ setWait(50.761,52.555)
    $ speak(JEFFERY, "I... Yeah.")
    $ setWait(52.555,56.976)
    $ speak(NICOLE, "So you go ahead and make me happy, make Mommy happy.")
    show jeffery sc2 blush:
        rightmidstage
        xzoom -1
        linear 3 off_right
    $ setWait(56.976,61.105)
    $ speak(JEFFERY, "Ugh yes Mommy...")
    $ setWait(61.105,62.523)
    $ speak(JECKA, "Is he really gonna--")
    show jecka sc9 surprised:
        xzoom -1
        leftmidstage

    show nicole sc6 surprised:
        rightcenterstage
    $ setWait(62.523,64.108)
    $ speak(NICOLE, "Oh my god.")
    show jeffery sc2 smile:
        off_right
        xzoom 1
        linear 1 rightmidstage
    $ setWait(64.108,66.36)
    $ speak(JEFFERY, "Okay was- was that good?")
    show nicole sc6 smile:
        rightcenterstage

    show jecka sc9:
        leftmidstage
        xzoom -1

    $ setWait(66.36,67.862)
    $ speak(NICOLE, "Awww that was so good.")
    $ setWait(67.862,68.779)
    $ speak(JECKA, "It was pretty cool.")

    show nicole sc6:
        xzoom -1
        rightcenterstage
        linear 1 leftcenterstage

    $ setWait(68.779,72.199)
    $ speak(NICOLE, "I didn't think he'd actually do it, I guess we gotta go to Red Lobster now.")
    $ setWait(72.199,74.952)
    $ speak(JEFFERY, "Is there anything else I can do for you?")
    show nicole sc6 smile:
        xzoom 1
        leftcenterstage

    $ setWait(74.952,78.372)
    $ speak(NICOLE, "Hmm well there's a couple things I wanted to steal at the mall lately.")
    show jeffery sc2:
        rightmidstage

    $ setWait(78.372,80.041)
    $ speak(JEFFERY, "You're gonna steal?")
    $ setWait(80.041,83.169)
    $ speak(NICOLE, "No you're gonna steal, for Mommy right?")
    show jecka sc9 sad:
        leftmidstage
        xzoom -1

    $ setWait(83.169,84.92)
    $ speak(JECKA, "Nicole you're gonna get us arrested.")
    show nicole sc6:
        leftcenterstage
        xzoom -1

    $ setWait(84.92,87.506)
    $ speak(NICOLE, "Don't worry, worst case scenario he gets arrested.")
    $ setWait(87.506,90.051)
    $ speak(JEFFERY, "Do you want me to steal anything for you Jecka?")

    show jecka sc9 sad:
        leftmidstage
        xzoom -1
        pause 5.9
        xzoom 1
        linear 1.3 off_left

    $ setWait(90.051,97.642)
    $ speak(JECKA, "Oh no that's okay- I just remembered I left a Digiorno in the oven, for the last 3 hours, so I gotta take care of that.")
    $ setWait(97.642,99.935)
    $ speak(JEFFERY, "Oh no, Mommy's digiornos...")
    show nicole sc6 smile:
        xzoom 1
        leftcenterstage
        linear 1.5 rightcenterstage

    $ setWait(99.935,101.854)
    $ speak(NICOLE, "Forget her, c'mon let's go to the mall.")
    $ setWait(101.854,103.648)
    $ speak(JEFFERY, "What store are we going to first?")
    $ setWait(103.648,108.235)
    $ speak(NICOLE, "I'm feeling Walgreens actually, I need you to steal a whole lot of cough medicine.")
    $ setWait(108.235,109.612)
    $ speak(JEFFERY, "Oh no, are you sick?")
    $ setWait(109.612,114.575)
    $ speak(NICOLE, "No you're sick, I need you to take all the medicine you steal, entire bottle.")
    $ setWait(114.575,118.496)
    $ speak(JEFFERY, "But I don't have a cough or anything. Why do you want me to take so much?")
    show nicole sc6 flirt:
        rightcenterstage
        xzoom 1
    $ setWait(118.496,123.751)
    $ speak(NICOLE, "Cause Mommy's bored and wants to see what DXM will do to you. So you gonna entertain Mommy?")
    $ setWait(123.751,125.544)
    $ speak(JEFFERY, "You're right, let's go.")
    show nicole sc6 smile:
        xzoom -1
        rightcenterstage
        linear 4 off_farleft

    show jeffery sc2:
        rightmidstage
        pause 1
        linear 3.8 off_left

    $ setWait(125.544,129.548)
    $ speak(NICOLE, "And after that we're going to Hot Topic to see how many T-shirts scare you.")
    stop ambient fadeout 1.5
    jump scene_S0034

label scene_S0034:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka night with Pause(2.834):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.834 zoom 1.05 truecenter
    $ setVoiceTrack("audio/Scenes/0034.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene livingroom jecka
    show dad undershirt upset:
        xzoom -1
        leftcenterstage
    $ setWait(2.834,3.835)
    $ speak(DAD, "Jessica!")

    show jecka pj:
        off_right
        linear 1.3 rightmidstage

    $ setWait(3.835,5.003)
    $ speak(JECKA, "Don't hit me, what.")
    $ setWait(5.003,10.926)
    $ speak(DAD, "What's this unpaid power bill notice? We made the power your responsibility, remember?")
    $ setWait(10.926,14.804)
    $ speak(JECKA, "I know it was just, something changed at work that messed with my income a little.")
    $ setWait(14.804,16.681)
    $ speak(DAD, "What kind of change?")
    $ setWait(16.681,21.645)
    $ speak(JECKA, "Well Nico-- I mean, my hours got split with some bitch who listens to Evanescence.")
    $ setWait(21.645,24.064)
    $ speak(DAD, "But you're still out for the same amount of time.")
    $ setWait(24.064,27.901)
    $ speak(JECKA, "Oh that's cause I'm just looking for a new job, I gotta stay proactive.")
    show dad undershirt smile:
        leftcenterstage
        xzoom -1
    $ setWait(27.901,32.405)
    $ speak(DAD, "Great initiative, dear. Unlike your waste of human flesh mother.")
    show jecka pj sad:
        rightmidstage

    $ setWait(32.405,33.74)
    $ speak(JECKA, "Uh y-yeah.")
    $ setWait(33.74,39.996)
    $ speak(DAD, "But so how's the day-to-day of your diner job? I'm sure you're up to your knees in hungry customers.")
    $ setWait(39.996,42.332)
    $ speak(JECKA, "Usually just the toes, sometimes ankles.")
    $ setWait(42.332,43.792)
    $ speak(DAD, "And do they tip well?")
    show jecka pj:
        rightmidstage

    $ setWait(43.792,48.38)
    $ speak(JECKA, "Yeah, but not always in money. One time a guy gave me a pair of shoes.")
    show dad undershirt:
        leftcenterstage

    $ setWait(48.38,53.635)
    $ speak(DAD, "I didn't know people would tip like that, just don't let 'em get away with that next time. Cash only.")
    $ setWait(53.635,56.054)
    $ speak(JECKA, "Yeah cash, smaller footprint too.")
    $ setWait(56.054,58.807)
    $ speak(DAD, "Y'know the saying, give 'em an inch and they take a mile.")
    $ setWait(58.807,59.599)
    $ speak(JECKA, "Or a foot.")
    $ setWait(59.599,63.52)
    $ speak(DAD, "The resaurant business can be so tricky, just stay on your toes.")
    $ setWait(63.52,64.521)
    $ speak(JECKA, "Oh I have been.")
    $ setWait(64.521,70.485)
    $ speak(DAD, "Still glad to hear you're applying other places, just gotta get that foot in the door in the right business.")
    $ setWait(70.485,72.862)
    $ speak(JECKA, "Totally, my foot's been in a lot of places.")
    $ setWait(72.862,79.077)
    $ speak(DAD, "Just don't spread yourself too thin though. Quantity can be the Achilles Heel of quality.")
    $ setWait(79.077,80.579)
    $ speak(JECKA, "They usually call it \"Mommy's heel\".")
    $ setWait(80.579,81.121)
    $ speak(DAD, "What was that?")
    show jecka pj sad:
        rightmidstage

    $ setWait(81.121,85.959)
    $ speak(JECKA, "Oh nothing, I was thinking about.. the penguins in Happy Feet.")
    show dad undershirt smile:
        leftcenterstage

    $ setWait(85.959,89.838)
    $ speak(DAD, "Some things never change, you always spaced out as a little girl.")
    show jecka pj:
        rightmidstage

    $ setWait(89.838,91.923)
    $ speak(JECKA, "Yeah I'm kind of a free thinker.")
    show dad undershirt:
        leftcenterstage
    $ setWait(91.923,96.052)
    $ speak(DAD, "But now that you're an adult you're gonna have to get your act together before I..")
    show dad undershirt yell:
        leftcenterstage

    show jecka pj surprised:
        rightmidstage
        linear 0.06 xalign .9
        linear 0.06 xalign .86
        linear 0.08 rightmidstage

    $ setWait(96.052,98.013)
    $ speak(DAD, "..Kick your fucking teeth in!!")
    show jecka pj sad:
        rightmidstage
    $ setWait(98.013,98.638)
    $ speak(JECKA, "Dad, no.")
    show dad undershirt yell:
        xzoom -1
        leftcenterstage
        linear 0.5 rightcenterstage
    $ setWait(98.638,103.727)
    $ speak(DAD, "No nothing, bitch!! Keep screwing around I'll shove my fucking foot down your throat!!")
    show jecka pj sad:
        rightmidstage
        linear 0.06 xalign .89
        linear 0.06 xalign .87
        linear 0.06 xalign .89
        linear 0.06 rightmidstage

    $ setWait(103.727,104.728)
    $ speak(JECKA, "For how much!?")

    show jecka pj sad:
        rightmidstage
        pause 4.5
        xzoom -1

    show dad undershirt upset:
        rightcenterstage
        xzoom -1
        pause 2.7
        linear 2.8 off_right



    $ setWait(104.728,110.358)
    $ speak(DAD, "Ugh now if you'll excuse me, The Love Guru's on HBO.")
    stop ambient fadeout 1.6
    jump scene_S0035

label scene_S0035:
    show black onlayer screens with Pause(1.5):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0035.mp3")
    play ambient "audio/Ambience/CornerStore_Ambience.mp3" fadein 1
    scene store_vabc
    show nicole sc7:
        rightcenterstage

    show jecka sc10:
        rightmidstage
    $ setWait(0.077,2.288)
    $ speak(JECKA, "Who's Bartles and Jaymes anyway?")
    $ setWait(2.288,4.582)
    $ speak(NICOLE, "Probably white guys who want us to respect the flag.")
    $ setWait(4.582,9.545)
    $ speak(JECKA, "My least favorite white guys are patriotic with an unexpected cross of forced quirkiness.")
    $ setWait(9.545,10.63)
    $ speak(NICOLE, "Quirky how?")
    show jecka sc10 angry:
        rightmidstage
    $ setWait(10.63,13.883)
    $ speak(JECKA, "Like shit like, proposing with a Ring Pop and thinking it's funny.")
    $ setWait(13.883,17.053)
    $ speak(NICOLE, "Ohhh I saw that on YouTube once. Yeah what're you Willy Wonka?")
    $ setWait(17.053,22.224)
    $ speak(JECKA, "Marriage proposal's like the one time in any boring man's life where he attempts a shred of creativity.")
    $ setWait(22.224,23.809)
    $ speak(NICOLE, "Yeah I was proposed to once.")
    show jecka sc10:
        rightmidstage
    $ setWait(23.809,24.935)
    $ speak(JECKA, "No way, who?")
    $ setWait(24.935,25.686)
    $ speak(NICOLE, "Cormac.")
    show jecka sc10 surprised:
        rightmidstage
    $ setWait(25.686,26.896)
    $ speak(JECKA, "Crusty Cormac??")
    $ setWait(26.896,30.566)
    $ speak(NICOLE, "Yeah he went insane when I stepped on him last week. It was a diamond toe-ring.")
    show jecka sc10 sad:
        rightmidstage
    $ setWait(30.566,31.4)
    $ speak(JECKA, "What the fuck.")
    $ setWait(31.4,33.027)
    $ speak(NICOLE, "Okay I'm exaggerating, it was quartz.")
    $ setWait(33.027,37.239)
    $ speak(JECKA, "No- last time we saw Cormac was 3 weeks ago. Are you seeing these guys without me?")
    $ setWait(37.239,38.491)
    $ speak(NICOLE, "What's wrong with that?")
    show jecka sc10:
        rightmidstage
    $ setWait(38.491,42.411)
    $ speak(JECKA, "Cause he hasn't called me in 3 weeks, I'm losing money. You're watering down the market.")
    $ setWait(42.411,44.372)
    $ speak(NICOLE, "What am I supposed to turn down free money?")
    show jecka sc10 angry:
        rightmidstage
    $ setWait(44.372,47.708)
    $ speak(JECKA, "You're supposed to include me cause I got you into this in the first place.")
    show nicole sc7 angry:
        rightcenterstage
    $ setWait(47.708,50.795)
    $ speak(NICOLE, "Wow you helped me be a foot whore, I should be so grateful.")
    $ setWait(50.795,53.798)
    $ speak(JECKA, "It was fine when you did it with Jeffery but now it's screwing my money up.")
    show nicole sc7 smile:
        rightcenterstage


    $ setWait(53.798,56.634)
    $ speak(NICOLE, "Oh speaking of Jeffery, he's like really fun.")
    show jecka sc10:
        rightmidstage

    $ setWait(56.634,58.803)
    $ speak(JECKA, "Fun how?")
    $ setWait(58.803,60.513)
    $ speak(NICOLE, "...I got him to suck off a homeless guy.")
    show jecka sc10 smile:
        rightmidstage

    $ setWait(60.513,62.264)
    $ speak(JECKA, "Oh okay yeah alright.")
    show nicole sc7:
        rightcenterstage
    $ setWait(62.264,67.269)
    $ speak(NICOLE, "No I'm not joking! It's his mommy thing, he'll do whatever I tell him to.")
    show jecka sc10 surprised:
        rightmidstage
    $ setWait(67.269,71.44)
    $ speak(JECKA, "Who, what, where, when, and why the fuck did you do that?")
    $ setWait(71.44,77.071)
    $ speak(NICOLE, "We were walking out of the mall and some homeless dude asked for change and I was just like \"Oh we got something better than change\".")
    $ setWait(77.071,81.367)
    $ speak(NICOLE, "So I told Jeffery I'd kill myself if he didn't do it.. Then he did it...")
    show nicole sc7 smile:
        rightcenterstage

    $ setWait(81.367,83.577)
    $ speak(NICOLE, "And the homeless guy got 10 dollars so it's all good.")
    $ setWait(83.577,86.956)
    $ speak(JECKA, "He got? --Jeffery paid 10 dollars to suck his dick?")
    $ setWait(86.956,88.833)
    $ speak(NICOLE, "Yeah it was pretty funny.")
    show jecka sc10 sad:
        rightmidstage

    $ setWait(88.833,93.045)
    $ speak(JECKA, "I'm like.. glad and not glad I missed that at the same time.")
    $ setWait(93.045,95.548)
    $ speak(JECKA, "But what if Jeffery got AIDS doing that?")
    show nicole sc7 angry:
        rightcenterstage
    $ setWait(95.548,99.427)
    $ speak(NICOLE, "Well he's locked in his room playing Spyro all day, not spreading it any time soon.")
    show jecka sc10:
        rightmidstage

    $ setWait(99.427,102.763)
    $ speak(JECKA, "Is that why you're getting 4 Captain Morgans? To drink the guilt away?")
    show nicole sc7:
        rightcenterstage

    $ setWait(102.763,110.062)
    $ speak(NICOLE, "No I'm going to a party tonight, I would never feel guilty over anything bad happening to Jeffery. Like genuinely a terrible human being.")
    $ setWait(110.062,111.522)
    $ speak(JECKA, "He's not that bad.")
    show nicole sc7 angry:
        rightcenterstage

    $ setWait(111.522,119.029)
    $ speak(NICOLE, "He told me he fantasizes about a world where women are milked like cows and mandated to have sex with any guy who wants them.")
    show jecka sc10 sad:
        rightmidstage

    $ setWait(119.029,120.448)
    $ speak(JECKA, "Ohh that's really bad.")

    $ setWait(120.448,125.077)
    $ speak(NICOLE, "So I literally don't care what happens to him. Now let's buy this Captain Morgan and get the hell out.")
    show jecka sc10:
        rightmidstage

    $ setWait(125.077,126.495)
    $ speak(JECKA, "When'd you get your fake ID?")
    show nicole sc7:
        rightcenterstage

    $ setWait(126.495,127.538)
    $ speak(NICOLE, "What fake ID?")
    show jecka sc10 angry:
        rightmidstage

    $ setWait(127.538,130.04)
    $ speak(JECKA, "We picked out all this shit and you don't even have a fake ID.")
    $ setWait(130.04,132.293)
    $ speak(NICOLE, "I don't need one, it's the Pakistani guy working today.")
    show jecka sc10:
        rightmidstage
    $ setWait(132.293,133.836)
    $ speak(JECKA, "He loves the white girls.")
    show nicole sc7 smile:
        rightcenterstage
        pause 0.6
        xzoom -1
        linear 4 off_left

    show jecka sc10:
        rightmidstage
        pause 1.15
        linear 4.3 off_left

    $ setWait(133.836,135.212)
    $ speak(NICOLE, "Yeah let's flirt.")
    stop ambient fadeout 1.5
    jump scene_S0036

label scene_S0036:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0036.mp3")
    play ambient "audio/Ambience/Hood_Ambience.mp3" fadein 1
    scene parkinglot night
    show jecka sc10:
        xzoom -1
        centerstage

    $ setWait(0.085,4.548)
    $ speak(FOOTFREAK, "Ohh man these FeetMeet reviews weren't lying.")
    $ setWait(4.548,5.507)
    $ speak(JECKA, "Reviews?")
    $ setWait(5.507,14.349)
    $ speak(FOOTFREAK, "Yeah there's a scoring system for every girl's feet on the forums. You got a solid 9.6 out of 10.")
    $ setWait(14.349,17.269)
    $ speak(JECKA, "How do you.. score feet?")
    $ setWait(17.269,25.986)
    $ speak(FOOTFREAK, "Oh like callouses, toe length, just a lot of science. Pretty important stuff. You're about top 20 on the whole site.")
    $ setWait(25.986,27.654)
    $ speak(JECKA, "Who's number 1?")
    $ setWait(27.654,29.281)
    $ speak(FOOTFREAK, "Anna Kournikova.")
    show jecka sc10 sad:
        xzoom -1
        centerstage
    $ setWait(29.281,32.659)
    $ speak(JECKA, "Oh... Guess that K-Swiss deal didn't work out.")
    $ setWait(32.659,37.915)
    $ speak(FOOTFREAK, "But number 3 is someone totally new to the scene, practically came out of nowhere.")
    show jecka sc10:
        xzoom -1
        centerstage
    $ setWait(37.915,39.875)
    $ speak(JECKA, "Uh, that's nice.")
    $ setWait(39.875,42.252)
    $ speak(FOOTFREAK, "I think her name's Nicole.")
    show jecka sc10 surprised:
        xzoom -1
        centerstage
    $ setWait(42.252,42.878)
    $ speak(JECKA, "What??")
    $ setWait(42.878,48.884)
    $ speak(FOOTFREAK, "Yeah a real special girl, I'll tell ya. They give her a 9.89 out of 10.")
    show jecka sc10 sad:
        xzoom -1
        centerstage
    $ setWait(48.884,50.219)
    $ speak(JECKA, "But she just started.")
    $ setWait(50.219,60.521)
    $ speak(FOOTFREAK, "I know she ranks higher than you, and honestly your feet alone are way nicer. Though it's not always about the feet, but the girl connected to them.")
    show jecka sc10:
        xzoom -1
        centerstage
    $ setWait(60.521,62.773)
    $ speak(JECKA, "Like we're objects, great.")
    $ setWait(62.773,65.692)
    $ speak(FOOTFREAK, "Can you stand on my face now?")
    show jecka sc10:
        xzoom -1
        centerstage
        linear 0.6 rightcenterstage
    $ setWait(65.692,69.238)
    $ speak(JECKA, "Yeah sure, I gotta make a phone call anyway.")
    show text_callnicole onlayer screens
    $ setWait(69.238,70.656)
    $ speak(JECKA, "...")
    $ setWait(70.656,73.075)
    $ speak(JECKA, "Damn that party must be wild.")
    hide text_callnicole onlayer screens
    $ setWait(73.075,77.079)
    $ speak(JECKA, "But if she's there then that means the other foot money should be available.")
    show text_calljeffery onlayer screens
    $ setWait(77.079,82.292)
    $ speak(JECKA, "...")
    $ setWait(82.292,86.171)
    $ speak(JECKA, "Jeffery's never out doing anything, why's his phone off?")
    hide text_calljeffery onlayer screens
    $ setWait(86.171,87.548)
    $ speak(JECKA, "...Unless...")
    $ setWait(87.548,93.011)
    $ speak(FOOTFREAK, "I know my phone's off when I'm getting stepped on. Kinda rude to leave it on.")
    $ setWait(93.011,95.013)
    $ speak(FOOTFREAK, "Might have to leave a bad review.")
    show jecka sc10 angry:
        rightcenterstage
        xzoom -1
        pause 1.64
        linear 2.4 off_right
    $ setWait(95.013,97.599)
    $ speak(JECKA, "Fuck off, foot bitch! I gotta go check something.")
    $ setWait(97.599,105.732)
    $ speak(FOOTFREAK, "Ughhhh the feet, I feel so cold without the feet.")
    stop ambient fadeout 1.5
    jump scene_S0037

label scene_S0037:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jeffery night with Pause(2.882):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.882 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0037.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    show black onlayer screens:
        alpha 0.2
    scene bedroom jeffery night
    show nicole sc7 smile:
        leftcenterstage

    show jeffery sc3 blush:
        rightcenterstage

    $ setWait(2.882,5.301)
    $ speak(NICOLE, "This is such a fun party, right?")
    $ setWait(5.301,7.678)
    $ speak(JEFFERY, "Yeah... Yeah I guess so.")
    show nicole sc7 angry:
        leftcenterstage

    $ setWait(7.678,9.764)
    $ speak(NICOLE, "What the hell, you don't like partying with mommy?")
    $ setWait(9.764,13.809)
    $ speak(JEFFERY, "No I do, I just feel a little weird.")
    show nicole sc7:
        leftcenterstage
    $ setWait(13.809,16.729)
    $ speak(NICOLE, "Weird how? Like how you make girls feel weird?")
    $ setWait(16.729,19.815)
    $ speak(JEFFERY, "No just.. woozy.")
    show nicole sc7 smile:
        leftcenterstage
        pause 2
        linear 0.25 centerstage
        linear 0.35 leftcenterstage
    $ setWait(19.815,24.362)
    $ speak(NICOLE, "You probably just haven't hit the vibe yet. Here, take another sip of mommy's Captain Morgan.")
    $ setWait(24.362,29.242)
    $ speak(JEFFERY, "Another drink? But you already made me take 3 ambien.")
    $ setWait(29.242,32.995)
    $ speak(NICOLE, "Yeah cause you looked super sick and you needed to take some medicine.")
    $ setWait(32.995,36.04)
    $ speak(NICOLE, "Come on, I just drank from the bottle. It's like you're kissing mommy.")
    $ setWait(36.04,41.045)
    $ speak(JEFFERY, "Well I never kissed a girl before so...")
    $ setWait(41.045,42.797)
    $ speak(NICOLE, "That's it, drink up.")
    $ setWait(42.797,44.966)
    $ speak(JEFFERY, "Ugh it burns my throat.")
    $ setWait(44.966,48.719)
    $ speak(NICOLE, "Uh uh, drink a little more. The burn means you love me, okay?")
    $ setWait(48.719,50.93)
    $ speak(JEFFERY, "Okay, mommy...")
    $ setWait(50.93,52.181)
    $ speak(NICOLE, "That's a good boy.")
    $ setWait(52.181,54.225)
    $ speak(JEFFERY, "Ugh... now what?")
    show nicole sc7:
        leftcenterstage
    $ setWait(54.225,56.769)
    $ speak(NICOLE, "I don't know, you still look kinda under the weather so-")
    show jeffery sc3 angry:
        rightcenterstage

    $ setWait(56.769,59.146)
    $ speak(JEFFERY, "I already told you, I'm fine!")
    show jeffery sc3 blush:
        rightcenterstage

    show nicole sc7 angry:
        leftcenterstage
    $ setWait(59.146,63.276)
    $ speak(NICOLE, "Don't you ever fucking talk back to me! Do you want mommy to go home?")
    $ setWait(63.276,64.235)
    $ speak(JEFFERY, "No...")
    $ setWait(64.235,66.57)
    $ speak(NICOLE, "God you'll be a virgin forever at this rate.")
    $ setWait(66.57,70.908)
    $ speak(JEFFERY, "Wait, do you mean that you'd...")
    show nicole sc7 surprised:
        leftcenterstage
    $ setWait(70.908,71.367)
    $ speak(NICOLE, "Oh-")
    show nicole sc7 flirt:
        leftcenterstage
    $ setWait(71.367,75.538)
    $ speak(NICOLE, "Only if you take your medicine. You want mommy to have sex with you, right?")
    $ setWait(75.538,80.418)
    $ speak(JEFFERY, "Mmm, okay what medicine?")
    show nicole sc7 smile:
        leftcenterstage

    $ setWait(80.418,83.337)
    $ speak(NICOLE, "Mommy needs you to take some xanax, okay?")
    $ setWait(83.337,86.465)
    $ speak(JEFFERY, "X-xanax? Is that good?")
    $ setWait(86.465,88.009)
    $ speak(NICOLE, "It's not just good...")
    show nicole sc7 flirt:
        leftcenterstage

    $ setWait(88.009,90.17)
    $ speak(NICOLE, "...It's on its best behavior.")
    stop ambient fadeout 1.5
    jump scene_S0038

label scene_S0038:
    show black onlayer screens with Pause(1.3):
        alpha 0.2
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0038.mp3")
    play ambient "audio/Ambience/Doorstep_Ambience.mp3" fadein 1
    scene driveway jeffery
    show jecka sc10 sad:
        off_left
        xzoom -1
        linear 1 leftmidstage
    $ setWait(0.038,2.248)
    $ speak(JECKA, "I can hear her playlist blasting from here.")
    $ setWait(2.248,4.375)
    $ speak(JECKA, "What the hell is she doing with him??")

    show jecka sc10 sad:
        leftmidstage
        xzoom -1
        linear 4.2 off_right

    $ setWait(4.375,6.336)
    $ speak(JECKA, "Hope I'm not too late.")
    $ setWait(6.336,8.88)
    $ speak(JECKA, "God that Chick-Fil-A drive thru took so long...")
    stop ambient fadeout 1.5
    jump scene_S0039

label scene_S0039:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.2
    $ setVoiceTrack("audio/Scenes/0039.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3" fadein 1
    scene bedroom jeffery night
    show nicole sc7:
        rightmidstage
        xzoom -1
    $ setWait(0.005,1.715)
    $ speak(NICOLE, "God this party sucks...")
    $ setWait(1.715,3.383)
    $ speak(NICOLE, "Is Rob & Big still on TV?")
    show jecka sc10 angry:
        off_right
        linear 0.3 rightstage

    $ setWait(3.383,4.218)
    $ speak(JECKA, "What're you--")
    hide black onlayer screens
    hide jecka sc10
    hide nicole sc7
    $ csbox = True
    scene cut0039a
    $ setWait(4.218,5.219)
    $ speak(JECKA, "Oh my god!!")
    $ setWait(5.219,6.345)
    $ speak(NICOLE, "How'd you know I was here?")
    $ setWait(6.345,8.096)
    $ speak(JECKA, "Why is he on the floor!?")
    $ setWait(8.096,9.014)
    $ speak(NICOLE, "He just passed out.")
    $ setWait(9.014,10.39)
    $ speak(JECKA, "From fuckin' what??")
    $ setWait(10.39,13.101)
    $ speak(NICOLE, "I don't know I got bored, he just took anything I gave him.")
    $ setWait(13.101,14.603)
    $ speak(JECKA, "He's not even breathing!")
    $ setWait(14.603,16.48)
    $ speak(NICOLE, "Yeah rum and ambien'll do that.")
    $ setWait(16.48,19.024)
    $ speak(JECKA, "You had him drink rum with ambien??")
    $ setWait(19.024,20.442)
    $ speak(NICOLE, "Nah he had xanax too.")
    $ setWait(20.442,22.152)
    $ speak(JECKA, "Were you trying to fucking kill him!?")
    $ setWait(22.152,24.488)
    $ speak(NICOLE, "I was trying to have a good time, you gotta mellow out.")
    $ setWait(24.488,27.491)
    $ speak(JECKA, "Nicole look at--ugh...")
    $ setWait(27.491,29.201)
    $ speak(JECKA, "He's not...")
    $ setWait(29.201,31.87)
    $ speak(JECKA, "I can't believe you...")
    $ setWait(31.87,34.289)
    $ speak(NICOLE, "What, you suddenly like him now?")
    $ setWait(34.289,36.375)
    $ speak(JECKA, "He was...")
    $ setWait(36.375,38.293)
    $ speak(NICOLE, "He was what?")
    $ setWait(38.293,43.465)
    $ speak(JECKA, "He was my best client, Nicole! If he's actually dead that's 800 dollars a month just gone!")
    $ setWait(43.465,45.133)
    $ speak(NICOLE, "I thought I was a sociopath.")
    $ setWait(45.133,46.635)
    $ speak(JECKA, "How long has been like this?")
    $ setWait(46.635,48.262)
    $ speak(NICOLE, "I don't know like 20 minutes.")
    scene cut0039b
    $ setWait(48.262,51.223)
    $ speak(JECKA, "I'm calling 911, they might be able to still save him!")
    scene cut0039a
    $ setWait(51.223,52.307)
    $ speak(NICOLE, "Are you fucking crazy??")
    $ setWait(52.307,53.976)
    $ speak(JECKA, "Are you??")
    scene cut0039b
    $ setWait(53.976,57.104)
    $ speak(NICOLE, "If you call 911 paramedics are gonna show up.")
    $ setWait(57.104,60.023)
    $ speak(NICOLE, "If paramedics show up they're gonna ask how this happened.")
    $ setWait(60.023,66.488)
    $ speak(NICOLE, "If they ask how this happened, I'm gonna have to lie, then they'll resuscitate Jeffery who's gonna have a totally different story!")
    scene cut0039a
    $ setWait(66.488,69.741)
    $ speak(JECKA, "Okay well let's worry about that later, he's gonna die if we just stand here!")
    $ setWait(69.741,71.868)
    $ speak(NICOLE, "I'm gonna go to jail if he doesn't die!")
    $ setWait(71.868,74.663)
    $ speak(JECKA, "So you wanna just stand here while his body fuckin' rots away?!")
    $ setWait(74.663,80.419)
    $ speak(NICOLE, "Yeah because then we can say we found him like this, so we don't go to jail when Jeffery wakes up to say otherwise.")
    $ setWait(80.419,82.254)
    $ speak(JECKA, "What do you mean \"we\"? You did this!")
    $ setWait(82.254,86.466)
    $ speak(NICOLE, "With your xanax prescription so it's gonna look like we both did it!")
    $ setWait(86.466,87.718)
    $ speak(JECKA, "...Are you serious?")
    $ setWait(87.718,94.141)
    $ speak(NICOLE, "So if I'm going down for some future pedophile who wants to literally fuck his mom, you're going with me!")
    $ setWait(94.141,97.561)
    $ speak(JECKA, "No, but I gave you that for...")
    scene cut0039b
    $ setWait(97.561,99.313)
    $ speak(NICOLE, "Close your phone.")

    $ setWait(99.313,100.647)
    $ speak(JECKA, "But...")
    $ setWait(100.647,102.316)
    $ speak(JECKA, "...800 a month--")
    $ setWait(102.316,106.57)
    $ speak(NICOLE, "Close your phone before I fucking break it...")
    show cut0039c:
        alpha 0.0
        pause 1
        linear 0.3 alpha 1.0

    $ setWait(106.57,108.822)
    $ speak(JECKA, "Unh...")
    hide cut0039c
    scene cut0039a
    stop ambient fadeout 9.5
    show black onlayer screens:
        alpha 0.0
        linear 8.3 alpha 1.0
    $ setWait(108.822,116.997)
    $ speak(NICOLE, "...")
    jump end_S0040

label end_S0040:

    show black onlayer screens with Pause(2):
        alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    scene black

    if "end_0040" not in persistent.endings:
        $ persistent.endings.append("end_0040")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    $ renpy.movie_cutscene("cs0040.webm")

    return

label scene_S0041:
    $ setVoiceTrack("audio/Scenes/0041.mp3")
    scene mall int
    show jecka sc6 angry:
        leftmidstage
        xzoom -1

    show jeffery sc1:
        centerstage
    $ setWait(0.042,1.794)
    $ speak(JECKA, "Wait-- no, fuck you!")
    show jeffery sc1 blush:
        centerstage
    $ setWait(1.794,2.795)
    $ speak(JEFFERY, "Hey c'mon!")
    $ setWait(2.795,5.881)
    $ speak(JECKA, "You think random girls in public wanna indulge your foot fetish?")
    $ setWait(5.881,9.218)
    $ speak(JEFFERY, "It's not a fetish! Stop trying to stigmatize it that way!")
    $ setWait(9.218,14.765)
    $ speak(JECKA, "You wanna pay girls money to step on you, I don't think anything's needed such little trying to be stigmatized.")
    show jeffery sc1 angry:
        centerstage
    $ setWait(14.765,17.184)
    $ speak(JEFFERY, "You're making it sexual, it's not like that!")

    $ setWait(17.184,19.311)
    $ speak(JECKA, "Oh so you have guys step on you too?")
    show jeffery sc1:
        centerstage

    $ setWait(19.311,21.48)
    $ speak(JEFFERY, "No, I only like it from girls.")
    $ setWait(21.48,24.733)
    $ speak(JECKA, "So if sex is involved, it's sexual you fuckin' freak!")
    show jeffery sc1 blush:
        centerstage

    $ setWait(24.733,30.156)
    $ speak(JEFFERY, "I swear it's not! I just like the warm feet of girls cause it's comforting.")
    $ setWait(30.156,33.284)
    $ speak(JEFFERY, "Like they're taking care of me if they were my mommy.")
    show jecka sc6:
        leftmidstage
        xzoom -1
    $ setWait(33.284,36.412)
    $ speak(JECKA, "Oh... Well when you put it that way it sounds normal.")
    $ setWait(36.412,38.289)
    $ speak(JEFFERY, "Really? So you wanna try--")
    $ setWait(38.289,40.624)
    $ speak(JECKA, "Fuck off and hang yourself in a Burger King playground.")

    show jeffery sc1 angry:
        centerstage

    $ setWait(40.624,42.042)
    $ speak(JEFFERY, "Rgh! I don't get it!")
    $ setWait(42.042,42.918)
    $ speak(JECKA, "Don't pull out a gun.")
    $ setWait(42.918,48.34)
    $ speak(JEFFERY, "I just try to be nice to girls by telling them how beautiful they are and they just throw it back in my face.")
    $ setWait(48.34,49.967)
    $ speak(JECKA, "Yeah, you know why?")
    show jeffery sc1:
        centerstage
    $ setWait(49.967,55.973)
    $ speak(JEFFERY, "Oh... I guess because it's inappropriate to go up to people in public with something so personal.")

    show jecka sc6 angry:
        leftmidstage
        xzoom -1

    $ setWait(55.973,61.145)
    $ speak(JECKA, "No, it's because you're ugly as shit. You dress like you're from a VHS tape that teaches kids how to read.")
    $ setWait(61.145,63.063)
    $ speak(JEFFERY, "So all you care about is looks?")
    $ setWait(63.063,64.732)
    $ speak(JECKA, "Y'know what, actually yeah.")
    $ setWait(64.732,68.402)
    $ speak(JEFFERY, "But there's gotta be more to people than that. Like kindness of heart.")
    $ setWait(68.402,74.617)
    $ speak(JECKA, "No, cause why would I date a guy for his kind heart while trying not to throw up while he fucks me on his broke-ass Sleepy's mattress.")
    show jeffery sc1 angry:
        centerstage

    $ setWait(74.617,78.162)
    $ speak(JEFFERY, "Ugh- I didn't even wanna date! I just wanted your feet...")
    show jecka sc6:
        leftmidstage
        xzoom -1
    $ setWait(78.162,82.166)
    $ speak(JECKA, "Damn even body parts reject you. Let's hope you won't need a kidney in 5 years.")
    $ setWait(82.166,86.587)
    $ speak(JEFFERY, "It's times like this where I wonder what's the point of even staying alive.")
    $ setWait(86.587,88.589)
    $ speak(JECKA, "For you? None. End it.")
    show jeffery sc1:
        centerstage
    $ setWait(88.589,94.929)
    $ speak(JEFFERY, "Well I won't argue anymore. I just hope that one day you'll come around to the idea of foot worship.")
    $ setWait(94.929,97.973)
    $ speak(JECKA, "Sorry I don't fuck with feet, I use the metric system.")
    show jeffery sc1 smile:
        centerstage


    $ setWait(97.973,101.477)
    $ speak(JEFFERY, "Actually, did you hear this article about the Japanese use of--")

    show jeffery sc1:
        centerstage

    show jecka sc6:
        leftmidstage
        xzoom 1
        linear 1.5 off_left

    $ setWait(101.477,103.187)
    $ speak(JECKA, "I don't care, I'm going to work.")

    stop ambient fadeout 1.5
    jump scene_S0042

label scene_S0042:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0042.mp3")
    play ambient "audio/Ambience/Diner_Ambience.mp3" fadein 1
    scene diner int
    show jecka sc6 sad:
        off_left
        xzoom -1
        linear 1.3 leftmidstage

    $ setWait(0.047,2.258)
    $ speak(JECKA, "Okay, I think I'm on time!")
    show emily sc4:
        off_right
        linear 2 rightcenterstage
    $ setWait(2.258,4.093)
    $ speak(EMILY, "What're you doing here?")
    $ setWait(4.093,8.305)
    $ speak(JECKA, "I'm working today, aren't I? Fuck did I get Tuesday mixed with Thursday again?")
    $ setWait(8.305,10.015)
    $ speak(EMILY, "Hate to break it to ya but--")
    show jecka sc6 angry:
        leftmidstage
        xzoom -1

    $ setWait(10.015,12.893)
    $ speak(JECKA, "Why don't they rename Thursday to something good like Chick-Fil-A Day??")
    show emily sc4 angry:
        rightcenterstage

    $ setWait(12.893,14.436)
    $ speak(EMILY, "Bitch you got fired!")
    show jecka sc6 surprised:
        leftmidstage
        xzoom -1
    $ setWait(14.436,15.145)
    $ speak(JECKA, "No way.")
    $ setWait(15.145,19.608)
    $ speak(EMILY, "Yeah way, the manager got mad that you pulled away when he leaned in to smell your hair last week.")
    $ setWait(19.608,23.07)
    $ speak(JECKA, "He fired me over that? Isn't that like workplace harassment or something?")
    $ setWait(23.07,25.531)
    $ speak(EMILY, "Not anymore, you don't work here.")
    show jecka sc6:
        leftmidstage
        xzoom -1

    $ setWait(25.531,27.408)
    $ speak(JECKA, "Is that how that...")
    show jecka sc6 angry:
        leftmidstage
        xzoom -1
    $ setWait(27.408,28.576)
    $ speak(JECKA, "Was that really it?")
    show emily sc4 upset:
        rightcenterstage

    $ setWait(28.576,34.039)
    $ speak(EMILY, "No he bitched about how you give out too many napkins to old ladies ordering iced tea and nothing else.")
    $ setWait(34.039,36.458)
    $ speak(JECKA, "But he told me customer service is my first priority!")
    $ setWait(36.458,38.21)
    $ speak(EMILY, "Yeah but saving money is his.")
    $ setWait(38.21,41.088)
    $ speak(JECKA, "Fuckin' what money? He steals Chipotle napkins to use here!")
    $ setWait(41.088,44.633)
    $ speak(EMILY, "He said it costs at least $1.50 in gas to drive over there.")
    $ setWait(44.633,46.719)
    $ speak(JECKA, "Y'know what? Fuck this job, this job sucks.")
    $ setWait(46.719,48.846)
    $ speak(EMILY, "Dude honestly you just sound mad that you got fired.")
    $ setWait(48.846,52.224)
    $ speak(JECKA, "Shut the fuck up, this is literally Stockholm syndrome.")
    show emily sc4:
        rightcenterstage

    $ setWait(52.224,55.936)
    $ speak(EMILY, "What's Stockholm syndrome? Is that a cybergoth band?")
    $ setWait(55.936,58.814)
    $ speak(JECKA, "I don't know I just sound smart when I say it. I'm not in college yet.")
    show emily sc4 upset:
        rightcenterstage
        pause 1.8
        xzoom -1
        linear 2.2 off_right

    $ setWait(58.814,63.277)
    $ speak(EMILY, "Okay well you go to college and I'll just keep making tips.")
    show jecka sc6 angry:
        xzoom 1
        leftmidstage
        linear 2.3 off_left

    $ setWait(63.277,65.738)
    $ speak(JECKA, "Fuck this place, I got another job lined up anyway.")
    stop ambient fadeout 1.5
    jump scene_S0043

label scene_S0043:
    show black onlayer screens with Pause(1.8):
        alpha 0.0
        linear 1.6 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0043.mp3")
    play ambient "audio/Ambience/FYE_NoMusic_Ambience.mp3" fadein 1
    scene fye

    show jecka fye:
        leftcenterstage
        xzoom -1

    show kelly fye:
        rightcenterstage

    $ setWait(0.044,3.59)
    $ speak(KELLY, "I'm actually like so stoked we get to work here together.")
    $ setWait(3.59,8.011)
    $ speak(JECKA, "I don't know.. I'm pretty sure I got drunk and made out with you at your party so it's kinda awkward.")
    show kelly fye sad:
        rightcenterstage

    $ setWait(8.011,9.262)
    $ speak(KELLY, "Wait you were drunk??")
    show jecka fye angry:
        leftcenterstage
        xzoom -1
    $ setWait(9.262,11.097)
    $ speak(JECKA, "Fuck-- see this is what I meant.")
    show kelly fye angry:
        rightcenterstage
    $ setWait(11.097,14.642)
    $ speak(KELLY, "Well I'm not gay, I just wanted attention so we're even.")
    show jecka fye:
        leftcenterstage
        xzoom -1
    $ setWait(14.642,16.436)
    $ speak(JECKA, "I mean yeah whatever works for ya.")
    show kelly fye:
        rightcenterstage
    $ setWait(16.436,21.816)
    $ speak(KELLY, "So now working for this place requires a lot of patience and an overall love of media.")
    $ setWait(21.816,23.568)
    $ speak(JECKA, "Do we really have to love it?")
    $ setWait(23.568,25.445)
    $ speak(KELLY, "Well why else would you work here?")
    $ setWait(25.445,27.697)
    $ speak(JECKA, "For a fucking paycheck, I love money bitch.")
    $ setWait(27.697,31.784)
    $ speak(KELLY, "I do too, but you gotta love other things. Like the customer.")
    show kylar sc2 smile:
        off_right
        linear 4 rightmidstage

    $ setWait(31.784,33.411)
    $ speak(JECKA, "Why would I love the customer?")
    $ setWait(33.411,35.455)
    $ speak(KELLY, "Oh- one's walking in right now. Lemme show ya.")
    show kelly fye:
        rightcenterstage
        xzoom -1

    $ setWait(35.455,38.666)
    $ speak(KYLAR, "Sup bitch, you got any Crank Yankers DVDs?")
    $ setWait(38.666,45.506)
    $ speak(KELLY, "Uh.. Hi! Yeah um, not sure if we have Crank Yankers but I could look on the computer.")
    $ setWait(45.506,48.968)
    $ speak(KYLAR, "Nah that's okay, I can look around. Maybe pick up some bitches and shit.")
    $ setWait(48.968,50.595)
    $ speak(KELLY, "Oh yeah give our showroom a look.")
    $ setWait(50.595,51.888)
    $ speak(KYLAR, "I'll give you this dick, bitch.")
    $ setWait(51.888,58.311)
    $ speak(KELLY, "And Crank Yankers.. Super funny, I remember seeing it on Comedy Central once at 2 in the morning.")
    $ setWait(58.311,60.897)
    $ speak(KYLAR, "You like that show too? Wow you're really hot.")
    show kelly fye sad:
        rightcenterstage
        xzoom -1

    $ setWait(60.897,62.899)
    $ speak(KELLY, "Uh... Hahahaha.")
    $ setWait(62.899,63.941)
    $ speak(KYLAR, "Damn I'm so funny.")
    show jecka fye angry:
        leftcenterstage
        xzoom -1

    $ setWait(63.941,65.526)
    $ speak(JECKA, "Yeah she thought it was funny.")
    $ setWait(65.526,67.612)
    $ speak(KYLAR, "So you wanna go out later?")
    $ setWait(67.612,69.405)
    $ speak(KELLY, "Go-- With you?")
    $ setWait(69.405,72.659)
    $ speak(KYLAR, "Yeah there's a pretty sick motorcross rally in town.")
    $ setWait(72.659,74.827)
    $ speak(KELLY, "Uh... I'm at work...")
    show kylar sc2:
        rightmidstage
    $ setWait(74.827,77.246)
    $ speak(KYLAR, "Yeah no I said later.")
    $ setWait(77.246,79.624)
    $ speak(KELLY, "Why don't we look for that Crank Yankers DVD?")
    show kylar sc2 angry:
        rightmidstage
        pause 1.2
        xzoom -1
        linear 1.8 off_right

    $ setWait(79.624,83.753)
    $ speak(KYLAR, "You're a fucking bitch I hope you get drugged and kidnapped.")
    show jecka fye:
        leftcenterstage
        xzoom -1
    $ setWait(83.753,85.421)
    $ speak(JECKA, "So I'm supposed to love the customer?")
    show kelly fye:
        rightcenterstage
        xzoom 1

    $ setWait(85.421,89.509)
    $ speak(KELLY, "Look this is retail, every now and then you get a few bad apples.")
    show mallcop:
        off_right
        linear 2 rightmidstage

    $ setWait(89.509,90.802)
    $ speak(MALLCOP, "Hello there, ladies.")
    show kelly fye:
        xzoom -1

    $ setWait(90.802,93.054)
    $ speak(KELLY, "Hi, welcome to FYE.")
    $ setWait(93.054,96.599)
    $ speak(MALLCOP, "Everything all secure here? No shoplifting, right?")
    $ setWait(96.599,99.018)
    $ speak(KELLY, "Uh nope, none so far today.")
    $ setWait(99.018,101.062)
    $ speak(MALLCOP, "And who might this fresh face be?")
    show kelly fye:
        xzoom 1
        pause 1.3
        xzoom -1

    $ setWait(101.062,104.816)
    $ speak(KELLY, "This is Jecka, she's our newest FYE sales rep.")
    $ setWait(104.816,105.566)
    $ speak(JECKA, "Hi.")
    $ setWait(105.566,110.947)
    $ speak(MALLCOP, "Well good luck working alongside us at the mall. You're very beautiful by the way.")
    $ setWait(110.947,112.573)
    $ speak(JECKA, "Yeah love hearing that at work.")
    $ setWait(112.573,115.326)
    $ speak(KELLY, "Is there anything else we can help you with?")
    $ setWait(115.326,120.415)
    $ speak(MALLCOP, "Actually yes! I was looking for a... certain product.")
    $ setWait(120.415,122.542)
    $ speak(KELLY, "Oh sure yeah, what's it called?")
    $ setWait(122.542,125.92)
    $ speak(MALLCOP, "A little bit of that special spectacle.")
    $ setWait(125.92,127.463)
    $ speak(KELLY, "Is that a band? Lemme look it up.")
    $ setWait(127.463,135.263)
    $ speak(MALLCOP, "No no no, you know about that mild style? That mild mild? A code 15- UN?")
    $ setWait(135.263,137.181)
    $ speak(JECKA, "Do you think we're under cover or something?")
    show mallcop:
        pause 0.4
        xzoom -1
        pause 0.3
        xzoom 1
    $ setWait(137.181,140.393)
    $ speak(MALLCOP, "What? Uh- Yeah you're not undercovers?")
    $ setWait(140.393,143.938)
    $ speak(KELLY, "Nope just regular FYE girls.")
    $ setWait(143.938,147.316)
    $ speak(MALLCOP, "My mistake, girls. Let me know if there's any theft.")
    $ setWait(147.316,148.276)
    $ speak(KELLY, "Will do.")
    show mallcop:
        xzoom -1
        rightmidstage
        linear 2 off_right

    $ setWait(148.276,152.029)
    $ speak(MALLCOP, "Fuckin' hate my job! They always tell me the wrong shit!")
    show jecka fye sad:
        leftcenterstage
        xzoom -1

    $ setWait(152.029,154.115)
    $ speak(JECKA, "What's the coherence rate of people shopping here?")
    show kelly fye:
        xzoom 1
    $ setWait(154.115,157.952)
    $ speak(KELLY, "Well they're buying CDs in 2009, they can't be the brightest.")
    stop ambient fadeout 1.5
    jump scene_S0044

label scene_S0044:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0044.mp3")
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1
    scene mall int
    show jecka fye:
        off_left
        xzoom -1
        linear 2.8 leftcenterstage
    $ setWait(0.039,2.708)
    $ speak(JECKA, "I wonder what un-burnt Domino's tastes like.")
    show mallcop:
        off_right
        linear 1.2 rightcenterstage

    $ setWait(2.708,5.378)
    $ speak(MALLCOP, "Ah hello again.")
    $ setWait(5.378,7.004)
    $ speak(JECKA, "Yeah.")
    $ setWait(7.004,8.714)
    $ speak(MALLCOP, "Is everything okay?")
    $ setWait(8.714,10.8)
    $ speak(JECKA, "I'm not at work so I don't have to be nice to you.")
    $ setWait(10.8,15.346)
    $ speak(MALLCOP, "Well wait before you go, just don't worry about what happened earlier.")
    $ setWait(15.346,16.472)
    $ speak(JECKA, "What do you mean?")
    $ setWait(16.472,18.015)
    $ speak(MALLCOP, "Exactly!")
    show jecka fye sad:
        leftcenterstage
        xzoom -1
    $ setWait(18.015,19.517)
    $ speak(JECKA, "What's going on?")
    $ setWait(19.517,23.396)
    $ speak(MALLCOP, "Just don't ask questions. Very serious operation.")
    $ setWait(23.396,26.315)
    $ speak(JECKA, "Are you gonna assassinate Obama? Oh my god I knew it!")
    $ setWait(26.315,30.319)
    $ speak(MALLCOP, "Whoa whoa! We don't have any plans for that...")
    $ setWait(30.319,30.903)
    $ speak(JECKA, "...Yet?")
    $ setWait(30.903,32.28)
    $ speak(MALLCOP, "Trying to get fresh with me?")

    show jecka fye:
        leftcenterstage
        xzoom -1

    $ setWait(32.28,33.281)
    $ speak(JECKA, "No I'm frozen.")
    $ setWait(33.281,36.576)
    $ speak(MALLCOP, "I will throw you off a 3-story ledge you fucking bitch!")
    show jecka fye surprised:
        xzoom 1
        leftcenterstage
        linear 0.5 off_left

    $ setWait(36.576,39.12)
    $ speak(JECKA, "Holy shit don't hurt me!")
    $ setWait(39.12,42.748)
    $ speak(MALLCOP, "Yeah, I did a good thing. The people need me.")
    show mallcop:
        xzoom -1
        rightcenterstage
        linear 4.5 off_right

    $ setWait(42.748,47.295)
    $ speak(MALLCOP, "The best thing about Obama's election is I can vote against him twice.")
    stop ambient fadeout 1.5
    jump scene_S0045

label scene_S0045:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka night with Pause(2.671):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.671 zoom 1.05 truecenter
    $ setVoiceTrack("audio/Scenes/0045.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene livingroom jecka
    show jecka fye:
        off_left
        xzoom -1
        linear 1.7 leftmidstage

    $ setWait(2.671,4.84)
    $ speak(JECKA, "I wonder if Britney's hair grew back.")
    show dad polo smile:
        off_right
        linear 2 rightmidstage

    $ setWait(4.84,7.884)
    $ speak(DAD, "Hello Jessica, have a nice day at work?")
    show jecka fye angry:
        leftmidstage
        xzoom -1

    $ setWait(7.884,10.095)
    $ speak(JECKA, "Fuck I thought I was gonna have the house to myself.")
    $ setWait(10.095,13.181)
    $ speak(DAD, "I was actually just stepping out with a new friend of mine.")
    $ setWait(13.181,15.934)
    $ speak(JECKA, "Dad, you're over 40, people don't make friends over 40.")
    $ setWait(15.934,18.77)
    $ speak(DAD, "Would you prefer the phrase \"new step-mom\"?")
    show jecka fye sad:
        leftmidstage
        xzoom -1

    $ setWait(18.77,20.355)
    $ speak(JECKA, "You're already dating someone?")
    show dad polo caring:
        rightmidstage

    $ setWait(20.355,27.154)
    $ speak(DAD, "Now darling, just because I'm seeing someone doesn't mean it's going to replace your filthy money pit mother.")
    show jecka fye:
        leftmidstage

    $ setWait(27.154,29.197)
    $ speak(JECKA, "Uh yeah that makes me feel better..")
    show dad polo:
        rightmidstage

    $ setWait(29.197,30.699)
    $ speak(DAD, "Would you like to meet her?")
    $ setWait(30.699,31.533)
    $ speak(JECKA, "Meter what?")
    $ setWait(31.533,34.244)
    $ speak(DAD, "No, meet. Her.")
    $ setWait(34.244,35.746)
    $ speak(JECKA, "Oh, not really.")
    $ setWait(35.746,37.789)
    $ speak(DAD, "Don't be so immature.")
    show dad polo smile:
        rightmidstage
        xzoom -1
        linear 1.5 rightstage

    $ setWait(37.789,40)
    $ speak(DAD, "Emmy! You can come out now!")
    show dad polo smile:
        rightstage
        xzoom 1
        linear 1.3 rightcenterstage

    $ setWait(40,41.585)
    $ speak(JECKA, "Trophy wife named Emmy..")
    show emily sc1 upset:
        off_right
        linear 1.7 rightmidstage

    $ setWait(41.585,43.754)
    $ speak(EMILY, "Oh fuck, she's your daughter?")
    show jecka fye surprised:
        leftmidstage
        xzoom -1
        linear 0.5 leftcenterstage

    $ setWait(43.754,46.798)
    $ speak(JECKA, "Emily?? A-Are we like Brady Bunch sisters? Where's your Mom?")
    $ setWait(46.798,51.636)
    $ speak(DAD, "Jessica I'd like you to meet your new step-mother Emily.")
    show jecka fye sad:
        leftcenterstage
        xzoom -1

    $ setWait(51.636,54.222)
    $ speak(JECKA, "Oh shit I wanna kill myself.")
    $ setWait(54.222,56.349)
    $ speak(EMILY, "And I thought the sex was awkward before.")
    show jecka fye angry:
        leftcenterstage
        xzoom -1

    $ setWait(56.349,58.268)
    $ speak(JECKA, "Why are you literally fucking my dad??")
    show emily sc1 angry:
        rightmidstage

    $ setWait(58.268,61.271)
    $ speak(EMILY, "I didn't know he was your dad! He kept calling his daughter \"Jessica\"!")
    $ setWait(61.271,65.484)
    $ speak(JECKA, "Bitch that's what Jecka's short for! I thought you said the older guy you were seeing was super cool!?")
    $ setWait(65.484,69.112)
    $ speak(EMILY, "Yeah cause he spends a lot of money on me, what's not super cool about that?")
    $ setWait(69.112,72.783)
    $ speak(JECKA, "Dad if you got all this money to spend on her why the fuck did I have to get a job!?")
    show dad polo caring:
        rightcenterstage

    $ setWait(72.783,75.16)
    $ speak(DAD, "There's only so much to go around, dear.")
    $ setWait(75.16,76.87)
    $ speak(EMILY, "Yeah don't hate cause I'm prettier than you.")
    $ setWait(76.87,79.414)
    $ speak(JECKA, "You're not prettier, you're just less related than me!")
    show emily sc1:
        rightmidstage

    $ setWait(79.414,82.417)
    $ speak(EMILY, "I know it's kinda weird but like, what about your Dad's happiness.")
    $ setWait(82.417,83.376)
    $ speak(JECKA, "Fuck my dad!")
    show emily sc1 upset:
        rightmidstage

    $ setWait(83.376,84.669)
    $ speak(EMILY, "Yeah did that, what else?")
    $ setWait(84.669,93.929)
    $ speak(DAD, "Listen, you all graduated a couple months ago, she's a consenting adult, and with your mother out of the picture I can date whoever I want.")
    show jecka fye sad:
        leftcenterstage

    $ setWait(93.929,96.89)
    $ speak(JECKA, "Ugh... Well at least you're not a pedophile.")
    $ setWait(96.89,98.183)
    $ speak(DAD, "See Jessica?")
    show dad polo smile:
        rightcenterstage

    $ setWait(98.183,100.185)
    $ speak(DAD, "Now who's Daddy's girl?")

    show emily sc1 smile:
        rightmidstage

    show dad polo caring:
        rightcenterstage
        pause 0.6
        xzoom -1

    $ setWait(100.185,101.269)
    $ speak(JECKAEMILY, "I am...")

    show dad polo caring:
        rightcenterstage
        xzoom 1

    show jecka fye angry:
        leftcenterstage

    $ setWait(101.269,103.021)
    $ speak(JECKA, "...Ohhh gay.")
    show emily sc1 angry:
        rightmidstage

    $ setWait(103.021,105.065)
    $ speak(EMILY, "You're gay, and jealous!")
    $ setWait(105.065,111.53)
    $ speak(JECKA, "If screwing some college-age girl fucked up on drugs and reeking of cigarettes is something to be jealous of...")
    show dad polo:
        rightcenterstage

    $ setWait(111.53,113.323)
    $ speak(DAD, "...Well.. Well yeah.")
    stop ambient fadeout 1.5
    jump scene_S0046

label scene_S0046:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0046.mp3")
    play ambient "audio/Ambience/FYE_NoMusic_Ambience.mp3" fadein 1
    scene fye
    show jecka fye:
        leftmidstage
        xzoom -1

    show crispin sc2:
        leftcenterstage

    $ setWait(0.036,5.958)
    $ speak(CRISPIN, "Yeah so... I don't really know... I guess it's like kinda all up to me, right?")
    $ setWait(5.958,7.668)
    $ speak(JECKA, "Uh huh...")
    $ setWait(7.668,13.424)
    $ speak(CRISPIN, "But uh- Oh your undershirt is shortsleeve, is that like a new kind of FYE uniform?")
    $ setWait(13.424,14.467)
    $ speak(JECKA, "A what?")
    $ setWait(14.467,19.263)
    $ speak(CRISPIN, "Cause y'know they're like, usually long sleeve. Was that a choice?")
    $ setWait(19.263,21.474)
    $ speak(JECKA, "Um, it's just what they had.")
    show crispin sc2 smile:
        leftcenterstage

    $ setWait(21.474,24.727)
    $ speak(CRISPIN, "Oh cool cool, how do you like it compared to the other ones?")
    $ setWait(24.727,27.188)
    $ speak(JECKA, "What does this have to do with what DVD you're looking for?")
    $ setWait(27.188,31.15)
    $ speak(CRISPIN, "Ah sorry yeah I just got distracted cause like...")
    $ setWait(31.15,34.07)
    $ speak(CRISPIN, "...Like I don't know your outfit's kinda cute like that.")
    show jecka fye smile:
        leftmidstage
        xzoom -1

    $ setWait(34.07,36.28)
    $ speak(JECKA, "Really? Hey do you want a job here?")
    $ setWait(36.28,38.699)
    $ speak(CRISPIN, "A job? Why? Do you think I'd be good at this?")
    show jecka fye:
        leftmidstage
        xzoom -1

    $ setWait(38.699,44.288)
    $ speak(JECKA, "No I just wanna be able to report workplace sexual harassment for you commenting on my outfit.")
    $ setWait(44.288,47.542)
    $ speak(CRISPIN, "Uh? Ahaha.. You're like hella funny.")
    $ setWait(47.542,50.962)
    $ speak(JECKA, "Yeah... so The Dana Carvey Show boxset?")
    show crispin sc2:
        leftcenterstage

    $ setWait(50.962,56.509)
    $ speak(CRISPIN, "Oh yeah I was thinking about it and... I don't really- yeah maybe I don't want it.")
    $ setWait(56.509,59.554)
    $ speak(JECKA, "Well at least I don't need to go in the back and pretend to look for it.")

    show crispin sc2 smile:
        xzoom -1
        leftcenterstage
        linear 3.2 off_right

    $ setWait(59.554,63.391)
    $ speak(CRISPIN, "Yeah I'm gonna go to Guitar Center, gonna chat it up.")
    show kelly fye:
        xzoom -1
        off_left
        linear 1.8 leftstage

    $ setWait(63.391,66.018)
    $ speak(KELLY, "Why would he want The Dana Carvey Show?")
    show jecka fye:
        xzoom 1

    $ setWait(66.018,68.146)
    $ speak(JECKA, "I think he just wanted a girl to talk to.")
    $ setWait(68.146,71.607)
    $ speak(KELLY, "That reminds me, did you ever see Master Of Diguise?")
    $ setWait(71.607,72.859)
    $ speak(JECKA, "Maybe once?")
    $ setWait(72.859,74.152)
    $ speak(KELLY, "Remember the turtle guy?")
    $ setWait(74.152,75.611)
    $ speak(JECKA, "Yeah the turtle club.")
    $ setWait(75.611,80.116)
    $ speak(KELLY, "Every Wednesday some fucked up weird guy comes in here who looks exactly like that.")
    $ setWait(80.116,83.494)
    $ speak(JECKA, "Can't believe I started on Thursday, guess I'll wait 'till next week.")
    $ setWait(83.494,88.583)
    $ speak(KELLY, "He comes in asking for cigarettes, like this is a fucking DVD store what's wrong with you?")
    show jecka fye smile:
        leftmidstage
        xzoom 1
    $ setWait(88.583,89.959)
    $ speak(JECKA, "That'd actually be cool.")
    $ setWait(89.959,90.626)
    $ speak(KELLY, "What would?")
    $ setWait(90.626,93.713)
    $ speak(JECKA, "A store that just sells bargain bin movies and alcohol.")
    $ setWait(93.713,96.549)
    $ speak(KELLY, "That's true. Cause when you're fucked up every movie's good.")
    $ setWait(96.549,99.552)
    $ speak(JECKA, "Yeah I'm basically a genius, by the way is my shift over?")
    $ setWait(99.552,101.345)
    $ speak(KELLY, "Oh yeah, you can go now.")
    show jecka fye:
        leftmidstage

    $ setWait(101.345,103.89)
    $ speak(JECKA, "But isn't it pay day? Can I have my check now?")
    show kelly fye sad:
        xzoom -1
        leftstage

    $ setWait(103.89,107.935)
    $ speak(KELLY, "So technically yes but there's a little problem.")
    show jecka fye angry:
        leftmidstage

    $ setWait(107.935,109.187)
    $ speak(JECKA, "Bitch don't make me choke you.")
    $ setWait(109.187,111.272)
    $ speak(KELLY, "Chill out, do you need anger management?")
    $ setWait(111.272,113.149)
    $ speak(JECKA, "I need my fuckin' money, slut.")
    $ setWait(113.149,114.609)
    $ speak(KELLY, "I'm not getting paid either!")
    $ setWait(114.609,115.818)
    $ speak(JECKA, "Well what's going on?")
    $ setWait(115.818,119.489)
    $ speak(KELLY, "The computers went down an hour ago totally out of nowhere.")
    $ setWait(119.489,120.239)
    $ speak(JECKA, "So?")
    $ setWait(120.239,124.535)
    $ speak(KELLY, "So if the computers aren't working we can't log the hours to print our paychecks.")
    $ setWait(124.535,125.62)
    $ speak(JECKA, "Get the manager.")
    show kelly fye angry:
        leftstage
        xzoom -1
    $ setWait(125.62,127.83)
    $ speak(KELLY, "I am the manager, I have a lanyard.")

    show jecka fye surprised:
        leftmidstage

    $ setWait(127.83,129.624)
    $ speak(JECKA, "Oh shit...")
    show jecka fye sad:
        leftmidstage

    $ setWait(129.624,131.792)
    $ speak(JECKA, "...Sorry I called you a bitch and a slut earlier.")
    show kelly fye:
        leftstage
        xzoom -1

    $ setWait(131.792,133.92)
    $ speak(KELLY, "It's okay, I only hate it when men do it.")
    show jecka fye:
        leftmidstage
    $ setWait(133.92,136.589)
    $ speak(JECKA, "Can't you call someone higher to fix the system? Like regional?")
    $ setWait(136.589,141.093)
    $ speak(KELLY, "I called regional, the whole phone line's down. And regional is never down.")
    $ setWait(141.093,143.095)
    $ speak(JECKA, "So who gives a shit just print the checks.")
    show kelly fye sad:
        leftstage
        xzoom -1
        linear 1.2 leftcenterstage
        xzoom 1

    show jecka fye:
        pause 0.9
        xzoom -1

    $ setWait(143.095,144.263)
    $ speak(KELLY, "You don't get it...")
    $ setWait(144.263,151.27)
    $ speak(KELLY, "...All the checks need to be ran by regional. If something's wrong with regional's system, they don't get paid, meaning we don't get paid!")
    $ setWait(151.27,154.524)
    $ speak(JECKA, "There's gotta be another number you can call. Like corporate, right?")
    show kelly fye sad:
        leftcenterstage
        linear 2 off_left

    show jecka fye:
        xzoom -1
        leftmidstage
        pause 1.1
        xzoom 1
        linear 1.9 off_left
    $ setWait(154.524,158.194)
    $ speak(KELLY, "Ugh, let's look in the break room.")
    show jeffery sc3 smile:
        off_right
        linear 5.5 leftcenterstage
    $ setWait(158.194,163.157)
    $ speak(JEFFERY, "I wonder if they have Dude Where's My Car... I like the giant woman at the end...")
    stop ambient fadeout 1.5
    jump scene_S0047

label scene_S0047:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0047.mp3")
    play ambient "audio/Ambience/Breakroom_Ambience.mp3" fadein 1
    scene breakroom
    show jecka fye:
        rightmidstage
        xzoom -1

    show kelly fye:
        leftstage

    $ setWait(0.047,1.924)
    $ speak(JECKA, "Is there anything on those shelves over there?")
    $ setWait(1.924,5.26)
    $ speak(KELLY, "No just fake Justin Timberlake autographs we gave out for an event.")
    $ setWait(5.26,6.303)
    $ speak(JECKA, "Wow that's evil.")
    $ setWait(6.303,8.305)
    $ speak(KELLY, "Yeah fake autos are pretty low.")
    show jecka fye angry:
        rightmidstage
        xzoom 1
    $ setWait(8.305,10.265)
    $ speak(JECKA, "No- who the fuck would want his autograph?")
    show kelly fye:
        xzoom -1
    $ setWait(10.265,11.225)
    $ speak(KELLY, "Tons of people.")
    $ setWait(11.225,12.184)
    $ speak(JECKA, "Like who?")
    show kelly fye:
        leftstage
        xzoom -1
        linear 2 rightcenterstage
    $ setWait(12.184,15.479)
    $ speak(KELLY, "Like girls who only get tattoos when they're drunk on spring break.")
    show jecka fye:
        rightmidstage
        xzoom 1
    $ setWait(15.479,19.149)
    $ speak(JECKA, "Okay whatever just help me get through this cabinet. There's like a hundred folders.")
    $ setWait(19.149,20.401)
    $ speak(KELLY, "What's inside of them?")
    $ setWait(20.401,22.528)
    $ speak(JECKA, "Mostly menus for takeout places.")
    hide jecka fye
    hide kelly fye
    $ csbox = True
    scene cut0047a

    $ setWait(22.528,27.074)
    $ speak(JECKA, "And stuffed away in the back there's these contact forms from an old FYE.")
    $ setWait(27.074,30.327)
    $ speak(KELLY, "Franconia Road... No.")
    $ setWait(30.327,31.453)
    $ speak(JECKA, "No what?")
    $ setWait(31.453,33.539)
    $ speak(KELLY, "That's not an old FYE...")
    scene cut0047b
    $ setWait(33.539,35.416)
    $ speak(KELLY, "That's the other FYE.")
    $ setWait(35.416,36.792)
    $ speak(JECKA, "What other FYE?")
    $ setWait(36.792,40.254)
    $ speak(KELLY, "The adult video branch... For Your Ejaculation.")
    scene cut0047a
    $ setWait(40.254,44.508)
    $ speak(JECKA, "Oh that makes sense it's in the shitty part of Springfield-- well shittier part of Springfield.")
    $ setWait(44.508,47.177)
    $ speak(KELLY, "Yeah, I wonder if they have the same problem as us.")
    $ setWait(47.177,50.472)
    $ speak(JECKA, "I wonder if people still buy porn in 2009.")
    $ setWait(50.472,53.1)
    $ speak(KELLY, "Totally, there's like porn purists.")
    $ setWait(53.1,54.81)
    $ speak(JECKA, "What could be more pure than RedTube?")
    $ setWait(54.81,57.354)
    $ speak(KELLY, "I don't know I don't look into this shit, let's go.")
    $ setWait(57.354,59.022)
    $ speak(JECKA, "Go where? To the porn store?")
    scene breakroom
    show jecka fye:
        rightmidstage

    show kelly fye:
        rightcenterstage
        xzoom -1

    $ setWait(59.022,61.108)
    $ speak(KELLY, "Yeah, better than doing nothing here.")
    $ setWait(61.108,62.359)
    $ speak(JECKA, "Who's gonna cover for us?")
    $ setWait(62.359,64.444)
    $ speak(KELLY, "No one buys shit here anyway, it'll be fine.")
    show jecka fye sad:
        rightmidstage

    $ setWait(64.444,68.031)
    $ speak(JECKA, "But then we have to like.. see the people who shop at porn stores.")
    show kelly fye:
        rightcenterstage
        xzoom -1
        pause 1.5
        linear 2.2 off_right
    $ setWait(68.031,71.326)
    $ speak(KELLY, "I doubt anyone buys stuff there either. It'll be totally empty.")
    show jecka fye:
        xzoom -1
        rightmidstage
        linear 1.8 off_right

    $ setWait(71.326,73.162)
    $ speak(JECKA, "Okay we'll see...")
    stop ambient fadeout 1.5
    jump scene_S0048

label scene_S0048:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show fye ext with Pause(2.672):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.672 zoom 0.54 truecenter
    $ setVoiceTrack("audio/Scenes/0048.mp3")
    $ csbox = False
    play ambient "audio/Ambience/FYE_NoMusic_Ambience.mp3"
    scene adult fye
    show kelly fye:
        off_right
        linear 3 rightcenterstage

    show jecka fye:
        off_farright
        linear 3 rightmidstage
    $ setWait(2.672,4.632)
    $ speak(KELLY, "Why do they get neon lights?")
    $ setWait(4.632,7.135)
    $ speak(JECKA, "It smells like plastic and Nick Nolte in here.")
    show kelly fye:
        xzoom -1
    $ setWait(7.135,8.47)
    $ speak(KELLY, "Who's Nick Nolte?")
    $ setWait(8.47,11.389)
    $ speak(JECKA, "Someone who'd go here just for casual conversation.")
    $ setWait(11.389,13.016)
    $ speak(KELLY, "Where's the other employees?")
    show counselor 3 smile:
        off_left
        xzoom -1
        linear 1.2 leftstage
    $ setWait(13.016,15.602)
    $ speak(COUNSELOR, "Hello girls, feel free to browse around.")
    show kelly fye sad:
        xzoom 1

    show jecka fye surprised:
        rightmidstage

    $ setWait(15.602,16.227)
    $ speak(KELLY, "Oh shit.")
    $ setWait(16.227,19.439)
    $ speak(JECKA, "Aren't you like the school counselor? Why do you work here?")
    show counselor 3 smile:
        leftstage
        xzoom -1
        linear 1.5 leftmidstage

    $ setWait(19.439,30.45)
    $ speak(COUNSELOR, "I thought you looked familiar, though not in those uniforms. There's no school three months out of the year so some of us get summer jobs outside of the school season.")
    $ setWait(30.45,31.951)
    $ speak(KELLY, "I heard you got fired.")
    show jecka fye:
        rightmidstage

    $ setWait(31.951,35.246)
    $ speak(JECKA, "Yeah for doing shit eerily related to this store.")
    $ setWait(35.246,38.833)
    $ speak(COUNSELOR, "Oh nonsensical rumors. Do you girls need help finding anything?")
    $ setWait(38.833,40.46)
    $ speak(JECKA, "We're not actually shopping here.")
    show counselor 3:
        leftmidstage
        xzoom -1
    $ setWait(40.46,45.798)
    $ speak(COUNSELOR, "Oh that's what they all say. Then you're in a failing marriage without the funds for a good divorce attorney.")
    show kelly fye:
        rightcenterstage
        xzoom 1
    $ setWait(45.798,48.343)
    $ speak(KELLY, "We're too pretty to get married-- is your system down?")
    $ setWait(48.343,57.81)
    $ speak(COUNSELOR, "Funny you ask, I was just off in the other room troubleshooting the network. Quite frustrating when your store takes in so much revenue and you can't print a simple paycheck.")
    $ setWait(57.81,61.314)
    $ speak(JECKA, "Revenue?? How do these places stay in business, don't they have RedTube?")
    $ setWait(61.314,67.529)
    $ speak(COUNSELOR, "Poor naive girl. Donning the uniform yet not understanding the business it represents.")
    $ setWait(67.529,69.906)
    $ speak(KELLY, "I'm a manager and I don't even get it.")
    $ setWait(69.906,78.206)
    $ speak(COUNSELOR, "You really think we just offer the slop on RedTube with longer runtimes? We would've gone out of business years ago.")
    show jecka fye angry:
        rightmidstage

    $ setWait(78.206,83.962)
    $ speak(JECKA, "I saw a bitch stretch her whole ass open on RedTube what could you possibly have wilder than that?")
    $ setWait(83.962,92.136)
    $ speak(COUNSELOR, "...Things mere individuals lack the connections to acquire... Acquire discreetly that is.")
    show jecka fye:
        rightmidstage
    $ setWait(92.136,99.143)
    $ speak(COUNSELOR, "Things only a traditional distributor would have the high profile carte-blanche to gain access to.")
    $ setWait(99.143,106.985)
    $ speak(COUNSELOR, "Things that wouldn't stay uploaded for long on even the most unsanctioned of online spaces.")
    $ setWait(106.985,116.119)
    $ speak(COUNSELOR, "The home to these things is an unregistered warehouse where only the most elite of corporate congregate.")
    show jecka fye angry:
        rightmidstage
    $ setWait(116.119,121.124)
    $ speak(JECKA, "How are big titty bitches takin' dick not enough for you?? You seriously need illegal porn!?")
    show kelly fye angry:
        rightcenterstage

    $ setWait(121.124,124.46)
    $ speak(KELLY, "Yeah and this is kinda off topic, what about our paychecks??")
    show counselor 3 smile:
        leftmidstage
        xzoom -1
    $ setWait(124.46,135.43)
    $ speak(COUNSELOR, "Funny how this tangent rounds back to being the answer for your original question. When you have something special, people tend to tamper with it.")
    show kelly fye:
        rightcenterstage

    $ setWait(135.43,136.347)
    $ speak(KELLY, "Who?")
    show counselor 3:
        leftmidstage
        xzoom -1
    $ setWait(136.347,147.191)
    $ speak(COUNSELOR, "Those who have the resources to tamper with the cyber security of FYE evidently. They've made staggering progress and attacked our financial networks this time.")
    show kelly fye angry:
        rightcenterstage
    $ setWait(147.191,150.445)
    $ speak(KELLY, "Well I'm over this middle management shit, where's the warehouse?")
    $ setWait(150.445,152.572)
    $ speak(COUNSELOR, "What do you want the warehouse for?")
    $ setWait(152.572,155.742)
    $ speak(JECKA, "If corporate's there then corporate can handwrite our checks in person.")
    $ setWait(155.742,160.163)
    $ speak(KELLY, "Yeah so where is it? I wanted to buy a nose-stud and this is fucking up my whole weekend!")
    $ setWait(160.163,165.126)
    $ speak(COUNSELOR, "I can't tell you anything of the sort. At least not for free.")
    show jecka fye sad:
        rightmidstage
    $ setWait(165.126,168.212)
    $ speak(JECKA, "Well you don't want us to like kiss in front of you or anything, right?")
    $ setWait(168.212,169.922)
    $ speak(COUNSELOR, "How old are you girls?")
    show kelly fye:
        rightcenterstage
    $ setWait(169.922,170.632)
    $ speak(KELLY, "Eighteen.")
    $ setWait(170.632,172.008)
    $ speak(COUNSELOR, "Eh nah. Get out.")

    $ setWait(172.008,174.677)
    $ speak(JECKA, "Fuck he knows we graduated so we can't even lie about it.")
    $ setWait(174.677,180.308)
    $ speak(KELLY, "Well.. If you don't tell us, I won't tell my 15 year old sister about the help wanted sign here!")
    show counselor 3 angry:
        leftmidstage
        xzoom -1
    $ setWait(180.308,181.851)
    $ speak(COUNSELOR, "Dammit! Alright...")
    show jecka fye angry:
        rightmidstage
    $ setWait(181.851,184.02)
    $ speak(JECKA, "Why the fuck-- Okay just tell us.")
    show counselor 3:
        leftmidstage
        xzoom -1

    $ setWait(184.02,186.606)
    $ speak(COUNSELOR, "All I can give you is this...")
    show jecka fye:
        rightmidstage
    $ setWait(186.606,200.662)
    $ speak(COUNSELOR, "The FYE secret inventory is a rarity much like a city of crystals... Not to be seen through.. But seen under.")
    show kelly fye angry:
        rightcenterstage
    $ setWait(200.662,203.498)
    $ speak(KELLY, "What... The fuck does that mean?")
    show counselor 3 smile:
        leftmidstage
        xzoom -1
    $ setWait(203.498,210.046)
    $ speak(COUNSELOR, "A riddle solved only by people who've laid eyes on the secret warehouse.")
    show kelly fye sad:
        rightcenterstage
    $ setWait(210.046,211.547)
    $ speak(KELLY, "I just want my money...")
    show jecka fye:
        rightmidstage
        pause 0.6
        xzoom -1
        linear 1.5 off_right

    show kelly fye sad:
        rightcenterstage
        pause 0.8
        xzoom -1
        linear 1.9 off_right

    $ setWait(211.547,213.633)
    $ speak(JECKA, "C'mon I might have someone we can ask.")
    stop ambient fadeout 1.5
    jump scene_S0049

label scene_S0049:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show home nicole ext day with Pause(2.788):
        zoom 0.75 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.788 zoom 0.79 truecenter
    $ setVoiceTrack("audio/Scenes/0049.mp3")
    play ambient "audio/Ambience/House_Ambience.mp3"
    scene home nicole int
    show nicole sc8 surprised:
        leftcenterstage

    show jecka fye sad:
        rightcenterstage

    show kelly fye:
        rightmidstage

    $ setWait(2.788,5.29)
    $ speak(NICOLE, "What... The fuck does that mean?")
    $ setWait(5.29,7.084)
    $ speak(JECKA, "I don't know, that's why we're asking you!")
    show nicole sc8 angry:
        leftcenterstage

    $ setWait(7.084,9.836)
    $ speak(NICOLE, "Why would I magically know how to solve some crystal riddle?")
    show jecka fye:
        rightcenterstage
    $ setWait(9.836,12.047)
    $ speak(JECKA, "Cause you had a tapestry on your wall junior year.")
    $ setWait(12.047,16.676)
    $ speak(NICOLE, "Just cause I didn't know what else to put on my wall doesn't mean I'm some bitch who knows horoscopes and fucks a different guy every week.")
    show kelly fye sad:
        rightmidstage

    $ setWait(16.676,18.053)
    $ speak(KELLY, "But I don't have a tapestry.")
    $ setWait(18.053,19.304)
    $ speak(NICOLE, "Why is this bitch in my house?")
    $ setWait(19.304,23.683)
    $ speak(JECKA, "We just came from work. If we can't solve this then we'll never find corporate to give us our paychecks.")
    show nicole sc8:
        leftcenterstage

    $ setWait(23.683,26.853)
    $ speak(NICOLE, "Damn so little words to protect so much illegal porn.")
    $ setWait(26.853,31.608)
    $ speak(KELLY, "But what about the part of \"not seen through but seen under\"?")
    show nicole sc8 angry:
        leftcenterstage

    $ setWait(31.608,34.569)
    $ speak(NICOLE, "Why the fuck do you keep asking me- I don't know.")
    $ setWait(34.569,36.405)
    $ speak(KELLY, "We wasted like an hour coming here.")
    $ setWait(36.405,37.864)
    $ speak(NICOLE, "Oh you had expectations?")
    show jecka fye angry:
        rightcenterstage

    $ setWait(37.864,40.409)
    $ speak(JECKA, "Shut up! You've never had a job, you wouldn't understand.")
    $ setWait(40.409,45.705)
    $ speak(NICOLE, "Yeah cause it either ends up in sexual assault or you doing this shit. This is why I steal stuff and sell it on eBay.")
    $ setWait(45.705,47.666)
    $ speak(KELLY, "This is hopeless, let's just go.")
    show nicole sc8 surprised:
        leftcenterstage

    $ setWait(47.666,50.627)
    $ speak(NICOLE, "Wait! What about your end of the deal? You gotta drive me to the metro now.")
    show kelly fye:
        rightmidstage

    $ setWait(50.627,51.837)
    $ speak(JECKA, "You didn't solve the riddle!")
    show nicole sc8:
        leftcenterstage

    $ setWait(51.837,54.005)
    $ speak(NICOLE, "You never said I had to solve it you just needed my help.")
    $ setWait(54.005,56.133)
    $ speak(JECKA, "Yeah and you didn't help, you didn't even try.")
    $ setWait(56.133,59.594)
    $ speak(NICOLE, "Okay \"city of crystals\"-- Maybe it's an antiques shop! You happy now?")
    show kelly fye angry:
        rightmidstage
    $ setWait(59.594,61.012)
    $ speak(KELLY, "You're just wasting our time.")
    show nicole sc8 angry:
        leftcenterstage

    $ setWait(61.012,63.14)
    $ speak(NICOLE, "You're wasting your life working at FYE.")
    $ setWait(63.14,64.641)
    $ speak(JECKA, "Like we had tons of options.")
    $ setWait(64.641,69.187)
    $ speak(NICOLE, "Sucking literal dick under a bridge is a more appealing option than FYE.")
    show kelly fye sad:
        rightmidstage

    $ setWait(69.187,70.063)
    $ speak(KELLY, "Is there figurative dick?")
    $ setWait(70.063,72.983)
    $ speak(JECKA, "Telling us our job sucks won't convince me to drive you, Nicole.")
    show kelly fye sad:
        rightmidstage
        pause 1.7
        xzoom -1
        linear 2 off_right
    $ setWait(72.983,75.652)
    $ speak(KELLY, "We may as well let her, we gotta go back that way anyway.")
    show nicole sc8 smile:
        leftcenterstage

    $ setWait(75.652,76.903)
    $ speak(NICOLE, "Geography's a bitch.")
    show jecka fye:
        xzoom -1
        rightcenterstage
        linear 1.5 off_right

    show nicole sc8:
        leftcenterstage
        pause 0.8
        linear 1.8 off_right

    $ setWait(76.903,78.363)
    $ speak(JECKA, "Alright let's go.")
    $ setWait(78.363,80.615)
    $ speak(NICOLE, "Can we smoke in your car with the windows up?")
    stop ambient fadeout 1.5
    jump scene_S0050

label scene_S0050:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0050.mp3")
    play ambient "audio/Ambience/Street_Ambience.mp3" fadein 1
    scene franconia ext
    show nicole sc8:
        xzoom -1
        rightmidstage
        linear 2.3 leftstage

    show jecka fye:
        rightstage
        linear 2.5 leftmidstage

    show kelly fye:
        off_right
        linear 2.5 rightcenterstage

    $ setWait(0.039,2.083)
    $ speak(JECKA, "Did we really have to get out of the car with you?")
    $ setWait(2.083,4.836)
    $ speak(NICOLE, "Yeah, if my train isn't running I need a ride back.")
    show kelly fye sad:
        rightcenterstage

    $ setWait(4.836,6.129)
    $ speak(KELLY, "I'm so over this.")
    $ setWait(6.129,9.34)
    $ speak(NICOLE, "Okay now where's Capitol Heights...")
    show jecka fye sad:
        leftmidstage

    $ setWait(9.34,11.926)
    $ speak(JECKA, "Isn't anywhere that ends with \"heights\" like a murder city?")
    show kelly fye:
        rightcenterstage

    $ setWait(11.926,13.219)
    $ speak(KELLY, "Yeah, \"heights\" and \"ville\".")
    $ setWait(13.219,15.763)
    $ speak(NICOLE, "I can't help that the murder cities have all the good ecstasy.")
    $ setWait(15.763,18.182)
    $ speak(JECKA, "You can get X from some white guy at a party school here.")
    show nicole sc8 angry:
        xzoom 1
        leftstage

    $ setWait(18.182,22.061)
    $ speak(NICOLE, "Yeah that's way overpriced from a guy who's gonna keep blowing my phone up.")
    $ setWait(22.061,23.688)
    $ speak(JECKA, "Okay I guess it's worth it.")
    hide nicole sc8
    hide jecka fye
    hide kelly fye
    $ csbox = True
    scene cut0050a
    $ setWait(23.688,28.192)
    $ speak(NICOLE, "So if I follow the blue line... Oh it just takes me all the way there.")
    $ setWait(28.192,31.654)
    $ speak(JECKA, "Wow so if someone fell asleep on the train here they'd wake up in murder land.")
    $ setWait(31.654,33.197)
    $ speak(NICOLE, "Okay it's running, I'll see ya later.")
    $ setWait(33.197,34.824)
    $ speak(KELLY, "Wait! Crystal City!")
    $ setWait(34.824,35.366)
    $ speak(JECKA, "What?")
    scene cut0050b
    $ setWait(35.366,37.201)
    $ speak(KELLY, "On the map? Look at the blue line.")
    $ setWait(37.201,39.62)
    $ speak(NICOLE, "Yeah what's the big deal? I always pass through there.")
    $ setWait(39.62,42.957)
    $ speak(JECKA, "\"A rarity much like a city of crystals\"...")
    scene franconia ext
    $ csbox = False
    show nicole sc8 angry:
        leftstage
        xzoom 1

    show jecka fye:
        leftmidstage

    show kelly fye:
        leftcenterstage

    $ setWait(42.957,45.626)
    $ speak(NICOLE, "Dude shut up about your bitchass Hannah Montana riddle.")
    $ setWait(45.626,46.919)
    $ speak(JECKA, "Do you have a better idea?")
    show kelly fye sad:
        leftcenterstage

    $ setWait(46.919,49.464)
    $ speak(KELLY, "I'm willing to try anything at this point, I just want my money.")
    $ setWait(49.464,51.841)
    $ speak(JECKA, "How much is the metro, can you show us where the stop is?")
    $ setWait(51.841,54.051)
    $ speak(NICOLE, "You think I pay to ride this? Just hop the gate with me.")
    $ setWait(54.051,56.721)
    $ speak(KELLY, "Do we need to be athletic to do that? What if they catch us?")
    show nicole sc8:
        leftstage
        pause 1.8
        xzoom -1
        linear 1 off_farleft

    $ setWait(56.721,59.265)
    $ speak(NICOLE, "Then you better know how to give some good ass head, bitch. C'mon let's go.")
    show jecka fye:
        leftmidstage
        linear 1.2 off_left
    $ setWait(59.265,60.224)
    $ speak(JECKA, "She's joking.")
    show kelly fye:
        leftcenterstage
        linear 1.35 off_left

    $ setWait(60.224,61.517)
    $ speak(KELLY, "Well shit let's hope.")
    stop ambient fadeout 1.5
    jump scene_S0051

label scene_S0051:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0051.mp3")
    play ambient "audio/Ambience/MetroCar_Ambience.mp3" fadein 1
    scene metro car
    show nicole sc8:
        leftcenterstage

    show jecka fye sad:
        rightcenterstage

    show kelly fye sad:
        rightmidstage

    $ setWait(0.037,1.747)
    $ speak(JECKA, "God why does it smell like piss??")
    $ setWait(1.747,4.208)
    $ speak(KELLY, "And why's all the graffiti so racially charged?")
    $ setWait(4.208,6.127)
    $ speak(JECKA, "And would it kill 'em to put padding on the seats?")
    $ setWait(6.127,7.837)
    $ speak(NICOLE, "It's like you never rode the metro before.")
    show jecka fye angry:
        rightcenterstage

    $ setWait(7.837,10.089)
    $ speak(JECKA, "Do I look like a bitch who would take a train home?")
    $ setWait(10.089,11.757)
    $ speak(NICOLE, "You've never once had to take the train?")
    $ setWait(11.757,14.385)
    $ speak(JECKA, "Is this a sitcom? Girls that look like us don't take trains.")
    show nicole sc8 angry:
        leftcenterstage

    $ setWait(14.385,17.388)
    $ speak(NICOLE, "But you'll take all day to find a fuckin' 50 dollar paycheck.")
    $ setWait(17.388,18.764)
    $ speak(JECKA, "90, thank you!")
    show kelly fye:
        rightmidstage

    $ setWait(18.764,21.726)
    $ speak(KELLY, "Yeah and mine's $350 cause I worked the whole week!")
    $ setWait(21.726,23.06)
    $ speak(NICOLE, "What can you afford with that?")
    show coach 1 smile:
        off_right
        linear 1.3 rightstage
    $ setWait(23.06,26.814)
    $ speak(COACH, "I thought I recognized some of the cutest girls I ever taught.")
    show kelly fye:
        xzoom -1

    show jecka fye:
        xzoom -1

    show nicole sc8:
        leftcenterstage

    $ setWait(26.814,27.773)
    $ speak(KELLY, "Mr. Colby?")
    $ setWait(27.773,30.735)
    $ speak(NICOLE, "Yeah we graduated, you're not legally allowed to talk to us anymore.")
    show coach 1 angry:
        rightstage
    $ setWait(30.735,34.071)
    $ speak(COACH, "Shut the fuck up bitch I don't wanna talk to you anyway!")
    show coach 1 smile:
        rightstage
    $ setWait(34.071,41.704)
    $ speak(COACH, "Kelly I just wanted to thank you for your help last week at FYE. I know you were confused but I found what I was looking for.")
    $ setWait(41.704,44.081)
    $ speak(KELLY, "Looking for what?")
    show coach 1 worried:
        rightstage
    $ setWait(44.081,49.545)
    $ speak(COACH, "That uh.. That mild style, y'know what I mean-- Well you don't know what I mean but that's okay.")
    show jecka fye surprised:
        rightcenterstage
        xzoom -1

    $ setWait(49.545,51.964)
    $ speak(JECKA, "Oh that was code for..")
    $ setWait(51.964,56.552)
    $ speak(KELLY, "Yeah well glad I could help. Looking forward to seeing you again at FYE.")
    show coach 1 smile:
        rightstage
    $ setWait(56.552,59.43)

    show kelly fye sad:
        rightmidstage
        xzoom -1

    $ speak(COACH, "Looking forward to seeing that ass.")
    $ setWait(59.43,60.89)
    $ speak(METRO, "Doors open.")
    show coach 1 smile:
        rightstage
        pause 1.6
        linear 3.4 off_left

    show kelly fye:
        rightmidstage
        pause 2.7
        xzoom 1

    show jecka fye:
        rightcenterstage
        pause 3.7
        xzoom 1


    $ setWait(60.89,66.646)
    $ speak(COACH, "You girls stay sexy, I got some airport bartenders to have a little chat with.")
    $ setWait(66.646,70.524)
    $ speak(NICOLE, "He's like every horny Indian guy that ends up in the spam box.")
    $ setWait(70.524,78.032)
    $ speak(METRO, "The next stop is: Crystal City. Step back, doors closing.")
    $ setWait(78.032,80.743)
    $ speak(JECKA, "So.. Do we get off at the next one?")
    $ setWait(80.743,82.536)
    $ speak(NICOLE, "Did you not just hear the intercom?")
    show jecka fye sad:
        rightcenterstage
    $ setWait(82.536,83.871)
    $ speak(JECKA, "I've never done this before!")
    show kelly fye sad:
        rightmidstage

    $ setWait(83.871,84.914)
    $ speak(KELLY, "Yeah we don't know!")
    show nicole sc8 angry:
        leftcenterstage

    $ setWait(84.914,87.041)
    $ speak(NICOLE, "Yes, you get off at the next one. Holy shit.")
    $ setWait(87.041,89.001)
    $ speak(KELLY, "Why's she your friend? She's so mean.")
    show jecka fye:
        xzoom -1
    $ setWait(89.001,90.586)
    $ speak(JECKA, "Cause she's not as stupid as you.")
    $ setWait(90.586,92.296)
    $ speak(KELLY, "Makes sense now.")
    $ setWait(92.296,94.59)
    $ speak(NICOLE, "So how crazy you think this illegal porn stash is?")
    show jecka fye:
        xzoom 1
    $ setWait(94.59,96.092)
    $ speak(JECKA, "Yeah just say it in public like that.")
    show kelly fye:
        rightmidstage
        xzoom 1

    $ setWait(96.092,97.635)
    $ speak(NICOLE, "No one on the train gives a shit.")
    $ setWait(97.635,99.72)
    $ speak(JECKA, "I don't know, what do you think?")
    show nicole sc8:
        leftcenterstage

    $ setWait(99.72,105.601)
    $ speak(NICOLE, "There's probably a bunch of murder videos. You think guys whack off to girls getting killed? Not even hot girls, just anyone.")
    show kelly fye sad:
        rightmidstage

    $ setWait(105.601,107.311)
    $ speak(KELLY, "Why would that even cross your mind?")
    show nicole sc8 angry:
        leftcenterstage

    $ setWait(107.311,109.73)
    $ speak(NICOLE, "Sorry let's talk about iCarly, is that more your level?")
    show jecka fye angry:
        rightcenterstage
        xzoom 1

    $ setWait(109.73,111.941)
    $ speak(JECKA, "Fuck iCarly that bitch is so annoying!")
    $ setWait(111.941,112.733)
    $ speak(KELLY, "Which one?")
    show jecka fye angry:
        xzoom -1
    $ setWait(112.733,113.609)
    $ speak(JECKA, "All of them!")
    stop ambient fadeout 1.5
    jump scene_S0052

label scene_S0052:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0052.mp3")
    play ambient "audio/Ambience/MetroStation_Ambience.mp3" fadein 1
    scene metro station
    show jecka fye:
        xzoom -1
        leftmidstage
        linear 2.71 rightcenterstage

    show kelly fye sad:
        off_left
        xzoom -1
        linear 3 leftcenterstage
    $ setWait(0.088,2.799)
    $ speak(KELLY, "Wait but how are we getting back without her?")
    show jecka fye surprised:
        rightcenterstage
        xzoom 1
    $ setWait(2.799,6.428)
    $ speak(JECKA, "Oh shit ummm...")
    show jecka fye sad:
        rightcenterstage
    $ setWait(6.428,8.43)
    $ speak(JECKA, "Well it can't be too hard, right?")
    $ setWait(8.43,10.432)
    $ speak(KELLY, "What if it is.")
    show jecka fye:
        rightcenterstage
    $ setWait(10.432,13.352)
    $ speak(JECKA, "We could just call a cab back to the car once we get our money.")
    $ setWait(13.352,16.563)
    $ speak(KELLY, "We don't even know if the riddle actually meant Crystal City.")
    $ setWait(16.563,17.648)
    $ speak(JECKA, "You have a better lead?")
    $ setWait(17.648,18.899)
    $ speak(KELLY, "I'm just thinking aloud.")
    show jecka fye angry:
        rightcenterstage
    $ setWait(18.899,22.319)
    $ speak(JECKA, "Well fuck off with that shit, what even is Crystal City anyway?")
    hide jecka fye angry
    hide kelly fye sad
    $ csbox = True
    scene cut0052
    $ setWait(22.319,23.987)
    $ speak(KELLY, "I don't know but they have a mall.")
    $ setWait(23.987,26.74)
    $ speak(JECKA, "Wait that's good, right? Only malls have FYE's.")
    $ setWait(26.74,30.202)
    $ speak(KELLY, "One time I saw a standalone FYE that replaced a Blockbuster.")
    $ setWait(30.202,34.164)
    $ speak(JECKA, "Actually standalone? Or was it like a duplex attached to a Subway?")
    $ setWait(34.164,35.832)
    $ speak(KELLY, "It might've been Quiznos.")
    $ setWait(35.832,37.793)
    $ speak(JECKA, "Ugh.. Now I want Quiznos.")
    $ setWait(37.793,39.044)
    $ speak(KELLY, "You wanna get that real quick?")
    $ setWait(39.044,43.048)
    $ speak(JECKA, "Yeah sure with all zero dollars and zero cents we got paid this week.")
    $ setWait(43.048,45.551)
    $ speak(KELLY, "C'mon we can't lose hope, let's just check the mall out.")
    $ setWait(45.551,47.594)
    $ speak(JECKA, "I'm gonna fucking kill myself.")
    stop ambient fadeout 1.5
    jump scene_S0053

label scene_S0053:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0053.mp3")
    play ambient "audio/Ambience/Underground_Ambience.mp3" fadein 1
    $ csbox = False
    scene ccug2
    show jecka fye:
        xzoom -1
        leftstage
        linear 9.9 rightmidstage
        xzoom 1

    show kelly fye sad:
        xzoom -1
        off_left
        linear 10 rightcenterstage

    $ setWait(0.042,5.673)
    $ speak(KELLY, "What kinda mall is this? There's no Best Buy or Chipotle or anything.")
    $ setWait(5.673,9.218)
    $ speak(JECKA, "Yeah and how are these stores in business when we're the only people in here?")
    $ setWait(9.218,16.183)
    $ speak(KELLY, "Shoe shine places and watch repair shops, it's so dated. Just tunnels with pointless stores.")
    show jecka fye:
        rightmidstage
        xzoom 1

    show kelly fye sad:
        rightcenterstage
        xzoom -1

    $ setWait(16.183,22.189)
    $ speak(JECKA, "It's like an underground society lost in time. All these stairways going down here and no one notices.")
    show kelly fye:
        rightcenterstage
        xzoom -1
    $ setWait(22.189,24.608)
    $ speak(KELLY, "Underground... Like the riddle!")
    show jecka fye surprised:
        rightmidstage
    $ setWait(24.608,27.778)
    $ speak(JECKA, "\"City of crystals, not seen through but seen under.\"-- No fuckin' way.")
    $ setWait(27.778,29.738)
    $ speak(KELLY, "It's Crystal City Underground! Here!")
    $ setWait(29.738,31.365)
    $ speak(JECKA, "Yeah can't be a coincidence.")
    $ setWait(31.365,35.536)
    $ speak(KELLY, "I guess you could hide a lot here, not like there's any people who'd randomly find it.")
    show jecka fye:
        rightmidstage

    $ setWait(35.536,38.038)
    $ speak(JECKA, "Could they really fit a whole warehouse down here?")
    $ setWait(38.038,41.292)
    $ speak(KELLY, "They fit a Taco Bell Express down here, they could fit anything.")
    $ setWait(41.292,46.505)
    $ speak(JECKA, "It just keeps going and going though. Even if we're near it, how do we find it?")
    $ setWait(46.505,47.673)
    $ speak(KELLY, "Let's check the directory.")
    show jecka fye angry:
        rightmidstage
    $ setWait(47.673,50.926)
    $ speak(JECKA, "Oh yeah we'll just look for the listing that says \"illegal porn warehouse\".")
    show kelly fye sad:
        rightcenterstage
        xzoom -1
    $ setWait(50.926,51.635)
    $ speak(KELLY, "Shhh!")
    $ setWait(51.635,52.72)
    $ speak(JECKA, "No one's here.")
    $ setWait(52.72,53.637)
    $ speak(KELLY, "The workers?")
    show jecka fye:
        rightmidstage
    $ setWait(53.637,58.517)
    $ speak(JECKA, "It's just middle-eastern guys selling Juicy Fruit, legal pads, and foil balloons all in the same store.")
    $ setWait(58.517,61.854)
    $ speak(KELLY, "Yeah I was wondering who would need that combination of things?")
    $ setWait(61.854,66.734)
    $ speak(JECKA, "There was even a puppet store, like this is what happens when Walmart doesn't destroy small businesses.")
    $ setWait(66.734,71.447)
    $ speak(KELLY, "Yeah they just make more and more progressively specific stores.")
    show jecka fye sad:
        rightmidstage
        pause 2.95
        xzoom -1
        linear 2 off_right
    $ setWait(71.447,76.744)
    $ speak(JECKA, "And we need the most specific store of them all. Let's find this place.")
    show kelly fye:
        rightcenterstage
        xzoom -1
        linear 2.3 off_right
    $ setWait(76.744,79.288)
    $ speak(KELLY, "Is \"illegal\" really that specific?")
    stop ambient fadeout 1.5
    jump scene_S0054

label scene_S0054:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0054.mp3")
    play ambient "audio/Ambience/Underground_Dead_Ambience.mp3" fadein 1
    scene ccug3
    show jecka fye:
        off_left
        xzoom -1
        linear 4 rightmidstage
        xzoom 1

    show kelly fye sad:
        off_farleft
        xzoom -1
        linear 4 rightcenterstage

    $ setWait(0.042,2.044)
    $ speak(JECKA, "Okay what is this?")
    $ setWait(2.044,3.087)
    $ speak(KELLY, "Are we lost?")
    $ setWait(3.087,6.966)
    $ speak(JECKA, "I can't tell, every hallway looks equally from the 80's.")
    show kelly fye sad:
        rightcenterstage
        xzoom -1

    show jecka fye:
        rightmidstage

    $ setWait(6.966,15.349)
    $ speak(KELLY, "Every pizza place has the same overly air bubbled crust... Every sandwich shop has a different line of off-brand chips.")
    $ setWait(15.349,24.567)
    $ speak(KELLY, "Did you see the toy store without any actual name brands or video games? It was just wooden dolls, what kid wants that?")
    $ setWait(24.567,29.03)
    $ speak(JECKA, "It's like the twilight zone of low-rent retail that can survive off 3 customers a day.")
    $ setWait(29.03,31.991)
    $ speak(KELLY, "And we can't even go in off impulse.. cause...")
    show kelly fye angry:
        rightcenterstage
        xzoom -1
    $ setWait(31.991,33.701)
    $ speak(KELLY, "We don't even have our paychecks!")
    show jecka fye surprised:
        rightmidstage
    $ setWait(33.701,34.285)
    $ speak(JECKA, "Shh!")
    $ setWait(34.285,37.163)
    $ speak(KELLY, "No! The counselor lied to us so we'd look for nothing!")
    show jecka fye angry:
        rightmidstage
    $ setWait(37.163,37.872)
    $ speak(JECKA, "Shut up!")
    $ setWait(37.872,41.167)
    $ speak(KELLY, "I don't care if they hear us! I hate FYE, I quit!")
    $ setWait(41.167,44.92)
    $ speak(JECKA, "It's not about FYE! If you don't shut up another homeless guy's gonna come up to us!")
    $ setWait(44.92,49.05)
    $ speak(KELLY, "I don't care! I don't care about him or his drumset made of buckets!")
    show jecka fye:
        rightmidstage

    $ setWait(49.05,51.427)
    $ speak(JECKA, "Wow you don't even care about the homeless anymore.")
    $ setWait(51.427,52.553)
    $ speak(KELLY, "Neither do you!")
    $ setWait(52.553,54.638)
    $ speak(JECKA, "Yeah but I never cared.")
    show kelly fye sad:
        rightcenterstage
        xzoom -1
    $ setWait(54.638,57.016)
    $ speak(KELLY, "I'd rather be homeless at this point...")
    show kelly fye sad:
        xzoom 1
    $ setWait(57.016,61.02)
    $ speak(KELLY, "...Or working at some weird underground 3Ad dungeon.")
    show jecka fye sad:
        rightmidstage

    $ setWait(61.02,64.857)
    $ speak(JECKA, "Your emotions are so not worth 8 an hour...")
    show jecka fye surprised:
        rightmidstage
    $ setWait(64.857,69.445)
    $ speak(JECKA, "...Wait what's a 3Ad dungeon? Is that like a Jeffery fetish?")
    show kelly fye:
        xzoom -1
        rightcenterstage
        pause 1.75
        xzoom 1
    $ setWait(69.445,73.366)
    $ speak(KELLY, "No it's this fuckin' weird business behind us.")
    scene cut0054a
    hide jecka fye surprised
    hide kelly fye
    $ csbox = True
    $ setWait(73.366,75.493)
    $ speak(JECKA, "I think that's just graffiti.")
    $ setWait(75.493,77.328)
    $ speak(KELLY, "There's a 3Ad gang?")
    $ setWait(77.328,80.498)
    $ speak(JECKA, "If enough rappers make mixtapes then eventually.")
    $ setWait(80.498,83.876)
    $ speak(KELLY, "But why would this be the only graffiti down here?")
    $ setWait(83.876,86.629)
    $ speak(JECKA, "Bitch is this Dora? How the fuck should I know?")
    $ setWait(86.629,89.84)
    $ speak(KELLY, "Kinda looks like FYE upside down.")
    $ setWait(89.84,92.51)
    $ speak(JECKA, "No way... This can't be it.")
    $ setWait(92.51,95.137)
    $ speak(KELLY, "Even if it is, it's closed anyway.")
    $ setWait(95.137,99.683)
    $ speak(JECKA, "I'm not sure if an illegal porn warehouse would just be commercially open.")
    $ setWait(99.683,101.602)
    $ speak(KELLY, "There isn't even anyone to let us in.")
    $ setWait(101.602,106.69)
    $ speak(JECKA, "Yeah look at that lock, they'd need a weird-ass Best Buy logo key.")
    scene cut0054b

    $ setWait(106.69,109.777)
    $ speak(KELLY, "It's kinda shaped like my manager's tag...")
    $ setWait(109.777,111.32)
    $ speak(JECKA, "...No fuckin' way.")
    $ setWait(111.32,112.863)
    $ speak(KELLY, "Do you think it'll fit?")
    $ setWait(112.863,114.824)
    $ speak(JECKA, "They can't stop us from trying.")
    scene cut0054c
    $ setWait(114.824,117.076)
    $ speak(KELLY, "Wow it's almost exactly...")
    scene cut0054d
    $ setWait(117.076,118.911)
    $ speak(JECKA, "It's exactly exactly.")
    $ setWait(118.911,120.204)
    $ speak(KELLY, "It's not opening though.")
    $ setWait(120.204,123.791)
    $ speak(JECKA, "Yeah this isn't Indiana Jones, we gotta turn it or move it or something.")
    $ setWait(123.791,126.293)
    $ speak(KELLY, "What's Indiana Jones? I always hear about it.")
    $ setWait(126.293,129.38)
    $ speak(JECKA, "Some boring movie Gen Xer white guys won't shut up about.")
    $ setWait(129.38,131.966)
    $ speak(KELLY, "Oh... So like Star Wars?")
    $ setWait(131.966,133.509)
    $ speak(JECKA, "Exactly. Turn it.")
    scene cut0054e
    show black onlayer screens:
        alpha 0.0
        pause 1.2
        linear 1.4 alpha 1.0

    $ setWait(133.509,137.555)
    $ speak(KELLY, "Holy shit it's actually moving!")
    stop ambient fadeout 1.5
    jump scene_S0055

label scene_S0055:
    show black onlayer screens with Pause(2.2):
        alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0055.mp3")
    $ csbox = False
    play ambient "audio/Ambience/Warehouse_Ambience.mp3" fadein 1
    scene int warehouse
    show kelly fye:
        off_right
        pause 0.5
        linear 4.5 rightcenterstage

    show jecka fye surprised:
        off_right
        linear 6 off_left

    $ setWait(0.047,2.049)
    $ speak(KELLY, "This is insane...")
    $ setWait(2.049,5.594)
    $ speak(JECKA, "There's like rows forever, it just keeps going back.")
    $ setWait(5.594,10.224)
    $ speak(KELLY, "I never thought there'd be such a collection of fully alphabatized illegal porn.")
    show jecka fye surprised:
        off_left
        xzoom -1
        linear 1 leftcenterstage

    $ setWait(10.224,12.143)
    $ speak(JECKA, "Do not go down the R section.")
    $ setWait(12.143,15.563)
    $ speak(KELLY, "They probably have way worse. I wouldn't put it past them to have a child porn aisle.")
    show jecka fye sad:
        leftcenterstage
        xzoom -1

    show cut0055a onlayer screens:
        alpha 0.0
        pause 1 alpha 1.0
    $ setWait(15.563,17.356)
    $ speak(JECKA, "Aisle? They got a whole wing for it.")
    $ setWait(17.356,20.151)
    $ speak(KELLY, "Ew oh my god! It literally can't get worse than this.")
    hide cut0055a onlayer screens
    show jecka fye sad:
        leftcenterstage
        xzoom 1

    show cut0055b onlayer screens:
        alpha 0.0
        pause 1.2 alpha 1.0
        pause 9.015 alpha 0.0

    $ setWait(20.151,22.194)
    $ speak(JECKA, "Yeah it can, they got two wings for it!")
    $ setWait(22.194,24.905)
    $ speak(KELLY, "Oh no... That's genuinely terrible.")
    $ setWait(24.905,28.159)
    $ speak(JECKA, "I know, who would get turned on by Amanda Show?")

    hide cut0055b onlayer screens

    show kelly fye:
        rightcenterstage

    show jecka fye:
        leftcenterstage
        xzoom -1

    $ setWait(28.159,30.369)
    $ speak(KELLY, "So are the corporate executive guys here?")
    $ setWait(30.369,32.955)
    $ speak(JECKA, "We might've shown up after business hours.")
    $ setWait(32.955,34.623)
    $ speak(KELLY, "You think their hours are better than ours?")
    $ setWait(34.623,37.626)
    $ speak(JECKA, "I don't see why you'd have hours at all with a fuckin' business like this.")
    $ setWait(37.626,41.255)
    $ speak(KELLY, "Hey FYE has really high standards, we're number 1 in the country.")
    $ setWait(41.255,43.382)
    $ speak(JECKA, "At what? Child porn? Wow I'm so honored.")
    $ setWait(43.382,45.217)
    $ speak(KELLY, "Let's just get our paychecks and get out of here.")
    $ setWait(45.217,47.386)
    $ speak(JECKA, "From who? There's no one here to sign 'em.")
    $ setWait(47.386,49.138)
    $ speak(KELLY, "Okay we'll just wait.")
    $ setWait(49.138,52.6)
    $ speak(JECKA, "Or we could just find some loose cash to steal and quit this place.")
    show kelly fye sad:
        rightcenterstage

    $ setWait(52.6,54.56)
    $ speak(KELLY, "Uh that's pretty illegal.")
    show jecka fye angry:
        leftcenterstage
        xzoom -1
    $ setWait(54.56,59.482)
    $ speak(JECKA, "We are standing in a forbidden porn warehouse, laws do not apply here.")
    $ setWait(59.482,61.15)
    $ speak(KELLY, "Ugh I guess you're right.")
    show kelly fye angry:
        rightcenterstage
    $ setWait(61.15,64.028)
    $ speak(KELLY, "Fuck FYE, I quit. Let's find some cash.")
    show jecka fye:
        leftcenterstage
        xzoom -1
    $ setWait(64.028,66.072)
    $ speak(JECKA, "Seriously? I thought you needed the money.")
    show kelly fye:
        rightcenterstage

    $ setWait(66.072,69.158)
    $ speak(KELLY, "No my dad has tons of money, he lets me live at home for free.")
    $ setWait(69.158,73.829)
    $ speak(JECKA, "Wow, my dad just hits me and forces me to get a job.")
    $ setWait(73.829,75.289)
    $ speak(KELLY, "But yeah, I quit.")
    show jecka fye surprised:
        leftcenterstage
        xzoom -1

    show kelly fye sad:
        rightcenterstage
        pause 0.4
        xzoom -1

    $ setWait(75.289,78.125)
    $ speak(COUNSELOR, "Why quit now? You've come so far.")
    show counselor 3 smile:
        off_right
        linear 1.4 rightstage

    show jecka fye surprised:
        leftcenterstage
        xzoom -1
        linear 0.4 leftmidstage

    show kelly fye sad:
        xzoom -1
        rightcenterstage
        linear 0.5 leftcenterstage

    $ setWait(78.125,78.751)
    $ speak(JECKA, "Oh fuck.")
    $ setWait(78.751,79.919)
    $ speak(KELLY, "What're you doing here!?")
    $ setWait(79.919,82.588)
    $ speak(COUNSELOR, "I work here, I thought you knew.")
    show counselor 3:
        rightstage
    $ setWait(82.588,88.803)
    $ speak(COUNSELOR, "Though what I didn't know was that you would actually find the secret of all secrets.")
    $ setWait(88.803,91.347)
    $ speak(KELLY, "You're putting porn on a really high pedestal.")
    show counselor 3 angry:
        rightstage

    $ setWait(91.347,97.311)
    $ speak(COUNSELOR, "Shut up!! You're in no place to act smart when you can't even watch your tail.")
    $ setWait(97.311,107.78)
    $ speak(COUNSELOR, "Do you realize what we do here? How we keep the fabric of society together? Without this warehouse, chaos would ensue over half the nation.")
    show jecka fye angry:
        leftmidstage

    $ setWait(107.78,111.617)
    $ speak(JECKA, "Who the fuck needs illegal porn to not go insane??")
    show counselor 3:
        rightstage

    $ setWait(111.617,116.831)
    $ speak(COUNSELOR, "Mailmen, delivery boys, even the valets who park your car.")
    $ setWait(116.831,126.507)
    $ speak(COUNSELOR, "Without their preferred outlet society would crumble, this enterprise exists parallel to only the government itself.")
    $ setWait(126.507,128.717)
    $ speak(KELLY, "Wouldn't they need like therapy instead?")
    show counselor 3 angry:
        rightstage

    $ setWait(128.717,136.142)
    $ speak(COUNSELOR, "Therapy is controlled by this over-feminized society, escapism cannot be sanctioned.")
    $ setWait(136.142,138.686)
    $ speak(JECKA, "What Fight Club fan website did you get that from?")
    $ setWait(138.686,140.813)
    $ speak(KELLY, "Seriously? Ugh, kill me.")
    show counselor 3 smile:
        rightstage
        pause 1
        linear 1 rightmidstage

    $ setWait(140.813,142.106)
    $ speak(COUNSELOR, "With pleasure.")
    show jecka fye surprised:
        leftmidstage
        xzoom -1
        linear 0.5 leftstage

    $ setWait(142.106,142.648)
    $ speak(JECKA, "Oh shit!")
    show kelly fye sad:
        xzoom 1
        leftcenterstage
        linear 0.5 off_left

    show counselor 3 smile:
        rightmidstage
        pause 0.4
        linear 0.6 off_left

    show jecka fye surprised:
        leftstage
        pause 1
        xzoom 1

    show white onlayer screens:
        alpha 0.0
        pause 1
        alpha 1.0
        linear 0.16 alpha 0.0
        pause 0.28
        alpha 1.0
        linear 0.16 alpha 0.0
        pause 0.3
        alpha 1.0
        linear 0.3 alpha 0.0

    $ setWait(142.648,144.817)
    $ speak(KELLY, "Ahhhhhhhh!!!")
    show jecka fye surprised:
        xzoom 1
        leftstage
    $ setWait(144.817,146.36)
    $ speak(JECKA, "Fuck! Fuck!! Fuck!!")
    show counselor 3 smile:
        off_left
        xzoom -1
        linear 2.5 rightcenterstage
        xzoom 1

    $ setWait(146.36,149.697)
    $ speak(COUNSELOR, "That security footage should go for a nice price.")
    show jecka fye sad:
        xzoom -1
        leftstage

    $ setWait(149.697,151.49)
    $ speak(JECKA, "Lemme go! I wanna go home!!")
    $ setWait(151.49,154.535)
    $ speak(COUNSELOR, "That you wouldn't be fair, you know too much.")
    $ setWait(154.535,156.412)
    $ speak(JECKA, "No! I-I won't tell anyone!!")
    $ setWait(156.412,162.251)
    $ speak(COUNSELOR, "You don't need to die immediately, by all means watch a movie first. We have plenty.")
    $ setWait(162.251,167.047)
    $ speak(JECKA, "Watch fucking murder child porn or be shot and killed?? Those are my options!?")
    $ setWait(167.047,169.884)
    $ speak(COUNSELOR, "It seems it's the latter.")
    show white onlayer screens:
        alpha 0.0
        pause 1.5
        alpha 1.0
        pause 0.3
        linear 0.6 alpha 0.0
    $ setWait(169.884,171.635)
    $ speak(COP, "FBI! Freeze!!")
    show counselor 3 angry:
        xzoom -1

    $ setWait(171.635,172.553)
    $ speak(COUNSELOR, "Agh!!")

    show counselor 3 angry:
        xzoom -1
        ycenter 540
        pause 0.4
        linear 0.4 ycenter 2000

    show jecka fye surprised:
        xzoom -1
        leftstage

    $ setWait(172.553,173.888)
    $ speak(JECKA, "Holy shit!")
    show cop:
        off_right
        linear 1.5 rightmidstage

    $ setWait(173.888,175.89)
    $ speak(COP, "Miss, what's your business here??")
    show jecka fye surprised:
        xzoom -1
        leftstage
        linear 0.5 leftmidstage
        pause 1
        linear 0.5 leftcenterstage

    $ setWait(175.89,178.684)
    $ speak(JECKA, "I... I...")
    show jecka fye sad:
        xzoom -1
        leftcenterstage

    $ setWait(178.684,181.312)
    $ speak(JECKA, "I just wanted my paycheck!")
    $ setWait(181.312,186.525)
    $ speak(COP, "Good, jamming their financial systems was a success. We've been making attempts at it all year.")
    $ setWait(186.525,189.486)
    $ speak(JECKA, "The fuckin' FBI's why I ended up here?")
    $ setWait(189.486,193.866)
    $ speak(COP, "You didn't need to go snooping, but thankfully it led us to this goldmine.")
    $ setWait(193.866,197.119)
    $ speak(JECKA, "Goldmine?? O-Of evidence, right?")
    $ setWait(197.119,199.622)
    $ speak(COP, "This is far more than evidence...")
    $ setWait(199.622,201.248)
    $ speak(COP, "This is for us.")
    $ setWait(201.248,206.795)
    $ speak(COP, "Our government agencies have been seeking a treasure like this for decades.")
    show jecka fye angry:
        xzoom -1
        leftcenterstage

    $ setWait(206.795,210.09)
    $ speak(JECKA, "How is illegal porn a treasure??")
    $ setWait(210.09,212.843)
    $ speak(COP, "I'm afraid you know too much.")
    show jecka fye sad:
        xzoom -1
        leftcenterstage
        pause 0.5
        linear 0.4 leftmidstage
    $ setWait(212.843,214.47)
    $ speak(JECKA, "Oh don't- No don't kill me!")
    $ setWait(214.47,220.434)
    $ speak(COP, "Kill you? Don't be ludicrous. An officer would never execute a civilian in such a barbaric way.")
    $ setWait(220.434,222.269)
    $ speak(JECKA, "Okay that's your opinion.")
    $ setWait(222.269,224.813)
    $ speak(COP, "The Taliban however...")
    $ setWait(224.813,226.732)
    $ speak(JECKA, "Wh-what about 'em?")
    $ setWait(226.732,231.07)
    $ speak(COP, "Once we hand you off to them it's really out of our hands.")
    $ setWait(231.07,232.112)
    $ speak(JECKA, "No way!")
    show cop:
        rightmidstage
        pause 3.8
        linear 6 leftmidstage

    show black onlayer screens:
        alpha 0.0
        pause 4.5
        linear 3 alpha 1.0

    stop ambient fadeout 7
    $ setWait(232.112,240.403)
    $ speak(COP, "It's the most humane way the FBI can ensure you never tell a soul...")

    jump end_S0056

label end_S0056:

    show black onlayer screens with Pause(2):
        alpha 1.0
        linear 1.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    scene black

    if "end_0056" not in persistent.endings:
        $ persistent.endings.append("end_0056")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    $ renpy.movie_cutscene("cs0056.webm")

    return
label scene_S0057:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1.2
    show title_april2008 onlayer screens
    scene onlayer master
    show black
    show school front with Pause(3.008):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 3.008 zoom 1.1 truecenter

    $ setVoiceTrack("audio/Scenes/0057.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3"
    hide title_april2008 onlayer screens
    $ csbox = False
    scene classroom int 3
    show jecka sc1 smoke:
        leftcenterstage

    show nicole sc1 smoke:
        leftmidstage

    show smoke:
        xalign 0.0
        yalign 0.0

    $ setWait(3.008,7.054)
    $ speak(NICOLE, "How do they enforce \"no smoking\" when there's no smoke alarm in here.")
    $ setWait(7.054,11.35)
    $ speak(JECKA, "Yeah I was afraid the sprinkler would go off when I flicked the lighter but I guess it's just broken.")
    $ setWait(11.35,13.268)
    $ speak(NICOLE, "That's cool. Yeah we don't need that anyway.")
    $ setWait(13.268,18.231)
    $ speak(JECKA, "If the nerds catch on fire in chemistry they'll just burn to a crisp of unwashed hair and Skechers.")
    $ setWait(18.231,21.276)
    $ speak(NICOLE, "Or the Tony Hawk shoes if they think Xbox is a personality trait.")
    $ setWait(21.276,23.362)
    $ speak(JECKA, "Oh those shitty ass sneakers at Kohl's??")
    $ setWait(23.362,26.073)
    $ speak(NICOLE, "Yeah they're like the christian rock of skate shoes.")
    $ setWait(26.073,28.45)
    $ speak(JECKA, "I wonder what the christian rock of cigarettes is.")
    $ setWait(28.45,29.701)
    $ speak(NICOLE, "Marlboro Ultra Lights.")
    $ setWait(29.701,31.495)
    $ speak(JECKA, "Yeah those are for when you're pregnant, right?")
    $ setWait(31.495,33.538)
    $ speak(NICOLE, "No, suicide's for when you're pregnant.")
    $ setWait(33.538,37.209)
    $ speak(JECKA, "You're right. But what's the anti-Christ of cigarettes?")
    $ setWait(37.209,38.543)
    $ speak(NICOLE, "Maybe cloves.")
    $ setWait(38.543,41.755)
    $ speak(JECKA, "Goth girl certified. I heard they get rid of your gag reflex.")
    $ setWait(41.755,43.548)
    $ speak(NICOLE, "Yeah I read that on MySpace too.")
    $ setWait(43.548,47.302)
    $ speak(JECKA, "I'm gonna start smoking cloves so I can get a really rich husband when I'm 30.")
    show katz 1 angry:
        off_right
        linear 2 rightmidstage

    show jecka sc1 smoke:
        leftcenterstage
        pause 1
        xzoom -1

    $ setWait(47.302,50.305)
    $ speak(KATZ, "What do you girls think you're doing in here??")
    $ setWait(50.305,52.641)
    $ speak(JECKA, "Oh sorry, we'll go to the English classroom instead.")
    $ setWait(52.641,55.477)
    $ speak(KATZ, "I mean the smoking??")
    $ setWait(55.477,58.73)
    $ speak(NICOLE, "So you want us to stay here but do as you say? Controlling much?")
    $ setWait(58.73,63.735)
    $ speak(JECKA, "C'mon Mr. Katz, just let us finish this cigarette and we'll never do it again.")
    show katz 1 sad:
        rightmidstage
        pause 2.15
        xzoom -1
        linear 1.3 off_right

    $ setWait(63.735,67.114)
    $ speak(KATZ, "Ugh.. Um.. Well okay.")
    $ setWait(67.114,69.449)
    $ speak(NICOLE, "God what a lonely-ass stamp collecting bitch.")
    hide katz 1 sad
    show jecka sc1 smoke:
        xzoom 1
    $ setWait(69.449,72.411)
    $ speak(JECKA, "Yeah you can talk to men like they're dogs and they'll fold on anything.")
    $ setWait(72.411,73.495)
    $ speak(NICOLE, "Have you tried it with women?")
    show lynn:
        off_left
        xzoom -1
        linear 0.5 leftstage

    show nicole sc1 smoke:
        leftmidstage
        pause 0.4
        xzoom -1
    $ setWait(73.495,77.04)
    $ speak(LYNN, "Are you out of your mind? Why would you smoke in here??")
    $ setWait(77.04,81.712)
    $ speak(JECKA, "Oh we're sorry Ms. Lynn, let us just finish this one and we'll be done, okay?")
    $ setWait(81.712,83.797)
    $ speak(LYNN, "Put it out now before you're both expelled!")
    show nicole sc1 angry:
        leftmidstage
        xzoom -1

    show jecka sc1:
        leftcenterstage
        xzoom 1

    $ setWait(83.797,85.007)
    $ speak(NICOLE, "Okay calm down!")
    show lynn:
        leftstage
        xzoom -1
        pause 0.8
        xzoom 1
        linear 0.6 off_left

    show smoke:
        xalign 0.0
        yalign 0.0
        alpha 1.0
        linear 4 alpha 0.0

    $ setWait(85.007,87.676)
    $ speak(LYNN, "Unbelievable! Back to class!")

    $ setWait(87.676,88.552)
    $ speak(NICOLE, "Fuckin' whore.")
    hide lynn
    $ setWait(88.552,90.095)
    $ speak(JECKA, "I guess it doesn't work on women.")
    show nicole sc1:
        leftmidstage
        xzoom 1
    $ setWait(90.095,92.097)
    $ speak(NICOLE, "Yeah you're just not hot enough.")
    show jecka sc1 smile:
        leftcenterstage
        xzoom 1
    $ setWait(92.097,94.349)
    $ speak(JECKA, "I need a Hello Kitty eyebrow tattoo.")
    stop ambient fadeout 1.5
    jump scene_S0058

label scene_S0058:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0058.mp3")
    play ambient "audio/Ambience/hallway_Ambience.mp3" fadein 1
    scene school int 1

    show nicole sc1:
        leftmidstage

    show jecka sc1:
        xzoom -1
        leftcenterstage

    show crispin sc1:
        rightcenterstage

    $ setWait(0.039,4.836)
    $ speak(CRISPIN, "But yeah uh you see that one YouTube video?")
    $ setWait(4.836,6.295)
    $ speak(NICOLE, "There's a lot of YouTube videos.")
    $ setWait(6.295,10.341)
    $ speak(CRISPIN, "No! Like the one where this guy just goes crazy? He's like outside.")
    $ setWait(10.341,12.677)
    $ speak(NICOLE, "Oh yeah that narrows it down.")
    $ setWait(12.677,14.554)
    $ speak(JECKA, "Why do you think we like you?")
    $ setWait(14.554,17.14)
    $ speak(CRISPIN, "Y-you... You don't like me? Like not like talking?")
    show jecka sc1 angry:
        xzoom -1
        leftcenterstage

    $ setWait(17.14,22.77)
    $ speak(JECKA, "What the fuck do we have to talk about with you? We don't play guitar or drink Rockstar Energy or any of that virgin shit.")
    $ setWait(22.77,24.647)
    $ speak(CRISPIN, "Wait- playing guitar is for virgins?")
    $ setWait(24.647,27.65)
    $ speak(JECKA, "When they look like you? A million percent yeah.")
    $ setWait(27.65,30.027)
    $ speak(CRISPIN, "Well.. if you don't wanna talk...")
    $ setWait(30.027,32.238)
    $ speak(JECKA, "Yeah don\'t let the door hit ya in the JNCOs.")
    show crispin sc1:
        rightcenterstage
        xzoom -1
        linear 3 off_right

    show jecka sc1:
        leftcenterstage
        xzoom -1

    $ setWait(32.238,33.322)
    $ speak(CRISPIN, "I'll see ya 'round, Nicole.")
    $ setWait(33.322,35.491)
    $ speak(NICOLE, "Yeah sure.. Whatever.")
    show kylar sc1 smile:
        off_right
        linear 1.7 rightcenterstage

    $ setWait(35.491,36.659)
    $ speak(KYLAR, "What's up, hos?")
    $ setWait(36.659,39.704)
    $ speak(NICOLE, "It's like a revolving door of people who idolize John Cena.")
    $ setWait(39.704,40.746)
    $ speak(JECKA, "What do you want?")
    $ setWait(40.746,43.791)
    $ speak(KYLAR, "Oh just seeing what you were doing this weekend, if you wanted to hang out.")
    $ setWait(43.791,45.418)
    $ speak(JECKA, "Why? Why me?")
    show kylar sc1:
        rightcenterstage
    $ setWait(45.418,47.753)
    $ speak(KYLAR, "I don't know you look kinda good I guess.")
    $ setWait(47.753,49.547)
    $ speak(NICOLE, "This is like a text message in real life.")
    show jecka sc1:
        xzoom 1
        leftcenterstage
    $ setWait(49.547,51.883)
    $ speak(JECKA, "Yeah it's like trauma: live in concert.")
    $ setWait(51.883,54.302)
    $ speak(KYLAR, "But yeah I said you look good, so you wanna do it?")

    show jecka sc1 angry:
        leftcenterstage
        xzoom -1

    $ setWait(54.302,59.348)
    $ speak(JECKA, "Just good? No- I'm fucking gorgeous! If I killed someone I'd be a sex symbol overnight!")
    $ setWait(59.348,60.725)
    $ speak(NICOLE, "Actually true.")
    $ setWait(60.725,61.767)
    $ speak(KYLAR, "So is that a yes?")
    $ setWait(61.767,62.56)
    $ speak(JECKA, "No!")

    show kylar sc1 angry:
        rightcenterstage

    $ setWait(62.56,65.897)
    $ speak(KYLAR, "What the fuck? If you don't say yes I'm gonna knock your teeth in!")
    $ setWait(65.897,68.649)
    $ speak(JECKA, "Wow if this was 1950 you'd get away with it too.")
    show burleday 1 angry:
        off_right
        linear 2 rightmidstage

    $ setWait(68.649,70.276)
    $ speak(BURLEDAY, "Okay that's enough Kylar!")
    show kylar sc1 angry:
        xzoom -1
        rightcenterstage
    $ setWait(70.276,73.029)
    $ speak(KYLAR, "Shut the fuck up you four-eyed Fruit Loop eatin' bitch!")
    $ setWait(73.029,74.488)
    $ speak(BURLEDAY, "You are way out of line!")
    show jecka sc1 smile:
        leftcenterstage
        xzoom -1

    $ setWait(74.488,75.489)
    $ speak(JECKA, "And out of bitches.")
    show kylar sc1 angry:
        xzoom 1
        rightcenterstage

    show jecka sc1:
        leftcenterstage
        xzoom -1

    $ setWait(75.489,78.409)
    $ speak(KYLAR, "Shut up whore! I know where you live I'll fuckin' stab you!")
    $ setWait(78.409,80.87)
    $ speak(BURLEDAY, "That's it! You're going to the school therapist!")
    show burleday 1 angry:
        rightmidstage
        linear 4 off_right

    show kylar sc1 angry:
        rightcenterstage
        xzoom -1
        linear 6.5 off_right

    $ setWait(80.87,83.706)
    $ speak(BURLEDAY, "We'll see what she has to say about these threats!")
    $ setWait(83.706,87.251)
    $ speak(KYLAR, "School therapist? Aw fuck that book-reading bitch!")
    show nicole sc1 surprised:
        leftmidstage

    $ setWait(87.251,89.629)
    $ speak(NICOLE, "\"She\"? Did the counselor finally get fired?")
    show jecka sc1:
        leftcenterstage
        xzoom 1

    $ setWait(89.629,94.55)
    $ speak(JECKA, "No the therapist. They hired her to help the counselor over winter break, at least that's what I heard.")
    show nicole sc1:
        leftmidstage

    $ setWait(94.55,97.803)
    $ speak(NICOLE, "Do you think she's a pedophile like the counselor? Maybe that's why she got the job.")
    $ setWait(97.803,98.888)
    $ speak(JECKA, "Like nepotism?")
    $ setWait(98.888,100.389)
    $ speak(NICOLE, "More like \"pedotism\".")
    $ setWait(100.389,103.601)
    $ speak(JECKA, "Well she's a girl so statistically no.")
    $ setWait(103.601,106.479)
    $ speak(NICOLE, "Yeah I guess there's nothing to worry about...")
    $ setWait(106.479,111.817)
    $ speak(JECKA, "How fucked up would it be if the one female pedophile in existence ended up the other counselor here?")
    $ setWait(111.817,114.487)
    $ speak(NICOLE, "Well it's the only consensual sex Kylar would ever get.")
    $ setWait(114.487,117.114)
    $ speak(JECKA, "No he was held back a year, I think he's 18.")
    show nicole sc1:
        leftmidstage
        xzoom -1
        linear 3.2 off_farleft

    show jecka sc1:
        leftcenterstage
        linear 3.2 off_left
    $ setWait(117.114,120.284)
    $ speak(NICOLE, "Shucks, virgin for life then. Legal virgin.")
    stop ambient fadeout 1.5
    jump scene_S0059

label scene_S0059:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0059.mp3")
    play ambient "audio/Ambience/Classroom_Ambience_2.mp3" fadein 1
    scene classroom int 5
    show lynn:
        leftstage
        xzoom -1

    show jeffery sc1:
        leftcenterstage

    show emily sc1:
        rightcenterstage

    show jecka sc2:
        rightmidstage

    show hunter sc1:
        rightstage

    $ setWait(0.039,6.921)
    $ speak(LYNN, "As you might have noticed, I'll be filling in for your usual health teacher to go over our seminar on bullying.")
    $ setWait(6.921,9.299)
    $ speak(JEFFERY, "Aw finally.")
    $ setWait(9.299,10.592)
    $ speak(JECKA, "Taxes pay for this.")
    $ setWait(10.592,18.558)
    $ speak(LYNN, "Now you might not see it as all that serious but there's been a steep uptick in bullying over the last 10 years.")
    $ setWait(18.558,20.018)
    $ speak(EMILY, "How do you count that?")
    $ setWait(20.018,23.813)
    $ speak(JECKA, "Yeah has it actually gone up or do you just report it more after Columbine?")
    $ setWait(23.813,26.9)
    $ speak(JEFFERY, "No way, it's definitely gone up.")
    show emily sc1 upset:
        rightcenterstage
    $ setWait(26.9,29.194)
    $ speak(EMILY, "That's really cool that you think that.")

    show jecka sc2 smile:
        rightmidstage

    show hunter sc1 smile:
        rightstage

    $ setWait(29.194,32.113)
    $ speak(LYNN, "See? That right there is why it's a problem!")
    $ setWait(32.113,32.947)
    $ speak(EMILY, "What??")
    show jecka sc2:
        rightmidstage

    show hunter sc1:
        rightstage
    $ setWait(32.947,38.036)
    $ speak(LYNN, "Passive aggressive remarks like that are the bullying that led to the columbine shooting.")
    $ setWait(38.036,41.122)
    $ speak(HUNTER, "Are you comparing Jeffery to the columbine shooters?")
    $ setWait(41.122,45.126)
    $ speak(LYNN, "Jeffery's bullying is no different from any other student in America.")
    $ setWait(45.126,49.088)
    $ speak(JECKA, "It's literally Jeffery, who cares? Like we'd bully the Columbine shooters.")
    show emily sc1 smile:
        rightcenterstage
    $ setWait(49.088,51.257)
    $ speak(EMILY, "Yeah I'd fuck the shit out of the Columbine shooters.")
    $ setWait(51.257,52.175)
    $ speak(LYNN, "Excuse me?")
    show emily sc1 upset:
        rightcenterstage
    $ setWait(52.175,56.262)
    $ speak(EMILY, "They killed people, that's cool. All Jeffery does is bring toys to lunch.")
    show jeffery sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(56.262,59.516)
    $ speak(JEFFERY, "They're not toys! It's Magic The Gathering cards!")
    $ setWait(59.516,63.228)
    $ speak(EMILY, "How 'bout you magically gather some friends, bitch?")
    show emily sc1:
        rightcenterstage

    show jeffery sc1:
        leftcenterstage
        xzoom 1

    $ setWait(63.228,72.237)
    $ speak(LYNN, "That's exactly what I mean! Would anyone like to take a guess of how many bullying incidents occur in America per day??")
    $ setWait(72.237,73.279)
    $ speak(HUNTER, "Like five?")
    $ setWait(73.279,77.408)
    $ speak(LYNN, "Thirty... Six... Hundred!")
    show emily sc1 smile:
        rightcenterstage

    show hunter sc1 smile:
        rightstage
    $ setWait(77.408,79.953)
    $ speak(JECKA, "...Is Jeffery half of those?")
    $ setWait(79.953,85.416)
    $ speak(LYNN, "I don't think you get it. You're only here for 7 hours a day, can you do the math?")
    show emily sc1:
        rightcenterstage

    show hunter sc1:
        rightstage

    $ setWait(85.416,86.501)
    $ speak(HUNTER, "I thought this was health.")
    $ setWait(86.501,92.715)
    $ speak(LYNN, "It means every 7 seconds, a K through 12 student is bullied.")
    $ setWait(92.715,95.301)
    $ speak(HUNTER, "Huh... Hey Jeffery.")
    show jeffery sc1:
        leftcenterstage
        xzoom -1

    $ setWait(95.301,95.885)
    $ speak(JEFFERY, "Yeah?")
    $ setWait(95.885,98.179)
    $ speak(HUNTER, "Fuck you. It's been 7 seconds.")
    $ setWait(98.179,99.389)
    $ speak(EMILY, "Damn true.")
    $ setWait(99.389,101.015)
    $ speak(JECKA, "Emily shut your ho ass up.")
    show emily sc1 angry:
        rightcenterstage
        xzoom -1

    $ setWait(101.015,102.308)
    $ speak(EMILY, "What?? You wanna fight!?")
    show jecka sc2 smile:
        rightmidstage

    $ setWait(102.308,103.977)
    $ speak(JECKA, "No, it's been 7 seconds.")
    show emily sc1 smile:
        rightcenterstage

    $ setWait(103.977,106.479)
    $ speak(EMILY, "Oh damn now I'm gonna shoot up the school.")
    $ setWait(106.479,107.939)
    $ speak(LYNN, "Hey! That isn't funny!")
    $ setWait(107.939,109.524)
    $ speak(HUNTER, "Then why did I laugh?")
    show lynn:
        leftstage
        xzoom -1
        pause 1
        xzoom 1
        linear 0.75 off_left

    show jeffery sc1:
        leftcenterstage
        xzoom 1

    $ setWait(109.524,112.735)
    $ speak(LYNN, "That's it! Just Unbelievable!")
    show jecka sc2:
        rightmidstage

    show emily sc1:
        rightcenterstage
        xzoom -1


    $ setWait(112.735,116.531)
    $ speak(JECKA, "...She didn't really punish us. Should we just keep bullying people?")
    $ setWait(116.531,118.783)
    $ speak(EMILY, "Yeah they can't expel all of us.")
    $ setWait(118.783,120.994)
    $ speak(JECKA, "Cool- Yeah you should fucking die, Jeffery.")
    show emily sc1:
        rightcenterstage
        xzoom 1
    $ setWait(120.994,123.288)
    $ speak(EMILY, "Family tree ends with you, Harry Potter watcher.")
    show jeffery sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(123.288,125.79)
    $ speak(JEFFERY, "Hey that was a lot sooner than 7 seconds!")
    $ setWait(125.79,127.667)
    $ speak(JECKA, "No we just actually mean it.")
    stop ambient fadeout 1.5
    jump scene_S0060

label scene_S0060:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0060.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1.2
    scene school ext 2
    show nicole sc2:
        leftcenterstage

    show jecka sc3:
        rightcenterstage

    show trody sc1:
        leftstage

    $ setWait(0.083,4.921)
    $ speak(NICOLE, "So then he was outside of my house at 1AM texting a play-by-play of what's in my front yard.")
    $ setWait(4.921,7.131)
    $ speak(JECKA, "And you didn't call the police?")
    $ setWait(7.131,8.633)
    $ speak(NICOLE, "Uh I was bored.")
    $ setWait(8.633,10.885)
    $ speak(JECKA, "Could be worse, you could be failing history.")
    $ setWait(10.885,12.512)
    $ speak(NICOLE, "Yeah cause that'll get you murdered.")
    $ setWait(12.512,15.556)
    $ speak(JECKA, "Maybe by my parents. They want me in some amazing college.")
    $ setWait(15.556,19.268)
    $ speak(NICOLE, "Yeah the big colleges have a whole stadium that fratboys can molest you in.")
    $ setWait(19.268,23.731)
    $ speak(JECKA, "I'm basically accepting I'll end up a victim where ever I go so it may as well be expensive.")
    show trody sc1:
        leftstage
        pause 0.3
        linear 0.3 leftmidstage

    show kylar sc2 smile:
        off_left
        xzoom -1
        linear 0.4 leftstage


    $ setWait(23.731,24.774)
    $ speak(KYLAR, "Hey bitchlike!")
    $ setWait(24.774,25.733)
    $ speak(TRODY, "What was that for??")
    show kylar sc2 smile:
        xzoom 1
        leftstage
        linear 0.7 off_left
    $ setWait(25.733,26.859)
    $ speak(KYLAR, "It's been 7 seconds.")
    show trody sc1:
        leftmidstage
        linear 0.8 off_left

    $ setWait(26.859,28.736)
    $ speak(TRODY, "Aw dude, not straight!")
    show kelly sc1:
        off_farright
        linear 6 off_left

    show karen sc1 sad:
        off_right
        linear 6 off_farleft

    $ setWait(28.736,31.406)
    $ speak(KELLY, "Karen why do you dress like a mom going through menopause?")
    $ setWait(31.406,32.657)
    $ speak(KAREN, "Is that necessary??")
    $ setWait(32.657,34.701)
    $ speak(KELLY, "Yeah, it's been 7 seconds.")
    show crispin sc2 smile:
        xzoom -1
        off_left
        linear 1.2 off_right

    show jecka sc3:
        rightcenterstage
        pause 0.8
        xzoom -1

    $ setWait(34.701,37.161)
    $ speak(CRISPIN, "Hey watch out, guys! Haha.")
    $ setWait(37.161,39.58)
    $ speak(NICOLE, "Why does he have a Razor scooter in 2008?")
    show jecka sc3 angry:
        rightcenterstage
        xzoom -1

    $ setWait(39.58,41.541)
    $ speak(JECKA, "Yeah what the fuck is this? Toys R Us?")
    $ setWait(41.541,43.084)
    $ speak(NICOLE, "I'm like genuinely upset.")
    show jecka sc3:
        xzoom 1

    $ setWait(43.084,46.421)
    $ speak(JECKA, "You wanna do something about? It's been a lot more than 7 seconds.")
    $ setWait(46.421,48.506)
    $ speak(NICOLE, "I don't know, I don't wanna get involved.")
    show jecka sc3 angry:
        rightcenterstage
    $ setWait(48.506,52.885)
    $ speak(JECKA, "Why are you like this lately? You used to love messing with people, it feels like I'm doing all the work.")
    $ setWait(52.885,53.845)
    $ speak(NICOLE, "Don't worry about it.")
    show jecka sc3 surprised:
        xzoom -1
        rightcenterstage

    $ setWait(53.845,55.346)
    $ speak(JECKA, "Oh wait he's coming back around.")
    $ setWait(55.346,56.472)
    $ speak(NICOLE, "What're you gonna do?")
    show jecka sc3 smile:
        rightcenterstage
        xzoom -1
        pause 2
        linear 0.3 xalign 0.7
        linear 0.3 rightcenterstage
    $ setWait(56.472,59.183)
    $ speak(JECKA, "The question is, what's this stick gonna do?")
    show crispin sc2 smile:
        off_farright
        xzoom 1
        pause 0.76
        linear 0.3 centerstage
    $ setWait(59.183,60.184)
    $ speak(CRISPIN, "Yo hey again!")

    show jecka sc3:
        rightcenterstage
        xzoom 1

    show nicole sc2:
        leftcenterstage
        pause 0.3
        xzoom -1

    show crispin sc2:
        xzoom 1
        centerstage
        ycenter 540
        parallel:
            linear 0.4 off_left
        parallel:
            linear 1 ycenter 1800

    $ setWait(60.184,62.687)
    $ speak(CRISPIN, "Whoa! Agh!")

    show nicole sc2 smile:
        leftcenterstage
        xzoom -1

    $ setWait(62.687,63.896)
    $ speak(NICOLE, "Oh damn that was cool.")
    $ setWait(63.896,66.315)
    $ speak(CRISPIN, "Shit ugh- My leg! Ow!")
    $ setWait(66.315,67.734)
    $ speak(JECKA, "Nice Spongebob impression.")
    $ setWait(67.734,71.487)
    $ speak(CRISPIN, "No for real! I think I actually broke my leg!")
    $ setWait(71.487,73.072)
    $ speak(JECKA, "...Nice Spongebob impression.")
    show lynn:
        xzoom -1
        off_left
        linear 0.7 leftmidstage
        xzoom 1
    $ setWait(73.072,74.991)
    $ speak(LYNN, "What is the m-- Oh my god!")
    $ setWait(74.991,76.701)
    $ speak(CRISPIN, "Ugh my foot's numb too!")
    $ setWait(76.701,81.08)
    $ speak(LYNN, "Why on earth would someone just throw a stick in the middle of the sidewalk?")
    $ setWait(81.08,83.458)
    $ speak(NICOLE, "I mean it's been more than 7 seconds, right?")

    show nicole sc2:
        leftcenterstage
        xzoom -1

    show lynn:
        xzoom -1

    $ setWait(83.458,86.002)
    $ speak(LYNN, "Ugh you kids don't listen to anything-- that's it!")
    $ setWait(86.002,86.711)
    $ speak(JECKA, "What's it?")
    $ setWait(86.711,92.3)
    $ speak(LYNN, "All this bullying's led to a student breaking their leg! This calls for drastic measures!")
    $ setWait(92.3,93.593)
    $ speak(NICOLE, "Like calling an ambulance?")
    show lynn:
        leftmidstage
        xzoom -1
        pause 4.5
        xzoom 1
        linear 1 off_left

    $ setWait(93.593,100.85)
    $ speak(LYNN, "From now on there's going to be very strict anti-bullying mandates around here! Then we'll see how funny it is!")
    $ setWait(100.85,103.061)
    $ speak(JECKA, "...I guess she's not calling an ambulance.")
    $ setWait(103.061,106.23)
    $ speak(CRISPIN, "Hey c-can you guys help me get to the nurse?")
    $ setWait(106.23,108.649)
    $ speak(JECKA, "Why would I help a white cripple? 7 seconds.")
    $ setWait(108.649,110.818)
    $ speak(CRISPIN, "But she just said she banned bullying here.")
    $ setWait(110.818,112.779)
    $ speak(JECKA, "No? She's about to ban bullying.")
    show nicole sc2 smile:
        leftcenterstage
        xzoom -1
    $ setWait(112.779,114.489)
    $ speak(NICOLE, "Yeah get it in while you can.")
    stop ambient fadeout 2
    jump scene_S0061

label scene_S0061:
    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.7 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0061.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1

    scene cafeteria int
    show jecka sc4 surprised:
        rightcenterstage

    show nicole sc3 surprised:
        leftcenterstage

    $ setWait(0.047,2.758)
    $ speak(JECKA, "Did she actually do assigned seating for lunch?")
    $ setWait(2.758,6.012)
    $ speak(NICOLE, "Did she actually put us together for assigned seating?")
    show jecka sc4:
        rightcenterstage

    show nicole sc3:
        leftcenterstage

    $ setWait(6.012,9.348)
    $ speak(JECKA, "No there's gotta be a catch. Did you see who else was at Table 12?")
    $ setWait(9.348,13.144)
    $ speak(NICOLE, "I just looked for our names and left, way too afraid to see who else they stuck us with.")
    $ setWait(13.144,16.606)
    $ speak(JECKA, "What if it's not even a student? Like they just get the janitor to sit with us.")
    $ setWait(16.606,18.649)
    $ speak(NICOLE, "Do you think the janitor would also be a pedophile?")
    $ setWait(18.649,21.611)
    $ speak(JECKA, "It's not like he had to commit to be here, he's just a janitor.")
    $ setWait(21.611,25.239)
    $ speak(NICOLE, "Yeah you gotta really wanna fuck kids to finish a bachelors to be around them.")
    $ setWait(25.239,27.992)
    $ speak(JECKA, "That's good to say in public- who is gonna sit here?")
    show jeffery sc3 smile:
        off_left
        xzoom -1
        linear 2.2 leftmidstage

    $ setWait(27.992,32.038)
    $ speak(JEFFERY, "Hey guys, do you mind if I draw Sento Takahashi fan art in front of you?")
    show nicole sc3:
        xzoom -1
        leftcenterstage
    $ setWait(32.038,33.247)
    $ speak(NICOLE, "Assigned seating, Jeffery.")
    $ setWait(33.247,35.708)
    $ speak(JECKA, "Yeah so you're gonna have to go somewhere else, sorry.")
    show jeffery sc3:
        leftmidstage
        xzoom -1
    $ setWait(35.708,38.044)
    $ speak(JEFFERY, "I know it's assigned, table 12 right?")
    show nicole sc3 surprised:
        leftcenterstage
        xzoom 1
    $ setWait(38.044,39.128)
    $ speak(NICOLE, "Is this table 12?")
    show jecka sc4 sad:
        rightcenterstage
    $ setWait(39.128,40.254)
    $ speak(JECKA, "Yeah it's 12.")
    show nicole sc3 angry:
        leftcenterstage
        xzoom -1
    $ setWait(40.254,41.38)
    $ speak(NICOLE, "Man fuck 12!")
    $ setWait(41.38,43.09)
    $ speak(JECKA, "Do you really have to sit here, Jeffery?")
    $ setWait(43.09,46.761)
    $ speak(JEFFERY, "Yes I do. I don't wanna break the rules and get expelled.")
    $ setWait(46.761,50.139)
    $ speak(NICOLE, "Rules that were entirely created just for you and two other people.")
    show jeffery sc3 smile:
        leftmidstage
        xzoom -1
    $ setWait(50.139,53.851)
    $ speak(JEFFERY, "Okay let's draw Hikari-chan.")
    show jecka sc4:
        rightcenterstage
    $ setWait(53.851,56.354)
    $ speak(JECKA, "But yeah have you seen a white guy work at Chipotle yet?")
    show nicole sc3:
        xzoom 1
        leftcenterstage
    $ setWait(56.354,57.73)
    $ speak(NICOLE, "Actually no.")
    $ setWait(57.73,60.024)
    $ speak(JEFFERY, "My cousin works at a Chipotle in Maryland.")
    $ setWait(60.024,61.233)
    $ speak(JECKA, "We weren't asking you--")
    show jecka sc4 surprised:
        rightcenterstage

    show nicole sc3:
        leftcenterstage
        xzoom -1

    show jeffery sc3:
        leftmidstage
        xzoom -1
    $ setWait(61.233,62.818)
    $ speak(JECKA, "What are you drawing??")
    show drawing onlayer screens
    $ setWait(62.818,68.866)
    $ speak(JEFFERY, "I told you, I was drawing Hikarichan from Sento Takahashi's Girls Free-For-All!")
    $ setWait(68.866,71.494)
    $ speak(NICOLE, "That was a lot of really heterosexual words.")
    show jecka sc4:
        rightcenterstage
    $ setWait(71.494,75.539)
    $ speak(JECKA, "D-Does Sento Hakamoshi actually draw it that shitty?")
    hide drawing onlayer screens
    $ setWait(75.539,77.416)
    $ speak(JEFFERY, "No. Wha-- Hey!")
    $ setWait(77.416,78.959)
    $ speak(NICOLE, "What's the actual thing look like?")
    $ setWait(78.959,82.922)
    $ speak(JEFFERY, "Luckily I have volume 6 of the manga with her on the front cover.")
    show manga onlayer screens
    $ setWait(82.922,83.756)
    $ speak(NICOLE, "Whoa.")
    $ setWait(83.756,86.217)
    $ speak(JECKA, "Damn she got some big ass fuckin' titties, Jeffery.")
    $ setWait(86.217,92.056)
    $ speak(JEFFERY, "I know, but I don't just like her for that! She's really strong and determined to fight for her friends.")
    $ setWait(92.056,95.267)
    $ speak(JECKA, "This is like virgin nerd version of \"I can fix her\".")
    $ setWait(95.267,96.894)
    $ speak(NICOLE, "How does she even fight with those?")
    hide manga onlayer screens
    $ setWait(96.894,100.022)
    $ speak(JEFFERY, "She does a lot of cool moves, you'd just have to read it.")
    $ setWait(100.022,101.107)
    $ speak(JECKA, "Cool moves?")
    $ setWait(101.107,102.525)
    $ speak(NICOLE, "Sucks and fucks, duh.")
    show jeffery sc3 angry:
        leftmidstage
        xzoom -1
    $ setWait(102.525,106.987)
    $ speak(JEFFERY, "No! It's a really intricate story without any of that naughty stuff!")
    $ setWait(106.987,111.492)
    $ speak(JECKA, "Why do all these animes have hot girls in a porn-level plot without the sex?")
    $ setWait(111.492,113.911)
    $ speak(NICOLE, "So people afraid of growing up have something to beat off to.")
    $ setWait(113.911,121.293)
    $ speak(JEFFERY, "No her backstory's good! When Hikari-chan was a young girl she escaped from an orphanage ran by the evil Kage Clan!")
    show jeffery sc3 smile:
        leftmidstage
        xzoom -1
    $ setWait(121.293,126.1)
    $ speak(JEFFERY, "Then she trained in martial arts and sorcery until she was allowed to join the rebellion...")
    $ setWait(126.1,127.508)
    $ speak(JEFFERY, "...at the age of 13.")
    show nicole sc3 surprised:
        leftcenterstage
        xzoom -1

    show jecka sc4 sad:
        rightcenterstage

    show jeffery sc3:
        leftmidstage
        xzoom -1
    $ setWait(127.508,128.342)
    $ speak(NICOLE, "13!?")
    $ setWait(128.342,132.388)
    $ speak(JECKA, "Why does a 13 year old look like she's ready to suck and fuck her way through an HBO pilot??")
    show jeffery sc3 angry:
        leftmidstage
        xzoom -1
    $ setWait(132.388,136.016)
    $ speak(JEFFERY, "It's a work of fantasy, there's no HBO in her universe!")
    show nicole sc3:
        leftcenterstage
        xzoom -1
    $ setWait(136.016,137.309)
    $ speak(NICOLE, "Yeah that's what she was getting at.")
    $ setWait(137.309,140.771)
    $ speak(JECKA, "God I wish I had tits like that at 13, then I wouldn't have failed algebra.")
    $ setWait(140.771,145.276)
    $ speak(NICOLE, "Jeffery, you don't think it's a little statutory for a 13 year old to look like that?")

    $ setWait(145.276,148.195)
    $ speak(JEFFERY, "Look like what? She can't help how her body is.")
    $ setWait(148.195,152.7)
    $ speak(JEFFERY, "If someone touched you inappropriately would you want 'em to say your body makes it your fault?")
    $ setWait(152.7,156.62)
    $ speak(NICOLE, "Oh yeah that's a really good point... Except for one little part...")
    show jeffery sc3:
        leftmidstage
        xzoom -1
    $ setWait(156.62,157.204)
    $ speak(JEFFERY, "What?")
    show nicole sc3 angry:
        leftcenterstage
        xzoom -1

    show jecka sc4 angry:
        rightcenterstage

    $ setWait(157.204,158.33)
    $ speak(NICOLE, "She's not real!")

    $ setWait(158.33,163.085)
    $ speak(JECKA, "Yeah some fucked-up lonely Asian guy drew that in his parents' basement cause he wanted her to look like that.")
    show jeffery sc3 angry:
        leftmidstage
        xzoom -1
    $ setWait(163.085,167.798)
    $ speak(JEFFERY, "Ugh wasn't the point of arranged seating that I wouldn't get bullied anymore? I'm gonna tell.")
    show nicole sc3 surprised:
        leftcenterstage
        xzoom -1
    $ setWait(167.798,169.383)
    $ speak(NICOLE, "No! Wait! We support it.")
    $ setWait(169.383,171.135)
    $ speak(JEFFERY, "Support what?")
    $ setWait(171.135,174.68)
    $ speak(NICOLE, "You loving this imaginary 13 year old girl.")
    $ setWait(174.68,176.515)
    $ speak(JEFFERY, "Both of you?")
    show jecka sc4 sad:
        rightcenterstage
    $ setWait(176.515,180.895)
    $ speak(JECKA, "If I say \"no\" I'll get expelled... If I say \"yes\" I'll go to jail...")
    stop ambient fadeout 1.5
    jump scene_S0062

label scene_S0062:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show home nicole ext day with Pause(2.633):
        zoom 0.75 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.633 zoom 0.79 truecenter
    $ setVoiceTrack("audio/Scenes/0062.mp3")
    scene home nicole int
    play ambient "audio/Ambience/House_Ambience.mp3"
    show nicole sc3 sad:
        leftmidstage

    show jecka sc4:
        leftcenterstage

    $ setWait(2.633,5.844)
    $ speak(NICOLE, "I don't know, you ever feel like the girl from Nightmare Before Christmas?")
    $ setWait(5.844,10.307)
    $ speak(JECKA, "No I don't watch dumb shit for ugly girls who can only be pretty by being alternative.")
    show nicole sc3:
        leftmidstage
    $ setWait(10.307,12.601)
    $ speak(NICOLE, "Damn that kinda ruins my depression tangent.")
    $ setWait(12.601,15.312)
    $ speak(JECKA, "Like you think I'd watch a cartoon after the age of 9.")
    $ setWait(15.312,16.396)
    $ speak(NICOLE, "What about Family Guy?")
    $ setWait(16.396,18.398)
    $ speak(JECKA, "That's not a cartoon, it's for adults.")
    $ setWait(18.398,19.233)
    $ speak(NICOLE, "Are you sure?")
    show jecka sc4 angry:
        leftcenterstage
    $ setWait(19.233,22.486)
    $ speak(JECKA, "Why would it reference the 80's so much if it wasn't for adults??")
    $ setWait(22.486,26.782)
    $ speak(NICOLE, "Yeah I guess Jack Skellington never talks about MTV or why he hates minorities.")
    show jecka sc4:
        leftcenterstage
    $ setWait(26.782,28.492)
    $ speak(JECKA, "They don't talk about that on Family Guy.")
    $ setWait(28.492,29.409)
    $ speak(NICOLE, "Talk about what?")
    $ setWait(29.409,30.327)
    $ speak(JECKA, "MTV.")
    show brother upset:
        off_right
        linear 2 rightmidstage

    show jecka sc4:
        leftcenterstage
        pause 0.5
        xzoom -1
    $ setWait(30.327,32.746)
    $ speak(BROTHER, "God I can never have the house to myself.")
    $ setWait(32.746,34.748)
    $ speak(NICOLE, "What are you so fat now you fill all the rooms up?")
    $ setWait(34.748,38.919)
    $ speak(BROTHER, "No! I just like peace and quiet when mackin' on these online bitches!")
    show nicole sc3 sad:
        leftmidstage

    $ setWait(38.919,41.171)
    $ speak(NICOLE, "Oh my god is our house gonna end up on Dateline again?")
    $ setWait(41.171,44.049)
    $ speak(JECKA, "Dateline? What do you like teenage girls or something?")
    show brother:
        rightmidstage

    $ setWait(44.049,47.803)
    $ speak(BROTHER, "Uh... When you say \"teenage\", how old are we talking here?")
    show jecka sc4 sad:
        leftcenterstage
        xzoom -1

    $ setWait(47.803,50.097)
    $ speak(JECKA, "That was way more words than \"no\".")

    show brother upset:
        rightmidstage

    $ setWait(50.097,53.141)
    $ speak(BROTHER, "Why is everyone a god damn ageist!?")
    $ setWait(53.141,55.894)
    $ speak(NICOLE, "Dude nobody cares, just go in your basement and prey on children.")
    show brother upset:
        rightmidstage
        linear 5.5 off_farleft

    $ setWait(55.894,57.688)
    $ speak(BROTHER, "Fine, dumb bitch.")
    $ setWait(57.688,62.276)
    $ speak(BROTHER, "And they're not children, they're overdeveloped middle schoolers.")
    show jecka sc4:
        xzoom 1
        leftcenterstage

    $ setWait(62.276,64.486)
    $ speak(JECKA, "That's... That's swell.")
    show nicole sc3 smile:
        leftmidstage
    $ setWait(64.486,68.782)
    $ speak(NICOLE, "Oh you know what would actually cure my depression? Marilyn Manson's gonna be in town.")
    $ setWait(68.782,69.658)
    $ speak(JECKA, "At MCI?")
    $ setWait(69.658,70.576)
    $ speak(NICOLE, "Next Friday.")
    $ setWait(70.576,72.661)
    $ speak(JECKA, "I thought you wanted to see Marilyn Manson.")
    show nicole sc3:
        leftmidstage

    $ setWait(72.661,73.328)
    $ speak(NICOLE, "I do.")
    $ setWait(73.328,75.163)
    $ speak(JECKA, "Then why'd you bring up the Ice Cube movie?")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(75.163,77.708)
    $ speak(NICOLE, "No- Not Next Friday the movie, next friday the time.")
    show jecka sc4 smile:
        leftcenterstage
    $ setWait(77.708,79.459)
    $ speak(JECKA, "Oh got you, yeah let's do it.")
    show nicole sc3 smile:
        leftmidstage
    $ setWait(79.459,83.255)
    $ speak(NICOLE, "Cool, and I know a guy who can get us ecstasy so it's gonna be an extra good concert.")
    $ setWait(83.255,85.465)
    $ speak(JECKA, "What does that do? Is it like PCP?")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(85.465,88.927)
    $ speak(NICOLE, "No it's not like fucking PCP. That's for like the saddest drug addicts.")
    show jecka sc4:
        leftcenterstage

    $ setWait(88.927,91.805)
    $ speak(JECKA, "So is ecstasy for the happiest drug addicts?")
    show nicole sc3 smile:
        leftmidstage
    $ setWait(91.805,92.931)
    $ speak(NICOLE, "Literally yes.")
    $ setWait(92.931,94.099)
    $ speak(JECKA, "Oh cool I'm down.")
    $ setWait(94.099,95.934)
    $ speak(NICOLE, "Plus Marilyn's just a great show anyway.")
    show jecka sc4 smile:
        leftcenterstage

    $ setWait(95.934,98.395)
    $ speak(JECKA, "Yeah he's kinda hot in a \"kidnap me\" sort of way.")
    $ setWait(98.395,102.357)
    $ speak(NICOLE, "He's like the one man on Earth I want to trap me in a hotel room and sexually abuse me.")
    $ setWait(102.357,105.902)
    $ speak(JECKA, "Yeah you seen the Youtube videos where he just goes on stage and says that?")
    $ setWait(105.902,110.157)
    $ speak(NICOLE, "What is it about fame and money that makes us wanna ignore a man's flagrant warning signs?")
    $ setWait(110.157,113.66)
    $ speak(JECKA, "Cause a rockstar traumatizing you is something to actually brag about?")
    $ setWait(113.66,116.997)
    $ speak(NICOLE, "True. Letting a Denny's cook do that just makes you feel worthless.")
    show cop:
        off_right
        linear 0.55 rightmidstage

    show jecka sc4:
        leftcenterstage
        pause 0.5
        xzoom -1

    show nicole sc3:
        leftmidstage

    $ setWait(116.997,120.417)
    $ speak(COP, "This is the county police, we have a warrant to search this residence!")
    $ setWait(120.417,122.669)
    $ speak(NICOLE, "Oh yeah, what you're looking for's in the basement.")
    $ setWait(122.669,125.005)
    $ speak(COP, "But I haven't made you aware of the charges.")
    $ setWait(125.005,126.131)
    $ speak(JECKA, "Oh we're aware.")
    show cop:
        rightmidstage
        linear 2.5 off_left

    $ setWait(126.131,127.799)
    $ speak(COP, "Just a moment.")
    show nicole sc3 smile:
        leftmidstage

    show jecka sc4 smile:
        leftcenterstage
        xzoom 1

    $ setWait(127.799,132.429)
    $ speak(NICOLE, "But yeah Manson could like cut me with broken glass and lick the blood off, it's cool cause he's famous.")
    $ setWait(132.429,136.224)
    $ speak(JECKA, "Yeah I want some rockstar welts all over my ass so I can show off at the mental ward.")
    $ setWait(136.224,137.476)
    $ speak(NICOLE, "Actually same.")
    $ setWait(137.476,138.685)
    $ speak(JECKA, "Can you get us backstage?")
    show nicole sc3:
        leftmidstage
    $ setWait(138.685,141.188)
    $ speak(NICOLE, "No I can't afford the drugs and the VIP.")
    $ setWait(141.188,144.524)
    $ speak(JECKA, "Oh well hopefully he sees how hot we are and picks us out of the crowd.")
    $ setWait(144.524,145.901)
    $ speak(NICOLE, "Bitch we're on the upper level.")
    show jecka sc4:
        leftcenterstage

    $ setWait(145.901,148.362)
    $ speak(JECKA, "Yeah he'd need a whole telescope to notice us.")
    show brother upset:
        xalign -0.51
        linear 5 xalign 1.01

    show cop:
        off_left
        linear 5 rightstage



    $ setWait(148.362,150.072)
    $ speak(BROTHER, "I-I didn't do anything wrong!!")
    $ setWait(150.072,154.076)
    $ speak(COP, "Tell it to the judge! That girl barely looked 12!")
    $ setWait(154.076,156.87)
    $ speak(NICOLE, "Yeah do you think your dad could give us money for better seats?")
    $ setWait(156.87,159.331)
    $ speak(JECKA, "Seats? My dad won't even give me the time of day.")
    $ setWait(159.331,164.795)
    $ speak(COP, "You're under arrest for 3 counts of digital misconduct with a minor and 2 counts of child pornography!")
    show brother upset:
        xalign 1.01
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.02
        linear 0.1 xalign .99
        linear 0.1 xalign 1.01
    $ setWait(164.795,168.256)
    $ speak(BROTHER, "No that was an 18 year old midget in my \"hot kids\" folder!")
    $ setWait(168.256,169.216)
    $ speak(NICOLE, "Dude your dad's lame--")
    $ setWait(169.216,170.258)
    $ speak(COP, "Tell it to the judge!")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(170.258,173.22)
    $ speak(NICOLE, "Hey can you guys keep it down? We're trying to have a conversation in here.")
    show jecka sc4 angry:
        leftcenterstage
        xzoom -1
    $ setWait(173.22,174.137)
    $ speak(JECKA, "Yeah honestly.")
    $ setWait(174.137,174.93)
    $ speak(COP, "Oh sorry!")
    $ setWait(174.93,176.056)
    $ speak(BROTHER, "You're not gonna help me??")
    $ setWait(176.056,178.183)
    $ speak(COP, "You're gonna have to tell it to the judge, let's go.")

    show cop:
        rightstage
        linear 5 off_farright

    show brother upset:
        xalign 1.01
        linear 5 xalign 1.49


    $ setWait(178.183,183.271)
    $ speak(BROTHER, "It was an 18 year old midget!!!")
    show jecka sc4:
        leftcenterstage
        xzoom 1
    $ setWait(183.271,185.941)
    $ speak(JECKA, "Yeah my dad would never just give me money for a better concert.")
    hide cop
    hide brother upset
    $ setWait(185.941,188.652)
    $ speak(NICOLE, "That makes me feel a lot less bad about my Dad killing himself.")
    show jecka sc4 angry:
        leftcenterstage
    $ setWait(188.652,190.821)
    $ speak(JECKA, "Bitch you didn't fuckin' feel bad in the first place.")
    $ setWait(190.821,191.905)
    $ speak(NICOLE, "You don't know that.")
    show jecka sc4 sad:
        leftcenterstage
    $ setWait(191.905,194.324)
    $ speak(JECKA, "I guess you do wear a lot of stud belts.")
    show nicole sc3 smile:
        leftmidstage
    $ setWait(194.324,195.617)
    $ speak(NICOLE, "So next friday?")
    show jecka sc4 smile:
        leftcenterstage
    $ setWait(195.617,197.828)
    $ speak(JECKA, "Yeah next friday, not the Ice Cube movie.")
    stop ambient fadeout 1.5
    jump scene_S0063

label scene_S0063:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show title_dayslater onlayer screens:
        alpha 0.0
        linear 0.7 alpha 1.0
    show school front with Pause(2.46):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.46 zoom 1.05 truecenter
    $ setVoiceTrack("audio/Scenes/0063.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3"
    scene classroom int 3
    hide title_dayslater onlayer screens

    show jecka sc5:
        rightstage

    show karen sc2:
        rightmidstage

    show ari sc1:
        leftmidstage
        xzoom -1

    show megan sc1:
        leftstage
        xzoom -1

    show katz 2:
        centerstage

    $ setWait(2.46,10.259)
    $ speak(KATZ, "And so y'know, that's why Malcolm X was a little uh.. controversial.. in his time.")
    $ setWait(10.259,12.804)
    $ speak(KATZ, "Any other questions? Ari.")
    show ari sc1 think:
        leftmidstage
        xzoom -1

    $ setWait(12.804,14.555)
    $ speak(ARI, "Do you really live alone with your pets?")
    show katz 2 angry:
        centerstage
        pause 3.25
        xzoom -1

    show ari sc1:
        leftmidstage
        xzoom -1

    $ setWait(14.555,18.726)
    $ speak(KATZ, "Questions about AP History?? Karen.")
    show karen sc2 sad:
        rightmidstage

    show katz 2:
        centerstage
        xzoom -1
    $ setWait(18.726,22.73)
    $ speak(KAREN, "I-Is it okay for you to use the N-word when reading those civil rights quotes?")
    $ setWait(22.73,28.194)
    $ speak(KATZ, "Okay it's just history.. Purely historical.. Not a big deal.")
    show karen sc2:
        rightmidstage

    show jecka sc5 smile:
        rightstage
    $ setWait(28.194,31.113)
    $ speak(JECKA, "Yeah you were like Rick Ross with the hard R.")
    show katz 2 angry:
        centerstage
        xzoom -1

    show ari sc1 smile:
        leftmidstage
        xzoom -1
        pause 0.4
        xzoom 1
        linear 2 off_left

    show megan sc1:
        leftstage
        pause 0.3
        xzoom 1
        linear 1.1 off_left

    show karen sc2:
        rightmidstage
        pause 0.2
        linear 4 off_left

    show jecka sc5:
        rightstage
        pause 0.2
        linear 1.2 rightmidstage

    $ setWait(31.113,33.658)
    $ speak(KATZ, "Y'know what Jecka, you can stay after!")
    show jecka sc5 angry:
        rightmidstage

    $ setWait(33.658,34.867)
    $ speak(JECKA, "Oh my god- over that??")
    $ setWait(34.867,36.702)
    $ speak(KATZ, "We need to have a little talk.")
    hide megan sc1
    hide ari sc1 smile
    hide karen sc2
    show jecka sc5 sad:
        rightmidstage
    $ setWait(36.702,38.746)
    $ speak(JECKA, "This feels like a big talk.")
    show katz 2:
        centerstage
        xzoom -1
    $ setWait(38.746,41.123)
    $ speak(KATZ, "What do you think you've been doing here this semester?")
    show jecka sc5:
        rightmidstage

    $ setWait(41.123,44.043)
    $ speak(JECKA, "What do I think? Or what's the reality?")
    $ setWait(44.043,50.716)
    $ speak(KATZ, "All this talking out of turn and spacing out is truly unbecoming of an AP student.")
    $ setWait(50.716,53.177)
    $ speak(JECKA, "I thought AP stood for Already Perfect.")
    $ setWait(53.177,56.931)
    $ speak(KATZ, "Evidently not. Your grades have been slipping too, what's wrong with you?")
    $ setWait(56.931,58.641)
    $ speak(JECKA, "If I knew that I wouldn't be in school.")
    $ setWait(58.641,64.522)
    $ speak(KATZ, "Just all this horsing around and lack of homework.. is there something you need to tell me?")
    show jecka sc5 sad:
        rightmidstage
        xzoom -1

    $ setWait(64.522,67.275)
    $ speak(JECKA, "Uh what'll get me out of this...")
    show jecka sc5 smile:
        rightmidstage
        xzoom 1
    $ setWait(67.275,68.568)
    $ speak(JECKA, "I'm basically in love with you.")
    show katz 2 sad:
        centerstage
        xzoom -1
    $ setWait(68.568,69.485)
    $ speak(KATZ, "What??")
    show jecka sc5 flirt:
        rightmidstage

    $ setWait(69.485,73.03)
    $ speak(JECKA, "Yeah, I-I just wanted you to notice me.")
    $ setWait(73.03,79.161)
    $ speak(JECKA, "Those Asics you wear every day regardless of whether you're running or not are such a turn on.")
    show katz 2 weird:
        centerstage
        xzoom -1
    $ setWait(79.161,80.663)
    $ speak(KATZ, "Uh, really?")
    $ setWait(80.663,85.668)
    $ speak(JECKA, "Uh huh, I just got in trouble to be alone with my favorite teacher.")
    $ setWait(85.668,88.379)
    $ speak(KATZ, "And you favorite teacher is...")
    $ setWait(88.379,89.714)
    $ speak(JECKA, "You, yep.")
    $ setWait(89.714,92.55)
    $ speak(KATZ, "I-I don't know what to say uh...")
    show jecka sc5 sad:
        rightmidstage
    $ setWait(92.55,95.553)
    $ speak(JECKA, "That this isn't school appropriate and I should run along?")
    show katz 2 smile:
        centerstage
        xzoom -1
    $ setWait(95.553,97.179)
    $ speak(KATZ, "Are you doing anything tonight?")
    show jecka sc5 surprised:
        rightmidstage
    $ setWait(97.179,98.681)
    $ speak(JECKA, "Oh uh...")
    show jecka sc5:
        rightmidstage
    $ setWait(98.681,100.641)
    $ speak(JECKA, "I might try klonopin, I don't know.")
    show katz 2 weird:
        centerstage
        xzoom -1
    $ setWait(100.641,105.521)
    $ speak(KATZ, "No I meant are uh, are you going anywhere for dinner?")
    $ setWait(105.521,108.524)
    $ speak(JECKA, "No just my usual Ritz crackers and Nutella.")
    $ setWait(108.524,112.028)
    $ speak(KATZ, "How would you feel about going out to dinner with me?")
    show jecka sc5 sad:
        rightmidstage
        pause 0.7
        xzoom -1
    $ setWait(112.028,113.613)
    $ speak(JECKA, "With you? Oh fuck..")
    show katz 2 angry:
        centerstage
        xzoom -1

    $ setWait(113.613,116.157)
    $ speak(KATZ, "You weren't lying were you?")

    show jecka sc5:
        rightmidstage
        xzoom 1
    $ setWait(116.157,118.242)
    $ speak(JECKA, "Oh no, where we goin'?")
    show katz 2 smile:
        centerstage
        xzoom -1
    $ setWait(118.242,122.204)
    $ speak(KATZ, "Somewhere very very fancy. Within reason of course.")
    $ setWait(122.204,126.125)
    $ speak(JECKA, "Oh yeah totally. Like a date?")
    show katz 2:
        centerstage
        xzoom -1
    $ setWait(126.125,128.461)
    $ speak(KATZ, "That's what you want, right?")
    $ setWait(128.461,131.714)
    $ speak(JECKA, "Uh, will you spend lots of money on me too?")
    $ setWait(131.714,133.883)
    $ speak(KATZ, "How much is a lot of money?")
    $ setWait(133.883,135.718)
    $ speak(JECKA, "Like will you buy me cigarettes?")
    $ setWait(135.718,136.719)
    $ speak(KATZ, "Sure.")
    $ setWait(136.719,137.929)
    $ speak(JECKA, "American Spirits?")
    show katz 2 angry:
        centerstage
        xzoom -1
    $ setWait(137.929,139.138)
    $ speak(KATZ, "Well hold on now-")
    show jecka sc5 sad:
        rightmidstage

    $ setWait(139.138,146.103)
    $ speak(JECKA, "It's the only cigarette my Mom lets me smoke cause I'm 1/128th Cherokee.. I think.")
    show katz 2:
        centerstage
        xzoom -1
    $ setWait(146.103,147.897)
    $ speak(KATZ, "But you're serious about this, right?")
    show jecka sc5:
        rightmidstage
    $ setWait(147.897,150.107)
    $ speak(JECKA, "Yeah totally, if it saves my grade.")
    show katz 2 weird:
        centerstage
        xzoom -1
    $ setWait(150.107,156.238)
    $ speak(KATZ, "Meet me after school in the cafeteria and that can be arranged over our fancy little dinner.")
    $ setWait(156.238,159.367)
    $ speak(JECKA, "Alright cool. S-see ya later.")
    show katz 2 smile:
        centerstage
        xzoom -1
        linear 3 off_right
    $ setWait(159.367,161.16)
    $ speak(KATZ, "I'll see you too.")
    show jecka sc5 sad:
        rightmidstage
        linear 4 off_left

    $ setWait(161.16,163.996)
    $ speak(JECKA, "Why didn't they have a Fresh Prince episode on dating your teacher?")
    stop ambient fadeout 1.5
    jump scene_S0064

label scene_S0064:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0064.mp3")
    play ambient "audio/Ambience/hallway_Ambience.mp3" fadein 1
    scene school int 1
    show nicole sc4:
        leftcenterstage

    show crispin sc3 smile:
        rightcenterstage

    $ setWait(0.043,7.092)
    $ speak(CRISPIN, "Yeah yeah that's cool that you like guitars. I've been thinking about getting a ukulele cause it's like heh, pretty manly.")
    $ setWait(7.092,10.47)
    $ speak(NICOLE, "Wow you're definitely not the first person to make that joke.")
    $ setWait(10.47,13.807)
    $ speak(CRISPIN, "I really wanna play it at parties, I think it'd be funny.")
    show jecka sc5:
        off_right
        linear 2.8 rightmidstage
    $ setWait(13.807,15.058)
    $ speak(JECKA, "Oh hey.")
    $ setWait(15.058,16.101)
    $ speak(NICOLE, "You got out kinda late.")
    show crispin sc3 smile:
        rightcenterstage
        xzoom -1
    $ setWait(16.101,17.561)
    $ speak(CRISPIN, "Aw yeah you get in trouble--")
    show crispin sc3:
        rightcenterstage
        xzoom -1

    show jecka sc5 angry:
        rightmidstage
    $ setWait(17.561,20.939)
    $ speak(JECKA, "Shut the fuck up! Die! Die in a plane crash!")
    show crispin sc3:
        xzoom 1
        rightcenterstage
        linear 3.5 off_left

    $ setWait(20.939,23.191)
    $ speak(CRISPIN, "Heh that's... whatever.")
    show jecka sc5 angry:
        rightmidstage
        linear 0.7 rightcenterstage

    $ setWait(23.191,25.443)
    $ speak(JECKA, "Holy shit, you can't tell him to fuck off??")
    $ setWait(25.443,27.654)
    $ speak(NICOLE, "Long story. Why'd he hold you late?")
    show jecka sc5:
        rightcenterstage

    $ setWait(27.654,31.575)
    $ speak(JECKA, "Mr. Katz was mad I'm failing and making fun of him at the same time.")
    hide crispin sc3
    $ setWait(31.575,33.577)
    $ speak(NICOLE, "Yeah you usually just get one or the other.")
    $ setWait(33.577,37.08)
    $ speak(JECKA, "So he got all on my case and I had to flirt with him to go easy on me for the quarter.")
    $ setWait(37.08,39.124)
    $ speak(NICOLE, "Oh yeah, acting out for him to notice you?")
    $ setWait(39.124,44.379)
    $ speak(JECKA, "Yeah always works. But this time it worked a little too good.")
    $ setWait(44.379,45.338)
    $ speak(NICOLE, "Did he whip it out?")
    $ setWait(45.338,46.59)
    $ speak(JECKA, "He asked me out to dinner.")
    $ setWait(46.59,50.468)
    $ speak(NICOLE, "Damn, dinner on a teacher's salary? That's gotta suck some khaki ass.")
    $ setWait(50.468,52.387)
    $ speak(JECKA, "He said it'd be really really fancy.")
    show nicole sc4 angry:
        leftcenterstage
    $ setWait(52.387,54.347)
    $ speak(NICOLE, "Fuckin' Boston Market's fancy to him.")
    show jecka sc5 sad:
        rightcenterstage

    $ setWait(54.347,57.475)
    $ speak(JECKA, "Whatever but yeah so I guess I gotta do that tonight.")
    show nicole sc4 surprised:
        leftcenterstage

    $ setWait(57.475,58.643)
    $ speak(NICOLE, "Do what tonight?")
    $ setWait(58.643,60.27)
    $ speak(JECKA, "Date my literal teacher?")
    show nicole sc4 sad:
        leftcenterstage
    $ setWait(60.27,62.48)
    $ speak(NICOLE, "But it's Friday, we have the concert tonight!")
    show jecka sc5 surprised:
        rightcenterstage

    $ setWait(62.48,64.107)
    $ speak(JECKA, "You said that was next Friday!")
    show nicole sc4 angry:
        leftcenterstage

    $ setWait(64.107,66.234)
    $ speak(NICOLE, "Today's next Friday! I told you this week.")
    show jecka sc5 angry:
        rightcenterstage

    $ setWait(66.234,69.654)
    $ speak(JECKA, "No today's this Friday! Don't tell me it's next Friday when it's this Friday!")
    $ setWait(69.654,71.865)
    $ speak(NICOLE, "I didn't think you'd be doing anything either Friday!")
    $ setWait(71.865,75.702)
    $ speak(JECKA, "Me neither but as of 10 minutes ago this is the busiest Friday of my whole life!")
    show trody sc1:
        off_left
        xzoom -1
        linear 1 leftstage
    $ setWait(75.702,77.662)
    $ speak(TRODY, "Hey are we talking about the Ice Cube movie?")
    $ setWait(77.662,79.372)
    $ speak(JECKA, "No we're talking about the restaurant.")
    show trody sc1:
        leftstage
        xzoom -1
        pause 1.2
        xzoom 1
        linear 0.8 off_left
    $ setWait(79.372,82.459)
    $ speak(TRODY, "Aw fuck Friday's, they cancelled endless appetizers.")
    show nicole sc4 sad:
        leftcenterstage

    $ setWait(82.459,88.214)
    $ speak(NICOLE, "But you're seriously not gonna go to this? I got the tickets and everything! This is the one thing in my life I've actually planned!")
    show jecka sc5 sad:
        rightcenterstage

    $ setWait(88.214,89.799)
    $ speak(JECKA, "Is it really the end of the world?")
    $ setWait(89.799,92.761)
    $ speak(NICOLE, "It's the end of my world! What world ends if you fail history?")
    show jecka sc5:
        rightcenterstage
    $ setWait(92.761,96.306)
    $ speak(JECKA, "History's a core class, you need that to graduate and have a future??")
    $ setWait(96.306,99.643)
    $ speak(NICOLE, "History's literally \"been there, done that\" that's like the opposite of the future!")
    show jecka sc5 sad:
        rightcenterstage
    $ setWait(99.643,103.521)
    $ speak(JECKA, "Yeah but now if he gets stood up he's definitely gonna fail me for the year!")
    $ setWait(103.521,105.273)
    $ speak(NICOLE, "Just tell the principal he's trying to molest you.")
    $ setWait(105.273,108.276)
    $ speak(JECKA, "We did that like 5 times this year, they're not gonna believe that anymore.")
    show nicole sc4 angry:
        leftcenterstage
    $ setWait(108.276,111.446)
    $ speak(NICOLE, "But it was true all 5 times!")
    $ setWait(111.446,115.367)
    $ speak(JECKA, "Look... Is this like an ultimatum?")
    show nicole sc4 sad:
        leftcenterstage
    $ setWait(115.367,119.496)
    $ speak(NICOLE, "I can't tell you that but like...")
    show nicole sc4:
        leftcenterstage
    $ setWait(119.496,121.831)
    $ speak(NICOLE, "So what's it gonna be?")

    menu:
        "FRIENDS FIRST":
            jump scene_S0065
        "FUTURE FIRST":

            jump scene_S0082

label scene_S0065:
    $ setVoiceTrack("audio/Scenes/0065.mp3")
    scene school int 1
    show nicole sc4:
        leftcenterstage

    show jecka sc5 sad:
        rightcenterstage
    $ setWait(0.039,1.874)
    $ speak(JECKA, "You really think it's gonna be that good?")
    $ setWait(1.874,5.544)
    $ speak(NICOLE, "I wouldn't spend money on it if it wasn't. I'd just sneak in for free.")
    show jecka sc5 angry:
        rightcenterstage
    $ setWait(5.544,7.63)
    $ speak(JECKA, "I better get really fuckin' high while I'm at this thing.")
    show nicole sc4 smile:
        leftcenterstage

    $ setWait(7.63,8.839)
    $ speak(NICOLE, "No don't worry I got you.")
    $ setWait(8.839,13.135)
    $ speak(JECKA, "Cause if I have a single coherent thought while I'm out there it's gonna ruin my whole night.")
    $ setWait(13.135,14.053)
    $ speak(NICOLE, "So you're going?")
    $ setWait(14.053,15.137)
    $ speak(JECKA, "Yeah I guess so!")
    $ setWait(15.137,20.81)
    $ speak(NICOLE, "Cool. Yeah don't worry about Mr. Katz, you can just apologize and compliment how he dresses like Steve Jobs later.")
    show jecka sc5:
        rightcenterstage
    $ setWait(20.81,22.77)
    $ speak(JECKA, "Yeah all he needs is the turtleneck.")
    show nicole sc4:
        leftcenterstage

    $ setWait(22.77,25.815)
    $ speak(NICOLE, "So I'm gonna walk to the gas station, just drive to my house at 7.")
    $ setWait(25.815,28.401)
    $ speak(JECKA, "Why would you go to the gas station when you don't have a car?")
    $ setWait(28.401,30.903)
    $ speak(NICOLE, "Oh yeah that's where White Marvin sells all his shit.")

    $ setWait(30.903,33.572)
    $ speak(JECKA, "Who- Why do you call him \"White Marvin\"?")
    $ setWait(33.572,35.241)
    $ speak(NICOLE, "Cause he's white and named Marvin.")
    show jecka sc5 surprised:
        rightcenterstage
    $ setWait(35.241,36.784)
    $ speak(JECKA, "No fuckin' way, actually?")
    $ setWait(36.784,39.286)
    $ speak(NICOLE, "Yeah he's like 1 of 20 white Marvins on earth.")
    show jecka sc5 sad:
        rightcenterstage
    $ setWait(39.286,41.247)
    $ speak(JECKA, "I thought it was just cause he sold coke or whatever.")
    $ setWait(41.247,45.126)
    $ speak(NICOLE, "No he does that too. When you're white and named Marvin there aren't a whole lot of options for ya.")
    $ setWait(45.126,49.171)
    $ speak(JECKA, "Yeah it's either sell drugs or fix rides at the carnival.")
    show ari domino:
        off_right
        pause 0.44
        linear 0.393 xalign 0.7
    $ setWait(49.171,49.964)
    $ speak(ARI, "I'm gonna be late.")
    show ari domino think:
        xalign 0.7
        linear 0.25 rightmidstage

    show jecka sc5 surprised:
        rightcenterstage
        linear 0.08 xalign .61
        linear 0.08 xalign .65
        linear 0.08 xalign .61
        linear 0.08 xalign .65
        linear 0.08 xalign .61
        linear 0.08 rightcenterstage
    $ setWait(49.964,50.297)
    $ speak(ARI, "Ugh!")
    show jecka sc5 angry:
        rightcenterstage
        xzoom -1

    $ setWait(50.297,51.882)
    $ speak(JECKA, "Ow bitch! Watch where you're going!")
    show ari domino sad:
        rightmidstage

    $ setWait(51.882,52.466)
    $ speak(ARI, "Sorry!")
    $ setWait(52.466,53.843)
    $ speak(NICOLE, "What're you in a rush for?")
    $ setWait(53.843,57.096)
    $ speak(ARI, "I'm late to my job at Domino's. It's only my second day!")
    show jecka sc5:
        rightcenterstage
        xzoom -1
    $ setWait(57.096,58.848)
    $ speak(JECKA, "Why would you work at a Domino's?")
    show ari domino:
        rightmidstage

    $ setWait(58.848,62.017)
    $ speak(ARI, "Cause I need money? It's not that bad, I just do deliveries.")
    $ setWait(62.017,64.353)
    $ speak(NICOLE, "You drive to random dude's houses alone?")
    $ setWait(64.353,66.73)
    $ speak(ARI, "Well how else do they get their Chicken Kickers?")
    $ setWait(66.73,68.524)
    $ speak(JECKA, "Someone's gonna actaully kill you.")
    $ setWait(68.524,73.028)
    $ speak(NICOLE, "Yeah what if some guy falls in love with you and keeps ordering Chicken Kickers until you show up again?")
    show ari domino think:
        rightmidstage

    $ setWait(73.028,74.572)
    $ speak(ARI, "There's actually one guy who does that.")
    $ setWait(74.572,75.364)
    $ speak(NICOLE, "See??")
    show ari domino:
        rightmidstage

    $ setWait(75.364,79.16)
    $ speak(ARI, "Well no he's like 400 pounds so I'm pretty sure it's just for the Chicken Kickers.")
    $ setWait(79.16,80.786)
    $ speak(JECKA, "Oh that's what they all say.")
    show ari domino angry:
        rightmidstage
        linear 2.2 off_left
    $ setWait(80.786,82.872)
    $ speak(ARI, "Lazy bitches.")
    show jecka sc5 sad:
        rightcenterstage
        xzoom 1
    $ setWait(82.872,86.417)
    $ speak(JECKA, "Is she right? I'm literally picking a concert over school.")
    $ setWait(86.417,93.966)
    $ speak(NICOLE, "You're picking a concert over dating some loser 3 times older than you. If anything a Marilyn Manson concert's way more work cause you'll be sweating the whole time.")
    $ setWait(93.966,95.301)
    $ speak(JECKA, "Cause of the ecstasy, right?")
    show nicole sc4 smile:
        leftcenterstage
    $ setWait(95.301,98.053)
    $ speak(NICOLE, "No, all the dancing you do while you're on the ecstasy.")
    show jecka sc5 smile:
        rightcenterstage
    $ setWait(98.053,99.93)
    $ speak(JECKA, "I can't wait to be a concert cutaway girl.")
    $ setWait(99.93,103.142)
    $ speak(NICOLE, "I can't wait to get fucked up and black out in a Chevy's parking lot.")
    $ setWait(103.142,104.602)
    $ speak(JECKA, "You better get those beans then.")
    show nicole sc4 smile:
        leftcenterstage
        pause 1
        xzoom -1
        linear 3 off_left
    $ setWait(104.602,107.354)
    $ speak(NICOLE, "For real- okay I'm gonna go do that now, see ya later.")
    show jecka sc5 smile:
        rightcenterstage
        linear 3.05 rightmidstage
    $ setWait(107.354,110.483)
    $ speak(JECKA, "Yeah see ya at 7...")
    show jecka sc5 sad:
        xzoom -1
        rightmidstage
        linear 3.4 off_right

    $ setWait(110.483,112.443)
    $ speak(JECKA, "...What am I doing with my life?")
    stop ambient fadeout 2.1
    jump scene_S0066

label scene_S0066:
    show black onlayer screens with Pause(2.3):
        alpha 0.0
        linear 1.9 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Hood_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show concert ext with Pause(3.001):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 3.001 zoom 0.55 truecenter
    $ setVoiceTrack("audio/Scenes/0066.mp3")
    play ambient "audio/Ambience/Venue_Ambience.mp3"
    scene concert
    show nicole sc4:
        leftmidstage

    show jecka sc5:
        leftcenterstage

    $ setWait(3.001,4.67)
    $ speak(JECKA, "This isn't Marilyn Manson.")
    $ setWait(4.67,6.463)
    $ speak(NICOLE, "No this is just the opening act.")
    $ setWait(6.463,9.925)
    $ speak(JECKA, "Oh well gimme the X now so it kicks in when he goes on.")
    show nicole sc4 sad:
        leftmidstage
    $ setWait(9.925,11.134)
    $ speak(NICOLE, "About that...")
    show jecka sc5 angry:
        leftcenterstage

    $ setWait(11.134,13.512)
    $ speak(JECKA, "No... I'm not doing this sober!")
    $ setWait(13.512,14.846)
    $ speak(NICOLE, "Don't worry I got plan B.")
    $ setWait(14.846,16.515)
    $ speak(JECKA, "You think I'm gonna fuck someone here?")
    show nicole sc4 angry:
        leftmidstage
    $ setWait(16.515,18.517)
    $ speak(NICOLE, "No- Plan B the backup plan!")
    $ setWait(18.517,19.976)
    $ speak(JECKA, "What happened to plan A??")
    show nicole sc4 sad:
        leftmidstage

    $ setWait(19.976,21.978)
    $ speak(NICOLE, "White Marvin kinda flaked on me.")
    $ setWait(21.978,25.649)
    $ speak(JECKA, "Drug dealers are like the most unreliable people, they never show up on time.")
    show nicole sc4:
        leftmidstage
    $ setWait(25.649,28.193)
    $ speak(NICOLE, "Yeah especially not when they're in jail.")

    show jecka sc5 surprised:
        leftcenterstage

    $ setWait(28.193,29.695)
    $ speak(JECKA, "Really? What's he in for?")
    $ setWait(29.695,32.739)
    $ speak(NICOLE, "Identity theft, turns out he wasn't actually named Marvin.")
    show jecka sc5:
        leftcenterstage
    $ setWait(32.739,34.783)
    $ speak(JECKA, "Damn. So what's plan B?")
    $ setWait(34.783,38.328)
    $ speak(NICOLE, "I went to Rite Aid on the way home and got a bunch of Robitussin and Benadryl.")
    show jecka sc5 sad:
        leftcenterstage
    $ setWait(38.328,41.164)
    $ speak(JECKA, "You wanna robotrip at a Marilyn Manson concert??")
    $ setWait(41.164,43.25)
    $ speak(NICOLE, "That's like asking me if I need air to breathe.")
    $ setWait(43.25,45.794)
    $ speak(JECKA, "Isn't that gonna make it like 5 times scarier?")
    $ setWait(45.794,49.464)
    $ speak(NICOLE, "That's kinda the point. Otherwise we're gonna be bored for 2 hours.")
    show jecka sc5:
        leftcenterstage
    $ setWait(49.464,51.508)
    $ speak(JECKA, "Just rip the seal off for me.")
    show nicole sc4:
        leftmidstage
        pause 0.4
        linear 0.2 xalign 0.22
        linear 0.2 leftmidstage

    $ setWait(51.508,52.509)
    $ speak(NICOLE, "Yeah here ya go.")

    $ setWait(52.509,55.22)
    $ speak(JECKA, "Thanks...")
    show jecka sc5 sad:
        leftcenterstage
    $ setWait(55.22,57.222)
    $ speak(JECKA, "Ugh it's always so nasty.")
    $ setWait(57.222,60.142)
    $ speak(NICOLE, "Yeah every Robitussin tastes like Diet Robitussin.")
    show emily sc2 angry:
        off_right
        linear 2.2 rightcenterstage

    show jecka sc5:
        leftcenterstage
        pause 0.5
        xzoom -1

    $ setWait(60.142,62.144)
    $ speak(EMILY, "What're you guys doing here?")
    $ setWait(62.144,63.77)
    $ speak(NICOLE, "Nothing technically illegal.")
    $ setWait(63.77,64.73)
    $ speak(JECKA, "What do you want?")
    $ setWait(64.73,68.316)
    $ speak(EMILY, "Since when do you guys like Marilyn Manson, you're wasting those tickets!")
    show jecka sc5 angry:
        leftcenterstage
        xzoom -1
    $ setWait(68.316,69.818)
    $ speak(JECKA, "I like Marilyn Manson!")
    $ setWait(69.818,71.695)
    $ speak(EMILY, "Name 5 of his songs, poser!")
    $ setWait(71.695,73.488)
    $ speak(JECKA, "I don't have time for that. Why don't you?")
    $ setWait(73.488,77.617)
    $ speak(EMILY, "I had the time to buy all of his albums, EPs, and singles!")
    $ setWait(77.617,78.869)
    $ speak(NICOLE, "Dude he's not that good.")
    $ setWait(78.869,80.454)
    $ speak(EMILY, "See I knew you were a poser!")
    show nicole sc4 angry:
        leftmidstage

    $ setWait(80.454,81.413)
    $ speak(NICOLE, "No we're not.")
    $ setWait(81.413,82.581)
    $ speak(EMILY, "Prove it!")
    show jecka sc5 angry:
        leftcenterstage
        xzoom 1
        pause 1
        xzoom -1
    $ setWait(82.581,87.586)
    $ speak(JECKA, "Uh... we go to his concerts even when we're deathly sick! That's how dedicated we are!")
    $ setWait(87.586,90.422)
    $ speak(NICOLE, "Yeah you see all the Robitussin she needs to even stand?")
    show emily sc2 sad:
        rightcenterstage
        linear 0.6 xalign 0.7

    $ setWait(90.422,91.757)
    $ speak(EMILY, "Ohhh shit..")
    $ setWait(91.757,93.8)
    $ speak(JECKA, "Yeah so fuck off.")
    show emily sc2 angry:
        xalign 0.7
        linear 1.8 rightstage
        xzoom -1
        linear 1.4 off_right
    $ setWait(93.8,97.137)
    $ speak(EMILY, "Alright fine, but I'll be watching.")
    show jecka sc5 angry:
        leftcenterstage
        xzoom 1
    $ setWait(97.137,99.89)
    $ speak(JECKA, "I thought that was just shit guys do when they think a girl's hot.")
    show nicole sc4:
        leftmidstage

    $ setWait(99.89,102.601)
    $ speak(NICOLE, "Yeah but I'm pretty sure Emily's gay so it checks out.")
    show jecka sc5 surprised:
        leftcenterstage
    $ setWait(102.601,104.186)
    $ speak(JECKA, "No way, how can you tell?")
    $ setWait(104.186,109.399)
    $ speak(NICOLE, "Cause all white girls are either really gay or really racist, there's no inbetween.")
    show jecka sc5 sad:
        leftcenterstage
    $ setWait(109.399,110.609)
    $ speak(JECKA, "Which one are we?")
    $ setWait(110.609,111.777)
    $ speak(NICOLE, "To be determined.")
    show jecka sc5:
        leftcenterstage

    $ setWait(111.777,113.445)
    $ speak(JECKA, "Whatever, pass the Benadryl.")
    stop ambient fadeout 1.5
    jump scene_S0067

label scene_S0067:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka night with Pause(2.668):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.668 zoom 1.05 truecenter
    $ setVoiceTrack("audio/Scenes/0067.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene livingroom jecka night

    show black onlayer screens:
        alpha 0.2

    show jecka sc5 sad:
        off_left
        xzoom -1
        linear 4 leftcenterstage


    $ setWait(2.668,7.339)
    $ speak(JECKA, "Aww fuck... Let's just.. just get in bed.")
    hide black onlayer screens

    scene livingroom jecka
    show dad undershirt upset:
        off_farright
        linear 1.6 rightmidstage

    show jecka sc5 sad:
        leftcenterstage
        xzoom -1

    $ setWait(7.339,8.549)
    $ speak(DAD, "Where were you??")
    show jecka sc5 surprised:
        leftcenterstage
        xzoom -1

    $ setWait(8.549,10.676)
    $ speak(JECKA, "Oh shit- who're you again?")
    $ setWait(10.676,12.011)
    $ speak(DAD, "Your father?")
    $ setWait(12.011,14.93)
    $ speak(JECKA, "Fuck- I can't even like.. register facial features.")
    $ setWait(14.93,16.932)
    $ speak(DAD, "What were you doing out all night!?")

    $ setWait(16.932,19.643)
    $ speak(JECKA, "It's uhhh... Concert.")
    show dad undershirt angry:
        rightmidstage

    $ setWait(19.643,24.565)
    $ speak(DAD, "A concert? You think you can go to a concert after failing history!?")
    $ setWait(24.565,25.566)
    $ speak(JECKA, "Wait- What?")
    $ setWait(25.566,31.363)
    $ speak(DAD, "Your history teacher gave me a phone call saying you missed a benchmark exam that would save your grade for the year!")

    show jecka sc5 sad:
        leftcenterstage
        xzoom -1

    $ setWait(31.363,33.949)
    $ speak(JECKA, "No he just wanted to date I didn't go!")
    $ setWait(33.949,39.288)
    $ speak(DAD, "You think you can keep up this shit up in the real world? You know what they do to girls like you in the real world??")
    $ setWait(39.288,39.872)
    $ speak(JECKA, "What?")
    show dad undershirt yell:
        rightmidstage
        linear 0.4 rightcenterstage

    $ setWait(39.872,41.54)
    $ speak(DAD, "Smack the shit out of you!!")
    $ setWait(41.54,42.249)
    $ speak(JECKA, "Nooooo.")
    $ setWait(42.249,44.585)
    $ speak(DAD, "Beat you into the whorish pulp you are!!")
    show jecka sc5 surprised:
        leftcenterstage
        xzoom 1
    $ setWait(44.585,46.504)
    $ speak(JECKA, "Why is there a spider in the corner of my eye?")
    $ setWait(46.504,48.881)
    $ speak(DAD, "You're not even listening! That's it!")
    show jecka sc5 sad:
        leftcenterstage
        xzoom -1

    show dad undershirt angry:
        rightcenterstage

    $ setWait(48.881,55.095)
    $ speak(DAD, "From now on your free time will be spent on a job instead of this mindless bullshit you get up to every night!")
    $ setWait(55.095,56.806)
    $ speak(JECKA, "I am no condition to work...")
    $ setWait(56.806,60.017)
    $ speak(DAD, "You sure won't be after I break your knees backwards!!")
    show jecka sc5 sad:
        leftcenterstage
        xzoom -1
        linear 0.4 leftmidstage
    $ setWait(60.017,62.019)
    $ speak(JECKA, "Okay okay I'm sorry!")
    show dad undershirt angry:
        rightcenterstage
        xzoom -1
        linear 3.5 off_right
    $ setWait(62.019,66.982)
    $ speak(DAD, "I'll kick your ass to the curb if you're unemployed by Monday!")
    show jecka sc5 sad:
        leftmidstage
        xzoom -1
        linear 3 rightstage
    $ setWait(66.982,68.943)
    $ speak(JECKA, "I hope that wasn't my dad...")
    stop ambient fadeout 1.5
    jump scene_S0068

label scene_S0068:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.15

    $ setVoiceTrack("audio/Scenes/0068.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3" fadein 1
    scene bedroom jecka night
    show jecka pj sad:
        leftstage
        xzoom -1
        linear 4 rightmidstage

    show shadow:
        alpha 0.4
        zoom 4
        ycenter 800
        xcenter 3000
        pause 3.6
        linear 0.7 xcenter -3000


    $ setWait(0.037,4.166)
    $ speak(JECKA, "I'm too fucked up to fall asleep I don't like this...")
    show jecka pj surprised:
        rightmidstage
        xzoom 1
        linear 0.06 xalign .9
        linear 0.06 xalign 0.86
        linear 0.06 xalign 0.9
        linear 0.06 rightmidstage

    show shadow:
        alpha 0.7
        zoom 4
        ycenter 800
        xcenter -3000
        pause 1
        linear 0.6 xcenter 3000
    $ setWait(4.166,5.834)
    $ speak(JECKA, "What was that??")

    show jecka pj sad:
        rightmidstage

    $ setWait(5.834,8.962)
    $ speak(JECKA, "This Benadryl's fuckin' my brain missionary.")
    show shadow:
        ycenter 540
        zoom 1
        leftstage
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 0.3 leftcenterstage


    $ setWait(8.962,10.964)
    $ speak(SHADOW, "Hey how's it going?")
    $ setWait(10.964,13.05)
    $ speak(JECKA, "What are you doing here?")
    $ setWait(13.05,16.553)
    $ speak(SHADOW, "Oh I'm the hat man. You have any Benadryl?")
    $ setWait(16.553,18.388)
    $ speak(JECKA, "No I took it all...")
    $ setWait(18.388,20.849)
    $ speak(SHADOW, "Damn, every time I show up too.")
    $ setWait(20.849,22.643)
    $ speak(JECKA, "Are you gonna kill me?")
    $ setWait(22.643,24.353)
    $ speak(SHADOW, "I could if you want me to.")
    $ setWait(24.353,26.063)
    $ speak(JECKA, "No that's okay.")
    $ setWait(26.063,28.94)
    $ speak(SHADOW, "Ugh... see it's never the good answer.")
    $ setWait(28.94,30.609)
    $ speak(JECKA, "How would you kill me?")
    $ setWait(30.609,34.613)
    $ speak(SHADOW, "Well see I'm made of shadows so I'd have to go into your brain and get you to kill yourself.")
    $ setWait(34.613,36.907)
    $ speak(JECKA, "That's kinda false advertising.")
    $ setWait(36.907,40.202)
    $ speak(SHADOW, "Could you not put me in the same category as McDonald's?")
    $ setWait(40.202,42.287)
    $ speak(JECKA, "When do they false advertise?")
    $ setWait(42.287,51.254)
    $ speak(SHADOW, "The 10 piece McNugget? Sometimes you get the siamese nuggets joined at the breading and they count that as 2 and short change you an extra nugget.")
    $ setWait(51.254,54.174)
    $ speak(JECKA, "I mean I kinda count that as 2 too.")
    $ setWait(54.174,61.431)
    $ speak(SHADOW, "Oh so I get 2 McNuggets, half the crispy breading, and I still gotta pay full price. You're a capitalist, aren't you?")
    $ setWait(61.431,62.599)
    $ speak(JECKA, "Isn't everybody?")
    $ setWait(62.599,66.144)
    $ speak(SHADOW, "You really make me wanna make you kill yourself, you know that?")
    $ setWait(66.144,69.606)
    $ speak(JECKA, "Okay I'll kill myself tomorrow, can you go?")
    show shadow:
        zoom 1
        leftcenterstage
        alpha 1.0
        parallel:
            linear 1 xalign -1.7
        parallel:
            linear 3 zoom 5
        parallel:
            linear 0.8 alpha 0.0

    $ setWait(69.606,72.909)
    $ speak(SHADOW, "I'm stealing the loose change in your car.")
    stop ambient fadeout 2.5
    jump scene_S0069

label scene_S0069:
    show black onlayer screens with Pause(2.3):
        alpha 0.15
        linear 2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0069.mp3")
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1
    scene mall int

    show jecka sc6 angry:
        rightstage
        linear 1 rightcenterstage

    show nicole sc5:
        rightmidstage
        xzoom -1
        linear 1 leftcenterstage
        xzoom 1

    $ setWait(0.001,2.381)
    $ speak(JECKA, "Who the fuck did this to the economy??")
    $ setWait(2.381,3.466)
    $ speak(NICOLE, "Did what?")
    $ setWait(3.466,6.552)
    $ speak(JECKA, "Like, make it shitty or whatever? No one's hiring!")
    $ setWait(6.552,7.845)
    $ speak(NICOLE, "I don't know but they're probably white.")
    $ setWait(7.845,10.89)
    $ speak(JECKA, "Leave it to my Dad to force me to work when I don't even have to.")
    $ setWait(10.89,13.684)
    $ speak(NICOLE, "Yeah work is for ugly bitches who wear Ecko Unltd.")
    $ setWait(13.684,17.771)
    $ speak(JECKA, "We made fun of Ari for delivering Domino's but now I'm the loser getting a job.")
    $ setWait(17.771,19.356)
    $ speak(NICOLE, "Was your dad really that mad?")
    $ setWait(19.356,23.319)
    $ speak(JECKA, "Even after he cooled down he said he wanted to put a tracking chip in my uterus.")
    $ setWait(23.319,24.445)
    $ speak(NICOLE, "How patriotic.")

    show jecka sc6 sad:
        rightcenterstage

    $ setWait(24.445,29.617)
    $ speak(JECKA, "It just feels like a job is this pitfall we eventually fall into. All I wanted was to go to school.")

    show nicole sc5 angry:
        leftcenterstage

    $ setWait(29.617,31.035)
    $ speak(NICOLE, "What do you think school's for??")

    show jecka sc6 angry:
        rightcenterstage


    $ setWait(31.035,35.706)
    $ speak(JECKA, "Eventually getting you a job that's not shitty and hard? Like being a doctor.")
    $ setWait(35.706,37.583)
    $ speak(NICOLE, "Being a doctor is hard.")
    $ setWait(37.583,40.085)
    $ speak(JECKA, "No but it gets you a job that makes you like a millionaire.")
    show nicole sc5:
        leftcenterstage

    $ setWait(40.085,43.756)
    $ speak(NICOLE, "My Mom said doctors start at only $60k a year.")
    $ setWait(43.756,45.591)
    $ speak(JECKA, "Then what the fuck is the point of college??")
    $ setWait(45.591,47.51)
    $ speak(NICOLE, "Hey you're the one that wants to go to school.")

    show jecka sc6 sad:
        rightcenterstage

    $ setWait(47.51,52.097)
    $ speak(JECKA, "It's like the world's set up for us to either live with our parents or live with our future husbands.")

    $ setWait(52.097,54.433)
    $ speak(NICOLE, "Husbands plural? You want two husbands?")
    show jecka sc6:
        rightcenterstage
    $ setWait(54.433,55.935)
    $ speak(JECKA, "No I meant like each of us.")
    show nicole sc5 angry:
        leftcenterstage

    $ setWait(55.935,57.811)
    $ speak(NICOLE, "Bitch you meant wrong, what husband?")
    $ setWait(57.811,60.231)
    $ speak(JECKA, "Alright whatever, I gotta go to Hot Topic now.")

    show nicole sc5:
        leftcenterstage

    $ setWait(60.231,62.608)
    $ speak(NICOLE, "What you gonna find some meek-ass bitch husband there?")
    $ setWait(62.608,64.443)
    $ speak(JECKA, "No, for a job application.")
    show nicole sc5 angry:
        leftcenterstage

    $ setWait(64.443,67.863)
    $ speak(NICOLE, "Dude they're not gonna hire you unless you have like 15 pussy piercings.")
    show jecka sc6 surprised:
        rightcenterstage

    $ setWait(67.863,70.199)
    $ speak(JECKA, "I do not have the real-estate for 15 of those.")

    show nicole sc5:
        leftcenterstage

    $ setWait(70.199,72.493)
    $ speak(NICOLE, "Workplace discrimination's a bitch, huh?")
    show jecka sc6 sad:
        rightcenterstage

    $ setWait(72.493,74.37)
    $ speak(JECKA, "Now I know how it feels to be black.")
    $ setWait(74.37,79.458)
    $ speak(NICOLE, "Yeah I think one of the Beatles made a song about that. \"Woman is the N-word of the world\".")
    $ setWait(79.458,80.834)
    $ speak(JECKA, "The one that hit his kids?")
    $ setWait(80.834,83.254)
    $ speak(NICOLE, "I mean they're 80 now, that's like kinda all of them.")

    show jecka sc6:
        rightcenterstage

    $ setWait(83.254,85.13)
    $ speak(JECKA, "This is why I don't like The Beatles.")
    show nicole sc5 smile:
        leftcenterstage

    $ setWait(85.13,86.84)
    $ speak(NICOLE, "I don't like 'em cause I'm too cool for that.")
    show jecka sc6 angry:
        rightcenterstage
        linear 3.2 off_left

    $ setWait(86.84,89.843)
    $ speak(JECKA, "Alright, stop distracting me. I'm gonna go get my job.")
    show nicole sc5 smile:
        leftcenterstage
        linear 4 off_right

    $ setWait(89.843,92.555)
    $ speak(NICOLE, "I'm gonna get Benadryl from a bathroom vending machine.")
    stop ambient fadeout 1.5
    jump scene_S0070

label scene_S0070:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0070.mp3")
    play ambient "audio/Ambience/HotTopic_Ambience.mp3" fadein 1
    scene hot topic
    show jecka sc6:
        centerstage

    show trody ht:
        leftmidstage
        xzoom -1
    $ setWait(0.045,4.8)
    $ speak(JECKA, "So that's basically why I stole from here 2 years ago.")
    $ setWait(4.8,8.595)
    $ speak(TRODY, "Okay, so what other qualifications do you have to work here?")
    $ setWait(8.595,14.684)
    $ speak(JECKA, "I guess I get pretty good grades. Like I have a C in an AP class, that's pretty much an A in any other class.")
    $ setWait(14.684,15.852)
    $ speak(TRODY, "Yeah good point.")
    $ setWait(15.852,19.773)
    $ speak(JECKA, "Also I really need this job so I'll try to be decent at it maybe.")
    $ setWait(19.773,23.485)
    $ speak(TRODY, "Sounds promising, there's only one issue though.")

    show jecka sc6 surprised:
        centerstage

    $ setWait(23.485,25.028)
    $ speak(JECKA, "Issue? What issue?")
    $ setWait(25.028,26.905)
    $ speak(TRODY, "Well it kinda had to do with--")

    $ setWait(26.905,28.99)
    $ speak(JECKA, "When I said I wasn't looking for a boyfriend- I was just joking!")
    $ setWait(28.99,32.494)
    $ speak(TRODY, "Whoa no hold on, it's a perfectly changeable thing.")
    show jecka sc6:
        centerstage
    $ setWait(32.494,33.912)
    $ speak(JECKA, "Then what?")
    $ setWait(33.912,36.206)
    $ speak(TRODY, "Uh kinda your look.")
    show jecka sc6 sad:
        centerstage
    $ setWait(36.206,38.333)
    $ speak(JECKA, "My... My look??")
    $ setWait(38.333,42.254)
    $ speak(TRODY, "Yeah see usually the girls that work here fit the theme a little better.")
    show jecka sc6 surprised:
        centerstage
        linear 0.4 rightmidstage
    $ setWait(42.254,43.839)
    $ speak(JECKA, "No way I'm getting a piercing there!")
    $ setWait(43.839,44.798)
    $ speak(TRODY, "Wait what?")

    show jecka sc6:
        rightmidstage
        linear 1 centerstage

    $ setWait(44.798,46.049)
    $ speak(JECKA, "Just tell me.")
    $ setWait(46.049,51.263)
    $ speak(TRODY, "You're kinda not like hardcore enough. Hot Topic really prides itself in that.")

    show jecka sc6 angry:
        centerstage

    $ setWait(51.263,55.851)
    $ speak(JECKA, "Wait... You won't hire me cause I'm not emo enough? But look how qualified I am!")
    $ setWait(55.851,58.728)
    $ speak(TRODY, "Yeah I know but it's sort of the store policy.")
    $ setWait(58.728,61.815)
    $ speak(JECKA, "Your store policy supports workplace discrimination?")
    $ setWait(61.815,63.942)
    $ speak(TRODY, "Dude you're white, that's not gonna work.")
    $ setWait(63.942,67.571)
    $ speak(JECKA, "I'm a white woman, thank you. My problems should come first in the world.")
    $ setWait(67.571,71.408)
    $ speak(TRODY, "Look I'm sorry but the boss prefers girls with abusive parents and substance issues.")
    $ setWait(71.408,76.496)
    $ speak(JECKA, "I am literally the living embodiment of that! Just cause I'm too pretty to look emo doesn't mean I'm not emo!")
    $ setWait(76.496,81.209)
    $ speak(TRODY, "Well look your qualifications are good but.. the boss might lean towards another girl.")
    show jecka sc6 angry:
        centerstage
        pause 0.8
        xzoom -1
        linear 1.8 off_right

    $ setWait(81.209,84.087)
    $ speak(JECKA, "Y'know what? Fuck this place!")
    show trody ht smile:
        leftmidstage
        xzoom -1
        linear 6 rightmidstage

    $ setWait(84.087,87.382)
    $ speak(TRODY, "Wait 'till she sees it's Hot Topic that controls the courts.")
    stop ambient fadeout 1.5
    jump scene_S0071

label scene_S0071:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show barcade ext with Pause(2.544):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.544 zoom 0.55 truecenter

    $ setVoiceTrack("audio/Scenes/0071.mp3")
    play ambient "audio/Ambience/barcade_NoMusic_Ambience.mp3"
    scene barcade int
    show nicole sc6:
        leftmidstage

    show emily sc3:
        centerstage

    $ setWait(2.544,4.63)
    $ speak(NICOLE, "Are we really gonna find a sugar daddy here?")
    $ setWait(4.63,9.217)
    $ speak(EMILY, "I told you, there's tons of losers who come in here with so much money to blow on games.")
    $ setWait(9.217,10.385)
    $ speak(NICOLE, "Yeah games.")
    show emily sc3 smile:
        centerstage

    $ setWait(10.385,14.139)
    $ speak(EMILY, "But if we go up to them they'll wanna blow money on us instead.")
    $ setWait(14.139,16.975)
    $ speak(NICOLE, "Half of 'em can barely run, they couldn't blow out a candle.")
    show emo jecka sc1:
        off_right
        linear 1.7 rightmidstage

    $ setWait(16.975,18.018)
    $ speak(JECKA, "What about blowing?")
    show emily sc3:
        xzoom -1
    $ setWait(18.018,18.81)
    $ speak(EMILY, "Do we know you?")
    show nicole sc6 surprised:
        leftmidstage

    $ setWait(18.81,19.811)
    $ speak(NICOLE, "Jecka what the fuck.")
    $ setWait(19.811,22.064)
    $ speak(JECKA, "Sorry I know I said I'd stop doing those jokes.")
    $ setWait(22.064,23.565)
    $ speak(NICOLE, "No- what is your hair??")
    show emily sc3 sad:
        centerstage
        xzoom -1
    $ setWait(23.565,25.692)
    $ speak(EMILY, "Ohhh shit that is Jecka.")

    show emo jecka sc1 sad:
        rightmidstage

    $ setWait(25.692,26.652)
    $ speak(JECKA, "Long story.")
    show emily sc3:
        centerstage
        xzoom -1

    show nicole sc6:
        leftmidstage

    $ setWait(26.652,28.111)
    $ speak(EMILY, "Are you working at Hot Topic?")
    show emo jecka sc1:
        rightmidstage
    $ setWait(28.111,29.571)
    $ speak(JECKA, "Maybe- How'd you know?")
    $ setWait(29.571,35.911)
    $ speak(EMILY, "They make every girl do that. If conventionally attractive people worked there all the fat metalheads would feel insecure while they're shopping.")
    $ setWait(35.911,38.747)
    $ speak(JECKA, "Isn't it like workplace discrimination though?")
    $ setWait(38.747,39.706)
    $ speak(EMILY, "You're white.")
    $ setWait(39.706,42.709)
    $ speak(JECKA, "I'm not just white, I'm like dutch and swedish.")
    $ setWait(42.709,44.461)
    $ speak(NICOLE, "What exotic flavors of oppression.")
    show emo jecka sc1 angry:
        rightmidstage

    $ setWait(44.461,47.297)
    $ speak(JECKA, "I'm the one who's oppressed here, do you know how hard it is to be emo?")
    show emily sc3 upset:
        centerstage
        xzoom -1

    $ setWait(47.297,48.965)
    $ speak(EMILY, "You're not even straightening your hair.")
    $ setWait(48.965,54.179)
    $ speak(JECKA, "No- I get hit on like twice as much now, it's so annoying. I thought looking uglier would reverse that.")
    $ setWait(54.179,56.306)
    $ speak(NICOLE, "The uglier you are the more approachable you get.")
    show emily sc3 smile:
        centerstage
        xzoom -1
    $ setWait(56.306,58.308)
    $ speak(EMILY, "Yeah welcome to the low-maintenance club.")
    $ setWait(58.308,63.522)
    $ speak(NICOLE, "Before you wanted 6 feet and 6 figures. Now it looks like all you'd expect is Five Guys and Five Below.")
    show emo jecka sc1 sad:
        rightmidstage
    $ setWait(63.522,65.273)
    $ speak(JECKA, "Not Five Below...")

    show emo jecka sc1:
        rightmidstage

    $ setWait(65.273,67.567)
    $ speak(JECKA, "...Unless it's their candy, I really like the gum there.")
    show emily sc3:
        centerstage
        xzoom -1
    $ setWait(67.567,68.902)
    $ speak(EMILY, "See it's already starting.")
    show emo jecka sc1:
        rightmidstage

    $ setWait(68.902,70.362)
    $ speak(NICOLE, "You're so down-to-earth now.")
    $ setWait(70.362,72.406)
    $ speak(EMILY, "You look like a girl who gets off by being choked.")
    show emo jecka sc1 angry:
        rightmidstage

    $ setWait(72.406,74.324)
    $ speak(JECKA, "Bitch you look like you like getting choked!")
    show emily sc3 upset:
        centerstage
        xzoom -1

    $ setWait(74.324,75.575)
    $ speak(EMILY, "Takes one to know one.")
    $ setWait(75.575,79.413)
    $ speak(JECKA, "I needed the money, okay? If I didn't get a job my dad was gonna beat the shit out of me.")
    $ setWait(79.413,80.247)
    $ speak(NICOLE, "Human laxative.")
    $ setWait(80.247,83.542)
    $ speak(EMILY, "My Dad threatens that all the time, you actually take him seriously?")
    show kyle sc1 smile:
        off_right
        linear 1.3 rightstage

    $ setWait(83.542,86.294)
    $ speak(KYLE, "Oh hey guys, you havin' a birthday party here?")
    show emo jecka sc1 angry:
        xzoom -1
        rightmidstage
    $ setWait(86.294,87.713)
    $ speak(JECKA, "Yeah we're turning six.")

    show kyle sc1:
        rightstage

    show emily sc3 smile:
        centerstage
        xzoom -1
        linear 1 rightmidstage

    show emo jecka sc1:
        rightmidstage
        xzoom -1
        pause 0.5
        linear 0.8 rightcenterstage

    $ setWait(87.713,89.089)
    $ speak(EMILY, "Do you have a lot of money?")
    $ setWait(89.089,92.801)
    $ speak(KYLE, "Uhh.. Kinda. I bring a lot to play a while.")
    $ setWait(92.801,94.594)
    $ speak(EMILY, "Like 10,000 dollars?")
    $ setWait(94.594,96.596)
    $ speak(KYLE, "I don't even have that much in the bank.")
    show emily sc3 upset:
        rightmidstage
        xzoom -1
        pause 0.8
        xzoom 1
        linear 3 leftstage

    $ setWait(96.596,98.223)
    $ speak(EMILY, "Oh fuck you then, go away.")
    stop ambient fadeout 1.5
    jump scene_S0072

label scene_S0072:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka day with Pause(2.459):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.459 zoom 0.55 truecenter
    $ setVoiceTrack("audio/Scenes/0072.mp3")
    play ambient "audio/Ambience/House_Ambience_2.mp3"
    scene livingroom jecka
    show emo jecka sc2:
        off_left
        xzoom -1
        linear 1.5 leftmidstage

    $ setWait(2.459,6.087)
    $ speak(JECKA, "Ugh if I see one more Nightmare Before Christmas hoodie...")
    show dad buttonup:
        off_right
        linear 2 rightmidstage

    $ setWait(6.087,7.756)
    $ speak(DAD, "You're back from work already?")
    $ setWait(7.756,11.927)
    $ speak(JECKA, "Yeah some suicidal guy tried impaling himself with one of the clothing rack rods.")
    show dad buttonup upset:
        rightmidstage

    $ setWait(11.927,13.97)
    $ speak(DAD, "Oh no way, be serious.")
    $ setWait(13.97,16.806)
    $ speak(JECKA, "I don't care if you believe me or not, just leave me alone.")
    $ setWait(16.806,18.224)
    $ speak(DAD, "Is work going alright?")
    show emo jecka sc2 angry:
        leftmidstage

    $ setWait(18.224,19.768)
    $ speak(JECKA, "It's work, what do you think?")
    $ setWait(19.768,22.062)
    $ speak(DAD, "C'mon that's not the right attitude.")
    $ setWait(22.062,22.938)
    $ speak(JECKA, "What is?")
    show dad buttonup:
        rightmidstage

    $ setWait(22.938,27.359)
    $ speak(DAD, "You should feel good about contributing to society, making a fair wage.")
    $ setWait(27.359,32.697)
    $ speak(JECKA, "Dad, having a job fucking sucks! Every minute I'm there I just wanna get drunk and watch edited TNT movies!")
    $ setWait(32.697,34.783)
    $ speak(DAD, "Is that why the liquor cabinet's been empty this week?")
    $ setWait(34.783,36.826)
    $ speak(JECKA, "You're the one who wanted me to have a job, dad!")

    show dad buttonup upset:
        rightmidstage

    $ setWait(36.826,39.955)
    $ speak(DAD, "Ugh at least you're not out and about causing trouble.")
    $ setWait(39.955,43.291)
    $ speak(JECKA, "Yeah I'm just gonna be depressed and destroy my liver with UV Blue every night.")
    $ setWait(43.291,46.002)
    $ speak(DAD, "UV Blue? Mixed with what?")
    $ setWait(46.002,49.756)
    $ speak(JECKA, "I just drink it straight. It's like blue Gatorade but kills me slowly.")
    show dad buttonup caring:
        rightmidstage
    $ setWait(49.756,53.218)
    $ speak(DAD, "Dear, I don't think that's a healthy way to look at things.")
    $ setWait(53.218,54.886)
    $ speak(JECKA, "Well so do you want me to quit?")
    $ setWait(54.886,61.267)
    $ speak(DAD, "I want you to figure out a way to work at this job in a nondestructive way. It's part of being an adult.")
    $ setWait(61.267,62.936)
    $ speak(JECKA, "Who's the one with the liquor cabinet?")
    show dad buttonup upset:
        rightmidstage
    $ setWait(62.936,64.729)
    $ speak(DAD, "That's for entertaining guests.")
    $ setWait(64.729,66.606)
    $ speak(JECKA, "What guests? You don't let anyone over here.")
    $ setWait(66.606,71.903)
    $ speak(DAD, "My social life is none of your concern, now do your job with a smile on your face...")
    show dad buttonup yell:
        rightmidstage
        linear 0.3 leftcenterstage

    show emo jecka sc2 surprised:
        leftmidstage
        xzoom -1

    $ setWait(71.903,74.072)
    $ speak(DAD, "...before I beat the fuck out of you!!")
    show emo jecka sc2 sad:
        leftmidstage
        xzoom -1
        linear 0.2 leftstage

    $ setWait(74.072,75.115)
    $ speak(JECKA, "Okay! Okay!")
    show dad buttonup smile:
        leftcenterstage
        pause 2
        xzoom -1
        linear 3 off_right

    $ setWait(75.115,79.953)
    $ speak(DAD, "Now that's more like it. Responsibility.")
    show emo jecka sc2 sad:
        leftstage
        xzoom -1
        linear 5.5 rightstage
    $ setWait(79.953,82.872)
    $ speak(JECKA, "...Is 200 proof just rubbing alcohol?")
    stop ambient fadeout 1.5
    jump scene_S0073

label scene_S0073:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0073.mp3")
    play ambient "audio/Ambience/HotTopic_Ambience.mp3" fadein 1
    scene hot topic
    show emo jecka sc3:
        leftcenterstage

    show ari sc1:
        xzoom -1
        leftmidstage

    $ setWait(0.039,3.835)
    $ speak(ARI, "Wow so you really dyed your hair and everything.")
    $ setWait(3.835,5.503)
    $ speak(JECKA, "Are you gonna buy something?")

    $ setWait(5.503,7.63)
    $ speak(ARI, "Well I do need to feel different today.")
    $ setWait(7.63,9.34)
    $ speak(JECKA, "Basically what we're here for.")
    show ari sc1 smile:
        xzoom 1
        leftmidstage
        linear 1.2 leftstage

    $ setWait(9.34,11.217)
    $ speak(ARI, "Is that a Hello Kitty stud belt?")
    $ setWait(11.217,13.678)
    $ speak(JECKA, "That belt that 5 other people bought today? Yeah.")

    show ari sc1 smile:
        leftstage
        pause 1.9
        xzoom -1
        linear 4 off_right

    $ setWait(13.678,17.932)
    $ speak(ARI, "This gets me so well, I'm gonna go to the ATM.")
    show emo jecka sc3:
        xzoom -1
        leftcenterstage

    $ setWait(17.932,20.226)
    $ speak(JECKA, "At least I didn't get sexually harassed.")
    show crispin sc4 smile:
        off_right
        linear 3.5 rightcenterstage

    $ setWait(20.226,22.395)
    $ speak(CRISPIN, "Hey cool didn't know you worked here.")
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1
    $ setWait(22.395,23.896)
    $ speak(JECKA, "Oh come on.")
    $ setWait(23.896,25.69)
    $ speak(CRISPIN, "On what? Haha.")
    show emo jecka sc3:
        leftcenterstage
        xzoom -1
    $ setWait(25.69,27.275)
    $ speak(JECKA, "Five seconds, new record.")
    $ setWait(27.275,31.863)
    $ speak(CRISPIN, "But yeah I like your hair, kinda like Thursday Addams from the Addams Family.")
    $ setWait(31.863,33.448)
    $ speak(JECKA, "Which one is that?")
    show crispin sc4:
        rightcenterstage

    $ setWait(33.448,35.908)
    $ speak(CRISPIN, "Like the girl.. in it.")
    show emo jecka sc3 angry:
        xzoom 1
        leftcenterstage

    $ setWait(35.908,38.953)
    $ speak(JECKA, "Ugh, I just want this shift to be over so I can go to this party...")
    $ setWait(38.953,40.663)
    $ speak(CRISPIN, "Party? Who's party?")
    show emo jecka sc3:
        xzoom -1
        leftcenterstage

    $ setWait(40.663,41.581)
    $ speak(JECKA, "Kylar's.")
    $ setWait(41.581,42.707)
    $ speak(CRISPIN, "You're friends with Kylar?")
    $ setWait(42.707,45.084)
    $ speak(JECKA, "No but there's free alcohol so I'm going.")
    show crispin sc4 smile:
        rightcenterstage

    $ setWait(45.084,46.461)
    $ speak(CRISPIN, "Oh cool, can I--")
    show crispin sc4:
        rightcenterstage

    $ setWait(46.461,48.504)
    $ speak(JECKA, "No. Are you gonna buy anything?")
    $ setWait(48.504,53.05)
    $ speak(CRISPIN, "Uh.. huh well there's a pretty cool Suge Knight shirt over there.")
    $ setWait(53.05,57.096)
    $ speak(JECKA, "Did you seriously just pronounce it like \"Soog Knight\"?")
    $ setWait(57.096,58.347)
    $ speak(CRISPIN, "The rapper, right?")
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom 1
    $ setWait(58.347,60.016)
    $ speak(JECKA, "Oh my god is it 5 o'clock yet?")
    $ setWait(60.016,61.559)
    $ speak(CRISPIN, "But yeah I'll take the Suge Knight shirt.")
    show emo jecka sc3:
        leftcenterstage
        xzoom -1
    $ setWait(61.559,65.938)
    $ speak(JECKA, "Cool, well the manager can help ya with that. I gotta go home early cause I'm sick.")
    $ setWait(65.938,68.858)
    $ speak(CRISPIN, "Seriously? You seem fine, are you really sick?")

    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1
        linear 3 off_right
    $ setWait(68.858,70.193)
    $ speak(JECKA, "Of you? Yeah!")
    stop ambient fadeout 1.5
    jump scene_S0074

label scene_S0074:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house kylar night with Pause(2.672):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.672 zoom 0.55 truecenter
    $ setVoiceTrack("audio/Scenes/0074.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene home kylar

    show emily sc4 upset:
        rightcenterstage

    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1

    $ setWait(2.672,5.091)
    $ speak(EMILY, "Where do they keep the booze? This party sucks.")
    $ setWait(5.091,10.221)
    $ speak(JECKA, "I know! It's been 9 straight Godsmack songs and there's barely anyone here to talk shit about it with.")
    show emily sc4:
        rightcenterstage
    $ setWait(10.221,11.514)
    $ speak(EMILY, "Do you even like Kylar?")
    $ setWait(11.514,12.431)
    $ speak(JECKA, "Fuck no!")
    $ setWait(12.431,13.516)
    $ speak(EMILY, "Yeah me neither.")
    $ setWait(13.516,15.643)
    $ speak(JECKA, "I only came here to get medicinally drunk.")
    $ setWait(15.643,19.188)
    $ speak(EMILY, "Kinda same now. I only came to find a connect with DMT.")
    show emo jecka sc3:
        leftcenterstage
        xzoom -1
    $ setWait(19.188,20.856)
    $ speak(JECKA, "What's DMT?")
    $ setWait(20.856,25.236)
    $ speak(EMILY, "It's stands for dimeth-- fuck it's just that stuff your brain releases when you die.")
    $ setWait(25.236,27.571)
    $ speak(JECKA, "Oh cool.. I think.")
    $ setWait(27.571,28.698)
    $ speak(EMILY, "You wouldn't try it?")
    $ setWait(28.698,32.451)
    $ speak(JECKA, "I'm about to try one of these half-drank solo cups just to feel something.")
    show emily sc4 upset:
        rightcenterstage
        pause 1
        linear 3 off_left

    $ setWait(32.451,35.538)
    $ speak(EMILY, "Good luck with that, I'm gonna check in the basement.")
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1
    $ setWait(35.538,39.166)
    $ speak(JECKA, "The legal drinking age should be like 14 so I don't have to put up with this.")
    show kylar sc4 smile:
        off_right
        linear 2.5 rightcenterstage

    $ setWait(39.166,42.169)
    $ speak(KYLAR, "Sup my bitch, you enjoying my sweet party right now?")
    show emo jecka sc3:
        leftcenterstage
        xzoom -1
    $ setWait(42.169,43.546)
    $ speak(JECKA, "Yeah where's the drinks?")
    $ setWait(43.546,46.215)
    $ speak(KYLAR, "Okay yeah sorry about that, but I got you, don't worry.")
    $ setWait(46.215,47.383)
    $ speak(JECKA, "Yeah? I'm listening.")
    $ setWait(47.383,52.93)
    $ speak(KYLAR, "I got this really special whiskey, my dad says it's like made by the best brewery in the world.")
    $ setWait(52.93,54.14)
    $ speak(JECKA, "Special how?")
    $ setWait(54.14,60.271)
    $ speak(KYLAR, "Oh just the flavor and careful distilling process. It goes down extra smooth too cause it uses Nebraska corn and--")
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1
    $ setWait(60.271,62.064)
    $ speak(JECKA, "Who gives a shit, will it get me drunk!?")
    show kylar sc4:
        rightcenterstage

    $ setWait(62.064,63.899)
    $ speak(KYLAR, "Yeah yeah for sure, go ahead.")
    show emo jecka sc3:
        leftcenterstage
        xzoom -1
    $ setWait(63.899,66.944)
    $ speak(JECKA, "Alright thanks... You can go now.")
    $ setWait(66.944,68.571)
    $ speak(KYLAR, "Y-you don't wanna hang out?")
    $ setWait(68.571,69.989)
    $ speak(JECKA, "No that's okay.")
    show kylar sc4 smile:
        rightcenterstage
        xzoom -1
        linear 2.6 off_right

    $ setWait(69.989,72.241)
    $ speak(KYLAR, "Whatever I'll just come back when you're blacking out.")
    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1

    show black onlayer screens:
        alpha 0.0
        pause 1.7
        linear 1 alpha 1.0
    $ setWait(72.241,77.121)
    $ speak(JECKA, "Damn you really gotta drink responsibly here.")
    show black onlayer screens:
        alpha 1.0
        linear 2.3 alpha 0.0

    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1

    show crispin sc4:
        rightcenterstage

    $ setWait(77.121,80.458)
    $ speak(CRISPIN, "But yeah it's kinda weird how the government will just do that.")
    $ setWait(80.458,81.959)
    $ speak(JECKA, "Uh huh yeah.")
    $ setWait(81.959,85.379)
    $ speak(CRISPIN, "Oh did you know that government is \"mind control\" in latin?")
    $ setWait(85.379,89.133)
    $ speak(JECKA, "Oh shit, oh man. Crazy.")
    $ setWait(89.133,93.846)
    $ speak(CRISPIN, "By the way I kinda like you, you wanna make out in the bathroom?")
    $ setWait(93.846,96.265)
    $ speak(JECKA, "Uh... Like...")
    show emo jecka sc3 sad:
        xzoom 1
        leftcenterstage

    $ setWait(96.265,99.101)
    $ speak(JECKA, "God I am shitfaced taking this long to answer.")
    $ setWait(99.101,101.312)
    $ speak(CRISPIN, "We could have a lot of fun, no drama or anything.")
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1

    $ setWait(101.312,104.482)
    $ speak(JECKA, "No, fuck off and kill yourself!")
    show crispin sc4:
        rightcenterstage
        xzoom -1
        linear 3.5 off_right

    $ setWait(104.482,108.444)
    $ speak(CRISPIN, "Well um, I guess that's your choice.")
    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1

    $ setWait(108.444,111.197)
    $ speak(JECKA, "At least I feel way less shitty about having a job.")
    show emo jecka sc3 smile:
        leftcenterstage
        xzoom -1
    $ setWait(111.197,114.366)
    $ speak(JECKA, "Now I kinda like my job cause it makes drinking even better.")
    show kylar sc4 smile:
        xzoom 1
        off_right
        linear 2.7 rightcenterstage

    $ setWait(114.366,115.785)
    $ speak(KYLAR, "What's up you hot bitch?")
    $ setWait(115.785,116.911)
    $ speak(JECKA, "That's me.")
    $ setWait(116.911,119.58)
    $ speak(KYLAR, "Yo that's good whiskey, so you down to fuck?")
    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1

    $ setWait(119.58,122.75)
    $ speak(JECKA, "Oh no.. It's harder to get angry at that.")
    show kylar sc4 smile:
        rightcenterstage
        linear 3 off_left

    $ setWait(122.75,125.753)
    $ speak(KYLAR, "Drink the whole bottle if you want, I'll circle back around.")
    $ setWait(125.753,128.923)
    $ speak(JECKA, "Okay I gotta get outta here before I get molested.")
    show emily sc4 sad:
        off_right
        linear 2.4 rightcenterstage

    $ setWait(128.923,130.674)
    $ speak(EMILY, "Damn you look fucked up.")
    $ setWait(130.674,131.967)
    $ speak(JECKA, "Am I really that drunk?")
    show emily sc4:
        rightcenterstage

    $ setWait(131.967,134.053)
    $ speak(EMILY, "No someone gave me a hit of acid.")
    $ setWait(134.053,135.596)
    $ speak(JECKA, "Oh, I'll take it then.")
    $ setWait(135.596,136.639)
    $ speak(EMILY, "You trying to leave?")
    $ setWait(136.639,140.768)
    $ speak(JECKA, "Yeah if I don't get out of here soon I'm gonna end up handcuffed to a furnace tomorrow.")
    $ setWait(140.768,142.186)
    $ speak(EMILY, "Are you good to drive though?")
    $ setWait(142.186,143.354)
    $ speak(JECKA, "Yeah I got a car.")
    $ setWait(143.354,144.98)
    $ speak(EMILY, "No I meant drunk-wise.")
    $ setWait(144.98,147.149)
    $ speak(JECKA, "Oh shit I forgot you can't do that.")
    $ setWait(147.149,149.527)
    $ speak(EMILY, "I mean you can, you just can't get caught.")
    $ setWait(149.527,151.987)
    $ speak(JECKA, "Yeah the Mothers Against Drunk Driving.")
    $ setWait(151.987,153.405)
    $ speak(EMILY, "You'll make the MADDs mad.")
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1
    $ setWait(153.405,159.245)
    $ speak(JECKA, "How much you wanna bet every bitch who runs that shit is ugly as fuck and never had to worry at a party?")
    $ setWait(159.245,161.872)
    $ speak(EMILY, "Well they work non-profit so probably all of them?")
    $ setWait(161.872,162.832)
    $ speak(JECKA, "Exactly.")
    show emily sc4 sad:
        rightcenterstage

    $ setWait(162.832,164.208)
    $ speak(EMILY, "You got money for a cab?")
    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1
    $ setWait(164.208,165.835)
    $ speak(JECKA, "No, I work at Hot Topic.")
    $ setWait(165.835,167.419)
    $ speak(EMILY, "My condolences.")
    $ setWait(167.419,172.091)
    $ speak(JECKA, "And if I call my dad he's gonna yell at me.. ugh...")

    menu:
        "DRINK AND DRIVE":
            jump scene_S0075
        "CALL FOR RIDE":

            jump scene_S0076

label scene_S0075:
    $ setVoiceTrack("audio/Scenes/0075.mp3")
    scene home kylar
    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1


    show emily sc4:
        rightcenterstage

    $ setWait(0.046,1.714)
    $ speak(JECKA, "Fuck it, I'll suck it up.")
    $ setWait(1.714,2.84)
    $ speak(EMILY, "You're driving?")
    $ setWait(2.84,4.717)
    $ speak(JECKA, "Yeah you wanna go with me?")
    $ setWait(4.717,7.345)
    $ speak(EMILY, "It should be okay. Do you feel like throwing up?")
    $ setWait(7.345,9.722)
    $ speak(JECKA, "Kinda yeah.")
    $ setWait(9.722,10.848)
    $ speak(EMILY, "..It should be okay.")
    show emo jecka sc3 sad:
        leftcenterstage
        xzoom 1
        linear 5.5 off_farleft

    show emily sc4 smile:
        rightcenterstage
        linear 5.6 off_left

    $ setWait(10.848,13.142)
    $ speak(JECKA, "You wanna stop at McDonald's on the way back?")
    $ setWait(13.142,16)
    $ speak(EMILY, "Yeah McDonald's goes really good with drugs.")
    stop ambient fadeout 2.5
    jump scene_S0077

label scene_S0076:
    $ setVoiceTrack("audio/Scenes/0076.mp3")
    scene home kylar

    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1


    show emily sc4:
        rightcenterstage

    $ setWait(0.005,3.259)
    $ speak(JECKA, "Why does the safest option feel the most traumatizing?")
    $ setWait(3.259,4.802)
    $ speak(EMILY, "What's your dad gonna be mad about?")
    $ setWait(4.802,7.513)
    $ speak(JECKA, "He really hates it when I go out and get fucked up.")
    $ setWait(7.513,8.973)
    $ speak(EMILY, "Can you play sober?")
    $ setWait(8.973,10.391)
    $ speak(JECKA, "Is that on Playstation?")
    $ setWait(10.391,13.811)
    $ speak(EMILY, "What if you just made up a story that puts the blame on someone else?")
    $ setWait(13.811,16.48)
    $ speak(JECKA, "Like someone else forced me to drink?")
    $ setWait(16.48,17.481)
    $ speak(EMILY, "Yeah like that.")
    $ setWait(17.481,18.524)
    $ speak(JECKA, "But why?")
    $ setWait(18.524,22.82)
    $ speak(EMILY, "Oh maybe you entered an apple-juice drinking contest and they spiked it with whiskey.")
    show text_calldad onlayer screens:
        alpha 0.0
        pause 2.8
        alpha 1.0
    $ setWait(22.82,29.41)
    $ speak(JECKA, "Okay I'll call him with that.")

    $ setWait(29.41,30.995)
    $ speak(JECKA, "...Come on what the hell?")
    $ setWait(30.995,33.998)
    $ speak(DAD, "Sorry I can't get to the phone right now but if you leave your name and number-")
    hide text_calldad onlayer screens
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1
    $ setWait(33.998,36.208)
    $ speak(JECKA, "My dad let me go to fucking voicemail!")
    show emily sc4 upset:
        rightcenterstage

    $ setWait(36.208,37.251)
    $ speak(EMILY, "What an asshole.")
    show emo jecka sc3 sad:
        leftcenterstage
        xzoom -1
    $ setWait(37.251,38.627)
    $ speak(JECKA, "I know, he hates me.")
    $ setWait(38.627,41.964)
    $ speak(EMILY, "If it makes you feel any better I hope your dad fucking kills himself.")
    $ setWait(41.964,43.257)
    $ speak(JECKA, "Me too.")
    $ setWait(43.257,44.675)
    $ speak(EMILY, "So what are you gonna do?")
    show emo jecka sc3 angry:
        leftcenterstage
        xzoom -1
        pause 1
        xzoom 1
        linear 2 off_left

    $ setWait(44.675,47.544)
    $ speak(JECKA, "Screw this, I'm driving home!")
    stop ambient fadeout 2.5
    jump scene_S0077

label scene_S0077:
    show black onlayer screens with Pause(3):
        alpha 0.0
        linear 2.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka night with Pause(2.631):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.631 zoom 1.05 truecenter
    $ setVoiceTrack("audio/Scenes/0077.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene livingroom jecka
    show emo jecka sc3 sad:
        xzoom -1
        off_left
        linear 2.4 leftcenterstage

    $ setWait(2.631,5.091)
    $ speak(JECKA, "Is McDonald's an Irish restaurant?")
    show dad undershirt angry:
        off_right
        linear 1 rightmidstage

    $ setWait(5.091,6.676)
    $ speak(DAD, "What are you doing home so late??")
    show emo jecka sc3 surprised:
        xzoom 1
        leftcenterstage
        linear 0.4 leftstage
    $ setWait(6.676,7.26)
    $ speak(JECKA, "Oh god!")
    show dad undershirt angry:
        rightmidstage
        linear 3 centerstage
    $ setWait(7.26,10.722)
    $ speak(DAD, "Answer me! What are you doing home so late!?")
    show emo jecka sc3 sad:
        leftstage
        xzoom -1

    $ setWait(10.722,11.473)
    $ speak(JECKA, "Panicking!")
    $ setWait(11.473,16.686)
    $ speak(DAD, "What did I say about going out and goofing off? And why do you reek of whiskey??")
    $ setWait(16.686,19.022)
    $ speak(JECKA, "Um, a lumberjack threw up on me.")
    $ setWait(19.022,20.982)
    $ speak(DAD, "You can't even speak clearly!")
    $ setWait(20.982,23.276)
    $ speak(JECKA, "I don't know clearly I just speak English.")
    $ setWait(23.276,26.529)
    $ speak(DAD, "Is your car out front? Did you drive home!?")
    $ setWait(26.529,27.53)
    $ speak(JECKA, "Don't yell at me!")
    show dad undershirt yell:
        centerstage

    $ setWait(27.53,31.076)
    $ speak(DAD, "Drunk driving! How could you be so fucking stupid!?")
    $ setWait(31.076,32.452)
    $ speak(JECKA, "Y-You don't get it!")
    $ setWait(32.452,34.204)
    $ speak(DAD, "I get the law!")
    show emo jecka sc3 angry:
        leftstage
        xzoom -1
        linear 1 leftmidstage
    $ setWait(34.204,37.04)
    $ speak(JECKA, "Oh so you want me to stay there without a ride and get raped??")
    show dad undershirt angry:
        centerstage
    $ setWait(37.04,38.5)
    $ speak(DAD, "Maybe that'd teach you a lesson!")
    show emo jecka sc3 sad:
        leftmidstage
        xzoom -1
    $ setWait(38.5,39.501)
    $ speak(JECKA, "What the fuck!?")
    $ setWait(39.501,41.586)
    $ speak(DAD, "Who was at this party anyway? Where was it?")

    $ setWait(41.586,42.879)
    $ speak(JECKA, "I don't need to tell you.")
    show dad undershirt yell:
        centerstage
        pause 2
        linear 0.09 xalign .49
        linear 0.09 xalign .51
        linear 0.09 xalign .48
        linear 0.09 xalign .52
        linear 0.08 xalign .48
        linear 0.08 xalign .52
        linear 0.08 xalign .48
        linear 0.08 xalign .52
        linear 0.07 xalign .48
        linear 0.07 xalign .52
        linear 0.06 xalign .48
        linear 0.06 xalign .52
        linear 0.06 xalign .48
        linear 0.06 xalign .52
        linear 0.06 xalign .48
        linear 0.06 xalign .52
        linear 0.07 xalign .48
        linear 0.07 centerstage
    $ setWait(42.879,46.216)
    $ speak(DAD, "Do I need to smack you through the fucking drywall!?")
    $ setWait(46.216,48.343)
    $ speak(JECKA, "It was just the neighborhood over!")
    show dad undershirt angry:
        centerstage
    $ setWait(48.343,52.597)
    $ speak(DAD, "And everyone there was from around here, right?")
    $ setWait(52.597,54.182)
    $ speak(JECKA, "What do you mean?")

    show dad undershirt upset:
        centerstage

    $ setWait(54.182,58.728)
    $ speak(DAD, "Everyone's parents make the same money?")
    $ setWait(58.728,61.731)
    $ speak(JECKA, "Are you asking me if there were minorities at the party?")
    $ setWait(61.731,63.233)
    $ speak(DAD, "It's not about that it's--")
    show emo jecka sc3 angry:
        leftmidstage
        xzoom -1

    $ setWait(63.233,66.736)
    $ speak(JECKA, "And what if there were dad?? You don't answer your fucking phone anyway!")
    show dad undershirt angry:
        centerstage

    $ setWait(66.736,68.071)
    $ speak(DAD, "You're out of control!")
    $ setWait(68.071,72.867)
    $ speak(JECKA, "I'm perfectly in control! If you're gonna make me go to work then I'm gonna go have fun after!")
    show dad undershirt angry:
        centerstage
        xzoom -1
        linear 3.3 off_right
    $ setWait(72.867,75.62)
    $ speak(DAD, "Such an idiot, I'm going to sleep.")
    show emo jecka sc3 angry:
        leftmidstage
        xzoom -1
        linear 1 centerstage
    $ setWait(75.62,80.375)
    $ speak(JECKA, "Yeah so let me do whatever I want or I'm gonna date a 30 year old Jiffy Lube cashier!")
    stop ambient fadeout 1.5
    jump scene_S0078

label scene_S0078:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0078.mp3")
    play ambient "audio/Ambience/HotTopic_Ambience.mp3" fadein 1
    scene hot topic
    show emo jecka sc2:
        rightcenterstage

    show crispin sc1:
        leftcenterstage
        xzoom -1

    $ setWait(0.042,6.298)
    $ speak(CRISPIN, "And so the scientologists got real mad when all the guys in the mustache masks showed up.")
    $ setWait(6.298,8.217)
    $ speak(JECKA, "...Like the Groucho glasses?")
    $ setWait(8.217,12.638)
    $ speak(CRISPIN, "No, no, it's from that movie uh.. V for Vendetta.")
    $ setWait(12.638,14.723)
    $ speak(JECKA, "Oh yeah I know that one...")
    $ setWait(14.723,16.1)
    $ speak(JECKA, "...I don't give a shit, get out.")
    $ setWait(16.1,17.684)
    $ speak(CRISPIN, "Wait! I wanted to buy something though.")
    show emo jecka sc2 angry:
        rightcenterstage

    $ setWait(17.684,21.188)
    $ speak(JECKA, "No you don't. You come in here twice a week and you never buy anything.")
    show crispin sc1:
        leftcenterstage
        xzoom -1
        pause 1.3
        xzoom 1
        linear 3 off_left

    $ setWait(21.188,24.149)
    $ speak(CRISPIN, "I'm just looking around, lemme see these belts.")
    show emo jecka sc2:
        rightcenterstage

    $ setWait(24.149,27.319)
    $ speak(JECKA, "How does one guy hold so much useless information?")
    show nicole sc7:
        off_right
        xzoom -1
        linear 2 rightmidstage
    $ setWait(27.319,28.57)
    $ speak(NICOLE, "Hey are you off yet?")
    show emo jecka sc2:
        rightcenterstage
        xzoom -1
    $ setWait(28.57,31.74)
    $ speak(JECKA, "Uh like 45 minutes. What you got for us?")
    $ setWait(31.74,32.991)
    $ speak(NICOLE, "Kelly's having a party.")
    $ setWait(32.991,33.909)
    $ speak(JECKA, "At her parent's house?")
    show nicole sc7 angry:
        rightmidstage
        xzoom -1

    $ setWait(33.909,35.119)
    $ speak(NICOLE, "No her own fuckin' house.")

    show nicole sc7:
        rightmidstage
        xzoom -1

    $ setWait(35.119,36.954)
    $ speak(JECKA, "Whatever- who else is gonna be there?")
    $ setWait(36.954,38.914)
    $ speak(NICOLE, "A bunch of college guys Kelly wants to impress.")
    show emo jecka sc2 smile:
        rightcenterstage
        xzoom -1

    $ setWait(38.914,41.5)
    $ speak(JECKA, "Oh shit there's gonna be a lot to drink then.")
    $ setWait(41.5,45.254)
    $ speak(NICOLE, "Yeah but a lot of people drinking it too so we gotta go pretty close to now.")
    $ setWait(45.254,46.922)
    $ speak(JECKA, "You're like my binge drinking agent.")
    show nicole sc7 smile:
        rightmidstage
        xzoom -1

    show crispin sc1:
        xzoom -1
        off_left
        linear 3.5 leftcenterstage

    $ setWait(46.922,49.091)
    $ speak(NICOLE, "I just like drinking, I don't know what you're talkin' about.")
    $ setWait(49.091,50.217)
    $ speak(CRISPIN, "Drinking again?")
    show nicole sc7:
        rightmidstage
        xzoom -1

    show emo jecka sc2:
        rightcenterstage
        xzoom 1

    $ setWait(50.217,50.968)
    $ speak(NICOLE, "Obvi.")
    $ setWait(50.968,52.886)
    $ speak(JECKA, "Where's your belt? You're ringing up, right?")
    $ setWait(52.886,55.973)
    $ speak(CRISPIN, "Well I just overheard you guys are going to another party.")
    $ setWait(55.973,56.974)
    $ speak(NICOLE, "No you can't come.")
    $ setWait(56.974,63.397)
    $ speak(CRISPIN, "Not that, it's just gotten around that you guys are getting really messed up at everyone's party lately.")
    $ setWait(63.397,64.69)
    $ speak(JECKA, "Is that like a compliment?")
    $ setWait(64.69,68.11)
    $ speak(CRISPIN, "Actually, more like a concern. Are you sure that's safe?")
    show nicole sc7 angry:
        rightmidstage
        xzoom -1

    show emo jecka sc2 angry:
        rightcenterstage
        xzoom 1
    $ setWait(68.11,69.528)
    $ speak(NICOLE, "Oh my fucking god!")
    $ setWait(69.528,71.655)
    $ speak(JECKA, "Is this an intervention from the fun police?")
    $ setWait(71.655,75.909)
    $ speak(NICOLE, "You sexually harass every girl we know daily and think you can talk to us about safety?")
    $ setWait(75.909,78.328)
    $ speak(CRISPIN, "Whoa, I don't do that, I just try to be cool with people.")
    $ setWait(78.328,80.08)
    $ speak(JECKA, "Buy something or get the fuck out!")
    $ setWait(80.08,81.373)
    $ speak(CRISPIN, "What's wrong with what I said?")
    $ setWait(81.373,82.541)
    $ speak(JECKA, "Basically everything?")
    $ setWait(82.541,83.709)
    $ speak(NICOLE, "You're not our fuckin' dad.")
    $ setWait(83.709,86.086)
    $ speak(CRISPIN, "I never said I was! Just like as a friend.")
    $ setWait(86.086,88.714)
    $ speak(NICOLE, "We don't fucking like you. Kill your self.")
    $ setWait(88.714,91.091)
    $ speak(JECKA, "Your suicide would be a breakthrough for women's rights.")
    $ setWait(91.091,93.343)
    $ speak(CRISPIN, "Where is this even coming from? What the hell.")
    $ setWait(93.343,95.637)
    $ speak(NICOLE, "We'll do whatever the fuck we want, okay?")

    show crispin sc1:
        leftcenterstage
        xzoom -1
        linear 3 off_right

    $ setWait(95.637,97.764)
    $ speak(CRISPIN, "Alright whatever.")
    show emo jecka sc2:
        rightcenterstage
        xzoom -1
    $ setWait(97.764,100.058)
    $ speak(JECKA, "Since when's having fun dangerous anyway?")
    show nicole sc7:
        rightmidstage
        xzoom -1

    $ setWait(100.058,102.478)
    $ speak(NICOLE, "Dude he just thinks good samaritan pussy's real.")
    $ setWait(102.478,105.397)
    $ speak(JECKA, "God that pissed me off so much, I'm just gonna leave early.")
    show nicole sc7 smile:
        rightmidstage
        xzoom -1

    $ setWait(105.397,106.565)
    $ speak(NICOLE, "For real? Cool.")
    show emo jecka sc2:
        rightcenterstage
        xzoom -1
        linear 1.5 off_right

    show nicole sc7 smile:
        xzoom -1
        rightmidstage
        pause 0.9
        xzoom 1
        linear 1.9 off_right

    $ setWait(106.565,107.566)
    $ speak(JECKA, "Let's go.")
    stop ambient fadeout 1.5
    jump scene_S0079

label scene_S0079:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show home jecka ext night with Pause(2.584):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.584 zoom 0.55 truecenter
    $ setVoiceTrack("audio/Scenes/0079.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene living room generic
    show emo jecka sc2 sad:
        rightcenterstage
        xzoom -1

    show nicole sc7:
        leftcenterstage

    show hunter sc2:
        rightmidstage

    $ setWait(2.584,7.13)
    $ speak(HUNTER, "But yeah if you hold your tongue up the breathalyzer can't get the alcohol.")
    $ setWait(7.13,8.423)
    $ speak(NICOLE, "Have you tried that?")
    $ setWait(8.423,11.551)
    $ speak(HUNTER, "No I just watched a video on YouTube about it.")
    $ setWait(11.551,13.761)
    $ speak(NICOLE, "Oh okay, it must work then.")
    $ setWait(13.761,15.305)
    $ speak(HUNTER, "I know.")
    $ setWait(15.305,18.641)
    $ speak(JECKA, "Hey Hunter? Could you uh...")
    $ setWait(18.641,19.851)
    $ speak(JECKA, "Go fuck off?")
    $ setWait(19.851,21.311)
    $ speak(HUNTER, "What'd I do?")
    $ setWait(21.311,22.645)
    $ speak(JECKA, "Just you.")
    show hunter sc2 angry:
        rightmidstage
        xzoom -1
        linear 4 off_right

    $ setWait(22.645,27.066)
    $ speak(HUNTER, "Whatever, I'm gonna go punch holes in some drywall.")
    show emo jecka sc2 sad:
        xzoom 1
        rightcenterstage

    $ setWait(27.066,33.031)
    $ speak(JECKA, "Okay I think I'm passing peak drunkness so by like 12:30 I should be good to drive.")
    $ setWait(33.031,36.201)
    $ speak(NICOLE, "Yeah see, this idea's way better than a designated driver.")
    $ setWait(36.201,39.412)
    $ speak(JECKA, "I can have fun and independence at the same time.")
    $ setWait(39.412,42.332)
    $ speak(NICOLE, "Yeah you're like George Washington but less racist.")
    show emo jecka sc2 angry:
        rightcenterstage

    $ setWait(42.332,44.25)
    $ speak(JECKA, "Bitch I'm not racist at all!")
    show kelly sc2 sad:
        off_left
        xzoom -1
        linear 2 leftmidstage

    show emo jecka sc2 sad:
        rightcenterstage

    $ setWait(44.25,47.253)
    $ speak(KELLY, "Hey have you guys seen somebody punching holes in the wall?")
    show nicole sc7:
        leftcenterstage
        xzoom -1
    $ setWait(47.253,48.713)
    $ speak(NICOLE, "Sorry, not really.")
    $ setWait(48.713,49.756)
    $ speak(JECKA, "Yeah bye.")
    $ setWait(49.756,50.715)
    $ speak(KELLY, "No I'm serious!")
    show emo jecka sc2 angry:
        rightcenterstage
    $ setWait(50.715,53.009)
    $ speak(JECKA, "Bitch get the fuck out of my face!!")
    show kelly sc2 angry:
        leftmidstage
        xzoom -1
        linear 2.5 off_right

    $ setWait(53.009,55.303)
    $ speak(KELLY, "That's it, I'm literally done!")
    show nicole sc7:
        xzoom 1
        leftcenterstage

    $ setWait(55.303,57.847)
    $ speak(NICOLE, "Look how rich her parents are, she can afford a few holes.")
    show emo jecka sc2 smile:
        rightcenterstage
        xzoom 1

    $ setWait(57.847,61.392)
    $ speak(JECKA, "I could afford a few holes too, I'mma buy me some hoes!")
    show nicole sc7 sad:
        leftcenterstage

    $ setWait(61.392,65.021)
    $ speak(NICOLE, "Dude you're albino girl drunk, we better wait longer than 12:30.")
    show emo jecka sc2 sad:
        rightcenterstage

    $ setWait(65.021,67.065)
    $ speak(JECKA, "I'm not embarassing you am I?")
    show nicole sc7:
        leftcenterstage
    $ setWait(67.065,68.107)
    $ speak(NICOLE, "No you're cool.")
    show emo jecka sc2 smile:
        rightcenterstage
    $ setWait(68.107,70.527)
    $ speak(JECKA, "Good cause I don't fucking care!")
    show nicole sc7 surprised:
        leftcenterstage
        xzoom -1

    show emo jecka sc2 surprised:
        rightcenterstage

    show hunter sc2 sad:
        off_right
        xzoom 1
        linear 1.7 off_left

    $ setWait(70.527,71.778)
    $ speak(HUNTER, "Who called the cops!?")
    $ setWait(71.778,74.447)
    $ speak(COP, "This is the FCPD, we're coming in!")
    $ setWait(74.447,75.114)
    $ speak(NICOLE, "Oh fuck!")
    $ setWait(75.114,75.949)
    $ speak(JECKA, "No way!")
    show kylar sc3 angry:
        off_right
        linear 1.7 off_left

    $ setWait(75.949,77.909)
    $ speak(KYLAR, "Who snitched!? So fucked up!")
    show nicole sc7 sad:
        leftcenterstage
        xzoom 1

    show emo jecka sc2 sad:
        rightcenterstage
        xzoom 1
    $ setWait(77.909,78.91)
    $ speak(JECKA, "Do you think we should--")
    show coach 1 worried:
        off_farright
        linear 2.4 off_farleft

    $ setWait(78.91,80.703)
    $ speak(COACH, "I gotta get out of here!!")
    show nicole sc7:
        leftcenterstage
        xzoom -1

    $ setWait(80.703,81.829)
    $ speak(NICOLE, "Well that alone.")
    $ setWait(81.829,83.248)
    $ speak(JECKA, "Do you think I'm sober enough?")
    show nicole sc7 surprised:
        leftcenterstage
        xzoom 1
    $ setWait(83.248,84.457)
    $ speak(NICOLE, "To what? Drive?")
    $ setWait(84.457,86.167)
    $ speak(JECKA, "Yeah how else are we leaving?")
    show nicole sc7 sad:
        leftcenterstage
    $ setWait(86.167,87.919)
    $ speak(NICOLE, "Shit uh...")
    show nicole sc7:
        leftcenterstage
    $ setWait(87.919,89.003)
    $ speak(NICOLE, "Do you give good head?")
    $ setWait(89.003,90.421)
    $ speak(JECKA, "When there's money involved.")
    show nicole sc7:
        leftcenterstage
        pause 2
        xzoom -1
        linear 1 off_left

    show emo jecka sc2 sad:
        rightcenterstage
        xzoom 1
        pause 2.4
        linear 1.1 off_left

    $ setWait(90.421,93.99)
    $ speak(NICOLE, "Well I don't think the cop's gonna bribe you back so just drive us out of here!")
    stop ambient fadeout 2.2
    jump scene_S0080

label scene_S0080:
    show black onlayer screens with Pause(3):
        alpha 0.0
        linear 2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0080.mp3")
    play ambient "audio/Ambience/Car_Ambience.mp3" fadein 1
    $ csbox = True
    scene cut0080a
    $ setWait(0.077,1.119)
    $ speak(NICOLE, "Was that a stop sign?")
    scene cut0080b
    $ setWait(1.119,2.371)
    $ speak(JECKA, "Don't backseat drive me!")
    scene cut0080e
    $ setWait(2.371,3.58)
    $ speak(NICOLE, "You said you wanted help!")
    $ setWait(3.58,6.208)
    $ speak(JECKA, "Yeah like help me by telling me how good I'm doing!")
    scene cut0080a
    $ setWait(6.208,9.169)
    $ speak(NICOLE, "I mean for half a handle of rum you're actually doing awesome.")
    $ setWait(9.169,10.671)
    $ speak(JECKA, "Should we stop by McDonald's?")
    $ setWait(10.671,11.797)
    $ speak(NICOLE, "Why do you want McDonald's?")
    $ setWait(11.797,14.341)
    $ speak(JECKA, "There's the truck with the big Egg McMuffin on the side.")
    scene cut0080c
    $ setWait(14.341,14.925)
    $ speak(NICOLE, "What the fuck!!")
    $ setWait(14.925,16.009)
    $ speak(JECKA, "Oh god!")
    scene cut0080d
    $ setWait(16.009,17.678)
    $ speak(NICOLE, "Holy shit...")
    scene cut0080a
    $ setWait(17.678,21.39)
    $ speak(NICOLE, "That wasn't even your drunkness, it was just driving on the wrong side of the road.")
    $ setWait(21.39,25.102)
    $ speak(JECKA, "I know what an asshole, fuck McDonald's I don't wanna go there anymore.")
    $ setWait(25.102,26.979)
    $ speak(NICOLE, "Yeah let's just go home.")
    $ setWait(26.979,28.313)
    $ speak(JECKA, "But I want Popeyes now.")
    $ setWait(28.313,29.606)
    $ speak(NICOLE, "Popeyes isn't open!")
    $ setWait(29.606,32.651)
    $ speak(JECKA, "It's always crowded there, they really went out of business?")
    $ setWait(32.651,34.278)
    $ speak(NICOLE, "No I meant for the night.")
    $ setWait(34.278,36.863)
    $ speak(JECKA, "I wish there were as many Popeyes as KFCs.")
    scene cut0080c
    $ setWait(36.863,37.823)
    $ speak(NICOLE, "Shit watch out!!")
    stop ambient fadeout 4.5
    scene black
    show cut0080c:
        alpha 1.0
        pause 0.95
        alpha 0.0

    show white onlayer screens:
        alpha 0.0
        pause 0.9
        alpha 1.0
        pause 0.08
        alpha 0.0
        pause 0.08
        alpha 1.0
        pause 0.08
        alpha 1.0
        pause 0.08
        alpha 0.0

    $ setWait(37.823,47.624)
    $ speak(JECKA, "Ahhh!!!")
    jump end_S0081

label end_S0081:

    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    scene black

    if "end_0081" not in persistent.endings:
        $ persistent.endings.append("end_0081")
        $ persistent.new_ending = True

    $ quick_menu = False



    $ renpy.movie_cutscene("cs0081.webm")

    return
label scene_S0082:
    $ setVoiceTrack("audio/Scenes/0082.mp3")
    scene school int 1

    show nicole sc4:
        leftcenterstage

    show jecka sc5 sad:
        rightcenterstage
    $ setWait(0.042,2.461)
    $ speak(JECKA, "Sorry, it's just--")
    show nicole sc4 angry:
        leftcenterstage

    $ setWait(2.461,3.671)
    $ speak(NICOLE, "Are you fucking kidding me?")
    $ setWait(3.671,5.464)
    $ speak(JECKA, "You said it wasn't an ultimatum!")
    $ setWait(5.464,6.882)
    $ speak(NICOLE, "I'm still allowed to be mad!")
    $ setWait(6.882,10.428)
    $ speak(JECKA, "I can't screw up my life over a Marilyn Manson concert.")
    $ setWait(10.428,12.305)
    $ speak(NICOLE, "If it was Ryan Sheckler you'd go.")
    show jecka sc5 angry:
        rightcenterstage

    $ setWait(12.305,13.764)
    $ speak(JECKA, "That's different and you know it.")
    show nicole sc4 sad:
        leftcenterstage
    $ setWait(13.764,15.433)
    $ speak(NICOLE, "But what am I supposed to do with all this now?")
    $ setWait(15.433,16.392)
    $ speak(JECKA, "All what?")
    $ setWait(16.392,17.643)
    $ speak(NICOLE, "Tickets and ecstasy.")
    show jecka sc5:
        rightcenterstage
    $ setWait(17.643,19.645)
    $ speak(JECKA, "You can't find someone else to go with you?")
    $ setWait(19.645,22.189)
    $ speak(NICOLE, "Not really, unless it's some guy.")
    $ setWait(22.189,23.733)
    $ speak(JECKA, "Well make some regular friends.")
    $ setWait(23.733,26.986)
    $ speak(NICOLE, "I don't know how to make friends! I don't even know how I talk to you.")
    show jecka sc5 angry:
        rightcenterstage
    $ setWait(26.986,28.946)
    $ speak(JECKA, "Ugh, can't you just scalp the tickets then?")
    $ setWait(28.946,32.283)
    $ speak(NICOLE, "I'm not some 50 year old Italian guy, I don't know how to do that either!")
    show jecka sc5 sad:
        rightcenterstage
    $ setWait(32.283,33.576)
    $ speak(JECKA, "Look...")
    $ setWait(33.576,35.578)
    $ speak(NICOLE, "Look what?")
    show jecka sc5:
        rightcenterstage
    $ setWait(35.578,40.416)
    $ speak(JECKA, "I don't know if you should need me this much...")

    show jecka sc5:
        rightcenterstage
        xzoom -1
        linear 3 off_right

    $ setWait(40.416,42.877)
    $ speak(JECKA, "...I'm gonna go date my teacher now.")

    show nicole sc4 angry:
        leftcenterstage
        xzoom -1
        linear 3.4 off_left

    $ setWait(42.877,45.463)
    $ speak(NICOLE, "Yeah you would.")
    stop ambient fadeout 2.2
    jump scene_S0083

label scene_S0083:
    show black onlayer screens with Pause(3):
        alpha 0.0
        linear 2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show olive garden ext with Pause(2.54):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.54 zoom 0.55 truecenter
    $ setVoiceTrack("audio/Scenes/0083.mp3")
    play ambient "audio/Ambience/Restaurant_Ambience.mp3"
    scene olive garden int
    show jecka sc5 angry:
        leftcenterstage
        xzoom -1

    show katz 2 smile:
        rightcenterstage

    $ setWait(2.54,4.5)
    $ speak(JECKA, "You took me to fucking Olive Garden??")
    $ setWait(4.5,5.835)
    $ speak(KATZ, "Told you it'd be fancy.")
    $ setWait(5.835,7.712)
    $ speak(JECKA, "How is Olive Garden fancy?")
    $ setWait(7.712,11.466)
    $ speak(KATZ, "Well the Mediterranean dishes and lovely atmosphere.")
    show jecka sc5:
        leftcenterstage


    $ setWait(11.466,13.76)
    $ speak(JECKA, "Do you think I'm 9 or just want me to be 9.")
    $ setWait(13.76,16.512)
    $ speak(KATZ, "Best of all; all-you-can-eat salad.")
    $ setWait(16.512,17.805)
    $ speak(JECKA, "Are you calling me fat?")
    show katz 2 sad:
        rightcenterstage

    $ setWait(17.805,22.268)
    $ speak(KATZ, "No no, I just think it's very generous of them to do that.")
    $ setWait(22.268,24.02)
    $ speak(JECKA, "So about my grade.")
    show katz 2:
        rightcenterstage

    $ setWait(24.02,34.197)
    $ speak(KATZ, "Right well seeing that we have a brewing arrangement here, I think it's a clever idea to call this extra credit.")
    $ setWait(34.197,36.574)
    $ speak(JECKA, "How much extra credit if I just sit here?")
    $ setWait(36.574,39.869)
    $ speak(KATZ, "I don't know yet, maybe a few assignments worth.")
    show jecka sc5 smile:
        leftcenterstage
        xzoom -1
    $ setWait(39.869,43.665)
    $ speak(JECKA, "Oh that's pretty cool. How do we get my tests regraded?")
    $ setWait(43.665,47.46)
    $ speak(KATZ, "I'd just have to go into the program and change the numbers.")
    show jecka sc5:
        leftcenterstage
        xzoom -1
    $ setWait(47.46,51.464)
    $ speak(JECKA, "No I meant like, what do you need from me to do that?")
    show katz 2 weird:
        rightcenterstage

    $ setWait(51.464,54.05)
    $ speak(KATZ, "Let's not make it so creepy like that.")
    $ setWait(54.05,58.68)
    $ speak(JECKA, "Oh yeah wouldn't wanna ruin this transactional date with a high schooler at Olive Garden.")
    show katz 2 smile:
        rightcenterstage

    $ setWait(58.68,59.764)
    $ speak(KATZ, "See anything you like?")
    show jecka sc5 sad:
        leftcenterstage
        xzoom -1
    $ setWait(59.764,61.808)
    $ speak(JECKA, "You're really ugly, don't make me do this.")
    show katz 2:
        rightcenterstage

    $ setWait(61.808,63.518)
    $ speak(KATZ, "I meant on the menu.")
    show jecka sc5:
        leftcenterstage
        xzoom -1

    $ setWait(63.518,68.481)
    $ speak(JECKA, "Whatever makes me look really unattractive while eating it. Maybe Spaghetti.")
    show katz 2 smile:
        rightcenterstage

    $ setWait(68.481,69.44)
    $ speak(KATZ, "Delicious.")
    $ setWait(69.44,72.11)
    $ speak(JECKA, "Oh wait you'd like that cause I'd look even more like a minor.")
    show katz 2 angry:
        rightcenterstage

    $ setWait(72.11,74.195)
    $ speak(KATZ, "Can we stop with the petty insults?")
    $ setWait(74.195,77.031)
    $ speak(JECKA, "That wasn't an insult, it's just what your people like, right?")
    $ setWait(77.031,77.865)
    $ speak(KATZ, "What people?")
    $ setWait(77.865,79.492)
    $ speak(JECKA, "Pedo-- I mean NAMBLA.")
    $ setWait(79.492,80.952)
    $ speak(KATZ, "Oh don't be ridiculous.")
    show jecka sc5 smile:
        leftcenterstage
        xzoom -1

    $ setWait(80.952,83.663)
    $ speak(JECKA, "You're right. I'm a girl so it's NAMGLA.")
    show katz 2:
        rightcenterstage

    $ setWait(83.663,86.708)
    $ speak(KATZ, "Okay I think the waiter's coming, let's not talk about this.")
    show jecka sc5:
        leftcenterstage
        xzoom -1
    $ setWait(86.708,91.671)
    $ speak(JECKA, "Should I switch to politics or NeoPets? Which one's less suspicious for me to know about?")
    stop ambient fadeout 1.5
    jump scene_S0084

label scene_S0084:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka night with Pause(2.25):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.25 zoom 1.05 truecenter

    $ setVoiceTrack("audio/Scenes/0084.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene livingroom jecka
    show dad shorts:
        leftcenterstage
        xzoom -1

    $ setWait(2.25,3.126)
    $ speak(DAD, "Jessica?")
    show jecka sc12:
        off_right
        linear 0.6 rightstage

    $ setWait(3.126,4.586)
    $ speak(JECKA, "Okay don't hit me.")
    $ setWait(4.586,6.379)
    $ speak(DAD, "Wh-- Why would I hit you?")
    show jecka sc12 sad:
        rightstage

    $ setWait(6.379,9.799)
    $ speak(JECKA, "That's like asking how Vietnam happened, there's like so many answers.")
    show dad shorts smile:
        leftcenterstage
        xzoom -1

    $ setWait(9.799,15.43)
    $ speak(DAD, "I just wanted to say your teacher called and said you were making some great progress in AP History.")
    $ setWait(15.43,18.391)
    $ speak(JECKA, "Oh cool, really glad he called you.")
    $ setWait(18.391,20.769)
    $ speak(DAD, "I told you that hitting those books would pay off.")
    show jecka sc12:
        rightstage

    $ setWait(20.769,21.811)
    $ speak(JECKA, "Am I books to you?")
    $ setWait(21.811,24.773)
    $ speak(DAD, "Let's just hope you can keep this up until graduation.")
    $ setWait(24.773,28.86)
    $ speak(JECKA, "At least there's anti-bullying rules now so no one makes fun of me for being good at school.")
    show dad shorts upset:
        leftcenterstage
        xzoom -1

    $ setWait(28.86,34.491)
    $ speak(DAD, "Anti-bullying rules? How do they expect you kids to build character?")
    $ setWait(34.491,35.658)
    $ speak(JECKA, "...What?")
    show dad shorts:
        leftcenterstage
        xzoom -1

    $ setWait(35.658,39.37)
    $ speak(DAD, "Bullying is a necessary evil to prepare you all for the real world.")
    $ setWait(39.37,43.291)
    $ speak(JECKA, "Dad it's not that deep, we're just not allowed to call kids gay anymore.")
    $ setWait(43.291,45.71)
    $ speak(DAD, "They're not actually gay, are they?")
    show jecka sc12 sad:
        rightstage
    $ setWait(45.71,46.92)
    $ speak(JECKA, "Uh...")
    show jecka sc12:
        rightstage
        linear 2.5 leftstage
        xzoom -1

    $ setWait(46.92,49.255)
    $ speak(JECKA, "I'm gonna avoid this one, I'll see ya later dad.")
    show dad shorts:
        leftcenterstage
        xzoom 1

    $ setWait(49.255,51.758)
    $ speak(DAD, "Wait hold on, where are you going?")
    show jecka sc12 angry:
        leftstage
        xzoom -1
    $ setWait(51.758,52.55)
    $ speak(JECKA, "Out?")
    show dad shorts upset:
        leftcenterstage

    $ setWait(52.55,57.347)
    $ speak(DAD, "You've been going out a few times a week lately, anything I should know?")
    $ setWait(57.347,60.1)
    $ speak(JECKA, "Yeah child abuse actually leads to failing grades.")
    $ setWait(60.1,61.935)
    $ speak(DAD, "No, who are you seeing?")
    $ setWait(61.935,63.228)
    $ speak(JECKA, "Friends.")
    $ setWait(63.228,65.438)
    $ speak(DAD, "You're out studying, right?")
    show jecka sc12:
        leftstage
        xzoom -1
    $ setWait(65.438,67.482)
    $ speak(JECKA, "Of course, haven't you seen my grades?")
    $ setWait(67.482,69.025)
    $ speak(DAD, "You're not seeing a boy, are you?")
    show jecka sc12 angry:
        leftstage
        xzoom -1
    $ setWait(69.025,70.318)
    $ speak(JECKA, "And what if I was?")
    show dad shorts:
        leftcenterstage


    $ setWait(70.318,72.028)
    $ speak(DAD, "Oh nothing...")
    $ setWait(72.028,74.239)
    $ speak(DAD, "It's just if you came home pregnant I'd...")
    show dad shorts yell:
        leftcenterstage
        linear 0.2 leftmidstage

    show jecka sc12 sad:
        leftstage
        xzoom -1
        linear .07 xalign -0.13
        linear .07 xalign -0.09
        linear .07 xalign -0.13
        linear .07 xalign -0.09
        linear .08 leftstage

    $ setWait(74.239,76.282)
    $ speak(DAD, "...beat the fucking baby out of you!!!")
    $ setWait(76.282,77.951)
    $ speak(JECKA, "No Dad! I'm just going out, okay!?")
    show dad shorts angry:
        leftmidstage

    $ setWait(77.951,78.952)
    $ speak(DAD, "No boyfriend!?")
    $ setWait(78.952,79.994)
    $ speak(JECKA, "Definitely not!")
    $ setWait(79.994,80.954)
    $ speak(DAD, "Yeah we'll see!")
    show jecka sc12 sad:
        leftstage
        pause 0.6
        xzoom 1
        linear 0.26 off_left

    $ setWait(80.954,82.705)
    $ speak(JECKA, "Okay dad, bye!")
    $ setWait(82.705,84.833)
    $ speak(DAD, "God I wish breaking her legs was legal!!")
    show dad shorts angry:
        leftmidstage
        xzoom -1
        linear 4.5 off_right

    $ setWait(84.833,88.169)
    $ speak(DAD, "Where the fuck's the remote I wanna watch Ugly Betty.")
    stop ambient fadeout 1.5
    jump scene_S0085

label scene_S0085:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0085.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 3
    show katz 3:
        centerstage

    show ari sc2:
        leftmidstage
        xzoom -1

    show megan sc2:
        leftstage
        xzoom -1

    show karen sc1:
        rightmidstage

    show jecka sc6:
        rightstage

    $ setWait(0.044,7.218)
    $ speak(KATZ, "And so that's why the Chinese Exclusion Act was a little problematic.")
    $ setWait(7.218,8.261)
    $ speak(KATZ, "Ari?")
    show ari sc2 sad:
        leftmidstage
        xzoom -1
    $ setWait(8.261,12.098)
    $ speak(ARI, "Was it necessary for you to tell us all the slurs they were using?")
    show karen sc1 sad:
        rightmidstage

    $ setWait(12.098,14.809)
    $ speak(KAREN, "Yeah and why'd you put the F-word before all of them?")
    $ setWait(14.809,20.064)
    $ speak(KATZ, "Again. Reciting quotes from history, not a big deal.")

    $ setWait(20.064,23.276)
    $ speak(JECKA, "You'd say all that stuff at the podium of a lecture?")
    show katz 3:
        centerstage
        xzoom -1

    show karen sc1:
        rightmidstage

    show ari sc2:
        leftmidstage
        xzoom -1

    $ setWait(23.276,27.989)
    $ speak(KATZ, "Of course, it'd be irresponsible if I didn't. It's like that time we went to Olive Garden, when you--")
    show ari sc2 shy:
        leftmidstage
        xzoom -1
    $ setWait(27.989,29.574)
    $ speak(ARI, "Wait you went to Olive Garden together??")
    show jecka sc6 surprised:
        rightstage

    $ setWait(29.574,30.032)
    $ speak(JECKA, "Uh??")
    show katz 3 weird:
        centerstage
        xzoom 1

    $ setWait(30.032,34.162)
    $ speak(KATZ, "Oh no! I didn't mean her and I, I meant as in with my family!")
    $ setWait(34.162,35.329)
    $ speak(KAREN, "You have a family?")
    show katz 3 sad:
        centerstage
        xzoom -1

    $ setWait(35.329,37.957)
    $ speak(KATZ, "Uh um, uh l-like my parents.")

    show jecka sc6:
        rightstage

    show ari sc2:
        leftmidstage
        xzoom -1

    $ setWait(37.957,39.333)
    $ speak(ARI, "Ohhhkay.")
    $ setWait(39.333,41.043)
    $ speak(KAREN, "Yeah I was about to say.")
    show katz 3:
        centerstage
        xzoom 1

    show megan sc2:
        xzoom -1
        leftstage
        pause 1.4
        xzoom 1
        linear 1 off_left

    show ari sc2:
        leftmidstage
        xzoom -1
        pause 1.2
        xzoom 1
        linear 1.7 off_left

    show karen sc1:
        rightmidstage
        pause 2
        linear 5.2 off_left

    $ setWait(41.043,45.715)
    $ speak(KATZ, "Well anyway, good luck on your crossword puzzles. They're due next class.")
    $ setWait(45.715,47.675)
    $ speak(KAREN, "I hope the answers aren't racist.")
    show katz 3:
        xzoom -1
        centerstage
    $ setWait(47.675,51.763)
    $ speak(KATZ, "Jecka I think we might need to have a little talk.")
    show jecka sc6:
        rightstage
        linear 1 rightmidstage

    $ setWait(51.763,53.139)
    $ speak(JECKA, "About what?")
    hide karen sc1
    hide ari sc2
    hide megan sc2

    $ setWait(53.139,56.1)
    $ speak(KATZ, "Our uh... little arrangement.")
    $ setWait(56.1,57.185)
    $ speak(JECKA, "What about it?")
    show katz 3 weird:
        centerstage
        xzoom -1

    $ setWait(57.185,61.898)
    $ speak(KATZ, "Let's y'know, just be careful and try to keep things on the down low.")
    show jecka sc6 angry:
        rightmidstage
    $ setWait(61.898,63.524)
    $ speak(JECKA, "You're the one who almost fucked it up.")
    show katz 3 sad:
        centerstage
        xzoom -1

    $ setWait(63.524,65.818)
    $ speak(KATZ, "Just a little hiccup, won't happen again.")
    show jecka sc6:
        rightmidstage

    $ setWait(65.818,68.279)
    $ speak(JECKA, "Let's hope you handle yourself better around police.")
    $ setWait(68.279,71.032)
    $ speak(KATZ, "Police? There won't be any police, right?")
    $ setWait(71.032,72.158)
    $ speak(JECKA, "I guess not.")
    show katz 3 weird:
        centerstage

    $ setWait(72.158,73.993)
    $ speak(KATZ, "You were beautiful in class today.")
    $ setWait(73.993,75.787)
    $ speak(JECKA, "Really? I was just spacing out.")
    $ setWait(75.787,79.04)
    $ speak(KATZ, "So effortless! You won't leave me, right?")
    show jecka sc6:
        rightmidstage
        xzoom -1
        pause 1.95
        xzoom 1

    $ setWait(79.04,82.21)
    $ speak(JECKA, "Oh uh... Ask again later.")
    $ setWait(82.21,86.464)
    $ speak(KATZ, "Ahahaha you're so funny! Like the 8 ball, right?")
    $ setWait(86.464,90.134)
    $ speak(JECKA, "Like 8 ball the 8 ball or 8 ball the drugs?")
    $ setWait(90.134,94.931)
    $ speak(KATZ, "Nevermind that, I got a great place lined up for dinner tonight. Joe's Crab Shack!")
    show jecka sc6 sad:
        rightmidstage

    $ setWait(94.931,96.766)
    $ speak(JECKA, "Aww do we have to go there again?")
    show katz 3 sad:
        centerstage
        xzoom -1

    $ setWait(96.766,98.392)
    $ speak(KATZ, "What you don't like Joe's?")
    show jecka sc6 angry:
        rightmidstage

    $ setWait(98.392,100.52)
    $ speak(JECKA, "Crabs looks like bugs I don't wanna eat that shit!")
    $ setWait(100.52,102.396)
    $ speak(KATZ, "Aw but I have reservations!")
    show jecka sc6:
        rightmidstage

    $ setWait(102.396,103.731)
    $ speak(JECKA, "It's a chain restaurant.")
    show katz 3 weird:
        centerstage
        xzoom -1
    $ setWait(103.731,106.192)
    $ speak(KATZ, "C'mon I'll give you extra credit if you go with me.")
    show jecka sc6 angry:
        rightmidstage
    $ setWait(106.192,107.652)
    $ speak(JECKA, "Ugh alright fine.")
    $ setWait(107.652,110.029)
    $ speak(KATZ, "See? That's my little girl.")
    show jecka sc6:
        rightmidstage

    $ setWait(110.029,110.822)
    $ speak(JECKA, "Whatever.")
    $ setWait(110.822,113.825)
    $ speak(KATZ, "You're such a good cute little girl for daddy.")
    show jecka sc6 sad:
        rightmidstage

    $ setWait(113.825,117.036)
    $ speak(JECKA, "Oh y-you're into that... alright.")
    $ setWait(117.036,120.456)
    $ speak(KATZ, "On top of that, why don't we get you some ice cream after?")
    show jecka sc6:
        rightmidstage

    $ setWait(120.456,123.292)
    $ speak(JECKA, "Yeah sure, okay can I go to lunch now?")
    $ setWait(123.292,127.255)
    $ speak(KATZ, "Of course, I don't wanna be controlling or abusive.")
    show jecka sc6:
        rightmidstage
        linear 3.4 off_left

    show katz 3 weird:
        centerstage
        xzoom -1
        pause 1.2
        xzoom 1

    $ setWait(127.255,130.258)
    $ speak(JECKA, "Bare minimum, that's great. I'll see ya later.")
    stop ambient fadeout 1.5
    jump scene_S0086

label scene_S0086:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0


    $ setVoiceTrack("audio/Scenes/0086.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1

    scene cafeteria int 2
    show jecka sc6:
        rightcenterstage

    show nicole sc5:
        leftcenterstage

    $ setWait(0.037,2.957)
    $ speak(NICOLE, "Do you know what D&D is?")
    $ setWait(2.957,4.166)
    $ speak(JECKA, "Dick and Denny's?")
    $ setWait(4.166,5.126)
    $ speak(NICOLE, "The restaurant?")
    $ setWait(5.126,6.502)
    $ speak(JECKA, "I guess I don't know.")
    $ setWait(6.502,10.047)
    $ speak(NICOLE, "I don't think Jeffery has any burning obsession with dick and Denny's.")
    $ setWait(10.047,11.465)
    $ speak(JECKA, "You were talking to Jeffery?")
    $ setWait(11.465,16.178)
    $ speak(NICOLE, "No I was just kinda there and he kept going on about this D&D thing.")
    $ setWait(16.178,17.555)
    $ speak(JECKA, "Like what about it?")
    $ setWait(17.555,21.893)
    $ speak(NICOLE, "Something about probability and sheets and... dragons?")
    $ setWait(21.893,24.395)
    $ speak(JECKA, "Dragon's-- Like Dungeon's & Dragons?")
    $ setWait(24.395,26.689)
    $ speak(NICOLE, "Yeah is it like a board game?")
    $ setWait(26.689,32.445)
    $ speak(JECKA, "D&D's basically Monopoly for people who write letters with magazine clippings.")
    $ setWait(32.445,34.655)
    $ speak(NICOLE, "Oh.. so white people?")
    $ setWait(34.655,36.616)
    $ speak(JECKA, "Yeah it's like a Jim Crow-level hobby.")
    $ setWait(36.616,37.867)
    $ speak(NICOLE, "How do you even know about it?")
    $ setWait(37.867,41.412)
    $ speak(JECKA, "My cousin took me to Wizards in Springfield Mall back when it was open.")
    $ setWait(41.412,42.997)
    $ speak(NICOLE, "There was a whole store for it?")
    $ setWait(42.997,46)
    $ speak(JECKA, "Yeah I was like 12 and these ugly college guys were hitting on me.")
    $ setWait(46,46.918)
    $ speak(NICOLE, "What'd you do?")
    $ setWait(46.918,50.922)
    $ speak(JECKA, "Nothing, I didn't realize that back then. Were you in class with Jeffery?")
    $ setWait(50.922,52.423)
    $ speak(NICOLE, "Uh, not really.")
    show jecka sc6 surprised:
        rightcenterstage

    $ setWait(52.423,56.844)
    $ speak(JECKA, "Wait.. you were in contact with Jeffery in an extra-curricular way?")
    $ setWait(56.844,62.642)
    $ speak(NICOLE, "I guess, my Mom sorta like... Whatever. But it's not like it was just Jeffery, I saw a few other guys too.")
    show jecka sc6 angry:
        rightcenterstage

    $ setWait(62.642,65.478)
    $ speak(JECKA, "That's like saying \"I didn't just murder someone I stole a car too\".")
    show nicole sc5 angry:
        leftcenterstage

    $ setWait(65.478,67.063)
    $ speak(NICOLE, "Fuck you, you're seeing your teacher.")
    $ setWait(67.063,70.107)
    $ speak(JECKA, "Yeah cause I get a good grade out of it, what the fuck are you getting?")
    show nicole sc5 sad:
        leftcenterstage

    $ setWait(70.107,71.901)
    $ speak(NICOLE, "This conversation I guess.")
    show jecka sc6:
        rightcenterstage

    $ setWait(71.901,76.072)
    $ speak(JECKA, "Well, at least we can talk about it. If anyone else knew about this I'd be on the news.")
    show nicole sc5:
        leftcenterstage

    $ setWait(76.072,79.659)
    $ speak(NICOLE, "I wish it was my teacher, the news won't care about me 'till it's too late.")
    $ setWait(79.659,82.828)
    $ speak(JECKA, "I'm not an expert or whatever but you could see the school therapist.")
    $ setWait(82.828,83.996)
    $ speak(NICOLE, "What's she gonna do?")
    $ setWait(83.996,86.499)
    $ speak(JECKA, "Help with your problems? Is that what therapy is?")
    show nicole sc5 angry:
        leftcenterstage

    $ setWait(86.499,89.377)
    $ speak(NICOLE, "Fuck no, they just sit there go \"what do you think the answer is?\"")
    show jecka sc6 smile:
        rightcenterstage

    show nicole sc5:
        leftcenterstage

    $ setWait(89.377,95.216)
    $ speak(JECKA, "Well this can just be our therapy then. All we need is a coffee machine and the most un-fuckable wardrobe imaginable.")
    $ setWait(95.216,96.509)
    $ speak(NICOLE, "Whatever works for ya.")
    $ setWait(96.509,97.885)
    $ speak(JECKA, "I totally got this.")
    stop ambient fadeout 1.5
    jump scene_S0087

label scene_S0087:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0087.mp3")
    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene georgetown
    show jecka sc9 angry:
        leftcenterstage
        xzoom -1

    show katz 4 smile:
        rightmidstage
    $ setWait(0.041,2.294)
    $ speak(KATZ, "Isn't it just wonderful out here?")
    $ setWait(2.294,4.796)
    $ speak(JECKA, "Why'd you take me all the way out to Georgetown??")
    show katz 4 sad:
        rightmidstage

    $ setWait(4.796,6.339)
    $ speak(KATZ, "Y-you don't like it?")
    $ setWait(6.339,10.135)
    $ speak(JECKA, "No I love Georgetown, but it's expensive as shit and you don't have the money to spoil me.")
    $ setWait(10.135,16.767)
    $ speak(KATZ, "Hey, hey, I thought it'd be a safer idea to have our dates be a little further out so less people would recognize us.")
    $ setWait(16.767,20.479)
    $ speak(JECKA, "I mean, look at you and look at me, this is still kinda high profile.")
    show katz 4:
        rightmidstage

    $ setWait(20.479,23.94)
    $ speak(KATZ, "Well how bout somewhere a little darker, like the movies?")
    show jecka sc9:
        leftcenterstage
        xzoom -1
    $ setWait(23.94,25.942)
    $ speak(JECKA, "What movie could you possibly wanna see with me?")
    show katz 4 angry:
        rightmidstage
        linear 0.4 rightcenterstage

    $ setWait(25.942,27.861)
    $ speak(KATZ, "Will you just stop and go with me??")
    show jecka sc9 sad:
        leftcenterstage
        xzoom -1
        linear 0.6 leftmidstage

    $ setWait(27.861,28.528)
    $ speak(JECKA, "Calm down.")
    show katz 4 angry:
        rightcenterstage
        linear 0.3 leftcenterstage

    $ setWait(28.528,30.655)
    $ speak(KATZ, "Shut the fuck up! Just do what I say!")
    $ setWait(30.655,33.658)
    $ speak(JECKA, "Wha? Um.. Okay...")
    show katz 4 weird:
        leftcenterstage
    $ setWait(33.658,36.62)
    $ speak(KATZ, "That's right, now that's a good girl, now let's go.")
    show jecka sc9:
        xzoom 1
        leftmidstage
    $ setWait(36.62,38.705)
    $ speak(JECKA, "Hold on I need a cigarette first.")
    hide jecka sc9
    hide katz 4 weird
    $ csbox = True
    scene cut0087a
    $ setWait(38.705,39.456)
    $ speak(JECKA, "...")
    $ setWait(39.456,41.082)
    $ speak(KATZ, "You like the ones I bought for you?")
    scene cut0087b
    $ setWait(41.082,43.46)
    $ speak(JECKA, "Ughhhhhh fuck me...")
    $ setWait(43.46,45.504)
    $ speak(KATZ, "You like them, they're really good, right?")
    scene cut0087c
    $ setWait(45.504,47.214)
    $ speak(JECKA, "They're okay, whatever.")
    $ setWait(47.214,49.174)
    $ speak(KATZ, "I bet you liked that extra credit though.")
    scene cut0087d
    $ setWait(49.174,51.885)
    $ speak(JECKA, "Okay okay they're great, I love 'em, thank you.")
    $ setWait(51.885,55.138)
    $ speak(KATZ, "Good now hold daddy's hand let's go to the movies.")
    scene cut0087e
    $ setWait(55.138,56.306)
    $ speak(JECKA, "Sure.")
    $ setWait(56.306,59.1)
    $ speak(KATZ, "Good thinking with that cigarette, you look so much older now.")
    $ setWait(59.1,61.52)
    $ speak(JECKA, "Yeah now I only look one half your age.")
    scene cut0087f
    $ setWait(61.52,63.021)
    $ speak(KATZ, "Enough!")
    stop ambient fadeout 1.5
    jump scene_S0088

label scene_S0088:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show school front with Pause(2.715):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.715 zoom 1.05 truecenter
    $ setVoiceTrack("audio/Scenes/0088.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3"
    $ csbox = False
    scene office 1
    show jecka sc7:
        off_left
        xzoom -1
        linear 2.2 leftmidstage

    show ames 1 smile:
        rightmidstage

    $ setWait(2.715,4.174)
    $ speak(AMES, "How could I help you?")
    $ setWait(4.174,7.219)
    $ speak(JECKA, "Are you the school therapist?")
    $ setWait(7.219,13.183)
    $ speak(AMES, "Yes I just started here this school year. Glad to see the fliers haven't been defaced with Spongebob bandaids.")
    show ames 1:
        rightmidstage

    $ setWait(13.183,15.936)
    $ speak(JECKA, "Oh they were, I had to peel 'em off on one.")
    $ setWait(15.936,18.063)
    $ speak(AMES, "That's okay.")
    show jecka sc7 surprised:
        leftmidstage
        xzoom -1

    $ setWait(18.063,19.732)
    $ speak(JECKA, "You're not mad?")

    $ setWait(19.732,22.568)
    $ speak(AMES, "Impressed to see the results of proper therapy?")
    show jecka sc7:
        leftmidstage
        xzoom -1
    $ setWait(22.568,24.445)
    $ speak(JECKA, "No I just thought you were weird.")
    $ setWait(24.445,27.197)
    $ speak(AMES, "Have a seat, what brings you in today?")
    show jecka sc7:
        leftmidstage
        xzoom -1
        linear 1.3 centerstage

    $ setWait(27.197,30.993)
    $ speak(JECKA, "It's kinda about this guy I'm seeing.")
    $ setWait(30.993,33.704)
    $ speak(AMES, "Could you speak with your parents about it?")
    show jecka sc7 sad:
        centerstage
        xzoom -1
    $ setWait(33.704,38.959)
    $ speak(JECKA, "What? -No, not cause it's weird, it's just I don't want 'em to know.")
    $ setWait(38.959,44.381)
    $ speak(AMES, "Don't worry I hear that almost every time when it comes to high school dating issues.")
    show jecka sc7:
        centerstage
        xzoom -1
    $ setWait(44.381,46.675)
    $ speak(JECKA, "Oh cool, alright.")
    $ setWait(46.675,47.885)
    $ speak(AMES, "So what's their name?")
    $ setWait(47.885,49.428)
    $ speak(JECKA, "I can't tell you that.")
    $ setWait(49.428,52.139)
    $ speak(AMES, "Are they older or younger than you?")
    $ setWait(52.139,55.392)
    $ speak(JECKA, "Uh.. maybe just a little older.")
    $ setWait(55.392,57.394)
    $ speak(AMES, "And do they go here?")
    $ setWait(57.394,58.937)
    $ speak(JECKA, "Yeah technically.")
    $ setWait(58.937,63.275)
    $ speak(AMES, "Okay and where exactly is the problem stemming from?")
    $ setWait(63.275,67.363)
    $ speak(JECKA, "Kinda like everywhere. I'm not attracted to him for one.")
    $ setWait(67.363,71.533)
    $ speak(AMES, "Then why would you romantically involve yourself in the first place?")
    show jecka sc7 sad:
        centerstage
        xzoom -1
    $ setWait(71.533,74.119)
    $ speak(JECKA, "W-Wow so it's all about looks? Shallow much?")
    $ setWait(74.119,78.29)
    $ speak(AMES, "I'm simply asking why couldn't you stay friends?")
    show jecka sc7:
        centerstage
        xzoom -1

    $ setWait(78.29,85.422)
    $ speak(JECKA, "It's complicated, he has a lot of control over how my life goes so it's best to make him happy.")
    $ setWait(85.422,89.051)
    $ speak(AMES, "So you're dating not for your own happiness, but his?")
    $ setWait(89.051,96.308)
    $ speak(JECKA, "Yeah but sort of like... I don't know- if he's happy I'll be happier in the long run.")
    $ setWait(96.308,100.104)
    $ speak(AMES, "And what exactly in your life does he have control over?")
    show jecka sc7 sad:
        centerstage
        xzoom -1
    $ setWait(100.104,102.147)
    $ speak(JECKA, "That is a really personal question.")
    show ames 1 smug:
        rightmidstage

    $ setWait(102.147,103.19)
    $ speak(AMES, "You're in therapy.")
    show jecka sc7 angry:
        centerstage
        xzoom -1
    $ setWait(103.19,105.609)
    $ speak(JECKA, "Oh I didn't know this was the no-consent room!")
    show ames 1:
        rightmidstage

    $ setWait(105.609,110.906)
    $ speak(AMES, "You don't have to share anything you don't want to. It's just this is a private space.")
    show jecka sc7:
        centerstage
        xzoom -1
    $ setWait(110.906,115.494)
    $ speak(JECKA, "Okay well you got the jist so help me, what do I do?")
    $ setWait(115.494,124.002)
    $ speak(AMES, "So generally we consider a one-sided controlling relationship an abusive relationship.")
    $ setWait(124.002,131.218)
    $ speak(AMES, "However if I don't know the insides of this relationship all I can really do is offer coping strategies.")
    $ setWait(131.218,132.845)
    $ speak(JECKA, "Yeah sure gimme those.")
    $ setWait(132.845,141.603)
    $ speak(AMES, "Well it's good to have a supportive friend network so spend more time with your friends, if they're true friends they'll empathize with you.")
    $ setWait(141.603,146.024)
    $ speak(JECKA, "But what if my friends are more abusive than my boyfriends?")
    $ setWait(146.024,147.734)
    $ speak(AMES, "Then why are they your friends?")
    show jecka sc7 sad:
        centerstage
        xzoom -1
    $ setWait(147.734,148.777)
    $ speak(JECKA, "Long story.")
    $ setWait(148.777,155.451)
    $ speak(AMES, "But the point stands, more time and acitivies with your friends can serve as a temporary coping mechanism.")
    show jecka sc7 smile:
        centerstage
        xzoom -1
    $ setWait(155.451,157.161)
    $ speak(JECKA, "I guess that makes sense.")
    $ setWait(157.161,161.123)
    $ speak(AMES, "So unless there's any further questions I'll be off to lunch now.")
    show jecka sc7:
        centerstage
        xzoom -1
    $ setWait(161.123,163.834)
    $ speak(JECKA, "Is it cold pasta salad in tupperware?")
    $ setWait(163.834,164.71)
    $ speak(AMES, "How'd you know?")
    $ setWait(164.71,167.504)
    $ speak(JECKA, "Cause that's what all public school teachers eat for lunch.")
    $ setWait(167.504,168.672)
    $ speak(AMES, "Again, if that's all--")
    show jecka sc7 surprised:
        centerstage
        xzoom -1
    $ setWait(168.672,171.258)
    $ speak(JECKA, "Wait I actually had one more question!")
    $ setWait(171.258,172.426)
    $ speak(AMES, "Yes?")
    show jecka sc7 sad:
        centerstage
        xzoom -1
    $ setWait(172.426,174.636)
    $ speak(JECKA, "Okay how would I word this...")
    show jecka sc7:
        centerstage
        xzoom -1
    $ setWait(174.636,184.396)
    $ speak(JECKA, "What's more important; my happiness right now or possible future happiness from my status in life later?")
    show ames 1 smile:
        rightmidstage

    $ setWait(184.396,186.273)
    $ speak(AMES, "Well what do you think the answer is?")
    show jecka sc7 angry:
        centerstage
        xzoom -1
    $ setWait(186.273,188.192)
    $ speak(JECKA, "Bitch I'm asking you!")
    $ setWait(188.192,189.902)
    $ speak(AMES, "Can I eat my pasta salad now?")
    show jecka sc7 surprised:
        centerstage
        xzoom -1
    $ setWait(189.902,194.323)
    $ speak(JECKA, "Okay no- one more thing! Totally unrelated to anything we talked about!")
    show ames 1 smug:
        rightmidstage
    $ setWait(194.323,195.157)
    $ speak(AMES, "What is it?")
    $ setWait(195.157,197.367)
    $ speak(JECKA, "Seriously, unrelated...")
    show ames 1:
        rightmidstage

    show jecka sc7:
        centerstage
        xzoom -1

    $ setWait(197.367,206.835)
    $ speak(JECKA, "If a guy mainly gets off on me acting like a little girl and doing little girl voices...")
    show jecka sc7 sad:
        centerstage
        xzoom -1
    $ setWait(206.835,210.255)
    $ speak(JECKA, "...Does that mean he'd fuck an actual little girl?")
    $ setWait(210.255,211.757)
    $ speak(AMES, "...Is that a trick question?")
    stop ambient fadeout 1.6

    jump scene_S0089

label scene_S0089:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0089.mp3")
    play ambient "audio/Ambience/House_Ambience_2.mp3" fadein 1
    scene livingroom jecka

    show jecka pj sad:
        centerstage
        linear 1.7 leftcenterstage

    $ setWait(0.038,2.04)
    $ speak(JECKA, "What I'm doing's actually crazy.")
    show jecka pj sad:
        xzoom -1
        leftcenterstage
        linear 0.5 centerstage

    $ setWait(2.04,4.084)
    $ speak(JECKA, "This is like an Amanda Bynes movie!")

    show jecka pj sad:
        leftcenterstage
        xzoom 1
        linear 0.6 leftcenterstage

    $ setWait(4.084,7.212)
    $ speak(JECKA, "I don't think the grade's worth it, I gotta break it off.")
    show dad undershirt smile:
        off_right
        linear 1 rightstage

    $ setWait(7.212,9.131)
    $ speak(DAD, "There's my favorite daughter!")
    show jecka pj surprised:
        xzoom -1
        leftcenterstage
        linear 0.08 xalign .39
        linear 0.08 xalign .35
        linear 0.08 xalign .39
        linear 0.08 leftcenterstage

    $ setWait(9.131,10.298)
    $ speak(JECKA, "What??")
    show dad undershirt:
        rightstage
        linear 1.3 rightmidstage

    $ setWait(10.298,12.259)
    $ speak(DAD, "There's my favorite daughter...")
    show jecka pj:
        leftcenterstage
        xzoom -1

    $ setWait(12.259,14.636)
    $ speak(JECKA, "I'm your only daughter, Dad can I talk to you about--")
    show dad undershirt smile:
        rightmidstage

    $ setWait(14.636,19.307)
    $ speak(DAD, "Wait I just wanted to say I love to see great news in my email about you!")
    show jecka pj smile:
        leftcenterstage
        xzoom -1

    $ setWait(19.307,21.101)
    $ speak(JECKA, "Did I win the Spice Girls sweepstakes?")
    show dad undershirt:
        rightmidstage

    $ setWait(21.101,23.061)
    $ speak(DAD, "You mailed that in 10 years ago.")
    show jecka pj:
        leftcenterstage
        xzoom -1

    $ setWait(23.061,24.146)
    $ speak(JECKA, "It could still happen.")

    show dad undershirt smile:
        rightmidstage

    $ setWait(24.146,28.024)
    $ speak(DAD, "No, you're on honor roll! The school website just told me.")
    show jecka pj surprised:
        leftcenterstage

    $ setWait(28.024,30.36)
    $ speak(JECKA, "Oh that's.. huh.")
    $ setWait(30.36,37.784)
    $ speak(DAD, "I knew that turnaround in AP History was a good sign. I swear that was always your weakest subject but you made it work.")
    show jecka pj sad:
        leftcenterstage
        xzoom -1

    $ setWait(37.784,40.662)
    $ speak(JECKA, "Yeah it's like I sold my soul for that grade.")
    $ setWait(40.662,45.375)
    $ speak(DAD, "Acceptance letters flooding out of the mailbox, like that scene in Harry Potter!")
    show jecka pj:
        leftcenterstage
        xzoom -1

    $ setWait(45.375,47.627)
    $ speak(JECKA, "And here I thought you couldn't get any whiter.")
    show dad undershirt:
        rightmidstage

    $ setWait(47.627,50.755)
    $ speak(DAD, "Wh-Why aren't you excited, what's wrong?")

    show jecka pj sad:
        leftcenterstage
        xzoom -1

    $ setWait(50.755,60.849)
    $ speak(JECKA, "Dad, hypothetically what if I didn't wanna go to a great college, or even college in general?")
    show dad undershirt upset:
        rightmidstage

    $ setWait(60.849,62.726)
    $ speak(DAD, "You don't want to?")
    show jecka pj:
        leftcenterstage
        xzoom -1

    $ setWait(62.726,65.979)
    $ speak(JECKA, "No no- I do! Just hypothetically!")
    $ setWait(65.979,71.234)
    $ speak(DAD, "Well if you didn't go you'd be a failure, a waste of your mother and I's time in general.")
    show jecka pj sad:
        leftcenterstage
        xzoom -1

    $ setWait(71.234,71.985)
    $ speak(JECKA, "Really?")
    $ setWait(71.985,74.237)
    $ speak(DAD, "Aside from us, look at the reality.")
    show dad undershirt upset:
        rightmidstage
        linear 3 rightcenterstage

    $ setWait(74.237,80.702)
    $ speak(DAD, "Without a college degree you'll end up some worthless whore on the side of the road. Just a fragranced meat pile!")

    $ setWait(80.702,83.079)
    $ speak(JECKA, "Oh good thing I'm not doing that-")

    show dad undershirt angry:
        rightcenterstage
    $ setWait(83.079,86.541)
    $ speak(DAD, "If I ever saw you selling your body on the side of the road...")

    show dad undershirt yell:
        rightcenterstage
    $ setWait(86.541,91.338)
    $ speak(DAD, "...I'd take an aluminum baseball bat and beat your teeth out one-by-one!!")
    $ setWait(91.338,92.797)
    $ speak(JECKA, "Why does the material matter?")
    show dad undershirt smile:
        rightcenterstage

    $ setWait(92.797,96.927)
    $ speak(DAD, "Ugh but yeah, good thing your grades are your first priority.")
    $ setWait(96.927,98.011)
    $ speak(JECKA, "Great thing.")
    show dad undershirt:
        rightcenterstage

    $ setWait(98.011,99.638)
    $ speak(DAD, "So what were you saying earlier?")
    show jecka pj:
        leftcenterstage
        xzoom -1

    $ setWait(99.638,102.265)
    $ speak(JECKA, "N-nothing.. nothing at all.")
    show dad undershirt smile:
        rightcenterstage
        xzoom -1
        linear 3.2 off_right

    $ setWait(102.265,105.101)
    $ speak(DAD, "Good luck at school tomorrow.")
    show jecka pj sad:
        leftcenterstage
        xzoom -1
        linear 4 centerstage

    $ setWait(105.101,107.103)
    $ speak(JECKA, "Why couldn't it be the Spice Girls?")
    stop ambient fadeout 1.5
    jump scene_S0090

label scene_S0090:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0090.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school ext 6

    show jecka sc11:
        rightstage
        linear 1.4 rightcenterstage


    show nicole sc8:
        off_right
        xzoom -1
        linear 1.6 rightmidstage


    show lorre 1:
        leftmidstage
        xzoom -1

    $ setWait(0.036,2.83)
    $ speak(LORRE, "Oh here they come, hello girls!")
    $ setWait(2.83,4.665)
    $ speak(NICOLE, "Do you always need to be right where we smoke?")
    $ setWait(4.665,7.335)
    $ speak(LORRE, "Some teachers need a cigarette too.")
    $ setWait(7.335,10.546)
    $ speak(JECKA, "How are you a teacher when neither of us have seen you work in the school?")
    $ setWait(10.546,13.507)
    $ speak(LORRE, "I told you last week I only teach the seniors.")
    $ setWait(13.507,16.302)
    $ speak(JECKA, "Teach 'em what? How to kidnap a girl without a paper trail?")
    show nicole sc8 sad:
        rightmidstage
        xzoom -1
    $ setWait(16.302,18.721)
    $ speak(NICOLE, "Uh I just realized my pack's in the other backpack.")
    show jecka sc11:
        xzoom -1
    $ setWait(18.721,20.681)
    $ speak(JECKA, "Oh my god do we have to walk all the way back?")
    show nicole sc8:
        rightmidstage
        xzoom -1
    $ setWait(20.681,22.308)
    $ speak(NICOLE, "Maybe not, can we have yours?")
    show jecka sc11:
        xzoom 1

    $ setWait(22.308,25.603)
    $ speak(LORRE, "Have them? No, I can sell you the rest though.")
    $ setWait(25.603,26.228)
    $ speak(JECKA, "How much?")
    $ setWait(26.228,27.563)
    $ speak(LORRE, "Just 5 dollars.")
    show jecka sc11 angry:
        rightcenterstage
        xzoom 1
    $ setWait(27.563,30.358)
    $ speak(JECKA, "You're gonna be that petty over an open pack of cigarettes?")
    $ setWait(30.358,33.527)
    $ speak(LORRE, "Take it or leave it, I need to get back to work soon.")
    $ setWait(33.527,34.82)
    $ speak(NICOLE, "So you don't work here.")
    $ setWait(34.82,37.823)
    $ speak(LORRE, "No I work here, I meant off my break.")
    show jecka sc11:
        rightcenterstage
        pause 1.3
        linear 0.7 leftcenterstage
        linear 0.8 rightcenterstage

    $ setWait(37.823,39.7)
    $ speak(JECKA, "Yeah sure, here's the money.")
    $ setWait(39.7,42.578)
    $ speak(LORRE, "I'd love to have a chat with you girls some other time though.")
    $ setWait(42.578,44.121)
    $ speak(NICOLE, "Uh yeah, whatever.")
    show lorre 1:
        xzoom 1
        leftmidstage
        linear 2 off_left

    $ setWait(44.121,46.582)
    $ speak(LORRE, "I'll see you around.")
    show jecka sc11:
        rightcenterstage
        xzoom -1

    $ setWait(46.582,48.542)
    $ speak(JECKA, "Which of us do you think he wants to murder?")
    $ setWait(48.542,49.752)
    $ speak(NICOLE, "What do you mean \"which of us\"?")
    $ setWait(49.752,51.295)
    $ speak(JECKA, "Aw yeah it's probably both.")
    $ setWait(51.295,53.631)
    $ speak(NICOLE, "He gave us American Spirits, no way he's a teacher.")
    $ setWait(53.631,56.217)
    $ speak(JECKA, "Yeah teachers can't even afford the menthol in Newports.")
    $ setWait(56.217,60.012)
    $ speak(NICOLE, "But yeah I can only hang out for one, I gotta meet somebody for some concert.")
    show jecka sc11 sad:
        rightcenterstage
        xzoom -1
    $ setWait(60.012,61.055)
    $ speak(JECKA, "Just one?")
    $ setWait(61.055,63.683)
    $ speak(NICOLE, "Well yeah, how long do you need to be out here?")
    $ setWait(63.683,66.978)
    $ speak(JECKA, "Uh, a little longer? History's my next class.")
    $ setWait(66.978,70.606)
    $ speak(NICOLE, "Oh you gotta see Roman Polanski live-and-in classroom?")
    show jecka sc11:
        rightcenterstage
        xzoom -1
    $ setWait(70.606,72.733)
    $ speak(JECKA, "Who's Roman Polanski?")
    $ setWait(72.733,74.193)
    $ speak(NICOLE, "I don't know, it just sounded funny.")
    $ setWait(74.193,77.863)
    $ speak(JECKA, "Mr. Katz is kinda weird lately, like really paranoid.")
    show nicole sc8 angry:
        rightmidstage

    $ setWait(77.863,80.408)
    $ speak(NICOLE, "Daddy roleplay with a student? What's he worried about?")
    $ setWait(80.408,83.786)
    $ speak(JECKA, "I just gotta last 2 more months and I'm in the clear to break up.")
    $ setWait(83.786,84.87)
    $ speak(NICOLE, "Yeah...")
    $ setWait(84.87,86.497)
    $ speak(NICOLE, "...Unless he's your teacher next year.")

    show jecka sc11 surprised:
        rightcenterstage
        xzoom -1

    $ setWait(86.497,87.081)
    $ speak(JECKA, "What??")
    $ setWait(87.081,89.5)
    $ speak(NICOLE, "He teaches seniors too, I saw his class once.")

    show jecka sc11 sad:
        rightcenterstage
        xzoom -1

    $ setWait(89.5,93.17)
    $ speak(JECKA, "Oh my god, what if I break up with him over the summer and I get him again?")
    $ setWait(93.17,95.965)
    $ speak(NICOLE, "If you actually study and do the work it won't matter, right?")
    $ setWait(95.965,96.966)
    $ speak(JECKA, "I can't do that!")
    $ setWait(96.966,98.05)
    $ speak(NICOLE, "Yeah me neither.")
    show jecka sc11 angry:
        rightcenterstage
        xzoom -1

    $ setWait(98.05,101.887)
    $ speak(JECKA, "Why can't he just find some dumpy 30 year old bitch who also lives with her cats?")
    $ setWait(101.887,104.265)
    $ speak(NICOLE, "There's no power dynamic, that's not fun for him.")
    show jecka sc11:
        rightcenterstage
        xzoom -1

    $ setWait(104.265,108.269)
    $ speak(JECKA, "Yeah I guess I'd rather fuck me than some dumpy 30 year old bitch too.")
    $ setWait(108.269,112.523)
    $ speak(NICOLE, "I'd rather stay and smoke some more but I actually gotta get going to my hostage friendship.")
    show jecka sc11 sad:
        rightcenterstage
        xzoom -1

    $ setWait(112.523,113.399)
    $ speak(JECKA, "Already??")
    $ setWait(113.399,116.444)
    $ speak(NICOLE, "Yeah these taste like shit anyway, which is weird cause I usually like these.")
    $ setWait(116.444,117.611)
    $ speak(JECKA, "Maybe you're depressed.")

    show nicole sc8 angry:
        rightmidstage

    $ setWait(117.611,120.239)
    $ speak(NICOLE, "Depression isn't the flu, it doesn't make everything taste weird.")
    show jecka sc11:
        rightcenterstage
        xzoom -1

    $ setWait(120.239,121.741)
    $ speak(JECKA, "Depression affects everything.")
    show nicole sc8:
        rightmidstage
        pause 3.1
        xzoom 1
        linear 0.7 rightstage

    $ setWait(121.741,125.411)
    $ speak(NICOLE, "Yeah like my decision to leave and go talk to this idiot about his concert, alright bye.")
    show jecka sc11 sad:
        rightcenterstage
        xzoom -1

    $ setWait(125.411,126.746)
    $ speak(JECKA, "Wait no don't go!")
    show nicole sc8 angry:
        rightstage
        xzoom -1
    $ setWait(126.746,127.997)
    $ speak(NICOLE, "I have to go.")
    $ setWait(127.997,129.457)
    $ speak(JECKA, "You don't have to do anything.")
    $ setWait(129.457,130.916)
    $ speak(NICOLE, "You don't have to date your teacher.")
    show jecka sc11 angry:
        rightcenterstage
        xzoom -1
    $ setWait(130.916,132.084)
    $ speak(JECKA, "Yeah I do!")
    show nicole sc8:
        rightstage
        xzoom -1

    $ setWait(132.084,133.753)
    $ speak(NICOLE, "Sure, so can I go?")
    $ setWait(133.753,134.628)
    $ speak(JECKA, "Fine!")
    show jecka sc11 angry:
        xzoom 1
        linear 3 off_left

    $ setWait(134.628,135.921)
    $ speak(JECKA, "...Hate white people.")
    stop ambient fadeout 1.5
    jump scene_S0091

label scene_S0091:
    show black onlayer screens with Pause(3):
        alpha 0.0
        linear 2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0091.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 3

    show jecka sc11:
        rightcenterstage

    show katz 5 smile:
        leftcenterstage
        xzoom -1

    $ setWait(0.038,2.457)
    $ speak(KATZ, "We could bump that up a few points.")
    $ setWait(2.457,5.001)
    $ speak(JECKA, "Oh okay cool.")
    $ setWait(5.001,8.213)
    $ speak(KATZ, "And maybe a few more if uh...")
    $ setWait(8.213,9.547)
    $ speak(JECKA, "If what?")
    show katz 5 weird:
        leftcenterstage
        xzoom -1

    $ setWait(9.547,12.008)
    $ speak(KATZ, "You wear that little outfit I bought you.")
    $ setWait(12.008,15.637)
    $ speak(JECKA, "Like in public? It looks like it's from the kids section.")
    $ setWait(15.637,18.473)
    $ speak(KATZ, "Yeah it was a Kids \"R\" Us going out of business sale.")
    $ setWait(18.473,21.81)
    $ speak(JECKA, "Wow ballin' on a budget. Why do you want me to be a little girl so bad?")
    show katz 5 angry:
        leftcenterstage
        xzoom -1

    $ setWait(21.81,25.48)
    $ speak(KATZ, "Why do you beg for higher scores without doing the work yourself?")
    show jecka sc11 sad:
        rightcenterstage

    $ setWait(25.48,26.356)
    $ speak(JECKA, "Excuse me?")
    $ setWait(26.356,29.693)
    $ speak(KATZ, "I'm not so sure you actually appreciate everything I do for you.")
    $ setWait(29.693,30.443)
    $ speak(JECKA, "Yeah I do.")
    $ setWait(30.443,34.572)
    $ speak(KATZ, "Then why're you getting sloppy? Did you forget this needs to be a secret or do you want it to get out?")
    $ setWait(34.572,35.532)
    $ speak(JECKA, "How am I sloppy?")
    $ setWait(35.532,39.869)
    $ speak(KATZ, "Leaving the same exits I do, renaming me in your phone contacts, the list goes on.")
    show jecka sc11 angry:
        rightcenterstage

    $ setWait(39.869,41.746)
    $ speak(JECKA, "You told me to rename you in my contacts.")
    $ setWait(41.746,44.291)
    $ speak(KATZ, "Yes but not something as obvious as \"Teacher Date\"")
    $ setWait(44.291,45.333)
    $ speak(JECKA, "What am I supposed to do??")
    $ setWait(45.333,50.964)
    $ speak(KATZ, "Stop talking back and just.. do as a I say! I can feel 'em closing in, you didn't tell anyone about us, right??")
    show jecka sc11 surprised:
        rightcenterstage
    $ setWait(50.964,51.923)
    $ speak(JECKA, "Yeah, no one.")
    $ setWait(51.923,52.882)
    $ speak(KATZ, "Are you sure??")
    show jecka sc11:
        rightcenterstage

    $ setWait(52.882,54.718)
    $ speak(JECKA, "...No one, daddy.")
    show katz 5 weird:
        leftcenterstage
        xzoom -1

    $ setWait(54.718,58.179)
    $ speak(KATZ, "Aww that's a sweet girl, I'm sorry.")
    $ setWait(58.179,60.598)
    $ speak(JECKA, "Yeah sure. About my grade?")
    $ setWait(60.598,65.937)
    $ speak(KATZ, "Yes I'll bump it for you and you'll see me in your shirt I bought you next week. Deal?")
    show jecka sc11 sad:
        rightcenterstage

    $ setWait(65.937,67.188)
    $ speak(JECKA, "In class?")
    $ setWait(67.188,68.732)
    $ speak(KATZ, "What's wrong with that?")
    show jecka sc11:
        rightcenterstage

    $ setWait(68.732,73.778)
    $ speak(JECKA, "I don't know it just has Dora on it that's kinda..-yeah I'll do it.")
    $ setWait(73.778,76.239)
    $ speak(KATZ, "That's a good little girl. Run along.")
    show jecka sc11 angry:
        rightcenterstage
        linear 3.5 off_left

    $ setWait(76.239,79.534)
    $ speak(JECKA, "Yes daddy, right into oncoming traffic.")
    stop ambient fadeout 1.5
    jump scene_S0092

label scene_S0092:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0092.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 1

    show jecka sc13:
        centerstage
        xzoom -1

    show ames 2:
        rightmidstage

    $ setWait(0.003,5.842)
    $ speak(AMES, "So you've come in about this a few times now, what sort of progress can we make here?")
    $ setWait(5.842,10.055)
    $ speak(JECKA, "Progress? I'm kinda just doing this to get out of class now.")
    show ames 2 smug:
        rightmidstage
    $ setWait(10.055,15.644)
    $ speak(AMES, "Progress in regards to the relationship? How it affects your future and home life.")
    $ setWait(15.644,21.608)
    $ speak(JECKA, "Oh. I'm not really sure if that's ever gonna get better at this point.")
    show ames 2:
        rightmidstage
    $ setWait(21.608,24.486)
    $ speak(AMES, "Is there anything else you'd like to tell me?")
    show jecka sc13 sad:
        centerstage
        xzoom -1
    $ setWait(24.486,28.531)
    $ speak(JECKA, "I already told you I'm caught between an abusive relationship and my dad hating me.")
    $ setWait(28.531,29.658)
    $ speak(AMES, "Why do you say that?")
    show jecka sc13:
        centerstage
        xzoom -1
    $ setWait(29.658,30.951)
    $ speak(JECKA, "Cause it's happening?")
    $ setWait(30.951,32.994)
    $ speak(AMES, "No- your father hating you?")
    show jecka sc13 sad:
        centerstage
        xzoom -1
    $ setWait(32.994,39.834)
    $ speak(JECKA, "Oh, yeah. You're not allowed to tell anyone about what I tell you here, right?")
    $ setWait(39.834,42.963)
    $ speak(AMES, "Of course I can't, that'd defeat the purpose of therapy.")
    $ setWait(42.963,47.384)
    $ speak(JECKA, "And you swear you won't? Like not even your friends to laugh about your job?")
    $ setWait(47.384,48.843)
    $ speak(AMES, "Don't be ridiculous.")
    show jecka sc13:
        centerstage
        xzoom -1
    $ setWait(48.843,51.388)
    $ speak(JECKA, "Oh yeah you don't look like the having-friends type anyway.")
    show ames 2 smug:
        rightmidstage

    $ setWait(51.388,53.181)
    $ speak(AMES, "Your father.")

    $ setWait(53.181,57.811)
    $ speak(JECKA, "Uh I guess like... Nothing's ever good enough for him.")
    show ames 2:
        rightmidstage

    $ setWait(57.811,59.354)
    $ speak(AMES, "How so?")

    $ setWait(59.354,67.07)
    $ speak(JECKA, "Like.. I don't know, I'll go pick up Popeyes for the family and make sure they don't put too little gravy in the mashed potatoes- cause they always do that.")
    $ setWait(67.07,74.035)
    $ speak(JECKA, "And I'll come home like \"look dad\" and he'll open up the chicken like \"there's only 23 pieces in here, why didn't you check!?\"")
    $ setWait(74.035,75.996)
    $ speak(AMES, "So nagging you would say?")
    show jecka sc13 sad:
        centerstage
        xzoom -1

    $ setWait(75.996,81.71)
    $ speak(JECKA, "It's more than nagging, if I don't graduate and go to a school he approves of he just says I'll end up a whore.")
    $ setWait(81.71,83.753)
    $ speak(AMES, "I hope that's an exaggeration.")
    show jecka sc13:
        centerstage
        xzoom -1
    $ setWait(83.753,86.715)
    $ speak(JECKA, "No that's about as tame as I can put it.")
    $ setWait(86.715,91.011)
    $ speak(AMES, "And what do you think your father would do if he found out about this relationship you're in?")
    show jecka sc13 angry:
        centerstage
        xzoom -1
    $ setWait(91.011,92.721)
    $ speak(JECKA, "Beat the shit out of me.")
    $ setWait(92.721,94.222)
    $ speak(AMES, "And you're completely sure?")
    $ setWait(94.222,97.225)
    $ speak(JECKA, "Why wouldn't he? I'd beat the shit out of me for dating this guy.")
    $ setWait(97.225,103.606)
    $ speak(AMES, "Little things like a fast food order might not paint the whole picture of his support for you.")
    show jecka sc13:
        centerstage
        xzoom -1
    $ setWait(103.606,106.026)
    $ speak(JECKA, "You're saying he'd help get me out of it?")
    $ setWait(106.026,107.277)
    $ speak(AMES, "Possibly.")

    $ setWait(107.277,110.572)
    $ speak(JECKA, "Knowing his priorities he'd probably encourage it.")
    $ setWait(110.572,113.533)
    $ speak(AMES, "What would his priorities have to do with your dating life?")
    $ setWait(113.533,115.702)
    $ speak(JECKA, "He'd want me to stay with him so I pass History.")
    show ames 2 sad:
        rightmidstage

    $ setWait(115.702,116.369)
    $ speak(AMES, "I'm sorry?")
    show jecka sc13 surprised:
        centerstage
        xzoom -1

    $ setWait(116.369,117.037)
    $ speak(JECKA, "Oh uh!")
    $ setWait(117.037,120.123)
    $ speak(AMES, "What would your boyfriend have to do with your grade in History?")
    show jecka sc13 surprised:
        centerstage
        xzoom 1
        linear 0.4 leftcenterstage

    $ setWait(120.123,120.498)
    $ speak(JECKA, "Fuck!")
    show ames 2 angry:
        rightmidstage

    $ setWait(120.498,125.503)
    $ speak(AMES, "You're not dating a boy to sneak answers in class, are you? Cheating on tests can lead to expulsion.")
    show jecka sc13 sad:
        leftcenterstage
        xzoom -1
    $ setWait(125.503,128.631)
    $ speak(JECKA, "I'm dating the teacher!")
    show ames 2 sad:
        rightmidstage

    $ setWait(128.631,130.175)
    $ speak(AMES, "...What?")
    show jecka sc13 sad:
        leftcenterstage
        xzoom -1
        pause 2.6
        xzoom 1

    $ setWait(130.175,134.679)
    $ speak(JECKA, "I'm dating Mr. Katz so I don't fail History.")
    $ setWait(134.679,138.099)
    $ speak(AMES, "This is... probably not good.")
    show jecka sc13 angry:
        leftcenterstage
        xzoom -1
        linear 1 centerstage

    $ setWait(138.099,146.816)
    $ speak(JECKA, "Yeah but you can't tell anyone, right? Cause you can't interfere, cause this is my problem! That defeats the point of therapy, right??")
    $ setWait(146.816,148.109)
    $ speak(AMES, "Sure of course.")
    $ setWait(148.109,149.944)
    $ speak(JECKA, "You better not fuck my life up, bitch!")
    show ames 2 sad:
        rightmidstage


    $ setWait(149.944,151.821)
    $ speak(AMES, "I'm not here to hurt you.")
    $ setWait(151.821,157.035)
    $ speak(JECKA, "I have to keep dating him, cause if I don't he's gonna fail me, and if get him next year he's gonna fail me again!")



    $ setWait(157.035,162.248)
    $ speak(JECKA, "And if I get held back my GPA's gonna tank, then colleges aren't gonna want me, and my dad's gonna fucking hit me!")
    show jecka sc13 sad:
        centerstage
        xzoom -1
    $ setWait(162.248,173.051)
    $ speak(JECKA, "So I need to do this! I need to act like a little girl for some daddy fetish weirdo or I'm gonna end up a worthless whore on the side of the road!")
    $ setWait(173.051,176.513)
    $ speak(AMES, "I understand this can be.. very tough.")
    $ setWait(176.513,181.059)
    $ speak(JECKA, "What the fuck do you understand? About about any of this!?")
    show jecka sc13 angry:
        centerstage
        xzoom -1
        linear 0.8 leftcenterstage

    $ setWait(181.059,185.438)
    $ speak(JECKA, "After work you're just gonna go home and watch Ugly Betty or some other stupid shit!")
    show ames 2 sad:
        rightmidstage
        linear 1 rightcenterstage

    $ setWait(185.438,188.316)
    $ speak(AMES, "Okay we need to discuss our coping mechanisms--")
    show jecka sc13 angry:
        leftcenterstage
        xzoom -1
        linear 0.7 leftstage
    $ setWait(188.316,191.986)
    $ speak(JECKA, "Shut up I can cope just fine without you!")
    show jecka sc13 angry:
        leftstage
        xzoom 1
        linear 0.68 off_left

    $ setWait(191.986,193.53)
    $ speak(JECKA, "Fuck this place.")
    stop ambient fadeout 1.5

    jump scene_S0093

label scene_S0093:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0093.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 1
    show nicole sc9:
        xzoom -1
        leftcenterstage

    show megan sc1:
        leftstage
        linear 1.2 off_left

    $ setWait(0.039,2.417)
    $ speak(NICOLE, "Is Prozac short for Professional Zachary?")
    show jecka sc13 surprised:
        off_right
        linear 0.8 rightstage

    $ setWait(2.417,3.543)
    $ speak(JECKA, "Oh found you!")
    show nicole sc9:
        xzoom 1
        leftcenterstage

    $ setWait(3.543,4.46)
    $ speak(NICOLE, "What's up?")
    show jecka sc13 sad:
        rightstage
        linear 1 rightcenterstage
        pause 0.55
        xzoom -1
        pause 0.7
        xzoom 1

    $ setWait(4.46,9.048)
    $ speak(JECKA, "Yeah I just uh.. I need to hang out- -I wanna hang out.")
    $ setWait(9.048,11.551)
    $ speak(NICOLE, "Just in the middle of the main hallway?")
    show jecka sc13:
        rightcenterstage
        xzoom 1

    $ setWait(11.551,15.305)
    $ speak(JECKA, "Sure, we can talk. I just got out of some stupid meeting.")
    $ setWait(15.305,16.264)
    $ speak(NICOLE, "Were you in trouble?")
    show jecka sc13 sad:
        rightcenterstage

    $ setWait(16.264,19.017)
    $ speak(JECKA, "N-no it's probably fine.")

    show jecka sc13:
        rightcenterstage

    $ setWait(19.017,21.227)
    $ speak(JECKA, "But hey how was the concert last weekend?")
    $ setWait(21.227,22.312)
    $ speak(NICOLE, "Went as expected.")
    $ setWait(22.312,28.067)
    $ speak(JECKA, "Makes sense, so hey you wanna skip 4th period and buy cigarettes off that weird guy that hangs out in front of our school?")
    show nicole sc9 sad:
        leftcenterstage

    $ setWait(28.067,33.406)
    $ speak(NICOLE, "I would but I've just lost the will to do anything. And 4th period's one of my sleeping classes--")
    $ setWait(33.406,37.744)
    $ speak(JECKA, "Come on I can't go alone. We skip all the time together, what if he kidnaps me?")
    $ setWait(37.744,40.747)
    $ speak(NICOLE, "What am I gonna do? Use my tiny arms to rip you from his grasp?")
    show jecka sc13 angry:
        rightcenterstage

    $ setWait(40.747,41.873)
    $ speak(JECKA, "This is bullshit.")
    $ setWait(41.873,42.54)
    $ speak(NICOLE, "What?")
    $ setWait(42.54,47.837)
    $ speak(JECKA, "You blow all your time on these idiots you don't even like and now you can't even hang when it's someone you do like?")
    $ setWait(47.837,52.592)
    $ speak(NICOLE, "I know but like, I'm too far in, it's gonna be a nightmare if I tell everyone to fuck off now.")
    $ setWait(52.592,57.347)
    $ speak(JECKA, "You have a choice to make. It's either me or your hostage friendships. End of discussion.")
    $ setWait(57.347,61.434)
    $ speak(NICOLE, "Fuck.. well now I gotta think if I love you more than I hate being stalked.")
    show jecka sc13 angry:
        rightcenterstage
        pause 3.5
        xzoom -1
        linear 2.2 off_right

    $ setWait(61.434,66.189)
    $ speak(JECKA, "If you don't have an answer by 4th period, I'll have one for you. See ya, Nicole.")
    stop ambient fadeout 1.5
    jump scene_S0094

label scene_S0094:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0094.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 2

    show jecka sc13 sad:
        off_left
        xzoom -1
        linear 0.7 leftmidstage

    $ setWait(0.045,2.381)
    $ speak(JECKA, "Jesus Christ what the fuck is wrong with me?")

    show jecka sc13 sad:
        leftmidstage
        xzoom 1

    $ setWait(2.381,5.634)
    $ speak(JECKA, "She'll probably never talk to me again, what friends can I cope with now?")
    $ setWait(5.634,8.387)
    $ speak(JECKA, "I'm gonna end up one of those strangers on AIM.")
    show ames 2 sad:
        off_right
        linear 1 rightstage

    $ setWait(8.387,9.054)
    $ speak(AMES, "Jecka?")
    show jecka sc13 angry:
        leftmidstage
        xzoom -1

    $ setWait(9.054,10.305)
    $ speak(JECKA, "Oh god you again!")

    show ames 2 sad:
        rightstage
        linear 2.2 rightcenterstage

    $ setWait(10.305,14.518)
    $ speak(AMES, "No need to get upset, I just wanted to see how you were doing.")
    $ setWait(14.518,17.021)
    $ speak(JECKA, "Bitch you are not helping as much as you think you are.")
    $ setWait(17.021,21.316)
    $ speak(AMES, "It's in your best interest to come back and finish our talk, you shouldn't leave like that.")
    $ setWait(21.316,26.447)
    $ speak(JECKA, "Why so you can trick me into spilling my life more? I'm not some dumbass Ellen-watching bitch like you!")
    $ setWait(26.447,32.369)
    $ speak(AMES, "Let's not bring Ellen into this, you didn't do or say anything wrong.")

    show jecka sc13 sad:
        leftmidstage
        xzoom -1

    $ setWait(32.369,33.203)
    $ speak(JECKA, "...Really?")
    $ setWait(33.203,36.79)
    $ speak(AMES, "Yes really, now will you come with me?")
    show jecka sc13 sad:
        leftmidstage
        xzoom -1
        linear 1.5 leftcenterstage

    $ setWait(36.79,38.125)
    $ speak(JECKA, "I guess.")
    show ames 2:
        rightcenterstage

    $ setWait(38.125,40.335)
    $ speak(AMES, "Good, okay...")
    $ setWait(40.335,42.546)
    $ speak(AMES, "Now there's someone I need you to speak with.")
    show jecka sc13 surprised:
        leftcenterstage
        xzoom -1
    $ setWait(42.546,43.047)
    $ speak(JECKA, "What??")
    show cop:
        off_right
        linear 1 rightstage

    $ setWait(43.047,43.714)
    $ speak(COP, "Is this her?")
    show jecka sc13 sad:
        leftcenterstage
        xzoom -1
        linear 0.7 leftmidstage

    $ setWait(43.714,45.215)
    $ speak(JECKA, "What the fuck you told someone!?")
    show ames 2 sad:
        rightcenterstage

    $ setWait(45.215,49.511)
    $ speak(AMES, "You're not in trouble, the officer just has to file a report--")
    show jecka sc13 angry:
        leftmidstage
        xzoom -1

    $ setWait(49.511,51.764)
    $ speak(JECKA, "No! No this ruins everything!!")
    $ setWait(51.764,53.974)
    $ speak(COP, "We need to talk about Mr. Katz.")
    show jecka sc13 sad:
        leftmidstage
        xzoom -1

    $ setWait(53.974,55.726)
    $ speak(JECKA, "You said you wouldn't tell anybody!")
    show ames 2 sad:
        rightcenterstage
        linear 1 centerstage
    $ setWait(55.726,56.852)
    $ speak(AMES, "I had to.")
    show jecka sc13 angry:
        leftmidstage
        xzoom -1

    $ setWait(56.852,60.564)
    $ speak(JECKA, "Yeah I guess you had to fuck my future up too! Now I'm never passing that class!")


    $ setWait(60.564,63.108)
    $ speak(COP, "Why don't you come with us back into the counseling room.")
    show jecka sc13 angry:
        leftmidstage
        xzoom 1
        linear 0.55 off_left
    $ setWait(63.108,64.651)
    $ speak(JECKA, "I'm not telling you shit!")
    show ames 2 sad:
        centerstage
        linear 0.4 leftcenterstage
    $ setWait(64.651,67.196)
    $ speak(AMES, "Jecka!")
    show cop:
        rightstage
        linear 0.6 rightmidstage

    show ames 2 sad:
        leftcenterstage
        pause 0.5
        xzoom -1

    $ setWait(67.196,68.864)
    $ speak(COP, "Can I go back to my car now?")
    stop ambient fadeout 1.5

    jump scene_S0095

label scene_S0095:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1.2
    scene onlayer master
    show black
    show house jecka day with Pause(2.293):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.293 zoom 0.55 truecenter
    $ setVoiceTrack("audio/Scenes/0095.mp3")
    play ambient "audio/Ambience/House_Ambience_2.mp3"
    scene livingroom jecka
    show jecka sc13 sad:
        off_left
        xzoom -1
        linear 1 leftcenterstage

    $ setWait(2.293,4.212)
    $ speak(JECKA, "Thank god they're not home.")
    show jecka sc13 sad:
        leftcenterstage
        xzoom 1
    $ setWait(4.212,9.133)
    $ speak(JECKA, "I gotta... I gotta just tell 'em before they do. Then they're the liars cause he heard it from me first!")
    $ setWait(9.133,14.889)
    $ speak(JECKA, "Okay \"Dad... Someone spread a rumor about me at school and...\"")
    show jecka sc13 angry:
        leftcenterstage
        xzoom 1

    $ setWait(14.889,16.182)
    $ speak(JECKA, "Fuck what would come after that??")
    show dad polo angry:
        off_right
        linear 1 rightstage

    show jecka sc13 surprised:
        leftcenterstage
        pause 0.4
        xzoom -1

    $ setWait(16.182,17.725)
    $ speak(DAD, "What the hell are you doing here!?")

    $ setWait(17.725,20.77)
    $ speak(JECKA, "Oh, Dad! Why're you home so early?")
    $ setWait(20.77,23.94)
    $ speak(DAD, "The unbelievable phone call I just got!")
    show jecka sc13 sad:
        leftcenterstage
        xzoom -1
    $ setWait(23.94,27.735)
    $ speak(JECKA, "U-Unbelievable's right, these rumors they start at school--")
    show dad polo yell:
        rightstage

    $ setWait(27.735,31.823)
    $ speak(DAD, "Shut the fuck up! I should've known you weren't actually working harder!")
    show dad polo angry:
        rightstage

    show jecka sc13 angry:
        leftcenterstage
        xzoom -1

    $ setWait(31.823,32.657)
    $ speak(JECKA, "Yeah I was!")
    show dad polo yell:
        rightstage
        linear 0.7 rightcenterstage

    $ setWait(32.657,35.66)
    $ speak(DAD, "Your principal said you fucked your history teacher!")
    show jecka sc13 surprised:
        leftcenterstage
        xzoom -1

    $ setWait(35.66,36.619)
    $ speak(JECKA, "Wh-what??")
    show dad polo angry:
        rightcenterstage

    $ setWait(36.619,39.08)
    $ speak(DAD, "Is this true!?")
    show jecka sc13 sad:
        leftcenterstage
        xzoom -1

    $ setWait(39.08,40.665)
    $ speak(JECKA, "...I didn't fuck him fuck him!")

    show dad polo yell:
        rightcenterstage
        xzoom -1
        linear 0.6 rightmidstage
        pause 0.85
        xzoom 1

    $ setWait(40.665,44.919)
    $ speak(DAD, "Oh my god you're a whore!! I'm gonna beat the shit out of you!")
    show dad polo angry:
        rightmidstage
        xzoom -1
        linear 1 off_right

    $ setWait(44.919,46.379)
    $ speak(DAD, "Where's the fire poker!?")
    $ setWait(46.379,48.464)
    $ speak(JECKA, "Fuck I gotta hide somewhere uh...")
    show jecka sc13 sad:
        leftcenterstage
        xzoom 1

    $ setWait(48.464,49.799)
    $ speak(JECKA, "Would Nicole be home right now?")
    show jecka sc13 sad:
        leftcenterstage
        linear 1 off_left

    $ setWait(49.799,52.552)
    $ speak(JECKA, "Yeah she skips all the time, of course.")
    stop ambient fadeout 1.5
    jump scene_S0096

label scene_S0096:
    show black onlayer screens with Pause(3.3):
        alpha 0.0
        linear 2.2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.8 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1.2
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.458):
        zoom 0.75 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.458 zoom 0.8 truecenter
    $ setVoiceTrack("audio/Scenes/0096.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    show black onlayer screens:
        alpha 0.16
    scene home nicole int dark
    show jecka sc13 sad:
        off_right
        linear 2 rightmidstage

    $ setWait(2.458,5.294)
    $ speak(JECKA, "Is seriously no one home?")
    show jecka sc13 sad:
        rightmidstage
        linear 1.7 rightcenterstage

    $ setWait(5.294,8.255)
    $ speak(JECKA, "Hello!?")
    show jecka sc13:
        rightcenterstage
        linear 2 leftstage

    show black onlayer screens:
        alpha .15
        pause 1.1
        linear 1 alpha 1.0

    $ setWait(8.255,10.507)
    $ speak(JECKA, "Maybe her headphones are really loud.")
    hide jecka sc13
    scene black
    $ csbox = True
    $ setWait(10.507,15.554)
    $ speak(JECKA, "...")
    scene cut0096a
    show black onlayer screens:
        alpha 1
        linear 1 alpha 0.0

    $ setWait(15.554,19.725)
    $ speak(JECKA, "Why's it so quiet? Don't tell me she's still at school.")
    show black onlayer screens:
        alpha 0.0

    scene cut0096b

    $ setWait(19.725,21.852)
    $ speak(JECKA, "...")
    $ setWait(21.852,24.021)
    $ speak(JECKA, "Nicole?")
    show cut0096c:
        zoom 0.9 truecenter
        linear 0.2 zoom 0.5 truecenter

    $ setWait(24.021,25.814)
    $ speak(JECKA, "What the fuck!?")
    hide cut0096c
    scene cut0096d
    $ setWait(25.814,28.442)
    $ speak(JECKA, "She didn't-- ...No.")
    scene cut0096e
    $ setWait(28.442,29.776)
    $ speak(JECKA, "...")
    $ setWait(29.776,31.403)
    $ speak(JECKA, "Oh my god she left a note...")
    scene cut0096f
    $ setWait(31.403,33.071)
    $ speak(JECKA, "...")
    $ setWait(33.071,35.991)
    $ speak(JECKA, "\"Books puzzles and pawns\"...")
    $ setWait(35.991,38.994)
    $ speak(JECKA, "\"Don't be mean, don't judge\"...")
    $ setWait(38.994,41.163)
    $ speak(JECKA, "Her Mom did this??")
    $ setWait(41.163,43.749)
    $ speak(JECKA, "That's why she was hanging out with those idiots!")
    show cut0096g:
        zoom 0.59 truecenter
        linear 15 zoom 0.5 truecenter


    $ setWait(43.749,47.711)
    $ speak(JECKA, "...")
    stop ambient fadeout 15
    show black onlayer screens:
        alpha 0.0
        pause 7
        linear 4 alpha 1.0

    $ setWait(47.711,58.466)
    $ speak(JECKA, "What do I do now?")

    jump scene_S0097

label scene_S0097:
    show black onlayer screens with Pause(4):
        alpha 1.0
        linear 1.3 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 2.2 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1.2
    scene onlayer master
    show title_onemonthlater onlayer screens
    show black

    show school front with Pause(3.381):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 3.381 zoom 1.05 truecenter



    $ setVoiceTrack("audio/Scenes/0097.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3"
    $ csbox = False
    hide title_onemonthlater onlayer screens
    scene office 1

    show jecka sc10:
        centerstage
        xzoom -1

    show ames 1:
        rightmidstage

    $ setWait(3.381,6.634)
    $ speak(AMES, "And you did the assignment?")
    $ setWait(6.634,8.803)
    $ speak(JECKA, "Well yeah.")
    $ setWait(8.803,11.931)
    $ speak(AMES, "So why didn't you submit it on time?")
    $ setWait(11.931,14.976)
    $ speak(JECKA, "Cause Blackboard sucks actual fucking dick.")
    $ setWait(14.976,19.689)
    $ speak(AMES, "Shouldn't you clarify with your teacher that you're having technical problems before the deadline?")
    show jecka sc10 angry:
        centerstage
        xzoom -1

    $ setWait(19.689,22.733)
    $ speak(JECKA, "Shouldn't they make sure it works before they make us use it??")
    $ setWait(22.733,31.2)
    $ speak(AMES, "As a few teachers described it to me, they're having you use the online platforms since colleges will be very digital by the time you get there.")
    show jecka sc10:
        centerstage
        xzoom -1

    $ setWait(31.2,35.079)
    $ speak(JECKA, "I can just worry about it then.. If I even make it there.")
    $ setWait(35.079,38.499)
    $ speak(AMES, "I'm sure the grading with your new History teacher will be fair.")
    $ setWait(38.499,40.334)
    $ speak(JECKA, "That's what you think.")
    $ setWait(40.334,44.463)
    $ speak(AMES, "Other than that, how's it going with your new classmates?")
    $ setWait(44.463,46.632)
    $ speak(JECKA, "Same as the old ones.")
    $ setWait(46.632,48.426)
    $ speak(AMES, "Is that good?")
    $ setWait(48.426,51.137)
    $ speak(JECKA, "Was it ever?")
    $ setWait(51.137,54.223)
    $ speak(AMES, "Do you experience problems making new friends?")
    show jecka sc10 angry:
        centerstage
        xzoom -1
    $ setWait(54.223,58.06)
    $ speak(JECKA, "Did you really just ask me if I replaced my dead friend yet?")
    $ setWait(58.06,59.687)
    $ speak(AMES, "Do you think you could replace her?")
    $ setWait(59.687,62.606)
    $ speak(JECKA, "You're making a terrible case for women in the workplace right now.")
    show ames 1 sad:
        rightmidstage


    $ setWait(62.606,70.114)
    $ speak(AMES, "It wasn't just a turbulent day for you. The entire school was upside down with multiple problematic events.")
    show ames 1:
        rightmidstage

    $ setWait(70.114,73.784)
    $ speak(AMES, "But as they say... Life goes on.")
    show jecka sc10:
        centerstage
        xzoom -1

    $ setWait(73.784,75.286)
    $ speak(JECKA, "For who?")
    $ setWait(75.286,76.704)
    $ speak(AMES, "Everyone.")
    $ setWait(76.704,79.04)
    $ speak(JECKA, "Everyone else.")
    $ setWait(79.04,81.459)
    $ speak(AMES, "Her passing was very difficult for you?")
    show jecka sc10 angry:
        centerstage
        xzoom -1
    $ setWait(81.459,84.295)
    $ speak(JECKA, "What the fuck do you think?")
    $ setWait(84.295,93.22)
    $ speak(AMES, "It might be tricky to see it this way now but certain tragedies don't affect everyone else the way they affect you.")
    $ setWait(93.22,99.477)
    $ speak(JECKA, "So is this therapy session for everyone else or me? Call everybody in, ask them some rhetorical questions for a salary.")

    $ setWait(99.477,111.906)
    $ speak(AMES, "What I mean is the world revolves everyday whether you're sad or happy. Our goal here is to make sure you're happy enough to keep up with the world.")
    $ setWait(111.906,115.034)
    $ speak(JECKA, "I don't wanna be happy in a world that doesn't give a shit about me.")
    show ames 1 sad:
        rightmidstage

    $ setWait(115.034,117.286)
    $ speak(AMES, "Plenty of people care about you.")
    show jecka sc10:
        centerstage
        xzoom -1

    $ setWait(117.286,122.75)
    $ speak(JECKA, "Did my math teacher give a shit when Nicole killed herself? Or what about the guys asking me out the day after?")
    $ setWait(122.75,127.296)
    $ speak(JECKA, "2 or 3 people cared about Nicole, tops. That's not plenty.")
    $ setWait(127.296,131.008)
    $ speak(JECKA, "No one really cares about me now, learned that the hard way.")
    show ames 1:
        rightmidstage
    $ setWait(131.008,132.259)
    $ speak(AMES, "How do you know?")
    $ setWait(132.259,137.264)
    $ speak(JECKA, "I got molested by my teacher, my friend killed herself, and guess what changed?")

    show jecka sc10 angry:
        centerstage
        xzoom -1

    $ setWait(137.264,139.642)
    $ speak(JECKA, "Absolutely nothing.")
    $ setWait(139.642,147.942)
    $ speak(JECKA, "Flowers and Target gift cards for a week and everything's back to normal. Everyone's back to not caring.")
    show jecka sc10:
        centerstage
        xzoom -1
    $ setWait(147.942,154.406)
    $ speak(JECKA, "No one cares about me cause no one considers how my life's gonna be different forever.")
    show ames 1 smile:
        rightmidstage
    $ setWait(154.406,156.492)
    $ speak(AMES, "It won't be different forever.")
    stop ambient fadeout 3.3
    show black onlayer screens:
        alpha 0.0
        pause 2
        linear 4 alpha 1.0

    $ setWait(156.492,162.994)
    $ speak(JECKA, "Exactly...")

    scene black

    jump scene_S0098

label scene_S0098:

    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    if "end_0098" not in persistent.endings:
        $ persistent.endings.append("end_0098")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    return

label scene_S0997:

    scene onlayer master
    show black

    $ renpy.music.set_pause(True)
    $ quick_menu = False
    $ csbox = True

    $ renpy.movie_cutscene("secret_a.webm")
    $ renpy.music.set_pause(False)

    return

label scene_S0998:

    scene onlayer master
    show black

    $ renpy.music.set_pause(True)
    $ quick_menu = False
    $ csbox = True

    $ renpy.movie_cutscene("secret_b.webm")
    $ renpy.music.set_pause(False)

    return

label scene_S0999:

    scene onlayer master
    show black

    $ renpy.music.set_pause(True)
    $ quick_menu = False
    $ csbox = True

    $ renpy.movie_cutscene("secret_c.webm")
    $ renpy.music.set_pause(False)
    $ persistent.seen_last_video_message = True

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

# The script of the game goes in this file.

####################################################################################
# Audio
# 
# Declare and confiugre audio tracks used by this game.
####################################################################################

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

define config.sample_sound = "sfx_paperflip.mp3"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
define config.main_menu_music_fadein = 1.0 #Song fades in

####################################################################################
# Character Config
# 
# Declare characters used by this game.
# The color argument colorizes the name of the character.
# Organized by order of appearance.
####################################################################################

define alex = Character('Alex', color="#000000", what_color="#000000", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf", window_background="gui/textbox.png")#, callback=writingAlex)

define claudiaUnknown = Character('???', color="#000000", what_color="#000000", who_font="fonts/claudia_font.ttf", what_font="fonts/claudia_font.ttf", window_background="gui/textbox.png")#, callback=writingClaudia)

define claudia = Character('Claudia', color="#000000", what_color="#000000", who_font="fonts/claudia_font.ttf", what_font="fonts/claudia_font.ttf", window_background="gui/textbox.png")#, callback=writingClaudia)

define tsukuneUnknown = Character('???', color="#000000", what_color="#000000", who_font="fonts/tsukune_font.ttf", what_font="fonts/tsukune_font.ttf", window_background="gui/textbox.png")#, callback=writingTsukune)

define tsukune = Character('Tsukune', color="#000000", what_color="#000000", who_font="fonts/tsukune_font.ttf", what_font="fonts/tsukune_font.ttf", window_background="gui/textbox.png")#, callback=writingTsukune)

define witness = Character('Witness', color="#000000", what_color="#000000")

####################################################################################
# Variables
# 
# Relevant variables used by this game.
####################################################################################

## Persistent Data
    #$ persistent.journal_unlock
        ## True: Enable "journal" button in quick_menu
        ## False: Hide "journal" button in quick_menu

    #$ persistent.quick_menu_display
        ## True: Displays all quick_menu buttons
        ## False: Hides all quick_menu buttons

## Journal Notes
    ## Tsukune
        #$ persistent.tsukuneNotes_cigaretteAddiction = True
    ## Claudia
        #$ persistent.claudiaNotes_athletic = True
        #$ persistent.claudiaNotes_barista = True

## Route Variables
    #$ persistent.alexChoice_therapy
        ## Alex chooses to go to therapy

## Relationship Bar
    #$ loveMeter=True
        ## Show love bars
    #$ loveMeter=False
        ## Hide love bars

    #$ lovePoints_Claudia+=10
        ## Increase Claudia's love points
    #$ lovePoints_Tsukune-=10
        ## Decrease Tsukune's love points
init python:
    max_love=100
    lovePoints_Claudia=0
    lovePoints_Tsukune=25
    loveMeter=False
   
    def stats_overlay():
        if loveMeter:
            ui.frame()
            ui.vbox()
            ui.text("Claudia")
            ui.bar(max_love,lovePoints_Claudia, xmaximum=1500)

            ui.text("Tsukune")
            ui.bar(max_love,lovePoints_tsukune, xmaximum=1500)

            ui.close()

    config.overlay_functions.append(stats_overlay)


define config.window_auto_hide = [ "scene", "menu", "hide", "show" ]

init python:
    config.overlay_screens.append("quick_menu")

# The game starts here.

label start:

    jump chapter_0_start
# The script of the game goes in this file.

init offset = -1


###############################################################
## Typewriting Effect
###############################################################

# Declare characters used by this game. The color argument colorizes the
# name of the character.

##pick between one of the two and add an # to the other to keep it

## Journal SFX
define alexJournalSounds = ['sfx/Key.ogg']

## Dialogue SFX
define tsukuneWritingSounds = ['sfx/swipe.ogg']
define claudiaWritingSounds = ['sfx/paper-flip.ogg']
define alexWritingSounds = ['sfx/Coin.ogg']

##regular taps, medium intervals
    #define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

##light taps, smaller intervals
    #define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

##both combined
    #define sounds = ['sfx/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def journalAlex(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            renpy.sound.queue(renpy.random.choice(alexJournalSounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def writingTsukune(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            renpy.sound.queue(renpy.random.choice(tsukuneWritingSounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def writingAlex(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            renpy.sound.queue(renpy.random.choice(alexWritingSounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def writingClaudia(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            renpy.sound.queue(renpy.random.choice(claudiaWritingSounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

## Click To Continue
## Button that fades in and out to indicate the player needs to click to progress.

#image ctc_arrow:
#    "gui/button/right_arrow.png"
#    yalign 0.98 xalign 0.99
#    linear 0.3 alpha 1.0
#    pause 2.0
#    linear 0.3 alpha 0.0
#    pause 0.2
#    repeat


define config.window_auto_hide = [ "scene", "menu", "hide", "show" ]

#######################################################################
## Quick Menu
#######################################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
##
## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.

init python:
    config.overlay_screens.append("quick_menu")

#######################################################################
## Love Meter
#######################################################################
## Relationship levels in visual form

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

    ######################################
    ## In-Game Use Example
    ######################################

    #$ loveMeter=True
        ## Show love bars
    #$ loveMeter=False
        ## Hide love bars

    #$ lovePoints_Claudia+=10
        ## Increase Claudia's love points
    #$ lovePoints_Tsukune-=10
        ## Decrease Tsukune's love points

#######################################################################
## GAME START
#######################################################################

label start:
    stop music fadeout 1.0

    window auto
    
    $ persistent.quick_menu_display = False

    jump chapter_0_start
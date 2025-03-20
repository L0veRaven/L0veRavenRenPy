init python:
    ## Music List ##################################################################
    music_title = "audio/music/blurred.mp3" #Plays on title screen

    ## Sound Effect List ###########################################################
    sfx_paperflip = "audio/sfx/paper_flip.mp3" #Paper flip sound effect

## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

define config.sample_sound = sfx_paperflip
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
define config.main_menu_music = music_title
define config.main_menu_music_fadein = 1.0 #Song fades in
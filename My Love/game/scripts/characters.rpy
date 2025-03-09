############################################################################################################################################################
## Characters ##############################################################################################################################################
##
## Declares characters used
    ## 'color' colorizes character text
    ## 'who_font' chooses font for character name
    ## 'what_font' chooses font for character dialogue
    ## 'kind' usually ' = nvl' to have character function in nvl format

define claudia = Character('Claudia', color="#000000")

define tsukune = Character('Tsukune', color="#000000")

define witness = Character('Witness', color="#000000")

define you = Character('You', color="#000000", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf")

define journal = Character(None, kind=nvl, color="#000000", ctc="ctc_arrow", ctc_position="fixed", ctc_pause="ctc_arrow", ctc_timedpause="ctc_arrow")

define disclaimerText = Character(None, kind=nvl, color="#a0a0a0", what_text_align=0.5)

############################################################################################################################################################


##################################
## Transition Variables ##########
##

define fade = Fade(0.5, 2.0, 0.5)

##################################


###############################################
## Persistent Variables #######################
##

#$ persistent.journal_unlock
    ## Enables "journal" button in quick_menu

#$ persistent.cutscene_off
    ## True: Displays all quick_menu buttons
    ## False: Hides all quick_menu buttons

###############################################
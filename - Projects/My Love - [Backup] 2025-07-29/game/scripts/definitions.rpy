## Transitions

#define fade = Fade(0.5, 2.0, 0.5)

## Persistent Variables
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
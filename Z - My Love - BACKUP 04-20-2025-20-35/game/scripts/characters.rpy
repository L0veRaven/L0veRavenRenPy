## Declares characters used
    ## 'None' [without ''] prevents a name from being displayed with the dialogue
    ## '<>' [without <>] allows input for the Character's name to be displayed when they speak

    ## 'color' colorizes character name
    ## 'what_color' colorizes character dialogue

    ## 'who_font' chooses font for character name
    ## 'what_font' chooses font for character dialogue

    ## 'kind' usually ' = nvl' to have character function in nvl format

define claudia = Character('Claudia', color="#884625", what_color="#884625", who_font="fonts/claudia_font.ttf", what_font="fonts/claudia_font.ttf")

define tsukune = Character('Tsukune', color="#0c357d", what_color="#0c357d", who_font="fonts/tsukune_font.ttf", what_font="fonts/tsukune_font.ttf")

define witness = Character('Witness', color="#000000")

define alex = Character('Alex', color="#000000", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf")

define alexJournal = Character(None, kind=nvl, color="#000000", ctc="ctc_arrow", ctc_position="fixed", ctc_pause="ctc_arrow", ctc_timedpause="ctc_arrow")
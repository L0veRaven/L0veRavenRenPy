## Declares characters used
    ## 'None' [without ''] prevents a name from being displayed with the dialogue
    ## '<>' [without <>] allows input for the Character's name to be displayed when they speak

    ## 'color' colorizes character name
    ## 'what_color' colorizes character dialogue

    ## 'who_font' chooses font for character name
    ## 'what_font' chooses font for character dialogue

    ## 'kind' usually ' = nvl' to have character function in nvl format

## Speaking Characters

define claudia = Character('Claudia', color="#884625", what_color="#884625", who_font="fonts/claudia_font.ttf", what_font="fonts/claudia_font.ttf")#, callback=writingClaudia)

define claudiaUnknown = Character('???', color="#884625", what_color="#884625", who_font="fonts/claudia_font.ttf", what_font="fonts/claudia_font.ttf")#, callback=writingClaudia)

define tsukune = Character('Tsukune', color="#0c357d", what_color="#0c357d", who_font="fonts/tsukune_font.ttf", what_font="fonts/tsukune_font.ttf")#, callback=writingTsukune)

define tsukuneUnknown = Character('???', color="#0c357d", what_color="#0c357d", who_font="fonts/tsukune_font.ttf", what_font="fonts/tsukune_font.ttf")#, callback=writingTsukune)

define alex = Character('Alex', color="#000000", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf")#, callback=writingAlex)

define witness = Character('Witness', color="#7a2d7d")

## Journal Characters

define alexJournal = Character(None, kind=nvl, color="#000000", what_color="#000000", what_font="fonts/you_font.ttf")#, callback=journalAlex)
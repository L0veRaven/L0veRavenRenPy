## Declares characters used
    ## 'None' [without ''] prevents a name from being displayed with the dialogue
    ## '<>' [without <>] allows input for the Character's name to be displayed when they speak

    ## 'color' colorizes character name
    ## 'what_color' colorizes character dialogue

    ## 'who_font' chooses font for character name
    ## 'what_font' chooses font for character dialogue

    ## 'kind' usually ' = nvl' to have character function in nvl format

## Speaking Characters

define claudia = Character('Claudia', color="#ffffff", what_color="#ffffff", who_font="fonts/claudia_font.ttf", what_font="fonts/claudia_font.ttf")#, callback=writingClaudia)

define claudiaUnknown = Character('???', color="#ffffff", what_color="#ffffff", who_font="fonts/claudia_font.ttf", what_font="fonts/claudia_font.ttf")#, callback=writingClaudia)

define tsukune = Character('Tsukune', color="#ffffff", what_color="#ffffff", who_font="fonts/tsukune_font.ttf", what_font="fonts/tsukune_font.ttf")#, callback=writingTsukune)

define tsukuneUnknown = Character('???', color="#ffffff", what_color="#ffffff", who_font="fonts/tsukune_font.ttf", what_font="fonts/tsukune_font.ttf")#, callback=writingTsukune)

define alex = Character('Alex', color="#ffffff", what_color="#ffffff", who_font="fonts/you_font.ttf", what_font="fonts/you_font.ttf")#, callback=writingAlex)

define witness = Character('Witness', color="#ffffff", what_color="#ffffff")

## Journal Characters

define alexJournal = Character(None, kind=nvl, color="#000000", what_color="#000000", what_font="fonts/you_font.ttf")#, callback=journalAlex)
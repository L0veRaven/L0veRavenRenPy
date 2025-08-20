## The bookmarks navigate the different journal pages

screen journalBookmarks():
    hbox:
        xalign 0.5
        yanchor 0.0
        ypos 10
        imagebutton:
            auto "gui/button/journalTabs/redTab_%s.png"
            focus_mask True
            action ShowMenu('claudiaPage')
            
        imagebutton:
            auto "gui/button/journalTabs/orangeTab_%s.png"
            focus_mask True
            action ShowMenu('tsukunePage')
            
        imagebutton:
            auto "gui/button/journalTabs/yellowTab_%s.png"
            focus_mask True
            action ShowMenu('imageGallery')
            
        imagebutton:
            auto "gui/button/journalTabs/greenTab_%s.png"
            focus_mask True
            action ShowMenu('preferences')
            
        imagebutton:
            auto "gui/button/journalTabs/blueTab_%s.png"
            focus_mask True
            action Return()

## All the journal's layers

screen journalBook():
    image "gui/overlay/gameMenu_journalBase.png"

    use journalBookmarks

    image "gui/overlay/gameMenu_journalPaper.png"
    image "gui/overlay/gameMenu_journalRings.png"

default lovePoints_Claudia = 0
default lovePoints_Tsukune = 25

default currentObjective = "Check my journal."

screen journalMenu():
    style_prefix "journal_menu"

    use journalBook

    tag menu

    vbox:
        xalign 0.5
        yanchor 0.0
        ypos 150


        text _("Stats"):
            xalign 0.5
        
        text _("\n{u}Love Points{/u}\n"):
            xalign 0.5
        
        text _("Claudia: [lovePoints_Claudia]\n"):
            xalign 0.5
        text _("Tsukune: [lovePoints_Tsukune]"):
            xalign 0.5

        text _("\n\n{u}Current Objective{/u}\n")
        text _([currentObjective])
        
        if persistent.tsukuneDrive_end == True:
            text _("Get some rest."):
                xpos 0.5

        if (lovePoints_Claudia > 100):
            text _("Ask Claudia on a date.")
            
        if (lovePoints_Tsukune > 100):
            text _("Ask Tsukune on a date.")

    
screen claudiaPage():
    style_prefix "journal_menu"

    use journalBook

    tag menu

    vbox:
        xalign 0.5

        text _("Claudia Notes\n\n"):
            xalign 0.5
            ypos 150

        text _("{u}Notes of Interest{/u}\n"):
            xalign 0.5
            ypos 105


    
screen tsukunePage():
    style_prefix "journal_menu"

    use journalBook

    tag menu

    vbox:
        xalign 0.5

        text _("Tsukune Notes\n\n"):
            xalign 0.5
            ypos 150

        vbox:
            ypos 105

            text _("{u}Notes of Interest{/u}"):
                xalign 0.5
            
            if (persistent.tsukuneNotes_cigaretteAddiction == True):
                text _("\nCigarrete addiction"):
                    xalign 0.5
    
screen imageGallery():
    style_prefix "journal_menu"

    use journalBook

    tag menu

    text _("Image Gallery"):
        xalign 0.5
        ypos 150
screen journalMenu():
    style_prefix "journal_menu"

    image "gui/overlay/gameMenu_journal.png"

    tag menu

    text _("Notes"):
        xalign 0.5
        ypos 150

    textbutton _("Return"):
        action Return()
        xalign 0.5
        yalign 0.94
label c0_alexApartment_livingRoom:
    scene bg_alex_apartment_living_room with Dissolve(2.0)

    $ persistent.journal_unlock = True
    "Well then... I guess that's all I'm gonna learn for now. Actually, I need to check my notes!\n\n(To check your notes, click on the journal icon.)"

    stop music fadeout 3.0

    #########################
    ## In Apartment
    #########################

    jump c1_start
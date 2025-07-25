## [Answer 1b] Happy for Tsukune
label chapter_0_tsukuneTherapy_b:
    $ lovePoints_Tsukune+=15
    alex "That sounds great! It can be pretty difficult for people to start therapy."
    
    tsukune "It really can! I only finally started therapy once I noticed I was going to relapse on smoking cigarettes again."
    
    $ renpy.notify("You have information about Tsukune.")
    $ persistent.tsukuneNotes_cigaretteAddiction = True
    alex "You used to smoke?"

    tsukune "Yup, but I quit before I started working at this company. It honestly sucks to have people side-eyeing you and talking shit for having an addiction."

    alex "Were your old coworkers mad about it?"

    tsukune "They really were, but they thought I couldn't hear them. They always changed topics when I made my presence known during those conversations."

    alex "That must really suck. At least you're not dealing with that here, right?"

    tsukune "Exactly, it's why I really like working here."

    jump chapter_0_tsukuneDrive_end
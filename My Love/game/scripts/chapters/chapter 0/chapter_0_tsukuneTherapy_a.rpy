## [Answer 1a] Therapy is bullshit
label drive_conversation_tsukuneTherapy_a:
    alex "I don't see the point in therapy. I doesn't even {i}{b}really{/b}{/i} help you."

    tsukune "What do you mean?"

    alex "Therapists basically have {i}{b}you{/b}{/i} try to figure everything out by yourself?"

    tsukune "Not exactly. At least for me, my therapist offers suggestions, but ultimately leaves decisions up to me."

    alex "That's my point."

    tsukune "Well, it {i}{b}is{/b}{/i} my life, so she can't make me do anything, even if she wanted to."

    alex "So therapy is where you go to get suggestions?"

    tsukune "She also walks me through different coping skills. It's much better than me smoking cigarettes like before."

    $ renpy.notify("You have information about Tsukune.")
    $ persistent.tsukuneNotes_cigaretteAddiction = True
    alex "She helped you quit smoking?"

    tsukune "No, I quit before I started getting therapy. If anything, therapy is helping me stay away from cigarettes."

    alex "Really?"

    tsukune "It might be hard to believe, but learning how to manage my stress and triggers makes me less likely to want to smoke. Cigarettes honestly made my issues worse."

    alex "I guess therapy {i}{b}is{/b}{/i} pretty helpful after all."

    tsukune "It really is, for me at least."

    jump chapter_0_conversation_ClaudiaApartments
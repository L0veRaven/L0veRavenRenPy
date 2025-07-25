## [Answer 1c] Alex needs therapy
label c0_tsukuneTherapy_c:
    alex "I know this is kind of weird to ask, but do you think {i}{b}I{/b}{/i} need therapy?"
    
    tsukune "Well, I don't think it's my place to say. Even though {i}{b}I{/b}{/i} think everyone would benefit from seeing a therapist, that doesn't mean it'll work for everyone."

    alex "I guess you're right... If you don't mind me asking, why did you decide to see a therapist?"

    tsukune "Oh, well my reason was because I was getting close to relapsing on smoking cigarettes. I used to smoke four per day!"
    
    $ renpy.notify("You have information about Tsukune.")
    $ persistent.tsukuneNotes_cigaretteAddiction = True
    alex "... Four packs a day?!"

    tsukune "Woah, not {i}{b}that{/b}{/i} many. Just four cigarettes per day."

    alex "Is that a lot?"

    tsukune "Any amount of cigarettes is too much, realistically."

    alex "That's a good point. I think I could qualify for therapy. I know that I have depression, but I'm not sure how a therapist would fix that."

    tsukune "Well, it's not the therapist's job to fix your problems necessarily. They provide you with the tools to heal yourself emotionally and work through your issues."

    alex "It sounds like I'd be doing all the work, right?"

    tsukune "They help you through the process, so you're not just raw dogging everything."

    $ persistent.alexChoice_therapy
    alex "I'll consider it. I just hope it doesn't change my schedule too much."

    tsukune "I think you should do therapy when you feel ready for it. It only works if you {i}{b}really{/b}{/i} want the help."

    jump c0_tsukuneDrive_end
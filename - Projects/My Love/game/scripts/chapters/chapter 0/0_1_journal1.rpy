label c0_journal1:
    scene black with Dissolve(2.0)
    pause 2.0
    scene bg_alex_apartment_living_room with Dissolve(2.0)
    pause (2.0)
    $ persistent.quick_menu_display = True
    
    play sound scribble
    alexJournal "June 12, 2023 - Monday @ 7:05 AM"

    play sound scribble
    alexJournal "I slept like usual, another nightmare. The thing is that I can't remember what the nightmare even was. All I can recall is me waking up feeling afraid with sweat all over me. I hate waking up that way almost every morning. Hopefully the nightmares settle down one of these days."
    
    play sound scribble
    alexJournal "Other than that, I'm really liking doing these journal entries. Sure, it's weird to feel like you're talking to a wall at first, but there's something therapeutic about it. It's like someone is letting you vent to them for as long as you're willing to keep writing with a pen. It's nice to feel listened to, even if it's just a little journal holding all my thoughts together."
    
    play sound scribble
    alexJournal "There is something that I recently realized that I'm struggling with. I didn't realize that I was feeling {sc=3}l o n e l y{/sc} for as long as I have. I thought I was just uncomfortable about being alone for too long at a time, but I'm also horrible at reaching out to people. I'd like to stay on top of talking with people, but it just ends up slipping my mind. I forget to talk to people until it's been so long that it'd feel out of place for me to reach out to them."

    nvl clear
    
    play sound scribble
    alexJournal "In fact, I actually noticed that I'm starting to learn to identify my emotions better after journaling for the past month. I make it a point to ask myself, \"What am I feeling?\" when I write these entries because it's more than just venting about my problems. If I know what I'm feeling, then it makes it easier to learn how to manage my emotions better. I guess re-learning emotions is common after suppressing my emotions for so many years..."

    nvl clear
    pause 1.0
    #play sound "muffled speech"
    #play sound "noise"
    play sound carDoorClose
    pause 2.0

    stop music

    alex "{i}It's usually never noisy this early in the morning unless it's the landscapers. I've been hearing noise all morning. I wonder what it's all about?{/i}"
    #play sound footssteps1

    jump c0_meetClaudia
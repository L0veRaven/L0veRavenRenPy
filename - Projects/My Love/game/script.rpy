# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define alex = Character("Alex", kind=adv)
define journal = Character(None, kind=nvl)
define claudia = Character("Claudia", kind=adv)
define tsukune = Character("Tsukune", kind=adv)
define rando = Character("???", kind=adv)
define witness = Character("Witness", kind=adv)


# The game starts here.

label start:
    stop music
    scene bg_alex_apartment_living_room with Dissolve(2.0)
    jump chapter_0_journal_1

label chapter_0_journal_1:
    journal "June 12, 2023 - Monday @ 7:05 AM"
    journal "I slept like usual, another nightmare. The thing is that I can't remember what the nightmare even was. All I can recall is waking up feeling afraid with sweat all over me. It sucks to be woken up like that every morning. Hopefully the nightmares settle down one of these days..."
    play sound "sfx/thud_1.mp3"
    journal "Other than that, I'm really liking doing these journal entries. Sure, it's weird to feel like you're talking to a wall at first, but there's something therapeutic about it. It's like someone is letting you vent to them for as long as you're willing to keep writing with a pen. It's nice to feel listened to, even if it's just a little journal holding all my thoughts together."
    nvl clear
    play sound "sfx/muffled_noise_1.mp3"
    journal "There is something that I recently realized that I'm struggling wtih. I didn't realize that I was feeling lonely for as long as I have. I thought I was just uncomfortable about being alone for too long at a time, but I'm also horrible at reaching out to people. I'd like to stay on top of talking with people, but it just ends up slipping my mind. I forget to talk to people until it's been so long that it'd feel out of place for me to reach out to them."
    play sound "sfx/thud_1.mp3"
    journal "I also noticed that I'm starting to learn to identify my emotions better after journaling for the past month. I make it a point to ask myself, \"What am I feeling?\" when I write these entries because it's more than just venting about my problems. If I know what I'm feeling, then it makes it easier to learn how to manage my emotions better. I guess re-learning emotions is common after suppressing them for so many years..."
    play sound "sfx/thud_1.mp3"
    "It's usually never this noisy this early in the morning unless it's the landscapers. I've been hearning noise all morning. I wonder what it's all about?"
    play sound  "sfx/door_lock.mp3"
    jump chapter_0_meet_claudia

label chapter_0_meet_claudia:
    scene bg_apartment_outside with fade
    rando "Alright Claudia, you take care!"
    play sound  "sfx/carDoor_close.mp3"
    claudia "Thanks Toby, I appreciate your help!"
    play sound  "sfx/carDrive_start.mp3"
    alex "..."
    alex "O-oh, hey there!"
    "Smooth."
    claudia "Hi, I didn't mean to startle you. I just moved my things in. Were my friend and I too loud?"
    alex "Don't worry about the noise, it's a one-time thing I'm sure. Which unit are you in?"
    claudia "The one next to yours. It took a couple hours to get everything out of the moving van, but I still have to unpack stuff. It'll be a while before everything is out of those boxes!"
    claudia "Moving to a new place can be pretty challengign, but I needed the change of scenery."
    alex "It can be good to move to a new area. Fresh starts, you know?"
    claudia "I'm definitely with you there. My name's Claudia. What about you?"
    alex "Oh, I'm Alex. I don't have any nicknames, though. My name kinda is too short for that."
    "I hope I'm not being too awkward in this conversation. It seems to be going well so far at least."
    alex "I'm kinda surprised it took them two and a half years to fill that unit."
    claudia "It's been that long? I better deep clean it then. I can't stand when dust builds up, and you know that maintenance doesn't do upkeep with empty units."
    "I can't tell if she's happy or upset. I probably shouldn't ask, just in case."
    alex "I get what you mean. It can be a struggle sometimes to pick up the slack for lazy apartment managers, right?"
    claudia "Heh... Yeah, it is."
    "She's struggling to keep a straight face. Is she sad, upset, or neutral? I can't get a good read on her."
    claudia "So... you've lived here for a while?"
    alex "Yeah, I've been here for about three years now."
    "She has a small smile on her face. MAybe she isn't all too mad? I wonder if I did anythign to make her upset..."
    claudia "There aren't any roaches here, right?"
    alex "Oh, no! They have pest control come out here every week, so wer don't have any pests like that around here."
    claudia "That's great. The place before the one I just moved from had a pretty bad roach infestation. You can thank the hoarder neighbors for that."
    claudia "Anyways, I'd better start unpacking and cleaning. I'll see you later!"
    alex "See you later!"
    "I should probably start heading off. I might be cutting it kinda close..."
    scene black with fade
    "See you later? I didn't think I'd get along with someone new so easily. Hopefully that's a good sign."
    "I felt pretty awkward when talking to her though."
    "It's good to know she's interested in seeing me again."
    ## INSERT RACING MINIGAME
    jump chapter_0_journal_2

label chapter_0_journal_2:
    "I didn't spend as much time as I wanted to on my journaling this morning."
    "Maybe if I spend a couple of minutes doing it now, now one will notice?"
    journal "8:02 AM"
    journal "I have something on my mind, or rather someone. I have a new neighbor that moved in to the unit right next to me. Her name is Claudia and I was able to say hi to her right as her friend drove off with the moving van. She and her friend were making a lot of noise when moving things inside the unit but it's not very common. She seems very nice but I think she got uncomfortable during the conversation at some point. She wasn't able to keep her facial expression consistent sometimes, so it was kind of hard to read her."
    journal "Something sticks out about her though... I just can't tell what it is exactly. I think I'll talk with Tsukune about her later. After all, it would be nice if we ended up becoming friends. I don't think friendships start that fast though, so maybe it'll take some time."
    "Oh shit, Tsukune's coming!"
    tsukune "Hey Alex, how's your morning going so far?"
    alex "I'm doing pretty good, I dound out I have a new neighbor this morning. You're pretty upbeat like usual, how's your morning?"
    tsukune "So, I had to take the bus to get to work today. Yesterday, my car's AC compressor seized up and snapped the serpentine belt, so now my car's in the shop until they get the parts delivered to replace what got trashed."
    alex "How much did it cost to get here by bus?"
    tsukune "It was about $3.50 just to get here, but I had to use coins or cash. They don't do card, which sucks. I'll live though. It could be a lot more expensive like in some other cities."
    tsukune "Ah, I should probably get to my desk now. Don't wanna get in any trouble."
    alex "Wait, before you go, I can take you to and from work until your car is fixed! We live in the same apartment complex after all."
    "I would hate for him to waste money on the bus fare if he can just take a ride home with me instead."
    tsukune "Really? Are you sure that's fine? I can pay you back in gas mon-"
    alex "Don't worry about it, it's on me. I wanna help you out if I can, and it's not like I'm going out of my way to take you home. I'm still doing the same drive as usual, just with an extra person in the car with me."
    tsukune "You're a great friend, Alex. I'll meet you after work, alright?"
    "Tsukune's right, we should get back to work before we get in trouble. Let's go!"
    
    return

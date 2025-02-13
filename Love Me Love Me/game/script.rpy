# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define claudia = Character('Claudia')
define nvl_claudia = Character('Claudia', kind=nvl, color="#000000")

define taro = Character('Taro')
define nvl_taro = Character('Taro', kind=nvl, color="#000000")

define narrator = nvl_narrator

define witness = Character('Witness', color="#000000")


# The game starts here.

label start:

    scene main_menu

    narrator """
    Claudia... I wish you knew how much I care about you.

    You're so kind... So beautiful...

    It hurts to see you show that same kindness to other people.

    It should be just me and you.
    
    {clear}

    No...

    It NEEDS to be just me and you.
    """

    claudia "Hey..."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "claudia happy.png" to the images
    # directory.

    show claudia neutral

    # These display lines of dialogue.

    claudia "Whatcha writing there?" 
    
    # This ends the game.

    return

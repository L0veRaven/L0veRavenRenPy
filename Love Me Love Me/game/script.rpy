# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define claudia = Character("Claudia")
define persona = Character("Person A")
define personb = Character("Person B")
define personc = Character("Person C")
define persond = Character("Person D")


# The game starts here.

label start:

    scene black

    claudia "Hey..."

    persona "Hey! Wake up!"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "claudia happy.png" to the images
    # directory.

    show claudia happy

    # These display lines of dialogue.

    claudia "You've created a new Ren'Py game."

    claudia "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

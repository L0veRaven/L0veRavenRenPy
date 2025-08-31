# **** SCRIPT INFO ****
# This script was made for a free online video tutorial on Youtube for teaching purposes by creator "__ess__ Ren'Py Tutorials".
#
# This finished script is only available to download and use in projects by being a Patreon in the tier "Scripter" or higher on the Patreon page as linked to below.
#
# URL to video tutorial series: https://www.youtube.com/watch?v=ZZsCUROxKQk&list=PL7wM8yQ325u-JGrVeQwkjHCPIQa6TdI6x
#
# The script comes with no warranty that it will work as the Ren'Py engine updates/changes.
#
# If you don't understand how something is working in this script, it's recommended you have a look at the tutorial video for more information.
#
# Please, do not redistribute this script for download anywhere. If you wish to share it with others, please link to the Patreon page as specified below.
#
# You may use and adapt this script for your game for personal or commercial purposes.
#
# Patreon page where this script is available: https://www.patreon.com/ess_renpy_tutorials
#
# Images available for this tutorial can be used in your finished commercial or personal projects if you wish.
#
# Update 1.0.1: I had defined a variable called "selected_character_xpos" but called it "selected_character_pos" in other places of the code. This is now fixed.

init python:
    def reset_racing_game():
        # Function to reset variables for the mini-game so it can start over.
        global selected_character
        global selected_character_pos
        global who_won
        global goal_reached
        global countdown_timer

        countdown_timer = 3
        who_won = None
        goal_reached = False
        selected_character = None
        selected_character_pos = [0, 0]
        character_1.x = character_start_xpos
        character_2.x = character_start_xpos
        character_3.x = character_start_xpos

        # Hide game over screen and show the menu again.
        renpy.hide_screen("game_over")
        renpy.hide_screen("racing_mini_game")
        renpy.show_screen("racing_game_menu")

    def npc_movement(st):
        # This is the update function of the spritemanager object. We use it to move NPC characters automatically.
        if not goal_reached and countdown_timer == 0:
            if selected_character == "character 1":
                # The player's character is "character 1" so we move character 2 and 3.
                npc_move(character = character_2)
                npc_move(character = character_3)

            elif selected_character == "character 2":
                npc_move(character = character_1)
                npc_move(character = character_3)

            elif selected_character == "character 3":
                npc_move(character = character_1)
                npc_move(character = character_2)

            return 0

        elif countdown_timer != 0:
            return 0

        else:
            return None

    def npc_move(character):
        # This function is for moving an NPC character according to their individual speeds.
        global goal_reached
        global who_won

        if character.x < goal_xpos:
            character.x += character.speed
        else:
            goal_reached = True
            who_won = character
            renpy.show_screen("game_over")
            renpy.restart_interaction()

    def character_move(character):
        # This function is for moving the player character according to its speed.
        global goal_reached
        global who_won
        global selected_character_pos

        if character.x < goal_xpos:
            character.x += player_char_speed
            selected_character_pos = [character.x, character.y]
            renpy.restart_interaction()
        else:
            goal_reached = True
            who_won = character
            renpy.show_screen("game_over")
            renpy.restart_interaction()

    def character_events(event, x, y, st):
        # This function is the "event" function of the spritemanager object.
        # It's responsible for detecting input from the user like key presses.
        # Here we check if the player has pressed the correct keys, one by one, in order to move their character.
        global left_key_pressed
        global right_key_pressed
        global player_start_move

        if event.type == renpy.pygame_sdl2.KEYDOWN and countdown_timer == 0:
            # A key is being pressed down.
            # To make sure the player needs to press the left and right key one at a time (and not at the same time), we need to know which keys are currently pressed down.
            # That is done by using the function "get_pressed" available to the pygame "key" module which will return a sequence with all the keyboard keys available, together with "True" or "False" values according to if they're pressed or not.
            keys_pressed = renpy.pygame_sdl2.key.get_pressed()

            if keys_pressed[renpy.pygame_sdl2.K_LEFT]:
                # The left key is being pressed down.
                player_start_move = True
                left_key_pressed = True
            elif keys_pressed[renpy.pygame_sdl2.K_RIGHT]:
                # The right key is being pressed down.
                player_start_move = True
                right_key_pressed = True

            if left_key_pressed and right_key_pressed:
                # Both left and right keys have been pressed down, so now we want the player character to move.
                # Reset the variables back to False so we can check again next time.
                left_key_pressed = False
                right_key_pressed = False

                if selected_character == "character 1":
                    character_move(character_1)
                elif selected_character == "character 2":
                    character_move(character_2)
                elif selected_character == "character 3":
                    character_move(character_3)

    def setup_racing_game():
        # This function is responsible for setting up the racing mini-game.
        # It sets the speeds of each NPC character and their initial positions.
        # The "speed" attribute are only applicable if a character is not chosen as the player character, as it uses it's own speed stored in "player_char_speed".
        # Anything else you want to setup (your own variables, custom function calls etc.) before the mini-game starts can be done here.
        global selected_character_pos

        character_1.x = character_start_xpos
        character_1.y = 500
        character_1.speed = 0.1
        character_2.x = character_start_xpos
        character_2.y = 620
        character_2.speed = 0.4
        character_3.x = character_start_xpos
        character_3.y = 730
        character_3.speed = 0.3

        if selected_character == "character 1":
            selected_character_pos = [character_1.x, character_1.y]
        elif selected_character == "character 2":
            selected_character_pos = [character_2.x, character_2.y]
        elif selected_character == "character 3":
            selected_character_pos = [character_3.x, character_3.y]

        renpy.hide_screen("racing_game_menu")
        renpy.show_screen("racing_mini_game")


screen game_over:
    modal True

    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            align(0.5, 0.5)
            xysize(500, 350)
            background Solid("#00000080")
            text "Game Over!" size 50 align(0.5, 0.2)

            if who_won == character_1:
                if selected_character == "character 1":
                    text "You won!" size 40 align(0.5, 0.4)
                else:
                    text "Character 1 won!" size 40 align(0.5, 0.4)
            elif who_won == character_2:
                if selected_character == "character 2":
                    text "You won!" size 40 align(0.5, 0.4)
                else:
                    text "Character 2 won!" size 40 align(0.5, 0.4)
            elif who_won == character_3:
                if selected_character == "character 3":
                    text "You won!" size 40 align(0.5, 0.4)
                else:
                    text "Character 3 won!" size 40 align(0.5, 0.4)

            textbutton "Play Again!" align(0.5, 0.8) action Function(reset_racing_game)

screen countdown_timer:
    # Countdown to start.
    frame:
        background "#00000080"
        align(0.5, 0.5)
        xysize 400, 250
        vbox:
            align(0.5, 0.5)
            text "Get Ready!" size 40 xalign 0.5
            text "[countdown_timer]" size 40 xalign 0.5

    timer 1.0 action If(countdown_timer > 1, SetVariable("countdown_timer", countdown_timer - 1), [SetVariable("countdown_timer", 0), Hide("countdown_timer")]) repeat If(countdown_timer > 1, True, False)

screen racing_mini_game:
    on "show" action Show("countdown_timer")
    key ["K_LEFT", "K_RIGHT"] action NullAction() # Since we use left and right keyboard buttons to move the player character, we make sure they don't focus on the quick menu buttons.
    image "background.png"

    # Character sprites
    add character_sprites

    # Show player how to play the game
    if not player_start_move and countdown_timer == 0:
        frame:
            align(0.5, 0.3)
            xysize(600, 250)
            background "#00000080"
            vbox:
                spacing 20
                align(0.5, 0.5)
                text "Alternate arrow keys to move" xalign 0.5
                add "arrow_keys" xalign 0.5

    # Player's character indicator
    image "player_indicator.png" xpos selected_character_pos[0] + 50 ypos selected_character_pos[1] - 50

screen racing_game_menu:
    image "background.png"
    image Solid("#00000080") # Black transparent background.

    text "Select a character" size 50 align(0.5, 0.1)

    hbox:
        align(0.5, 0.4)
        spacing 10
        imagebutton auto "Menu/character_1_%s.png" selected If(selected_character == "character 1", True, False) align(0.5, 0.5) action SetVariable("selected_character", "character 1")
        imagebutton auto "Menu/character_2_%s.png" selected If(selected_character == "character 2", True, False) align(0.5, 0.5) action SetVariable("selected_character", "character 2")
        imagebutton auto "Menu/character_3_%s.png" selected If(selected_character == "character 3", True, False) align(0.5, 0.5) action SetVariable("selected_character", "character 3")

    imagebutton idle "Menu/play_button_idle.png" sensitive If(selected_character is not None, True, False) action Function(setup_racing_game) align(0.5, 0.8)

image arrow_keys:
    zoom 0.5
    "arrow_keys_1.png"
    pause 0.5
    "arrow_keys_2.png"
    pause 0.5
    repeat

#Example of an animated image
image character_1_animation:
    "character1-1.png"
    pause 0.5
    "character1-2.png"
    pause 0.5
    "character1-3.png"
    pause 0.5
    repeat

# Character sprites
default character_sprites = SpriteManager(update = npc_movement, event = character_events)
default character_1 = character_sprites.create("character_1.png")
default character_2 = character_sprites.create("character_2.png")
default character_3 = character_sprites.create("character_3.png")

# Character variables
default character_start_xpos = 100 # Since the x-value of the characters will change, it will be good to have a variable that stores what the inital position is so we can grab it when needed.
default goal_xpos = 1500 # The x-coordinate of there the goal is.
default player_char_speed = 20 # Speed of the player character.

# Keypress variables
default left_key_pressed = False
default right_key_pressed = False
default player_start_move = False

# Other variables
default selected_character = None # The character the player has chosen. Is "None" at start but will be changed to the player's choice in-game.
default selected_character_pos = [0, 0] # Keeps track of the current position of the playable character to help position the "player indicator".
default who_won = None
default goal_reached = False
default countdown_timer = 3

label start:
    call screen racing_game_menu

    return

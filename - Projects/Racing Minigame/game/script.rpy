# The script of the game goes in this file.

init python:
    ## Racing Minigame
    def reset_racing_game():
        # Resets variables for the game to restart
        global selected_car
        global selected_car_pos
        global who_won
        global goal_reached
        global countdown_timer

        countdown_timer = 3
        who_won = None
        goal_reached = False
        selected_car = None
        selected_car_pos = [0, 0]
        car_1.x - car_start_xpos
        car_2.x - car_start_xpos
        car_3.x - car_start_xpos

        # Hide game over screen and show the menu again
        renpy.hide_screen("game_over")
        renpy.hide_screen("racing_mini_game")
        renpy.show_screen("racing_game_menu")

    def setup_racing_game():
        # Sets the speed of each NPC car and their initial positions
        # "speed" attribute only applies to npc cars
        
        global selected_car_pos

        car_1.x = car_start_xpos
        car_1.y = 500
        car_1.speed = 0.1

        car_2.x = car_start_xpos
        car_2.y = 620
        car_2.speed = 0.4

        car_3.x = car_start_xpos
        car_3.y = 730
        car_3.speed = 0.3

        if selected_car == "car 1":
            selected_car_pos = [car_1.x, car_1.y]
        elif selected_car == "car 2":
            selected_car_pos = [car_2.x, car_2.y]
        elif selected_car == "car 3":
            selected_car_pos = [car_3.x, car_3.y]

        renpy.hide_screen("racing_game_menu")
        renpy.show_screen("racing_mini_game")

    def npc_move(car):
        # This function is for moving an NPC character according to their individual speeds.
        global goal_reached
        global who_won

        if car.x < goal_xpos:
            car.x += car.speed
        else:
            goal_reached = True
            who_won = car
            renpy.show_screen("game_over")
            renpy.restart_interaction()
    
    def car_move(car):
        # Moves player according to speed
        global goal_reached
        global who_won
        global selected_car_pos

        if car.x < goal_xpos:
            car.x += player_car_speed
            selected_car_pos = [car.x, car.y]
            renpy.restart_interaction()
        else:
            goal_reached = True
            who_won = car
            renpy.show_screen("game_over")
            renpy.restart_interaction()

    def car_events(event, x, y, st):
        # This function is the "event" function of the spritemanager object
        # Detects input from the user like key presses
        # Check if the player has pressed the correct keyes one by one to move the cars
        global left_key_pressed
        global right_key_pressed
        global player_start_move

        if event.type == renpy.pygame_sdl2.KEYDOWN and countdown_timer == 0:
            # A key is being pressed down
            # "get_pressed" (in the pygame "key" module) makes sure the player presses one key at a time

            keys_pressed = renpy.pygame_sdl2.key.get_pressed()

            if keys_pressed[renpy.pygame_sdl2.K_LEFT]:
                # Detects left key press
                player_start_move = True
                left_key_pressed = True
            elif keys_pressed[renpy.pygame_sdl2.K_RIGHT]:
                # Detects right key press
                player_start_move = True
                right_key_pressed = True

            if left_key_pressed and right_key_pressed:
                # Both keys are pressed down
                # Reset variables back to False so we can check again next time

                left_key_pressed = False
                right_key_pressed = False

                if selected_car == "car 1":
                    car_move(car_1)
                elif selected_car == "car 2":
                    car_move(car_2)
                elif selected_car == "car 3":
                    car_move(car_3)
    
    def npc_movement(st):
        # Update function for spritemanager object (automatically moves cars)

        if not goal_reached and countdown_timer == 0:
            if selected_car == "car 1":
                npc_move(car = car_2)
                npc_move(car = car_3)

            elif selected_car == "car 2":
                npc_move(car = car_1)
                npc_move(car = car_3)

            elif selected_car == "car 3":
                npc_move(car = car_1)
                npc_move(car = car_2)

            return 0

        elif countdown_timer != 0:
            return 0

        else:
            return None

## Racing Minigame
    ## Car Sprites
default car_sprites = SpriteManager(update = npc_movement, event = car_events)
default car_1 = car_sprites.create("racing_minigame/car_1.png")
default car_2 = car_sprites.create("racing_minigame/car_2.png")
default car_3 = car_sprites.create("racing_minigame/car_3.png")

    ## Car Variables
default car_start_xpos = 100 # Starting coordinate
default goal_xpos = 1500 # Goal coordinate
default player_car_speed = 20 # Speed of the player car

    ## Keypress Variables
default left_key_pressed = False
default right_key_pressed = False
default player_start_move = False

    ## Other Variables
default selected_car = None # The car the player selected
default selected_car_xpos = None # Keeps track of current position of the playable character
default who_won = None
default goal_reached = False
default countdown_timer = 3

image arrow_keys:
    zoom 0.5
    "arrow_keys_1.png"
    pause 0.5
    "arrow_keys_2.png"
    pause 0.5
    repeat

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

            text "Game Over!":
                size 50
                align(0.5, 0.2)
            
            if who_won == car_1:
                if selected_car == "car 1":
                    text "You won!":
                        size 40
                        align(0.5, 0.4)
                    
                    textbutton "Continue":
                        align(0.5, 0.8)
                        action Jump("start"), renpy.hide_screen("racing_mini_game"), renpy.hide_screen("game_over")
                else:
                    text "Character 1 won!":
                        size 40
                        align(0.5, 0.4)
                    
                    textbutton "Play Again!":
                        align(0.5, 0.8)
                        action Function(reset_racing_game)

            elif who_won == car_2:
                if selected_car == "car 2":
                    text "You won!":
                        size 40
                        align(0.5, 0.4)
                    
                    textbutton "Continue":
                        align(0.5, 0.8)
                        action Jump("start"), renpy.hide_screen("racing_mini_game"), renpy.hide_screen("game_over")
                else:
                    text "Character 2 won!":
                        size 40
                        align(0.5, 0.4)
                    
                    textbutton "Play Again!":
                        align(0.5, 0.8)
                        action Function(reset_racing_game)

            elif who_won == car_3:
                if selected_car == "car 3":
                    text "You won!":
                        size 40
                        align(0.5, 0.4)
                    
                    textbutton "Continue":
                        align(0.5, 0.8)
                        action Jump("start"), renpy.hide_screen("racing_mini_game"), renpy.hide_screen("game_over")
                else:
                    text "Character 3 won!":
                        size 40
                        align(0.5, 0.4)

                    textbutton "Play Again!":
                        align(0.5, 0.8)
                        action Function(reset_racing_game)

screen countdown_timer:
    # Countdown to start
    frame:
        background "#00000080"
        align(0.5, 0.5)
        xysize 400, 250
        
        vbox:
            align(0.5, 0.5)
            text "Get Ready!":
                size 40
                xalign 0.5
            text "[countdown_timer]":
                size 40
                xalign 0.5
    
    timer 1.0:
        action If(countdown_timer > 1, SetVariable("countdown_timer", countdown_timer - 1), [SetVariable("countdown_timer", 0), Hide("countdown_timer")])
        repeat If(countdown_timer > 1, True, False)

    ## Actual Minigame
screen racing_mini_game:
    on "show" action Show("countdown_timer")
    key ["K_LEFT", "K_RIGHT"] action NullAction()

    image "racing_minigame/racing_bg.png"

    # Car Sprites
    add car_sprites

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
    
    # Player's car indicator
    image "player_indicator.png":
        xpos selected_car_pos[0] + 50
        ypos selected_car_pos[1] - 50

    ## Car Select Screen
screen racing_game_menu:
    image "racing_minigame/racing_bg.png"
    image Solid("#00000080") #black transparent backgroun

    text "Select a car":
        size 50
        align (0.5, 0.1)

    hbox:
        align (0.5, 0.4)
        spacing 10

        imagebutton auto "racing_minigame/menu/car_1_%s.png":  
            selected If(selected_car == "car 1", True, False)
            align (0.5, 0.5)
            action SetVariable("selected_car", "car 1")

        imagebutton auto "racing_minigame/menu/car_2_%s.png":  
            selected If(selected_car == "car 2", True, False)
            align (0.5, 0.5)
            action SetVariable("selected_car", "car 2")

        imagebutton auto "racing_minigame/menu/car_3_%s.png":  
            selected If(selected_car == "car 3", True, False)
            align (0.5, 0.5)
            action SetVariable("selected_car", "car 3")
    
    imagebutton idle "racing_minigame/menu/play_button_idle.png":
        sensitive If(selected_car is not None, True, False)
        action Function(setup_racing_game)
        align (0.5, 0.8)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    call screen racing_game_menu

    # This ends the game.

    return

import os
import readchar
from random import randint

POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 11
obstacle_definition = """\
###########################
                       ####
####################   ####
####################   ####
###########                
###################  ######
################         ##
#########           #######
#############              
#####################   ###
#####     #######         #
########                ###
######## ########          
#####    ##########    ####
###########################\
"""
my_position = [0, 1]
tail = []
tail_len = 0
map_objects = []
end_game = False

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = 15

# Main Loop
while not end_game:
    # Generate random objects on the map
    # while len(map_objects) < NUM_OF_MAP_OBJECTS:
    #     new_object_position = [randint(0, MAP_WIDTH), randint(0, MAP_HEIGHT)]
    #     if new_object_position not in map_objects and new_object_position != my_position:
    #         map_objects.append(new_object_position)
    # Draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            i = 0
            for map_object in map_objects:
                i += 1
                if coordinate_x == map_object[POS_X] and coordinate_y == map_object[POS_Y]:
                    char_to_draw = "*"
                    break

            for tail_piece in tail:
                if coordinate_x == tail_piece[POS_X] and coordinate_y == tail_piece[POS_Y]:
                    char_to_draw = "@"
            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                if char_to_draw == "*":
                    map_objects.pop(i - 1)
                    tail_len += 1
                char_to_draw = "@"

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"
            print(f" {char_to_draw} ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where he wants to move
    # direction = input("¿Dónde te quieres mover? [WASD]: ")
    direction = readchar.readchar()
    # print(direction)
    old_position = my_position.copy()
    if direction == "w":
        my_position[POS_Y] = (my_position[POS_Y] - 1) % MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] = (my_position[POS_Y] + 1) % MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] = (my_position[POS_X] - 1) % MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] = (my_position[POS_X] + 1) % MAP_WIDTH
    elif direction == "q":
        end_game = True

    # Wall collision
    if obstacle_definition[my_position[POS_Y]][my_position[POS_X]] == "#":
        my_position = old_position

    # tail mechanics
    if my_position in tail:
        end_game = True

    tail.insert(0, old_position)
    tail = tail[:tail_len]
    os.system("clear")

print("End Game")

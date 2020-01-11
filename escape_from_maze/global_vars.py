
wall_view = '@'  # wall's view

player_view = 'A'  # player's view

maze_indents = (3, 5)  # horizontal and vertical indents


keys_map = {        # keys: params from pressing keyboard arrows buttons ( window.getch() )
    259: (1, 0),    # values: horizontal and vertical coordinates around something
    258: (-1, 0),
    260: (0, 1),
    261: (0, -1)
}


random_wall_map = tuple(keys_map.values())  # coordinates for building random walls in maze

start_text = 'Press "Space" to start!'
start_text_len = len(start_text)

# numbers of colors for game objects
start_text_color = 2
player_color = 3

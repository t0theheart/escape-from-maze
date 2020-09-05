
wall_view = '@'  # wall's view

player_view = 'A'  # player's view

enemy_view = '&'  # enemy's view

key_view = 'K'  # key's view

maze_indents = (3, 5)  # horizontal and vertical indents


keys_map = {        # keys: params from pressing keyboard arrows buttons ( window.getch() )
    259: (1, 0),    # values: horizontal and vertical coordinates around something
    258: (-1, 0),
    260: (0, 1),
    261: (0, -1)
}


keys_map_reversed = {
    259: 258,
    258: 259,
    260: 261,
    261: 260
}


random_wall_map = tuple(keys_map.values())  # coordinates for building random walls in maze

start_text = 'Press "Space" to start!'
start_text_len = len(start_text)

enemies_text = 'Enemies: '
enemies_text_len = len(enemies_text)

keys_text = 'Keys: '
keys_text_len = len(keys_text)

# numbers of colors for game objects
wall = 31
key = 32
player = 33
enemy = 34

# service colors
# white = 0
black = 11
yellow = 12
# blue = 3
# red = 4

# background colors
lose_game_screen = 66
win_game_screen = 77

# dividers for maze's objects
enemy_divider = 100

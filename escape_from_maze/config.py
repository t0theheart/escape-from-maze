import configparser


def read_rgb(rgb: str):
    return map(int, rgb.split(' '))


config = configparser.ConfigParser()
config.read('settings.ini')
settings = config['SETTINGS']


wall_view = settings['wall_view']
player_view = settings['player_view']
enemy_view = settings['enemy_view']
key_view = settings['key_view']


wall_color = read_rgb(settings['wall_color'])
player_color = read_rgb(settings['player_color'])
enemy_color = read_rgb(settings['enemy_color'])
key_color = read_rgb(settings['key_color'])

black_color = (0, 0, 0)
yellow_color = (855, 730, 150)


start_text = settings['start_text']
enemies_text = settings['enemies_text']
keys_text = settings['keys_text']


# numbers to init color in system

# numbers of colors for game objects
wall = 31
key = 32
player = 33
enemy = 34

# service colors
white = 0
black = 11
yellow = 12
blue = 3
red = 4

# background colors
lose_game_screen = 66
win_game_screen = 77


# dividers for maze's objects
enemy_divider = 100


# horizontal and vertical indents
maze_indents = (3, 5)


# keys: params from pressing keyboard arrows buttons ( window.getch() )
# values: horizontal and vertical coordinates around object
keys_map = {
    259: (1, 0),
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


# coordinates for building random walls in maze
random_wall_map = tuple(keys_map.values())

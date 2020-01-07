import random
from escape_from_maze.global_vars import maze_indents
from escape_from_maze.global_vars import wall
from escape_from_maze.global_vars import random_wall_map


def build_random_wall_near(window, y, x):
    params = random.choice(random_wall_map)
    y = y - params[0]
    x = x - params[1]
    window.addstr(y, x, wall)


def build_top_and_bottom_walls(window, top_wall, bottom_wall, left_wall, right_wall):
    for x in range(top_wall, bottom_wall):
        window.addstr(x, left_wall, wall)
        window.addstr(x, right_wall-1, wall)


def build_left_and_right_walls(window, top_wall, bottom_wall, left_wall, right_wall):
    for x in range(left_wall, right_wall):
        window.addstr(top_wall, x, wall)
        window.addstr(bottom_wall, x, wall)


def build_inner_walls(window, top_wall, bottom_wall, left_wall, right_wall):
    for y in range(top_wall + 1, bottom_wall):
        for x in range(left_wall + 1, right_wall - 1):
            if y % 2 != 0 and x % 2 != 0:
                window.addstr(y, x, wall)
                build_random_wall_near(window, y, x)


def generate_maze(window, height, width):
    horizontal, vertical = maze_indents

    top_wall = horizontal
    left_wall = vertical
    bottom_wall = height - top_wall - 1
    right_wall = width - left_wall

    if height % 2 == 0:
        bottom_wall -= 1
    if width % 2 == 0:
        right_wall -= 1

    args = (window, top_wall, bottom_wall, left_wall, right_wall)

    build_top_and_bottom_walls(*args)

    build_left_and_right_walls(*args)

    build_inner_walls(*args)

import curses
import random


HEIGHT, WEIGHT = 0, 0


random_wall = [
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0)
]


def build_random_wall_near(window, y, x):
    params = random.choice(random_wall)
    y = y - params[0]
    x = x - params[1]
    window.addstr(y, x, '@')


def build_borders(window, height, width, maze_indents):
    """Create borders of maze in window"""

    top, left, right, bottom = maze_indents
    height -= top + bottom
    to_right_side = width-left

    if height % 2 == 0:
        height = height - 1
    if width % 2 == 0:
        to_right_side = to_right_side - 1

    for x in range(top, height):
        window.addstr(x, left, '@')
        window.addstr(x, to_right_side-1, '@')

    for x in range(left, to_right_side):
        window.addstr(left, x, '@')
        window.addstr(height, x, '@')

    # for y in range(top+1, height):
    #     for x in range(left+1, to_right_side-1):
    #         window.addstr(y, x, '.')

    for y in range(top + 1, height):
        for x in range(left + 1, to_right_side - 1):
            if y % 2 != 0 and x % 2 != 0:
                window.addstr(y, x, '@')
                build_random_wall_near(window, y, x)


def render_maze(window, height, width, maze_indents):
    build_borders(window, height, width, maze_indents)



def refresh_window_handler(window) -> tuple:
    """Return tuple of window's height and width"""

    return window.getmaxyx()


# temporary func for test
def print_h_w_window(window, height, width):
    window.addstr(0, 0, '{0}, {1}'.format(height, width))


def main(window):
    global HEIGHT, WEIGHT
    curses.curs_set(False)
    #window.nodelay(True)

    maze_indents = [5, 5, 5, 1]  # top, left, right, bottom

    while True:
        height, width = refresh_window_handler(window)
        if HEIGHT == height and WEIGHT == width:
            pass
        else:
            window.clear()
            render_maze(window, height, width, maze_indents)
            HEIGHT, WEIGHT = height, width

        print_h_w_window(window, height, width)
        window.refresh()


curses.wrapper(main)

import curses
from escape_from_maze.maze_generator import generate_maze
from escape_from_maze.units import Player
from escape_from_maze.global_vars import player_view


# temporary func for test
def print_h_w_window(window, height, width):
    window.addstr(0, 0, '{0}, {1}'.format(height, width))


def main(window):
    curses.curs_set(False)

    window_height_width = (0, 0)
    start = False
    player = None

    while True:
        height, width = window.getmaxyx()
        if window_height_width[0] != height or window_height_width[1] != width:
            window.clear()
            coordinates = generate_maze(window, height, width)
            window_height_width = height, width

        print_h_w_window(window, height, width)

        key = window.getch()

        if not start and key == 32:
            start = True
            x = coordinates[0] + 1
            y = coordinates[2] + 1
            player = Player(x, y, window, player_view)
            window.refresh()

        elif start and key in player.keys_map.keys():
            player.do_move(key)
            window.refresh()


curses.wrapper(main)

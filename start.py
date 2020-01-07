import curses
from escape_from_maze.handlers import change_window_size_handler


def main(window):
    curses.curs_set(False)

    change_window_size_handler(window)


curses.wrapper(main)

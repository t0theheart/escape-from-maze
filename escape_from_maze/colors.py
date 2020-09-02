from escape_from_maze.global_vars import yellow, red, blue, black
import curses


def init_color(number: int, rgb: tuple):
    curses.init_color(number, *rgb)
    curses.init_pair(number, number, 0)


def init_colors():
    init_color(blue, (455, 730, 750))
    init_color(yellow, (855, 730, 150))
    init_color(red, (800, 400, 400))
    init_color(black, (0, 0, 0))


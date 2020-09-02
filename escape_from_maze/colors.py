from escape_from_maze.global_vars import yellow, red, blue, black, lose_game_screen, win_game_screen
import curses


def init_background(number: int, front_color: int, back_color):
    curses.init_pair(number, front_color, back_color)


def init_color(number: int, rgb: tuple):
    curses.init_color(number, *rgb)
    curses.init_pair(number, number, 0)


def init_colors():
    init_color(blue, (455, 730, 750))
    init_color(yellow, (855, 730, 150))
    init_color(red, (800, 400, 400))
    init_color(black, (0, 0, 0))

    init_background(lose_game_screen, curses.COLOR_WHITE, curses.COLOR_RED)
    init_background(win_game_screen, black, yellow)


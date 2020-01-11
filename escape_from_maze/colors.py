from escape_from_maze.global_vars import player_color, start_text_color
import curses


def init_color_start_text():
    number = start_text_color
    curses.init_color(number, 855, 730, 150)
    curses.init_pair(number, number, 0)


def init_color_player():
    number = player_color
    curses.init_color(number, 455, 730, 750)
    curses.init_pair(number, number, 0)


def init_colors():
    init_color_player()
    init_color_start_text()

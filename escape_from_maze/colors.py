from escape_from_maze.global_vars import key, enemy, player, black, yellow, lose_game_screen, win_game_screen, wall
import curses


def init_background(number: int, front_color: int, back_color):
    curses.init_pair(number, front_color, back_color)


def init_color(number: int, rgb: tuple):
    curses.init_color(number, *rgb)
    curses.init_pair(number, number, 0)


def init_colors():
    init_color(player, (455, 730, 750))
    init_color(key, (855, 730, 150))
    init_color(enemy, (800, 400, 400))
    init_color(wall, (800, 800, 800))

    init_color(black, (0, 0, 0))

    init_background(lose_game_screen, curses.COLOR_WHITE, curses.COLOR_RED)
    init_background(win_game_screen, black, yellow)


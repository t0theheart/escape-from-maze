from escape_from_maze.config import (
    key, enemy, player, black, yellow, lose_game_screen, win_game_screen, wall,
    key_color, enemy_color, player_color, wall_color, black_color, yellow_color
)
import curses


def init_background(number: int, front_color: int, back_color):
    curses.init_pair(number, front_color, back_color)


def init_color(number: int, rgb: tuple):
    curses.init_color(number, *rgb)
    curses.init_pair(number, number, 0)


def init_colors():
    init_color(player, player_color)
    init_color(key, key_color)
    init_color(enemy, enemy_color)
    init_color(wall, wall_color)

    init_color(black, black_color)
    init_color(yellow, yellow_color)

    init_background(lose_game_screen, curses.COLOR_WHITE, curses.COLOR_RED)
    init_background(win_game_screen, black, yellow)


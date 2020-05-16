from escape_from_maze.global_vars import player_color, start_text_color, enemy_color
from escape_from_maze.global_vars import enemy_view, player_view
import curses


def init_color(number: int, rgb: tuple):
    curses.init_color(number, *rgb)
    curses.init_pair(number, number, 0)


def init_colors():
    init_color(player_color, (455, 730, 750))
    init_color(start_text_color, (855, 730, 150))
    init_color(enemy_color, (800, 400, 400))


def get_color_ord(number: int) -> int:
    return curses.color_pair(number)


def get_view_with_color_and_ord_map() -> dict:
    return {
        get_color_ord(player_color) + ord(player_view): player_view,
        get_color_ord(enemy_color) + ord(enemy_view): enemy_view
    }

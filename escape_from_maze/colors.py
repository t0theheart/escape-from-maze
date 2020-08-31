from escape_from_maze.global_vars import yellow, red, blue
from escape_from_maze.global_vars import enemy_view, player_view, key_view
import curses


def init_color(number: int, rgb: tuple):
    curses.init_color(number, *rgb)
    curses.init_pair(number, number, 0)


def init_colors():
    init_color(blue, (455, 730, 750))
    init_color(yellow, (855, 730, 150))
    init_color(red, (800, 400, 400))


def get_color_ord(number: int) -> int:
    return curses.color_pair(number)


def get_view_with_color_and_ord_map() -> dict:
    return {
        get_color_ord(blue) + ord(player_view): player_view,
        get_color_ord(red) + ord(enemy_view): enemy_view,
        get_color_ord(yellow) + ord(key_view): key_view,
    }

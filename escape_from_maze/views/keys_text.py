from escape_from_maze.global_vars import keys_text, keys_text_len, maze_indents, yellow
import curses


def print_keys_amount(window, keys_amount):
    print_indent = maze_indents[0] + 2
    window.addstr(1, print_indent, keys_text.format(keys_amount))
    window.addstr(1, print_indent + keys_text_len, f'0/{keys_amount}', curses.color_pair(yellow))

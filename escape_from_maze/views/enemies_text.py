from escape_from_maze.global_vars import enemies_text, enemies_text_len, maze_indents, red
import curses


def print_enemies_amount(window, enemies_amount):
    print_indent = maze_indents[0] + 15
    window.addstr(1, print_indent, enemies_text.format(enemies_amount))
    window.addstr(1, print_indent + enemies_text_len, str(enemies_amount), curses.color_pair(red))

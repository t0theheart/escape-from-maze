from escape_from_maze.config import enemies_text, maze_indents, enemy
import curses


def print_enemies_amount(window, enemies_amount):
    print_indent = maze_indents[0] + 15
    window.addstr(1, print_indent, enemies_text.format(enemies_amount))
    window.addstr(1, print_indent + len(enemies_text), f' {enemies_amount}', curses.color_pair(enemy))

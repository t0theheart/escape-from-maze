from escape_from_maze.global_vars import start_text, start_text_len
import curses


def print_press_space_to_start(window, height, width):
    window.addstr(height-2, (width//2)-start_text_len//2, start_text, curses.color_pair(2))


def remove_press_space_to_start(window, height, width):
    window.addstr(height - 2, (width // 2) - start_text_len // 2, ' ' * start_text_len)

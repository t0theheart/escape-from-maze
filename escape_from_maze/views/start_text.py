from escape_from_maze.config import start_text, yellow
import curses


def print_press_space_to_start(window, height, width):
    window.addstr(height-2, (width//2) - len(start_text)//2, start_text, curses.color_pair(yellow))


def remove_press_space_to_start(window, height, width):
    window.addstr(height - 2, (width // 2) - len(start_text) // 2, ' ' * len(start_text))

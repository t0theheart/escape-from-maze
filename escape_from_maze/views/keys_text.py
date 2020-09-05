from escape_from_maze.config import keys_text, maze_indents, key
import curses


class KeysText:
    def __init__(self, window, total_keys):
        self.window = window
        self.total_keys = total_keys
        self.collected_keys = 0
        self.indent = maze_indents[0] + 2
        self.indent_with_text = self.indent + len(keys_text)

    def print_keys_amount(self):
        self.window.addstr(1, self.indent, keys_text.format(self.total_keys))
        self.window.addstr(1, self.indent_with_text, f' {self.collected_keys}/{self.total_keys}', curses.color_pair(key))

    def up_and_print_keys_amount(self):
        self.collected_keys += 1
        self.print_keys_amount()

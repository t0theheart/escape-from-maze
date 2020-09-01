from escape_from_maze.global_vars import keys_text, keys_text_len, maze_indents, yellow
import curses


class KeysText:
    def __init__(self, window, total_keys):
        self.window = window
        self.total_keys = total_keys
        self.collected_keys = 0
        self.indent = maze_indents[0] + 2
        self.indent_with_text = self._indent + keys_text_len

    def print_keys_amount(self):
        self.window.addstr(1, self.indent, keys_text.format(self.total_keys))
        self.window.addstr(1, self.indent_with_text, f'{self.collected_keys}/{self.total_keys}', curses.color_pair(yellow))

    def up_and_print_keys_amount(self):
        self.collected_keys += 1
        self.print_keys_amount()

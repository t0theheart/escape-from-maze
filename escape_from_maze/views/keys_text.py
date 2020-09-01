from escape_from_maze.global_vars import keys_text, keys_text_len, maze_indents, yellow
import curses


class KeysText:
    def __init__(self, window, total_keys):
        self._window = window
        self._total_keys = total_keys
        self._collected_keys = 0
        self._indent = maze_indents[0] + 2
        self._indent_with_text = self._indent + keys_text_len

    def print_keys_amount(self):
        self._window.addstr(1, self._indent, keys_text.format(self._total_keys))
        self._window.addstr(1, self._indent_with_text, f'{self._collected_keys}/{self._total_keys}', curses.color_pair(yellow))

    def up_and_print_keys_amount(self):
        self._collected_keys += 1
        self.print_keys_amount()

from escape_from_maze.units import Unit
from escape_from_maze.global_vars import player_view, player_color, keys_map


class Player(Unit):

    color = player_color

    def __init__(self, x, y, window):
        super().__init__(x, y, window, player_view)

    def do_move(self, key):
        self._do_move(keys_map[key])

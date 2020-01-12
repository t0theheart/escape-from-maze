from escape_from_maze.units import Unit
from escape_from_maze.global_vars import enemy_view, enemy_color, keys_map


class Enemy(Unit):

    color = enemy_color

    def __init__(self, x, y, window):
        super().__init__(x, y, window, enemy_view)

    def do_move(self, key):
        self._do_move(keys_map[key])

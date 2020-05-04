from escape_from_maze.units import Unit
from escape_from_maze.global_vars import enemy_view, enemy_color, keys_map, keys_map_reversed
import random


class Enemy(Unit):

    color = enemy_color

    def __init__(self, x, y, window):
        super().__init__(x, y, window, enemy_view)
        self._last_move: int = 0

    def _decide_where_to_move(self) -> int:
        free_moves = self._get_free_moves(keys_map)
        if len(free_moves) > 1 and self._last_move:
            free_moves.remove(self._last_move)
        return random.choice(free_moves)

    def do_move(self):
        key = self._decide_where_to_move()
        self._do_move(keys_map[key])
        self._last_move = keys_map_reversed[key]

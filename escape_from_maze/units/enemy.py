from escape_from_maze.units import Unit
from escape_from_maze.global_vars import keys_map, keys_map_reversed
import random


class Enemy(Unit):
    def __init__(self, x, y, game):
        super().__init__(x, y, game.objects_view.get('enemy').view, game)
        self.color = game.objects_view.get('enemy').color
        self._last_move: int = 0
        self._not_allow_do_move.append(self.game.objects_view.get('key').ord)

    def _decide_where_to_move(self) -> int:
        free_moves = self._get_free_moves(keys_map)
        if len(free_moves) > 1 and self._last_move:
            free_moves.remove(self._last_move)
        return random.choice(free_moves)

    def _do_action(self, item_here: str):
        if item_here == self.game.objects_view.get('player').ord:
            self.game.lose_game()
            exit()

    def do_move(self):
        key = self._decide_where_to_move()
        self._do_move(keys_map[key])
        self._last_move = keys_map_reversed[key]

from escape_from_maze.units import Unit
from escape_from_maze.global_vars import player_view, player_color, keys_map, enemy_view, enemy_color


class Player(Unit):

    color = player_color

    def __init__(self, x, y, game):
        super().__init__(x, y, player_view, game)

    def _do_action(self, item_here: str):
        if item_here == enemy_view:
            self._replace(enemy_view, enemy_color)
            self.game.lose_game()

    def do_move(self, key):
        self._do_move(keys_map[key])

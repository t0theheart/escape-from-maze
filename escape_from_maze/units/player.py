from escape_from_maze.units import Unit
from escape_from_maze.global_vars import player_view, blue, keys_map, enemy_view, red


class Player(Unit):

    color = blue

    def __init__(self, coordinates, game):
        x, y = self._calculate_start_coordinates(coordinates)
        super().__init__(x, y, player_view, game)

    @staticmethod
    def _calculate_start_coordinates(coordinates: tuple) -> tuple:
        x = coordinates[1] // 2 + 2
        y = coordinates[3] // 2 + 2
        return x, y

    def _do_action(self, item_here: str):
        if item_here == enemy_view:
            self._replace(enemy_view, red)
            self.game.lose_game()

    def do_move(self, key):
        self._do_move(keys_map[key])

from escape_from_maze.units import Unit
from escape_from_maze.global_vars import keys_map


class Player(Unit):
    def __init__(self, coordinates, game):
        x, y = self._calculate_start_coordinates(coordinates)
        self.color = game.objects_view.get('player').color
        super().__init__(x, y, game.objects_view.get('player').view, game)

    @staticmethod
    def _calculate_start_coordinates(coordinates: tuple) -> tuple:
        x = coordinates[1] // 2 + 2
        y = coordinates[3] // 2 + 2
        return x, y

    def _do_action(self, item_here: str):
        if item_here == self.game.objects_view.get('enemy').ord:
            self._replace(self.game.objects_view.get('enemy').view, self.game.objects_view.get('enemy').color)
            self.game.lose_game()

    def do_move(self, key):
        self._do_move(keys_map[key])

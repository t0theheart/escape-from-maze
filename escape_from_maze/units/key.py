from escape_from_maze.units import Unit
from escape_from_maze.global_vars import yellow, key_view


class Key(Unit):

    color = yellow

    def __init__(self, x, y, game):
        super().__init__(x, y, key_view, game)

from escape_from_maze.units import Unit
from escape_from_maze.global_vars import key_color, key_view


class Key(Unit):

    color = key_color

    def __init__(self, x, y, game):
        super().__init__(x, y, key_view, game)

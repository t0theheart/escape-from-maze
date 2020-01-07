from escape_from_maze.units import Unit


class Player(Unit):

    def __init__(self, x, y, window, view):
        super().__init__(x, y, window, view)
        self.keys_map = {
            259: (1, 0),
            258: (-1, 0),
            260: (0, 1),
            261: (0, -1)
        }

    def do_move(self, key):
        self._do_move(self.keys_map[key])

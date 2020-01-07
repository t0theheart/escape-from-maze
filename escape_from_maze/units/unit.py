from escape_from_maze.global_vars import wall_view


class Unit:

    def __init__(self, x, y, window, view):
        self.x = x
        self.y = y
        self.window = window
        self.view = view
        self._create()

    def _create(self):
        self.window.addstr(self.x, self.y, self.view)

    def _do_move(self, move):
        if self._allow_to_move(move):
            self.window.addstr(self.x, self.y, ' ')
            self.x -= move[0]
            self.y -= move[1]
            self.window.addstr(self.x, self.y, self.view)

    def _allow_to_move(self, move):
        _x, _y = self.x, self.y
        _x -= move[0]
        _y -= move[1]
        onward = self.window.inch(_x, _y)
        if chr(onward) == wall_view:
            return False
        return True

import curses


class Unit:

    color = 0

    def __init__(self, x, y, view, game):
        self.x = x
        self.y = y
        self.view = view
        self.game = game
        self._create()
        self._not_allow_do_move = [self.game.objects_view.get('wall').ord]

    def _create(self):
        self.game.window.addstr(self.x, self.y, self.view, curses.color_pair(self.color))

    def _do_action(self, item_here: str):
        pass

    def _do_move(self, move):
        self.game.window.addstr(self.x, self.y, ' ')
        self.x -= move[0]
        self.y -= move[1]
        item_here = self.game.window.inch(self.x, self.y)
        self.game.window.addstr(self.x, self.y, self.view, curses.color_pair(self.color))
        self._do_action(item_here)

    def _allow_to_move(self, move):
        _x, _y = self.x, self.y
        _x -= move[0]
        _y -= move[1]
        onward = self.game.window.inch(_x, _y)
        if onward in self._not_allow_do_move:
            return False
        return True

    def _get_free_moves(self, keys_map: dict) -> list:
        free_moves = []
        for key, move in keys_map.items():
            if self._allow_to_move(move):
                free_moves.append(key)
        return free_moves

    def _replace(self, item_view, item_color):
        self.game.window.addstr(self.x, self.y, item_view, curses.color_pair(item_color))
        self.game.window.refresh()

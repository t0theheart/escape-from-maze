from escape_from_maze.units import Unit


class Key(Unit):
    def __init__(self, x, y, game):
        self.color = game.objects_view.get('key').color
        super().__init__(x, y, game.objects_view.get('key').view, game)

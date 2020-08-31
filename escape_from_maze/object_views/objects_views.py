import curses
from escape_from_maze.global_vars import red, blue, yellow, white
from escape_from_maze.global_vars import player_view, enemy_view, key_view, wall_view
from .object_view import ObjectView


class ObjectViews:
    def __init__(self):
        self._object_views = {}
        self._init_objects_views()

    def _init_objects_views(self):
        self._init_colors()
        self._object_views = {
            'player': ObjectView(player_view, blue),
            'enemy': ObjectView(enemy_view, red),
            'key': ObjectView(key_view, yellow),
            'wall': ObjectView(wall_view, white),
        }

    def get(self, name: str):
        return self._object_views.get(name)

    def _init_colors(self):
        self._init_color(blue, (455, 730, 750))
        self._init_color(yellow, (855, 730, 150))
        self._init_color(red, (800, 400, 400))

    @staticmethod
    def _init_color(number: int, rgb: tuple):
        curses.init_color(number, *rgb)
        curses.init_pair(number, number, 0)


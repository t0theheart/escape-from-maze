from escape_from_maze.global_vars import red, blue, yellow, white
from escape_from_maze.global_vars import player_view, enemy_view, key_view, wall_view
from .object_view import ObjectView


class ObjectViews:
    def __init__(self):
        self._object_views = {
            'player': ObjectView(player_view, blue),
            'enemy': ObjectView(enemy_view, red),
            'key': ObjectView(key_view, yellow),
            'wall': ObjectView(wall_view, white),
        }

    def get(self, name: str):
        return self._object_views.get(name)

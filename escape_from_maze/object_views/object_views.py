from escape_from_maze.global_vars import enemy, player, key, wall
from escape_from_maze.global_vars import player_view, enemy_view, key_view, wall_view
from .object_view import ObjectView


class ObjectViews:
    def __init__(self):
        self._object_views = {
            'player': ObjectView(player_view, player),
            'enemy': ObjectView(enemy_view, enemy),
            'key': ObjectView(key_view, key),
            'wall': ObjectView(wall_view, wall),
        }

    def get(self, name: str):
        return self._object_views.get(name)

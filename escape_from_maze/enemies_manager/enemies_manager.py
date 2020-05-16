import threading
from time import sleep


class EnemiesManager:

    def __init__(self):
        self.enemies = []
        self._do_moving = True

    def take_enemies(self, enemies: list):
        self.enemies.extend(enemies)

    def _move_enemies(self):
        for enemy in self.enemies:
            enemy.do_move()

    def move_enemies(self):
        while self._do_moving:
            self._move_enemies()
            sleep(0.3)

    def start(self):
        t = threading.Thread(target=self.move_enemies)
        t.start()

    def stop(self):
        self._do_moving = False

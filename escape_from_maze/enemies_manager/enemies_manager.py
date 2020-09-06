import threading
from time import sleep


class EnemiesManager:

    def __init__(self, wait_before_step: float):
        self.enemies = []
        self._do_moving = True
        self._wait = wait_before_step

    def take_enemies(self, enemies: list):
        self.enemies.extend(enemies)

    def _move_enemies(self):
        for enemy in self.enemies:
            enemy.do_move()

    def move_enemies(self):
        while self._do_moving:
            self._move_enemies()
            sleep(self._wait)

    def start(self):
        t = threading.Thread(target=self.move_enemies)
        t.start()

    def stop(self):
        self._do_moving = False

import curses
from escape_from_maze.maze_generator import generate_maze
from escape_from_maze.enemies_generator import generate_enemies
from escape_from_maze.enemies_manager.enemies_manager import EnemiesManager
from escape_from_maze.units import Player
from escape_from_maze.views import print_press_space_to_start, remove_press_space_to_start, print_enemies_amount
from escape_from_maze.colors import init_colors, get_view_with_color_and_ord_map
from escape_from_maze.global_vars import keys_map
from time import sleep


# temporary func for test
def print_h_w_window(window, height, width):
    window.addstr(0, 0, '{0}, {1}'.format(height, width))


class Game:
    def __init__(self):
        self.enemies_manager = EnemiesManager()
        self.player = None
        self.window_height_width = (0, 0)
        self.view_ord_map = {}
        self.started = False
        self.player = None
        self.window = None

    def _prepare_game(self, window):
        self.window = window
        self.view_ord_map = get_view_with_color_and_ord_map()
        self.window.nodelay(True)
        curses.curs_set(False)
        init_colors()

    def start(self, window):
        self._prepare_game(window)

        while True:
            height, width = window.getmaxyx()
            if self.window_height_width[0] != height or self.window_height_width[1] != width:
                self.window.clear()
                coordinates = generate_maze(self.window, height, width)
                self.window_height_width = height, width

            print_h_w_window(self.window, height, width)

            if not self.started:
                print_press_space_to_start(self.window, height, width)

            key = window.getch()

            if not self.started and key == 32:
                self.started = True
                remove_press_space_to_start(self.window, height, width)
                self.player = Player(coordinates, self)

                enemies = generate_enemies(coordinates, self)
                print_enemies_amount(self.window, len(enemies))

                self.enemies_manager.take_enemies(enemies)
                self.enemies_manager.start()

            elif self.started and key in keys_map.keys():
                self.player.do_move(key)

            self.window.refresh()

    def lose_game(self):
        sleep(3)
        self.window.erase()
        self.enemies_manager.stop()
        text = 'GAME OVER'
        height, width = self.window_height_width
        height = (height // 2) - 1
        width = (width // 2) - 1 - len(text)//2
        self.window.addstr(height, width, text)

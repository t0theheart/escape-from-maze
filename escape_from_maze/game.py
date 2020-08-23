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
    def __init__(self, window):
        self.enemies_manager = EnemiesManager()
        self.player = None
        self.window_height_width = (0, 0)
        self.view_ord_map = get_view_with_color_and_ord_map()
        self.started = False
        self.window = window
        self.game_over = False
        self._init_settings()

    def _init_settings(self):
        self.window.nodelay(True)
        curses.curs_set(False)
        init_colors()

    def _before_press_start(self):
        while True:
            height, width = self.window.getmaxyx()
            if self.window_height_width[0] != height or self.window_height_width[1] != width:
                self.window.clear()
                coordinates = generate_maze(self.window, height, width)
                self.window_height_width = height, width

            print_h_w_window(self.window, height, width)
            print_press_space_to_start(self.window, height, width)
            key = self.window.getch()
            if key == 32:
                self.started = True
                remove_press_space_to_start(self.window, height, width)
                self.player = Player(coordinates, self)

                enemies = generate_enemies(coordinates, self)
                print_enemies_amount(self.window, len(enemies))

                self.enemies_manager.take_enemies(enemies)
                self.enemies_manager.start()
                break

            self.window.refresh()

    def _after_press_start(self):
        while True:
            key = self.window.getch()
            if not self.game_over and key in keys_map.keys():
                self.player.do_move(key)

            self.window.refresh()

    def start(self):
        self._before_press_start()
        self._after_press_start()

    def lose_game(self):
        self.game_over = True
        sleep(1)
        self.window.erase()
        self.enemies_manager.stop()
        text = 'GAME OVER'
        height, width = self.window_height_width
        height = (height // 2) - 1
        width = (width // 2) - 2 - len(text)//2
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_RED)
        self.window.bkgd(' ', curses.color_pair(6) | curses.A_BOLD)
        self.window.addstr(height, width, text)

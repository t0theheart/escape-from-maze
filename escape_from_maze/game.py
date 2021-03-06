import curses
from escape_from_maze.maze_generator import generate_maze
from escape_from_maze.enemies_generator import generate_enemies
from escape_from_maze.keys_generator import generate_keys, clear_area_around_keys
from escape_from_maze.enemies_manager.enemies_manager import EnemiesManager
from escape_from_maze.units import Player
from escape_from_maze.views import print_press_space_to_start, remove_press_space_to_start, print_enemies_amount, KeysText
from escape_from_maze.config import keys_map, lose_game_screen, win_game_screen, wait_before_step
from escape_from_maze.object_views import ObjectViews
from escape_from_maze.colors import init_colors
from time import sleep


class Game:
    def __init__(self, window):
        self.window = window
        self._init_settings()
        self.enemies_manager = EnemiesManager(wait_before_step)
        self.objects_view = ObjectViews()
        self.keys_text = None
        self.player = None
        self.window_height_width = (0, 0)
        self.game_over = False

    def _init_settings(self):
        init_colors()
        self.window.nodelay(True)
        curses.curs_set(False)

    def _before_press_start(self):
        while True:
            height, width = self.window.getmaxyx()
            if self.window_height_width[0] != height or self.window_height_width[1] != width:
                self.window.clear()
                coordinates = generate_maze(self.window, height, width)
                self.window_height_width = height, width

            print_press_space_to_start(self.window, height, width)
            key = self.window.getch()
            if key == 32:
                self.started = True
                remove_press_space_to_start(self.window, height, width)

                self.player = Player(coordinates, self)

                keys = generate_keys(coordinates, self)
                self.keys_text = KeysText(self.window, len(keys))
                self.keys_text.print_keys_amount()
                clear_area_around_keys(coordinates, self)

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

    def _end_game(self):
        self.game_over = True
        self.enemies_manager.stop()
        sleep(1)
        self.window.erase()

    def _show_screen(self, phrase: str, screen_color: int):
        height, width = self.window_height_width
        height = (height // 2) - 1
        width = (width // 2) - len(phrase) // 2
        self.window.bkgd(' ', curses.color_pair(screen_color) | curses.A_BOLD)
        self.window.addstr(height, width, phrase)

    def lose_game(self):
        phrase = 'GAME OVER'
        self._end_game()
        self._show_screen(phrase, lose_game_screen)
        
    def win_game(self):
        phrase = 'CONGRATULATIONS, YOU WIN'
        self._end_game()
        self._show_screen(phrase, win_game_screen)

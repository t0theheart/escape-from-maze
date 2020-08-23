from escape_from_maze.game import Game
import curses


def game(window):
    Game(window).start()


if __name__ == '__main__':
    curses.wrapper(game)

from escape_from_maze.game import Game
import curses


if __name__ == '__main__':
    curses.wrapper(Game().start)

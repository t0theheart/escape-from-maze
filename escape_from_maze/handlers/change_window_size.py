from escape_from_maze.maze_generator import generate_maze


# temporary func for test
def print_h_w_window(window, height, width):
    window.addstr(0, 0, '{0}, {1}'.format(height, width))


def change_window_size_handler(window):
    window_height_width = (0, 0)
    while True:
        height, width = window.getmaxyx()
        if window_height_width[0] != height or window_height_width[1] != width:
            window.clear()
            generate_maze(window, height, width)
            window_height_width = height, width

        print_h_w_window(window, height, width)
        window.refresh()

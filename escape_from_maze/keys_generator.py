from escape_from_maze.units import Key


def get_keys_positions(coordinates) -> tuple:
    return (
        (coordinates[0] + 1, coordinates[2] + 1),  # upper_left
        (coordinates[0] + 1, coordinates[3] - 2),  # upper_right
        (coordinates[1] - 1, coordinates[0] + 3),  # lower_left
        (coordinates[1] - 1, coordinates[3] - 2),  # lower_right
    )


def generate_keys(coordinates, game) -> list:
    return [Key(*position, game) for position in get_keys_positions(coordinates)]


clear_area_map = {
    0: ((0, 1), (1, 1), (1, 0)),     # upper_left
    1: ((0, -1), (1, -1), (1, 0)),   # upper_right
    2: ((-1, 0), (-1, 1), (0, 1)),   # lower_left
    3: ((-1, 0), (0, -1), (-1, -1))  # lower_right
}


def clear_area(n, position, game):
    items_to_clear = clear_area_map[n]
    for item in items_to_clear:
        x = position[0] + item[0]
        y = position[1] + item[1]
        game.window.addstr(x, y, ' ')


def clear_area_around_keys(coordinates, game):
    positions = get_keys_positions(coordinates)
    for n, position in enumerate(positions):
        clear_area(n, position, game)

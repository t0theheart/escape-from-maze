

def compute_square(coordinates):
    vertical = coordinates[1] - coordinates[0]
    horizontal = coordinates[3] - coordinates[2]
    square = vertical * horizontal
    return square

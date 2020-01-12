from escape_from_maze.units import Enemy
import random


def get_enemies_area(coordinates):
    top = coordinates[0] + 3
    bottom = coordinates[1] - 2
    left = coordinates[2] + 3
    right = coordinates[3] - 3
    return top, bottom, left, right


def get_enemy_coordinates(top, bottom, left, right):
    x = random.randint(top, bottom)
    y = random.randint(left, right)
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y += 1
    return x, y


def generate_enemies(coordinates, window):
    enemies_area = get_enemies_area(coordinates)
    count = 50

    for n in range(count):
        x, y = get_enemy_coordinates(*enemies_area)
        Enemy(x, y, window)

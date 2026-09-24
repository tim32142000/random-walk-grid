import random

GRID_SIZE = 10

DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def step_people(people, grid_size=GRID_SIZE):
    new_people = []

    for row, col in people:
        dr, dc = random.choice(DIRECTION)

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
            new_people.append((new_row, new_col))

    return new_people


people = [(6, 6), (0, 0), (5, 5)]

for step in range(10):
    people = step_people(people)
    print(step + 1, people)

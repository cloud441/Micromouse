import numpy as np


def generateMap(height, width):
    lab_map = np.zeros((height, width))
    nb_wall = np.random.randint(0, 1000)
    x_positions = np.random.randint(0, 50, size=nb_wall)
    y_positions = np.random.randint(0, 50, size=nb_wall)

    for i in range(nb_wall):
        lab_map[x_positions[i], y_positions[i]] = 1

    return lab_map

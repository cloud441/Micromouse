import matplotlib.pyplot as plt
import numpy as np


class LabyrinthMap:

    def __init__(self, height=50, width=50):
        self.map = np.zeros((height, width))
        nb_wall = np.random.randint(0, 1000)
        x_positions = np.random.randint(0, 50, size=nb_wall)
        y_positions = np.random.randint(0, 50, size=nb_wall)

        for i in range(nb_wall):
            self.map[x_positions[i], y_positions[i]] = 1

    def flush(self):
        plt.matshow(self.map)
        plt.show()

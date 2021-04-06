import matplotlib.pyplot as plt

from Labyrinth.utils import generateMap

''' Class of random labyrinth generation. '''


class LabyrinthMap:

    def __init__(self, height=50, width=50):
        self.map = generateMap(height, width)

    ''' Flush the generated labyrinth. '''

    def flush(self):
        plt.matshow(self.map)
        plt.show()

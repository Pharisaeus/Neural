from math import exp
from pl.edu.agh.neural.learning.kohonen.neighbourhood.NeighbourhoodFunction import NeighbourhoodFunction

class GaussianNeighbourhoodFunction(NeighbourhoodFunction):
    NAME = "Gaussian neighbourhood function"

    def compute_value(self, distance, radius):
        return exp(- (distance ** 2) / (2 * radius ** 2))

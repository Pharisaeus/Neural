from pl.edu.agh.neural.learning.kohonen.topology.Topology import Topology

class RectangularTopology(Topology):
    NAME = "2D Rectangular Topology"

    def __init__(self, neighbourhood_function, initial_radius, rows, cols):
        super(RectangularTopology, self).__init__(neighbourhood_function, initial_radius)
        self.rows = rows
        self.cols = cols

    @staticmethod
    def create(*args):
        return RectangularTopology(args[0], args[1], args[2], args[3])

    def neighbours(self, neurons, chosen_neuron):
        center = neurons.index(chosen_neuron)
        neighbourhood = []
        for row in range(-self.radius, self.radius + 1):
            for col in range(-self.radius, self.radius + 1):
                position = center + row * self.cols + col
                if 0 <= position < len(neurons):
                    neighbourhood.append((neurons[position], self._neighbourhood_factor(max(abs(row), abs(col)))))
        return neighbourhood

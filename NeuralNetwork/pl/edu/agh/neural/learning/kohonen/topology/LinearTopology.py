from pl.edu.agh.neural.learning.kohonen.topology.Topology import Topology

class LinearTopology(Topology):
    NAME = "1D Topology"

    def __init__(self, neighbourhood_function, initial_radius):
        super(LinearTopology, self).__init__(neighbourhood_function, initial_radius)

    @staticmethod
    def create(*args):
        return LinearTopology(args[0], args[1])

    def neighbours(self, neurons, chosen_neuron):
        center = neurons.index(chosen_neuron)
        neighbourhood = [(chosen_neuron, 0)]
        for r in range(1, self.radius + 1):
            self._safe_append(neighbourhood, neurons, center + r, self._neighbourhood_factor(r))
            self._safe_append(neighbourhood, neurons, center - r, self._neighbourhood_factor(r))
        return neighbourhood

    def _safe_append(self, neighbourhood, list, index, value):
        if 0 <= index < len(list):
            neighbourhood.append((list[index], value))


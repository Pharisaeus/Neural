class Topology(object):
    def __init__(self, neighbourhood_function, initial_radius):
        self.neighbourhood_function = neighbourhood_function
        self.radius = initial_radius

    def neighbours(self, neurons, chosen_neuron):
        raise NotImplementedError("Subclass must implement abstract method")

    def _neighbourhood_factor(self, distance):
        return self.neighbourhood_function.compute_value(distance, self.radius)
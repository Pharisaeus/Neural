class ConscientiousNeuron(object):
    def __init__(self, neuron):
        self.neuron = neuron
        self.potential = 1

    def get_weights(self):
        return self.neuron.get_weights()

    def change_weight(self, input, value):
        edge = self.neuron.get_input_edge(input)
        edge.set_weight(edge.get_weight() + float(value))

    def adjust_potential(self, value):
        if self.potential + value < 1:
            self.potential += value

    def get_potential(self):
        return self.potential
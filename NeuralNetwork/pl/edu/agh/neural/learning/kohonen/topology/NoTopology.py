class NoTopology(object):
    def neighbours(self, neurons, chosen_neuron):
        return [(chosen_neuron, 1)]

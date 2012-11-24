class ConscienceUtil(object):
    @staticmethod
    def create_conscience(layer, potential_threshold=0):
        potential_step = 1.0 / len(layer)
        if potential_threshold > 0:
            return (lambda neuron: ConscienceUtil.evaluate(layer, potential_threshold, potential_step, neuron),
                    lambda neuron: neuron.get_potential() >= potential_threshold)
        else:
            return lambda neuron: None, lambda neuron: True

    @staticmethod
    def evaluate(layer, threshold, potential_step, chosen_neuron):
        for neuron in layer:
            if neuron is chosen_neuron:
                neuron.adjust_potential(-threshold)
            else:
                neuron.adjust_potential(potential_step)
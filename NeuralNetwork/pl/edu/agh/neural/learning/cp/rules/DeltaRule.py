from pl.edu.agh.neural.learning.cp.rules.AbstractLearningRule import AbstractLearningRule

class DeltaRule(AbstractLearningRule):
    NAME = "Delta Rule"

    def adjust_weight(self, neuron, input_number, factor, error, response):
        neuron.change_weight(input_number, factor * neuron.get_activator().derivative(response) * error)



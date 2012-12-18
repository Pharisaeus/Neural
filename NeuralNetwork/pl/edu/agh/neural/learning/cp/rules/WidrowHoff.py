from pl.edu.agh.neural.learning.cp.rules.AbstractLearningRule import AbstractLearningRule

class WidrowHoff(AbstractLearningRule):
    NAME = "Widrow-Hoff"

    def adjust_weight(self, neuron, input_number, factor, error, response):
        neuron.change_weight(input_number, factor * error)


class AbstractLearningRule(object):
    def adjust_weight(self, neuron, input_number, factor, error, response):
        raise NotImplementedError("Subclass must implement abstract method")
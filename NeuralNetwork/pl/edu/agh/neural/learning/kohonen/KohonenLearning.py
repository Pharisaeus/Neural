from pl.edu.agh.neural.learning.kohonen.ConscientiousNeuron import ConscientiousNeuron
from pl.edu.agh.neural.learning.kohonen.conscience.ConscienceUtil import ConscienceUtil

class KohonenLearning(object):
    def __init__(self, layer, topology, metric, learning_factor, conscience_threshold):
        self.layer = [ConscientiousNeuron(neuron) for neuron in layer.get_neurons()]
        self.topology = topology
        self.metric = metric
        self.learning_factor = learning_factor
        self.conscience_evaluator, self.conscience_function = ConscienceUtil.create_conscience(self.layer,
            conscience_threshold)

    def learn(self, input_data, iterations):
        for iteration in range(iterations):
            for data in input_data:
                closest_neuron = self._find_closest_neuron(data)
                neighbourhood = self.topology.neighbours(self.layer, closest_neuron)
                for neuron, neighbourhood_factor in neighbourhood:
                    self._change_weight(neuron, data, iteration, neighbourhood_factor)
                self.conscience_evaluator(closest_neuron)

    def _find_closest_neuron(self, data):
        return min([(self.metric.compute_distance(data, neuron.get_weights()), neuron)
                    for neuron in self.layer if self.conscience_function(neuron)])[1]

    def _change_weight(self, neuron, data, iteration, neighbourhood_factor):
        weights = neuron.get_weights()
        for i in range(len(data)):
            neuron.change_weight(i,
                self.learning_factor.compute_factor(iteration) *
                neighbourhood_factor *
                (data[i] - weights[i])
            )

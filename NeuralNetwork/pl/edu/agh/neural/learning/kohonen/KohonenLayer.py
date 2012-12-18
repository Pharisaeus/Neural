from pl.edu.agh.neural.NeuronsLayer import NeuronsLayer
from pl.edu.agh.neural.learning.kohonen.metrics.EuclideanMetric import EuclideanMetric

class KohonenLayer(NeuronsLayer):
    NAME = "Kohonen Layer"

    #    def calculate_response(self):
    #        super(KohonenLayer, self).calculate_response()
    #        closest_neuron = max([(neuron.get_value(), neuron) for neuron in self.neurons])[1]
    #        for neuron in self.neurons:
    #            neuron.set_value(neuron is closest_neuron)
    #

    def calculate_response(self, input_data):
        super(KohonenLayer, self).calculate_response(input_data)

        closest_neuron = min([(EuclideanMetric().compute_distance(input_data, neuron.get_weights()), neuron)
                              for neuron in self.neurons])[1]
        for neuron in self.neurons:
            neuron.set_value(neuron is closest_neuron)

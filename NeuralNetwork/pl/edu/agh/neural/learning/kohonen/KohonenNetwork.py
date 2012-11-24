from pl.edu.agh.neural.Network import Network

class KohonenNetwork(Network):
    def __init__(self, network, metric):
        super(KohonenNetwork, self).__init__([])
        self.add_layer(network.get_layer(0))
        self.inputs = network.inputs
        self.metric = metric

    def calculate_network_response(self, input_data):
        neurons = self.layers[0].get_neurons()
        closest_neuron = min([(self.metric.compute_distance(input_data, neuron.get_weights()), neuron)
                              for neuron in neurons])[1]
        return [1 if neuron is closest_neuron else 0 for neuron in neurons]

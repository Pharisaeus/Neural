from pl.edu.agh.neural.Layers import Layers
from pl.edu.agh.neural.Network import Network
from pl.edu.agh.neural.Neuron import Neuron
from pl.edu.agh.neural.activators.ActivatorUtil import ActivatorUtil
from pl.edu.agh.neural.edges.Input import Input
from pl.edu.agh.neural.psp.PSPUtil import PSPUtil

class NetworkCreator(object):
    def create_network(self, network_model):
        inputs = self._create_inputs(network_model.network_inputs())
        network = Network(inputs)
        for layer in network_model.layers():
            new_layer = self._create_layer(layer)
            network.add_layer(new_layer)
            self._set_weights(new_layer, layer)
        return network

    def _create_inputs(self, inputs):
        return [Input() for _ in range(inputs)]

    def _create_layer(self, standard_layer_data):
        layer = Layers.create_layer(standard_layer_data.layer_type())
        layer_data = standard_layer_data.get_neurons_data()
        for neuron_data in layer_data:
            layer.add_neuron(Neuron(
                PSPUtil.get_psp(neuron_data[0]),
                ActivatorUtil.get_activator(neuron_data[1]),
                float(neuron_data[2]))
            )
        return layer

    def _set_weights(self, layer, layer_data):
        weights = layer_data.get_weights()
        for neuron_number in range(0, len(weights)):
            for input_number in range(0, len(weights[neuron_number])):
                layer.set_edge_weight(neuron_number, input_number, weights[neuron_number][input_number])

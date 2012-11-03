from pl.edu.agh.neural.Network import Network
from pl.edu.agh.neural.Neuron import Neuron
from pl.edu.agh.neural.NeuronsLayer import NeuronsLayer
from pl.edu.agh.neural.activators.ActivatorUtil import ActivatorUtil
from pl.edu.agh.neural.edges.Input import Input
from pl.edu.agh.neural.psp.PSPUtil import PSPUtil

class NetworkCreator(object):
    def create_network(self, layers_data):
        inputs = self._create_inputs(layers_data[0])
        network = Network(inputs)
        for layer_index in range(1, len(layers_data)):
            layer = layers_data[layer_index]
            new_layer = self._create_layer(layer)
            network.add_layer(new_layer)
            self._set_weights(new_layer, layer)
        return network

    def _create_inputs(self, inputs):
        return [Input() for _ in range(inputs)]

    def _create_layer(self, standard_layer_data):
        layer = NeuronsLayer()
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
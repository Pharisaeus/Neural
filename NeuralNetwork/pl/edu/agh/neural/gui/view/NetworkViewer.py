from PyQt4.QtGui import QGraphicsScene
from pl.edu.agh.neural.gui.view.EdgeItem import EdgeItem
from pl.edu.agh.neural.gui.view.NeuronItem import NeuronItem

class NetworkViewer(QGraphicsScene):
    def __init__(self, *__args):
        QGraphicsScene.__init__(self, *__args)
        self.layer_width = 200
        self.layer_height = 500
        self.neurons_positions = {}
        self.addText("Neural Networks Simulator\nv. 0.4")

    def show_network(self, network):
        self._draw_inputs(network.inputs)
        layer_number = 2
        for layer in network.layers:
            self._draw_neurons_layer(layer, layer_number)
            layer_number += 1
        self.setSceneRect(self.itemsBoundingRect().adjusted(-10, -10, 10, 10))

    def _draw_inputs(self, inputs):
        neuron_height = self._compute_neuron_height(len(inputs))
        input_number = 1
        for input in inputs:
            self._draw_input_neuron(input, input_number, neuron_height, 1)
            input_number += 1
            self._draw_input_edge(self.neurons_positions[input])

    def _draw_input_edge(self, input):
        self.addItem(EdgeItem((input[0] - 100, input[1]), input))

    def _draw_neurons_layer(self, layer, layer_number):
        neuron_height = self._compute_neuron_height(len(layer.neurons))
        neuron_number = 1
        for neuron in layer.neurons:
            self._draw_neuron(neuron, neuron_number, neuron_height, layer_number)
            self._draw_connections(neuron)
            neuron_number += 1

    def _draw_input_neuron(self, neuron, neuron_number, neuron_height, layer_number):
        position = self._compute_position(neuron, neuron_number, neuron_height, layer_number)
        self.addItem(NeuronItem(position))

    def _draw_neuron(self, neuron, neuron_number, neuron_height, layer_number):
        position = self._compute_position(neuron, neuron_number, neuron_height, layer_number)
        self.addItem(NeuronItem(position, neuron.get_bias().get_weight()))

    def _compute_position(self, neuron, neuron_number, neuron_height, layer_number):
        position = layer_number * self.layer_width, neuron_number * neuron_height
        self.neurons_positions[neuron] = position
        return position

    def _draw_connections(self, neuron):
        for input in neuron.get_inputs():
            self.addItem(EdgeItem(self.neurons_positions[input.input_source],
                self.neurons_positions[neuron], input.get_weight()))

    def _compute_neuron_height(self, neurons_count):
        return self.layer_height / (neurons_count + 1)

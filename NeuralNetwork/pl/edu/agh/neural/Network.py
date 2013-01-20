"""
Implementation of neural network
"""
from pl.edu.agh.neural.utils.DataNormalizer import DataNormalizer

class Network(object):
    """
    Implementation of neural network
        :param inputs: list of network inputs
        :type inputs: list
    """

    def __init__(self, inputs):
        self.inputs = inputs
        self.layers = []

    def calculate_network_response(self, input_data):
        """
        Method used to calculate response of network based on given input signals
            :param input_data: list of signals that should be placed as input
            :type input_data: list
            :return: list of response signals
            :rtype: list
        """
        self.set_input_data(input_data)
        for layer in self.layers:
            layer.calculate_response(input_data)
        return self.layers[-1].fetch_response()

    def set_input_data(self, input_data):
        input_data = DataNormalizer.normalize([input_data])[0]
        for input, input_value in zip(self.inputs, input_data):
            input.set_value(input_value)

    def add_input(self, new_input):
        """
        Method used to add new input to network
                :param new_input: new input for the network, that should be connected with all neurons in first layer
                :type new_input: Input
        """
        self.inputs.append(new_input)

    def add_layer(self, new_layer):
        """
        Method used to add new layer to this network
            :param new_layer: new layer that should be placed at the end of network
            :type new_layer: NeuronsLayer
        """
        if len(self.layers) == 0:
            new_layer.set_inputs(self.inputs)
        else:
            new_layer.set_inputs(self.layers[-1].get_neurons())
        self.layers.append(new_layer)

    def add_neuron_to_layer(self, layer_number, new_neuron):
        """
        Method used to add new neuron to given neurons layer
            :param layer_number: number of layer where new neuron should be placed
            :type layer_number: int
            :param new_neuron: neuron that we are adding
            :type new_neuron: Neuron
        """
        self.layers[layer_number].add_neuron(new_neuron)
        if layer_number < len(self.layers):
            self.layers[layer_number + 1].add_input(new_neuron)

    def get_layer(self, number):
        """
        Method used to access selected layer
                :param number: number of layer we want to access
                :type number: int
                :return: selected layer
                :rtype: NeuronsLayer
                """
        return self.layers[number]

    def get_layers(self):
        return self.layers

    def inputs_count(self):
        return len(self.inputs)

    def get_inputs(self):
        return self.inputs

    def enable_bias(self):
        for layer in self.get_layers():
            layer.enable_bias()

    def disable_bias(self):
        for layer in self.get_layers():
            layer.disable_bias()
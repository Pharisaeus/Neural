"""
Implementation of single layer of neurons
"""
from pl.edu.agh.neural.edges.Edge import Edge
import random

class NeuronsLayer(object):
    """
    Implementation of single layer of neurons
    """
    NAME = "General layer"

    def __init__(self):
        self.neurons = []

    def calculate_response(self, input):
        """
        Method used to calculate response of this layer
                :return: list of float values that are responses of every neuron in layer
                :rtype: list
        """
        for neuron in self.neurons:
            neuron.calculate_value()

    def fetch_response(self):
        return [neuron.get_value() for neuron in self.neurons]

    def add_neuron(self, new_neuron):
        """
        Method used to add new neuron to this layer
                :param new_neuron: new neuron for this layer
                :type new_neuron: Neuron
        """
        self.neurons.append(new_neuron)

    def add_input_neuron(self, input_neuron):
        """
        Method used to add new input for this layer
            :param input_neuron: new input neuron
            :type input_neuron: AbstractInput
        """
        for neuron in self.neurons:
            neuron.add_input(Edge(input_neuron, random.random()))

    def set_inputs(self, new_inputs):
        """
        Method used to set new set of inputs for this layer
            :param new_inputs: inputs list that should replace old one
            :type new_inputs: list
        """
        for new_input in new_inputs:
            self.add_input_neuron(new_input)

    def set_edge_weight(self, neuron, edge, new_weight):
        """
        Method used to set edge weight for selected edge
                :param neuron: number of neuron we want to access
                :type neuron: int
                :param edge: number of edge from neuron we want to access
                :type edge: int
                :param new_weight: new weight of this edge
                :type new_weight: float
        """
        self.neurons[neuron].get_input_edge(edge).set_weight(new_weight)

    def set_bias_weight(self, neuron, new_weight):
        """
        Method used to set new weight for bias edge for selected neuron
                :param neuron: number of neuron we want to access
                :type neuron: int
                :param new_weight: new weight of bias connection for neuron
                :type new_weight: float
        """
        self.neurons[neuron].get_bias().set_weight(new_weight)

    def get_neurons(self):
        """
        Method used to access all neurons from this layer
                :return: list of Neuron objects
                :rtype: list
        """
        return self.neurons

    def get_neuron(self, number):
        """
        Method used to access selected neuron from this layer
                :param number: number of neuron we want to access
                :type number: int
                :return: selected neuron
                :rtype: Neuron
        """
        return self.neurons[number]

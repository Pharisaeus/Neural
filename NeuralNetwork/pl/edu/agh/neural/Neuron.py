"""
Implementation of neuron
"""
from pl.edu.agh.neural.edges.AbstractInput import AbstractInput
from pl.edu.agh.neural.edges.Bias import Bias

class Neuron(AbstractInput):
    """
    Implementation of neuron
        :param psp: post synaptic potential function object
        :type psp: AbstractPSP
        :param activator: activator function object
        :type activator: Activator
        :param bias: bias input object
        :type bias: float
    """

    def __init__(self, psp, activator, bias):
        self.psp = psp
        self.activator = activator
        self.inputs = []
        self.bias = Bias(bias)

    def add_input(self, new_input):
        """
        Method used to add new input for this layer
                :param new_input: new input for this neuron
                :type new_input: Input
        """
        self.inputs.append(new_input)

    def clear_inputs(self):
        """
        Method used to remove all inputs from this layer
        :rtype: None
        """
        self.inputs = []

    def get_bias(self):
        """
        Method used to access bias of this layer
                :return: bias node
                :rtype: Bias
        """
        return self.bias

    def get_input_edge(self, number):
        """
        Method used to access selected input edge of this layer
                :param number: number of input edge we want to access
                :type number: int
                :return: selected input edge
                :rtype: Input
                """
        return self.get_inputs()[number]

    def get_inputs(self):
        return self.inputs + [self.bias]

    def calculate_value(self):
        """
        Method used to precalculate value of this neuron
            :return: None
            :rtype: float
        """
        self.value = self.activator.calculate_response(self.get_psp_value())

    def get_value(self):
        """
        Method used to collect response value from this neuron
                :return: response value of this neuron
                :rtype: float
        """
        return self.value

    def set_value(self, value):
        self.value = value

    def get_psp(self):
        return self.psp

    def get_psp_value(self):
        return self.psp.calculate_potential(self.get_inputs())

    def get_activator(self):
        return self.activator

    def get_weights(self):
        return [input.get_weight() for input in self.get_inputs()]

    def change_weight(self, input, value):
        edge = self.get_input_edge(input)
        edge.set_weight(edge.get_weight() + float(value))

    def enable_bias(self):
        self.get_bias().enable()

    def disable_bias(self):
        self.get_bias().disable()

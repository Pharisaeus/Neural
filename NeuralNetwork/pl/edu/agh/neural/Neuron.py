from pl.edu.agh.neural.edges.AbstractInput import AbstractInput
from pl.edu.agh.neural.edges.Bias import Bias

class Neuron(AbstractInput):

    def __init__(self, psp, activator):
        '''
        :param psp: object responsible for calculating post-synaptic-potential
        :param activator: object responsible for calculating activation funtion
        '''
        self.psp = psp
        self.activator = activator
        self.inputs = []
        self.bias = Bias(0)
        
    def add_input(self, new_input):
        self.inputs.append(new_input)
        
    def clear_inputs(self):
        self.inputs = []
        
    def get_bias(self):
        return self.bias
        
    def get_input_edge(self, number):
        return self.inputs[number]
        
    def get_value(self):
        return self.activator.calculate_response(self.psp.calculate_potential(self.inputs + [self.bias]))

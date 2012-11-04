from pl.edu.agh.neural.edges.Edge import Edge
import random

class NeuronsLayer(object):

    def __init__(self):
        self.neurons = []
        
    def calculate_response(self):
        return [neuron.get_value() for neuron in self.neurons]
    
    def add_neuron(self, new_neuron):
        self.neurons.append(new_neuron)
            
    def add_input_neuron(self, input_neuron):
        for neuron in self.neurons:
            neuron.add_input(Edge(input_neuron, random.random()))
                
    def set_inputs(self, new_inputs):
        for new_input in new_inputs:
            self.add_input_neuron(new_input)
                
    def set_edge_weight(self, neuron, edge, new_weight):
        self.neurons[neuron].get_input_edge(edge).set_weight(new_weight)

    def set_bias_weight(self, neuron, new_weight):
        self.neurons[neuron].get_bias().set_weight(new_weight)

    def get_neurons(self):
        return self.neurons
    
    def get_neuron(self, number):
        return self.neurons[number]

class Network(object):

    def __init__(self, inputs):
        self.inputs = inputs
        self.layers = []

    def calculate_network_response(self, input_data):
        for input, input_value in zip(self.inputs, input_data):
            input.set_value(input_value)
        return self.layers[-1].calculate_response()
    
    def add_input(self, new_input):
        self.inputs.append(new_input)
    
    def add_layer(self, new_layer):
        if len(self.layers) == 0:
            new_layer.set_inputs(self.inputs)
        else:
            new_layer.set_inputs(self.layers[-1].get_neurons())
        self.layers.append(new_layer)
        
    def add_neuron_to_layer(self, layer_number, new_neuron):
        self.layers[layer_number].add_neuron(new_neuron)
        if layer_number < len(self.layers):
            self.layers[layer_number + 1].add_input(new_neuron)
            
    def get_layer(self, number):
        return self.layers[number]

    def get_layers(self):
        return self.layers

    def inputs_count(self):
        return len(self.inputs)

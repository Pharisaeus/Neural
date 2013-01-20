from pl.edu.agh.neural.utils.DataNormalizer import DataNormalizer

class BackpropagationLearning(object):
    def __init__(self, network, error_metric, learning_factor, momentum, bias_enabled):
        self.network = network
        if bias_enabled:
            self.network.enable_bias()
        else:
            self.network.disable_bias()
        self.error_metric = error_metric
        self.learning_factor = learning_factor
        self.momentum = momentum
        self.previous_weights = []

    def learn(self, learning_data, iterations):
        input_data, output_data = self.extract_data(learning_data)
        self.initialize_previous_weights()
        for iteration in range(iterations):
            error = 0.0
            for i in range(len(input_data)):
                network_response = self.network.calculate_network_response(input_data[i])
                error += self.back_propagate(output_data[i], network_response)
        return error

    def initialize_previous_weights(self):
        self.previous_weights = [[self.network.get_layer(i).get_neurons()[j].get_weights() for j in
                                  range(len(self.network.get_layer(i).get_neurons()))] for i in
                                 range(len(self.network.get_layers()))]

    def back_propagate(self, expected_outputs, network_response):
        deltas = self.calculate_deltas(expected_outputs)
        self.update_weights(deltas)
        return self.error_metric.calculate_error(expected_outputs, network_response)

    def calculate_deltas(self, expected_outputs):
        output_layer = self.network.get_layer(len(self.network.get_layers()) - 1)
        deltas = [
            [self.output_delta(neuron, expected_outputs[i]) for i, neuron in enumerate(output_layer.get_neurons())]]
        for i in range(len(self.network.get_layers()) - 2, -1, -1): #form last layer
            layer = self.network.get_layers()[i]
            layer_neuron_deltas = []
            for j in range(len(layer.get_neurons())):
                neuron = layer.get_neurons()[j]
                next_layer_neurons = (self.network.get_layers()[i + 1]).get_neurons()
                next_layer_weights = [next_layer_neuron.get_weights()[j] for next_layer_neuron in
                                      next_layer_neurons]
                layer_neuron_deltas.append(self.hidden_delta(neuron, next_layer_weights, deltas[0]))
            deltas.insert(0,layer_neuron_deltas)
        return deltas

    def update_weights(self, deltas):
        for i, layer in enumerate(self.network.get_layers()):
            for j, neuron in enumerate(layer.get_neurons()):
                for weight in range(len(neuron.get_weights())):
                    delta_part = self.learning_factor * deltas[i][j] * neuron.get_inputs()[weight].get_value()
                    momentum_part = self.momentum * (neuron.get_weights()[weight] - self.previous_weights[i][j][weight])
                    self.previous_weights[i][j][weight] = neuron.get_weights()[weight] #update previous weight
                    neuron.change_weight(weight,delta_part + momentum_part)

    def output_delta(self, neuron, expected_output):
        ekj = neuron.get_psp_value()
        activator_derivative = neuron.get_activator().derivative(ekj)
        return activator_derivative * (expected_output - neuron.get_value())

    def hidden_delta(self, neuron, next_layer_weights, next_layer_deltas):
        ekj = neuron.get_psp_value()
        activator_derivative = neuron.get_activator().derivative(ekj)
        return activator_derivative * sum(
            [next_layer_weights[i] * next_layer_deltas[i] for i in range(len(next_layer_weights))])

    def extract_data(self, learning_data):
        inputs_count = self.network.inputs_count()
        outputs_count = len(learning_data[0])
        input_data = [[case[i]  for i in range(inputs_count)]  for case in learning_data]
        output_data = [[case[i] for i in range(inputs_count, outputs_count)] for case in learning_data]
        return input_data, output_data
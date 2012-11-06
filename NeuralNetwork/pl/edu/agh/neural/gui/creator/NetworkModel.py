from pl.edu.agh.neural.gui.creator.LayerModel import LayerModel

class NetworkModel(object):
    DEFAULT_NEURONS_COUNT = 2
    DEFAULT_INPUT_NEURONS_COUNT = 2

    def __init__(self, empty=False):
        self.input_neurons = NetworkModel.DEFAULT_INPUT_NEURONS_COUNT
        self.layers_data = []
        if not empty:
            self.add_layer()

    def layers(self):
        return self.layers_data

    def add_layer(self):
        layer_name = self._layer_name(len(self.layers_data) + 1)
        input_neurons = self.input_neurons
        if len(self.layers_data) != 0:
            input_neurons = self.layers_data[-1].rowCount()
        layer_model = LayerModel(layer_name, NetworkModel.DEFAULT_NEURONS_COUNT, input_neurons)
        self.layers_data.append(layer_model)
        return layer_model

    def remove_layer(self):
        del self.layers_data[-1]

    def set_network_input_neurons(self, neurons_number):
        self.input_neurons = neurons_number
        if len(self.layers_data) != 0:
            self.layers_data[0].set_input_neurons(neurons_number)

    def set_neurons_for_layer(self, layer_index, neurons_number):
        self.layers_data[layer_index].set_neurons(neurons_number)
        if layer_index != len(self.layers_data) - 1:
            self.layers_data[layer_index + 1].set_input_neurons(neurons_number)

    def layer_model(self, layer_number):
        return self.layers_data[layer_number]

    def default_layer(self):
        return self.layers_data[0]

    def network_inputs(self):
        return self.input_neurons

    def _layer_name(self, layer_number):
        return str(layer_number) + " layer"

    @staticmethod
    def from_network(network):
        model = NetworkModel(empty=True)
        model.set_network_input_neurons(network.inputs_count())
        for layer in network.get_layers():
            layer_model = model.add_layer()
            neurons = layer.get_neurons()
            layer_model.set_neurons(len(neurons))
            for neuron_index in range(len(neurons)):
                neuron = neurons[neuron_index]
                layer_model.set_psp_for_neuron(neuron_index, neuron.get_psp().NAME)
                layer_model.set_activation_for_neuron(neuron_index, neuron.get_activator().NAME)
                layer_model.set_bias_for_neuron(neuron_index, neuron.get_bias().get_weight())
                inputs = neuron.get_inputs()
                for input_index in range(len(inputs)):
                    layer_model.set_weight_for_connection(neuron_index, input_index, neuron.get_input_edge(input_index).get_weight())
        return model

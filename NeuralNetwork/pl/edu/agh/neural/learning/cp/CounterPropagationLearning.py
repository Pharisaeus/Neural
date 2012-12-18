from pl.edu.agh.neural.utils.DataNormalizer import DataNormalizer

class CounterPropagationLearning(object):
    def __init__(self, network, learning_rule, learning_factor, kohonen_learning):
        self.network = network
        self.kohonen_learning = kohonen_learning
        self.learning_factor = learning_factor
        self.learning_rule = learning_rule

    def learn(self, kohonen_iterations, grossberg_iterations, learning_data):
        inputs_count = self.network.inputs_count()
        outputs_count = len(learning_data[0])
        input_data = DataNormalizer.normalize([[case[i]  for i in range(inputs_count)]  for case in learning_data])
        output_data = [[case[i] for i in range(inputs_count, outputs_count)] for case in learning_data]

        self.kohonen_learning.learn(input_data, kohonen_iterations)
        self.grossberg_layer_learning(grossberg_iterations, input_data, output_data)

    def grossberg_layer_learning(self, iterations, input_data, output_data):
        output_neurons = self.network.get_layer(1).get_neurons()
        kohonen_layer = self.network.get_layer(0)
        for iteration in range(iterations):
            factor = self.learning_factor.compute_factor(iteration)
            for case in zip(input_data, output_data):
                response = self.network.calculate_network_response(case[0])
                kohonen_response = kohonen_layer.fetch_response().index(1)
                for i in range(len(output_neurons)):
                    error = case[1][i] - response[i]
                    self.learning_rule.adjust_weight(output_neurons[i], kohonen_response, factor, error, response[i])

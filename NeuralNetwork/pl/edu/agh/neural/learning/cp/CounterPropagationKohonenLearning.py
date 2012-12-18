from pl.edu.agh.neural.learning.kohonen.KohonenLearning import KohonenLearning

class CounterPropagationKohonenLearning(KohonenLearning):
    def __init__(self, layer, topology, metric, learning_factor, conscience_threshold):
        super(CounterPropagationKohonenLearning, self).__init__(layer, topology, metric, learning_factor,
            conscience_threshold)

    def learn(self, input_data, iterations):
        step = 1.0 / iterations
        alfa = 0
        initial_weight = (1.0 / len(self.layer)) ** 0.5
        for iteration in range(iterations):
            alfa += step
            for data in input_data:
                data = [alfa * x + (1 - alfa) * initial_weight for x in data]
                closest_neuron = self._find_closest_neuron(data)
                neighbourhood = self.topology.neighbours(self.layer, closest_neuron)
                for neuron, neighbourhood_factor in neighbourhood:
                    self._change_weight(neuron, data, iteration, neighbourhood_factor)
                self.conscience_evaluator(closest_neuron)
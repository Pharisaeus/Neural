from random import  uniform
from PyQt4.QtGui import QStandardItemModel
from pl.edu.agh.neural.activators.ActivatorUtil import ActivatorUtil
from pl.edu.agh.neural.psp.PSPUtil import PSPUtil

class LayerModel(QStandardItemModel):
    DEFAULT_HEADER = ["PSP", "Activation", "Bias"]

    def __init__(self, name, layer_type, neurons_count, inputs, minWeight, maxWeight, *__args):
        QStandardItemModel.__init__(self, *__args)
        self.setHorizontalHeaderLabels(LayerModel.DEFAULT_HEADER)
        self.name = name
        self.type = layer_type
        self.minWeight = minWeight
        self.maxWeight = maxWeight
        self.set_neurons(neurons_count)
        self.set_input_neurons(inputs)

    def set_layer_type(self, value):
        self.type = value

    def layer_type(self):
        return self.type

    def set_neurons(self, size):
        old_row_count = self.rowCount()
        self.setRowCount(size)
        for i in range(old_row_count, size):
            self._create_neuron(i)

    def set_input_neurons(self, size):
        old_columns_count = self.columnCount()
        self.setColumnCount(len(LayerModel.DEFAULT_HEADER) + size)
        self.setHorizontalHeaderLabels(
            LayerModel.DEFAULT_HEADER + ["Input neuron " + str(i) for i in range(1, size + 1)])
        for column in range(old_columns_count, self.columnCount()):
            for row in range(self.rowCount()):
                self.setData(self.index(row, column), self._random_input_weight())

    def set_default_psp(self, psp):
        for row in range(self.rowCount()):
            self.set_psp_for_neuron(row, psp)

    def set_default_activation(self, activation):
        for row in range(self.rowCount()):
            self.set_activation_for_neuron(row, activation)

    def _create_neuron(self, row):
        self.setData(self.index(row, 0), PSPUtil.default_psp())
        self.setData(self.index(row, 1), ActivatorUtil.default_activator())
        self.setData(self.index(row, 2), 0.0)
        for i in range(3, self.columnCount()):
            self.setData(self.index(row, i), self._random_input_weight())

    def _random_input_weight(self):
        return round(uniform(self.minWeight, self.maxWeight), 3)

    def get_neurons_data(self):
        return [[str(self.item(row, column).text()) for column in range(len(LayerModel.DEFAULT_HEADER))] for row in
                range(self.rowCount())]

    def get_weights(self):
        return [
        [float(self.item(row, column).text()) for column in range(len(LayerModel.DEFAULT_HEADER), self.columnCount())]
        for row in
        range(self.rowCount())]

    def layer_name(self):
        return self.name

    def set_psp_for_neuron(self, neuron_index, psp):
        self.setData(self.index(neuron_index, 0), psp)

    def set_activation_for_neuron(self, neuron_index, activation):
        self.setData(self.index(neuron_index, 1), activation)

    def set_bias_for_neuron(self, neuron_index, bias):
        self.setData(self.index(neuron_index, 2), bias)

    def set_weight_for_connection(self, neuron_index, input_index, weight):
        self.setData(self.index(neuron_index, input_index + 3), weight)

    def randomize_weights(self, min, max):
        self.minWeight = min
        self.maxWeight = max
        for row in range(self.rowCount()):
            for column in range(len(LayerModel.DEFAULT_HEADER), self.columnCount()):
                self.setData(self.index(row, column), self._random_input_weight())


from random import random
from PyQt4.QtGui import QStandardItemModel
from pl.edu.agh.neural.activators.ActivatorUtil import ActivatorUtil
from pl.edu.agh.neural.psp.PSPUtil import PSPUtil

class LayerModel(QStandardItemModel):
    def __init__(self, neurons_count, inputs, *__args):
        QStandardItemModel.__init__(self, *__args)
        self.default_header = ["PSP", "Activation", "Bias"]
        self.setHorizontalHeaderLabels(self.default_header)
        self.set_neurons(neurons_count)
        self.set_input_neurons(inputs)

    def set_neurons(self, size):
        old_row_count = self.rowCount()
        self.setRowCount(size)
        for i in range(old_row_count, size):
            self._create_neuron(i)

    def set_input_neurons(self, size):
        old_columns_count = self.columnCount()
        self.setColumnCount(len(self.default_header) + size)
        self.setHorizontalHeaderLabels(self.default_header + ["Input neuron " + str(i) for i in range(1, size + 1)])
        for column in range(old_columns_count, self.columnCount()):
            for row in range(0, self.rowCount()):
                self.setData(self.index(row, column), self._random_input_weight())

    def set_default_psp(self, psp):
        for row in range(self.rowCount()):
            self.setData(self.index(row, 0), psp)

    def set_default_activation(self, activation):
        for row in range(self.rowCount()):
            self.setData(self.index(row, 1), activation)

    def _create_neuron(self, row):
        self.setData(self.index(row, 0), PSPUtil.default_psp())
        self.setData(self.index(row, 1), ActivatorUtil.default_activator())
        self.setData(self.index(row, 2), str(0))
        for i in range(3, self.columnCount()):
            self.setData(self.index(row, i), self._random_input_weight())

    def _random_input_weight(self):
        return str(round(random(), 3))

    def get_neurons_data(self):
        return [[str(self.item(row, column).text()) for column in range(0, len(self.default_header))] for row in
                range(self.rowCount())]

    def get_weights(self):
        return [[float(self.item(row, column).text()) for column in range(len(self.default_header), self.columnCount())]
                for row in
                range(self.rowCount())]

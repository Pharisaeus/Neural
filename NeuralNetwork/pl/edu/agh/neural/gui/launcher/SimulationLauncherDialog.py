from random import random
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QStandardItemModel, QMessageBox
from pl.edu.agh.neural.gui.launcher.SimulationLauncherUi import Ui_SimulationLauncher

class SimulationLauncherDialog(QDialog):
    def __init__(self, network, test_data):
        QDialog.__init__(self)

        self.ui = Ui_SimulationLauncher()
        self.ui.setupUi(self)

        self.network = network
        inputs_count = len(network.inputs)
        self.input_data = test_data or self._setup_data_model(inputs_count)
        self.ui.dataView.setModel(self.input_data)

        outputs_count = len(network.layers[-1].neurons)
        self.output_data = self._setup_data_model(outputs_count)
        self.ui.outputView.setModel(self.output_data)

        self._setup_headers(inputs_count, outputs_count)
        self.ui.testsCountSpinBox.setValue(self.input_data.rowCount())

    def _setup_data_model(self, columns_count):
        data = QStandardItemModel()
        data.setColumnCount(columns_count)
        data.setRowCount(self.ui.testsCountSpinBox.value())
        return data

    def _setup_headers(self, inputs_count, outputs_count):
        self.input_data.setHorizontalHeaderLabels(["Input " + str(i) for i in range(inputs_count)])
        self.output_data.setHorizontalHeaderLabels(["Output " + str(i) for i in range(outputs_count)])

    @pyqtSlot()
    def on_runButton_clicked(self):
        if not self._check_input():
            QMessageBox.warning(None, "Error", "Input data is invalid")
        else:
            inputs = self._get_input()
            for row_index in range(len(inputs)):
                row = inputs[row_index]
                response = self.network.calculate_network_response(row)
                for i in range(len(response)):
                    self.output_data.setData(self.output_data.index(row_index, i), round(response[i], 3))

    def _check_input(self):
        for column in range(self.input_data.columnCount()):
            for row in range(self.input_data.rowCount()):
                if self.input_data.item(row, column) is None:
                    return False
        return True

    def _get_input(self):
        return [[float(self.input_data.item(row, column).text())
                 for column in range(self.input_data.columnCount())]
                for row in range(self.input_data.rowCount())]

    def get_model(self):
        return self.input_data

    @pyqtSlot()
    def on_generateRandomButton_clicked(self):
        for row in range(self.input_data.rowCount()):
            for column in range(self.input_data.columnCount()):
                self.input_data.setData(self.input_data.index(row, column), round(random(), 3))

    @pyqtSlot(int)
    def on_testsCountSpinBox_valueChanged(self, value):
        self.input_data.setRowCount(value)
        self.output_data.setRowCount(value)

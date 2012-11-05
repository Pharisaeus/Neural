from random import random
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QStandardItemModel, QMessageBox, QFileDialog
from pl.edu.agh.neural.gui.launcher.SimulationLauncherUi import Ui_SimulationLauncher

class SimulationLauncherDialog(QDialog):
    def __init__(self, network):
        QDialog.__init__(self)

        self.ui = Ui_SimulationLauncher()
        self.ui.setupUi(self)

        self.network = network
        inputs_count = len(network.inputs)
        outputs_count = len(network.layers[-1].neurons)
        self.input_data = self._setup_data_model(inputs_count)
        self.output_data = self._setup_data_model(outputs_count)
        self._setup_headers(inputs_count, outputs_count)

        self.ui.dataView.setModel(self.input_data)
        self.ui.outputView.setModel(self.output_data)

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
                    self.output_data.setData(self.output_data.index(row_index, i), str(response[i]))

    @pyqtSlot()
    def on_readFileButton_clicked(self):
        filePath = QFileDialog().getOpenFileName(None,"Select input data file")
        try:
            with open(filePath,"r") as file:
                file_lines = file.readlines()
                rows_count = len(file_lines)
                self.ui.testsCountSpinBox.setValue(rows_count)
                for (line,row) in zip(file_lines,range(rows_count)):
                    for (value,column) in zip(line.split(),range(self.input_data.columnCount())):
                        self.input_data.setData(self.input_data.index(row, column),float(value))
        except Exception as e:
            print e

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

    @pyqtSlot()
    def on_generateRandomButton_clicked(self):
        for row in range(self.input_data.rowCount()):
            for column in range(self.input_data.columnCount()):
                self.input_data.setData(self.input_data.index(row, column), round(random(), 3))

    @pyqtSlot(int)
    def on_testsCountSpinBox_valueChanged(self, value):
        self.input_data.setRowCount(value)
        self.output_data.setRowCount(value)

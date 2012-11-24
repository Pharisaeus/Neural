from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QMessageBox, QFileDialog
from pl.edu.agh.neural.gui.common.DataView import DataView
from pl.edu.agh.neural.gui.launcher.SimulationLauncherUi import Ui_SimulationLauncher

class SimulationLauncherDialog(QDialog):
    def __init__(self, network, test_data):
        QDialog.__init__(self)

        self.ui = Ui_SimulationLauncher()
        self.ui.setupUi(self)

        self.network = network

        inputs_count = len(network.inputs)
        self.input_view = DataView(self.ui.dataView, model=test_data, header="Input", columns=inputs_count)

        outputs_count = len(network.layers[-1].neurons)
        self.output_view = DataView(self.ui.outputView, header="Output", columns=outputs_count)

        self.ui.testsCountSpinBox.setValue(self.input_view.row_count())

    @pyqtSlot()
    def on_runButton_clicked(self):
        if not self.input_view.check_data():
            QMessageBox.warning(None, "Error", "Input data is invalid")
        else:
            inputs = self.input_view.get_data()
            for row_index in range(len(inputs)):
                row = inputs[row_index]
                response = self.network.calculate_network_response(row)
                for i in range(len(response)):
                    self.output_view.set_data(row_index, i, round(response[i], 3))

    @pyqtSlot()
    def on_readFileButton_clicked(self):
        filePath = QFileDialog().getOpenFileName(None, "Select input data file")
        try:
            with open(filePath, "r") as file:
                file_lines = file.readlines()
                rows_count = len(file_lines)
                self.ui.testsCountSpinBox.setValue(rows_count)
                for (line, row) in zip(file_lines, range(rows_count)):
                    for (value, column) in zip(line.split(), range(self.input_view.column_count())):
                        self.input_view.set_data(row, column, float(value))
        except Exception as e:
            print e

    def get_model(self):
        return self.input_view.get_model()

    @pyqtSlot()
    def on_generateRandomButton_clicked(self):
        self.input_view.randomize_data()

    @pyqtSlot(int)
    def on_testsCountSpinBox_valueChanged(self, value):
        self.input_view.set_rows(value)
        self.output_view.set_rows(value)

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QFileDialog
from pl.edu.agh.neural.gui.common.DataView import DataView
from pl.edu.agh.neural.learning.backpropagation.BackpropagationLearning import BackpropagationLearning
from pl.edu.agh.neural.learning.backpropagation.error.ErrorUtil import ErrorUtil
from pl.edu.agh.neural.learning.backpropagation.gui.LearningLauncherUi import Ui_LearningLauncher
from pl.edu.agh.neural.learning.factors.LearningFactorUtil import LearningFactorUtil
from pl.edu.agh.neural.utils.DataNormalizer import DataNormalizer

class BackPropagationLearningDialog(QDialog):
    def __init__(self, network):
        QDialog.__init__(self)

        self.ui = Ui_LearningLauncher()
        self.ui.setupUi(self)

        self.network = network
        self._setup_gui()

        self.input_view = DataView(self.ui.learningDataView, header="Input",
            columns=network.inputs_count())
        self.input_view.randomize_data()

    @pyqtSlot()
    def on_runButton_clicked(self):
        self.error_metric = ErrorUtil.get_factor(str(self.ui.errorMetricSelector.currentText()))()
        learning_factor = LearningFactorUtil.get_factor(str(self.ui.learningFactorSelector.currentText()),
            float(self.ui.learningFactorInitialValue.text()), int(self.ui.learningIterations.text()))

        momentum = float(self.ui.momentumValue.text())
        learning_iterations = int(self.ui.learningIterations.text())
        learning = BackpropagationLearning(self.network, self.metric, learning_factor, momentum)
        learning.learn(DataNormalizer.normalize(self.input_view.get_data()), learning_iterations)
        self.accept()

    @pyqtSlot()
    def on_randomizeButton_clicked(self):
        self.input_view.randomize_data()

    @pyqtSlot()
    def on_readInputButton_clicked(self):
        filePath = QFileDialog().getOpenFileName(None, "Select input data file")
        try:
            with open(filePath, "r") as file:
                file_lines = file.readlines()
                rows_count = len(file_lines)
                self.ui.dataCount.setValue(rows_count)
                for (line, row) in zip(file_lines, range(rows_count)):
                    for (value, column) in zip(line.split(), range(self.input_view.column_count())):
                        self.input_view.set_data(row, column, float(value))
        except Exception as e:
            print e

    @pyqtSlot(int)
    def on_dataCount_valueChanged(self, value):
        old_rows_count = self.input_view.row_count()
        self.input_view.set_rows(value)
        self.input_view.randomize_data(old_rows_count)

    def _setup_gui(self):
        self.ui.errorMetricSelector.addItems(ErrorUtil.registered_factors())
        self.ui.errorMetricSelector.setCurrentIndex(self.ui.errorMetricSelector.findText(ErrorUtil.default_factor()))
from math import ceil
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QFileDialog
from pl.edu.agh.neural.gui.common.DataView import DataView
from pl.edu.agh.neural.learning.cp.CounterPropagationKohonenLearning import CounterPropagationKohonenLearning
from pl.edu.agh.neural.learning.cp.CounterPropagationLearning import CounterPropagationLearning
from pl.edu.agh.neural.learning.cp.gui.LearningLauncherUi import Ui_LearningLauncher
from pl.edu.agh.neural.learning.cp.rules.RulesUtil import RulesUtil
from pl.edu.agh.neural.learning.factors.LearningFactorUtil import LearningFactorUtil
from pl.edu.agh.neural.learning.kohonen.metrics.MetricUtil import MetricUtil
from pl.edu.agh.neural.learning.kohonen.neighbourhood.NeighbourhoodUtil import NeighbourhoodUtil
from pl.edu.agh.neural.learning.kohonen.topology.NoTopology import NoTopology
from pl.edu.agh.neural.learning.kohonen.topology.TopologyUtil import TopologyUtil

class CounterPropagationLearningDialog(QDialog):
    def __init__(self, network):
        QDialog.__init__(self)

        self.ui = Ui_LearningLauncher()
        self.ui.setupUi(self)

        self.network = network
        self.network_layer = network.get_layer(0)
        self.default_rectangular_topology_dimension = int(ceil(len(self.network_layer.get_neurons()) ** 0.5))
        self._setup_gui()

        self.input_view = DataView(self.ui.learningDataView, header="Input",
            columns=network.inputs_count() + len(network.get_layer(-1).get_neurons()))
        self.input_view.randomize_data()

    @pyqtSlot()
    def on_runButton_clicked(self):
        if self.ui.neighbourhoodEnabled.isChecked():
            neighbourhood = NeighbourhoodUtil.get_neighbourhood(
                str(self.ui.neighbourhoodFunctionSelector.currentText()))()
            topology = TopologyUtil.get_topology(str(self.ui.topologySelector.currentText()),
                neighbourhood, int(self.ui.initialNeighbourhoodRadius.text()),
                int(self.ui.topologyRowsValue.text()), int(self.ui.topologyColsValue.text()))
        else:
            topology = NoTopology()
        self.metric = MetricUtil.get_metric(str(self.ui.metricSelector.currentText()))()
        learning_factor = LearningFactorUtil.get_factor(str(self.ui.kohonenLearningFactorSelector.currentText()),
            float(self.ui.kohonenLearningFactorInitialValue.text()), int(self.ui.kohonenLearningIterations.text()))

        conscience_threshold =\
        float(self.ui.conscienceThresholdValue.text()) if self.ui.conscienceEnabled.isChecked() else 0
        kohonen_learning_iterations = int(self.ui.kohonenLearningIterations.text())
        kohonen_learning = CounterPropagationKohonenLearning(self.network_layer, topology, self.metric, learning_factor,
            conscience_threshold)
        learning_data = self.input_view.get_data()

        grossberg_learning_rule = RulesUtil.get_rule(self.ui.learningRuleSelector.currentText())

        grossberg_learning_factor = LearningFactorUtil.get_factor(
            str(self.ui.grossbergLearningFactorSelector.currentText()),
            float(self.ui.grossbergLearningFactorInitialValue.text()), int(self.ui.grossbergLearningIterations.text()))

        grossberg_learning_iterations = int(self.ui.grossbergLearningIterations.text())
        cp_learning = CounterPropagationLearning(self.network, grossberg_learning_rule, grossberg_learning_factor,
            kohonen_learning)
        cp_learning.learn(kohonen_learning_iterations, grossberg_learning_iterations, learning_data)
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

    @pyqtSlot(int)
    def on_topologySelector_currentIndexChanged(self, value):
        self.ui.topologyDimensionsBox.setVisible(self.ui.topologySelector.itemText(value).startsWith("2D"))
        self.ui.topologyRowsValue.setText(str(self.default_rectangular_topology_dimension))
        self.ui.topologyColsValue.setText(str(self.default_rectangular_topology_dimension))

    @pyqtSlot()
    def on_initializeWeightsButton_clicked(self):
        kohonen_layer = self.network.get_layer(0)
        weight = (1.0 / self.network.inputs_count()) ** 0.5
        for neuron in range(len(kohonen_layer.get_neurons())):
            for input in range(self.network.inputs_count()):
                kohonen_layer.set_edge_weight(neuron, input, weight)

    def _setup_gui(self):
        self.ui.topologyDimensionsBox.hide()
        self.ui.topologySelector.addItems(TopologyUtil.registered_topologies())
        self.ui.topologySelector.setCurrentIndex(self.ui.topologySelector.findText(TopologyUtil.default_topology()))
        self.ui.neighbourhoodFunctionSelector.addItems(NeighbourhoodUtil.registered_neighbourhoods())
        self.ui.neighbourhoodFunctionSelector.setCurrentIndex(
            self.ui.neighbourhoodFunctionSelector.findText(NeighbourhoodUtil.default_neighbourhood()))
        self.ui.metricSelector.addItems(MetricUtil.registered_metrics())
        self.ui.metricSelector.setCurrentIndex(self.ui.metricSelector.findText(MetricUtil.default_metric()))
        self.ui.kohonenLearningFactorSelector.addItems(LearningFactorUtil.registered_factors())
        self.ui.kohonenLearningFactorSelector.setCurrentIndex(
            self.ui.kohonenLearningFactorSelector.findText(LearningFactorUtil.default_factor()))
        self.ui.grossbergLearningFactorSelector.addItems(LearningFactorUtil.registered_factors())
        self.ui.grossbergLearningFactorSelector.setCurrentIndex(
            self.ui.grossbergLearningFactorSelector.findText(LearningFactorUtil.default_factor()))
        self.ui.learningRuleSelector.addItems(RulesUtil.rules())
        self.ui.learningRuleSelector.setCurrentIndex(self.ui.learningRuleSelector.findText(RulesUtil.default_layer()))
        self.ui.conscienceThresholdValue.setText(str(1 - round(float(1.0 / self.network.inputs_count()), 2) - 0.01))

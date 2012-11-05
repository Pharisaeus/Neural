from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QHeaderView
from NetworkCreatorUi import Ui_NetworkCreator
from ComboBoxSelector import ComboBoxSelector
from pl.edu.agh.neural.activators.ActivatorUtil import ActivatorUtil
from pl.edu.agh.neural.gui.creator.NetworkCreator import NetworkCreator
from pl.edu.agh.neural.gui.creator.NetworkModel import NetworkModel
from pl.edu.agh.neural.psp.PSPUtil import PSPUtil

class NetworkCreatorDialog(QDialog):
    def __init__(self, network_model = None):
        QDialog.__init__(self)

        self.ui = Ui_NetworkCreator()
        self.ui.setupUi(self)

        self.model_ready = False
        self.network_model = network_model or NetworkModel()

        self._setup_default_functions_comboboxes()
        self._setup_table()
        self._setup_network_parameters()
        self.ui.neuronsTable.setModel(self.network_model.default_layer())
        self.model_ready = True

    def create_network(self):
        return NetworkCreator().create_network(self.network_model)

    @pyqtSlot(int)
    def on_layersEdit_valueChanged(self, value):
        if self.model_ready:
            items_count = self.ui.layerComboBox.count()
            if value > items_count:
                for i in range(items_count + 1, value + 1):
                    layer = self.network_model.add_layer()
                    self.ui.layerComboBox.addItem(layer.layer_name())
            elif value < items_count:
                for i in range(value, items_count):
                    self.ui.layerComboBox.removeItem(i)
                    self.network_model.remove_layer()

    @pyqtSlot(int)
    def on_neuronsEdit_valueChanged(self, neurons_number):
        if self.model_ready:
            layer_index = self.ui.layerComboBox.currentIndex()
            self.network_model.set_neurons_for_layer(layer_index, neurons_number)

    @pyqtSlot(int)
    def on_inputNeuronsEdit_valueChanged(self, value):
        if self.model_ready:
            self.network_model.set_network_input_neurons(value)

    @pyqtSlot(int)
    def on_layerComboBox_currentIndexChanged(self, layer_number):
        if self.model_ready:
            model = self.network_model.layer_model(layer_number)
            self.ui.neuronsTable.setModel(model)
            self.ui.neuronsEdit.setValue(model.rowCount())

    @pyqtSlot(str)
    def on_defaultPSPComboBox_currentIndexChanged(self, value):
        if self.model_ready:
            self.ui.neuronsTable.model().set_default_psp(value)

    @pyqtSlot(str)
    def on_defaultActivationComboBox_currentIndexChanged(self, value):
        if self.model_ready:
            self.ui.neuronsTable.model().set_default_activation(value)

    def _setup_table(self):
        self.ui.neuronsTable.setItemDelegateForColumn(0, self._create_psp_combobox())
        self.ui.neuronsTable.setItemDelegateForColumn(1, self._create_activator_combobox())
        self.ui.neuronsTable.horizontalHeader().setResizeMode(QHeaderView.Stretch)

    def _setup_default_functions_comboboxes(self):
        self.ui.defaultPSPComboBox.addItems(PSPUtil.registered_psps())
        self.ui.defaultActivationComboBox.addItems(ActivatorUtil.registered_activators())
        self.ui.defaultActivationComboBox.setCurrentIndex(
            self.ui.defaultActivationComboBox.findText(ActivatorUtil.default_activator()))

    def _setup_network_parameters(self):
        self.ui.layersEdit.setValue(len(self.network_model.layers()))
        for layer in self.network_model.layers():
            self.ui.layerComboBox.addItem(layer.layer_name())
        self.ui.inputNeuronsEdit.setValue(self.network_model.network_inputs())
        self.ui.neuronsEdit.setValue(self.network_model.default_layer().rowCount())

    def _create_activator_combobox(self):
        return ComboBoxSelector(self.ui.neuronsTable, ActivatorUtil.registered_activators())

    def _create_psp_combobox(self):
        return ComboBoxSelector(self.ui.neuronsTable, PSPUtil.registered_psps())

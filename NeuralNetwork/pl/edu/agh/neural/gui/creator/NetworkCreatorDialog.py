from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog
from NetworkCreatorUi import Ui_NetworkCreator
from LayerModel import LayerModel
from ComboBoxSelector import ComboBoxSelector
from pl.edu.agh.neural.activators.ActivatorUtil import ActivatorUtil
from pl.edu.agh.neural.gui.creator.NetworkCreator import NetworkCreator
from pl.edu.agh.neural.psp.PSPUtil import PSPUtil

class NetworkCreatorDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_NetworkCreator()
        self.ui.setupUi(self)

        self.default_neurons_count = 2
        self.layers_data = {}

        self._setup_table()
        self._setup_layersComboBox(self.ui.layersEdit.value())
        self.ui.neuronsTable.setModel(self.layers_data[1])
        self._setup_default_functions_comboboxes()

    def create_network(self):
        return NetworkCreator().create_network(self.layers_data)

    def _setup_layersComboBox(self, value):
        self.layers_data[0] = self.default_neurons_count
        self._add_layers(range(1, value + 1))

    def _add_layers(self, layers):
        for i in layers:
            self.ui.layerComboBox.addItem(str(i) + " layer")
            if i == 1:
                self.layers_data[i] = LayerModel(self.default_neurons_count, self.layers_data[0])
            else:
                self.layers_data[i] = LayerModel(self.default_neurons_count, self.layers_data[i - 1].rowCount())

    @pyqtSlot(int)
    def on_layersEdit_valueChanged(self, value):
        items_count = self.ui.layerComboBox.count()
        if value > items_count:
            self._add_layers(range(items_count + 1, value + 1))
        elif value < items_count:
            for i in range(value, items_count):
                self.ui.layerComboBox.removeItem(i)
                del self.layers_data[i + 1]

    @pyqtSlot(int)
    def on_neuronsEdit_valueChanged(self, value):
        self.ui.neuronsTable.model().set_neurons(value)
        index = self.ui.layerComboBox.currentIndex()
        if index != len(self.layers_data) - 2:
            self.layers_data[index + 2].set_input_neurons(value)

    @pyqtSlot(int)
    def on_inputNeuronsEdit_valueChanged(self, value):
        self.layers_data[0] = value
        self.layers_data[1].set_input_neurons(value)

    @pyqtSlot(int)
    def on_layerComboBox_currentIndexChanged(self, value):
        model_key = value + 1
        if self.layers_data.has_key(model_key):
            self.ui.neuronsTable.setModel(self.layers_data[model_key])
            self.ui.neuronsEdit.setValue(self.layers_data[model_key].rowCount())

    @pyqtSlot(str)
    def on_defaultPSPComboBox_currentIndexChanged(self, value):
        self.ui.neuronsTable.model().set_default_psp(value)

    @pyqtSlot(str)
    def on_defaultActivationComboBox_currentIndexChanged(self, value):
        self.ui.neuronsTable.model().set_default_activation(value)

    def _setup_table(self):
        self.ui.neuronsTable.setItemDelegateForColumn(0, self._create_psp_combobox())
        self.ui.neuronsTable.setItemDelegateForColumn(1, self._create_activator_combobox())
        self.ui.neuronsTable.setColumnWidth(0, 150)
        self.ui.neuronsTable.setColumnWidth(1, 150)
        self.ui.neuronsTable.setColumnWidth(2, 80)

    def _setup_default_functions_comboboxes(self):
        self.ui.defaultPSPComboBox.addItems(PSPUtil.registered_psps())
        self.ui.defaultActivationComboBox.addItems(ActivatorUtil.registered_activators())
        self.ui.defaultActivationComboBox.setCurrentIndex(
            self.ui.defaultActivationComboBox.findText(ActivatorUtil.default_activator()))

    def _create_activator_combobox(self):
        return ComboBoxSelector(self.ui.neuronsTable, ActivatorUtil.registered_activators())

    def _create_psp_combobox(self):
        return ComboBoxSelector(self.ui.neuronsTable, PSPUtil.registered_psps())

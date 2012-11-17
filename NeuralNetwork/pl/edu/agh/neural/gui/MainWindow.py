from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QDialog, QPainter, QMainWindow, QFileDialog
import yaml
from MainWindowUi import Ui_MainWindow
from creator.NetworkCreatorDialog import NetworkCreatorDialog
from pl.edu.agh.neural.gui.creator.NetworkModel import NetworkModel
from pl.edu.agh.neural.gui.launcher.SimulationLauncherDialog import SimulationLauncherDialog
from pl.edu.agh.neural.gui.view.NetworkViewer import NetworkViewer

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = NetworkViewer()
        self.ui.view.setScene(self.scene)
        self.ui.view.setRenderHint(QPainter.Antialiasing)
        self.test_data = None

        self.creator = None

    def _show_network(self):
        self.scene.clear()
        self.scene.show_network(self.network)
        self.ui.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def _activate_actions(self):
        self.ui.launchAction.setEnabled(True)
        self.ui.editNetworkAction.setEnabled(True)
        self.ui.saveNetworkAction.setEnabled(True)

    @pyqtSlot()
    def on_newNetworkAction_triggered(self):
        self.creator = NetworkCreatorDialog()
        result = self.creator.exec_()
        if result == QDialog.Accepted:
            self.network = self.creator.create_network()
            self._show_network()
            self._activate_actions()

#    @pyqtSlot()
#    def on_editNetworkAction_triggered(self):
#        result = self.creator.exec_()
#        if result == QDialog.Accepted:
#            self.network = self.creator.create_network()
#            self._show_network()
#            self.ui.launchAction.setEnabled(True)
#            self.ui.editNetworkAction.setEnabled(True)

    @pyqtSlot()
    def on_editNetworkAction_triggered(self):
        creator = NetworkCreatorDialog(NetworkModel.from_network(self.network))
        result = creator.exec_()
        if result == QDialog.Accepted:
            self.network = creator.create_network()
            self._show_network()

    @pyqtSlot()
    def on_launchAction_triggered(self):
        creator = SimulationLauncherDialog(self.network, self.test_data)
        creator.exec_()
        self.test_data = creator.get_model()

    @pyqtSlot()
    def on_openNetworkAction_triggered(self):
        filePath = QFileDialog().getOpenFileName(None, "Select input data file")
        try:
            with open(filePath, "r") as file:
                self.network = yaml.load(file)
                self._show_network()
                self._activate_actions()
        except Exception as e:
            print e

    @pyqtSlot()
    def on_saveNetworkAction_triggered(self):
        filePath = QFileDialog().getSaveFileName(None, "Select output file")
        try:
            with open(filePath, "w") as file:
                yaml.dump(self.network, file)
        except Exception as e:
            print e

    def resizeEvent(self, QResizeEvent):
        self.ui.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def show(self):
        QMainWindow.show(self)
        self.resizeEvent(None)

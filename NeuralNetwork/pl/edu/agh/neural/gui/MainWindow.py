from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QDialog, QPainter
from MainWindowUi import Ui_MainWindow
from creator.NetworkCreatorDialog import NetworkCreatorDialog
from pl.edu.agh.neural.gui.creator.NetworkModel import NetworkModel
from pl.edu.agh.neural.gui.launcher.SimulationLauncherDialog import SimulationLauncherDialog
from pl.edu.agh.neural.gui.view.NetworkViewer import NetworkViewer

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = NetworkViewer()
        self.ui.view.setScene(self.scene)
        self.ui.view.setRenderHint(QPainter.Antialiasing)

    def _show_network(self):
        self.scene.clear()
        self.scene.show_network(self.network)
        self.ui.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    @pyqtSlot()
    def on_newNetworkAction_triggered(self):
        creator = NetworkCreatorDialog()
        result = creator.exec_()
        if result == QDialog.Accepted:
            self.network = creator.create_network()
            self._show_network()
            self.ui.launchAction.setEnabled(True)
            self.ui.editNetworkAction.setEnabled(True)

    @pyqtSlot()
    def on_editNetworkAction_triggered(self):
        creator = NetworkCreatorDialog(NetworkModel.from_network(self.network))
        result = creator.exec_()
        if result == QDialog.Accepted:
            self.network = creator.create_network()
            self._show_network()

    @pyqtSlot()
    def on_launchAction_triggered(self):
        creator = SimulationLauncherDialog(self.network)
        creator.exec_()

    def resizeEvent(self, QResizeEvent):
        self.ui.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

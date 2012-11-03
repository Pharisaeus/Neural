from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate, QComboBox

class ComboBoxSelector(QItemDelegate):
    def __init__(self, parent, items):
        QItemDelegate.__init__(self, parent)
        self.items = items

    def createEditor(self, parent, QStyleOptionViewItem, QModelIndex):
        editor = QComboBox(parent)
        editor.addItems(self.items)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole).toString()
        editor.setCurrentIndex(editor.findText(value))

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
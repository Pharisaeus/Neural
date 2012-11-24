from random import random
from PyQt4.QtGui import QHeaderView, QStandardItemModel

class DataView(object):
    def __init__(self, view, header, columns, model=None, rows=1):
        self.view = view
        self.model = model or self._create_model(rows, columns)
        self.view.setModel(self.model)
        self.view.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.model.setHorizontalHeaderLabels([header + " " + str(i) for i in range(1, columns + 1)])

    def _create_model(self, rows, columns):
        model = QStandardItemModel()
        model.setColumnCount(columns)
        model.setRowCount(rows)
        return model

    def setup_headers(self, headers):
        self.model.setHorizontalHeaderLabels(headers)

    def set_data(self, row, column, data):
        self.model.setData(self.model.index(row, column), data)

    def row_count(self):
        return self.model.rowCount()

    def set_rows(self, value):
        self.model.setRowCount(value)

    def column_count(self):
        return self.model.columnCount()

    def get_model(self):
        return self.model

    def check_data(self):
        for column in range(self.model.columnCount()):
            for row in range(self.model.rowCount()):
                if self.model.item(row, column) is None:
                    return False
        return True

    def get_data(self):
        return [[float(self.model.item(row, column).text())
                 for column in range(self.model.columnCount())]
                for row in range(self.model.rowCount())]

    def randomize_data(self, start_row=0):
        for row in range(start_row, self.model.rowCount()):
            for column in range(self.model.columnCount()):
                self.set_data(row, column, round(random(), 3))
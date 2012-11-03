from numpy.linalg import linalg
from PyQt4.QtCore import QRectF, Qt, QPointF
from PyQt4.QtGui import QGraphicsItem, QPolygonF

class EdgeItem(QGraphicsItem):
    def __init__(self, start, end):
        QGraphicsItem.__init__(self)
        self.vector = (end[0] - start[0], end[1] - start[1])
        self.setPos(start[0], start[1])
        self.setZValue(-1)

    def paint(self, painter, QStyleOptionGraphicsItem, QWidget_widget=None):
        painter.setBrush(Qt.darkGray)
        painter.drawLine(0, 0, self.vector[0], self.vector[1])
        vector = self._scale_vector(self.vector)
        arrow_point = QPointF(vector[0], vector[1])

        vector = self._scale_vector(vector)
        unit_vector = vector / (linalg.norm(vector) / 5)

        painter.drawPolygon(QPolygonF([
            QPointF(vector[0] - unit_vector[1], vector[1] + unit_vector[0]),
            QPointF(vector[0] + unit_vector[1], vector[1] - unit_vector[0]),
            arrow_point
        ]))

    def _scale_vector(self, vector):
        ratio = 1 - 20 / linalg.norm(vector)
        return vector[0] * ratio, vector[1] * ratio

    def boundingRect(self):
        return QRectF(0, 0, self.vector[0], self.vector[1])

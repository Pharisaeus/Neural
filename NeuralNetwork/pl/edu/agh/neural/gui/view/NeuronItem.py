from PyQt4.QtCore import QRectF, Qt
from PyQt4.QtGui import QGraphicsItem

class NeuronItem(QGraphicsItem):
    def __init__(self, (x, y), bias=None):
        QGraphicsItem.__init__(self)
        self.radius = 20
        self.setX(x)
        self.setY(y)
        self.bias = bias

    def paint(self, painter, QStyleOptionGraphicsItem, QWidget_widget=None):
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)
        if self.bias is not None:
            painter.scale(0.5, 0.5)
            painter.drawText(-30, 50, "Bias = " + str(self.bias))

    def boundingRect(self):
        return QRectF(-self.radius, -self.radius, self.radius * 2, self.radius * 2)
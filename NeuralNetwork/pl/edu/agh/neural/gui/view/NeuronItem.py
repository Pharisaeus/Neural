from PyQt4.QtCore import QRectF, Qt
from PyQt4.QtGui import QGraphicsItem

class NeuronItem(QGraphicsItem):
    def __init__(self, (x, y)):
        QGraphicsItem.__init__(self)
        self.radius = 20
        self.setX(x)
        self.setY(y)

    def paint(self, painter, QStyleOptionGraphicsItem, QWidget_widget=None):
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def boundingRect(self):
        return QRectF(-self.radius, -self.radius, self.radius * 2, self.radius * 2)
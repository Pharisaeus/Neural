from PyQt4.QtGui import QApplication
import sys

from gui.MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    print "Ciekawe czy to będzie konflikt..."

main()

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    root = QMainWindow()
    root.setGeometry(200, 200, 400, 300)
    root.setWindowTitle("Random GUI")

    label = QtWidgets.QLabel(root)
    label.setText("Labels!")
    label.move(20,20)

    root.show()
    sys.exit(app.exec_())

window()
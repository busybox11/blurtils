import sys, os
from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2 import QtUiTools

app = QApplication(sys.argv)
w = QtUiTools.QUiLoader().load(os.path.join(os.path.dirname(__file__), "form.ui"))

def open_image():
    name = QFileDialog.getOpenFileName(w, 'Open File')
    print(name)
    w.image = QtGui.QImage(name[0])
    pixmap = QtGui.QPixmap(w.image)
    w.imageLabel.setPixmap(pixmap)

w.openFileBtn.clicked.connect(open_image)

w.show()
sys.exit(app.exec_())

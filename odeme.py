import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from odeme_UI import *
from PyQt5.QtCore import Qt


class Odeme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.odeme = odeme_ui()
        self.odeme.setupUi(self)
       
        

uyg = QApplication(sys.argv)
pencere = Odeme()
pencere.show()
sys.exit(uyg.exec_())

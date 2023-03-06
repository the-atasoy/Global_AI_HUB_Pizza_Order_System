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
       
        

#uyg_2 = QApplication(sys.argv)
#pencere_2 = Odeme()
#pencere_2.show()
#sys.exit(uyg_2.exec_())

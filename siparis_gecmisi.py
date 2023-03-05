import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from siparis_gecmisi_UI import *
from PyQt5.QtCore import Qt


class Siparis_Gecmisi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SP =siparis_gecmisi()
        self.SP.setupUi(self)
        self.SP.pushButton_search.clicked.connect(self.search_customer)
        self.csv_to_table()

    def csv_to_table(self):
        pass

    def search_customer(self):
        pass

uyg = QApplication(sys.argv)
pencere = Siparis_Gecmisi()
pencere.show()
sys.exit(uyg.exec_())

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QCheckBox
from siparis_gecmisi_UI import siparis_gecmisi
from PyQt5.QtCore import Qt


class Siparis_Gecmisi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.SP = siparis_gecmisi()
        self.SP.setupUi(self)
        self.csv_to_table()

        self.SP.pushButton_search.clicked.connect(self.search_customer)

    def csv_to_table(self):
        reader = pd.read_csv("Payment/payment_history.csv")
        data = reader.values.tolist()

        for row_index, row_data in enumerate(data):
            self.SP.order_history.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.SP.order_history.setItem(row_index, col_index, item)
                self.SP.order_history.item(row_index, col_index).setFlags(self.SP.order_history.item(row_index, col_index).flags() & ~Qt.ItemIsEditable)

            check_box = QCheckBox()
            self.SP.order_history.setCellWidget(row_index, self.SP.order_history.columnCount() - 1, check_box)

    def search_customer(self):
        pass

    def sil(self):
        pass



uyg = QApplication(sys.argv)
pencere = Siparis_Gecmisi()
pencere.show()
sys.exit(uyg.exec_())

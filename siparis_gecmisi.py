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
        self.tablo_arama()
        self.SP.pushButton_search.clicked.connect(self.tablo_arama)


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

    def tablo_arama(self):
        search = self.SP.customer_info.text().capitalize()
        table = self.SP.order_history
        self.SP.error_handling.setText("")

        for row in range(table.rowCount()):
            match = False
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item is not None and search in item.text().capitalize():
                    match = True
                    break

            table.setRowHidden(row, not match)

        if not any([not table.isRowHidden(row) for row in range(table.rowCount())]):
            self.SP.error_handling.setText("Aradığınız kritere uygun bir eşleşme bulunamadı.")

    def secili_sifre_sil(self):
        for row in range(self.sifrelerim.kayit_defteri.rowCount()-1, -1, -1):
            if self.sifrelerim.kayit_defteri.cellWidget(row, 3).isChecked():
                sifre_id = self.sifrelerim.kayit_defteri.item(row, 1).text() # sifre id sütununu al
                self.sifrelerim.kayit_defteri.removeRow(row)



uyg = QApplication(sys.argv)
pencere = Siparis_Gecmisi()
pencere.show()
sys.exit(uyg.exec_())

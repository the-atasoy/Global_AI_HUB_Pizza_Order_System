import sys
import csv
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QCheckBox
from siparis_gecmisi_UI import siparis_gecmisi
from PyQt5.QtCore import Qt

class Siparis_Gecmisi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SP = siparis_gecmisi()
        self.SP.setupUi(self)
        self.file= open("Data\order_history.csv", "r", newline='', encoding="utf-8")
        self.SP.customer_info.returnPressed.connect(self.tablo_arama)
        self.SP.pushButton_search.clicked.connect(self.tablo_arama)
        self.SP.pushbutton_remove_.clicked.connect(self.secili_sil)
        self.SP.pushbutton_choose_all.clicked.connect(self.tumunu_sec)
        self.last_row_count = 0
        self.loadCsv()

   
    def loadCsv(self):
        self.SP.order_history.setRowCount(0)
        with open("Data\order_history.csv", "r", newline='', encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            next(reader)
            for row_num, row_data in enumerate(reader):
                items = [
                    QTableWidgetItem(field)
                    for field in row_data
                ]
                self.SP.order_history.insertRow(row_num)
                for col_num, item in enumerate(items):
                    self.SP.order_history.setItem(row_num, col_num, item)
                    self.SP.order_history.item(row_num, col_num).setFlags(self.SP.order_history.item(row_num, col_num).flags() & ~Qt.ItemIsEditable)
                
                check_box = QCheckBox()
                self.SP.order_history.setCellWidget(row_num, self.SP.order_history.columnCount() - 1, check_box)

    def clear_table(self):
        self.SP.order_history.clearContents()


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

    def secili_sil(self):
        df = pd.read_csv("Data\order_history.csv")
        rows_to_delete = []
        for row in range(df.shape[0]):
            if self.SP.order_history.cellWidget(row, 8) is not None and self.SP.order_history.cellWidget(row, 8).isChecked():
                rows_to_delete.append(row)
        df.drop(rows_to_delete, inplace=True)
        df.to_csv("Data\order_history.csv", index=False)
        self.SP.order_history.setRowCount(df.shape[0])
        for row_num, row_data in df.iterrows():
            items = [
                QTableWidgetItem(str(field))
                for field in row_data
            ]
            for col_num, item in enumerate(items):
                if self.SP.order_history.item(row_num, col_num) is not None:
                    self.SP.order_history.setItem(row_num, col_num, item)
                    self.SP.order_history.item(row_num, col_num).setFlags(self.SP.order_history.item(row_num, col_num).flags() & ~Qt.ItemIsEditable)
            check_box = QCheckBox()
            self.SP.order_history.setCellWidget(row_num, self.SP.order_history.columnCount() - 1, check_box)

    def tumunu_sec(self):
        for row in range(self.SP.order_history.rowCount()):
            checkbox = self.SP.order_history.cellWidget(row, 8)
            if not checkbox.isChecked():
                checkbox.setChecked(True)


#uyg_1 = QApplication(sys.argv)
#pencere_1 = Siparis_Gecmisi()
#pencere_1.show()
#sys.exit(uyg_1.exec_())

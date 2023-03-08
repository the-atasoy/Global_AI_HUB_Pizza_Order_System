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
        self.SP.pushButton_search.clicked.connect(self.tablo_arama)
        self.SP.pushbutton_remove_.clicked.connect(self.secili_sil)
        self.SP.pushbutton_choose_all.clicked.connect(self.tumunu_sec)
        self.csv_to_table()
        self.last_row_count = 0
        self.update_table()


    def csv_to_table(self):
        table = self.SP.order_history

        # CSV dosyasını aç ve içindeki verileri oku
        csvfile= open("Data\order_history.csv", newline='', encoding="utf-8") 
        reader = csv.reader(csvfile)
            # Her satırı table widget içine ekle
        for row_num, row_data in enumerate(reader):
            table.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                table.setItem(row_num, col_num, item)
                self.SP.order_history.item(row_num, col_num).setFlags(self.SP.order_history.item(row_num, col_num).flags() & ~Qt.ItemIsEditable)

            check_box = QCheckBox()
            self.SP.order_history.setCellWidget(row_num, self.SP.order_history.columnCount() - 1, check_box)
        table.update()

    def update_table(self):
        with open('Data\order_history.csv', 'r') as file:
            reader = csv.reader(file)
            rows = [row for i, row in enumerate(reader) if i >= self.last_row_count] # sadece yeni eklenen verileri al
            self.last_row_count = reader.line_num # son okunan satır sayısını güncelle
        if rows: # eğer yeni veri varsa, tabloyu güncelle
            self.SP.order_history.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, item in enumerate(row):
                    self.SP.order_history.setItem(i, j, QTableWidgetItem(item))

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
        for row in range(self.SP.order_history.rowCount()-1, -1, -1):
            if self.SP.order_history.cellWidget(row, 8).isChecked():
                reader = pd.read_csv("Data\order_history.csv")
                reader.drop(row, inplace=True)
                reader.to_csv("Data\order_history.csv", index=False)
                self.SP.order_history.removeRow(row)

    def tumunu_sec(self):
        for row in range(self.SP.order_history.rowCount()):
            checkbox = self.SP.order_history.cellWidget(row, 7)
            if not checkbox.isChecked():
                checkbox.setChecked(True)


#uyg_1 = QApplication(sys.argv)
#pencere_1 = Siparis_Gecmisi()
#pencere_1.show()
#sys.exit(uyg_1.exec_())

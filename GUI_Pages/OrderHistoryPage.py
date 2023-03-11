import csv
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QCheckBox
from UI_Files.siparis_gecmisi_UI import OrderHistory
from PyQt5.QtCore import Qt

class OrderHistoryPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # History page object
        self.order_history_page = OrderHistory()
        self.order_history_page.setupUi(self)

        # Order history data as csv
        self.file = open("Data/order_history.csv", "r", newline='', encoding="utf-8")
        # Connection
        # Searching a specific order in order history when press the enter key
        self.order_history_page.customer_info.returnPressed.connect(self.search_in_orders)

        # Connection
        # Searching a specific order in order history when press the clicked the search button
        self.order_history_page.pushButton_search.clicked.connect(self.search_in_orders)

        # Connection
        # Selecting all rows in order history page
        self.order_history_page.pushbutton_choose_all.clicked.connect(self.select_all)

        # Connection
        # Deleting selected rows in order history page
        self.order_history_page.pushbutton_remove_.clicked.connect(self.del_chosen)

        self.last_row_count = 0

        # Loading the csv to the order history table
        self.load_csv()

    # This function clears the order history table before loading the csv to the table
    # because of repeating order problem
    def clear_table(self):
        self.order_history_page.order_history.clearContents()

    # This function loads the csv to the order history table
    def load_csv(self):
        self.order_history_page.order_history.setRowCount(0)
        with open("Data/order_history.csv", "r", newline='', encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            next(reader)
            for row_num, row_data in enumerate(reader):
                items = [
                    QTableWidgetItem(field)
                    for field in row_data
                ]
                self.order_history_page.order_history.insertRow(row_num)
                for col_num, item in enumerate(items):
                    self.order_history_page.order_history.setItem(row_num, col_num, item)
                    self.order_history_page.order_history.item(row_num, col_num).setFlags(self.order_history_page.order_history.item(row_num, col_num).flags() & ~Qt.ItemIsEditable)
                
                check_box = QCheckBox()
                self.order_history_page.order_history.setCellWidget(row_num, self.order_history_page.order_history.columnCount() - 1, check_box)

    # This function searches a specific order in order history table
    def search_in_orders(self):
        search = self.order_history_page.customer_info.text().capitalize()
        table = self.order_history_page.order_history
        self.order_history_page.error_handling.setText("")

        for row in range(table.rowCount()):
            match = False
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item is not None and search in item.text().capitalize():
                    match = True
                    break

            table.setRowHidden(row, not match)

        if not any([not table.isRowHidden(row) for row in range(table.rowCount())]):
            self.order_history_page.error_handling.setText("Aradığınız kritere uygun eşleşme bulunamadı.")

    # This function selects all rows in order table
    def select_all(self):
        for row in range(self.order_history_page.order_history.rowCount()):
            checkbox = self.order_history_page.order_history.cellWidget(row, 8)
            if not checkbox.isChecked():
                checkbox.setChecked(True)
            elif checkbox.isChecked():
                if checkbox.isChecked():
                    checkbox.setChecked(True)
                else:
                    checkbox.setChecked(False)

    # This function deletes selected rows in order history table
    def del_chosen(self):
        df = pd.read_csv("Data/order_history.csv")
        rows_to_delete = []
        for row in range(self.order_history_page.order_history.rowCount()):
            if self.order_history_page.order_history.cellWidget(row, 8) is not None and self.order_history_page.order_history.cellWidget(row, 8).isChecked():
                rows_to_delete.append(row)
        df.drop(rows_to_delete, inplace=True)
        df.to_csv("Data/order_history.csv", index=False)
        for i, row in enumerate(rows_to_delete):
            self.order_history_page.order_history.removeRow(row - i)
        for row_num, row_data in df.iterrows():
            items = [QTableWidgetItem(str(field)) for field in row_data]
            for col_num, item in enumerate(items):
                if self.order_history_page.order_history.item(row_num, col_num) is not None:
                    self.order_history_page.order_history.setItem(row_num, col_num, item)
                    self.order_history_page.order_history.item(row_num, col_num).setFlags(
                        self.order_history_page.order_history.item(row_num, col_num).flags() & ~Qt.ItemIsEditable
                    )
            check_box = QCheckBox()
            self.order_history_page.order_history.setCellWidget(row_num, self.order_history_page.order_history.columnCount() - 1, check_box)

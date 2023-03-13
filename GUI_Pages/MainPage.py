from Connections.MealMenu import pizza_menu, ingredient_menu, sauce_menu, beverage_menu
import datetime
import Connections.Tuples as Tuples
from UI_Files.MainPage_UI import *
from Connections.Objects import *
from GUI_Pages.OrderHistoryPage import *
from GUI_Pages.PaymentPage import *
from PyQt5.QtCore import Qt

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main page object
        self.main_page = MainPage_UI()
        self.main_page.setupUi(self)

        # Payment page object
        self.payment_window = PaymentPage()

        # Order history page object
        self.order_history_window = OrderHistoryPage()

        # Displaying menu on GUI
        pizza_menu(self)
        ingredient_menu(self)
        sauce_menu(self)
        beverage_menu(self)

        # Checkbox connections
        self.main_page.classic_pizza_check.stateChanged.connect(self.choose_pizza)
        self.main_page.margherita_pizza_check.stateChanged.connect(self.choose_pizza)
        self.main_page.turk_pizza_check.stateChanged.connect(self.choose_pizza)
        self.main_page.dominos_pizza_check.stateChanged.connect(self.choose_pizza)
        self.main_page.ketchup_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.mayo_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.mustard_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.bbq_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.hot_sauce_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.ranch_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.coke_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.fanta_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.pop_soda_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.lemonade_check.stateChanged.connect(self.choose_sauce_beverage)
        self.main_page.ayran_check.stateChanged.connect(self.choose_sauce_beverage)

        # Connection
        # Amount of item automatically will be 1 when you choose the item
        self.main_page.ketchup_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.mayo_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.mustard_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.bbq_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.hot_sauce_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.ranch_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.coke_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.fanta_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.pop_soda_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.lemonade_check.stateChanged.connect(self.auto_increment_spinbox)
        self.main_page.ayran_check.stateChanged.connect(self.auto_increment_spinbox)

        # Connection
        # Item is checked automatically when you change amount of it using spinbox
        self.main_page.spinBox_ketchup_4.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_mayo_4.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_mustard_4.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_bbq_4.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_hot_sauce_4.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_ranch_4.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_coke.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_fanta.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_pop_soda.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_lemonade.valueChanged.connect(self.auto_check)
        self.main_page.spinBox_ayran.valueChanged.connect(self.auto_check)

        # Connection
        # Add selected items to basket
        self.main_page.button_add_to_basket.clicked.connect(self.add_to_basket)

        # A list to save order
        self.order = []

        # Signals from payment page to delete items in basket when payment is successful
        self.payment_window.table_cleaning_signal.connect(self.choose_all)
        self.payment_window.table_cleaning_signal.connect(self.del_chosen)

        # Connection to choose all items in basket
        self.main_page.select_all.clicked.connect(self.choose_all)

        # Connection to delete chosen items in basket
        self.main_page.delete_chosen.clicked.connect(self.del_chosen)

        # Connection to go to the payment page when confirm the basket
        self.main_page.confirm_basket.clicked.connect(self.go_to_payment)

        # A signal from payment page to save datas in payment page to the order history database
        self.payment_window.order_history_signal.connect(self.save_to_order_history)

        # Connection to show order history when clicked on "orders"
        self.main_page.action_past_orders.triggered.connect(self.show_order_history)

    # This function checks if a pizza is checked or not and if a pizza is checked, do not allow checking another pizza
    def choose_pizza(self):
        check_box = [
            [self.main_page.classic_pizza_check, self.main_page.classic_pizza_check.isChecked()],
            [self.main_page.margherita_pizza_check, self.main_page.margherita_pizza_check.isChecked()],
            [self.main_page.turk_pizza_check, self.main_page.turk_pizza_check.isChecked()],
            [self.main_page.dominos_pizza_check, self.main_page.dominos_pizza_check.isChecked()]
        ]

        for checkbox in check_box:
            if checkbox[1]:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(False)
                        self.order.clear()
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(True)
                    self.order.clear()

    # This function checks if sauces and beverages are checked or not
    def choose_sauce_beverage(self):
        check_box_sauces_beverages = [
            [self.main_page.ketchup_check, self.main_page.ketchup_check.isChecked()],
            [self.main_page.mayo_check, self.main_page.mayo_check.isChecked()],
            [self.main_page.mustard_check, self.main_page.mustard_check.isChecked()],
            [self.main_page.bbq_check, self.main_page.bbq_check.isChecked()],
            [self.main_page.hot_sauce_check, self.main_page.hot_sauce_check.isChecked()],
            [self.main_page.ranch_check, self.main_page.ranch_check.isChecked()],
            [self.main_page.coke_check, self.main_page.coke_check.isChecked()],
            [self.main_page.fanta_check, self.main_page.fanta_check.isChecked()],
            [self.main_page.pop_soda_check, self.main_page.pop_soda_check.isChecked()],
            [self.main_page.lemonade_check, self.main_page.lemonade_check.isChecked()],
            [self.main_page.ayran_check, self.main_page.ayran_check.isChecked()]
        ]
        for checkbox in check_box_sauces_beverages:
            if checkbox[1]:
                for other_checkbox in check_box_sauces_beverages:
                    if other_checkbox[0] != checkbox[0]:
                        self.order.clear()
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box_sauces_beverages:
                    if other_checkbox[0] != checkbox[0]:
                        self.order.clear()

    # This function increases the amount of selected item to 1 automatically when it is chosen
    def auto_increment_spinbox(self):
        checkbox = [self.main_page.ketchup_check,
                    self.main_page.mayo_check,
                    self.main_page.mustard_check,
                    self.main_page.bbq_check,
                    self.main_page.hot_sauce_check,
                    self.main_page.ranch_check,
                    self.main_page.coke_check,
                    self.main_page.fanta_check,
                    self.main_page.pop_soda_check,
                    self.main_page.lemonade_check,
                    self.main_page.ayran_check
                    ]
        spinbox = [self.main_page.spinBox_ketchup_4,
                   self.main_page.spinBox_mayo_4,
                   self.main_page.spinBox_mustard_4,
                   self.main_page.spinBox_bbq_4,
                   self.main_page.spinBox_hot_sauce_4,
                   self.main_page.spinBox_ranch_4,
                   self.main_page.spinBox_coke,
                   self.main_page.spinBox_fanta,
                   self.main_page.spinBox_pop_soda,
                   self.main_page.spinBox_lemonade,
                   self.main_page.spinBox_ayran]

        for i, e in enumerate(checkbox):
            if e.isChecked():
                if spinbox[i].value() == 0:
                    spinbox[i].setValue(1)
            else:
                # if item is unchecked, value of spinbox will be 0
                spinbox[i].setValue(0)

    # This function checks the item automatically if amount of it is increased via spinbox
    def auto_check(self):
        checkbox = [self.main_page.ketchup_check,
                    self.main_page.mayo_check,
                    self.main_page.mustard_check,
                    self.main_page.bbq_check,
                    self.main_page.hot_sauce_check,
                    self.main_page.ranch_check,
                    self.main_page.coke_check,
                    self.main_page.fanta_check,
                    self.main_page.pop_soda_check,
                    self.main_page.lemonade_check,
                    self.main_page.ayran_check
                    ]
        spinbox = [self.main_page.spinBox_ketchup_4,
                   self.main_page.spinBox_mayo_4,
                   self.main_page.spinBox_mustard_4,
                   self.main_page.spinBox_bbq_4,
                   self.main_page.spinBox_hot_sauce_4,
                   self.main_page.spinBox_ranch_4,
                   self.main_page.spinBox_coke,
                   self.main_page.spinBox_fanta,
                   self.main_page.spinBox_pop_soda,
                   self.main_page.spinBox_lemonade,
                   self.main_page.spinBox_ayran]

        for i, e in enumerate(spinbox):
            if e.value() > 0:
                checkbox[i].setChecked(True)
            else:
                checkbox[i].setChecked(False)

    # This function is added the selected pizza to order list
    def add_pizza(self, pizza_list):
        for element in pizza_list:
            if element[2]:
                self.order.append(element[0:2])
        return self.order

    # This function is added the selected ingredients to order list
    def add_ingredient(self, ingredient_list):
        for element in ingredient_list:
            if element[2]:
                self.order.append(element[0:2])
        return self.order

    # This function is added the selected sauces to order list
    def add_sauce(self, sauce_list):
        for element in sauce_list:
            if element[2]:
                self.order.append(element[0:2])
        return self.order

    # This function is added the selected beverages to order list
    def add_beverages(self, beverages_list):
        for element in beverages_list:
            if element[2]:
                self.order.append(element[0:2])
        return self.order

    # This function displays the order which is created to the basket table and
    # call the set_default_situation function to make options and note table default
    def add_to_basket(self):
        self.add_pizza(Tuples.pizza_tuple(self))
        self.add_ingredient(Tuples.ingredient_tuple(self))
        self.add_sauce(Tuples.sauce_tuple(self))
        self.add_beverages(Tuples.beverage_tuple(self))
        order_dict = self.create_dictionary(self.order)
        self.add_data_to_table(order_dict)
        self.set_default_situation()
        return order_dict

    # This function make options and note table default
    def set_default_situation(self):
        checkbox_list = [
            self.main_page.classic_pizza_check,
            self.main_page.margherita_pizza_check,
            self.main_page.turk_pizza_check,
            self.main_page.dominos_pizza_check,
            self.main_page.zeytin_check,
            self.main_page.keci_peyniri_check,
            self.main_page.misir_check,
            self.main_page.et_check,
            self.main_page.sogan_check,
            self.main_page.mantar_check,
            self.main_page.keci_peyniri_check,
            self.main_page.ketchup_check,
            self.main_page.mayo_check,
            self.main_page.mustard_check,
            self.main_page.bbq_check,
            self.main_page.hot_sauce_check,
            self.main_page.ranch_check,
            self.main_page.coke_check,
            self.main_page.fanta_check,
            self.main_page.pop_soda_check,
            self.main_page.lemonade_check,
            self.main_page.ayran_check]

        for e in checkbox_list:
            if e.isChecked():
                e.setChecked(False)

        # this code make add note widget default when push the "add to basket" button
        self.main_page.plainTextEdit.clear()
        self.main_page.plainTextEdit.setPlaceholderText("Not Ekleyin")

    # This function creates a dictionary in order to add items to database and basket table
    def create_dictionary(self, order_list):

        pizzas = [classic.get_description(),
                  margherita.get_description(),
                  turk.get_description(),
                  dominos.get_description()]

        ingredients = [olive.get_description(),
                       mushroom.get_description(),
                       goat_cheese.get_description(),
                       meat.get_description(),
                       onion.get_description(),
                       corn.get_description()]

        sauces = [ketchup.get_description(),
                  mayo.get_description(),
                  mustard.get_description(),
                  bbq.get_description(),
                  hot_sauce.get_description(),
                  ranch.get_description()]

        beverages = [coke.get_description(),
                     fanta.get_description(),
                     pop_soda.get_description(),
                     lemonade.get_description(),
                     ayran.get_description()]

        basket = {"Pizza": "", "Malzemeler": "", "Soslar": "", "İçecekler": "", "Fiyat": 0, "Notlar": ""}
        for data in order_list:
            if data[0] in pizzas:
                basket['Pizza'] = data[0]
            elif data[0] in sauces:
                if basket["Soslar"] != "":
                    basket["Soslar"] += ", "
                basket["Soslar"] += data[0]
            elif data[0] in beverages:
                if basket["İçecekler"] != "":
                    basket["İçecekler"] += ", "
                basket["İçecekler"] += data[0]
            else:
                if basket["Malzemeler"] != "":
                    basket["Malzemeler"] += ", "
                basket["Malzemeler"] += data[0]
            basket["Fiyat"] += data[1]
            basket["Notlar"] = self.main_page.plainTextEdit.toPlainText()
        return basket

    # This function displays order in basket table getting datas
    # from dictionary which is created in "create_dictionary function
    def add_data_to_table(self, data):
        table_widget = self.main_page.basket_table
        row_count = table_widget.rowCount()
        table_widget.setRowCount(row_count + 1)
        row = row_count

        # Create a new QTableWidgetItem object
        pizza_item = QTableWidgetItem(data["Pizza"])
        ingredient_item = QTableWidgetItem(data["Malzemeler"])
        sauce_item = QTableWidgetItem(data["Soslar"])
        beverage_item = QTableWidgetItem(data["İçecekler"])
        cost_item = QTableWidgetItem(str(data["Fiyat"]))
        notes_item = QTableWidgetItem(data["Notlar"])

        # Blocking outside access to the QTableWidgetItem
        pizza_item.setFlags(pizza_item.flags() ^ Qt.ItemIsEditable)
        ingredient_item.setFlags(ingredient_item.flags() ^ Qt.ItemIsEditable)
        sauce_item.setFlags(sauce_item.flags() ^ Qt.ItemIsEditable)
        beverage_item.setFlags(beverage_item.flags() ^ Qt.ItemIsEditable)
        cost_item.setFlags(cost_item.flags() ^ Qt.ItemIsEditable)
        notes_item.setFlags(notes_item.flags() ^ Qt.ItemIsEditable)

        # Add objects to the table
        table_widget.setItem(row, 0, pizza_item)
        table_widget.setItem(row, 1, ingredient_item)
        table_widget.setItem(row, 2, sauce_item)
        table_widget.setItem(row, 3, beverage_item)
        table_widget.setItem(row, 4, cost_item)
        table_widget.setItem(row, 5, notes_item)

        # Checkboxes in allow/delete column
        check_box = QCheckBox()
        self.main_page.basket_table.setCellWidget(row, 6, check_box)

    # This function choose all rows in basket table
    def choose_all(self):
        # QCheckBox is used to find checkbox widgets
        for row in range(self.main_page.basket_table.rowCount()):
            checkbox = self.main_page.basket_table.cellWidget(row, 6)
            if not checkbox.isChecked():
                checkbox.setChecked(True)  # check all checkboxes

    # This function deletes selected rows in basket table
    def del_chosen(self):
        for row in range(self.main_page.basket_table.rowCount() - 1, -1, -1):
            if self.main_page.basket_table.cellWidget(row, 6).isChecked():
                self.main_page.basket_table.removeRow(row)

    # This function brings you to payment page if you choose all rows in basket table
    def go_to_payment(self):
        all_checked = True
        if self.main_page.basket_table.rowCount() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen Sepete Ürün Ekleyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return

        for row in range(self.main_page.basket_table.rowCount()):
            if not self.main_page.basket_table.cellWidget(row, 6).isChecked():
                all_checked = False
                break

        if all_checked:
            self.payment_window.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Tüm siparişlerin seçili olması gerek")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()

    # This function add order information to database and clear the basket table when payment is successful
    # This function uses signals in order to these
    def save_to_order_history(self, info):
        order_info = []
        total_price = 0
        notes_info = []
        table_widget = self.main_page.basket_table
        payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for row in range(table_widget.rowCount()):
            pizza = table_widget.item(row, 0).text()
            ingredient = table_widget.item(row, 1).text()
            sauce = table_widget.item(row, 2).text()
            beverages = table_widget.item(row, 3).text()
            order_info.append(pizza)
            order_info.append(ingredient)
            order_info.append(sauce)
            order_info.append(beverages)

        for row in range(table_widget.rowCount()):
            total_price += int(table_widget.item(row, 4).text())

        for row in range(table_widget.rowCount()):
            notes = table_widget.item(row, 5).text()
            notes_info.append(notes)

        customer_order_info = {"Müşteri Bilgisi": info["name_lastname"],
                               "Sipariş": "",
                               "Notlar": "",
                               "Tarih-Saat": payment_date,
                               "Toplam Tutar": total_price,
                               "TC Kimlik Numarası": info["tc"],
                               "Kart Numarası": info["card_no"],
                               "Şifre": info["sifre"]}

        for i in order_info:
            if customer_order_info["Sipariş"] != "":
                customer_order_info["Sipariş"] += ", "
            customer_order_info["Sipariş"] += i

        for i in notes_info:
            if customer_order_info["Notlar"] != "":
                customer_order_info["Notlar"] += ", "
            customer_order_info["Notlar"] += i

        with open("Data/order_history.csv", "a", newline='', encoding="utf-8") as myFile:
            writer = csv.DictWriter(myFile, fieldnames=list(customer_order_info.keys()))
            writer.writerow(customer_order_info)

        self.order_history_window.clear_table()

    # This function shows order history
    def show_order_history(self):
        self.order_history_window.show()
        self.order_history_window.load_csv()

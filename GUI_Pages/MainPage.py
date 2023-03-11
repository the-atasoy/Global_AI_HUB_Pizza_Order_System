from Connections.MealMenu import pizza_menu, ingredient_menu, sauce_menu, drink_menu
import datetime
import Connections.Tuples as Tuples
from UI_Files.Anaekran_UI import *
from Connections.Objects import *
from GUI_Pages.OrderHistoryPage import *
from GUI_Pages.PaymentPage import *
from PyQt5.QtCore import Qt

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main page object
        self.main_page = Ui_MainWindow()
        self.main_page.setupUi(self)

        # Displaying menu on GUI
        pizza_menu(self)
        ingredient_menu(self)
        sauce_menu(self)
        drink_menu(self)

        # Button "add to basket" connection
        self.main_page.button_add_to_basket.clicked.connect(self.add_to_basket)

        # Checkbox connections
        self.main_page.classic_pizza_check.stateChanged.connect(self.choose_checkbox)
        self.main_page.margherita_pizza_check.stateChanged.connect(self.choose_checkbox)
        self.main_page.turk_pizza_check.stateChanged.connect(self.choose_checkbox)
        self.main_page.dominos_pizza_check.stateChanged.connect(self.choose_checkbox)
        self.main_page.ketchup_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.mayo_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.mustard_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.bbq_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.hot_sauce_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.ranch_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.coke_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.fanta_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.pop_soda_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.lemonade_check.stateChanged.connect(self.sauces_beverages_check)
        self.main_page.ayran_check.stateChanged.connect(self.sauces_beverages_check)

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

        # Order history page object
        self.order_history_window = OrderHistoryPage()

        # Payment page object
        self.payment_window = PaymentPage()

        # A signal from payment page to save datas in payment page to the order history database
        self.payment_window.order_history_signal.connect(self.save_to_order_history)

        # Signals from payment page to delete items in basket when payment is successful
        self.payment_window.table_cleaning_signal.connect(self.choose_all)
        self.payment_window.table_cleaning_signal.connect(self.del_chosen_row)

        # Connection to choose all items in basket
        self.main_page.select_all.clicked.connect(self.choose_all)

        # Connection to delete chosen items in basket
        self.main_page.delete_chosen.clicked.connect(self.del_chosen_row)

        # Connection to go to the payment page when confirm the basket
        self.main_page.confirm_basket.clicked.connect(self.go_to_payment)

        # Connection to show order history when clicked on "orders"
        self.main_page.action_past_orders.triggered.connect(self.show_order_history)
        self.main_page.action_past_orders.triggered.connect(self.show_order_history)

        # A list to save order
        self.order = []

    def show_order_history(self):
        self.order_history_window.show()
        self.order_history_window.loadCsv()

    def save_to_order_history(self, info):
        order_info = []
        total_price = 0
        notes_info = []
        table_widget = self.main_page.sepet_table
        payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for row in range(table_widget.rowCount()):
            pizza = table_widget.item(row, 0).text()
            malzemeler = table_widget.item(row, 1).text()
            soslar = table_widget.item(row, 2).text()
            icecekler = table_widget.item(row, 3).text()
            order_info.append(pizza)
            order_info.append(malzemeler)
            order_info.append(soslar)
            order_info.append(icecekler)

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

    def go_to_payment(self):
        all_checked = True
        if self.main_page.sepet_table.rowCount() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen Sepete Ürün Ekleyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return

        for row in range(self.main_page.sepet_table.rowCount()):
            if not self.main_page.sepet_table.cellWidget(row, 6).isChecked():
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

    def add_to_basket(self):
        self.pizza_secim(Tuples.pizza_tuple(self))
        self.malzeme_secimi(Tuples.ingredient_tuple(self))
        self.sos_secim(Tuples.sauce_tuple(self))
        self.icecekler_secim(Tuples.drinks_tuple(self))
        order_dict = self.sozluk_olustur(self.order)
        self.tabloya_veri_ekle(order_dict)
        self.set_default_situation()
        return order_dict

    def pizza_secim(self, pizza_listesi):
        for eleman in pizza_listesi:
            if eleman[2] == True:
                self.order.append(eleman[0:2])
        return self.order

    def malzeme_secimi(self, malzeme_listesi):
        for eleman in malzeme_listesi:
            if eleman[2] == True:
                self.order.append(eleman[0:2])
        return self.order

    def sos_secim(self, sos_listesi):
        for i in sos_listesi:
            if i[2] == True:
                self.order.append(i[0:2])
        return self.order

    def icecekler_secim(self, icecek_listesi):
        for i in icecek_listesi:
            if i[2] == True:
                self.order.append(i[0:2])
        return self.order

    def sozluk_olustur(self, siparis_listesi):

        pizzalar = [classic.get_description(),
                    margherita.get_description(),
                    turk.get_description(),
                    dominos.get_description()]

        malzemeler = [olive.get_description(),
                      mushroom.get_description(),
                      goat_cheese.get_description(),
                      meat.get_description(),
                      onion.get_description(),
                      corn.get_description()]

        soslar = [ketchup.get_description(),
                  mayo.get_description(),
                  mustard.get_description(),
                  bbq.get_description(),
                  hot_sauce.get_description(),
                  ranch.get_description()]

        icecekler = [coke.get_description(),
                     fanta.get_description(),
                     pop_soda.get_description(),
                     lemonade.get_description(),
                     ayran.get_description()]

        sepet_ekle = {"Pizza": "", "Malzemeler": "", "Soslar": "", "İçecekler": "", "Fiyat": 0, "Notlar": ""}
        for veri in siparis_listesi:
            if veri[0] in pizzalar:
                sepet_ekle['Pizza'] = veri[0]
            elif veri[0] in soslar:
                if sepet_ekle["Soslar"] != "":
                    sepet_ekle["Soslar"] += ", "
                sepet_ekle["Soslar"] += veri[0]
            elif veri[0] in icecekler:
                if sepet_ekle["İçecekler"] != "":
                    sepet_ekle["İçecekler"] += ", "
                sepet_ekle["İçecekler"] += veri[0]
            else:
                if sepet_ekle["Malzemeler"] != "":
                    sepet_ekle["Malzemeler"] += ", "
                sepet_ekle["Malzemeler"] += veri[0]
            sepet_ekle["Fiyat"] += veri[1]
            sepet_ekle["Notlar"] = self.main_page.plainTextEdit.toPlainText()
        return sepet_ekle

    def choose_checkbox(self):
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

    def sauces_beverages_check(self):
        check_box_soslar_icecekler = [
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
        for checkbox in check_box_soslar_icecekler:
            if checkbox[1]:
                for other_checkbox in check_box_soslar_icecekler:
                    if other_checkbox[0] != checkbox[0]:
                        self.order.clear()
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box_soslar_icecekler:
                    if other_checkbox[0] != checkbox[0]:
                        self.order.clear()

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
                # checkbox false konumuna geldiğinde spinbox değerini 0 yap
                spinbox[i].setValue(0)

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

    def tabloya_veri_ekle(self, veriler):
        table_widget = self.main_page.sepet_table
        row_count = table_widget.rowCount()
        table_widget.setRowCount(row_count + 1)
        row = row_count

        # yeni bir QTableWidgetItem objesi oluştur
        pizza_item = QTableWidgetItem(veriler["Pizza"])
        malzeme_item = QTableWidgetItem(veriler["Malzemeler"])
        sos_item = QTableWidgetItem(veriler["Soslar"])
        icecekler_item = QTableWidgetItem(veriler["İçecekler"])
        tutar_item = QTableWidgetItem(str(veriler["Fiyat"]))
        notlar_item = QTableWidgetItem(veriler["Notlar"])

        # Tablonun dışarıdan erişilmesini engelleme
        pizza_item.setFlags(pizza_item.flags() ^ Qt.ItemIsEditable)
        malzeme_item.setFlags(malzeme_item.flags() ^ Qt.ItemIsEditable)
        sos_item.setFlags(sos_item.flags() ^ Qt.ItemIsEditable)
        icecekler_item.setFlags(icecekler_item.flags() ^ Qt.ItemIsEditable)
        tutar_item.setFlags(tutar_item.flags() ^ Qt.ItemIsEditable)
        notlar_item.setFlags(notlar_item.flags() ^ Qt.ItemIsEditable)

        # QTableWidgetItem objelerini tableWidget'a ekle
        table_widget.setItem(row, 0, pizza_item)
        table_widget.setItem(row, 1, malzeme_item)
        table_widget.setItem(row, 2, sos_item)
        table_widget.setItem(row, 3, icecekler_item)
        table_widget.setItem(row, 4, tutar_item)
        table_widget.setItem(row, 5, notlar_item)

        #  Sil Sütununa Checkbox eklenmesi
        check_box = QCheckBox()
        self.main_page.sepet_table.setCellWidget(row, 6, check_box)

    def choose_all(self):
        # burada checkbox widgetlerini bulmak için QCheckBox tipi kullanılır
        for row in range(self.main_page.sepet_table.rowCount()):
            checkBox = self.main_page.sepet_table.cellWidget(row, 6)
            if not checkBox.isChecked():
                checkBox.setChecked(True)  # tüm checkbox'ları işaretleyin

    def del_chosen_row(self):
        for row in range(self.main_page.sepet_table.rowCount() - 1, -1, -1):
            if self.main_page.sepet_table.cellWidget(row, 6).isChecked():
                self.main_page.sepet_table.removeRow(row)

    def set_default_situation(self):
        checkBox_list = [
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

        for e in checkBox_list:
            if e.isChecked():
                e.setChecked(False)

        # this code make add note widget default when push the "Sepete Ekle" button
        self.main_page.plainTextEdit.clear()
        self.main_page.plainTextEdit.setPlaceholderText("Not Ekleyin")


#uyg = QApplication(sys.argv)
#pencere = MainPage()
#pencere.show()
#sys.exit(uyg.exec_())

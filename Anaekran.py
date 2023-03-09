import MealMenu
import datetime
import Tuples
from UI_Files.Anaekran_UI import *
from Objects import *
from siparis_gecmisi import *
from odeme import *
from PyQt5.QtCore import Qt
import sys


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        MealMenu.pizza_menu(self)
        MealMenu.ingredient_menu(self)
        MealMenu.sauce_menu(self)
        MealMenu.drink_menu(self)
        self.ui.sepete_ekle_button.clicked.connect(self.sepete_ekle)
        self.ui.klas_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.Mar_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.turk_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.s_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.ketcap_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.mayonez_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.hardal_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.bbq_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.aci_sos_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.ranch_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.kola_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.fanta_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.gazoz_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.limonata_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.ayran_check.stateChanged.connect(self.soslar_icecekler_check)
        self.ui.ketcap_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.mayonez_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.hardal_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.bbq_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.aci_sos_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.ranch_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.kola_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.fanta_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.gazoz_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.limonata_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.ayran_check.stateChanged.connect(self.Auto_increament_spinbox)
        self.ui.spinBox_ketcap_4.valueChanged.connect(self.auto_check)
        self.ui.spinBox_mayonez_4.valueChanged.connect(self.auto_check)
        self.ui.spinBox_hardal_4.valueChanged.connect(self.auto_check)
        self.ui.spinBox_bbq_4.valueChanged.connect(self.auto_check)
        self.ui.spinBox_aci_sos_4.valueChanged.connect(self.auto_check)
        self.ui.spinBox_ranch_4.valueChanged.connect(self.auto_check)
        self.ui.spinBox_KOLA.valueChanged.connect(self.auto_check)
        self.ui.spinBox_FANTA.valueChanged.connect(self.auto_check)
        self.ui.spinBox_GAZOZ.valueChanged.connect(self.auto_check)
        self.ui.spinBox_LMONATA.valueChanged.connect(self.auto_check)
        self.ui.spinBox_AYRAN.valueChanged.connect(self.auto_check)
        self.order_history = Siparis_Gecmisi()
        self.odeme_ekrani = Odeme()
        self.odeme_ekrani.order_history_signal.connect(self.save_to_order_history)
        self.odeme_ekrani.table_cleaning_signal.connect(self.choose_all)
        self.odeme_ekrani.table_cleaning_signal.connect(self.del_chosen_row)
        self.ui.tumunu_sec.clicked.connect(self.choose_all)
        self.ui.secilenleri_sil.clicked.connect(self.del_chosen_row)
        self.ui.sepeti_onayla.clicked.connect(self.go_to_payment)
        self.ui.actionGe_mi_Sipari_lerim.triggered.connect(self.show_order_history)
        self.ui.actionGe_mi_Sipari_lerim.triggered.connect(self.show_order_history)
        self.siparis = []

    def show_order_history(self):
        self.order_history.show()
        self.order_history.loadCsv()

    def save_to_order_history(self, info):
        order_info = []
        total_price = 0
        notes_info = []
        table_widget = self.ui.sepet_table
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

        self.order_history.clear_table()

    def go_to_payment(self):
        all_checked = True
        if self.ui.sepet_table.rowCount() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen Sepete Ürün Ekleyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return

        for row in range(self.ui.sepet_table.rowCount()):
            if not self.ui.sepet_table.cellWidget(row, 6).isChecked():
                all_checked = False
                break

        if all_checked:
            self.odeme_ekrani.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Tüm siparişlerin seçili olması gerek")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()

    def sepete_ekle(self):
        self.pizza_secim(Tuples.pizza_tuple(self))
        self.malzeme_secimi(Tuples.ingredient_tuple(self))
        self.sos_secim(Tuples.sauce_tuple(self))
        self.icecekler_secim(Tuples.drinks_tuple(self))
        order_dict = self.sozluk_olustur(self.siparis)
        self.tabloya_veri_ekle(order_dict)
        self.set_default_situation()
        return order_dict

    def pizza_secim(self, pizza_listesi):
        for eleman in pizza_listesi:
            if eleman[2] == True:
                self.siparis.append(eleman[0:2])
        return self.siparis

    def malzeme_secimi(self, malzeme_listesi):
        for eleman in malzeme_listesi:
            if eleman[2] == True:
                self.siparis.append(eleman[0:2])
        return self.siparis

    def sos_secim(self, sos_listesi):
        for i in sos_listesi:
            if i[2] == True:
                self.siparis.append(i[0:2])
        return self.siparis

    def icecekler_secim(self, icecek_listesi):
        for i in icecek_listesi:
            if i[2] == True:
                self.siparis.append(i[0:2])
        return self.siparis

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
            sepet_ekle["Notlar"] = self.ui.plainTextEdit.toPlainText()
        return sepet_ekle

    def checkBox_secim(self):
        check_box = [
            [self.ui.klas_pizza_check, self.ui.klas_pizza_check.isChecked()],
            [self.ui.Mar_pizza_check, self.ui.Mar_pizza_check.isChecked()],
            [self.ui.turk_pizza_check, self.ui.turk_pizza_check.isChecked()],
            [self.ui.s_pizza_check, self.ui.s_pizza_check.isChecked()]
        ]

        for checkbox in check_box:
            if checkbox[1]:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(False)
                        self.siparis.clear()
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(True)
                    self.siparis.clear()

    def soslar_icecekler_check(self):
        check_box_soslar_icecekler = [
            [self.ui.ketcap_check, self.ui.ketcap_check.isChecked()],
            [self.ui.mayonez_check, self.ui.mayonez_check.isChecked()],
            [self.ui.hardal_check, self.ui.hardal_check.isChecked()],
            [self.ui.bbq_check, self.ui.bbq_check.isChecked()],
            [self.ui.aci_sos_check, self.ui.aci_sos_check.isChecked()],
            [self.ui.ranch_check, self.ui.ranch_check.isChecked()],
            [self.ui.kola_check, self.ui.kola_check.isChecked()],
            [self.ui.fanta_check, self.ui.fanta_check.isChecked()],
            [self.ui.gazoz_check, self.ui.gazoz_check.isChecked()],
            [self.ui.limonata_check, self.ui.limonata_check.isChecked()],
            [self.ui.ayran_check, self.ui.ayran_check.isChecked()]
        ]
        for checkbox in check_box_soslar_icecekler:
            if checkbox[1]:
                for other_checkbox in check_box_soslar_icecekler:
                    if other_checkbox[0] != checkbox[0]:
                        self.siparis.clear()
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box_soslar_icecekler:
                    if other_checkbox[0] != checkbox[0]:
                        self.siparis.clear()

    def Auto_increament_spinbox(self):
        checkBox = [self.ui.ketcap_check,
                    self.ui.mayonez_check,
                    self.ui.hardal_check,
                    self.ui.bbq_check,
                    self.ui.aci_sos_check,
                    self.ui.ranch_check,
                    self.ui.kola_check,
                    self.ui.fanta_check,
                    self.ui.gazoz_check,
                    self.ui.limonata_check,
                    self.ui.ayran_check
                    ]
        spinBox = [self.ui.spinBox_ketcap_4,
                   self.ui.spinBox_mayonez_4,
                   self.ui.spinBox_hardal_4,
                   self.ui.spinBox_bbq_4,
                   self.ui.spinBox_aci_sos_4,
                   self.ui.spinBox_ranch_4,
                   self.ui.spinBox_KOLA,
                   self.ui.spinBox_FANTA,
                   self.ui.spinBox_GAZOZ,
                   self.ui.spinBox_LMONATA,
                   self.ui.spinBox_AYRAN]

        for i, e in enumerate(checkBox):
            if e.isChecked():
                if spinBox[i].value() == 0:
                    spinBox[i].setValue(1)
            else:
                # checkbox false konumuna geldiğinde spinbox değerini 0 yap
                spinBox[i].setValue(0)

    def auto_check(self):
        checkBox = [self.ui.ketcap_check,
                    self.ui.mayonez_check,
                    self.ui.hardal_check,
                    self.ui.bbq_check,
                    self.ui.aci_sos_check,
                    self.ui.ranch_check,
                    self.ui.kola_check,
                    self.ui.fanta_check,
                    self.ui.gazoz_check,
                    self.ui.limonata_check,
                    self.ui.ayran_check
                    ]
        spinBox = [self.ui.spinBox_ketcap_4,
                   self.ui.spinBox_mayonez_4,
                   self.ui.spinBox_hardal_4,
                   self.ui.spinBox_bbq_4,
                   self.ui.spinBox_aci_sos_4,
                   self.ui.spinBox_ranch_4,
                   self.ui.spinBox_KOLA,
                   self.ui.spinBox_FANTA,
                   self.ui.spinBox_GAZOZ,
                   self.ui.spinBox_LMONATA,
                   self.ui.spinBox_AYRAN]

        for i, e in enumerate(spinBox):
            if e.value() > 0:
                checkBox[i].setChecked(True)
            else:
                checkBox[i].setChecked(False)

    def tabloya_veri_ekle(self, veriler):
        table_widget = self.ui.sepet_table
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
        self.ui.sepet_table.setCellWidget(row, 6, check_box)

    def choose_all(self):
        # burada checkbox widgetlerini bulmak için QCheckBox tipi kullanılır
        for row in range(self.ui.sepet_table.rowCount()):
            checkBox = self.ui.sepet_table.cellWidget(row, 6)
            if not checkBox.isChecked():
                checkBox.setChecked(True)  # tüm checkbox'ları işaretleyin

    def del_chosen_row(self):
        for row in range(self.ui.sepet_table.rowCount() - 1, -1, -1):
            if self.ui.sepet_table.cellWidget(row, 6).isChecked():
                self.ui.sepet_table.removeRow(row)

    def set_default_situation(self):
        checkBox_list = [
            self.ui.klas_pizza_check,
            self.ui.Mar_pizza_check,
            self.ui.turk_pizza_check,
            self.ui.s_pizza_check,
            self.ui.zeytin_check,
            self.ui.keci_peyniri_check,
            self.ui.misir_check,
            self.ui.et_check,
            self.ui.sogan_check,
            self.ui.mantar_check,
            self.ui.keci_peyniri_check,
            self.ui.ketcap_check,
            self.ui.mayonez_check,
            self.ui.hardal_check,
            self.ui.bbq_check,
            self.ui.aci_sos_check,
            self.ui.ranch_check,
            self.ui.kola_check,
            self.ui.fanta_check,
            self.ui.gazoz_check,
            self.ui.limonata_check,
            self.ui.ayran_check]

        for e in checkBox_list:
            if e.isChecked():
                e.setChecked(False)

        # this code make add note widget default when push the "Sepete Ekle" button
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setPlaceholderText("Not Ekleyin")


uyg = QApplication(sys.argv)
pencere = MainPage()
pencere.show()
sys.exit(uyg.exec_())

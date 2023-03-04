import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import Menu
from Anaekran_UI import *
from PyQt5.QtCore import Qt
from Product.Ingredient.SubIngredient import Olive, Mushroom, GoatCheese, Meat, Onion, Corn

import pandas as pd

from Product.Pizza.SubPizza import Classic, Turk, Margherita, Dominos

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.pizza_ad_cheB()
        # self.veri_ekle({'pizza': 'margarita Pizza', 'malzeme': 'zeytin, et, mantar', 'fiyat': 87})
        self.ui.sepete_ekle_button.clicked.connect(self.sepete_ekle)
        self.ui.klas_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.Mar_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.turk_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.s_pizza_check.stateChanged.connect(self.checkBox_secim)
        #self.ui.ketcap_check.stateChanged.connect(self.a)
        self.siparis = []



    def sepete_ekle(self):
        a = self.pizza_secim(self.pizza_tuple())
        return print(a)

    def pizza_tuple(self):
        dominos = Dominos("Domino's pizza plain", Menu.Costs.dominos_pizza_cost())
        turk = Turk("Turkish style pizza plain", Menu.Costs.turk_pizza_cost())
        margherita = Margherita("Margherita pizza plain", Menu.Costs.margarita_pizza_cost())
        classic = Classic("Classic pizza plain", Menu.Costs.klasik_pizza_cost())
        pizzalar_tuple = [
            (classic.get_description(), classic.get_cost(), self.ui.klas_pizza_check.isChecked()),
            (margherita.get_description(), margherita.get_cost(), self.ui.Mar_pizza_check.isChecked()),
            (turk.get_description(), turk.get_cost(), self.ui.turk_pizza_check.isChecked()),
            (dominos.get_description(), dominos.get_cost(), self.ui.s_pizza_check.isChecked())
        ]
        return pizzalar_tuple

    def ingredient_tuple(self):
        olive = Olive("Zeytin", Menu.Costs.zeytin_cost())
        mushroom = Mushroom("Mantar", Menu.Costs.mantar_cost())
        goat_cheese = GoatCheese("Keçi Peyniri", Menu.Costs.keci_peyniri_cost())
        meat = Meat("Et", Menu.Costs.et_cost())
        onion = Onion("Sogan", Menu.Costs.sogan_cost())
        corn = Corn("Misir", Menu.Costs.misir_cost())

        ingredient_tuple = [
            (olive.get_description(), olive.get_cost(), self.ui.zeytin_check.isChecked()),
            (mushroom.get_description(), mushroom.get_cost(), self.ui.mantar_check.isChecked()),
            (goat_cheese.get_description(), goat_cheese.get_cost(), self.ui.keci_peyniri_check.isChecked()),
            (meat.get_description(), meat.get_cost(), self.ui.et_check.isChecked()),
            (onion.get_description(), onion.get_cost(), self.ui.sogan_check.isChecked()),
            (corn.get_description(), corn.get_cost(), self.ui.misir_check.isChecked())
        ]
        return ingredient_tuple

    def soslar_tuple(self):
        pass

    def icecekler_tuple(self):
        pass

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
        pass

    def icecekler_secim(self, icecek_listesi):
        pass

    #def a(self):
        #self.ui.spinBox_aci_sos_4.setValue(self..value()+1)


    def sozluk_olustur(self, siparis_listesi):
        sepet_ekle = {"Pizza": "", "Malzemeler": "", "Soslar": "", "İçecekler": "", "Fiyat": 0, "Notlar": ""}
        for veri in siparis_listesi:
            if "Pizza" in veri[0]:
                sepet_ekle['pizza'] = veri[0]
            else:
                if sepet_ekle["malzeme"] != "":
                    sepet_ekle["malzeme"] += ", "
                sepet_ekle["malzeme"] += veri[0]
            sepet_ekle["fiyat"] += veri[1]
        
        #self.ui.plainTextEdit.text()

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
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(True)

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
        checkbox_item = QTableWidgetItem()
        checkbox_item.setCheckState(Qt.Checked)
        table_widget.setItem(row, 6, checkbox_item)


uyg = QApplication(sys.argv)
pencere = MainPage()
pencere.show()
sys.exit(uyg.exec_())

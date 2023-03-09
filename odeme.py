import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from odeme_UI import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt


class Odeme(QMainWindow):
    # this signal sends a signal to main page
    # to save datas to database when push the pay button
    order_history_signal = pyqtSignal(dict)
    # this signal sends a signal to main page
    # to delete datas on order table in main page when push the pay button
    table_cleaning_signal = pyqtSignal()

    def __init__(self):

        super().__init__()
        self.payment = odeme_ui()
        self.payment.setupUi(self)
        self.payment.pay_button.clicked.connect(self.pay)


    def pay(self):

        if not self.name_lastname_check():
            return
        if not self.id_check():
            return
        if not self.card_no_check():
            return
        if not self.password_check():
            return
        info = {"name_lastname": self.payment.name_lastname.text(), "tc": int(self.payment.id_number.text()),
                "card_no": int(self.payment.card_number.text()), "sifre": str(self.payment.password_edit.text())}
        self.order_history_signal.emit(info)
        self.table_cleaning_signal.emit()
        self.close()

    def name_lastname_check(self):
        name_lastname = self.payment.name_lastname.text().capitalize()
        split_name_lastname = name_lastname.split()
        turkish_chars = "İıÖöÜüÇçŞşĞğ"
        if all(c.isalpha() or c in turkish_chars for c in split_name_lastname):
            return True
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Ad Soyad Bilgisi Hatalı, Tekrar Deneyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return False

    def id_check(self):
        id_no = self.payment.id_number.text()
        if (len(id_no) != 11) or not all(c.isdigit() for c in id_no) or (id_no[0] == '0') or (sum(map(int, id_no[:10])) % 10 != int(id_no[10])) or ((((7 * sum(map(int, id_no[:9][-1::-2]))) - sum(map(int, id_no[:9][-2::-2]))) % 10 != int(id_no[9]))):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("TC Kimlik Numarası Hatalı, Tekrar Deneyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return False
        else:
            return True

    def card_no_check(self):
        card_num = self.payment.card_number.text()
        card_num_list = [int(num) for num in card_num]
        if len(card_num_list) != 16:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Kart Numarası Hatalı, Tekrar Deneyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return False
        else:
            return True 
        
    def password_check(self):
        password = self.payment.password_edit.text()
        passwor_list = [e for e in password]
        if len(passwor_list) != 4 or not all(c.isdigit() for c in password):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Şifre Hatalı, Tekrar Deneyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return False
        else:
            return True











        

#uyg_2 = QApplication(sys.argv)
#pencere_2 = Odeme()
#pencere_2.show()
#sys.exit(uyg_2.exec_())

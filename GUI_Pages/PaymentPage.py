from PyQt5.QtWidgets import *
from UI_Files.PaymentPageUI import *
from PyQt5.QtCore import pyqtSignal


class PaymentPage(QMainWindow):
    # This signal sends a signal to main page
    # To save datas to database when push the pay button
    order_history_signal = pyqtSignal(dict)
    # This signal sends a signal to main page
    # To delete datas on order table in main page when push the pay button
    table_cleaning_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Payment page object
        self.payment_page = PaymentPage_UI()
        self.payment_page.setupUi(self)

        # Connection
        # Pay button
        self.payment_page.pay_button.clicked.connect(self.pay)

    # This function checks if payment information are valid or not,
    # deletes all datas in payment page if payment is successful,
    # closes the payment page if payments is successful,
    # sends a signal in order to save payment datas to database to main page,
    # sends a signal in order to delete orders in basket table
    def pay(self):
        if not self.name_lastname_check():
            return
        if not self.id_check():
            return
        if not self.card_no_check():
            return
        if not self.password_check():
            return
        info = {"name_lastname": self.payment_page.name_lastname.text(), "tc": int(self.payment_page.id_number.text()),
                "card_no": str(self.payment_page.card_number.text()), "sifre": str(self.payment_page.password_edit.text())}
        self.order_history_signal.emit(info)
        self.table_cleaning_signal.emit()
        # these methods clean the data on payment screen when the payment completed
        self.payment_page.name_lastname.clear()
        self.payment_page.id_number.clear()
        self.payment_page.card_number.clear()
        self.payment_page.password_edit.clear()
        self.close()

    # This function checks name of the customer is valid or not
    def name_lastname_check(self):
        name_lastname = self.payment_page.name_lastname.text().capitalize()
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

    # This function checks id card number of the customer is valid or not
    def id_check(self):
        id_no = self.payment_page.id_number.text()
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

    # This function checks credit card number of the customer is valid or not
    def card_no_check(self):
        card_num = self.payment_page.card_number.text()
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

    # This function checks credit card password of the customer is valid or not
    def password_check(self):
        password = self.payment_page.password_edit.text()
        password_list = [e for e in password]
        if len(password_list) != 4 or not all(c.isdigit() for c in password):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Şifre Hatalı, Tekrar Deneyin")
            msg.setWindowTitle("HATA")
            ok_button = msg.addButton("Tamam", QMessageBox.AcceptRole)
            msg.exec_()
            return False
        else:
            return True


import pandas as pd
import datetime
from Anaekran import MainPage

def tc_kontrol(value):
    value = str(value)
    if not len(value) == 11:
        return False
    if not value.isdigit():
        return False
    if int(value[0]) == 0:
        return False
    digits = [int(d) for d in str(value)]
    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    return True

class Payment:

    def __init__(self):
        self.deneme = 0
        self.payment_history = pd.read_csv("payment_history.csv")
        self.tutar()
        self.order()
        self.notlar()
        self.tc()
        self.name()
        self.kart_no()
        self.sifre()
        self.odeme_yap()
        self.isim = self.name()

    def tutar(self):
        a = MainPage()
        sepet = a.siparis

        tutar = sepet["Fiyat"]
        #tutar = 25

        return print(tutar)
    def order(self):
        a = MainPage()
        sepet = a.siparis
        pizza = sepet["Pizza"]
        malzemeler = sepet["Malzemeler"]
        soslar = sepet["Soslar"]
        icecekler = sepet["İçecekler"]

        order = f" {pizza}, {malzemeler}, {soslar}, {icecekler}"
        #order = "Margarita, kola, ayran, mayonez,et"
        return print(order)

    def notlar(self):
        a = MainPage()
        sepet = a.siparis

        notlar = sepet["Notlar"]
        #notlar = "Acılı olsun"
        return print(notlar)

    def tc(self):
        id_number = input("Kimlik numarası:  ")
        if not tc_kontrol(id_number):
            self.deneme += 1
            print("Kimlik no hatalı!")

    def name(self):
        name = str(input("İsim: "))
        if not isinstance(name, str):
            self.deneme += 1
            print("Kart üzerindeki isim hatalı!")
        return print(name)

    def kart_no(self):
        card_number = input("Kart numarası:  ")
        if len(card_number) != 16:
            self.deneme += 1
            print("Kart numarası hatalı!")
        return print(card_number)
    def sifre(self):
        password = input("Kart şifresi: ")
        if len(password) != 4:
            self.deneme += 1
            print("Kart şifresi hatalı!")

    def odeme_yap(self):
        if self.deneme == 0:
            print("Ödeme başarılı.")
            payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payment_info = {"Payment": "Successful",
                            "Date/Time": payment_date,
                            "Customer": self.isim,
                            "Total Price": float(self.tutar()),
                            "Card Number": self.kart_no,
                            "Order": self.order,
                            "Notlar": self.notlar
                            }
            self.payment_history = self.payment_history.append(payment_info, ignore_index=True)
            self.payment_history.to_csv("payment_history.csv", index=False)

        if self.deneme != 0:
            print("Ödeme başarısız. Lütfen tekrar deneyin.")
            payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payment_info = {"Payment": "Failed",
                            "Date/Time": payment_date,
                            "Customer": self.name,
                            "Total Price": float(self.tutar()),
                            "Card Number": self.kart_no,
                            "Order": self.order,
                            "Notlar": self.notlar
                            }
            self.payment_history = self.payment_history.append(payment_info, ignore_index=True)
            self.payment_history.to_csv("payment_history.csv", index=False)

a = Payment()

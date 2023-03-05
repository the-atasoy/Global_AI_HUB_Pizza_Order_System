import pandas as pd
import datetime
# from Anaekran import MainPage

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
        self.payment_history = pd.read_csv("payment_history.csv")

    def kart_bilgisi_al(self):

        #a = MainPage.sozluk_olustur()
        # buraya costların toplamını çekeceğiz.
        tutar = float(input("Tutar: "))

        # pizza = a["Pizza"]
        #malzemeler = a["Malzemeler"]
        #soslar = a["Soslar"]
        #icecekler = a["İçecekler"]

        deneme = 0


        #buraya sipariş toplanmını çekeceğiz
        # order = f" {pizza}, {malzemeler}, {soslar}, {icecekler}"
        order = "Turk Pizza, Mayonez, Ketçap"

        notlar = "İyi kızarsın lütfen"


        id_number = input("Kimlik numarası:  ")
        if not tc_kontrol(id_number):
            deneme += 1
            print("Kimlik no hatalı!")

        name = str(input("İsim: "))
        if not isinstance(name, str):
            deneme += 1
            print("Kart üzerindeki isim hatalı!")

        card_number = input("Kart numarası:  ")
        if len(card_number) != 16:
            deneme += 1
            print("Kart numarası hatalı!")

        password = input("Kart şifresi: ")
        if len(password) != 4:
            deneme += 1
            print("Kart şifresi hatalı!")

        if deneme == 0:
            print("Ödeme başarılı.")
            payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payment_info = {"Payment": "Successful",
                            "Date/Time": payment_date,
                            "Customer": name,
                            "Total Price": float(tutar),
                            "Card Number": card_number,
                            "Order": order,
                            "Notlar": notlar
                            }
            self.payment_history = self.payment_history.append(payment_info, ignore_index=True)
            self.payment_history.to_csv("payment_history.csv", index=False)

        if deneme != 0:
            print("Ödeme başarısız. Lütfen tekrar deneyin.")
            payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payment_info = {"Payment": "Failed",
                            "Date/Time": payment_date,
                            "Customer": name,
                            "Total Price": float(tutar),
                            "Card Number": card_number,
                            "Order": order,
                            "Notlar": notlar
                            }
            self.payment_history = self.payment_history.append(payment_info, ignore_index=True)
            self.payment_history.to_csv("payment_history.csv", index=False)
a = Payment()
a.kart_bilgisi_al()
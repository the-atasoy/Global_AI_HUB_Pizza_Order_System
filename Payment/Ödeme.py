import pandas as pd
import datetime

class Payment:
    def __init__(self):
        self.payment_history = pd.read_csv("payment_history.csv")

    def kart_bilgisi_al(self):
        # buraya costların toplamını bağlayacağız get_cost buraya yazılabilir.
        tutar = float(input("Tutar: "))
        deneme = 0

        id_number = input("Kimlik numarası:  ")
        if len(id_number) != 11:
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
                            "Total Price": tutar,
                            "Card Number": card_number,
                            }
            self.payment_history = self.payment_history.append(payment_info, ignore_index=True)
            self.payment_history.to_csv("payment_history.csv", index=False)

        if deneme != 0:
            print("Ödeme başarısız. Lütfen tekrar deneyin.")
            payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payment_info = {"Payment": "Failed",
                            "Date/Time": payment_date,
                            "Customer": name,
                            "Total Price": tutar,
                            "Card Number": card_number,
                            }
            self.payment_history = self.payment_history.append(payment_info, ignore_index=True)
            self.payment_history.to_csv("payment_history.csv", index=False)

a = Payment()
a.kart_bilgisi_al()
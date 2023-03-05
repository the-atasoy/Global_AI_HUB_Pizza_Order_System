import pandas as pd
import datetime

class Payment:
    def __init__(self):
        self.payment_history = pd.read_csv("payment_history.csv")

    def kart_bilgisi_al(self):
        # buraya costların toplamını bağlayacağız get_cost buraya yazılabilir.
        tutar = float(input("Please enter cost: "))
        deneme = 0

        id_number = input("Please enter your ID Number:  ")
        if len(id_number) != 11:
            deneme += 1

        name = input("Please enter your name: ")

        card_number = input("Please enter card number:  ")
        if len(card_number) != 16:
            deneme += 1

        password = input("Please enter 4 digit password:")
        if len(password) != 4:
            deneme += 1

        if deneme == 0:
            print("Payment successful.")
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
            print("Payment Failed. Please try again")
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
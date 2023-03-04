import datetime

import pandas as pd


def kart_bilgisi_al():
    # buraya costların toplamını bağlayacağız get_cost buraya yazılabilir.
    tutar = float(input("Please enter cost: "))
    deneme = 0

    id_number = input("Please enter your ID Number:  ")
    if len(id_number) != 11:
        deneme += 1

    name = input("Please enter your name: ")
    if name != str:
        deneme += 1

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
                        "Date/Time": [payment_date],
                        "Customer": [name],
                        "Total Price": [tutar],
                        "Card Number": [card_number],
                        }
        payment_history = pd.DataFrame(payment_info)
        payment_history.to_csv("payment_history.cvs", index=False)

    if deneme != 0:
        print("Payment Failed. Please try again")
        payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payment_info = {"Payment": "Failed",
                        "Date/Time": [payment_date],
                        "Customer": [name],
                        "Total Price": [tutar],
                        "Card Number": [card_number],
                        }
        payment_history = pd.DataFrame(payment_info)
        payment_history.to_csv("payment_history.cvs", index=False)


kart_bilgisi_al()

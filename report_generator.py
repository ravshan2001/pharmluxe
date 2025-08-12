from datetime import datetime
from config import ONE_C_PASS, ONE_C_USER, BOT_TOKEN, ONE_C_URL
import requests
import os

today = datetime.today().strftime("%Y-%m-%d")

def get_todays_sales():
    try:
        response = requests.get(ONE_C_URL+'/get_todays_trade', auth=(ONE_C_USER, ONE_C_PASS), timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return e
    last_response = f"{response.json()['sum']:,.2f}"
    return f"{today} savdo {last_response} so'm"


# 📍 Viloyatlardagi savdo (test ma'lumotlari)
def get_trade_in_the_provinces():
    try:
        response = requests.get(ONE_C_URL + '/get_trade_in_the_provinces', auth=(ONE_C_USER, ONE_C_PASS), timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return e
    table = ''
    table += "-" * 35 + "\n"

    j = 1
    for i in response.json()['regions']:
        j = j+1
        if j%2==0:
            continue
        else:
            table += f"{i['name']:<20} {i['sum']:>15,}\n"
        print(j)
    return table

# 📦 Buyurtmalar soni
def get_order_count():
    try:
        response = requests.get(ONE_C_URL+'/get_the_numbers_of_orders', auth=(ONE_C_USER, ONE_C_PASS), timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return e
    last_response = f"{response.json()['quantity']:,.2f}"
    return f"{today} kuni jami buyurtmalar soni: {last_response} ta"


def get_money_amount():
    try:
        response = requests.get(ONE_C_URL+'/get_sum_received', auth=(ONE_C_USER, ONE_C_PASS), timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return e
    last_response = f"{response.json()['sum']:,.2f}"
    return f"{today}  tushgan so'mma: {last_response} so'm"


def get_amount_of_debt():
    try:
        response = requests.get(ONE_C_URL+'/get_amount_of_debt', auth=(ONE_C_USER, ONE_C_PASS), timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return e
    last_response = f"{response.json()['sum']:,.2f}"
    return f"{today}  kungi qarzdorlik: {last_response} so'm"
    return True




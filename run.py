import requests
from config import ONE_C_USER, ONE_C_PASS

url = "https://1c-uz.pharmlux.uz/phl/hs/bot_api/get_trade_in_the_provinces"

response = requests.get(url, auth=(ONE_C_USER, ONE_C_PASS), timeout=10)
print(response.json())



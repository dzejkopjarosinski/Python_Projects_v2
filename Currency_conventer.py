from requests import get
from pprint import PrettyPrinter

#Get the API Key
BASE_URL = "https://free.currconv.com/"
API_KEY = "187e7a5b0c9eb1d25315"

printer = PrettyPrinter()

# Go tu url, save data in a json format, then create sorted list from that data
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()

    return data


# Print currency's Ticker, Name and Symbol 
def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")

        print(f"{_id} - {name} - {symbol}")


data = get_currencies()
print_currencies(data)

import http.client
import json

# Function to get real-time exchange rate
def get_exchange_rate(from_currency, to_currency):
    try:
        conn = http.client.HTTPSConnection("api.exchangerate-api.com")
        conn.request("GET", f"/v4/latest/{from_currency}")
        response = conn.getresponse()
        data = response.read()
        rates = json.loads(data)

        if to_currency in rates["rates"]:
            return rates["rates"][to_currency]
        else:
            print("Invalid currency code.")
            return None
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion failed.")

# User input
amount = float(input("Enter amount to convert: "))
from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()

# Perform conversion
convert_currency(amount,from_currency,to_currency)
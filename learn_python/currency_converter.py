import requests

#exchange rate API 
API_KEY = "f03e7128cedf85c5acc84a4f"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def fetch_rates(base_currency):
    url = BASE_URL + base_currency
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["conversion_rates"]
    else:
        print("Error fetching data!")
        return None


def convert_currency(base_currency, target_currency, amount):
    rates = fetch_rates(base_currency)
    if rates and target_currency in rates:
        conversion_rate = rates[target_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        print("Target currency not available")
        return None


def main():
    print("Welcome to the Currency Converter!")
    base_currency = str(input("Enter the base currency: (USD, EUR, etc): "))
    target_currency = str(input("Enter the target currency in the same format (USD, EUR, etc): "))
    amount = float(input("Enter the amount to convert: "))

    result = convert_currency(base_currency, target_currency, amount)

    if result is not None:
        print(f"{amount} {base_currency} = {result:.2f} {target_currency}")
    else:
        print("Conversion failed")



if __name__=="__main__":
    main()
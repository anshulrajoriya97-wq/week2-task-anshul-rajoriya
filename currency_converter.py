import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency(amount, from_currency, to_currency):
    response = requests.get(API_URL + from_currency)
    if response.status_code != 200:
        print("Error fetching exchange rates.")
        return None
    
    data = response.json()
    if to_currency not in data["rates"]:
        print("Currency not supported.")
        return None

    rate = data["rates"][to_currency]
    return amount * rate

def main():
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., INR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    if result:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()

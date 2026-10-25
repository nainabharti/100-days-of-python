import requests
print("=" * 35)
print("       CURRENCY CONVERTER     ")
print("=" * 35)
print("Examples: USD, INR, EUR, GBP, JPY")
while True:
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            from_currency = input("Convert from (e.g. USD): ").strip().upper()
            to_currency = input("Convert to (e.g. INR): ").strip().upper()
            if not from_currency.isalpha() or len(from_currency) != 3:
                print("Invalid source currency code.")
            elif not to_currency.isalpha() or len(to_currency) != 3:
                print("Invalid target currency code.")
            else:
                try:
                    url = f"https://open.er-api.com/v6/latest/{from_currency}"

                    response = requests.get(url, timeout=10)
                    response.raise_for_status()
                    data = response.json()

                    if data.get("result") == "success":
                        rates = data["rates"]

                        if to_currency in rates:
                            exchange_rate = rates[to_currency]
                            converted_amount = amount * exchange_rate

                            print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
                        else:
                            print("Target currency not supported.")
                    else:
                        print("Unable to fetch exchange rates.")

                except requests.exceptions.RequestException:
                    print("Network error! Please check your internet connection and try again.")
                    print("\nAmount: ", amount)
                    print("From: ", from_currency)
                    print("To: ", to_currency)
                    print("API URL:", url)
    except ValueError:
        print("Please enter a valid numeric amount.")
    choice = input("\nDo you want to convert again? (yes/no): ").strip().lower()
    if choice not in ("yes", "y"):
        print("Thank you for using Currency Converter ! ")
        break

import requests

# Base URL for the currency conversion API
API_BASE_URL = "https://api.frankfurter.app"

def get_latest_rates(base_currency):
    """
    Fetches the latest exchange rates for a given base currency.
    Returns the JSON response from the API or None if an error occurs.
    """
    try:
        # Construct the full API URL
        url = f"{API_BASE_URL}/latest?from={base_currency}"
        response = requests.get(url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def main():
    """
    Main function to run the currency converter.
    """
    print("--- CLI Currency Converter ---")

    # Get user input with basic validation
    try:
        amount_str = input("Enter the amount to convert: ")
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    base_currency = input("Enter the source currency (e.g., USD, EUR, INR): ").upper()
    target_currency = input("Enter the target currency (e.g., USD, EUR, INR): ").upper()

    print(f"\nFetching exchange rates for {base_currency}...")
    
    # Fetch the exchange rate data
    data = get_latest_rates(base_currency)

    if data:
        # Check if the target currency is available in the API response
        if target_currency in data['rates']:
            rate = data['rates'][target_currency]
            converted_amount = amount * rate
            print("-" * 25)
            print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
            print(f"Current rate (as of {data['date']}): 1 {base_currency} = {rate} {target_currency}")
            print("-" * 25)
        else:
            print(f"Error: The target currency '{target_currency}' is not valid or supported.")
            print(f"Available currencies are: {', '.join(data['rates'].keys())}")

if __name__ == "__main__":
    main()
# CLI Currency Converter

A simple but powerful command-line tool to get real-time currency exchange rates using Python. This project utilizes the free [Frankfurter API](https://www.frankfurter.app/docs/) to fetch the latest conversion rates.

## Features

-   Convert any amount from a source currency to a target currency.
-   Uses real-time exchange rate data.
-   Simple and intuitive command-line interface.
-   Handles invalid inputs and API errors gracefully.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/aayush-0131/currency-converter.git](https://github.com/your-username/currency-converter.git)
    cd currency-converter
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file. See below.)*

## Usage

Run the script from your terminal:

```bash
python main.py

```

The application will then prompt you to enter the amount, the source currency code (e.g., USD), and the target currency code (e.g., INR).

Example



--- CLI Currency Converter ---




Enter the amount to convert: 100




Enter the source currency (e.g., USD, EUR, INR): USD





Enter the target currency (e.g., USD, EUR, INR): INR





Fetching exchange rates for USD...




-------------------------



100.0 USD is equal to 8343.30 INR





Current rate (as of 2025-09-17): 1 USD = 83.433 INR
-------------------------

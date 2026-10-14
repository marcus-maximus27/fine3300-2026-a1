"""Bank of Canada Exchange Rate Calculator (CAD <-> USD)."""

import csv
import os

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "BankOfCanadaExchangeRate.2026.csv")
RATE_COLUMN = "FXAUSDCAD"
CURRENCIES = ("CAD", "USD")


def get_latest_rate(path=CSV_FILE):
    """Return (date, rate) for the most recent row with a USD/CAD rate."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [row for row in csv.DictReader(f) if row.get(RATE_COLUMN)]
    latest = max(rows, key=lambda row: row["Date"])
    return latest["Date"], float(latest[RATE_COLUMN])


def prompt_amount():
    while True:
        value = input("Enter the amount: ").replace(",", "").replace("$", "").strip()
        try:
            amount = float(value)
            if amount >= 0:
                return amount
        except ValueError:
            pass
        print("Please enter a valid, non-negative number.")


def prompt_currency(label):
    while True:
        currency = input(f"Enter the '{label}' currency (CAD or USD): ").strip().upper()
        if currency in CURRENCIES:
            return currency
        print("Please enter either CAD or USD.")


def convert(amount, from_currency, to_currency, usd_cad_rate):
    if from_currency == to_currency:
        return amount
    if from_currency == "USD":
        return amount * usd_cad_rate
    return amount / usd_cad_rate


def main():
    rate_date, rate = get_latest_rate()
    print("Bank of Canada Exchange Rate Calculator")
    print(f"Latest rate ({rate_date}): 1 USD = {rate} CAD\n")

    amount = prompt_amount()
    from_currency = prompt_currency("from")
    to_currency = prompt_currency("to")

    result = convert(amount, from_currency, to_currency, rate)
    print(f"\n${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")


if __name__ == "__main__":
    main()

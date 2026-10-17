"""
Bank of Canada Exchange Rate Calculator (CAD <-> USD)

Reads the latest USD/CAD exchange rate (column 'FXAUSDCAD') from a Bank of
Canada CSV file and converts an amount between Canadian and US dollars.
"""

# The csv module parses the Bank of Canada exchange rate file.
import csv
# The os module builds a file path relative to this script's folder.
import os


class ExchangeRates:
    """Holds the latest USD/CAD rate from a CSV file and converts amounts."""

    # Name of the CSV column that holds the USD to CAD rate.
    RATE_COLUMN = "FXAUSDCAD"
    # The only two currencies this calculator supports.
    CURRENCIES = ("CAD", "USD")

    def __init__(self, file_name):
        """Store the file name and read the latest USD/CAD rate from it."""
        self.file_name = file_name
        # Read the date and rate once when the object is created.
        self.rate_date, self.rate = self._read_latest_rate()

    def _read_latest_rate(self):
        """Return (date, rate) from the most recent row that has a rate."""
        # 'utf-8-sig' skips the hidden byte-order mark at the start of the
        # file, so the first column header is read as 'Date'.
        with open(self.file_name, newline="", encoding="utf-8-sig") as file:
            # Keep only the rows where the USD/CAD rate is not blank.
            rows = [row for row in csv.DictReader(file) if row.get(self.RATE_COLUMN)]

        # Dates are in YYYY-MM-DD format, so the largest one is the latest.
        latest_row = max(rows, key=lambda row: row["Date"])
        return latest_row["Date"], float(latest_row[self.RATE_COLUMN])

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency (USD or CAD) to the other."""
        # Accept lowercase input such as 'usd'.
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        # Reject any currency other than CAD or USD.
        if from_currency not in self.CURRENCIES or to_currency not in self.CURRENCIES:
            raise ValueError("Currency must be CAD or USD.")

        # Same currency: the amount stays the same.
        if from_currency == to_currency:
            return amount
        # The rate is CAD per 1 USD, so USD to CAD multiplies by it.
        if from_currency == "USD":
            return amount * self.rate
        # CAD to USD divides by it.
        return amount / self.rate


def prompt_amount():
    """Ask for the amount until the user enters a valid, non-negative number."""
    while True:
        # Remove commas and dollar signs so inputs like '$100,000' work.
        value = input("Enter the amount: ").replace(",", "").replace("$", "").strip()
        try:
            amount = float(value)
            if amount >= 0:
                return amount
        except ValueError:
            pass
        print("Please enter a valid, non-negative number.")


def prompt_currency(label):
    """Ask for a currency until the user enters CAD or USD."""
    while True:
        currency = input(f"Enter the '{label}' currency (CAD or USD): ").strip().upper()
        if currency in ExchangeRates.CURRENCIES:
            return currency
        print("Please enter either CAD or USD.")


def main():
    # The CSV file is expected in the same folder as this script.
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "BankOfCanadaExchangeRate.2026.csv")

    # Create the ExchangeRates object, which reads the latest rate.
    rates = ExchangeRates(file_name)
    print("Bank of Canada Exchange Rate Calculator")
    print(f"Latest rate ({rates.rate_date}): 1 USD = {rates.rate} CAD\n")

    # Prompt the user for the amount and the 'from' and 'to' currencies.
    amount = prompt_amount()
    from_currency = prompt_currency("from")
    to_currency = prompt_currency("to")

    # Convert the amount using the latest rate.
    result = rates.convert(amount, from_currency, to_currency)

    # Round to the nearest penny, with dollar signs, thousands separators
    # and currency codes, e.g. '$100,000.00 USD = $139,780.00 CAD'.
    print(f"\n${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")


# Run the calculator only when this file is run directly.
if __name__ == "__main__":
    main()

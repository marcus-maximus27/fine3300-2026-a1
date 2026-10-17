'''
ExchangeRates

Author: Marcus Maximus Reyes
Course: FINE 3300 (Fall 2026)
Assignment 1

This is a Python script for an exchange rate calculator based on the latest annual exchange rates
from the Bank of Canada. The script reads the exchange rates from a CSV file and allows the user to convert between Canadian Dollars (CAD) and US Dollars (USD).

Sources:
    - FINE 3300 Lecture #4 class examples (Bond.py, Lottery.py): class structure
    = Python csv module documentation: https://docs.python.org/3/library/csv.html
    - Python format specification: https://docs.python.org/3/library/string.html#format-specification-mini-language
    - Python input() example (linked in assignment): https://cs.stanford.edu/people/nick/py/python-input.html
'''

import csv # Used to read the csv file containing the exchange rates

# Create class for exchange rates
class ExchangeRates:

    def __init__(self, filename): # Create constructor to read the exchange rates from a CSV file
        with open(filename) as fx_file:
            reader = csv.DictReader(fx_file) # Read each row as a dictionary with the column headers as keys (see csv docs in Sources)
            for row in reader:
                self.__rate = float(row['FXAUSDCAD']) # Overwritten each row, but the last row will be the most recent exchange rate

    def get_rate(self): # Create method to get the exchange rate
        return self.__rate

    def convert(self, amount, from_currency, to_currency): # Create method to convert between CAD and USD
        if from_currency == 'CAD' and to_currency == 'USD':
            return amount / self.__rate
        elif from_currency == 'USD' and to_currency == 'CAD':
            return amount * self.__rate
        else:
            raise ValueError("Please specify either CAD or USD for conversion.")

# Create main function to test the class
if __name__ == "__main__":
    aang = ExchangeRates('BankOfCanadaExchangeRate.2026.csv') # Create an instance of the ExchangeRates class

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (CAD or USD): ")
    to_currency = input("Enter the currency to convert to (CAD or USD): ")

    converted_amount = aang.convert(amount, from_currency, to_currency)

    # Prints the converted amount with 2 decimal places
    print("The converted amount is ${:,.2f} {}".format(converted_amount, to_currency))
# ExchangeRates
# 
# This is the Python script for an exchange rate calculator based on the latest annual exchange rates from the Bank of Canada

import csv # Used to read the csv file containing the exchange rates

class ExchangeRates: # Create class for exchange rates

    def __init__(self, filename): # Create constructor to read the exchange rates from a CSV file
        with open(filename) as fx_file:
            reader = csv.DictReader(fx_file)
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


if __name__ == "__main__": # Create main function to test the class
    aang = ExchangeRates('BankOfCanadaExchangeRate.2026.csv') # Create an instance of the ExchangeRates class

    rate = aang.get_rate()
    converted_amount = aang.convert(100000, 'USD', 'CAD')

    # print("The exchange rate is {:.4f}".format(rate))
    print("The converted amount is {:.2f}".format(converted_amount))

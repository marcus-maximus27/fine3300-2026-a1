# ExchangeRates
# 
# This is the Python script for an exchange rate calculator based on the latest annual exchange rates from the Bank of Canada

import csv

# Open the CSV file and read the exchange rates
with open('BankofCanadaExchangeRate.2026.csv') as fx_file:
    reader = csv.DictReader(fx_file)
    for row in reader:
        print(row['FXAUSDCAD'])

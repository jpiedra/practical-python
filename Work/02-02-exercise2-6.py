# report.py
#
# Exercise 2.6
# - Now modify the function from 2.5 so that it reads from 'prices.csv'
# - Read the data from that file, into a dictionary container, rather than a list of dictionaries...
# - The key for each element in your container is the stock symbol
# - The value for each element in your container is the price of said stock
import csv, sys
from pprint import pprint

def read_prices(filename):
    '''
    arguments
        filename: path to the CSV file to read for processing total cost
    return values
        portfolio: a list of tuples, built using the data from your CSV file
    '''
    # always set counters, or other variables, first!
    portfolio = {}
    
    try:
        file = open(filename, 'r')
        rows = csv.reader(file)
        
        # prices.csv does not have a header...

        for row in rows:
            if len(row) == 2: # to account for that last 'blank' line
                portfolio[row[0]] = float(row[1])

        file.close()
    except OSError:
        print(f'Error opening file: {filename}')

    # send the return value last!
    return portfolio

# modify this version so it also reads arguments from the command line...
portfolio = read_prices('Data/prices.csv')
pprint(portfolio) # 'pretty print', requires import of pprint module


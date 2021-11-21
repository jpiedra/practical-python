# report.py
#
# Exercise 2.5
# - Take the function you wrote in Exercise 2.4 and modify it to represent each stock in the portfolio with a dictionary instead of a tuple
# - Use the field names 'name', 'shares', and 'price'
import csv, sys, pprint

def read_portfolio(filename):
    '''
    arguments
        filename: path to the CSV file to read for processing total cost
    return values
        portfolio: a list of tuples, built using the data from your CSV file
    '''
    # always set counters, or other variables, first!
    portfolio = []
    
    try:
        file = open(filename)
        rows = csv.reader(file)
        
        # skip headers
        headers = next(rows)

        for row in rows:
            try:
                temp = { 
                    'name': row[0], 
                    'shares': int(row[1]), 
                    'price': float(row[2]),
                }
                portfolio.append(temp)
            except ValueError:
                print(f'Could not process row: {row}')

        file.close()
    except OSError:
        print(f'Error opening file: {filename}')

    # send the return value last!
    return portfolio

# modify this version so it also reads arguments from the command line...
portfolio = read_portfolio('Data/portfolio.csv')
pprint.pprint(portfolio) # 'pretty print', requires import of pprint module

total = 0.0

for name, shares, price in portfolio:   # use tuple unpacking for more readable code!
    total += shares*price

total
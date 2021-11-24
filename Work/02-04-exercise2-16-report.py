# report.py
#
# Exercise 2.4
import csv, sys

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

        for line, row in enumerate(rows):
            try:
                temp = dict(zip(headers, row))
                portfolio.append(temp)
            except:
                print(f'Line {line}: Could not process row: {row}')

        file.close()
    except OSError:
        print(f'Error opening file: {filename}')

    # send the return value last!
    return portfolio

# modify this version so it also reads arguments from the command line...
portfolio = read_portfolio('Data/portfolio.csv')
portfolio

total = 0.0

for data in portfolio:   # use tuple unpacking for more readable code!
    total += int(data['shares']) * float(data['price'])

print(total)
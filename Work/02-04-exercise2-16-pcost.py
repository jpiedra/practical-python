# Using enumerate(), print a warning with the line number every time a row with missing data is found in 'Data/missing.csv'
# Then, ALSO use zip() and dict() to create a temporary object we can then use to reference values for math by column name, NOT positional index
# Modify pcost.py to do this...
#
# pcost.py
#
# Exercise 2.15
import csv, sys

def portfolio_cost(filename):
    '''
    Calculates total cost to buy all shares as processed from a CSV file
        arguments
            filename: path to the CSV file to read for processing total cost
        return values
            total: total cost to buy all shares processed from filename
    '''
    # always set counters, or other variables, first!
    total = 0
    product = 0

    file = open(filename)
    rows = csv.reader(file)
    
    # skip headers
    headers = next(rows)

    for line, row in enumerate(rows):
        try:
            temp = dict(zip(headers, row))  # We no longer use indexes to reference the shares purchase and the price!
            product = int(temp['shares']) * float(temp['price'])
            total += product
        except:
            print(f'Line {line}: Could not process row: {row}')

    file.close()

    # send the return value last!
    return total

# modify this version so it also reads arguments from the command line...
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: ${cost}')

'''
We can run this same program on different files, and it will work
so long as the columns we're using for calculations (shares, price) are present in the .csv file:
python .\02-04-exercise2-16-pcost.py 'Data\missing.csv'
python .\02-04-exercise2-16-pcost.py 'Data\portfoliodate.csv'
'''
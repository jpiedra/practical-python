# pcost.py
#
# Exercise 1.27
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
    
    try:
        file = open(filename)
        rows = csv.reader(file)
        
        # skip headers
        headers = next(rows)

        for row in rows:
            try:
                product = int(row[1]) * float(row[2])
                total += product
            except ValueError:
                print(f'Could not process row: {row}')

        file.close()
    except OSError:
        print(f'Error opening file: {filename}')

    # send the return value last!
    return total

# modify this version so it also reads arguments from the command line...
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: ${cost}')
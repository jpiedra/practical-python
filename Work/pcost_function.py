# pcost.py
#
# Exercise 1.27

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
        file = open(filename,'rt')
        
        # skip headers
        headers = next(file)

        for line in file:
            fields = line.split(',')
            try:
                product = int(fields[1]) * float(fields[2])
                total += product
            except ValueError:
                print(f'Could not process line: {line}')

        file.close()
    except OSError:
        print(f'Error opening file: {filename}')

    # send the return value last!
    return total

# use the function
cost = portfolio_cost('Data/portfolio.csv')

# this will get caught by the outer try/except - OSError
# cost = portfolio_cost('Data/portfoliooooooo.csv')

# this will get caught by the inner try/except - ValueError
# cost = portfolio_cost('Data/missing.csv')

print(f'Total cost: ${cost}')
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

def read_prices(filename):
    '''
    arguments
        filename: path to the CSV file to read for processing total cost
    return values
        prices: a list of tuples, built using the data from your CSV file
    '''
    # always set counters, or other variables, first!
    prices = {}
    
    try:
        file = open(filename, 'r')
        rows = csv.reader(file)
        
        # prices.csv does not have a header...

        for row in rows:
            if len(row) == 2: # to account for that last 'blank' line
                prices[row[0]] = float(row[1])

        file.close()
    except OSError:
        print(f'Error opening file: {filename}')

    # send the return value last!
    return prices

def make_report(portfolio, prices):
    # portfolio is a list [] of dictionaries {}
    # prices is a dictionary {}

    report = []

    # print header information
    # report.append('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
    # report.append('{:>10s} {:>10s} {:>10s} {:>10s}'.format('----------', '----------', '----------', '----------'))

    for stock in portfolio:
        symbol = stock['name']
        # if prices has the price of the stock I'm looking at
        if prices.get(symbol):
            # then calculate current value of my investment (prices[symbol] * stock['shares'])
            shares_purchased = int(stock['shares'])
            initial_price = float(stock['price'])
            current_price = float(prices.get(symbol))

            change = current_price - initial_price
            temp = (
                symbol,
                shares_purchased,
                current_price,
                change
            )
            report.append(temp)

    return report

portfolio_file = 'Data/portfolio.csv'
prices_file = 'Data/prices.csv'

portfolio = read_portfolio(portfolio_file)
prices = read_prices(prices_file)
# make_report uses the objects, not the files!
report = make_report(portfolio, prices)

# print the report

print("Using c-style formatting...")
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('----------', '----------', '----------', '----------'))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)

print("")
print("Using tuple expansion with f-strings...")
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('----------', '----------', '----------', '----------'))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
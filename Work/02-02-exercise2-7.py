# report.py
#
# Exercise 2.7
# Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. 
# These statements should take the list of stocks in Exercise 2.5 (Data/portfolio.csv)
# and the dictionary of prices in Exercise 2.6 (Data/prices.csv)
# and compute the current value of the portfolio along with the gain/loss.
import csv, sys
from pprint import pprint

def build_investment_report(portfolio, prices):
    '''
    arguments
        portfolio: path to the portfolio file
        prices: path to the prices file
    return values
        report: data structure reporting total gain/loss data of your investments
    '''
    # always set counters, or other variables, first!
    report = {}
    
    '''
    {
        'IBM': { shares: '1', purchase_price: '100.0', intial_cost: '100.0', current_price: '300.0', net_gain: '200.0' }
    }

    Computing gain/loss
    - initial_cost   =  purchase_price  * shares
    - actual_gain =     current_price   * shares
    - net_gain =        actual_gain     - initial_cost        
    '''

    # Phase 1: Load investment data into the report object
    try:
        file = open(portfolio, 'r')
        rows = csv.reader(file)
        
        next(rows) # pass the header

        for row in rows:
            # Load relevant data into your report
            report[row[0]] = {
                'shares': int(row[1]),
                'purchase_price': float(row[2]),
                'initial_cost': int(row[1]) * float(row[2])
            }

        file.close()
    except OSError:
        print(f'Error opening file: {portfolio}')

    # Phase 2: Load prices file, and begin computing the remaining data (current_price, net_gain)
    try:
        file = open(prices, 'r')
        rows = csv.reader(file)

        # no header to pass

        for row in rows:
            if len(row) == 2:                       # bypass blank line at the end...
                if report.get(row[0]):              # If row[0] is present in report
                    symbol = str(row[0])            # calculate the remaining data
                    report[symbol]['current_price'] = float(row[1])
                    report[symbol]['actual_gain'] = report[symbol]['current_price'] * report[symbol]['shares']
                    report[symbol]['net_gain'] = report[symbol]['actual_gain'] - report[symbol]['initial_cost']

        file.close()
    except OSError:
        print(f'Error opening file: {prices}')

    # send the return value last!
    return report

# modify this version so it also reads arguments from the command line...
report = build_investment_report('Data/portfolio.csv','Data/prices.csv')
pprint(report) # 'pretty print', requires import of pprint module


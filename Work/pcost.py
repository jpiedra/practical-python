# pcost.py
#
# Exercise 1.27

import csv
file = open('Data\portfolio.csv')
rows = csv.reader(file)

# skip the headers
headers = next(rows)

# total cost to purchase all shares
total_cost = 0
product = 0

for row in rows:
    ''' OLD CODE, FOR REFERENCE ONLY
    current_row = line.split(',')
    product = int(current_row[1]) * float(current_row[2])
    total_cost += product
    '''
    product = int(row[1]) * float(row[2])
    total_cost += product

print(f'Total cost: ${total_cost}')
file.close()
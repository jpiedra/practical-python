# Using enumerate(), print a warning with the line number every time a row with missing data is found in 'Data/missing.csv'
# Modify pcost.py to do this...
#
# pcost.py
#
# Exercise 2.15

import csv
file = open(r'Data\missing.csv')
rows = csv.reader(file)

# skip the headers
headers = next(rows)

# total cost to purchase all shares
total_cost = 0
product = 0

for line, row in enumerate(rows):
    try:
        product = int(row[1]) * float(row[2])
        total_cost += product
    except:
        print(f"Row {line}: Couldn't convert: {row}")

print(f'Total cost: ${total_cost}')
file.close()
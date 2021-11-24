# Using zip() function
# - Using zip() to create a list using just one row
import csv

file = open(r'Data\portfolio.csv')
rows = csv.reader(file)
headers = next(rows)

print(headers)

row = next(rows)
zipped_row = list(zip(headers, row))
zipped_row  # a list, with tuples, where in each tuple, the header is paired to its corresponding value!

file.close()

# - Using zip(), with iteration, to create a list of dictionaries
file = open(r'Data\portfolio.csv')
rows = csv.reader(file)
headers = next(rows)

print(headers)

data = []

for row in rows:
    temp = dict(zip(headers,row))
    data.append(temp)

data    
# a list of dictionaries
# in each dictionary, thanks to zip()
# - the header is stilled paired with its corresponding value
# - IN THIS CASE, that's done through the key/value of each dictionary
# - the KEYS came from the 'header' sequence, the VALUE from each 'row'

h = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s}'
for i, d in enumerate(data):
    if i == 0:
        print(h)
    print('{name:>10s} {shares:>10s} {price:>10s}'.format_map(d))

file.close()

# Notice how zip() paired the column headers with the column values
# We've used list() and dict() to cast the result of zip() into the respective objects.
# Normally, zip() creates an iterator that must be consumed through a for-loop.
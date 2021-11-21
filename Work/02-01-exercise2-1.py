'''
    recall that we learned how to use the csv module
    to efficiently load and use data from a .csv file:

import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)

# pop the headers off
headers = next(rows)
print(headers)

# then iterate through each remaining row
for row in rows:
    print(row)

f.close()

    though reading a file is easy, we may want to do more with the data.
    yet, a 'raw row' of data is not as easy to work with:
    
...
cost = row[1] * row[2]
TypeError: can't multiply sequence by non-int of type 'str'
...

    typically, you'll want to interpret the raw data somehow, and turn
    it into a kind of object so you can work with it later...

'''

# exercise 1: create a tuple that represents the current row,
# but with the numeric columns converted to proper numbers

import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)

# pop the headers off
headers = next(rows)
print(headers)

# then iterate through each remaining row
for row in rows:
    # this works in a loop because, while tuple CONTENTS are immutable, you can always replace a tuple with a new one:
    t = (row[0], int(row[1]), float(row[2]))
    cost = t[1] * t[2]
    print(f'Total cost of {t[1]} share(s) of {t[0]} stock at ${t[2]} per share = ${cost:.2f}')

f.close()

# exrecise 2: do the same thing, but now use a dictionary
f = open('Data/portfolio.csv')
rows = csv.reader(f)

# pop the headers off
headers = next(rows)
print(headers)

# create a dictionary object 
# it will get loaded/used properly during the loop below
s = {
    'name': None,
    'shares': None,
    'price': None
}

# then iterate through each remaining row
for row in rows:
    s['name'] = row[0]
    s['shares'] = int(row[1])
    s['price'] = float(row[2])
    # this works because dictionaries ARE mutable
    s['cost'] = "{0:.2f}".format(s['shares'] * s['price'])
    # using a trick from our notes...
    print("#########################")
    for k in s:
        print(f"{k}: {s[k]}")
    # print(f"Total cost of {s['shares']} share(s) of {s['name']} stock at ${s['price']} per share = ${s['cost']}")

f.close()

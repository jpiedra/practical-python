'''
programs often have to work with many objects:
- portfolio of stocks
- table of stock prices

...there are three main choices to use for objects in python:
- lists: ordered data
- dictionaries: unordered data (data referenced via 'keys' within the dictionary object)
- sets: unordered collection of unique items

'''

# Lists as a container
# - Use a list when the order of the data matters. 
# - Remember that lists can hold any kind of object, such as a list of tuples:
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]

portfolio[0]
portfolio[2]

# List construction
# - You can initialize an empty list and append to it later, when required

records = []
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
records.append(('CAT', 150, 83.44))

# An example that builds a list by reading records from a file

records = []
with open('Data/portfolio.csv', 'rt') as f:
    next(f) # skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))

# Dictionaries as containers
# - Dictionaries are useful if you want fast, random lookups (by key name). For example, a dictionary of stock prices
prices = {
    'GOOG': 513.25,
    'CAT': 87.22,
    'IBM': 93.37,
    'MSFT': 44.12
}

prices['GOOG']
prices['IBM']

# Dict construction 
# - Since dicts are mutable simply defining the key/value works fine
prices = {}
prices['GOOG'] = 513.25

# Example populating from a file

prices = {}
with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.replace('\n','').replace('"','').split(',') 
        if len(row) == 2:
            prices[row[0]] = float(row[1])

prices

# to perform dictionary lookups, test the existence of a key
def findStockPrice(symbol, prices): # wrap the logic in a function
    if symbol in prices:            # the actual lookup...
        print(prices[symbol])
    else:
        print(f'Could not find {symbol}')

findStockPrice('GOOG', prices)
findStockPrice('IBM', prices)

# you can look up a value that MIGHT not exist, and provide a default value in case it doesn't...
prices.get('IBM', 0.0)
prices.get('SCOX', 0.0)

# Composite Keys
# - Almost any type of value can be used as a dictionary key in Python.
# - A dictionary key must be of a type that is immutable. For example, tuples:
holidays = {
    (1, 1) : 'New Years',
    (3, 14): 'Pi day',
    (9, 13): "Programmer's day",
} # this is why strings work as keys, remember from earlier chapters that strings are immutable...

# then to access:
holidays[3, 14]
# NEITHER A LIST, SET, NOR ANOTHER DICTIONARY can be used as a dictionary key, because lists and dictionares are MUTABLE.

# Sets
# - Sets are collections of unordered, unique items.
tech_stocks = { 'IBM', 'AAPL', 'MSFT' }
# alternative syntax
tech_stocks = set(
    ['IBM', 'AAPL', 'MSFT']
)

# Sets are useful for membership tests:
'IBM' in tech_stocks # True
'FB' in tech_stocks  # False

# Sets are also useful for duplicate elimination
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
unique_names = set(names)
# unique_names = set(['IBM', 'AAPL', 'GOOG', 'YHOO'])

# additional set operations:
unique_names.add('CAT')
unique_names.remove('YHOO')

s1 = { 'a', 'b', 'c' }
s2 = { 'c', 'd' }
s1 | s2 # Set union: all the elements from both sets
s1 & s2 # Set intersection: only the elements that both sets HAVE IN COMMON
s1 - s2 # Set difference: yields the elements from s1, after the elements from s2 are REMOVED from s1 = {'a', 'b'}
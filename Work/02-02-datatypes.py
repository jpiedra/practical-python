# recall we were introduced to several types already: integers, strings, floats, booleans

# the none type, evaluates to False
email_address = None

# real programs have more complex data
# For example information about a stock holding:
# 100 shares of GOOG at $490.10

# we can represent this in python as a Tuple:
# tuple = collection of values grouped together
stock1 = ('GOOG', 100, 490.1)

# sometimes the parens can be omitted in syntax
stock2 = 'GOOG', 100, 490.1

# special cases, a tuple can be empty, or contain exactly one type of value
t_empty = ()
t_one = ('GOOG', )

# tuples are often used to represent SIMPLE records or structures.
# A good analogy = a tuple is like a single row in a database table

# the contents of a tuple are ordered, like an array
name = stock1[0]
shares = stock1[1]
price = stock1[2]

# note that you cannot change the contents of a tuple once it's been defined
stock1[1] = 200
# TypeError: 'tuple' object does not support item assignment

# you can, however, make a new tuple based on a current tuple
# this is done by referencing the values of the original tuple you wish to preserve
stock3 = (stock1[0], 75, stock1[2])

# tuples are more about 'packing' related items together into a single entity
# a tuple is easier to pass around to other parts of a program as a single object

# tuple unpacking:
# to use the tuple elsewhere, you can unpack its parts into variables
name, shares, price = stock1
print(f'Total Cost: ${shares*price:0.2f}')

# the number of variables on the LEFT, must match the tuple structure
stock1 = ('GOOG', 100, 490.1)
name, shares = stock1
# ValueError: too many values to unpack (expected 2)

# TUPLES VS LISTS
# tuples look like read-only lists. however, tuples are most often used for a SINGLE ITEM consisting of multiple parts (each of which MAY BE DIFFERENT TYPES)
# lists, in contrast, are usually a COLLECTION OF DISTINT ITEMS, usually all of the SAME TYPE
record = ('GOOG', 100, 490.1) # A tuple representing a record in a portfolio
symbols = [ 'GOOG', 'AAPL', 'IBM' ] # A list representing several stock symbols

# DICTIONARIES
# a dictionary is mapping of keys to values. it's also sometimes called a Hash Table or associative array.
# the keys serve as indices for accessing values.
stock1 = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}

# common operations:
# to get values from a dictionary, use the key names
print(stock1['name'], stock1['shares'])
stock1['price']

# dictionary objects also expose a variety of methods (can be found using the help() method!)
help(stock1)

stock1.keys() # prints all the keys of an object
stock1.values() # prints all the values of an object
stock1.get('name') # equivalent to running stock1['name']

# example = using the keys() method to iterate through every key/value in a dictionary object!
print('stock1 keys/values')
for k in stock1.keys():
    print(f'{k}: {stock1[k]}')

# in contrast to tuples, dictionaries ARE mutable (can be changed):
# to add or modify values, assign using the key names
stock1['shares'] = 75
stock1['date'] = '6/6/2007'

for k in stock1.keys():
    print(f'{k}: {stock1[k]}')

# to delete values, use del
del stock1['date']
for k in stock1.keys():
    print(f'{k}: {stock1[k]}')

# WHY DICTIONARIES?
# dictionaries are useful when there are MANY different values, and those vlaues might be modified or manipulated.
# dictionaries make your code more READABLE as well, given that elements are reference by keys, rather than indices:
stock2[2]
# VS
stock1['price']

# [SEE 02-01-exercise2-1.py]

# DICTIONARY OPERATIONS
# if you turn a dictionary into a list, you'll get all of its keys:
list(stock1)

# similarly, if you use the 'for' statement to iterate on a dictionary, you'll get the keys:
for k in stock1:
    print(f'k = {k}')

# try this variant that performs a lookup at the same time
# (this means that using dict.keys() is not strictly needed to perform iterative dictionary lookups...)
for k in stock1:
    print(f'{k} = {stock1[k]}')

# the keys() method, already mentioned above, is unusual in that it returns a special dict_keys object
keys = stock1.keys()
keys

# the dict_keys object is an overlay on the original dictionary
# it ALWAYS GIVES YOU THE CURRENT KEYS of the dictionary = even if the dictionary changes!
# (note that the 'name' disappeared from keys, even though we did NOT call stock1.keys() again...)
del stock1['name']
keys

# a more elegant way to work with keys/values together is to use the items() method
# this method will give you (key, value) tuples:

stock1 = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}

items = stock1.items()
items

for k, v in stock1.items():
    print(f'{k} = {v}')

# if you have tuples, such as with 'items', you can create a dictionary using the dict() function...
stock7 = dict(items)
stock7
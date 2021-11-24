'''
SEQUENCES
Python has three sequence datatypes:
- String: 'hello'. A string is a sequence of characters
- List: [1, 4, 5]
- Tuple: ('GOOG', 100, 490.1)
'''

# All sequences are
# - Ordered
# - Indexed by integers
# - Have a length - len(seq)

a = 'Hello'
b = [1, 4, 5]
c = ('GOOG', 100, 490.1)

# Indexed order
a[0]    # 'H'
b[-1]   # 5
c[1]    # 100

# Length of sequence
len(a)
len(b)
len(c)

# Sequences can be replicated: s * n
a = 'Hello'
a * 3

b = [1, 2, 3]
b * 2

# Sequences (of the same type) can be concatenated: s + t
a = (1, 2, 3)
b = (4, 5)
a + b

c = [1, 5]
a + c       # throws error, cannot concatenate a list to a tuple

# Slicing
# - Slicing means to take a subsequence, from a sequence. The syntax is: s[start:end]
# - 'start' and 'end' are the indexes of the subsequence you want, and must be integers
# - Slices DO NOT INCLUDE THE END VALUE. 
# - If indices are omitted, they default to the beginning or the end of the list being sliced
a = [0,1,2,3,4,5,6,7,8]
a[2:5]  # [2,3,4]
a[-5:]  # [4,5,6,7,8]
a[:3]   # [0,1,2]

# Slice re-assignment
# - On lists, slices can be reassigned and deleted
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12] # Note - The reassigned sliced slice doesn't need to be the same length
a

a = [0,1,2,3,4,5,6,7,8]
del a[2:4]
a

# Sequence Reductions
# - There are some common functions to recuce a sequence to a single value
s = [1,2,3,4]
sum(s)  # returns a single value representing the sum of the list's elements 
min(s)  # returns a single value representing the smallest element in the list
max(s)  # returns a single value representing the largest element in the list

t = ['Hello', 'World']
max(t)  # even works when the list contains strings

# Iteration over a Sequence
# - The for-loop iterates over the elements in a sequence
# - On each iteration of the loop, you get a new item to work with. The new value is placed into the iteration variable
# - In the example below, 'i' is the iteration variable
s = [1,4,9,16]
for i in s:
    print(i) # On each iteration, the previous value of the iteration variable is overwritten (if any).

# After the loop finishes, the variable retains the last value
# The iteration variable is still available and can be used, for this reason
print(i)

# Break Statement
# - You can use the break statement to break out of a loop early
namelist = ['Robert', 'Mary', 'Jake', 'Paul']
for name in namelist:
    if name == 'Jake':  # every name up to, and NOT including 'Jake' gets printed
        break           # because when 'Jake' gets matched in 'name', the loop breaks!
    print(name)

# when the 'break' statement executes, it exits the loop, and moves on to the next statements in code
# The 'break' statement only applies to the inner-most loop.
# If this loop is within another loop, it will not break the outer loop
# (Meaning, if using nested loops, 'breaks' only occur in the loop within which they reside - Outer loops proceed on their own)

# Continue Statement
# - To skip one element and move to the next one, use the continue statement
for name in namelist:
    if name == 'Mary':  # in this example, every name EXCEPT 'Mary' gets printed
        continue        # because, when 'Mary' gets matched in 'name' variable, 'continue' statement forces
    print(name)         # the loop to start the next iteration, looking at the next element!
                        # effectively, the code that would have run gets skipped based on the conditional having evaluated 'True'

# 'continue' is useful when the current item is not of interest, or needs to be ignored in the processing

# Looping over Integers
# - If you need to count, use (range)
# - The syntax is range([start,] end[,step])
# - Calling range() returns a range object, which exposes various methods and members
# -- range.start(), range.stop(), range.step
# - Range `computes values as needed,` it does NOT store a large range of numbers
# - Much like with list slicing, ranges do NOT include the end value!

a = []
for i in range(0,8):    # example: intializing an array using range - supplying two arguments to range() sets the start and end of the range
    a.append(i)         # and a for loop, which iterates through the range() members and appends each to the list

a # [0,1,2,3,4,5,6,7]
                    
for i in range(100):    # supplying only one argument to range() defines the end of the range (default for start = 0, default for step = 1)
    print(i)            # 0, 1, 2... 97, 98, 99

for i in range(10, 50, 2):  # supplying the start, end, and step arguments to range() would result in the following sequence:
    print(i)                # 10, 12, 14... 46, 48    

# The enumerate() function
# - This function adds an extra counter value to iteration
names = ['Elwood', 'Jake', 'Curtis']
headers = ('Element', 'Value')
lines = ('----------', '----------')
print('%10s %10s' % headers)
print('%10s %10s' % lines)
for i, name in enumerate(names):
    # loops with: i = 0, name = 'Elwood' / i = 1, name = 'Jake' / i = 2, name = 'Curtis'
    print(f'{i:>10d} {name:>10s}')

# - The general form is `enumerate(sequence [, start = 0])`
# - `start` is optional, defaults to 0 if ommitted
# - A good example of using enumerate() is tracking line numbers while reading a file
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        ...

# - In the end, enumerate() is just a nice shortcut for this:
i = 0
for x in s:
    # statements...
    i += 1
# - Using enumerate() is less typing and runs slightly faster

# For and Tuples
# - You can iterate with multiple iteration variations...
points = [
    (1,4), (10,40), (23,14), (5,6), (7,8)
]
for x, y in points:     # when using multiple variables, each tuple is UNPACKED into a set of iteration variables
    print(x, y)         # the number of iteration variables, MUST match the number of items in each tuple

# zip() Function
# - The zip() function takes multiple sequences, and makes an iterator that combines them
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1]
pairs = zip(columns, values)

for column, value in pairs:         # to get the result, you must iterate.
    print(f'{column}: {value}')     # you can use multiple iterator variables to unpack each tuple, as shown previously

# A common use to `zip` is to create key/value pairs for constructing dictionaries
d = dict(zip(columns, values))
d # {'name': 'GOOG', 'shares': 100, 'price': 490.1}


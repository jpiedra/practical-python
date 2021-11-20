# three ways to define a string variable
a = 'yeah but no but yeah but no but...'
b = "Computer says so."
c = '''
this is a
multiline
string!
'''

# string escape codes
'''
'\n'      Line feed
'\r'      Carriage return
'\t'      Tab

'\''      Literal single quote
'\"'      Literal double quote
'\\'      Literal backslash
'''

# each character in a string is stored internally as a so-called unicode 'code-point' which is an integer.

# reference for all available character codes:
# https://unicode.org/charts
a = '\xf1'
b = '\u2200'
c = '\U0001D122'
d = '\N{FOR ALL}'

print(a, b, c, d)

# string indexing:
# strings work like arrays for accessing individual characters. you use an integer index, starting at 0.
# negative indices specify a position relative to the end of the string.
a = 'Hello world'
b = a[0] # H
c = a[4] # o
d = a[-1] # d, the end of the string!
print(a, b, c, d)

# you can also slice or select substrings specifying a range of indices with :
# missing indices assume the beginning or ending of the string
d = a[:5] # all characters from a[0] up to, but not including a[5] = 'Hello'
e = a[6:] # all characters from a[6] to the end of the string = 'world'
f = a[3:8] # all characters from a[3] up to, but not including a[8] = 'lo wo'
g = a[-5:] # 'world', negative indices indicate to start from the end of the string a
print(d, e, f, g)

# concatenation (+)
a = 'Hello' + 'World' # 'HelloWorld'
b = 'Say ' + a
print(a, b)

# length (len)
s = 'Hello'
print( len(s) ) # 5

# Membership test (`in`, `not in`)
t = 'e' in s # True
f = 'x' in s # False
g = 'hi' not in s # True
print(s, t, f, g)

# replication (s * n)
rep = s * 5
print(rep)

# string operations
# strings have methods that perform various operations with the string data
# remember, you can run help(str) in REPL to get complete list of available string class methods
s = ' Hello '
t = s.strip() # 'Hello'
print(s)
print(t)

# case conversion
s = 'Hello'
l = s.lower() # 'hello'
u = s.upper() # 'HELLO'
print(l, u)

# replacing text
s = 'Hello world'
t = s.replace('Hello', 'Hallo') # 'Hallo world'
print(s, t)

# string mutability
# strings are "immutable" or read-only. once created, the value cannot be changed
s = 'Hello World'
# this would produce an error: 'str' object does not support item assignment
# s[1] = 'a'
# THUS, ALL OPERATIONS AND METHODS THAT MANIPULATE STRING DATA, ALWAYS CREATE NEW STRINGS

# string conversions
# use str() to convert any value to a string.
# the result is a string holding the same text that would have been produced by the print() statement
x = 42
str(x)
print(x) # '42'

# byte strings
# A string of 8-bit bytes, commonly encountered with low-level I/O, is written as follows.
# by putting the b before the first quotation, you specify that it is a byte string as opposed to a text string
data = b'Hello World\r\n'

# most of the usual string operations work...
len(data) # 13
data[0:5] # 'Hello'
rep = data.replace(b'Hello', b'Cruel')
print(data, rep)

# indexing is a little different because it returns byte values as integers
print(data[0]) # will NOT return 'H', but 72 which is ASCII for 'H'

# conversion to/from text strings:
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
# the 'utf-8' argument specifies a character encoding. Other common values include 'ascii' and 'latin1'

# raw strings
# these are string literals with an uninterpreted backslash. 
# specified by prefixing the initial quote with a lowercase "r"
s = 'c:\newdata\test' # string (WILL interpret the backslashes)
rs = r'c:\newdata\test' # raw string (uninterpreted backslashes)
print(s)
print(rs)
# ideal use cases for raw strings are: filename, regular expressions, etc.

# f-strings
# A string with formatted expression substitution
name = 'IBM'
shares = 100
price = 91.1
a = f'{name:>10s} {shares:10d} {price:10.2f}'
print(a)

b = f'Cost = ${shares*price:0.2f}'
print(b)

# extra: how to get methods that an object exposes:
s = 'hello world'
print( dir(s) )









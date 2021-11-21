'''
Formatting
- When working with data, you often want to produce structured output (tables, etc.). For example:
      Name      Shares        Price
----------  ----------  -----------
        AA         100        32.20
       IBM          50        91.10
       CAT         150        83.44
      MSFT         200        51.23
        GE          95        40.37
      MSFT          50        65.10
       IBM         100        70.44

'''

# String Formatting
# - One way to format string in Python 3.6+ is with f-strings
name = 'IBM'
shares = 100
price = 91.1
formatted_string = f'{name:>10s} {shares:>10d} {price:>10.2f}' # The part {expression:format} is replaced.
print(formatted_string)
# f-strings are commonly used with the 'print' function
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')

# Format Codes
# - The format codes (after the : inside the {} braces) are similar to C printf() and common codes include:
'''
d   decimal integer
b   binary integer
x   hexadecimal integer
f   Float as [-]m.dddddd
e   Float as [-]m.dddddde+-xx
g   Float, but selective use of E notation
s   String
c   Character (from integer)
'''

# - Common modifiers adjust the field width and decimal precision. This is a partial list:
'''
:>10d   Integer, right aligned in 10-character field
:<10d   Integer, left aligned in 10-character field
:^10d   Integer, centered in 10-character field
:0.2f   Float, with 2 digit precision
'''

# Dictionary Formatting
# - You can use the format_map() method to apply string formatting to a dictionary of values:
s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}

'{name:>10s} {shares:>10d} {price:>10.2f}'.format_map(s) # It uses the same code as f-strings, but takes the values from the supplied dictionary

# format() method
# - There is a method format() that can apply formatting to arguments or keyword arguments
'{name:>10s} {shares:>10d} {price:>10.2f}'.format(name='IBM', shares=100, price=91.1) # named parameters
'{:>10s} {:>10d} {:>10.2f}'.format('IBM', 100, 91.1) # positional parameters, identifiers are absent in f-string AND params...

# C-Style formatting
# - You can also use the formatting operator %
# - This requires a single item or a tuple on the right. 
# - Format codes are modeled after the C printf() as well
"The value is $d" % 3
'%5d %-5d %10d' % (3, 4, 5)
'%0.2f' % (3.1415926,)

# Note: This is the only formatting available on byte strings.
b'%s has %d messages' % (b'Dave', 37)


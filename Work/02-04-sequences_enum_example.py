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

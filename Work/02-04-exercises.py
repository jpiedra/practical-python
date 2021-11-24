# Some basic counting examples
for n in range(10):
    print(n, end=' ')

for n in range(10, 0, -1):
    print(n, end=' ')

for n in range(0, 10, 2):
    print(n, end=' ')

# More sequence operations
data = [4,9,1,25,16,100,49]
min(data)
max(data)
sum(data)

# Looping over the data
for x in data:
    print(x)

for n, x in enumerate(data):
    print(f'{n:>3d}: {x:>3d}')

# Sometimes, the `for` statement, len() and range() get used by novices in some kind of horrible
# code fragment that looks like it emerged from the depths of a rusty C program...
for n in range(len(data)):
    print(data[n])

# You absolutely do NOT do this in Python! You don't need to do this!
# - If you want to access each element in the list, a simple for loop will work:
for n in data:
    print(n)

# - And, if you DO need to the element's index, we already know - enumerate() gets the job done
for n, x in enumerate(data):
    print(f'{n:>3d}: {x:>3d}')
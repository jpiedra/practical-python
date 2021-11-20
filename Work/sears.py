# sears.py
bill_height = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height in Meters, consistent unit of measurement...

# counters
num_bills = 1
day = 1

while num_bills * bill_height < sears_height:
    print(day, num_bills, num_bills * bill_height)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_height)
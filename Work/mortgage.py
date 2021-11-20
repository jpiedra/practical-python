# mortgage.py
#
# Exercise 1.7

# consts
principal =     5e5 # faster way to write 500,000 (5 zeroes)...
rate =          0.05 # interest rate
payment =       2684.11 # monthly payment

# counters
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print( 'Total paid', round(total_paid, 2) )
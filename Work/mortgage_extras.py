# mortgage.py
#
# Exercise 1.7

# consts
principal =           5e5 # faster way to write 500,000 (5 zeroes)...
rate =                0.05 # interest rate
payment =             2684.11 # monthly payment
extra_payment =       1000.00 # additional amount towards each payment, only during the first twelve months

# counters
total_paid = 0.0
num_months = 0

while principal > 0:
    # use the appropriate installment based on number of months passed
    if (num_months < 12):
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    
    # increment number of months elapsed
    num_months += 1

print( 'Total months passed', num_months )
print( 'Total paid', round(total_paid, 2) )
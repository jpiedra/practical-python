# mortgage.py
#
# Exercise 1.7

# consts
principal =           5e5 # faster way to write 500,000 (5 zeroes)...
rate =                0.05 # interest rate
payment =             2684.11 # monthly payment

# counters
total_paid = 0.0

# user specified variables
extra_payment =              input("Enter extra payment applied per year:") or 0 # quick failsafe for no user input...
extra_payment_start_month =  input("Enter the starting month to use for calculations:") or 0 
extra_payment_end_month =    input("Enter the end month to use for calculations:") or 0 

# explicit casting...
extra_payment = int(extra_payment)
extra_payment_start_month = int(extra_payment_start_month)
extra_payment_end_month = int(extra_payment_end_month)

num_months = extra_payment_start_month

while principal > 0:
    # use the appropriate installment based on number of months passed
    if (extra_payment_start_month <= num_months and extra_payment_end_month >= num_months):
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    
    # increment number of months elapsed
    num_months += 1

print( 'Total months passed', num_months )
print( 'Total paid', round(total_paid, 2) )
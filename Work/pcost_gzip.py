# pcost.py
#
# Exercise 1.27

import gzip
with gzip.open('Data/portfolio.csv.gz','rt') as f:
    for line in f:
        print(line,end='')

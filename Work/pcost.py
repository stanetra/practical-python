# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    cost = 0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    header = next(rows)
    cost = 0
    for row in rows:
        try:
            cost += float(row[1])*float(row[2])
        except (ValueError, IndexError):
            print(f"Error parsing line: '{row[1]}', '{row[2]}'")   
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
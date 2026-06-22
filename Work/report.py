# report.py
#
# Exercise 2.4
import sys
import csv
## List of tuples
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                holding = (name,shares,price)
                portfolio.append(holding)
            except (ValueError, IndexError):
                print(f"Error parsing line: '{row[1]}', '{row[2]}'")   
    return portfolio

# List of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            try:
                name = record['name']
                shares = int(record['shares'])
                price = float(record['price'])
                holding = {'name': name,'shares': shares,'price':price}
                portfolio.append(holding)
            except (ValueError, IndexError):
                print(f"Error parsing line: '{row[1]}', '{row[2]}'")   
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)



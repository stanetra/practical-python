import csv
import sys

# Exercise 2.4
import sys
import csv

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

def do_it(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Work/Data/portfolio.csv'
    portfolio = read_portfolio(filename)
    print(portfolio)

def test ():
    x = 10
    if (x == 10):
        x = 100
    print(x)

do_it(sys.argv)
test()


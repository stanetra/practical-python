# report.py
#
# Exercise 3.1
import sys
import file

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

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

def print_report(report):
    print(report)
    for r in report:
        name = r['name']
        shares = r['shares']
        price = r['price']
        print(f'Name: {name}, Shares: {shares}, Price: {price}')

prices = read_prices('Work/Data/prices.csv')
portfolio = read_portfolio('Work/Data/portfolio.csv')
print_report(portfolio)

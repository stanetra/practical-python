row = ['AA', '100', '32.20']

t = (row[0], int(row[1]), float(row[2]))
cost = t[1] * t[2]

d = {
        'name' : row[0],
        'shares' : int(row[1]),
        'price'  : float(row[2])
    }

d['date'] = (6, 11, 2007)
d['account'] = 12345

keys = d.keys()
items = d.items()

for k, v in items:
    print(k,'=',v)

prices = {} # Initial empty dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        try:
            row = line.split(',')
            prices[row[0]] = float(row[1])
        except (ValueError, IndexError):
            print(line)

# Exercise 2.6
# List of dicts
import csv
def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = row[0]
                price = float(row[1])
                prices[name] = price
            except (ValueError, IndexError):
                pass
    return prices

prices = read_prices('Data/prices.csv')
print(prices)

# Excercise 2.7
def read_portfolio_with_calcs(filename):
    portfolio = []
    prices = read_prices('Data/prices.csv')
    port_value = 0.0
    port_pnl = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                cost = shares * price
                value = shares * prices[name]
                holding = {'name': name,'shares': shares,'price':price, 'cost':cost, 'value':value}
                portfolio.append(holding)
                port_value += value
                port_pnl += value - cost
            except (ValueError, IndexError):
                pass   
    return portfolio, port_value, port_pnl

portfolio, port_value, port_pnl = read_portfolio_with_calcs('Data/portfolio.csv')
print(f"Portfolio Value: {port_value} Portfolio PnL: {port_pnl}")
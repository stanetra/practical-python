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
                holding = {'name': name,'shares': shares,'price':price}
                portfolio.append(holding)
            except (ValueError, IndexError):
                pass
    return portfolio

def make_report(portfolio, prices):
    report = []
    report.append(('Name', 'Shares', 'Price', 'Change'))
    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = holding['price']
        curr_price = prices[name]
        row = (name, shares, curr_price, curr_price - price)
        report.append(row)
    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

header = False
for name, shares, price, change in report:
    if header == False:
        print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
        header = True
    else:
        print(f'{name:>10s} {shares:>10d} {"$"+f"{price:.2f}":>10} {change:>10.2f}')



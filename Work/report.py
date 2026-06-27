#!/usr/bin/env python3
# report.py
#
# Exercise 3.12
import fileparse

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        prices = dict(fileparse.parse_csv(f, types=[str,float],has_headers=False))
    return prices

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        portfolio = fileparse.parse_csv(f, types=[str,int,float])
    return portfolio

def print_report(report):
    for r in report:
        name = r['name']
        shares = r['shares']
        price = r['price']
        print(f'Name: {name}, Shares: {shares}, Price: {price}')

def main(argv):
    if len(argv) >= 2:
        portfolio_filename = sys.argv[1]
    else:
        portfolio_filename = 'Data/portfolio.csv'

    if len(argv) >= 3:
        price_filename = sys.argv[2]
    else:
        price_filename = 'Data/prices.csv'

    prices = read_prices(price_filename)
    portfolio = read_portfolio(portfolio_filename)
    print_report(portfolio)

if __name__ == '__main__':
    import sys
    main(sys.argv)


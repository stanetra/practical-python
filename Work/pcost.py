#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import report

def portfolio_cost(filename):
    total_cost = 0
    portfolio = report.read_portfolio(filename)
    for r in portfolio:
        shares = r['shares']
        price = r['price']
        total_cost += shares * price
    return total_cost

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
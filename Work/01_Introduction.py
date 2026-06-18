# Exercise 1.26: File Preliminaries

with open('Data/portfolio.csv', 'rt') as f:
        data = f.read()

print(data)

Exercise 1.27: Reading a data file
cost = 0
with open('Data/portfolio.csv', 'rt') as f:
    skip = True
    for line in f:
        if skip:
            skip = False
            continue
        lline = line.split(',')
        cost += float(lline[1]) * float(lline[2])

print(f'Total cost: {cost}')

def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(sumcount(100))
# Exercise 1.29: Defining a function
def greeting(name):
     'Issues a greeting'
     print(f'Hello, {name}!')

#Exercise 1.30: Turning a script into a function
def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        skip = True
        for line in f:
            if skip:
                skip = False
                continue
            lline = line.split(',')
            cost += float(lline[1]) * float(lline[2])
    return cost

print(f'Cost: {portfolio_cost("Data/portfolio.csv")}')

# Exercise 1.31: Error handling 
def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        for line in f:
            try:
                lline = line.split(',')
                cost += float(lline[1]) * float(lline[2])
            except (ValueError, IndexError):
                print(f'Error parsing line: {line}')
    return cost

print(f'Cost: {portfolio_cost("Data/portfolio.csv")}')
print(f'Cost: {portfolio_cost("Data/missing.csv")}')

# Exercise 1.32: Using a library function
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

print(f'Cost: {portfolio_cost("Data/portfolio.csv")}')
print(f'Cost: {portfolio_cost("Data/missing.csv")}')


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

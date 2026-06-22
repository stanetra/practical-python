import csv
import sys
from datetime import datetime
import math

def read_date (value):
    # Need to check for date format
    date_value = datetime.strptime(value, "%Y-%m-%d").date()
    return date_value

def read_ccy (value):
    return float(value[1:])

def read_int (value):
    return int(value)

def read_stock_data(filename):
    stock_data = []
    headers = {}
    total_row_count = 0
    good_row_count = 0
    bad_row_count = 0
    bad_row_categories = {'bad_ccy': 0, 'bad_date': 0, 'bad_int': 0, 'missing_values':0 ,'extra_values': 0, 'empty_values': 0}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
      
        for row in rows:

            parsed_record = {}
            total_row_count += 1
            bad_row = False
            
            if len(headers) > len(row):
                bad_row_categories['missing_values'] += 1
                bad_row = True
            elif len(headers) < len(row):
                bad_row_categories['extra_values'] += 1
                bad_row = True
            
            record = zip(headers, row)
   
            for header, value in record:
                if value == '':
                    bad_row_categories['empty_values'] += 1
                    bad_row = True
                    continue
                
                if header in ['date']:  
                    try:
                        parsed_record[header] = read_date(value)
                    except:
                        bad_row_categories['bad_date'] += 1
                        bad_row = True
                elif header in ['open','high','low','close']:
                    try:
                        parsed_record[header] = read_ccy(value)
                    except:
                        bad_row_categories['bad_ccy'] += 1
                        bad_row = True
                elif header in ['volume']:
                    try:
                        parsed_record[header] = read_int(value)
                    except:
                        bad_row_categories['bad_int'] += 1
                        bad_row = True
                else:
                    parsed_record[header] = value
            if bad_row:
                bad_row_count += 1
            else:
                good_row_count += 1
            stock_data.append(parsed_record)
    print(f'Total row count {total_row_count}, Good row count {good_row_count}, Bad row count {bad_row_count}')
    print(f'Headers {headers}')
    print(bad_row_categories)
    return stock_data

def calc_stats(header, data):
    column = [row[header] for row in data if header in row]
    cmin = min(column)
    cmax = max(column)
    csum = sum(column)
    clen = len(column)

    mean = csum/clen
    sum_of_sqrs = 0
    for x in column:
        dev = (x - mean)
        sum_of_sqrs += dev * dev
    variance = sum_of_sqrs/(clen-1)
    std_dev = math.sqrt(variance)
    print(f'Attribute: {header}, Length: {clen}, Min: {cmin:.2f}, Max: {cmax:.2f}, Average: {mean:.2f}, Std Dev: {std_dev:.2f}')
    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Milestones/Milestone 1/stock_data.csv'

stock_data = read_stock_data(filename)
for header in ['open','high','low','close']:
    calc_stats(header, stock_data)



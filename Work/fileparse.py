# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file_iter, select: list = None, types: list = None, has_headers: bool =True, 
              delimiter: str = ',', silence_errors: bool = False) -> list:
    '''
    Parse a CSV file and return a list of records.

    Args:
        file_iter: Any iterable that returns a line of input for each iteration.
        select: List of column names to include. None means all columns.
        types: List of type conversion functions, one per column.
        has_headers: Whether the first row is a header row.
        delimiter: Field delimiter character.
        silence_errors: If True, suppress row parsing errors.

    Returns:
        List of records, each as a dict (with headers) or tuple (without).
    '''
    if ((select != None) and (has_headers == False)):
        raise RuntimeError("select argument requires column headers")
    if ((select != None) and (types != None)):
        if (len(select) != len(types)):
            raise RuntimeError("select and types have different lenghts")
    if (isinstance(file_iter, str)):
        raise RuntimeError("str not valid for file_iter")

    rows = csv.reader(file_iter, delimiter=delimiter)

    if has_headers:
        # Read the file headers
        headers = next(rows)

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if has_headers and (select != None):
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    rownum = 0
    for row in rows:
        rownum += 1
        if not row:    # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if indices:
            row = [ row[index] for index in indices ]
        try:
            if types:
                row = [type(val) for type,val in zip(types,row)]
        except ValueError as e:
            if not silence_errors:
                print(f'Row {rownum}: Couldn\'t convert ${row}')
                print(f'Row {rownum}: {e}')

        if has_headers:
            # make a dict
            record = dict(zip(headers, row))
        else:
            # make a typle
            record = tuple(row)

        records.append(record)

    return records



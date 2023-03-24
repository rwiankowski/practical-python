# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(file_contents: list, select: list = None, types: list = None, has_headers: bool = True, delimiter: str = ',', silence_errors: bool = False) -> list:

    if select and not has_headers:
        raise ValueError('The Select option requires headers in the csv file!')

    if type(file_contents) == str:
        raise ValueError('Incorrect File Contents input!')

    rows = file_contents

    if has_headers:
        headers = next(file_contents)
    if select:
        indices = [headers.index(column) for column in select]
        headers = select
        rows = [[row[index] for index in indices] for row in file_contents if row]

    if types:
        try:
            rows = [[func(val) for func, val in zip(types, row)] for row in rows if row]
        except ValueError as exception:
            if not silence_errors:
                print(f"Couldn't convert value: {exception}")

    if has_headers:
        parsed_rows = [dict(zip(headers, row)) for row in rows]
    else:
       parsed_rows = [tuple(row) for row in rows]

    return parsed_rows


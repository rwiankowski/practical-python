# report.py
#
# Exercise 2.4

import fileparse
import csv
import stock
import tableformat


def read_prices(filename: str) -> dict:

    with open(filename) as file:
        file_contents = csv.reader(file)
        return dict(fileparse.parse_csv(file_contents, types = [str, float], has_headers = False))


def read_portfolio(filename: str) -> list:

    with open(filename) as file:
        file_contents = csv.reader(file)
        rows = fileparse.parse_csv(file_contents, select = ['name', 'shares', 'price'], types = [str, int, float])

        return [stock.Stock(row['name'], row['shares'], row['price']) for row in rows]


def make_report(portfolio_list: list, prices_dict: dict) -> list:
    report = []

    for item in portfolio_list:
        new_price = prices_dict[item.name]
        holding = (item.name, item.shares, new_price, new_price - item.price)
        report.append(holding)

    return report


def print_report(report_list: list, formatter: tableformat.TableFormatter):

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in report_list:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_value(portfolio_list: list, prices_dict: dict) -> float:
    updated_portfolio_value = 0.0

    for item in portfolio_list:
        updated_portfolio_value += item['shares'] * prices_dict[item['name']]

    return updated_portfolio_value


def main(portfolio_filename: str, prices_filename: str, report_format: str = 'txt'):

    formatter = tableformat.create_formatter(report_format)

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report, formatter)


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2], sys.argv[3])
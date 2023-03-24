# pcost.py
#
# Exercise 1.27

import report

portfolio_filename = 'Data/portfoliodate.csv'


def portfolio_cost(filename: str) -> float:

    records = report.read_portfolio(filename)
    total_cost = sum([int(record.shares) * float(record.price) for record in records])
    return total_cost


def main(filename: str):
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost:0.2f}')


if __name__ == "__main__":
    import sys
    main(sys.argv[1])

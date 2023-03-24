class TableFormatter:
    def headings(self, headers: list):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError

    def row(self, rowdata: list):
        '''
        Emit a single row of data.
        '''
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def headings(self, headers: list):
        for heading in headers:
            print(f'{heading.title():>10s}', end=' ')

        print()
        print(('_' * 10 + ' ') * len(headers))

    def row(self, rowdata: list):
        for cell in rowdata:
            print(f'{cell:>10s}', end=' ')
        print()


class CsvTableFormatter(TableFormatter):
    def headings(self, headers: list):
        print(','.join(headers))

    def row(self, rowdata: list):
        print(','.join(rowdata))


class HtmlTableFormatter(TableFormatter):
    def headings(self, headers: list):
        print('<tr>', end='')
        for heading in headers:
            print(f'<th>{heading.title()}</th>', end='')
        print('</tr>')

    def row(self, rowdata: list):
        print('<tr>', end='')
        for cell in rowdata:
            print(f'<td>{cell}</td>', end='')
        print('</tr>')


class FormatError(Exception):
    pass


def create_formatter(fmt: str) -> TableFormatter:
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CsvTableFormatter()
    elif fmt == 'html':
        return HtmlTableFormatter()
    else:
        raise FormatError(f'Unknown format: {fmt}')


def print_table(table_data: list, table_columns: list, table_formatter: TableFormatter):

    table_formatter.headings(table_columns)

    for table_row in table_data:
        rowdata = [str(getattr(table_row, column)) for column in table_columns]
        table_formatter.row(rowdata)
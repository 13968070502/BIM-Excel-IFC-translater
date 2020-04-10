"""A file to import excel files."""
from openpyxl import load_workbook

from excel_utils import read_in_col, read_in_row


def import_from_excel(filename):
    """Read an excel file."""
    if not filename:
        filename = 'data/ExcelVorlage.xlsx'

    print(f'Import file from excel: {filename} ...')

    wb = load_workbook(filename)

    for ws in wb.worksheets:
        header_row = read_in_row((1, 1), ws)
        print(f'Read sheet {ws.title}:')
        print(f'header: {header_row}')


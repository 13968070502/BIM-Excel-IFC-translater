"""A file to import excel files."""
from openpyxl import load_workbook

from excel_utils import read_in_col, read_in_row


def print_sheet_info():
    """Print interesting details about a worksheet."""


def import_from_excel(filename):
    """Read an excel file."""
    if not filename:
        filename = 'data/ExcelVorlage.xlsx'

    print(f'Import file from excel: {filename} ...')

    wb = load_workbook(filename)

    data = []  # list of dictionaries to catch all data

    for ws in wb.worksheets:  # loop over worksheets
        header_row = read_in_row((1, 1), ws)
        print(f'Read sheet {ws.title}:')
        print(f'header: {header_row}')
        row_count = ws.max_row
        for row_idx in range(1, row_count):  # loop over rows
            cell_value = ws.cell(row=row_idx+1, column=1).value
            if not cell_value:
                continue  # skip if no data in first cell of row
            this_row_data = {}  # dictionary to catch single row content
            for col_idx, header in enumerate(header_row):  # loop over columns
                cell_value = ws.cell(row=row_idx+1, column=col_idx+1).value
                this_row_data[header] = cell_value
            print(this_row_data)
            data.append(this_row_data)

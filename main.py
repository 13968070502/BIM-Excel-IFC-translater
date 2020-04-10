"""The main file for the program."""
import import_from_excel
import write_to_ifc


def main():
    """Run the main functions."""
    data = import_from_excel.import_from_excel('data/ExcelVorlage.xlsx')
    write_to_ifc.write_to_ifc(data)


if __name__ == '__main__':
    main()
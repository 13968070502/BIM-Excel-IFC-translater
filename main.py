"""The main file for the program."""
import import_from_csv
import translate_to_ifc
import write_to_step


def main():
    """Run the main functions"""
    data = import_from_csv.import_from_csv('data\Input_Results_TGA_MA.csv')
    translate_to_ifc.translate_to_ifc(data)
    write_to_step.write_to_step(data)

#def main():
#    """Run the main functions."""
#    data = import_from_excel.import_from_excel('data/ExcelVorlage.xlsx')
#    write_to_ifc.write_to_ifc(data)

if __name__ == '__main__':
    main()
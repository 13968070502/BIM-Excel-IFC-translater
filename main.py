"""The main file for the program."""
from Import import import_from_excel


#def main():
#    """Run the main functions"""
#    data = import_from_csv.import_from_csv('data\Input_Results_TGA_MA.csv')
#    translate_to_ifc.translate_to_ifc(data)
#    write_to_step.write_to_step(data)

def main():
    """Run the main functions."""
    data = import_from_excel.import_from_excel('data/ExcelVorlage.xlsx')
 #   translate_to_ifc.translate_to_ifc(data)

if __name__ == '__main__':
    main()
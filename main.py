from os.path import exists
from CSV import creating
from filling_csv_file import write_csv


path = 'Phone_dictionary.csv'
valid = exists(path)
if not valid:
    creating()

write_csv()

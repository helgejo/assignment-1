__author__ = 'HELGJO'

import csv


#f = open("minisubCAT.csv", "rU")
#reader = csv.reader(f, dialect=csv.excel_tab)
#reader = csv.reader(f)
#for row in reader:
#    print(row)

with open('minisubCAT.csv', 'rU') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print your_list


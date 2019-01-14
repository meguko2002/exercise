import csv

example_file = open('fileEdit/101rawdata.csv')
example_reader = csv.reader(example_file)
for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))

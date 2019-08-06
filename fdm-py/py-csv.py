import csv

with open('peak.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count==0:
            print('Column names are ', row)
            line_count +=1
        else:
            print(row[0], row[1])
            line_count +=1
    print('Processed %d lines.'%line_count)

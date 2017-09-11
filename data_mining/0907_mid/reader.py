from csv import reader

with open('maryland_accident_dataset_by_report_no.csv') as f:
    spamreader = reader(f, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

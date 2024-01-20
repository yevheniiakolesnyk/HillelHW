import csv

with open('names.csv', 'r', encoding= 'utf-8') as file:
    csv_reader = csv.reader(file)
    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        for elements in csv_reader:
            csv_writer.writerow({elements[2]})

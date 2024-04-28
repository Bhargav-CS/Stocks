import csv

def remove_rows(csv_file, data, new_csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if data not in row]

    with open(new_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Example usage
csv_file = 'NSEI.csv'
data_to_remove = 'null'
new_csv_file = 'filtered_NSEI.csv'

remove_rows(csv_file, data_to_remove, new_csv_file)

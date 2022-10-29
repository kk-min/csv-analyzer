import csv
import seaborn as sb

def read_file(file):
    csv_data = csv.reader(file, delimiter=",")
    return csv_data

def get_columns(data):
    column_list = []
    for row in data:
        column_list.append(row)
        return column_list

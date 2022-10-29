import csv
import seaborn as sb

def read_file(file):
    csv_data = csv.reader(file, delimiter=",")
    return csv_data

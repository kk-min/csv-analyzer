import pandas as pd

def read_file(file):
    csv_data = pd.read_csv(file, delimiter=",")
    return csv_data

def get_column_list(data):
    return list(data.columns)

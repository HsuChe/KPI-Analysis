import os
import csv
from datetime import date

poll_csvpath = os.path.join("Resources","election_data.csv")
analysis_path = os.path.join("analysis",f"analysis_{date.today()}")

print(poll_csvpath, analysis_path,'hello world')

def parser():
    with open(poll_csvpath) as file:
        csvreader = csv.reader(file):
        csv_list = []
        for row in csvreader:
            csv_list.append(row)
    return csv_list


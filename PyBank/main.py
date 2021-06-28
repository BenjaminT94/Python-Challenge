import os
import csv
data = os.path.join('budget_data.csv')
# Using Exercise CSV Read, opening the source data file
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
# Skipping the first row as it's the row for column headers
    header = next(csvreader)
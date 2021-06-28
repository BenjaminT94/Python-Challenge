import os
import csv
data = os.path.join('budget_data.csv')
# Using Exercise CSV Read, opening the source data file
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
# Skipping the first row as it's the row for column headers
    header = next(csvreader)
# Creating lists to track values for the output
    months = []
    profit_loss = []
    profit_change = []
# Assigning a variable to calculate the average change of profit in the entire file
    average_change = sum(profit_change) / len(profit_change)
# Tracking the index of the change in profit each month plus 1
    increase = profit_change.index(max(profit_change)) + 1
    decrease = profit_change.index(min(profit_change)) + 1
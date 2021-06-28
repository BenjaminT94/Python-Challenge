import os
import csv
file = os.path.join("..", "Resources","budget_data.csv")
# Using Exercise CSV Read, opening the source data file
with open("budget_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
# Skipping the first row as it's the row for column headers
    header = next(csvreader)
# Creating lists to track values for the output
    months = []
    profit_loss = []
    profit_change = []
# Using a for loop to now append values to our list
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    for x in range(len(profit_loss)-1):
        profit_change.append(profit_change[x+1]-profit_change[x])
        # Assigning a variable to calculate the average change of profit in the entire file  
        average_change = sum(profit_change) / len(profit_change) 
        # Tracking the index of the change in profit each month plus 1 (House of Pie exercise)
        greatest_increase = profit_change.index(max(profit_change)) + 1
        greatest_decrease = profit_change.index(min(profit_change)) + 1

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {len(months)}")
print(f"Total: {sum(profit_loss)}")
print(f"Average Change: {int(average_change)}")
print(f"Greatest Increase: {months[greatest_increase]} {(str(max(profit_change)))}")
print(f"Greatest Decrease: {months[greatest_decrease]} {(str(min(profit_change)))}")



# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# As an example, your analysis should look similar to the one below:

#   Financial Analysis
#   --------------------------------------------------
#   Total Months: 86
#   Total: $38382578
#   Average Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   --------------------------------------------------


# Import the necessary modules
import os
import csv
import statistics


# Path to my csv file
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    header = next(csvreader)

# Create the lists to search through
    profit_list = []
    changes_list = []
    periods_list = []
    last_month = 0

    # for row in csvreader:
    for i, row in enumerate(csvreader):
        profit_list.append(int(row[1]))
        periods_list.append(row[0])
        if i == 0:
            changes_list.append(0)
        else:
            changes_list.append(int(row[1]) - last_month)
    last_month = int(row[1])
    total_profit = sum(profit_list)
    max_profit = max(profit_list)
    min_profit = min(profit_list)
    avg_change = statistics.mean(changes_list)
    total_months = len(periods_list)
    print()
    print(f"Financial Analysis")
    print(f"--------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(round(avg_change, 2))
    # print(f"Greatest Increase in Profits: {max_profit}")
    # print(f"Greatest Decrease in Profits: {min_profit}")
    # print(type(profit_list)

    for i, amount in enumerate(profit_list):
        if amount == max_profit:
            # print(profit_list[i], periods_list[i])
            total_profit_string = periods_list[i] + " " + str(profit_list[i])
            break
    print(f"Greatest Increase in Profits: {total_profit_string}")

    for i, amount in enumerate(profit_list):
        if amount == min_profit:
            # print(profit_list[i], periods_list[i])
            total_profit_string = periods_list[i] + " " + str(profit_list[i])
            break
    print(f"Greatest Decrease in Profits: {total_profit_string}")
    print(f"--------------------------------------------------")

# Define the function and have it accept the 'budget_data' as its sole parameter
#  def analysis(budget_data):
#      total_months = int(budget_data[1]))
#      total_profit = sum(int(budget_data[1]))
#      max_profit = max(float(budget_data[1]))
#      min_profit = min(float(budget_data[1]))

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


# Print analytical stats to the screen
# print(f"Total Months: {total_months}")
# print(f"Total: ${profit}")
# #print(f"Avg Change: {avg}")
# print(f"Greatest Profit Increase: {max_profit}")
# print(f"Greatest Profit Decrease: {min_profit}")


# Specify the file path to write to
# output_path = os.path.join("..", "python-challenge", "PyBank", "Analysis", "financial_analysis.csv")

# Write data to a .csv file
# with open(output_path, 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)

# To save specific data input as a row in the csv
    # writer.writerow(["row1", "row2"])


# Write the first row (column headers)
# csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

# Write the second row
# csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

# Write updated data to csv file
# csvpath = os.path.join("output", filename)
# with open(csvpath, "w") as csvfile:
#     fieldnames = ["last_name", "first_name", "ssn", "email"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(new_employee_data)
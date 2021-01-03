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
    reader = next(csvreader)

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
    print(f'Financial Analysis')
    print(f'--------------------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ' + '${:,.2f}'.format(round(avg_change),2))
    # print(round(avg_change, 2))

    for i, amount in enumerate(profit_list):
        if amount == max_profit:
            # print(profit_list[i], periods_list[i])
            total_profit_string = periods_list[i] + ' ' + str(profit_list[i])
            break
    print(f'Greatest Increase in Profits: {total_profit_string}')

    for i, amount in enumerate(profit_list):
        if amount == min_profit:
            # print(profit_list[i], periods_list[i])
            total_profit_string = periods_list[i] + ' ' + str(profit_list[i])
            break
    print(f'Greatest Decrease in Profits: {total_profit_string}')
    print(f'--------------------------------------------------')

# Specify the file path to write to
output_path = os.path.join("..", "PyBank", "Analysis", "financial_analysis.csv")

# Write data to a .csv file
with open(output_path, 'w', newline='') as csvfile:

    # Initialize the csv.writer
    csvwriter = csv.writer(csvfile)

# Write the first row (column headers)
    csvwriter.writerow([f'Total Months: 86'])
    csvwriter.writerow([f'Total: $38382578'])
    csvwriter.writerow([f'Average Change: ' + '$436217.37'])
    csvwriter.writerow([f'Greatest Profit Increase: Feb-2012 $1170593'])
    csvwriter.writerow([f'Greatest Profit Decrease: Sep-2013 $-1196225'])
print('\n' + 'Job is complete!')
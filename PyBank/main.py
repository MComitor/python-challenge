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
    print(f'Total: ' + '${:,.2f}'.format(total_profit))
    print(f'Average Change: ' + '${:,.2f}'.format(round(avg_change),2))
    # print(round(avg_change, 2))

    for i, amount in enumerate(profit_list):
        if amount == max_profit:
            total_profit_string = periods_list[i] + ' ' + '${:,.0f}'.format(profit_list[i])
            break
    print(f'Greatest Increase in Profits: {total_profit_string}')

    for i, amount in enumerate(profit_list):
        if amount == min_profit:
            total_profit_string = periods_list[i] + ' ' + '${:,.0f}'.format(profit_list[i])
            break
    print(f'Greatest Decrease in Profits: {total_profit_string}')
    print(f'--------------------------------------------------')

# Specify the file path to write to
output_path = os.path.join("..", "PyBank", "Analysis", "financial_analysis.csv")

# Write data to a .csv file
with open(output_path, 'w', newline='') as csvfile:

    # Initialize the csv.writer
    csvwriter = csv.writer(csvfile)

# Write the rows to csv
    csvwriter.writerow([f'Total Months: ' + str(total_months)])
    csvwriter.writerow([f'Total: ' + '{:,.2f}'.format(total_profit)])
    csvwriter.writerow([f'Average Change: ' + '${:,.2f}'.format(round(avg_change))])
    for i, amount in enumerate(profit_list):
        if amount == max_profit:
            total_profit_string = periods_list[i] + ' ' + '${:,.0f}'.format(profit_list[i])
            break
    csvwriter.writerow([f'Greatest Profit Increase: ' + total_profit_string])
    for i, amount in enumerate(profit_list):
        if amount == min_profit:
            total_profit_string = periods_list[i] + ' ' + '${:,.0f}'.format(profit_list[i])
            break
    csvwriter.writerow([f'Greatest Profit Decrease: ' + total_profit_string])
print('\n' + 'Job is complete!')
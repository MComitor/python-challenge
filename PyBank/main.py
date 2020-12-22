# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files so we don't have to parse manually
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print("{csv_header}")

    # Read each row of data after the header
     for row in csvreader:
         def 
        #  if float(row[7]) >= 5:
        #  print(row)

        fiber = float(row[7])
        if fiber >= 5:
            print(row)

# Specify the file to write to
# output_path = os.path.join("..", "Analysis", "financial_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

         
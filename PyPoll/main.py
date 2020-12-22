# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ````

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files so we don't have to parse manually
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

# Store the file path associated with the file (note the backslash may be OS specific)
# file = '../Resources/input.txt'

# # Open the file in "read" mode ('r') and store the contents in the variable "text"
# # with / open <file name> 'r' read file as text
# with open(file, 'w') as csv:

#     # This stores a reference to a file stream
#     print(text)

#     # Store all of the text inside a variable called "lines"
#     lines = text.read()

#     # Print the contents of the text file to "lines"
#     print(lines)


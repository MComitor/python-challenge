# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

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

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import the os and csv modules
import os
import csv
import statistics

# Path to my csv file
csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')
# print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    header = next(csvreader)
    print(header)
    print(list)

# # Create the lists to search through
    voter_list = []
    candidate_list = []
    # vote_percent = 0

# function to get unique values 
# def unique(candidate_list): 
    # khan_count = candidate_list.count("Khan") 

    # Read each row of data after the header
    for i, row in enumerate(csvreader):
        voter_list.append(int(row[0]))
        candidate_list.append(row[2])

        # if name not in candidate_list: 
        #     print(candidate_list(row[i])) 
    total_votes = len(voter_list)
    correy_count = candidate_list.count("Correy")
    khan_count = candidate_list.count("Khan")
    li_count = candidate_list.count("Li")
    otooley_count = candidate_list.count("O'Tooley")
    correy_percent = round(correy_count / total_votes * 100, 2)
    khan_percent = round(khan_count / total_votes * 100, 2)
    li_percent = round(li_count / total_votes * 100, 2)
    otooley_percent = round(otooley_count / total_votes * 100, 2)

    # Print list
    print("--------------------------------")
    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}") 
    print("--------------------------------")
    print(f"Correy: {correy_percent}% ({correy_count})")
    print(f"Khan: {khan_percent}% ({khan_count})")
    print(f"Li: {li_percent}% ({li_count})")
    print(f"O'Tooley: {otooley_percent}% ({otooley_count})")
    print("--------------------------------")

    # traverse for all elements 
    # for name in candidate_list: 
    #     # check if exists in unique_list or not 
    #     if name not in unique_candidate_list: 
    #         unique_candidate_list.append(name) 
    # print list 
    # for x in unique_candidate_list: 
    #     print(name)

#     # function to get unique values 
#     def unique(candidate_list): 
      
#         for name in candidate_list: 
#             print(name) 
#             total_votes = len(voter_list)
#             print(total_votes)
#             print(candidate_list[2])

# Store the file path associated with the file (note the backslash may be OS specific)
# file = 'PyPoll/Analysis/PyPollAnalysis.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
# with open(file, 'w') as csv:

# This stores a reference to a file stream
#     print(text)

# Store all of the text inside a variable called "lines"
#     lines = text.read()

# Print the contents of the text file to "lines"
#     print(lines)

    # Creating a dictionary
    # election_results = {'Total Votes': 3, 'Candidate Name': 5, 'Winner': 1}
    # Printing the dictionary
    # print(election_results)



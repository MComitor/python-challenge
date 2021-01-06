# Import the os and csv modules
import os
import csv
import pandas as pd

# Path to my csv file
csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

# print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    reader = next(csvreader)

# Create the lists to search through
    voter_list = []
    candidate_list = []

    # Read each row of data after the header
    for i, row in enumerate(csvreader):
        voter_list.append(int(row[0]))
        candidate_list.append(row[2])

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

# Create dictionary of candidates using total votes per candidate   
candidates = {"Correy": correy_count, 
                "Khan": khan_count,
                "Li": li_count,
                "O'Tooley": otooley_count}                 

# Determine the winner
winner = max(candidates, key=candidates.get)
print(f"Winner: {winner}!!!")
print("--------------------------------")

# # Specific file to write to 
output_path = os.path.join("..", "PyPoll", "Analysis", "PyPollAnalysis.csv")

# # Open the file using the "write" mode. Specifiy the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize the csv.writer
    csvwriter = csv.writer(csvfile)

    # # Create a DataFrame using a dictionary of lists
    election_results_df = pd.DataFrame({
        "Candidate": ["Correy", "Khan", "Li", "O'Tooley"],
        "Votes": [704200, 2218231, 492940, 105630],
        "Percentage of Total": [20.0, 63.0, 14.0, 3.0]
    })

    # Write rows to the csv file
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes: ' + str(total_votes)])
    csvwriter.writerow([])
    csvwriter.writerow([election_results_df])
    csvwriter.writerow([])
    csvwriter.writerow(['Winner: ' + (winner)])
    print('\n' + "Job is complete!")
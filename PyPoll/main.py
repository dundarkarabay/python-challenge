#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Libraries
import os
import csv

# Establish a path to access the input file
csv_path = os.path.join(".","Resources","election_data.csv")

# Setting up variables
voter_count = 0
votes = []
candidates = []
vote_counts = []

# (1) Opening the csv file (2) Calculating the number of voters while appending each individual vote into a list 
with open(csv_path, "r", newline = "") as file_handler:
    csv_reader = csv.reader(file_handler, delimiter = ",")
    header = next(csv_reader) # This creates a list called "header" from the first row and moves us to the next one
    for row in csv_reader:
        if (row[0] != "" and row[1] != "" and row[2] != ""): # excluding the rows with empty cells (if there is any)
            voter_count += 1
            votes.append(row[2])
            if row[2] not in candidates:
                candidates.append(row[2])
print(f"""Election Results
---------------------------
Total Votes: {voter_count}
---------------------------""")                

# Setting each candidates' vote count as 0 at the beginning 
for i in range(len(candidates)):
    vote_counts.append(0)

# Calculating each candidate's number of votes
for i in range(len(votes)):
    for j in range(len(candidates)):
        if votes[i] == candidates[j]:
            vote_counts[j] += 1

# (1) Calculating the percentages (2) Printing those and number of votes out to terminal (3) Computing the winner
percentages = []
for i,j in zip(candidates, vote_counts):
    percentage = round((j/voter_count) * 100,3)
    percentages.append(percentage) # Percentages list will be used when writing the results into a text file 
    print(f"{i}: {percentage}% ({j})")
    if j == max(vote_counts):
        winner = i
print("---------------------------")
print(f"Winner: {winner}")

# Writing the output into a text file called output.txt
output_path = os.path.join(".","Resources","output.txt")
with open(output_path,"w") as file_handler:
    output_writer = file_handler.write("""Election Results
---------------------------
Total Votes: """)
    output_writer = file_handler.write(str(voter_count))
    output_writer = file_handler.write("""
---------------------------
""")

    for i in candidates:
        output_writer = file_handler.write(str(i))
        output_writer = file_handler.write(", ")
    output_writer - file_handler.write("""
""")
    for i in percentages:
        output_writer = file_handler.write(str(i))
        output_writer = file_handler.write("%, ")
    output_writer - file_handler.write("""
""")
    for i in vote_counts:
        output_writer = file_handler.write(str(i))
        output_writer = file_handler.write(", ")
    output_writer - file_handler.write("""
""")

    output_writer = file_handler.write("""
---------------------------
Winner: """)
    output_writer = file_handler.write(winner)


# In[ ]:





import os
import csv

#election_data_csv = os.path.join("Resources", "election_data.csv")
path = "C:/Users/carol/OneDrive/Documents/Uni/homework/python-challenge/PyPoll/Resources/election_data.csv"

#path to output file to
text_path = "PyPoll.txt"

total_votes = 0
candidates = []
candidate_vote = {}

#open & read the csv
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row first (skip if no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    #read each row after header
    for row in csv_reader:
    #count the number of months
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_vote[row[2]] = 0

        candidate_vote[row[2]] = candidate_vote[row[2]] +1
        
#c is key in dictionary
    print("Total Votes: ", total_votes)
    print(" ")
    for c in candidate_vote:
        v = candidate_vote[c]
        print(c, v/total_votes, v)

#write changes to txt
with open(text_path, 'w') as file:

    text_to_write = (
        f"Total Votes: {total_votes}\n"
        f"\n"
        f"--------------------------\n"
        f"\n"
        f"{c} : {(v/total_votes):.3%}  ({v})"
        f"\n"
        f"Winner:"
        )
    file.write(text_to_write)

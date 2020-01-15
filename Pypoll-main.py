#import os & csv
import os
import csv

#create path
election_data = os.path.join("election_data.csv")

#list for storage and variables
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

#open and read the csv file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimter = ",")
    csv_header = next(csvreader)

    #go though and add to vote counter
    for row in csvreader:
        total_votes += 1

    #add candiadte to list if not their and add votes
        if row [2] not in candidates
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append[1]
        else:
            index = candidates.index(row[2])
            num_votes[index] +=1

    #add to percent_votes list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    #find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

#print results
print("Election Results")
print("-") * 80
print(f"Total Votes: {str(total_votes)}")
for i in range(len(candidates)):
    print(f"{candidates[1]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print(f"Winner: {winning_candidate}")

#export to txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "-" * 80
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str(f"Winner: {winning_candidate}")
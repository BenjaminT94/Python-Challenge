import os
import csv
input_file = os.path.join("..", "Resources", "election_data.csv")
with open("election_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    votes_total = 0
    candidates = []
    candidate_votes = {}
    winning_candidate = ""
    winning_votes = 0
    winning_percentage = 0
    for row in csvreader:
        votes_total = votes_total + 1
        


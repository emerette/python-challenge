import os
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    print (csvreader)

    csv_header = next(csvreader)
    print(f"Election Results: ")
    print("--------------------------")

    candidates = []
    votes = []
    count = 0

    for row in csvreader:
        count += 1
        candidate = row[2]

        if candidate in candidates:
            votes[candidates.index(candidate)] += 1
        else:
            candidates.append(candidate)
            votes.append(1)

    print("Total Votes: " + str(count))
    print("--------------------------")

    for i in range(len(candidates)):
        print(candidates[i] + ": " + str(round((votes[i]/count) * 100,4)) + "% (" + str(votes[i]) + ")")

    print("--------------------------")
    
    winner = candidates[votes.index(max(votes))]
    print("Winner: "  + winner)

    print("--------------------------")

    outputpath = os.path.join("Analysis", "analysis.txt")
    with open(outputpath, "w") as output:
        output.write(" Election Results: \n")
        output.write("--------------------------\n")
        output.write(" Total Votes: " + str(count) + "\n")
        output.write("--------------------------\n")
        for i in range(len(candidates)):
            output.write(candidates[i] + ": " + str(round((votes[i]/count) * 100,4)) + "% (" + str(votes[i]) + ")\n")
        output.write("--------------------------\n")
        output.write("Winner: "  + winner + "\n")
        output.write("--------------------------")
    
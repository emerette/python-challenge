import os
import csv
from statistics import mean

csvpath = os.path.join( 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    print (csvreader)

    csv_header = next(csvreader)
    print(f"Financial Analysis: ")
    print("--------------------------")

    count = 0
    total = 0

    # Count = number of rows there are
    # Total = total amt of profit/loss

    diffs = []
    prev = 0
    biggest = []
    smallest = []

    for row in csvreader:
        count += 1
        current = int(row[1])
        total += current

        if count > 1:
            diffs.append(current - prev)
            if int(biggest[1]) < current:
                biggest = [row[0], (current-prev)]
            if int(smallest[1]) > current:
                smallest = [row[0], (current-prev)]
        if count == 1:
            biggest = row
            smallest = row
        
        prev = current

    averagechange = sum(diffs)/len(diffs)
    print(averagechange)


    print(" Total Months: " + str(count))
    print(" Total: $" + str(total))
    print(" Average Change: $" + str(averagechange))
    print(" Greatest Increase in Profits: " + biggest[0] + " ($" + str(biggest[1]) + ") ")
    print(" Greatest Decrease in Profits: " + smallest[0] + " ($" + str(smallest[1]) + ") ")

    outputpath = os.path.join("Analysis", "analysis.txt")
    with open(outputpath, "w") as output:
        output.write(" Financial Analysis\n")
        output.write("--------------------------\n")
        output.write(" Total Months: " + str(count) + "\n")
        output.write(" Total: $" + str(total) + "\n")
        output.write(" Average Change: $" + str(averagechange) + "\n")
        output.write(" Greatest Increase in Profits: " + biggest[0] + " ($" + str(biggest[1]) + ") \n")
        output.write(" Greatest Decrease in Profits: " + smallest[0] + " ($" + str(smallest[1]) + ") \n")

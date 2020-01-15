#import os & csv
import os
import csv

#create path
budget_data = os.path.join("budget_data.csv")

#create empty list and variables
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#open and read the csv file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimter = ",")

    #read the header row
    csv_header = next(csvreader)

    #read the first row and track the changes
    first_row = next(cvsreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    #go though each row after the head and first row
    for row in csvreader:
        dates.append(row[0])

        #calculate the change, and then add it to the lists that changed, total number of months,
        #total amounts of profits and loses over the entire time
        change = int(row[1])-value
        profits.append(changes)
        value = int(row[1])
        total_months += 1
        total_pl = total_pl + int(row[1])

    #greatest increase, decreases, & avaerga change in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_inrease)
    greatest_date = dates[greatest_index]
    greatest_decrease = min(porfits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]
    avg_change = sum(profits)/len(profits)

#print financial information
print("Financial Analysis")
print("-") * 80
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greastest Decrease in Profits: {worst_date} (${str(greastest_decrese)})")

#export txt file
output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "-" * 80
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greastest Decrease in Profits: {worst_date} (${str(greastest_decrese)})")
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
    csvreader = csv.reader(csvfile, delimiter = ",")

    #read the header row
    csv_header = next(csvreader)

    #read the first row and track the changes
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    #go though each row after the head and first row
    for row in csvreader:
        dates.append(row[0])

        #calculate the change, and then add it to the lists that changed, total number of months,
        #total amounts of profits and loses over the entire time
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        total_months += 1
        total_pl = total_pl + int(row[1])

    #greatest increase, decreases, & avaerga change in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]
    avg_change = sum(profits)/len(profits)

#print financial information
print("Financial Analysis")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greastest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#export txt file
output = open("output.txt", 'w')
line1 = "Financial Analysis"
line2 = str(f"Total Months: {str(total_months)}")
line3 = str(f"Total: ${str(total_pl)}")
line4 = str(f"Average Change: ${str(round(avg_change,2))}")
line5 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line6 = str(f"Greastest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
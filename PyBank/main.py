import os
import csv

#path to read csv
path = "C:/Users/carol/OneDrive/Documents/Uni/homework/python-challenge/PyBank/Resources/budget_data.csv"

#path to output file to
text_path = "PyBank.txt"

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999999999999999]
total_net = 0

#open & read the csv
with open(path) as financial_data:
    csv_reader = csv.reader(financial_data, delimiter=",")

    #read the header row first (skip if no header)
    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")

    #define 1st row to calc from
    first_row = next(csv_reader)
    first_net = int(first_row[1])
     

    #count the number of months
    for row in csv_reader:
        total_months += 1
        #total the Profit/Loss
        profit_loss = int(row[1])
        total_net += int(profit_loss)
    
    #Net change by month
    #int(row[1]) = current column of Profit &loss
        net_change = int(row[1])-first_net

        first_net = int(row[1])
        net_change_list += [net_change]
        if net_change>greatest_increase[1]:
            greatest_increase[1]=net_change
            greatest_increase[0]=row[0]
        if net_change < greatest_decrease[1]:
            greatest_decrease[1]=net_change
            greatest_decrease[0]=row[0]

    #average change = (net change by month / number of months)
    #sum(net_change_list)
    avge_change = round((sum(net_change_list)/ (total_months)),2)

    print("Financial Analysis")
    print("")
    print("----------------------")
    print("")
    print("Total Months: ", total_months)
    print("")
    print("Total: $", total_net)
    print("")
    print("Average Change: $", avge_change)
    print("")
    print("Greatest Increase in Profits: ",greatest_increase[0], "$",greatest_increase[1])
    print("")
    print("Greatest Decrease in Profits: ",greatest_decrease[0], "$",greatest_decrease[1])
    print("")
   
#write changes to csv
with open(text_path, 'w') as file:
   
    text_to_write = (
                 f"Financial Analysis\n"
                 f"\n"
                 f"---------------------------\n"
                 f"\n"
                 f"Total Months: {total_months} \n"
                 f"\n"
                 f"Total: ${total_net}\n"
                 f"\n"
                 f"Average Change: ${avge_change}\n"
                 f"\n"
                 f"Greatest Increase in Profits: {greatest_increase[0]}  $({greatest_increase[1]})"
                 f"\n"
                 f"Greatest Decrease in Profits: {greatest_decrease[0]}  $({greatest_decrease[1]})"
                 )
    file.write(text_to_write)

# python-challenge
module 3 challenge

csv files for both PyBank and PyPoll were read from their respective folders.
In PyBank, total monthly changes to the profit/loss were captured.   The net value of these changes and its average were returned.  I had issues calculating the greatest descrease & increase so had a Tutor assist.  I did not notice that the previous calculations had been broken when this change was done.  I am unable to correct the issue on my own.
Outputs to txt files were generated.

## Acknowledgements
The code implementation for net_change_list was assisted by Tutor Limei Hou. 
### Code provided to tutor
#count the number of months
    for row in csv_reader:
        total_months += 1 
        #total the Profit/Loss
        profit_loss = float(row[1])
        total_net += int(profit_loss)

### Code advised by tutor to assist with net change
#int(row[1]) = current column of Profit &loss
        net_change = int(row[1])-first_net

        first_net = int(row[1])
        net_change_list += [net_change]

### Code provided to tutor
if net_change>greatest_increase[1]:
            greatest_increase[1]=net_change
            greatest_increase[0]=row[0]
        if net_change < greatest_decrease[1]:
            greatest_decrease[1]=net_change
            greatest_decrease[0]=row[0]


The insights and code helped calculate the net change but unfortunately broke the previously correct Total Months and Total values.

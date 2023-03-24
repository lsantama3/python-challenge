#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

#total month count
total_month_count = 0

#total amount of "Profit/Losses" over the entire period
total_pl = 0

#dates for increase/decrease
dates_bank = []

#profit from each row
profit_row = []

#chnage between rows
change_profit = []

greatest_increase = 0
greatest_decrease = 0

csvpath = os.path.join('.','Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    file = csv.reader(csvfile, delimiter = ',')
    
    #read the header row first
    csv_header = next(file)
    
    #read each row of csvreader after the header
    for row in file:
        total_month_count +=1
    
        total_pl += int(row[1])
    
        dates_bank.append(row[0])
    
        profit_row.append(int(row[1]))

for i in range(len(profit_row)-1):
    change_pl= profit_row[i+1] - profit_row[i]
    change_profit.append(change_pl)
    
    average_of_change = round(sum(change_profit)/len(change_profit), 2)
    

    if (change_pl > greatest_increase):
        gi_month = dates_bank[i+1]
        greatest_increase = change_pl

    if (change_pl < greatest_decrease):
        gd_month = dates_bank[i+1]
        greatest_decrease = change_pl
    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_month_count}") 
print("Total: $" + str(total_pl))
print(f"Average Change: ${average_of_change}")
print(f"Greatest Increase in Profits: {gi_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {gd_month} (${greatest_decrease})")

output_file = os.path.join(".", "Financial_Analysis.txt")
with open(output_file, 'w', newline='') as text:
    text.write(" Financial Analysis\n")
    text.write("---------------------------------- \n")
    text.write(f"Total Months: {total_month_count}\n") 
    text.write(f"Total: $ {total_pl}\n")
    text.write(f"Average Change: ${average_of_change}\n")
    text.write(f"Greatest Increase in Profits: {gi_month} (${greatest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {gd_month} (${greatest_decrease})\n")


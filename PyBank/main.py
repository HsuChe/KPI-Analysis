import os
import csv

# list if the directory that the csv is located in
csv_path = os.path.join("PyBank","Resources","budget_data.csv")

# Create a parser that loads the csv and gennerate a list

# function for finding total profit / loss based on a list
def total_profit(list):
    net = 0
    for month in range(1,len(list)):
        net = net + int(list[month][1])
    return net

# funnction that finds the average change and the list of change month to month
def month_change(list):
    change_list = []
    for month in range(1, len(list)-1):
        current_price, next_price = int(list[month][1]), int(list[month+1][1])
        change = next_price - current_price
        change_list.append(change)
    return change_list
    
def average_profit(change_list):
    average_change = sum(change_list) / len(change_list)
    average_change = round(average_change)
    return average_change

def greatest_change(list):
    change_list = month_change(list)
    greatest_increase, greatest_decrease = max(change_list), min(change_list) 
    gi_month = list[change_list.index(greatest_increase)+2][0]
    gd_month = list[change_list.index(greatest_decrease)+2][0]
    return gi_month, gd_month, greatest_increase, greatest_decrease

def summary_table(list):
    total_month = len(list)
    net = total_profit(list)
    average_change = average_profit(month_change(list))
    gi_month, gd_month, greatest_increase, greatest_decrease = greatest_change(list)
    report = f'''

    Financial Analysis
    ----------------------------
    Total Months: {total_month}
    Total: {net}
    Average Change: ${average_change}
    Greatest Increase in Profits: "{gi_month} ({greatest_increase})"
    Greatest Decrease in Profits: "{gd_month} ({greatest_decrease})"

    '''
    return report

def parse_csv():
    with open(csv_path) as file:
        csv_read = csv.reader(file)
        csv_list = []
        for row in csv_read:
            csv_list.append(row)
        summary = summary_table(csv_list)
    print (summary)
    with open (os.path.join("PyBank","analysis","analysis.txt"),"w") as file1:
        file1.write(summary)


    
    

# save the csv list to a variable

# Total number of month

#print(summary_table(csv_list))
print(parse_csv())

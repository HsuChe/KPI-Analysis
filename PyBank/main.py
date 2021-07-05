# impor the relevent libraries
import os
import csv
# library to define currennt to be used to make daily summary text unique
from datetime import date

# list if the directory that the csv is located in
csv_path = os.path.join("Resources","budget_data.csv")
# list the directory that the summary table text file will be generated in.
analysis_path = os.path.join("Analysis",f"analysis_{date.today()}.txt")

# load all the functions that would be used in our parser.
# function for finding total profit / loss based on a list
def total_profit(list):
    net = 0
    for month in range(1,len(list)):
        net = net + int(list[month][1])
    return net

# function that creates the difference month to month and makes it into a list for processing
def month_change(list):
    change_list = []
    for month in range(1, len(list)-1):
        current_price, next_price = int(list[month][1]), int(list[month + 1][1])
        change = next_price - current_price
        change_list.append(change)
    return change_list

# find the average change in profit and losses month to month
def average_profit(change_list):
    average_change = sum(change_list) / len(change_list)
    average_change = round(average_change)
    return average_change

# find the maximum change and minimum change within the list of monthly changes
# generate the monnths that that maximum changes occured in.
def greatest_change(list):
    change_list = month_change(list)
    header_loc = 1
    month_loc = 1
    # find the highest and lowest monthly changes in the monnthly changes list
    greatest_increase, greatest_decrease = max(change_list), min(change_list) 
    # find the specific date that the highest and lowest monthly changes take place in.
    gi_month = list[change_list.index(greatest_increase) + header_loc + month_loc][0]
    gd_month = list[change_list.index(greatest_decrease) + header_loc + month_loc][0]
    return gi_month, gd_month, greatest_increase, greatest_decrease

def summary_table(list):
    # define the variables that will be used inn the summary table f' stringn
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
    # return the string
    return report

def analysis_gen(string, path):
    with open (path,"w") as file1:
            file1.write(string)

# activationn function ----------------------------------------------
def main():
    #parse the csv given the path
    with open(csv_path) as file:
        csv_read = csv.reader(file)
        # transform the parsed csv to a list for processing
        csv_list = []
        for row in csv_read:
            csv_list.append(row)
        # generate the summary table f' string
        summary = summary_table(csv_list)
    # put summary table into the terminal
    print (summary)
    # generate a .txt file and write f' string into the text file.
    analysis_gen(summary,analysis_path)
    print("text file generation complete!")

main() 


<br />
<p align="center">

  <h3 align="center">Stock Ticker Summary Table</h3>

  <p align="center">
     An explanation for the creation of a summary table from ticker information
    <br />
    <a href="https://github.com/HsuChe/python-challenge"><strong>Project Github URL »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project

![hero image](https://github.com/HsuChe/python-challenge/blob/f3e0d54ab0d2365f8a35dd1a83ef981b05c49644/Image/PyBank_Hero.jpg)

Month to month analysis is critical to making operating decisions. For this homework, we are going to generate commonly used business metrics based on the monthly financial information.

Features of the dataset:
* The dataset is divided primarily between three sheets for each of the years that are being analyzed, starting with 2014 and ending on 2016.
* The following are columns provided by the dataset: 
    * Date: **The date that the information was generated**
    * Profit/Loss: **The profit and loss from a month before**
* The dataset is in the csv file format with delimiter of comma

* Download Dataset click [HERE](https://github.com/HsuChe/python-challenge/blob/f3e0d54ab0d2365f8a35dd1a83ef981b05c49644/PyBank/Resources/budget_data.csv)

The homework is interested generating a few specific items for the summary table.

* Total months accounted for in the dataset.
* Aggregate change given the entire dataset.
* Average change month to month.
* Month with the greatest increase in profits.
* Month with the greatest decrease in profits.

<!-- GETTING STARTED -->
## Processing the csv and make it into a easier to use dataset.

Open the csv with csv.reader() and using a for loop to iterate through each row and adding them to a list.

* For loop to add to list
  ```sh
  csv_list = []
  for row in csv_read:
    csv_list.append(row)
  ```

After generating the csv list, find the total number of month being accounted for. To do this, we will find the index of the rows.

* Finding the total month accounted for.
  ```sh
  total_month = len(list)
  Next i
  ```

### Finding the total net profit/loss

To find the totla net profit / loss, we will be using a loop that will iterate through each row in the data list and add up all of the values from loss/profit column

* Total Profit Function:
  ```sh
  def total_profit(list):
    net = 0
    for month in range(1,len(list)):
        net = net + int(list[month][1])
    return net  
  ```

### Average month to month change.

Next we find the average change month to month. The difference between the months will be put into a list.

* Headers for generated columns
  ```sh
  def month_change(list):
    change_list = []
    for month in range(1, len(list)-1):
        current_price, next_price = int(list[month][1]), int(list[month + 1][1])
        change = next_price - current_price
        change_list.append(change)
    return change_list
  ```

## Calculating the avearge change in profit / loss

The average change in profit / loss is the sum of the change list divided by the length of the change list. 

* Avearge change in profit and losses month to month  
    ```sh
    def average_profit(change_list):
            average_change = sum(change_list) / len(change_list)
            average_change = round(average_change)
        return average_change
    ```

## Calculating the greatest increase and decrease in profit / loss month to month

The great increase and decrease is calculated by calculating the max and min of the change list and while referencing their index location to find the months that these changes happened. 

* Finding the highest increase and decrease in profit / loss in the dataset.
  ```sh
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
  ```

The fact that our opening price will be extracted after the current iteration of unique value is calculated, we would have to calculate the price change year on year as well as the percentage change before updating a new opening price from the conditional.

* Store Yearly Change and Yearly Percent Change to memory
  ```sh
  YearlyChange = ClosingPrice - OpeningPrice
  ```

## Generate the summary table as a string.

We for variables for each of the information we calculated before and map them into a string. 

* Mapping the calculated value into the string. 
  ``` sh
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
  ```

## Generating the text file and terminal message with the summary table.

To generate the text file, we will be writing the string information into it.

* Second error checking outside the conditional that triggers when unique value is found
  ```sh
  def analysis_gen(string, path):
    with open (path,"w") as file1:
            file1.write(string)
  ```

## After everything is generated, we complete the PyBank portion of the assignment.

<br>
<br>
<br>

<!-- ABOUT THE PROJECT -->
## About The Project

![hero image](https://github.com/HsuChe/python-challenge/blob/f3e0d54ab0d2365f8a35dd1a83ef981b05c49644/Image/PyPoll_Hero.jpg)

Visualizing and processing voting data is how we can find our the winner and calculate critical descriptions through analyzing polling data. 

Features of the dataset:
* Voter ID: **The unique ID that each vote is identified by**
* County: **Name of the county where the vote was casted**
* Candidate: **Name of the candidate the vote was casted for**

* Download Dataset click [HERE](https://github.com/HsuChe/python-challenge/blob/f3e0d54ab0d2365f8a35dd1a83ef981b05c49644/PyPoll/Resources/election_data.csv)

The homework is interested generating a few specific items for the summary table.

* Total of votes casted
* Percentage of the total vote each candidate recieved
* Winner of the election.

<!-- GETTING STARTED -->
## Processing the csv and make it into a easier to use dataset.

Open the csv with csv.reader() and using a for loop to iterate through each row and adding them to a list.

* For loop to add to list
  ```sh
  csv_list = []
  for row in csv_read:
    csv_list.append(row)
  ```

After generating the csvlist, find the total number of votes being accounted for. To do this, we will find the index of the rows.

* Finding the total votes accounted for.
  ```sh
  total_vote = len(list)
  Next i
  ```

### Find information for each candidate

## Preprocessing information and putting them into a dictionary.

To find the specific information for each candidate, the first step is to find the list of unique candidates, to do this, we can generate a list and append each name into a list when a new iteration appears.

* Unique candidate function:
  ```sh
  def UniqueCandidate(datalist):
    UniqueList = []
    for vote in range(1, len(datalist)):
        if datalist[vote][2] not in UniqueList:
            UniqueList.append(datalist[vote][2])
    return UniqueList
  ```

### Finding out the amount of votes each candidate recieved.

We can find out the amount of votes each candidate recieved based on unique candidate names.

* Candidate vote counter:
  ```sh
  def CandidateCounter(candidate, datalist):
    CandidateCount = 0
    for vote in datalist:
        if vote[2] == candidate:
            CandidateCount += 1
    return CandidateCount
  ```

## Find the winner and total votes. 

To find the winner, we will iterate through each candidate within unique candidate information and then find the name through index of the maximum vote count. To do this, we will first create a dictionary with unique candidate names and add voting information based on candidates to the dictionary. 

* Generating and adding candidate voting information to dictionary
    ```sh
    CandidateInfo = {}
    for candidate in UniqueCandidate(datalist):
        CandidateCount = CandidateCounter(candidate,datalist)
        PercentVote = (CandidateCount/totalvote)*100
        StringConvert = "%.3f" % PercentVote + "%"
        CandidateInfo[candidate] = [CandidateCount,StringConvert]
    ```

* Comparing candidate vote count to find the winner  
    ```sh
    def winner(CandidateDict):
        winner = ''
        winning_vote = 0
        for candidate in CandidateDict:
            if CandidateDict[candidate][0] > winning_vote:
                winning_vote = CandidateDict[candidate][0]
                winner = candidate
        return winner
    ```
* Putting the rest of the information into the dictionary. 
    ```sh
    CandidateInfo['Winner'] = winner(CandidateInfo)
    CandidateInfo['Total'] = totalvote
    ```

## Generate the summary table as a string.

We for variables for each of the information we calculated before and map them into a string. 

* Mapping the calculated value into the string. 
  ``` sh
  def parser(CandidateDict):
    string = f'''
        Election Results
        -------------------------
        Total Votes: {CandidateDict['Total']}
        -------------------------
        Khan: {CandidateDict['Khan'][1]} ({CandidateDict['Khan'][0]})
        Correy: {CandidateDict['Correy'][1]} ({CandidateDict['Correy'][0]})
        Li: {CandidateDict['Li'][1]} ({CandidateDict['Li'][0]})
        O'Tooley: {CandidateDict["O'Tooley"][1]} ({CandidateDict["O'Tooley"][0]})
        -------------------------
        Winner: {CandidateDict['Winner']}
        -------------------------
        '''
    return string
  ```

## Generating the text file and terminal message with the summary table.

To generate the text file, we will be writing the string information into it.

* Second error checking outside the conditional that triggers when unique value is found
  ```sh
  def analysis_gen(string, path):
    with open (path,"w") as file1:
            file1.write(string)
  ```

## After everything is generated, we complete the PyBank portion of the assignment.
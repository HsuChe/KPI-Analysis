# impor the relevent libraries
import os
import csv
# library to define currennt to be used to make daily summary text unique
from datetime import date

# list if the directory that the csv is located in
poll_csvpath = os.path.join("Resources","election_data.csv")
# list the directory that the summary table text file will be generated in.
analysis_path = os.path.join("analysis",f"analysis_{date.today()}")

# load all the functions that would be used in our parser.

# Function to generate unique candidates and put them into a list
def UniqueCandidate(datalist):
    UniqueList = []
    for vote in range(1, len(datalist)):
        if datalist[vote][2] not in UniqueList:
            UniqueList.append(datalist[vote][2])
    return UniqueList

# Funciton to count the number of votes each candidate has gotten based on name.
def CandidateCounter(candidate, datalist):
    CandidateCount = 0
    for vote in datalist:
        if vote[2] == candidate:
            CandidateCount += 1
    return CandidateCount

# Funciton generating the name of the winner.
def winner(CandidateDict):
    winner = ''
    winning_vote = 0
    for candidate in CandidateDict:
        if CandidateDict[candidate][0] > winning_vote:
            winning_vote = CandidateDict[candidate][0]
            winner = candidate
    return winner
    
# Function generating candidate information and put into a dictionary.
def CandidateDict(totalvote, datalist):
    CandidateInfo = {}
    for candidate in UniqueCandidate(datalist):
        CandidateCount = CandidateCounter(candidate,datalist)
        PercentVote = (CandidateCount/totalvote)*100
        StringConvert = "%.3f" % PercentVote + "%"
        CandidateInfo[candidate] = [CandidateCount,StringConvert]
    CandidateInfo['Winner'] = winner(CandidateInfo)
    CandidateInfo['Total'] = totalvote
    return CandidateInfo

# Function to Parse the information into a string.
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

# Funciton to generate the text file to analysis folder
def analysis_gen(string, path):
    with open (path,"w") as file1:
            file1.write(string)

# activationn function ----------------------------------------------
def main():

    with open(poll_csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        csvlist = []
        for row in csvreader:
            csvlist.append(row)
            
    total_vote = len(csvlist) - 1
    CandidateInformation = CandidateDict(total_vote, csvlist)
    print(parser(CandidateInformation))
    analysis_gen(parser(CandidateInformation),analysis_path)
    print("text file generation complete!")

main()
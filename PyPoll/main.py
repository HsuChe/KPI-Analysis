import os
import csv
from datetime import date

poll_csvpath = os.path.join("Resources","election_data.csv")
analysis_path = os.path.join("analysis",f"analysis_{date.today()}")

def CandidateCounter(candidate, data_list):
    CandidateCount = 0
    for vote in data_list:
        if vote[2] == candidate:
            CandidateCount += 1
    return CandidateCount

def CandidatePercent (candidate_vote,total):
    return float(candidate_vote)/total

def winner(CandidateDict):
    winner = ""
    winning_vote = 0
    for candidate in CandidateDict:
        if CandidateDict[candidate][0] > winning_vote:
            winning_vote = CandidateDict[candidate][0]
            winner = candidate
    return winner

def summary_table (CandidateDict):
    string = f'''

        Election Results
        -------------------------
        Total Votes: {CandidateDict['Total']}
        -------------------------
        Khan: {round(CandidateDict['Khan'][1],3)*100}% ({CandidateDict['Khan'][0]})
        Correy: {round(CandidateDict['Correy'][1],3)*100}% ({CandidateDict['Correy'][0]})
        Li: {round(CandidateDict['Li'][1],3)*100}% ({CandidateDict['Li'][0]})
        O'Tooley: {round(CandidateDict["O'Tooley"][1],3)*100}% ({CandidateDict["O'Tooley"][0]})
        -------------------------
        Winner: {CandidateDict['Winner']}
        -------------------------

        '''
    return string

def parser():
    with open(poll_csvpath) as file:
        csvreader = csv.reader(file)
        csv_list = []
        for row in csvreader:
            csv_list.append(row)
    return csv_list


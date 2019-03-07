import os

import csv

TotalVotes = []
CandidateList = []
unique_list = []
UCandidateList = []
PercentVote = []

x = 0

csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
            
            TotalVotes.append(row[0])
            #Creating a List of all Candidates and All Votes
            CandidateList.append(row[2])
            #Total Number of Votes
            count = len(TotalVotes)
    print("Election Results")
    print(f"Total Votes:  {count}")
   
    #Creating a List of Candidates
    for x in CandidateList: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    
    #Counting the number of Votes for each Unique Candidate 
    for x in unique_list: 
        #print(CandidateList.count(x)) 
        UCandidateList.append(CandidateList.count(x))
    
    #Counting the % of Votes for each Unique Candidate 
    for x in UCandidateList:
        POV = (x/count)*100
        #print(f"{POV:.2f} %")
        PercentVote.append(POV)

    #Max Percent 
    MaxPercentVote = max(PercentVote)
    #Index of MAX Percent 
    IndexofMaxPercentVote = PercentVote.index(MaxPercentVote)
    #Index of MAX Percent Candidate = Winner
    Winner = unique_list[IndexofMaxPercentVote]

    loop = len(unique_list) -1
    y = 0
    while y <= loop:

        print(f"{unique_list[y]} : {PercentVote[y]:.2f}% ( {UCandidateList[y]} )")

        y +=1

    print (f"Winner is : {Winner} ")
   
   
 # Zip lists together

zipped = zip(unique_list, PercentVote, UCandidateList)

# Set variable for output file
output_file = os.path.join("main1.final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #writer.writerow(["Index", "Employee", "Department"])
    writer.writerow(["Election Results"])
    writer.writerow(["------------------"])
    writer.writerow(["Total Votes:"])
    writer.writerow([count])
    writer.writerow(["------------------"])
    writer.writerows(zipped)
    writer.writerow(["------------------"])
    writer.writerow(["Winner is :"])
    writer.writerow([Winner])
    
    
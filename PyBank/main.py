import os

import csv

Months = []
PNL = []
PNL1 = 0
AVG = 0
AVG_Change = []
Change = 0
NetPNL = 0

csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    csv_header = next(csvreader)
    
    #print("CSV Header: " + str(csv_header))

    for row in csvreader:
         
        #Creating List of Months to get total Months
        Months.append(row[0])
        
        #Creating List of Months to get total Months
        NetPNL = int(row[1]) + NetPNL

        #Creating List of Profit and Loss
        Change = (int(row[1]))
        PNL.append(Change)
              
    print(f"Financial Analysis")   
    print(f"----------------------------")         
    print(f"Total Months: {len(Months)}")
    print(f"Total: ${NetPNL}")
    
    
TotalMonths = len(Months)

    #########------------Finding Average Change--------------###
LIST_AVG = []
LIST_AVG1 = []
Decrease = []
Increase = []
DecreaseM = []
IncreaseM = []

j = (len(PNL))
k = (j - 1)
iIncrease = 0
iDecrease = 0
iNext = 0
i = 0
while i < k:
    iPrevious = PNL[i]
    iNext = PNL[i+1]
    iPreviousM = Months[i]
    iNextM = Months[i+1]
    

    if (iPrevious > iNext):
        iDecrease = iNext - iPrevious
        Decrease.append(iDecrease)
        DecreaseM.append(Months[i+1])
        AvgChange = iDecrease/2
        LIST_AVG.append(AvgChange)
        
            
    elif (iPrevious < iNext):
        iIncrease = iNext - iPrevious
        Increase.append(iIncrease)
        IncreaseM.append(Months[i+1])
        AvgChange1 = iIncrease/2
        LIST_AVG1.append(AvgChange1)
    i += 1    

#Calculating AVG Change
aChange = sum(LIST_AVG)/len(LIST_AVG)
bChange = sum(LIST_AVG1)/len(LIST_AVG1)
cchange = (aChange + bChange)/2
print("Average  Change: "+"{:.2f}".format(cchange))

#Calculating MAX INcrease
maxIncrease = max(Increase)
maxIncreaseindex = Increase.index(maxIncrease)
maxIncreaseMIndex = Increase.index(maxIncrease)
maxIncreaseM = IncreaseM[maxIncreaseindex]
print (f"Greatest Increase in Profits: {maxIncreaseM}  $({maxIncrease})")

#Calculating MAXDecrease
minDecrease = min(Decrease)
minDecreaseindex = Decrease.index(minDecrease)
minDecreaseMIndex = Decrease.index(minDecrease)
minDecreaseM = DecreaseM[minDecreaseindex]
print (f"Greatest Decrease in Profits: {minDecreaseM}  $({minDecrease})")



output_file = os.path.join("summary.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    #writer = csv.writer(datafile)

    #writer.writerow(["Index", "Employee", "Department"])
    text_file.write(f"Financial Analysis")
    text_file.write(f"\n----------------------------")
    text_file.write(f"\nTotal Months: {TotalMonths}")
    text_file.write(f"\nTotal: ${NetPNL}")
    text_file.write(f"\nAverage  Change: ${round(cchange,2)}  ")
    text_file.write(f"\nGreatest Increase in Profits: {maxIncreaseM}  ${maxIncrease}")
    text_file.write(f"\nGreatest Decrease in Profits: {minDecreaseM}  ${minDecrease}")
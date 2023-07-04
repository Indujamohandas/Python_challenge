import os
import csv
# open file the excel file
with open("C:/Users/induj/OneDrive/Documents/Repository/Python_challenge/PyPoll/Resources/election_data.csv")as csvfile:
    #print final output to the txt file
    file_save = open("C:/Users/induj/OneDrive/Documents/Repository/Python_challenge/PyPoll/analysis.txt","w")
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row
    csv_header= next(csvreader)
    print(f"csvheader: {csv_header}")
    print("Election Results")
    print("----------------------")
    Total_vote =0
    m=0
    k=0
    j=0
    # print each row in csv file
    for row in csvreader:
        Total_vote= Total_vote+1
        #list is used to assign the candidate names
        candidate_name=["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
        if(row[2]==candidate_name[0]):
            # count the number of votes
            k= k+1
            # prints the percentage
            vote_percentage=float(k)/float(Total_vote)*100
        elif(row[2]==candidate_name[1]):
            # count the number of votes
            j=j+1
            # prints the percentage
            vote_percent=float(j)/float(Total_vote)*100
        elif(row[2]==candidate_name[2]):
            # count the number of votes
            m=m+1
            # prints the percentage
            vote_percenta=float(m)/float(Total_vote)*100
            # if condition is used to select the winning candidate
            if (k>=j)and(k>=m):
                largest=candidate_name[0]
            elif(j>=k)and(j>=m):
                largest=candidate_name[1]
            else:
                largest=candidate_name[2]
     # prints the total number of votes in election_data.csv file           
    print("Total votes:"+str(Total_vote),file=file_save)
    print("---------------------",file=file_save)
    # prints the candidate name, number of votes and percentage
    print(f"Charles Casper Stockham:{k},{vote_percentage:.2f}%",file=file_save)
    # prints the candidate name, number of votes and percentage
    print(f"Diana DeGette:{j},{vote_percent:.2f}%",file=file_save)
    # prints the candidate name, number of votes and percentage
    print(f"Raymon Anthony Doane:{m},{vote_percenta:.2f}%",file=file_save)
    print("---------------------",file=file_save)
    # prints the winning candidate name
    print("Winner is :"+str(largest),file=file_save)
    print("---------------------",file=file_save)
    file_save.close() 








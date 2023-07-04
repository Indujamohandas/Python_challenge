import os
import csv
# open file the excel file
with open("C:/Users/induj/OneDrive/Documents/Repository/Python_challenge/PyBank/Resources/budget_data.csv")as csvfile:
    #print final output to the txt file
    file_save = open("C:/Users/induj/OneDrive/Documents/Repository/Python_challenge/PyBank/analysis.txt","w")
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row
    csv_header= next(csvreader)
    print(f"csvheader: {csv_header}")
    print("Financial Analysis")
    print("----------------------")
    i=0
    j=0
    k=0
    m=0
    sum=0
    # print each row in csv file
    for row in csvreader:
        i=i+1 
        j=int(row[1])+j
        if(i > 1):
            m = int(row[1])-k
        sum = sum + m  
        k=int(row[1])
        if(i == 3):
            a=m
            b=m
        if(i > 2): 
            if(m>a):
                a=m
            if(m<b):
                b=m           
    avg = sum/(i-1)
    # prints the total number of months in budget_data.csv file
    print("Total Months:"+str(i),file=file_save)
    # prints net total amount of profit/losses
    print("Total:"+str(j),file=file_save)
    # changes in the profit/losses
    print("Average change:"+str(avg),file=file_save)
    # how much increse in entire period
    print("Greatesr increase in profit:"+str(a),file=file_save)
    # how much decrease in entire period
    print("Greatest decrease in profit:"+str(b),file=file_save)
    file_save.close() 
    


    






    



    


        



    


import csv
import os
def main():
    with open("Resources/budget_data.csv", newline ='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        count = 0
        total = 0
        numberList = []
        maxNumber = 0
        maxDate = ""
        minNumber = 0
        minDate = ""
        checker = 0
        next(csvreader, None)
        for line in csvreader:
            count += 1
            total += int(line[1])
            if int(line[1]) > maxNumber:
                maxNumber = int(line[1])
                maxDate = line[0]
            if int(line[1]) < minNumber:
                minNumber = int(line[1])
                minDate = line[0]
        average = str(round((total/count),2))
        print("Total Months: " + str(count))
        print("Total $" + str(total))
        print("The average change is $" + average)
        print("Greatest Increase in Profits: " + str(maxDate) + " ($" + str(maxNumber) + ")")
        print("Greatest Decrease in Profits: " + str(minDate) + " ($" + str(minNumber) + ")")
        f = open("output/bank_output.txt" , 'w')
        f.write("Total Months: " + str(count) + "\n")
        f.write("Total $" + str(total) + "\n")
        f.write("The average change is $" + average + "\n")
        f.write("Greatest Increase in Profits: " + str(maxDate) + " ($" + str(maxNumber) + ")" + "\n")
        f.write("Greatest Decrease in Profits: " + str(minDate) + " ($" + str(minNumber) + ")"+ "\n")
 
main()
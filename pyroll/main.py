import csv
import os
def main():
    with open("Resources/election_data.csv", newline ='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)
        count = 0
        countKhan = 0
        countCorrey = 0
        countLi = 0
        countOTooley = 0
        candidateList = []
        for line in csvreader:
            count += 1
            if line[2] not in candidateList:
                candidateList.append(line[2])
            elif line[2] == "Khan":
                countKhan += 1
            elif line[2] == "Correy":
                countCorrey += 1
            elif line[2] == "Li":
                countLi += 1
            elif line[2] == "O'Tooley":
                countOTooley += 1
    decider = [countCorrey, countKhan, countLi, countOTooley]
    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(count))
    print("--------------------")
    print("Khan: " + str(round(((countKhan/count)*100),2)) + "% (" + str(countKhan) + ")")
    print("Correy: " + str(round(((countCorrey/count)*100),2)) + "% (" + str(countCorrey) + ")")
    print("Li: " + str(round(((countLi/count)*100),2)) + "% (" + str(countLi) + ")")
    print("O'Tooley: " + str(round(((countOTooley/count)*100),2)) + "% (" + str(countOTooley) + ")")
    print("--------------------")
    print("Winner: " + str(max(decider)))
    print("--------------------")
    f = open("output/roll_ouput.txt", "w")
    f.write("Election Results \n")
    f.write("-------------------- \n")
    f.write("Total Votes: " + str(count)+'\n')
    f.write("-------------------- \n")
    f.write("Khan: " + str(round(((countKhan/count)*100),2)) + "% (" + str(countKhan) + ")" + '\n')
    f.write("Correy: " + str(round(((countCorrey/count)*100),2)) + "% (" + str(countCorrey) + ")" + '\n')
    f.write("Li: " + str(round(((countLi/count)*100),2)) + "% (" + str(countLi) + ")" + '\n')
    f.write("O'Tooley: " + str(round(((countOTooley/count)*100),2)) + "% (" + str(countOTooley) + ")" + '\n')
    f.write("-------------------- \n")
    f.write("Winner: " + str(max(decider)) + '\n')
    f.write("-------------------- \n")
main()

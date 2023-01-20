import csv

with open('./inputFile.csv', newline='') as csvfile:
    inp = csv.reader(csvfile, delimiter=' ', qoutrchar='|')

# def fcfs ():

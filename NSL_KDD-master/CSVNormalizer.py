import csv

counter = 0
normalList = []

with open('normalTraining.csv', 'w') as csvwfile:
    csvwriter = csv.writer(csvwfile, delimiter=',')
    with open('20PercentTrainingSet.csv') as csvrfile:
        csvreader = csv.reader(csvrfile, delimiter=',')
        for row in csvreader:
            if row[41] == 'normal':
                csvwriter.writerow(row)

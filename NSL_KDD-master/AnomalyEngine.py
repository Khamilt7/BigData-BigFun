import math
import csv
import random
import statistics


def row_distance(test, normal) :
    sum_distance = 0
    for i in range(0, len(normal)-2):
        if i>=1 and i<=3 : # nominal attributes
            continue
        sum_distance += (float(test[i]) - float(normal[i]))**2
    return math.sqrt(sum_distance)


def get_neareast(test):
    with open('normalTraining.csv') as csvrfile:
        min_dist = 10000
        csvreader = csv.reader(csvrfile, delimiter=',')
        for row in csvreader:
            i = row_distance(test, row)
            if i > min_dist:
                min_dist = i
    return min_dist


def make_dataset():
    row_list = list()
    i = 0
    with open('KDDTest+.csv') as csvrfile:
        with open('data.csv', 'w') as datafile:
            csvreader = csv.reader(csvrfile, delimiter=',')
            csvwriter = csv.writer(datafile, delimiter=',')
            for row in csvreader:
                dist = get_neareast(row)
                row_list.append((row[41], dist))
                csvwriter.writerow([row[41], dist])
                print(i)
                i += 1


def anomaly_detect(dataset, threshold_list):
    with open('results.txt', 'w') as results:
        for threshold in threshold_list:
            fp, tp, fn, tn = 0,0,0,0
            for entry in dataset:
                if float(entry[1]) > threshold:
                    if entry[0] == 'normal':
                        fp += 1
                    else:
                        tp += 1
                else:
                    if entry[0] == 'normal':
                        tn += 1
                    else:
                        fn += 1
            total_normal = float(tn+fp)
            total_bad = float(fn+tp)
            result = "TPR is %f FPR is %f for k = %f \n" % (tp/total_bad, fp/total_normal, threshold)
            print(result)
            results.write(result)


def standardize(avg, sigma, value):
    return (value - avg) / sigma


num = 0
total = 0.0
stuff = list()
values = list()
with open('data.csv') as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        stuff.append(row)
        num +=1
        total += float(row[1])
        values.append((float(row[1])))

mean = total/num
st_dev = statistics.stdev(values)
for row in stuff:
    row[1] = standardize(mean, st_dev, float(row[1]))

thresholds = list()
for i in range(0, 9):
    thresholds.append(random.uniform(.004, .007))
thresholds.append(-1)
anomaly_detect(stuff, thresholds)

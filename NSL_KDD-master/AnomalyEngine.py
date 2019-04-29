import math
import csv
import random
import statistics


# calculates the Euclidian distance between
def row_distance(test, normal):
    sum_distance = 0
    for i in range(0, len(normal)-2):
        if i in range(1, 4):  # skip nominal attributes
            continue
        sum_distance += (float(test[i]) - float(normal[i]))**2
    return math.sqrt(sum_distance)


# iterates through the training set to find the minimum distance to the test point
def get_nearest(test):
    with open('normalTraining.csv') as csvrfile:
        min_dist = 10000
        csvreader = csv.reader(csvrfile, delimiter=',')
        for row in csvreader:
            i = row_distance(test, row)
            if i > min_dist:
                min_dist = i
    return min_dist


# helper function that creates a file with the attack type and corresponding weight
def make_dataset():
    row_list = list()
    i = 0
    with open('KDDTest+.csv') as csvrfile:
        with open('data.csv', 'w') as datafile:
            csvreader = csv.reader(csvrfile, delimiter=',')
            csvwriter = csv.writer(datafile, delimiter=',')
            for row in csvreader:
                dist = get_nearest(row)
                row_list.append((row[41], dist))
                csvwriter.writerow([row[41], dist])
                print(i)
                i += 1


# takes a list of thresholds and does anomaly detection on the distances based on each
# finds and prints the statistics for each threshold value
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


# transforms the data to a set with mean of 0 and sd of 1
def standardize(avg, sigma, value):
    return (value - avg) / sigma


def main():
    num = 0
    total = 0.0
    stuff = list()
    values = list()
    with open('data.csv') as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            stuff.append(row)
            num += 1
            total += float(row[1])
            values.append((float(row[1])))

    # find mean and sd to normalize
    mean = total / num
    st_dev = statistics.stdev(values)
    for row in stuff:
        row[1] = standardize(mean, st_dev, float(row[1]))

    thresholds = list()
    # generate random thresholds in the effective range for the IDS
    for i in range(0, 9):
        thresholds.append(random.uniform(.004, .007))
    thresholds.append(-1)
    anomaly_detect(stuff, thresholds)


if __name__ == '__main__':
    main()
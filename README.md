# BigData-BigFun
EN.650.654 Computer Intrusion Detection
Homework 3
Jay Chow, Kevin Hamilton, James Ballard
23rd April 2019

Instructions (60pts)
This assignment will conduct anomaly detection and  misuse detection using the NSL-KDD dataset that is available at GitHub (https://github.com/defcom17/NSL_KDD). Additional information of this dataset can be found at the website of Lincoln Laboratory (https://www.ll.mit.edu/ideval/data/). Posted with this assignment, a paper analyzing this data set should be helpful to understanding this dataset.

Note that the training data should come from “ 20 Percent Training Set.csv” and the testing data from
“ KDDTest+.csv” that are subsets of the original KDD data. There are different types of attacks in four
categories (higher level). The analysis may use the binary normal/intrusive classes as well as multiple
classes according to specific requirements below.

We have studied Instance Based-Learning (IBL). Now it is time for us to put it in use. Please specifically
complete the tasks described below for anomaly detection and misuse detection respectively. You can use
any data analysis tools that are useful, e.g., WEKA.


Tasks:
 (A) Anomaly Detection
Extract normal instances from the training dataset to be used for detection (testing);
For every instance in the testing dataset, find the nearest “neighbor” instance in the normal profile and calculate the corresponding distance to it;
Vary the control threshold value to appropriately cover the value range of this distance (using at least 10 different values), classify each new instance as normal or attack accordingly;
Calculate the False Positive Rate (FPR) and True Positive Rate (TPR) pair for each control threshold value used and plot the Receiver Operating Characteristic (ROC) curve;
Please calculate the Area Under the Curve (AUC) for this ROC.

 (B) Misuse Detection
Use the whole training dataset for detection;
Select different  k’s (using at least the first five odd numbers) used in the  k-NN classification to classify every instance in the testing dataset as normal or intrusive accordingly;
Calculate the FPR and TPR pair for each  k used and plot the ROC curve;
Please calculate the AUC for this ROC;
Lastly, use the closest neighbor method, i.e.,  k=1, to find the attack category (in the four attack categories) of each instance that is classified as intrusive, and show the resulting confusion matrix for these four attack categories plus the normal class.

Submission Requirements:
Please list all the team members in submission. Each submission should have the following:
A PDF file including the adequate descriptions of all the steps taken, code and tools used, and settings (e.g., distance used, threshold values chosen), as well as all the results with explanation as specified in the above, in completing these tasks;
A text file containing all the code, if any, and tools used (name, source, commands and parameters for each tool) used in analysis as applicable.

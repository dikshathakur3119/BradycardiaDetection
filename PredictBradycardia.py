import json
import os, sys
from operator import itemgetter
import math
import csv

time_window = 1.2
fs = 250
sample_window = int(fs*time_window)

files = ["11-10-30","11-44-37","13-12-05","13-45-41"]


def predict_bradycardia():
	for file_name in files:
		print("\n\n"+"*"*150)
		variance = []
		hr = []
		avg_hr = []
		hrclass = []
		avghrclass = []
		with open(file_name+"_heartrate.csv","r") as f:
			reader = csv.DictReader(f)
			for n, row in enumerate(reader):
				variance.append(int(float(row["AvgVariance"])))
				hr.append(int(float(row["HeartRate"])))
				avg_hr.append(int(float(row["AverageHr"])))
				hrclass.append(int(float(row["HRClass"])))
				avghrclass.append(int(float(row["AVHRClass"])))

		variance_threshold = []
		for i in range(len(avghrclass)):
			if avghrclass[i] == 2 or (avghrclass[i] == 1 and i+1<len(avghrclass) and avghrclass[i+1] == 1):
				if i-10 >= 0:
					variance_threshold.append(int(sum(variance[i-10:i+1])/11))
				else:
					variance_threshold.append(int(sum(variance[0:i+1])/(i+1)))
		variance_threshold = sorted(variance_threshold)

		#print(variance_threshold)
		minv = min(variance_threshold)
		maxv = max(variance_threshold)
		avgv = sum(variance_threshold)/len(variance_threshold)
		print(maxv, minv, avgv)
		print(max(variance), min(variance), sum(variance)/len(variance))
		rnge = [int(avgv-2),int(avgv+3)]

		predicted_class = [0]
		for i in range(len(variance)-1):
			if variance[i] >= rnge[0] and variance[i] <= rnge[1]:
				predicted_class.append(1)
				if predicted_class[i] == 0:
					predicted_class[i] = 2
			else:
				predicted_class.append(0)

		tp = 0
		fp = 0
		tn = 0
		fn = 0
		for i in range(len(predicted_class)):
			if predicted_class[i] == 0 and avghrclass[i] == 0:
				tn += 1
			elif predicted_class[i] >= 1 and avghrclass[i] == 1:
				tp += 1
			elif predicted_class[i] == 1 and avghrclass[i] == 0:
				fp += 1
			elif predicted_class[i] == 0 and avghrclass[i] == 1:
				fn += 1

		print("\nResult of thresholding algorithm\nTrue Positive: {} \nFalse Positive: {} \nTrue Negative: {} \nFalse Negative: {} \n".format(tp,fp,tn,fn))
		precision = (tp*100)/(tp+fp)  
		recall = (tp*100)/(tp+fn)
		print("\nPrecision: {}% \nRecall: {}% ".format(precision, recall))
		print("*"*150)


if __name__ == "__main__":
	predict_bradycardia()
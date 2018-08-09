from __future__ import division
import csv
import math
import numpy as np
from sklearn.cluster import KMeans
import random

files = ["11-10-30","11-44-37","13-12-05","13-45-41"]

def kmeans():
	for file_name in files:
		variance = []
		hr = []
		avg_hr = []
		hrclass = []
		avghrclass = []
		cluster_label = []

		with open(file_name+"_heartrate.csv","r") as f:
			reader = csv.DictReader(f)
			for n,row in enumerate(reader):
				variance.append(int(float(row["AvgVariance"])))
				hr.append(int(float(row["HeartRate"])))
				avg_hr.append(int(float(row["AverageHr"])))
				hrclass.append(int(float(row["HRClass"])))
				avghrclass.append(int(float(row["AVHRClass"])))
		
			for itern in range(0,5):
				if itern == 0:
					centroid1, centroid2, centroid3 = random.sample(range(1,max(variance)),3)
					for i in range(0,len(variance)-1):
						distance1 = abs(variance[i] - centroid1) 
						distance2 = abs(variance[i] - centroid2)
						distance3 = abs(variance[i] - centroid3)

						if min(distance1, distance2, distance3) == distance1:
							cluster_label.append(0) 
						elif min(distance1, distance2, distance3) == distance2:
							cluster_label.append(1)
						elif min(distance1, distance2, distance3) == distance3:
							cluster_label.append(2)
				else:
					cluster1 = []
					cluster2 = []
					cluster3 = []
					
					for i in range(0,len(variance)-1):
						if cluster_label[i] == 0:
							cluster1.append(variance[i])
						elif cluster_label[i] == 1:
							cluster2.append(variance[i])
						elif cluster_label[i] == 2:
							cluster3.append(variance[i])
							
					centroid1 = sum(cluster1)/len(cluster1)
					centroid2 = sum(cluster2)/len(cluster2)
					centroid3 = sum(cluster3)/len(cluster3)


					for i in range(0,len(variance)-1):
				
						distance1 = abs(variance[i] - centroid1) 
						distance2 = abs(variance[i] - centroid2)
						distance3 = abs(variance[i] - centroid3)

						if min(distance1, distance2, distance3) == distance1:
							cluster_label[i] = 0
						elif min(distance1, distance2, distance3) == distance2:
							cluster_label[i] = 1
						elif min(distance1, distance2, distance3) == distance3:
							cluster_label[i] = 2
				

		with open(file_name+'_kmeans.csv','w+') as f:
			writer = csv.writer(f)
			writer.writerow(("HeartRate","HRClass","AverageHr","AvgVariance","AVHRClass","ClusterLabel"))
			writer.writerows(zip(hr, hrclass, avg_hr, variance, avghrclass, cluster_label))

		tp = 0
		fp = 0
		tn = 0
		fn = 0
		for i in range(len(cluster_label)):
			if cluster_label[i] == 0 and avghrclass[i] == 0:
				tn += 1
			elif cluster_label[i] >= 1 and avghrclass[i] == 1:
				tp += 1
			elif cluster_label[i] == 1 and avghrclass[i] == 0:
				fp += 1
			elif cluster_label[i] == 0 and avghrclass[i] == 1:
				fn += 1

		print("\nK-means algorithm\nTrue positives: {}\nFalse positives: {}\nTrue negatives: {}\nFalse negatives: {}".format(tp,fp,tn,fn))
		precision = (tp*100)/(tp+fp)  
		recall = (tp*100)/(tp+fn)
		accuracy = (tp+tn)/(tp+tn+fp+fn) 
		accuracy = accuracy*100
		print("\nPrecision: {}% \nRecall: {}% ".format(precision, recall))
		print("\nAccuracy: {}%".format(accuracy))
		print(".................................................................")

if __name__ == "__main__":
	kmeans()

					


		
		



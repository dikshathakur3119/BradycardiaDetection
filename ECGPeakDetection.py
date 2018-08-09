import json
import os, sys
from operator import itemgetter
import math

time_window = 1.2
fs = 250
sample_window = int(fs*time_window)

files = ["11-10-30","11-44-37","13-12-05","13-45-41"]

def find_peaks():
	for file_name in files:
		with open(file_name+".dat","r") as f:
			lines = f.readlines()

		new_lines = [float(x) for x in lines]
		del lines

		w_start = 0
		w_stop = sample_window
		skip_samples = int(math.ceil(fs/(210/60)))  #assuming max heartrate of 210

		inverse_peaks = []
		while(w_stop < len(new_lines)):
			index, peak = min(enumerate(new_lines[w_start:w_stop]), key=itemgetter(1))
			inverse_peaks.append(w_start+index)
			w_start += index + skip_samples 
			w_stop = w_start+sample_window

		peaks = [str(x)+"\n" for x in inverse_peaks]
		with open(file_name+'_rpeaks.dat','w') as f:
			f.writelines(peaks)


def detect_bradycardia():
	for file_name in files:
		with open(file_name+'_rpeaks.dat','r') as f:
			lines = f.readlines()

		lines = [int(float(x)) for x in lines]
		multiplier = 60*fs
		heartrate = [int(multiplier/(lines[i+1]-lines[i])) for i in range(len(lines)-1)]
		# print(len(heartrate))
		# print(len(lines))
		# print(heartrate[:50])
		brc_count = 0
		flag = False
		max_bc = 0
		cur_bc = 0
		for l in heartrate:
			if l<60:
				brc_count += 1
				if not flag:
					cur_bc = 1
					flag = True
				else:
					cur_bc += 1
				max_bc = max(max_bc, cur_bc)
			else:
				flag = False

		count = len(lines)
		print("\nRecorded {} samples in a total of 8 hours with sampling frequency of {}...".format(fs*3600*8, fs))
		print("Total Peaks: {}\nTotal Bradycardic peaks: {}\nMax Continuous Bradycardic peaks streak: {}".format(count, brc_count, max_bc))
		print("Average Heartrate: {}".format(sum(heartrate)/len(heartrate)))
		print("\nDetecting Bradycardia by averaging heartrate over 60sec...If average heartrate<60 in any 2-minute period, Bradycardia present!!..")
		minute_samples = 2*60*fs
		avg_hr = []
		for i in range(count):
			j = i+1
			while j < count and lines[j]-lines[i] < minute_samples:
				j+=1
			if j<count:
				hr = sum(heartrate[i:j-1])/len(heartrate[i:j-1])
				avg_hr.append(hr)
		if min(avg_hr) < 60.0:
			print("\nPatient is affected by Bradycardia!!!")
		else:
			print("\nPatient does not have Bradycardia!!!")
		print("Minimum Average 2-min period heartrate:{}\nMaximum Average 2-min period heartrate:{}\n ".format(min(avg_hr), max(avg_hr)))


if __name__ == "__main__":
	find_peaks()
	detect_bradycardia()
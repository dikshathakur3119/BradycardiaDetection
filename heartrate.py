import csv, math
from matplotlib import pyplot as plt
files = ["11-10-30","11-44-37","13-12-05","13-45-41"]

ix = 1
for file_name in files:
	
	with open(file_name+'_rpeaks.dat','r') as f:
			lines = f.readlines()

	lines = [int(float(x)) for x in lines]
	fs = 250
	multiplier = 60*fs
	condition = []
	heartrate = [int(multiplier/(lines[i+1]-lines[i])) for i in range(len(lines)-1)]
	for i in range(0,len(heartrate)):
		if heartrate[i] < 60:
			condition.append("1")
		else:
			condition.append("0")

	count = len(lines)
	avg_hr = []
	avg_var = []
	minute_samples = 1*10*fs
	for i in range (count):
		j=i+1
		while j < count and lines[j]-lines[i] < minute_samples:
			j+=1
		if j<count:
			hr = sum(heartrate[i:j-1])/len(heartrate[i:j-1])
			avg_hr.append(hr)
			var =  math.sqrt((sum([heartrate[i]**2 for i in range(i,j-1)])/len(heartrate[i:j-1]) - math.pow(hr,2)))
			avg_var.append(var)

	avg_condition = []
	for i in range(0,len(avg_hr)):
		if avg_hr[i] < 60.0:
			avg_condition.append("1")
		else:
			avg_condition.append("0")

	for i in range(len(avg_condition)):
		if avg_condition[i]	== "1" and i-1>=0 and avg_condition[i-1] == "0":
			avg_condition[i-1] = "2"

	total_time = 60*60*8
	total_size = len(avg_var)
	x_data = [int(((i+1)*total_time)/total_size) for i in range(total_size)]
	plt.plot(x_data,avg_var)
	plt.title("HeartRate Variance vs Time Graph {}".format(ix))    
	plt.xlabel('time')
	plt.ylabel('Variance')
	plt.grid(True)
	plt.savefig(file_name+".png")
	plt.show()
	ix += 1


	with open(file_name+'_heartrate.csv','w+') as f:
		writer = csv.writer(f)
		writer.writerow(("HeartRate","HRClass","AverageHr","AvgVariance","AVHRClass"))
		writer.writerows(zip(heartrate, condition, avg_hr, avg_var, avg_condition))
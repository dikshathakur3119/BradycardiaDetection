Bradycardia Detection

A few of the currently existing attempts to predict Bradycardia, developed by various organizations and researchers has a little probability for failure. Also, during the course of this project, it has been observed that certain heart rate determination algorithms and Bradycardia detection algorithms have failed to detect the heart rate accurately and have shown poor performance. The main goal of this project was to collect the ECG data from four patients (group members), clean and process it for usage. From this pre-processed data, in order to detect the heart rate, the peaks in the ECG signal had to be detected. After detecting the heart rate from the peaks, a Bradycardia detection algorithms has been implemented after it has occurred. “If the computed heart rate falls below 60 beats per minute, then it is detected as Bradycardia.” Then, an Android application was developed to show the execution of this algorithm and measure the performance of it in terms of false positives and false negatives. Next considering the variance of heart rate as a precursor for Bradycardia, a prediction algorithm has been developed and this has been repeated by using a deep belief network as well. The performance for a k-fold cross validation has been reported.

Contributors:

Satya Srinija Kanteti, skantet1@asu.edu
Suraj Shah, ssshah22@asu.edu
Sita Rama Nikitha Pabolu, spabolu1@asu.edu
Akhila Muthyala, amuthyal@asu.edu
        
Project Demo Video: 

https://youtu.be/Pw1cPy78NwA

Getting Started

Find all the ECG data here: https://drive.google.com/file/d/1KXCdsJbV-aXJ82l5wskiu0N0IJPGWONL/view?usp=sharing

All project files: https://drive.google.com/open?id=12o9OjBAAgeV9SeiNxP2ml_Dt0nG-WXhE

Note: Please note that to run some of these functions (whose output is already specified in the project files) you might need to copy all input.dat files, heartrate.csv files and the python files in the same folder and then execute the code, otherwise it may not run.

Step 1: Run clean_data_filters.m on all the four ECG files to obtain the cleaned data (.dat files in folder 2.1 and 2.2)

Step 2: Run ECGPeakDetection.py to obtain the R-peaks of the cleaned signal (_rpeaks.dat files in folder 2.3)

Step 3: Run heartrate.py to obtain the heart rate files (_heartrate.csv files in folder 2.4 and 2.5, graphs included)

Step 4: Run BradycardiaDetection.py on the heartrate.csv files (in folder 3.1,3.2 and 3.3)

Step 5: Apply the same algorithm in Android (folder 3.4 and 3.5)

Step 6: Run PredictBradycardia.py on the heartrate files (in folder 4.1,4.2 and 4.3)

Step 7: Run Kmeans.py on the heartrate.csv files (folder 4.4 and 4.5)

Prerequisites:
Matlab
Python 3.5  
Android Studio

Note: All input and output files generated have been included in the project folder

Please let us know if you have any questions. Thank you!

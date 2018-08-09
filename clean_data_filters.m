% p = dlmread('ECGData\16272\ekg_raw_16272.dat');
% p = dlmread('E:\Spring 2018\Mobile Computing\Project\ECG Sample data and algo\ekg_raw_16272.dat');
% p = dlmread('E:\Spring 2018\Mobile Computing\Project\ECG Sample data and algo\ekg_raw_16273.dat');
% p = dlmread('E:\Spring 2018\Mobile Computing\Project\ECG Sample data and algo\ekg_raw_16420.dat');
% p = dlmread('E:\Spring 2018\Mobile Computing\Project\ECG Sample data and algo\ekg_raw_16483.dat');

% file_name = "11-10-30";
% file_name = "11-44-37";
% file_name = "13-12-05";
file_name = "13-45-41";
edfread('E:\Spring 2018\Mobile Computing\Project\ECG collected data\'+file_name+'.EDF'); 
[data, header] = ReadEDF('E:\Spring 2018\Mobile Computing\Project\ECG collected data\'+file_name+'.EDF');
data = data{1}(1:7200000);
X = [1:1:7200000];
X = X';
EKG = data;
Fs = 250;                                               % Sampling Frequency (Hz)
Fn = Fs/2;                                              % Nyquist Frequency
Ts = 1/Fs;
T = [0:size(data,1)-1]*Ts;
Wp = [1  100]/Fn;                                       % Passband (Normalised)
Ws = [0.5  110]/Fn;                                     % Stopband (Normalised)
Rp = 10;                                                % Passband Ripple (dB)
Rs = 30;                                                % Stopband Ripple (dB)
[n,Ws] = cheb2ord(Wp, Ws, Rp, Rs);                      % Chebyshev Type II Order
[b,a] = cheby2(n, Rs, Ws);                              % Transfer Function Coefficients
[sos,g] = tf2sos(b,a);     
EKG_F = filtfilt(sos,g,data);

save(file_name+'.dat','EKG_F','-ascii');

%[R, Rt] = findpeaks(EKGf, X, 'MinPeakHeight',140);
%[R, Rt] = findpeaks(EKGf, Fs);
%size(R)
%[RpeakIndex, values] = RPeakDetection(EKGf);
%hr = 60*250./(Rt(2:end)-Rt(1:end-1));


% [RpeakIndex, values] = RPeakDetection(EKG_F);
% size(RpeakIndex)

% fs = 250; gr = 1;
% [qrs_amp_raw,qrs_i_raw,delay]=pan_tompkin(EKG_F,fs,gr)

%plot(p(6000:7000,2))
% [RpeakIndex, values] = RPeakDetection(p(6000:7000,2));

% [RpeakIndex, values] = RPeakDetection(data);
% hold on;stem(RpeakIndex+22, p(6000+RpeakIndex+22,2),'r')
% 
% hr = 60*250./(RpeakIndex(2:end)-RpeakIndex(1:end-1))


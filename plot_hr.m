p = dlmread('11-10-30_rpeaks.dat');
hr = 60*250./(p(2:end)-p(1:end-1));
ylabel('Heart Rate');
xlabel('Time');
title("Heart rate of Patient 1");
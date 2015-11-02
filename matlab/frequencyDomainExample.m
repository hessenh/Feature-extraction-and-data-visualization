close all

x=[0:0.1:10]
time1 = sin(x/2)
time2 = 1.5*sin(3*x-2)
time3 = 0.5*sin(5*x-3)

sumOfWaves = time1 + time2 + time3

freq1 = fft(time1)
freq2 = fft(time2)
freq3 = fft(time3)

hold on 
plot(time1(1:100),'k')
plot(time2(1:100),'k--')
plot(time3(1:100),'k:')

figure
hold on
plot(abs(freq1(1:50)),'k')
plot(abs(freq2(1:50)),'k--')
plot(abs(freq3(1:50)),'k:')

figure
plot(sumOfWaves(1:100),'k')
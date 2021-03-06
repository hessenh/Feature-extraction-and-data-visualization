close all

% Generate sample data.
vector = [-0.31641,-0.30859,-0.30469,-0.30078,-0.28906,-0.28125,-0.28125,-0.28516,-0.28906,-0.28906,-0.28516,-0.30078,-0.30078,-0.30469,-0.30859,-0.31641,-0.32031,-0.32422,-0.33203,-0.32812,-0.32812,-0.32812,-0.32812,-0.32422,-0.32422,-0.32422,-0.32031,-0.31641,-0.3125,-0.3125,-0.31641,-0.3125,-0.30469,-0.30859,-0.30859,-0.30469,-0.30859,-0.30469,-0.30078,-0.29688,-0.30469,-0.30469,-0.3125,-0.31641,-0.32031,-0.32031,-0.32422,-0.32812,-0.32422,-0.32812,-0.32031,-0.32422,-0.32031,-0.32031,-0.31641,-0.3125,-0.30859,-0.30859,-0.30078,-0.29688,-0.29688,-0.29688,-0.30469,-0.30078,-0.3125,-0.32422,-0.32422,-0.33203,-0.32812,-0.32422,-0.31641,-0.30469,-0.30078,-0.28516,-0.27734,-0.26562,-0.26562,-0.26953,-0.27344,-0.27734,-0.29688,-0.3125,-0.31641,-0.32422,-0.32031,-0.31641,-0.30859,-0.3125,-0.30469,-0.30859,-0.30859,-0.31641,-0.32422,-0.32812,-0.33203,-0.33984,-0.33594,-0.33594,-0.32812,-0.32031]


% plot(vector, 'r-', 'linewidth', 3);
% set(gcf, 'Position', get(0,'Screensize')); % Maximize figure.
% 
% % Construct blurring window.
% windowWidth = int16(10);
% halfWidth = windowWidth / 2;
% gaussFilter = gausswin(10);
% gaussFilter = gaussFilter / sum(gaussFilter); % Normalize.
% 
% % Do the blur.
% smoothedVector = conv(vector, gaussFilter)
% 
% % plot it.
% hold on;
% plot(smoothedVector(halfWidth:end-halfWidth), 'b-', 'linewidth', 3);
% 
% 
% figure;
% [b,a] = ellip(3,0.01,100,0.05);
% freqz(b,a);
% dataIn = randn(1000,1);
% dataOut = filter(b,a,vector);
% plot(dataOut, 'b-', 'linewidth', 3);
filterSize = 10
alpha = 5


filtere = fspecial('gaussian',[filterSize 1], alpha); % gaussian kernel where s= size of contour
smooth = conv(vector, filtere); % convolution
smooth=smooth((filterSize+1)/2:end-(filterSize-1)/2)

plot(smooth)
hold on
plot(vector)
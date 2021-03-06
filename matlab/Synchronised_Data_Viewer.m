
%% Variables
Axes = 3;
A = 1:3; % Accelerometer axes
G = 4:5; % Gyroscope axes

DS = {};
%%
Main_Dir = cd;

Dir_Data_Exported = cd; % 'C:\Users\alankb\Documents\ADAPT\ADAPT DATA EXPORTED';

%% Reading and plotting Sensor data.


reply = input('Do you want to import the data files for viewing? Y/N [Y]:','s');
if isempty(reply)
    reply = 'N';
end

switch reply
    case {'y','Y'}
        %%
        ImportS = 1;
        if(ImportS == 1)
            cd(Dir_Data_Exported);
            
            Folders = dir;
            Folders.name
            
            directoryname = uigetdir(Dir_Data_Exported, 'Pick a Directory');
        
            cd(directoryname);
            Files = dir('2*.mat');
            SensorsN = length(Files);
            
            clear S;
            for i = 1:SensorsN
                S(i)=load(Files(i).name);
                Files(i).name
                disp(['Importing sensor: ' S(i).SensorExtracted.SensorType '  File name: ' Files(i).name ]);
            end
            
            
            
            cd(Main_Dir);
        end
        
        
end

 if(exist('S')==0)
            error('Data has not been loaded yet.');
 end     
   
for j=1:length(S) % 7:7 %
    
    if( strcmp( S(j).SensorExtracted.SensorType , 'SenseWear BodyMedia' ) )
        % Do nothing as the SenseWear armband didn't record during the
    else
        
        
        
        
        
        if( strcmp( S(j).SensorExtracted.SensorType , 'Shimmer3' ) )
            Accel = S(j).SensorExtracted.DataSignalsOnly.Sensor1(:,7:9);    % For the Shimmer sensors
        elseif( strcmp( S(j).SensorExtracted.SensorType , 'Video' ) )
            TempA = S(j).SensorExtracted.DataSignalsOnly;
            TempAccel = TempA; % + 1;
            %Accel = TempAccel
            Accel = [TempAccel TempAccel TempAccel];
        else
            Accel = S(j).SensorExtracted.DataSignalsOnly(:,A);
        end
        
        %%
        
        % Chect to see if the accelerometer data is in G's or m/s^2
        RSSa = mean(sqrt(sum(Accel(:,1:3).*Accel(:,1:3),2)));
        if(RSSa>2) % either the mean is ~9.81 or ~1
            Accel=Accel/RSSa; % or 9.81m/s
            disp('Inni gravity greien');
            S(j).SensorExtracted.SensorType
        else
            Accel=Accel;
        end
        %%
        
         Fs = floor(S(j).SensorExtracted.fs);
%         Fs = S(j).SensorExtracted.fs;

        
        
%         figure; plot(Accel);
%         title(S(j).SensorExtracted.SensorType);
        
%% Try 

%   SensorAddr =find(strcmp({Handshakes.SensorType},SensorNameHandshake)==1);
% % for j = 1:length(SensorAddr)    
%     [SyncStartSample , fs , SensorLocationName , SideOfBodyName ] = FN_find_SensorLocation_SideOfBody_SyncStart_for_index(Handshakes , SensorAddr  );
  
SyncStartSample = S(j).SensorExtracted.Handshakes.OffsetSamples;
    
 DataSignalsOnly_CUT=FN_Cut_Signal_For_Sync(Accel,SyncStartSample); 
 TimeStampCut=FN_Cut_Signal_For_Sync(S(j).SensorExtracted.TimeStamp,SyncStartSample); 
  
 TimeStampMS = datenum(TimeStampCut);
 
 if(length(DS)<2)
 DS{length(DS)+1}= DataSignalsOnly_CUT;
 end
 
  %%     
     
 ax(j) = subplot(length(S),1,j);
 
 Time = (0:length(DataSignalsOnly_CUT)-1)'/Fs;
 
 
 
 
 if( strcmp(S(j).SensorExtracted.SensorName , 'GoPro' ) )
     Activities = S(j).SensorExtracted.AllData.FramesResampled.Activity( SyncStartSample : end , :  );
%      ActivitiesTimeAll = S(j).SensorExtracted.AllData.FramesResampled.Time( SyncStartSample : end , :  );
%      ActivitiesTime = ActivitiesTimeAll - ActivitiesTimeAll(1);
%      subplot(ax(j));
%      plot( ActivitiesTime , Activities  ,...
%           Time , DataSignalsOnly_CUT);
% %          TimeStampConstruct , DataSignalsOnly_CUT);
% 
%      xlabel([S(j).SensorExtracted.SensorName ' ' S(j).SensorExtracted.SensorLocation]);
%      
%      YLabelTicks = S(j).SensorExtracted.AllData.YLabelTicks;
%      Ylabels = S(j).SensorExtracted.AllData.Labels;
%      
%      
%      set(gca,'YTick',YLabelTicks);
%      set(gca,'YTickLabel',Ylabels);
%      
 else
     
%      TimeStampConstructFULL=FN_Cut_Signal_For_Sync(S(j).SensorExtracted.TimeConstructed,SyncStartSample);
%      TimeStampConstruct = TimeStampConstructFULL - TimeStampConstructFULL(1);
%      
%      subplot(ax(j)),plot( TimeStampConstruct , DataSignalsOnly_CUT );
%      xlabel([S(j).SensorExtracted.SensorName ' ' S(j).SensorExtracted.SensorLocation]);

     DataSignalsOnly_CUT(1)
     % dateFormat = 13;
     % datetick('x',dateFormat);
     
 end
  
% 
%         %
%         
%         Ix_mode = Ix_mode_RSS;
%         
%         figure;
%         % plot((1:length(Accel))/Fs,Accel, 'b' , ( (S_search+Ix_mode+( 0:(length(TemplateRS)-1) )) )/Fs , TemplateRS , 'r--' );
%         plot((1:length(Accel))/Fs,Accel, 'b' , ( (S_search+Ix_mode+( 0:(length(y_RSS)-1) )) )/Fs , y_RSS-1 , 'r--' );%Axisi));
%         axis([(S_search+Ix_mode-length(y_RSS))/Fs (S_search+Ix_mode+2*length(y_RSS))/Fs -4 4]);
%         % plot((1:length(Accel))/Fs,Accel, 'b' , ( (S_search+Ix_mode+( 0:(length(Template_RSS)-1) )) /Fs) , Template_RSS , 'r--' );
%         % axis([(S_search+Ix_mode-length(Template_RSS))/Fs (S_search+Ix_mode+2*length(Template_RSS))/Fs -4 4]);
%         % pause;
%         
%                
        
%         [Ya,Ia] = max(HS_Results_RSS(:,1));
%         
%         Handshakes(j).Results=HS_Results_RSS;
%         Handshakes(j).MainOffset = S_search+Ix_mode;
%         Handshakes(j).Fs = S(j).SensorExtracted.fs; %         Handshakes(j).Fs = Fs; 
%         Handshakes(j).Ix_mode = Ix_mode;
%         Handshakes(j).S_search = S_search;
%         OffsetSamples = S_search+Ix_mode;
%         Handshakes(j).OffsetSamples = OffsetSamples;
%         Handshakes(j).OffsetSeconds = OffsetSamples/Fs;
%         Handshakes(j).Index = HS_Results_RSS(Ia,2);% Handshakes(j).Results(Ia,2); % Index of the maximum
%         Handshakes(j).SensorType = S(j).SensorExtracted.SensorType;
%         Handshakes(j).SensorName = S(j).SensorExtracted.SensorName;
%         Handshakes(j).SensorLocation = S(j).SensorExtracted.SensorLocation;
%         Handshakes(j).SideOfBody = S(j).SensorExtracted.SideOfBody;      
%         Handshakes(j).filename = S(j).SensorExtracted.filename;
%         Handshakes(j).SensorIDno = S(j).SensorExtracted.SensorIDno;
%         
% 
% %% Include the Handshake variables in the S structure also
%         S(j).SensorExtracted.Handshakes.Results=HS_Results_RSS;
%         S(j).SensorExtracted.Handshakes.MainOffset = S_search+Ix_mode;
%         S(j).SensorExtracted.Handshakes.Fs = Fs;
%         S(j).SensorExtracted.Handshakes.Ix_mode = Ix_mode;
%         S(j).SensorExtracted.Handshakes.S_search = S_search;
%         OffsetSamples = S_search+Ix_mode;
%         S(j).SensorExtracted.Handshakes.OffsetSamples = OffsetSamples;
%         S(j).SensorExtracted.Handshakes.OffsetSeconds = OffsetSamples/Fs;
%         S(j).SensorExtracted.Handshakes.Index = HS_Results_RSS(Ia,2);% Handshakes(j).Results(Ia,2); % Index of the maximum
%         
        
        
       
    end
    
   
end
% length(Activities)
% ActivitiesResampled = [];
% 
% for i=1:length(Activities)
%     ActivitiesResampled(length(ActivitiesResampled)+1) = Activities(i);
%     ActivitiesResampled(length(ActivitiesResampled)+1) = Activities(i);
%     ActivitiesResampled(length(ActivitiesResampled)+1) = Activities(i);
%     ActivitiesResampled(length(ActivitiesResampled)+1) = Activities(i);
% end
% 
% DS{length(DS)+1} = transpose(ActivitiesResampled);
% linkaxes(ax,'x');
DS{length(DS)+1} = Activities;
%  otherwise
%      
%         if(exist('S')==0)
%             error('Data has not been loaded yet.');
%         end        
% end

%WRITE DS to CSV File and make directories for subject


% 
    nameArray = strsplit(Files(1).name,'_');
     subjectName = char(nameArray(1));
     path = strcat('../data/',subjectName,'/RAW_SIGNALS/');
     mkdir(path);
% %    
% %   
% % 
% %     
   for i = 1:3   
      filename = strcat(Files(i).name(1:length(Files(i).name)-4),'.csv')
      csvwrite(strcat(path,filename), DS{i});
   end
    
% 
%  
     dirPath = strcat('../data/',subjectName,'/');
%     mkdir(dirPath,'DATA_WINDOW');
%     mkdir(dirPath,'WEKA');
%     mkdir(dirPath,'FEATURES');
     mkdir(dirPath,'RAW_SIGNALS_DC');
%     
    path = strcat('../data/',subjectName,'/RAW_SIGNALS_DC/');
%[b,a] = ellip(3,0.01,100,0.05);
%freqz(b,a);

filterSize = 99;
alpha = 7;


filtere = fspecial('gaussian',[filterSize 1], alpha); % gaussian kernel where s= size of contour




for i =1:3
   % Sensor signals
   if(i<3) 
        vector = DS{i};
        for j=1:3
            smooth = conv(vector(:,j), filtere); % convolution
            smooth=smooth((filterSize+1)/2:end-(filterSize-1)/2);
            vector(:,j) = smooth;
        end
        filename = strcat(Files(i).name(1:length(Files(i).name)-4),'_DC.csv');
        csvwrite(strcat(path,filename), vector);
   % Lables
   else 
        filename = strcat(Files(i).name(1:length(Files(i).name)-4),'.csv');
        csvwrite(strcat(path,filename), DS{i});
   end
   
end


% 
%     dirPath = strcat('../data/',subjectName,'/');
%     mkdir(dirPath,'DATA_WINDOW');
%     mkdir(dirPath,'WEKA');
%     mkdir(dirPath,'FEATURES');
%     mkdir(dirPath,'RAW_SIGNALS_SMOOTHED');
%     
%     path = strcat('../data/',subjectName,'/RAW_SIGNALS_SMOOTHED/');
% 
% 
% filterSize = 9;
% alpha = 5;
% 
% filtere = fspecial('gaussian',[filterSize 1], alpha); % gaussian kernel where s= size of contour
% 
% for i =1:3
%    % Sensor signals
%    if(i<3) 
%         vector = DS{i};
%         for j=1:3
%             smooth = conv(vector(:,j), filtere); % convolution
%             smooth=smooth((filterSize+1)/2:end-(filterSize-1)/2);
%             vector(:,j) = smooth;
%         end
%         filename = strcat(Files(i).name(1:length(Files(i).name)-4),'_smoothed.csv');
%         csvwrite(strcat(path,filename), vector);
%    % Lables
%    else 
%         filename = strcat(Files(i).name(1:length(Files(i).name)-4),'.csv');
%         csvwrite(strcat(path,filename), DS{i});
%    end
%    
% end
% 



 
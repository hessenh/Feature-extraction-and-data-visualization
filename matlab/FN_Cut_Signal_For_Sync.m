function DataOUT=FN_Cut_Signal_For_Sync(DataIN,SyncStartSample)
 
 LengthOfDataIn = length(DataIN);
 
 DataOUT = DataIN( SyncStartSample : LengthOfDataIn , : );
 
 end
To Guide you through our application please note the followings

STEP 1: Measurement 
STEP 2: Data preprocess
STEP 3: LSTM for orientation (DEAD END)
STEP 4: CNN for position


STPE 1: Measurement  
Every measurments located in the ./DATA/RAW folder.
At the begining the measurement were asyncronous which was a dead end. 
So we started using syncronous data. 
In the final version the algorithms uses only the measurements from the Measurement_04 folder.
In that folder a README can be found and everithing is explained in that file in connection with the measurement files.

STEP 2: Data preprocess
Preprocessing the data is made in the ./Code/Bazs/1_DataLoad_and_Preprocess.ipynb file.
This file contains every step to make our data useable. The code is commented and more visual information can be found in Visu_* files
In the filder a README file contains some additional information about the preprocess steps.

STEP 3: LSTM for orientation (DEAD END)
./Code/Bazs/1_DataLoad_and_Preprocess.ipynb file is an orientation prediction, but the experimental results are not so good.
We did not managed to debug the error from this code.

STEP 4: CNN for position
Using convolutional network to predict position is promising
./Code/CNN_Mark         : is an early stage of work (baseline solution)
./Code/CNN_Mark_absolute: In this version we tested the absolute position prediction (this is not the recommended way) 
./Code/CNN_Mark_relative: In this version the algorithm uses normalized sensor data to predict relative position changes
This sollution is very promising. The final plot shows a target and predicted rout.
Conclusion: Starting orientation in the MoCap system and the magneto coordinate system (absolute north) was not in align. 
This caused a missdirectional starting point, but the shape of the routs are similar. Improving the preprocess step(align the starting orientation)
and record more measurement it can be better and better. 
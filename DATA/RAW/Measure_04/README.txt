2018_ 11_ 27_9_39_00_ => StandStill measurement
2018_ 11_ 27_9_39_13_ => RollStill  measurement
2018_ 11_ 27_9_40_57_ => Test measurement
2018_ 11_ 27_9_45_58_ => LongRun measurement

=====================================================================================================
Idea behind the data parsing:
-----------------------------

To calibrate our sensor (normalize our data) two measurement were made befor the LongRun.

Magneto sensor is affected by hard iron and soft iron disturbances. These disturbances depend
on the actual position of the sensor. If someting change between two measurement, for example 
we take a new iron part on the robot, it affects the sensor output. So it is good to calibrate
the magneto sensor in a while. During RollStill measurement the robot takes 2 full circle left 
and right. 

StandStill measurement can help calibrate the accelero meter, and for example eliminate the 
effect of the gravity, which is a constant offset.

LongRun is the longest measurement. It can be used to teach neural networks

Test measurement is a short path, it can be used to test a neural network on an independent test set.

=====================================================================================================
Measurement pack infos:
-----------------------

Linear Speed   : 200
Rotation Speed : 60
Timing         : 9 ms (synronoused IMU and MoCap)

=====================================================================================================
Headers:
--------

IMU file:
0: time
1: acc0
2: acc1
3: acc2
4: gyro0
5: gyro1
6: gyro2
7: mag0
8: mag1
9: mag2

MoCap file:
0: time
1: x
2: y
3: z
4: tracked
5: orientation
6: Qx
7: Qy
8: Qz
9: Qw

Robot file:
0: time
1: mot0
2: mot1
3: mot2
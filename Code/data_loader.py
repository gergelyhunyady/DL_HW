"""This file contains code to load the raw data into python"""

import os
import datetime

import numpy as np
import pandas as pd
import sklearn as sk

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

print(DIR_PATH[:-5] + '\\DATA\\RAW\\Measure_01')

for FILE_NAME in os.listdir(DIR_PATH[:-5] + '\\DATA\\RAW\\Measure_01'):
    print(FILE_NAME)
    if FILE_NAME[-7:-4] == 'IMU':
        imu_data = pd.read_csv(DIR_PATH[:-5] + '\\DATA\\RAW\\Measure_01\\' + FILE_NAME, sep='\t',
                               names=['time', 'acc0', 'acc1', 'acc2', 'gyro0', 'gyro1', 'gyro2', 'mag0', 'mag1', 'mag2'])
        print(imu_data.head())
    elif FILE_NAME[-9:-4] == 'MoCap':
        imu_data = pd.read_csv(DIR_PATH[:-5] + '\\DATA\\RAW\\Measure_01\\' + FILE_NAME, sep='\t',
                               names=['time', 'x', 'y', 'z', 'tracked', 'zeta'])
        print(imu_data.head())

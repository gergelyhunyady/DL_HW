"""This file contains code to load the raw data into python"""

# ---------------------------------------------- Import packages here --------------------------------------------------
import os
import datetime

import numpy as np
import pandas as pd
import sklearn as sk
from sklearn import preprocessing
import matplotlib.pyplot as plt

# -------------------------------------------------- Package setup -----------------------------------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# --------------------------------------------------- Actual code ------------------------------------------------------
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

data_dict = {'IMU': {}, 'MoCap': {}}
file_names = []

for FILE_NAME in os.listdir(DIR_PATH[:-5] + '\\DATA\\RAW\\Measure_01'):
    print(FILE_NAME)
    if FILE_NAME[-7:-4] == 'IMU':
        imu_data = pd.read_csv(DIR_PATH[:-5] + '\\DATA\\RAW\\Measure_01\\' + FILE_NAME,
                               sep='\t',
                               decimal=',',
                               names=['time', 'acc0', 'acc1', 'acc2', 'gyro0', 'gyro1', 'gyro2', 'mag0', 'mag1', 'mag2'])
        data_dict['IMU'][FILE_NAME[:-8]] = imu_data
        file_names.append(FILE_NAME[:-8])
        print(imu_data.head())
        f, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
        imu_data.plot(x='time', y='mag0', ax=ax1)
        imu_data.plot(x='time', y='mag1', ax=ax2)
        imu_data.plot(x='time', y='mag2', ax=ax3)

    elif FILE_NAME[-9:-4] == 'MoCap':
        mocap_data = pd.read_csv(DIR_PATH[:-5] + '\\DATA\\RAW\\Measure_01\\' + FILE_NAME,
                                 sep='\t',
                                 decimal=',',
                                 names=['time', 'x', 'y', 'z', 'tracked', 'zeta'])
        data_dict['MoCap'][FILE_NAME[:-10]] = mocap_data
        print(mocap_data.describe())
        mocap_data.plot(x='x', y='z', ax=ax4)
        plt.show()

print(data_dict)

for name in file_names:
    scaler = preprocessing.StandardScaler().fit(data_dict['IMU'][name])
    data_dict['IMU'][name] = scaler.transform(data_dict['IMU'][name])
    print(data_dict['IMU'][name])
    scaler = preprocessing.StandardScaler().fit(data_dict['MoCap'][name])
    data_dict['MoCap'][name] = scaler.transform(data_dict['MoCap'][name])
    print(data_dict['MoCap'][name])
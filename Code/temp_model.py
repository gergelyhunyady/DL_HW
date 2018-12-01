#coding=utf-8

try:
    import os
except:
    pass

try:
    import datetime
except:
    pass

try:
    import hyperas
except:
    pass

try:
    import tensorflow as tf
except:
    pass

try:
    from tensorflow.python.client import device_lib
except:
    pass

try:
    import numpy as np
except:
    pass

try:
    import pandas as pd
except:
    pass

try:
    import sklearn as sk
except:
    pass

try:
    from sklearn import preprocessing
except:
    pass

try:
    from keras.models import Sequential
except:
    pass

try:
    from keras.layers.core import Activation, Dense, Flatten
except:
    pass

try:
    from keras.optimizers import SGD
except:
    pass

try:
    from keras.layers.convolutional import Conv1D, MaxPooling1D
except:
    pass

try:
    from keras.backend.tensorflow_backend import set_session
except:
    pass

try:
    from keras.callbacks import EarlyStopping, CSVLogger, ModelCheckpoint
except:
    pass

try:
    from keras.models import load_model
except:
    pass

try:
    import matplotlib.pyplot as plt
except:
    pass

try:
    from hyperopt import Trials, STATUS_OK, tpe
except:
    pass

try:
    from hyperas import optim
except:
    pass

try:
    from hyperas.distributions import choice, uniform
except:
    pass
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from hyperas.distributions import conditional

if timeseries.shape[0] == 1:
    timeseries = timeseries.T
nb_samples, nb_series = timeseries.shape
nb_inputs = nb_series - 8 #only 12 inputs (previous x,y,z position is an input now)
window_size = 20

#fill and split the input and output variables
X,y = make_timeseries_instances(timeseries, window_size,nb_inputs=nb_inputs)

test_size = int(0.15  * nb_samples)
valid_size = int(0.15 * nb_samples)

x_train, x_valid, x_test = X[:-(test_size+valid_size),:], X[-(test_size+valid_size):-test_size,:], X[-test_size:,:]
y_train, y_valid, y_test = y[:-(test_size+valid_size),:], y[-(test_size+valid_size):-test_size,:], y[-test_size:,:]

# Standardize input variables for train, valid and test data
for inpt in range(X.shape[1]):
    scaler = preprocessing.StandardScaler().fit(x_train[:,inpt])
    x_train[:,inpt] = scaler.transform(x_train[:,inpt])
    x_valid[:,inpt] = scaler.transform(x_valid[:,inpt])
    x_test[:,inpt] = scaler.transform(x_test[:,inpt])
    


def keras_fmin_fnct(space):

    n_layer1 = space['n_layer1']
    n_layer2 = space['n_layer1_1']
    optim = space['optim']
    n_batch = space['n_batch']
    
    window_size = 20
    filter_length = 5
    nb_outputs=3
    
    model = Sequential()
    model.add(Conv1D(filters=n_layer1, kernel_size=filter_length, activation='relu', 
                   input_shape=(window_size,nb_input_series)))
    model.add(MaxPooling1D())
    model.add(Conv1D(filters=n_layer2, kernel_size=filter_length, activation='relu'))
    model.add(MaxPooling1D())
    model.add(Flatten())
    model.add(Dense(nb_outputs,activation='linear'))
    model.compile(loss='mse', optimizer= optim, metrics=['mae'])
    
    result = model.fit(x_train, y_train,
              batch_size=n_batch,
              epochs=150,
              verbose=2,
              validation_data=(x_valid, y_valid),
              callbacks=[checkpointer,early_stopping],
              shuffle=True)
    
    validation_acc = np.amax(result.history['val_acc']) 
    print('Best validation acc of epoch:', validation_acc)
    return {'loss': -validation_acc, 'status': STATUS_OK, 'model': model}

def get_space():
    return {
        'n_layer1': hp.choice('n_layer1', [128, 256, 512]),
        'n_layer1_1': hp.choice('n_layer1_1', [128, 256, 512]),
        'optim': hp.choice('optim', ['rmsprop', 'adam', 'sgd']),
        'n_batch': hp.choice('n_batch', [16, 31, 64]),
    }

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from sklearn.metrics import mean_absolute_error 

import pandas as pd

training_data = pd.read_csv("final.csv")
training_data_x = training_data[['Day','Hour','Activity']]
training_data_y = training_data[['Duration']]

testing_data = pd.read_csv("final_test.csv")
testing_data_x = testing_data[['Day','Hour','Activity']]
testing_data_y = testing_data[['Duration']]

model = Sequential()

model.add(Dense(8, kernel_initializer='normal',input_dim = training_data_x.shape[1], activation='relu'))

model.add(Dense(8, kernel_initializer='normal',activation='relu'))
model.add(Dense(4, kernel_initializer='normal',activation='relu'))

model.add(Dense(1, kernel_initializer='normal',activation='linear'))

model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])

model.fit(training_data_x, training_data_y, epochs=5, batch_size=32, validation_split = 0.2)

predictions = model.predict(testing_data_x)

MAE = mean_absolute_error(testing_data_y , predictions)

print('Neural Network validation Mean Absolute Error = ')
print(MAE)

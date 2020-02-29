import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error 
import warnings 

warnings.filterwarnings('ignore')

training_data = pd.read_csv("studentOne.csv")
training_data_x = training_data[['Day','Hour','Activity']]
training_data_y = training_data[['Duration']]

testing_data = pd.read_csv("studentOnetest.csv")
testing_data_x = testing_data[['Day','Hour','Activity']]
testing_data_y = testing_data[['Duration']]

linearModel = LinearRegression()
linearModel.fit(training_data_x,training_data_y)

predicted_duration_linear = linearModel.predict(testing_data_x)

MAE = mean_absolute_error(testing_data_y , predicted_duration_linear)

print('Linear Regression validation Mean Absolute Error = ')
print(MAE)

poly = PolynomialFeatures(degree = 3) 
training_data_x_poly = poly.fit_transform(training_data_x) 

poly.fit(training_data_x_poly,training_data_y)

lin = LinearRegression() 
lin.fit(training_data_x_poly, training_data_y)

predicted_duration = lin.predict(poly.fit_transform(testing_data_x))

MAE = mean_absolute_error(testing_data_y , predicted_duration)

print('Polynomial Regression validation Mean Absolute Error = ')
print(MAE)

import csv
from datetime import datetime
from pytz import timezone
import calendar
import statistics 
from collections import Counter
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error 
import warnings 

warnings.filterwarnings('ignore')
csvfile = open('test.csv')
fileObject = csv.reader(csvfile, delimiter=' ', quotechar='|')

file = open('studentOne.csv', 'w')
writer = csv.writer(file)

file2 = open('studentOnetest.csv', 'w')
writer2 = csv.writer(file2)

prevhour = 9999
minutes = 9999
prevID = 0

next(fileObject)
writer.writerow(['Student IDs','Day','Hour','Activity','Duration'])
writer2.writerow(['Student IDs','Day','Hour','Activity','Duration'])

activityLastHour = []

def addToList(list1,writer,prevID,day_name,hr):
    list_table = Counter(list1)
    items = []
    for k, v in list_table.iteritems():
    	k = float(k)
    	if(k < 3):
    		items.append(k)
    		writer.writerow([prevID,day_name,hr,k,v*3])
    for i in range(0,3):
    	if(i not in items):
    		writer.writerow([prevID,day_name,hr,i,0])

i = 0

while(prevID < 1):
	row  = next(fileObject)
	arr = row[0].split(',')
	student_ID = int(arr[3])
	tz = timezone('EST')
	d = datetime.fromtimestamp(float(arr[1]),tz = tz)
	day_name = d.weekday()
	hr = d.hour

	if((hr != prevhour or student_ID != prevID) and activityLastHour != []):
		i = i + 3
		if(i < 3000):
			addToList(activityLastHour,writer,prevID,day_name,hr)
		else:
			addToList(activityLastHour,writer2,prevID,day_name,hr)
		activityLastHour = []

	else:
		activityLastHour.append(arr[2])

	prevhour = hr
	prevID = student_ID


training_data = pd.read_csv("studentOne.csv")
training_data_x = training_data[['Day','Hour','Activity']]
training_data_y = training_data[['Duration']]

testing_data = pd.read_csv("studentOnetest.csv")
testing_data_x = testing_data[['Day','Hour','Activity']]
testing_data_y = testing_data[['Duration']]

model = RandomForestRegressor()

training_data_x = training_data_x.ix[1:]
training_data_y = training_data_y.ix[1:]

model.fit(training_data_x,training_data_y.values.ravel())

predicted_duration = model.predict(testing_data_x)

MAE = mean_absolute_error(testing_data_y , predicted_duration)

print('Random forest validation Mean Absolute Error = ')
print(MAE)


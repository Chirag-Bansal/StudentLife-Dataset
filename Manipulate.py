import csv
from datetime import datetime
from pytz import timezone
import calendar
import statistics 
from collections import Counter

csvfile = open('test.csv')
fileObject = csv.reader(csvfile, delimiter=' ', quotechar='|')

file = open('final.csv', 'w')
writer = csv.writer(file) 

file2 = open('final_test.csv', 'w')
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

while(prevID < 50):
	row  = next(fileObject)
	arr = row[0].split(',')
	student_ID = int(arr[3])
	tz = timezone('EST')
	d = datetime.fromtimestamp(float(arr[1]),tz = tz)
	day_name = d.weekday()
	hr = d.hour

	if((hr != prevhour or student_ID != prevID) and activityLastHour != []):
		addToList(activityLastHour,writer,prevID,day_name,hr)
		activityLastHour = []

	else:
		activityLastHour.append(arr[2])

	prevhour = hr
	prevID = student_ID

while(prevID <= 59):
	row  = next(fileObject)
	arr = row[0].split(',')
	student_ID = int(arr[3])
	tz = timezone('EST')
	d = datetime.fromtimestamp(float(arr[1]),tz = tz)
	day_name = d.weekday()
	hr = d.hour

	if((hr != prevhour or student_ID != prevID) and activityLastHour != []):
		addToList(activityLastHour,writer2,prevID,day_name,hr)
		activityLastHour = []

	else:
		activityLastHour.append(arr[2])

	prevhour = hr
	prevID = student_ID
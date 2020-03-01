# StudentLife-Dataset

StudentLife Dataset is a dataset that uses sensing data from the phones of students to assess their mental health , academic performance and behavioral trends

The aim of this project was using the data of physical activity, (whether they are stationary, running or walking) we had to predict the user's activity for the next hour. 

### Getting the Dataset

I was unable to download the dataset from the University of Dartmouth website, I was however able to find the same dataset in the form of R tibbles. I wrote a small script called `CreateCsv.py` to convert that to csv file .

[The Link] (https://github.com/Frycast/studentlife)

I have uploaded the csv file as well named *test.csv*

### Converting the dataset

The data contained the location of the students for each second in UNIX Timestamp, which had to be converted to an hourly format. The activity should depend on the day and the hour, thus the data had to be converted into an hourly format and must contain the day number and the information about the durations spent in different activities.

I removed the data containing activity equal to 3 which represents unknown location as that would hamper results and does not indicate anything related to the information of the student.

The python file `Manipulate.csv` does the above mentioned task

The python file `Manipulate.py` creates two files, one file is `final.csv` (for training) for students 0-49 and the other is ` final_test.csv` (for testing) for students 50-59. 

### Data Details

Each file has the columns - StudentId, Day Number, Hour, Activity , Duration. Day Number denotes the day of the week(in integers i.e. 0 for sunday and 6 for saturday). Hour reprents the hour of the day in 24 hour format. 
Acitvity has three possible values- 0,1,2 and the duration contains their corresponding values. 
If there was no activity the duration will be 0 for that activity

---

Now this reduces to a regression problem, given three parameters we have to predict the duration. I have used various regression algorithms, thus I tried and tested their performance on the dataset.

The regression alogorithms I used were - 
* Decision Tree Regressor (DecisionTreeRegressor.py)
* Random Forrest Regressor (RandomForrestRegressor.py)
* Polynomial Regressor (degree = 3) (Also compared with Linear Regressor to understand the difference)
(PolynomialRegression.py)
* XGBoost (XGBoost.py)
* I also trained a small neural net using keras (NeuralNet.py)

Each of them have their own file(in brackets), running the file would fit the corresponding regressor

The paramter to compare models was mean absolute error (MAE)

The MAE for the different models were :
`````
For The Random Forrest Regressor, the value of MAE was 190.22
For The Polynomial Regressor, the value of MAE was 191.60 (Linear Regressor has a MAE of 334.12)
For The XGBoost , the value of MAE was 190.66
For The Decision Tree Regressor , the value of MAE was 190.23
For The Neural net, I tried different architechtures and the best MAE was for the architechture in the code with an MAE of 186.13
`````
They are very similar and have almost no difference.

### Another approaches tried:

* I tried to find the the mode for each hour, but almost each hour has the mode of 0 , which means most of the students spend most of their time in an hour being still. The performance was very great but gives us almost no information about the students

* When looking at the data I found that the students have very different lifestyles - ID 0 walks everyday at around 7, 11 but ID 50 rarely walks, therfore using the data of 0 to predict 50 will produce wrong results. Therefore I tried to use the data for each student to predict the activity of that particular student.

*This was only tried for student 0 with only two regression algorithms*

The results were as follows:
```
For The Random Forrest Regressor, the value of MAE was 85.13 
For The Polynomial Regressor, the value of MAE was 98.8
```
As the value of the MAE is significantly lower than the previous cases, using the students own data is better than to rely on the general trend. 
*The file `TestingForStudent.py` will create the csv file and run the Random Forrest Regressor. The file `PolynomialRegressorForStudent.py` will run the Polynomial Regressor*

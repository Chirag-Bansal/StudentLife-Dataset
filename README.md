# StudentLIfe-Dataset

StudentLife Dataset is a dataset that uses sensing data from the phones of students to assess their mental health , academic performance and behavioral trends

The aim of this project was given the data of physical activity, (i.e. whether they are still, running or walking) had to predict the user's acitivy for the next hour. I was unable to download the dataset from the darthmount website, I was however able to find the same datset in the form of R tibbles. I wrote a small script to convert that to csv file.

The data contained the location of the students for each second in UNIX Timestamp, which had to be converted to an hourly format. The activity should depend on the day and the hour, thus the data had to be converted into an hourly format containing the day and the information about the durations spent in different activities. I removed the data containing 3 which represents unknown location as that would hamper results and does not indicate anything


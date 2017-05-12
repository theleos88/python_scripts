import sys

import datetime

datetimeFormat = '%H:%M:%S'


file = open("/tmp/dates")

lines = file.readlines()


for i in lines:
	#print(i.strip())
	dates = i.strip().split("-")

	hour1 = dates[0].strip().split(" ")[3]
	hour2 = dates[1].strip().split(" ")[3]

	timedelta = datetime.datetime.strptime(hour2, datetimeFormat) - datetime.datetime.strptime(hour1,datetimeFormat)
	#print (hour1,hour2, timedelta)
	print (divmod(timedelta.total_seconds(), 60))
	




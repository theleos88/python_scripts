import csv
import sys

datafile = ""

perc_90 = 0
perc_94 = 0
perc_99 = 0
max = 0

if (__name__ == '__main__'):

	print (sys.argv[1])
	csvfile =  open(sys.argv[1], 'rb')
	sa = csv.reader(csvfile, delimiter=',')
	print sa
	max = 0

	for row in sa:
		max+=int (row[1])

	perc_90 = 0.90*max
	perc_94 = 0.94*max
	perc_99 = 0.99*max

	csvfile.seek(0)
	sa = csv.reader(csvfile, delimiter=',')

	max = 0
	p1=0
	p2=0
	p3=0
	for row in sa:
		max+=int (row[1])
		if (max>perc_90 and p1 == 0):
			p1 = 1
			print ("90th", row[0])

		if (max>perc_94 and p2 == 0):
			p2 = 1
			print ("94th", row[0])

		if (max>perc_99 and p3 == 0):
			p3 = 1
			print ("99th", row[0])

#	print ':'.join(row)



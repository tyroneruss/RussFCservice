# Read in date 
import sys


def CheckDup(salemonth):
	fclistpath = "build/Results.csv"

	# Build check for duplicate record in list 
	k=1
	duplicate = []
	
	duplfile = 'build/dupl-' + salemonth + '.csv'
	outduplfile = open(duplfile,'w')

	with open(fclistpath) as infile:
		seen = set()
		for line in infile:
			line_lower = line.lower()
			list = line_lower.split(",")
			address=list[1] + "_" + list[4]
			if address in seen:
				duplicate.append(address)
				outduplfile.write(line)
				k=k+1
			else:		
				seen.add(address)

	print "\nFile being scan for duplicates: ",fclistpath		
	print "\nTotal duplicate: ", k-1

	infile.close()
	outduplfile.close()

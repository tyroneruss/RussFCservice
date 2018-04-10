import os
import sys
import string
import CheckDupList
import ReadForeList

from os import listdir
from os.path import isfile, join

def main(argv):

	# My code here
	if len(argv) != 3:
		os.system("type help.txt")
		print("\nError! You do not have enough arguments")
		exit()

	salemonth = sys.argv[1]
	saledate  = sys.argv[2]
	
	fctotal = 0 # Initalize for FC total
	
	mypath="./data/" + salemonth
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	for county in onlyfiles:
		result = county.replace(".txt",'')
		if ("py" not in result) and ("csv" not in result):
			# print "County: ", county
			sum = ReadForeList.Readfclist(salemonth,result,saledate)
			fctotal = fctotal + sum
					
	print "\nThe total number records = ", fctotal
	
# results = CheckDupList.CheckDup(salemonth)

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

import os
import sys
import FindDupList
import RemoveDupl
import ConvertCamelCase

def MergeFiles(lastmonth,thismonth):

	oldfile = 'build/fc-final-' + lastmonth + ".csv"
	newfile = 'build/fc-final-' + thismonth + ".csv"
	
	filenames = [oldfile,newfile]
	with open('build/Results.csv', 'w') as outfile:
		for fname in filenames:
			with open(fname) as infile:
				for line in infile:
					outfile.write(line)
					
	print "\nResults file is now available"

def main(argv):

	# My code here
	if len(argv) < 3:
		print("\nError! You do not have enough arguments")
		exit()

	previous_month = sys.argv[1]
	salemonth = sys.argv[2]	
	
	MergeFiles(previous_month,salemonth)
	results = FindDupList.CheckDup(salemonth)
	
	os.remove("build/Results.csv") 
	print("\nThe Results file has been Removed!")
	
	RemoveDupl.RemoveDupRecords(salemonth)
	ConvertCamelCase.ChangeToCamelCase()
	
	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

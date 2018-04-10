# Read in date 
import sys
import os
import string
import re

from os import listdir
from os.path import isfile, join

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
      
def CountFC(county,salemonth):

	inputfile = "data/" + salemonth + "/" + county  + ".txt"

	# Open the file with read only
	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.
		
	my_list = data.splitlines()

	# Build foreclose list 
	i=0

	for line in my_list:
		if ("Title" in line):
			i=i+1
		
	infile.close()
	
	return i

def main(argv):

	# My code here
	if len(argv) < 2:
		print("\nError! You do not have enough arguments")
		exit()

	salemonth = sys.argv[1]
	
	# Create foreclosure list comma delimited
	fclistpath = "build/New-count-" + salemonth + ".csv"
	outfile = open(fclistpath,'a')
	outfile.write('County,Number\n')	
	
	fctotal = 0 # Initalize for FC total
	
	mypath="./data/" + salemonth
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]	
	
	for county in onlyfiles:
		countyname = county.replace(".txt",'')
		sum = CountFC(countyname,salemonth)
		print "County: ", countyname, " ",sum
		line = countyname + "," + str(sum) + "\n"
		outfile.write(line)
		fctotal = fctotal + sum
					
	print "\nThe total number records = ", fctotal
	lastline = "\nThe total number records = " + str(fctotal)
	outfile.write(lastline)	
	
	outfile.close()

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)
	

# Read in date 
import sys
import os
import requests
import socket
import string
import re
import shutil
import os.path

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
      
def FindRealTracList(vmonth,county,pagenum):
	
	flist = []
	forecloselist = {}

	inputfile = 'data/' + vmonth + '/RealTrac.txt'
	
	# Remove dupliacte records by address
	
	outputfile = '../Final-Build/' + vmonth + '/fc-final-05.csv'
	
	# Add  row to final output
	outfile = open(outputfile,'w')
	
	
	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.

	RealTrac_list = data.splitlines()

	# Build foreclose list 

	i=0
	count=1
	list = []
	
	for line in RealTrac_list:			
		if ("<span itemprop='streetAddress'>" in line):		
			list 	 = line.split("<span itemprop='streetAddress'>")
			Address  = list[1].split('</span>')
			citylist = Address[1].split('>')
			City 	 = citylist[1]
			i = i + 1
			count = 1
		if ("<span itemprop='postalCode'>" in line):
			postal = line.split("<span itemprop='postalCode'>")
			# print postal[1]
			listnum = len(postal)
			# print "\n",listnum
			zipcode = postal[1].split('</span>')
			zip = zipcode[0].split('</span>')
			strLocation = Address[0] + ',' + City + ',GA,' + str(zip[0]) + ',Homeowner,' + county
			print i,":", strLocation
			outfile.write(strLocation + "\n")
				
	return i
	
def main(argv):

	# Read data from Foreclosure Bid site 
	try:
	
		salemonth  = sys.argv[1]
		countyfile = "data/" + sys.argv[2]
		saledate   = sys.argv[3]
		
		total = 0
		sum   = 0
		count = 0

		
		with open(countyfile) as infile:
			for county in infile:
				county = county.replace("\n","")
				sum = FindRealTracList(salemonth,county,saledate)
				count = count + 1
				print count, " The number of records in the county ",county," is: ",sum
				total = total + sum 
	
		print "\nTotal records: ", total

	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

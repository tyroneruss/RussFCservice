# Read in date 
import sys
import os
import string
import re
import BuildFCList

from os import listdir
from os.path import isfile, join

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
      
def FixNameFC(month):

	inputfile = "build/fc-temp-" + month + ".csv"
	outputfile = "build/fc-list-" + month + ".csv"

	outfile = open(outputfile,'w')

	# Open the file with read only
	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.
		
	my_list = data.splitlines()

	# Build foreclose list 
	i=0
	# found records with a/k/a
	k=0

	for line in my_list:
		linearray = line.split(",") 
		fullname = linearray[5]
		FullName  = title_except(fullname,"and")	
	
		if FullName.find("A.k.a.") > -1: 
			#print FullName
			akaname = FullName.split("A.k.a.")
			number = len(akaname)
			member = number - 1
			# print akaname
			Name = akaname[member]
			print k,": ", Name
			k=k+1
		elif FullName.find("a/k/a") > -1: 
			#print FullName
			akaname = FullName.split("a/k/a")
			number = len(akaname)
			member = number - 1
			Name = akaname[member]
			# # print k,": ", Name
			k=k+1

		elif FullName.find("A/k/a") > -1: 
			#print FullName
			akaname = FullName.split("A/k/a")
			number = len(akaname)
			member = number - 1
			Name = akaname[member]
			# print k,": ", Name
			k=k+1
		elif FullName.find("Aka") > -1: 
			#print FullName
			akaname = FullName.split("Aka")
			number = len(akaname)
			member = number - 1
			Name = akaname[member]
			# print k,": ", Name
			k=k+1
		else:
			Name = FullName		
		
		strLine = linearray[0] + "," + linearray[1] + "," + linearray[2] + ",GA," + linearray[4] + "," + Name + "," + linearray[6]
		strLine = strLine + "\n"
		print strLine
		# Add client record to file	
		outfile.write(strLine)	
		i=i+1
		
	infile.close()
	outfile.close()
	
	return i,k

def main(argv):

	# My code here
	if len(argv) < 2:
		print("\nError! You do not have enough arguments")
		exit()

	salemonth = sys.argv[1]
	fctotal,akatotal = FixNameFC(salemonth)
	# print "\nThe total number records = ", fctotal, "AKA: ",akatotal
	sum = BuildFCList.BuildList(salemonth)
	print "\nThe total number records = ", sum, "AKA: ",akatotal
	
	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)
	

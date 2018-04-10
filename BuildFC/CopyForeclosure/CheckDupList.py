# Read in date 
import sys
import os
import re

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
   

def CheckDup(salemonth):
	fclistpath = "build/fc-list-" + salemonth + ".csv"

	# Build check for duplicate record in list 
	k=1
	i=0
	t=0
	duplicate = []
	
	# Remove dupliacte records by address
	filename = 'build/fc-temp-' + salemonth + '.csv'
	outfile = open(filename,'w')

	with open(fclistpath) as infile:
		seen = set()
		for line in infile:
			line_lower = line.lower()
			list = line_lower.split(",")
			address=list[1]
			temp = address.split(" ")
			street = title_except(temp[1], "")
			address = temp[0] + street
			if address in seen:
				duplicate.append(address)
				k=k+1
			else:		
				seen.add(address)
				outfile.write(line)
				t=t+1
				if "Homeowner" not in line:
					i=i+1
				# Build new list 		

	print "\nFile being scan for duplicates: ",fclistpath		
	print "\nTotal duplicate: ", k-1
	h=t-i
	print "\nTotal records without names: ", h
	print "\nTotal records with names: ", i
	print "\nTotal records: ", t

	infile.close()
	outfile.close()
	
	os.remove(fclistpath)
	

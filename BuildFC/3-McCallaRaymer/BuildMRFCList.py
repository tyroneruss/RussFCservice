# Read in date 
import sys
import os
import re
import CheckDupList
import CountyLookup
import shutil

from os import listdir
from os.path import isfile, join 

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)

def FindMRRecords(Month,filename,Saledate):

	# Add records records by address
	outputfile = './build/' + Month + '/fc-temp-' + Month + '.csv'	
	outfile = open(outputfile,'a+')

	with open(filename, "r") as datefile:
		data = datefile.read()  # Read the contents of the file into memory.
	datalist = data.splitlines()
	
	i = 0 
	count = 1
	list = []

	for line in datalist:
		if count == 1:
			list = line.split(',')
			# print len(list),' ', list
			Street 	 = list[2].replace('\xa0','')
			County 	 = list[3]
			value = Saledate + ',' + Street
			#print value
			
		if count == 2:
			location = line.split(',')
			Address = location[2].split('GA')	
			if len(Address) > 1:
				city   = Address[0].rstrip()
				zip    = Address[1].lstrip()
				strRecord = value + ',' + city + ',GA,' +  zip  + ',Homeowner,' + County + '\n'
				#print strRecord
				outfile.write(strRecord)

		if count == 3:
			i = i + 1
			# print i, ': ',strRecord
			count = 0
		
		count = count + 1

			
	outfile.close()
	
	print " "
	return i
	
def main(argv):

	sum = 0	
	total = 0
	
	Month    = sys.argv[1]
	saledate = sys.argv[2]

	# Remove old build file
	outputfile = './build/' + Month + '/fc-final-' + Month + '.csv'	
	if os.path.exists(outputfile):
		os.remove(outputfile)

	directory = './build/' + Month 
	if not os.path.exists(directory):
		os.makedirs(directory)		
		
	print 'Processing build files'
	print " "
	print '3 - MaCalla & Raymer '

	filename = './data/MCrecords-' + Month + '.csv'
	total  =  FindMRRecords(Month,filename,saledate)
	sum    =  CheckDupList.CheckDup(Month)
	
	src  = './build/' + Month + '/fc-final-' + Month + '.csv'
	dest = '../Final-Build/' + Month + '/fc-final-' + Month + '-03.csv'
		
	shutil.copy2(src,dest) 

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

	

# Read in date
import sys
import os
import re
import ConvertDate
import shutil

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
 
def FindFCRecords(Saledate,State,Month,year):

	builddir = './build/' + Month 
	if not os.path.exists(builddir):
		os.makedirs(builddir)		

	datadir = './data/' + Month 
	if not os.path.exists(datadir):
		os.makedirs(datadir)	
		
	inputfile = 'data/' + Month + '/auction.txt'
	
	# Remove dupliacte records by address
	outputfile =  './build/' + Month + '/fc-final-' + Month + ".csv"
	
	# Add  row to final output
	outfile = open(outputfile,'w')
	
	
	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.

	my_list = data.splitlines()

	# Build foreclose list 

	i=0
	count=1
	list = []
	Value1 = ""
	for line in my_list:
		if count == 1:
			Value1 = line.replace('\n','')	

		if "County" in line:
			strRecord = Value1 + ',' + line
			
		if "Auction" in line:
			recordlist = strRecord.split(',')
			Address	   = recordlist[0]
			if Address:
				Address   = title_except(recordlist[0], "")
				city      = title_except(recordlist[1], "")
				zipnumber = re.findall('\\d+', recordlist[2])
				if zipnumber:
					zip = zipnumber[0]
					county    = recordlist[3].replace("County","")
					county	  = county.lstrip()
					strRecord = Saledate + ',' + Address + ',' + city + ',' + State + ',' + str(zip) + ',Homeowner,' + county + '\n'
					i = i + 1
					# print i, ': ',strRecord
					outfile.write(strRecord)
			count = 0	
			
		count = count + 1
				
	infile.close()
	outfile.close()
	
	return i
	
def main(argv):

	results = 0
	sum   = 0
		
	state 	 = sys.argv[1]
	month 	 = sys.argv[2]
	saledate = sys.argv[3]
	MMDDYear = saledate.split('/')	
	Year	 = MMDDYear[2]
	
	filename = './build/' + month + '/fc-final-' + month + '.csv'
	# Remove old build file
	if os.path.exists(filename):
		os.remove(filename)
	
	directory = './build/' + month 
	if not os.path.exists(directory):
		os.makedirs(directory)		
	
	sum  = FindFCRecords(saledate,state,month,Year)

	print "1: Auction "
  	print "Total number of records found on the Auction sites: ", sum

	reportfile = '../Final-Build/' + month  + '/FCreportGA.txt'
		# Add  row to final output
	rptfile = open(reportfile,'a')
	
	strRecord = 'Auction|' + str(sum) + '|' + 'https://www.Auction.com|'  + './1-Auction/build/' + month +  '/fc-final-Aug.csv'
	rptfile.write(strRecord + '\n')	
	
	src  = './build/' + month + '/fc-final-' + month + '.csv'
	dest = '../Final-Build/' + month + '/fc-final-' + month + '-01.csv'
		
	shutil.copy2(src,dest) 

	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

	

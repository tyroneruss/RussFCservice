# Read in date 
import sys
import os
import re
import shutil

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   
   return " ".join(final)
   

def AddRecords(salemonth):

	fclistpath = './data/' + salemonth + '/BrockScott.txt'

	# Build check for duplicate record in list 
	k=0
	i=0
	t=0
	duplicate = []
	
	# Remove dupliacte records by address
	filename = './build/' + salemonth + '/fc-final-' + salemonth + '.csv'
	outfile = open(filename,'w')

	with open(fclistpath) as infile:
		seen = set()
		for line in infile:
			line_lower = line.lower()
			list = line_lower.split("\t")
			county   = title_except(list[0], "")
			saledate = list[1]
			location = title_except(list[6], "")
			AddressList = location.split(',')
			address = AddressList[0]
			zipcode = re.findall("\d+", AddressList[1])
			if zipcode:
				zip = zipcode[0]
				strLocation = saledate + ',' + address + ',GA,' + str(zip) + ',Homeowner,' + county	
				# print t,': ',strLocation
				temp = address.split(" ")
				if len(temp) > 1:
					street = title_except(temp[1], "")
					address = temp[0] + street							
				else:
					address = temp[0]
					
				if address in seen:
					duplicate.append(address)
					k=k+1
				else:		
					seen.add(address)
					outfile.write(strLocation + '\n')
					t=t+1

	
	return t

	infile.close()
	outfile.close()
	
	# os.remove(fclistpath)
	
def main(argv):

	# Read data from Aldp
	try:
	
		month  = sys.argv[1]
		sum = 0

		filename = './build/' + month + '/fc-final-' + month + '.csv'
		# Remove old build file
		if os.path.exists(filename):
			os.remove(filename)
		
		directory = './build/' + month 
		if not os.path.exists(directory):
			os.makedirs(directory)		
		
		sum = AddRecords(month)	
		print "5: Brack & Scoot"
		print ""
		print "The total number of records found on : ",sum


		src  = './build/' + month + '/fc-final-' + month + '.csv'
		dest = '../Final-Build/' + month + '/fc-final-' + month + '-05.csv'
			
		shutil.copy2(src,dest) 
		
		reportfile = '../Final-Build/' + month + '/FCreport.csv'
		# Add  row to final output
		rptfile = open(reportfile,'a')
		
		strRecord = 'Brack & Scott|' + str(sum) + '|https://www.brockandscott.com/BrockSearch.aspx|'+ './5-BrockScott/build/' + month +  '/fc-final-' + month + '.csv'
		rptfile.write(strRecord + '\n')
		rptfile.close()
	
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

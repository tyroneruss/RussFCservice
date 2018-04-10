# Read in date 
import sys
import os
import re
import shutil 
   
def SplitLocation(Location,StreetType):

	street = ''
	city   = ''
	
	for type in StreetType:
		if Location.find(type) > -1:
			address = Location.split(type)
			if len(address) > 1:
				street = address[0] + ' ' + type
				city   = address[1]
				if city.find('AKA') > -1:
					city = ''
				break;
		
	return street,city

def CreateList(salemonth):

	filepath = './data/' + salemonth + '/ShapiroHasting.csv'	
	StreetTypefile = './data/StreetType.txt'	
	
	with open(StreetTypefile, "r") as datefile:
		data = datefile.read()  # Read the contents of the file into memory.
	typelist = data.splitlines()
	
	# Build check for duplicate record in list 

	i=0
	
	# Remove dupliacte records by address
	filename = './build/' + salemonth + '/fc-final-' + salemonth + '.csv'
	outfile = open(filename,'w')

	strRecord = ''
	with open(filepath,"r") as infile:
		for line in infile:
			list = line.split(",")
			saledate = list[1]
			county	 = list[2]
			location = list[3]			
			location = location.replace('"','')			
			zipcode  = list[5].replace('\n','')
			Street,City = SplitLocation(location,typelist)
			if City != '':
				strRecord = saledate + ',' + Street + ',' + City + ',GA,' + str(zipcode) + ',Homeowner,' + county
				i = i  + 1
				#print i,': ',strRecord
				outfile.write(strRecord + '\n')
			
	infile.close()
	outfile.close()
	
	return i
	# os.remove(fclistpath)
	
def main(argv):

	# Read data from Aldp
	try:
	
		month  	 = sys.argv[1] 
		sum = 0
		
		directory = './build/' + month 
		if not os.path.exists(directory):
			os.makedirs(directory)		
		
		directory = './data/' + month 
		if not os.path.exists(directory):
			os.makedirs(directory)		
		
		sum = CreateList(month)			

		print "------------------------------------------------ "
		print "8: Shapiro and Hastings"
		print "Total numbers records found on this site: ",sum

		src  = './build/' + month + '/fc-final-' + month + '.csv'
		dest = '../Final-Build/' + month + '/fc-final-' + month + '-08.csv'
		
		shutil.copy2(src,dest) 
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

# Read in date 
import sys
import os
import requests
import string
import re
import shutil

from bs4 import BeautifulSoup
from lxml import html


def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
      
def ScrapeForeHtml(state,month):

	builddir = '../Final-Build/' + month 
	if not os.path.exists(builddir):
		os.makedirs(builddir)
		# Create folder
		
	filename = './build/' + month + '/fc-final-' + month + '.csv'
	
	outfile = open(filename,'w')
		
	URL = 'http://rubinlublin.com/property-listing/' + state + '-property-listings/'
	
	# Read data from URLforeclosure
	r = requests.get(URL)
	  		
	soup = BeautifulSoup(r.text,'lxml')

	# pri nt soup
	x = 0
	i = 0
	datelist = {}
	propertylist = {}
	citylist = {}
	propertylist = {}
	ziplist = {}
	countylist = {}
	
	# print soup
	
	for table_row in soup.select(".date"):
		line = repr(table_row)
		datearray = line.split('>')
		date = datearray[1].split(' ')
		datelist[i] = date[0]
		# print i,': ', datelist[i]
		i = i + 1

	i = 0	
	for table_row in soup.select(".property"):
		line = repr(table_row)
		propertyarray = line.split('>')
		property = propertyarray[1]
		propertylist[i] = property.replace("</td","")
		#print i,': ',datelist[i],',',propertylist[i]
		i = i + 1

	i = 0	
	for table_row in soup.select(".city"):
		line = repr(table_row)
		cityarray = line.split('>')
		city = cityarray[1]
		citylist[i] = city.replace("</td","")
		#print i,': ',datelist[i],',',propertylist[i],',',citylist[i]
		i = i + 1

	i = 0	
	for table_row in soup.select(".zip"):
		line = repr(table_row)
		ziparray = line.split('>')
		zip = ziparray[1]
		ziplist[i] = zip.replace("</td","")
		# print i,': ',datelist[i],',',propertylist[i],',',citylist[i],',',ziplist[i]
		i = i + 1

	i = 0	
	for table_row in soup.select(".county"):
		line = repr(table_row)
		countyarray = line.split('>')
		county = countyarray[1]
		countylist[i] = county.replace("</td","")
		strRecords = datelist[i] + ',' + propertylist[i] + ',' + citylist[i] + ',GA,' + ziplist[i] + ',Homeowner,' + countylist[i]
		# print strRecords 
		outfile.write(strRecords + '\n')
		i = i + 1

	return i
	
	
def main(argv):

	month 	 = sys.argv[1]
			
	filename = './build/' + month + '/fc-final-' + month + '.csv'
	# Remove old build file
	if os.path.exists(filename):
		os.remove(filename)

	directory = './build/' + month 
	if not os.path.exists(directory):
		os.makedirs(directory)		

			# Read data from Foreclosure site 
	try:
		
		sum = ScrapeForeHtml('georgia',month)
		
		src  = './build/' + month + '/fc-final-' + month + '.csv'
		dest = '../Final-Build/' + month + '/fc-final-' + month + '-07.csv'
		
		shutil.copy2(src,dest) 
		print "7 - Rubin & Lublin"
		print "The number of records on RealtyBid site: ",sum
			
		reportfile = '../Final-Build/' + month + '/FCreport.csv'
		# Add  row to final report
		rptfile = open(reportfile,'a')
		
		strRecord = 'Rubin & Lublin|' + str(sum) + '|http://rubinlublin.com|./7-RubinLublin/build/' + month + '/fc-final-' + month  + '.csv'
		rptfile.write(strRecord + '\n')

	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
	rptfile.close()
	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

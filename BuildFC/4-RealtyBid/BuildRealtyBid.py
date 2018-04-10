# Read in date 
import sys
import os
import requests
import string
import re
import shutil
import CountyLookup

from bs4 import BeautifulSoup
from lxml import html

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
      
def ScrapeForeHtml(page,state,month,saledate):
		
	filename = './build/' + month + '/fc-final-' + month + '.csv'
	
	outfile = open(filename,'a')
		
	URL = 'https://www.realtybid.com/search-results.cfm?page=' + str(page) + '&&q=GA&br=&ba=&st=&s=&ss=&pmin=&pmax='
	
	# Read data from URLforeclosure
	r = requests.get(URL)
	  		
	soup = BeautifulSoup(r.text,'lxml')

	# print soup
	x = 0
	i = 0
	location = {}
	for table_row in soup.select(".address"):
		line = repr(table_row)
		lineArray = line.split('>')
		street = lineArray[4].split('</span')
		citystzip = lineArray[5].split('</div')
		location  = citystzip[0].split(',')
		city = location[0].replace('\\r\\n','')
		newcity = city.lstrip()
		zip = re.findall('\\d+', location[1])		
		zipcode = zip[0] 
		county = CountyLookup.FindCounty(newcity)
		county = county.replace('\n','')
		address = saledate + ',' +street[0] + ',' + newcity + ',' +  state  + ',' + zipcode + ',Homeowner,'  + county
		outfile.write(address + '\n')
		i = i + 1

	return i
	
	
def main(argv):

	total = 0
	sum   = 0
	count = 0
	max   = 30
	state 	 = sys.argv[1]	
	month 	 = sys.argv[2]
	saledate = sys.argv[3]
	endrecord = 0
	
	filename = './build/' + month + '/fc-final-' + month + '.csv'
	# Remove old build file
	if os.path.exists(filename):
		os.remove(filename)
	
	directory = './build/' + month 
	if not os.path.exists(directory):
		os.makedirs(directory)		
		
	# Read data from Foreclosure Bid site 
	try:
	
		# for county in infile:
		print "Processing records on RealtyBid site......"
		for k in range(1,int(max)):	
			sum = ScrapeForeHtml(k,state,month,saledate)
			if (sum == 10):
				total = total + sum	
				# print "The number of records on RealtyBid page ",k,': ',total,"\n" 
			else:
				total = total + sum	
				break
													
		src  = './build/' + month + '/fc-final-' + month + '.csv'
		dest = '../Final-Build/' + month + '/fc-final-' + month + '-04.csv'
		
		shutil.copy2(src,dest) 
		print " "
		print "4 - RealtyBid.com "
		print "The number of records on RealtyBid site: ",total
			
		reportfile = '../Final-Build/' + month + '/FCreport.csv'
		# Add  row to final output
		rptfile = open(reportfile,'a')
		
		strRecord = 'RealtyBid|' + str(total) + '|' + 'http://www.foreclosurehotline.net|./4-RealtyBid/build/' + month +  '/fc-final-' + month + '.csv'
		rptfile.write(strRecord + '\n')
		
		rptfile.close()
	
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

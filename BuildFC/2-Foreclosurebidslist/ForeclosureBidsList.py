# Read in date 
import sys
import os
import requests
import ForelistCounter
import socket
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
      
def ScrapeForeHtml(salemonth,county,saledate):

	arraydate  = saledate.split('/')
	month_num  = arraydate[0]
	year_num   = arraydate[2]
	
	URLforeclosure = 'http://foreclosurebidslist.com/foreclosures/ga/' + county + '/' + year_num + '/' + month_num
	
	# Add header row to final output
	
	filename = './build/' + salemonth + '/fc-final-' + salemonth + '.csv'
	outfile = open(filename,'a+')
	
	# Read data from URLforeclosure
	r = requests.get(URLforeclosure)
	
	records = []
	# 
	soup = BeautifulSoup(r.text,'lxml')
	foreclosure_links = []

	j = 0
	x = 0
	i = 0
	suffix = ''
	
	for table_row in soup.select(".grid tr"):
		table_cells = table_row.findAll('td')	
		if len(table_cells) > 0:
			line = str(table_cells) + "\n"
			if "img" in line:
				strLine	= line.split("</td>")				
				# Address
				addressline = strLine[1].split('>')
				if len(addressline) >=4:					
					address = addressline[2].replace("<br/","")
					
					# City and Zip code
					cityzip = addressline[3].split(",")
					zipnumber = re.findall('\\d+', cityzip[1])		
					if zipnumber:
						# Client's first and last name
						strName = strLine[7]
						name = strName.split(">")
						
						#Build fullname 
						lastname = name[2].replace("</div","")
						lastname = lastname.lstrip()
						if lastname:
							firstname = name[4].replace("</div","")
							firstname = firstname.rstrip()
							fullname  = firstname + " " + lastname
							FullName  = title_except(fullname,"and")
							
							if FullName.find('A/k/a') > -1:
								namelist = FullName.split('A/k/a')
								length  = len(namelist)
								FullName = namelist[length-1]														
							elif FullName.find('Jt.') > -1 or FullName.find('Sr.') > -1 or FullName.find('IIi') > -1 or FullName.find('IIi') > -1:									   
								namelist = FullName.split(',') 
								if len(namelist) > 1:
									FullName = namelist[1]	
								else:
									FullName  = "Homeowner"	
							elif FullName.find('Inc') > -1 or FullName.find('Llc') > -1:									   
								# print 'This string includes Inc'								
								x = x + 1
						else:
							FullName  = "Homeowner"
												
						# Build file for foreclosure mailer
						# print saledate,",",address,",",cityzip[0],",GA,", zipnumber[0],",",FullName,",",county
						strLine = saledate + "," + address + "," + cityzip[0] + ",GA," + zipnumber[0] + "," + FullName + "," + county + "\n"
						
						# Add client record to file				
						outfile.write(strLine)			
						i = i + 1

	return i
	
	
def main(argv):

	month 	   = sys.argv[1]
	countyfile = sys.argv[2]
	saledate   = sys.argv[3]
	
	total   = 0
	sum     = 0
	count   = 0
	results = 0
	
	filename = './build/' + month + '/fc-final-' + month + '.csv'
	# Remove old build file
	if os.path.exists(filename):
		os.remove(filename)
	
	directory = './build/' + month 
	if not os.path.exists(directory):
		os.makedirs(directory)		

			
	# Read data from Foreclosure Bid site 
	try:

		print " "
		print '2 - ForeclosureBidsList.com '
		print 'Processing ForeclosureBidsList records... it will take a few minutes '

		with open(countyfile) as infile:
			for county in infile:
				county = county.replace("\n","")
				sum = ScrapeForeHtml(month,county,saledate)
				count = count + 1
				print count, ": The number of records in the county ",county," is: ",sum
				total = total + sum
				
		print 'The total number of records found in 158 counties: ',total

		src  = './build/' + month + '/fc-final-' + month + '.csv'
		dest = '../Final-Build/' + month + '/fc-final-' + month + '-02.csv'
			
		shutil.copy2(src,dest) 
		
		reportfile = '../Final-Build/' + month + '/FCreport.csv'
			# Add  row to final output
		rptfile = open(reportfile,'a')
		
		strRecord ='Foreclosurebidslist|' + str(total) + '|' + 'https://www.foreclosurebidslist.com|' + './2-Foreclosurebidslist/build/' + month +  '/fc-final-' + month  + '-.csv'
		rptfile.write(strRecord + '\n')
			
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

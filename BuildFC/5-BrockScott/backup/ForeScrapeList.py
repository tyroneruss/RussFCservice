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
	
	URLforeclosure = 'http://foreclosurebidslist.com/foreclosures/ga/' + county
	
	# Add header row to final output
	
	filename = 'build/fc-final-' + salemonth + '.csv'

	outfile = open(filename,'a')
	
	# Read data from URLforeclosure
	r = requests.get(URLforeclosure)
	
	records = []
	# 
	soup = BeautifulSoup(r.text,'lxml')
	foreclosure_links = []

	x = 0
	i = 0
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
					if not cityzip[0] == '':
						zipnumber = re.findall('\\d+', cityzip[1])		
						
						# Client's first and last name
						strName = strLine[7]
						name = strName.split(">")
								
						#Build fullname 
						#print name
						lastname = name[2].replace("</div","")
						lastname = lastname.lstrip()
						if lastname:
							firstname = name[4].replace("</div","")
							firstname = firstname.rstrip()
							fullname  = firstname + " " + lastname
							FullName  = title_except(fullname,"and")
						else:
							FullName  = "Homeowner"
						
						pattern = re.compile(r'Inc.')
						if pattern.findall(FullName):
							namelist = FullName.split(",")
							FullName = namelist[0]
						
						# Build file for foreclosure mailer
						# print saledate,",",address,",",cityzip[0],",GA,", zipnumber[0],",",FullName,",",county
						strLine = saledate + "," + address + "," + cityzip[0] + ",GA," + zipnumber[0] + "," + FullName + "," + county + "\n"
						
						# Add client record to file				
						outfile.write(strLine)			
						i = i + 1
						
	return i
	
	
def main(argv):

	if len(sys.argv) == 2 and sys.argv[1] == "-help":
		os.system("type help.txt")
		print("\nError! You do not have enough arguments")
		exit()
		
	# Count the number of foreclosure records
	if sys.argv[1] == "-C" and  len(sys.argv) == 3:
		month = ""
		countyfile = "data/" + sys.argv[2] + ".csv"		
		ForelistCounter.CountRecords(countyfile,month)
		exit()
	elif (sys.argv[1] == "-C" and  len(sys.argv) == 4):
		month = argv[3]
		countyfile = "data/" + sys.argv[2] + ".csv"		
		ForelistCounter.CountRecords(countyfile,month)
		exit()	

	# Run script to gather foreclosure records and create mailer list
	if len(sys.argv) >= 4:
		salemonth  = sys.argv[1]
		countyfile = "data/" + sys.argv[2] + ".csv"
		saledate   = sys.argv[3]
	else:
		print("\nError! You do not have enough arguments")
		print("\nError! You do not have enough arguments")
		print("\n---------------------------------------")
		print("Unknown options:")
		print("Usage: python ForeScrapeList.py [salemonth] [countyfolder] [saledate]")
		print(">>")
		print(">>")

	total = 0
	sum   = 0
	count = 0

			
	# Read data from Foreclosure Bid site 
	try:
	
		with open(countyfile) as infile:
			for county in infile:
				county = county.replace("\n","")
				sum = ScrapeForeHtml(salemonth,county,saledate)
				count = count + 1
				print count, ": The number of records in the county ",county," is: ",sum
				total = total + sum 
	
		print "\nTotal records: ", total
		
		filename = 'build/fc-final-' + salemonth + '.csv'

		destdir = '../Final-Build/' + salemonth
		if not os.path.exists(destdir):
			os.makedirs(destdir)
			
		src  = 'build/fc-final-' + salemonth + '.csv'
		dest = '../Final-Build/' + salemonth + '/fc-final-02.csv'
		
		shutil.move(dest, src)
				
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

# Read in date 
import sys
import os
import requests
import socket
import string
import re

from bs4 import BeautifulSoup
from lxml import html

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
      
def ScrapeForeCount(county, month):

	# Add header row to final output
	
	RunCopyfile   = open('../CopyForeclosure/data/RunCopyCounties.csv','a')
	RunScrapefile = open('data/RunScrapeCounties.csv','a')

	if month != "":
		month = "/2017/" + str(month)
		
	URLforeclosure = 'http://foreclosurebidslist.com/foreclosures/ga/' + county + month
	
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
						i = i + 1
	if i > 38:
		county = county + "\n"
		RunCopyfile.write(county)
		print county," county has more than 40 records"
		# i = i - 39
	else:
		county = county + "\n"
		RunScrapefile.write(county)
	
	RunCopyfile.close()	
	RunScrapefile.close()
	
	return i
	
def CountRecords(countyfile,month):
	
	# My code here
	total = 0
	sum   = 0
	count = 1
	
	# Read data from Foreclosure Bid site 
	try:
		with open(countyfile) as infile:
			for county in infile:
				county = county.replace("\n","")
				sum = ScrapeForeCount(county,month)
				print count,": County: ",county," - ",sum
				total = total + sum 
				count = count + 1
				
		print "\nTotal number of foreclosure records: ", total
		
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 

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
      
def ScrapeForeHtml():

	# builddir = '../Final-Build/' + month 
	
	# if not os.path.exists(builddir):
		# os.makedirs(builddir)
		# Create folder
		
	# filename = './build/fc-final-' + month + '.csv'
	
	# outfile = open(filename,'a')
		
	URL = 'http://rubinlublin.com/property-listing/georgia-property-listings/'
	
	# Read data from URLforeclosure
	r = requests.get(URL)
	  		
	soup = BeautifulSoup(r.text,'lxml')

	print soup
	x = 0
	i = 0
	
	return i
	
	
def main(argv):


	total = 0
	sum   = 0
		
	# Read data from Foreclosure Bid site 
	try:
	
		# print "Processing records on RealtyBid site......"
		# for k in range(1,int(max)):	
		sum = ScrapeForeHtml()
			# if (sum == 10):
				# total = total + sum	
				# print "The number of records on RealtyBid page ",k,': ',total,"\n" 
			# else:
				# total = total + sum	
				# break
				
									
		# src  = './build/fc-final-' + month + '.csv'
		# dest = '../Final-Build/' + month + '/fc-final-' + month + '-04.csv'
		
		# shutil.copy2(src,dest) 
		# print "4 - RealtyBid.com "
		# print "The number of records on RealtyBid site: ",total
			
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

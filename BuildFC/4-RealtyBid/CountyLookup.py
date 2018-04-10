# Read in date 
import sys
import os
import re

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)

def FindCounty(City):
	countyfile = './data/CityCounty.csv'

	# City/County/Zip lookup records
	k=0
	CountyTable = []
	CountyName = ""
	
	with open(countyfile) as infile:
		for line in infile:
			line_lower = line.lower()
			list = line_lower.split(",")
			k = k + 1
			cityname = title_except(list[0], "")
			if City == cityname:
				CountyName =  title_except(list[1], "") 

	infile.close()
	# print "The city ",City," is in ",CountyName
	
	return CountyName
	


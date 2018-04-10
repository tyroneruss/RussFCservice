# Read in date 
import sys
import os
import requests
import ForelistCounter
import socket
import string
import re
import CheckDupList
import shutil

def main(argv):

	county = sys.argv[1]
	
	try:
		FullName = 'Tyrone '
		
		suffix = county
		if county.find('Jr.') > -1:
			FullName = FullName + ' ' + suffix
		elif  county.find('Sr.') > -1:
			FullName = FullName + ' ' + suffix
			print 'The text found: ',suffix
		elif  county.find('Ii') > -1:
			FullName = FullName + ' ' + suffix
			print 'The text found: ',suffix
		elif  county.find('IIi') > -1:
			FullName = FullName + ' ' + suffix
			print 'The text II found: ',suffix
	
		
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

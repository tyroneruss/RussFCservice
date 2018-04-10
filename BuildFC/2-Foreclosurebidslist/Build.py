# Build Georgia listing

import sys
import os
import shutil

	
def main(argv):

	try:
		from configparser import ConfigParser

	except ImportError:
		from ConfigParser import ConfigParser  # ver. < 3.0

	# instantiate
	config = ConfigParser()

	# parse existing file
	config.read('Config.ini')	
	
	# Read paths from a section

	V_ScriptNameScrape 	= config.get('FC_SCRAPE_GA', 'ScriptNameScrape')  
	V_CountyFile 	  	= config.get('FC_SCRAPE_GA', 'CountyFile') 		
	V_Month 		  	= config.get('FC_SCRAPE_GA', 'Month') 		
	V_Saledate 		  	= config.get('FC_SCRAPE_GA', 'Saledate') 
	
	# 1 - 
	print V_Saledate
	RunScript = 'python ' + V_ScriptNameScrape + ' ' + V_Month + ' ' + V_CountyFile + ' ' + V_Saledate
	os.system(RunScript)
	os.chdir( '../' )

	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

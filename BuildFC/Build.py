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
	
	# Read config info from a file
	V_SriptPathAuction          = config.get('FC_LISTING','ScriptPathAuction')    # 1
	V_ScriptPathFCBidlist       = config.get('FC_LISTING','ScriptPathFCBidlist')  # 2
	V_ScriptPathMRFCList        = config.get('FC_LISTING','ScriptPathMRFCList')   # 3
	V_ScriptPathRealtyBid       = config.get('FC_LISTING','ScriptPathRealtyBid')  # 4
	V_ScriptPathBrockScott      = config.get('FC_LISTING','ScriptPathBrockScott') # 5	
	V_ScriptPathAldp            = config.get('FC_LISTING','ScriptPathAldp')       # 6
	V_ScriptPathRubin           = config.get('FC_LISTING','ScriptPathRubin')      # 7
	V_ScriptPathShapiroHasting  = config.get('FC_LISTING','ScriptPathShapiroHasting') # 8
	V_ScriptPathMartinBrunavs   = config.get('FC_LISTING','ScriptPathMartinBrunavs') # 9
	V_State                     = config.get('FC_LISTING', 'State') 
	V_CountyFile                = V_State + '-Counties.csv'
	V_Month                     = config.get('FC_LISTING', 'Month') 		
	V_Day                       = config.get('FC_LISTING', 'Day') 		
	V_Saledate1                 = config.get('FC_LISTING', 'Saledate1') 
	V_Saledate2                 = config.get('FC_LISTING', 'Saledate2') 
	V_Year                      = config.get('FC_LISTING', 'Year') 		
	
	directory = './Final-Build/' + V_Month 
	if not os.path.exists(directory):
		os.makedirs(directory)		
		
	# Clean build
	RunScript = 'python Clean.py ' + V_Month 
	# print RunScript
	os.system(RunScript)
	print "------------------------------------------------------------"
		
	#1 - Auction site
	os.chdir(V_SriptPathAuction)
	RunScript = 'python AuctionFCList.py ' +  V_State + ' ' + V_Month + ' ' + V_Saledate1
	#print RunScript
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )
	
	# 2 - Foreclosurebidslist.com
	os.chdir(V_ScriptPathFCBidlist)
	RunScript = 'python ForeclosureBidsList.py '  + V_Month + ' ' + V_CountyFile + ' ' + V_Saledate1
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )

	# 3 - McCalla Raymer MRFCList - Foreclosure Hotline
	os.chdir(V_ScriptPathMRFCList)
	RunScript = 'python BuildMRFCList.py ' + V_Month  + ' ' + V_Saledate1
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )

	# 4 - RealtyBid Foreclosure
	os.chdir(V_ScriptPathRealtyBid)
	RunScript = 'python BuildRealtyBid.py ' + V_State + ' ' + V_Month + ' ' + V_Saledate1
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )

	# 5 - Brock Scott  listings - ['\t']
	os.chdir( V_ScriptPathBrockScott )
	V_SriptName = 'BrockScott.py'
	RunScript = 'python ' + V_SriptName + ' ' + V_Month + ' ' + V_Saledate1
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )
	
	#6 - Adridgepite Foreclosure listings
	os.chdir( V_ScriptPathAldp )
	V_SriptName = 'BuildAdridge.py'
	RunScript = 'python ' + V_SriptName + ' ' + V_Month + ' ' + V_Saledate1
	# print "Run : ", RunScript
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )

	# 7 - Rubin Foreclosure listings
	os.chdir(V_ScriptPathRubin)
	RunScript = 'python BuildRubinLublin.py ' + V_Month
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )

	# 8 - ShapiroHasting listings
	os.chdir(V_ScriptPathShapiroHasting)
	RunScript = 'python BuildShapiroHasting.py ' + V_Month
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )

	# 9 - MartinBrunavs site
	os.chdir(V_ScriptPathMartinBrunavs)
	RunScript = 'python BuildMartinBrunavs.py ' + V_Month + ' ' + V_Saledate1
	os.system(RunScript)
	print " "
	print " "
	os.chdir( '../' )
	
	# Compile final FC list
	RunScript = 'python CompileList.py ' + V_Month + ' ' + V_Day 
	print "Run : ", RunScript
	os.system(RunScript)
			
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

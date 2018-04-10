# Read in date 
import sys
import os
import re
import shutil 

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   
   return " ".join(final)
   
def CreateList(salemonth,saledate):

	fclistpath = './data/' + salemonth + '/fc-temp-' + salemonth + '.txt'
	
	# Build check for duplicate record in list 
	k=1
	i=0
	
	# Remove dupliacte records by address
	filename = './build/' + salemonth + '/fc-final-' + salemonth + '.csv'
	outfile = open(filename,'w')

	with open(fclistpath) as infile:
		seen = set()
		for line in infile:
			line_lower = line.lower()
			list = line_lower.split("\t")
			street	= title_except(list[1],"")
			city	= title_except(list[3],"")
			zipcode = list[5]
			county	= title_except(list[6],"")
			strRecord = saledate + ',' + street + ',' + city + ',GA,' + str(zipcode) + ',Homeowner,' + county
			i = i  + 1
			outfile.write(strRecord + '\n')

	infile.close()
	outfile.close()
	
	return i
	# os.remove(fclistpath)
	
def main(argv):

	# Read data from Aldp
	try:
	
		month  	 = sys.argv[1]
		Saledate = sys.argv[2] 
		sum = 0
		
		filename = './build/' + month + '/fc-final-' + month + '.csv'
		# Remove old build file
		if os.path.exists(filename):
			os.remove(filename)

		directory = './build/' + month 
		if not os.path.exists(directory):
			os.makedirs(directory)		
		
		sum = CreateList(month,Saledate)			

		print "------------------------------------------------ "
		print "6: Adridgepite"
		print "Total numbers records found on this site: ",sum
		
		src  = './build/' + month + '/fc-final-' + month + '.csv'
		dest = '../Final-Build/' + month + '/fc-final-' + month + '-09.csv'
			
		shutil.copy2(src,dest) 
			
		
	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

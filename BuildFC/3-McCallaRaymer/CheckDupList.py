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

def CheckDup(month):
	srcfile =  "./build/" + month + '/fc-temp-' + month + ".csv"
	
	# Build check for duplicate record in list 
	k=1
	i=0
	t=0
	l=0
	duplicate = []
	
	# Remove dupliacte records by address
	DupRemovefile = "./build/" + month + '/fc-final-' + month + ".csv"
	outfile = open(DupRemovefile,'w')
	
	with open(srcfile) as infile:
		seen = set()
		for line in infile:
			line = line.replace("\n","")
			line_lower = line.lower()			
			list = line_lower.split(",")
			if len(list) > 1:
				address=list[1]
				temp = address.split(" ")
				count = len(temp)
				if count > 1:
					address = temp[0] + temp[1]
					l = l + 1
					if address in seen:
						duplicate.append(address)				
						k=k+1
					else:		
						seen.add(address)
						strRecord = line + '\n'
						outfile.write(strRecord)
						t=t+1
						#print i,": ",list[0]," ",temp			
						if "Homeowner" not in line:
							i=i+1
						# Build new list

	k = k - 1
	t = t- 1
	l = l + 1
	# print "\n\nFile being scan for duplicates: ",srcfile	
	print "\nTotal number of records found: ",l
	print "\nTotal duplicates removed: ", k
	print "\nTotal records found on this site: ", l - k
	

	infile.close()
	outfile.close()
	os.remove(srcfile)
	
	return i + l



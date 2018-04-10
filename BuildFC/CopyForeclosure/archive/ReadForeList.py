# Remove anything not digits
import string
import sys
import re

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)

# Read in date 
def Readfclist(salemonth,county,foreclosedate):

	flist = {}
	forecloselist = {}

	inputfile = "data/" + salemonth + "/" + county  + ".txt"

	# Open the file with read only
	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.
		
	my_list = data.splitlines()
	# Create foreclosure list comma delimited
	filepath = "build/fc-list-" + salemonth + ".csv"
	outfile = open(filepath,'a')

	# Build foreclose list 

	i=1
	count=1
	total=0

	finallist = ""
	
	for line in my_list:
		if ("Title" in line):
			forecloselist[i]= flist
			street =  title_except(forecloselist[i][1],"")
			citystatezip = forecloselist[i][2].split(",")
			city = citystatezip[0]
			city = title_except(city, "")					
			zip = re.findall('\\d+', citystatezip[1])
					
			if(len(flist) == 4):
				# print i, ": ", len(flist), forecloselist[i][1]," ",city," GA ",zip[0]," Homeowner"
				finallist = foreclosedate + "," + street + "," + city + ",GA" + "," + zip[0] + ",Homeowner"				
				finallist
				
			if(len(flist) == 6 or len(flist) == 7):
				# print i, ": ", len(flist), forecloselist[i][1]," ",city," GA ",zip[0]," Homeowner"
				firstname = forecloselist[i][4]
				firstname = firstname.strip()
				lastname = forecloselist[i][3]
				lastname = lastname.strip()
				fullname = firstname + " " + lastname
				clientname = title_except(fullname, "and")
				finallist = foreclosedate + "," + street + "," + city + ",GA" + "," + zip[0] + "," + clientname
				finallist
				
			finallist = finallist + "," + county + "\n"
			print finallist
			
			if (("LLC" not in finallist) and ("L.L.C." not in finallist)  and ("INC" not in finallist) and ("Inc" not in finallist) and ("Llc" not in finallist)):	
				outfile.write(finallist)		
				total=total+1
				
			count=1
			flist = {}
		
		else: 
			line=line.lstrip()
			flist[count]=line
			# print count, ": ", flist[count]
			count=count+1
			
	print "County: ", county," - total records: ", total

	outfile.close()
	infile.close()
	
	return total
	
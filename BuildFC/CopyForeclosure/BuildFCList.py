import sys
import os
import re 

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
   
def BuildList(month):

	inputfile = "build/fc-" + month + "-list.csv"
	with open(inputfile, "r") as infile:
		data = infile.read()  
		# Change client name to CamelCase	
		
	resultsfile = "build/fc-final-" + month + ".csv"
	outfile = open(resultsfile, "w")
		
	my_list = data.splitlines()
	
	i = 0
	newlist = {}

	for line in my_list:
		list = line.split(",")
		# Camel Case fields
		if len(list) == 7:
			saledate = list[0]
			street = title_except(list[1], "")			
			city = title_except(list[2], "")					
			clientname = title_except(list[5], "and")
			county = title_except(list[6], "")				
			zipcode = title_except(list[4], "")				
			# record = [saledate,street,city,'GA',zipcode,clientname,county]
			newline = saledate + "," + street + "," + city + "," + 'GA' + "," + zipcode + "," + clientname + "," + county + "\n"
			print newline
			# Create dictionary
			# newlist[i].append(record)
			i = i + 1
			outfile.write(newline)			
			
	#os.remove(inputfile)
	
	infile.close()
	outfile.close()
	return i
	
	
# total = BuildList("February")
# print "The mumber of records: ", total

		
		

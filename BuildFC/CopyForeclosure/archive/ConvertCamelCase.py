import sys
import os
import re 

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)
   
def ChangeToCamelCase(state,filename):

	inputfile = "build/" + state + "/" + filename + ".csv"
	with open(inputfile, "r") as infile:
		data = infile.read()  # Change client name to CamelCase

	resultsfile = "build/" + state + "/fc-final-" + filename + ".csv"
	outfile = open(resultsfile, "w")
		
	my_list = data.splitlines()
	
	header = "Sale Date,Address,City,State,Zip,Homeowner,County\n"
	outfile.write(header)

	for line in my_list:
		list = line.split(",")
		# Camel Case fields
		if len(list) == 7:
			street = title_except(list[1], "")			
			city = title_except(list[2], "")					
			clientname = title_except(list[5], "and")
			county = title_except(list[6], "")						
			# print street," ", city," ",state," ",clientname
			newline = list[0] + "," + street + "," + city + "," + state + "," + list[4] + "," + clientname + "," + county + "\n"
			outfile.write(newline)
			
	os.remove(inputfile)
	
	infile.close()
	outfile.close()
	

		
		

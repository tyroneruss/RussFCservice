import sys

def RemoveDupRecords(salemonth):
	records = []
	duplist = []

	print "\nRemoving Duplicates......................"
	with open('build/fc-final-September.csv') as f:
		records = f.read().splitlines()
		
	print "The number read in is: ", len(records)

	with open('build/dupl-September.csv') as duplicates:
		for line in duplicates:
			line = line.replace("\n","")
			duplist.append(line)

	print "The number dulicates is: ", len(duplist)

	i = 0
	for line in duplist:
		for x in range(0,len(records)-1):
			#print records[x]
			if line == records[x]:
				records.remove(line)
				i = i + 1
				# print len(records)
			
	print "Number of remaining records: ", len(records)
	
	filepath = "build/Mailer-" + salemonth + ".csv"
	with open(filepath,'w') as outfile:	
		header = "Sale Date,Address,City,State,Zip,Homeowner,County\n"
		outfile.write(header)
		for record in records:
			record = record + "\n"
			outfile.write(record)
	


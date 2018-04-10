import sys
import os
import shutil


def main(argv):

	if len(sys.argv) !=2:
		print len(sys.argv)
		os.system("type help.txt")
		print("\nError! You do not have enough arguments")
		exit()
	
	try:
	
		salemonth = sys.argv[1]
		destdir = '../Final-Build/' + salemonth + '/'
		
			
		buildSource = os.path.expanduser('~') + '\\Development\\Python\\Foreclosure-list\\BuildForeClosure-GA\\2 - GaScrape\\build\\fc-final-' + salemonth + '.csv'
	
		if not os.path.exists(buildSource):
			print "Not found: ",buildSource
			# os.makedirs(destdir)
		else:
			print "Found: ",buildSource
		

		# dest = '../Final-Build/' + salemonth + '/'

		# os.listdir(destdir)
		
		# shutil.move(filesource, dest)

	except ValueError:
		print "Oops!  That was not a valid URL.  Try again..."
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

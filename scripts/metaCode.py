"""
This program will attempt to write a selenium program and run it
"""
import time
import sys
import os
#import xlwt
#from xlwt import Workbook
from multiprocessing import Process


#selenium binding variables
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def openFile(fname):
	if not os.path.isfile("metaCode/"+fname+".py"):
		with open("metaCode/"+fname+".py","w") as f:
			pass

def importsAndFrom(f):
	"""writes all necessary imports and froms"""
	f.write("import time\n")
	f.write("import sys\n")
	f.write("import os\n")
	f.write("from multiprocessing import Process\n")
	f.write("from selenium import webdriver\n")
	f.write("from selenium.webdriver.common.keys import Keys\n")
	f.write("from selenium.webdriver.common.by import By\n")
	f.write("from selenium.webdriver.support import expected_conditions as EC\n")
	f.write("from selenium.webdriver.support.ui import WebDriverWait\n")
	f.write("driver = webdriver.Chrome('/usr/local/bin/chromedriver')\n")

	f.write("\n")

def helloWorld(fname):
	"""
	will write hello world in a program
	"""
	f = open("metaCode/"+fname+".py","w")

	importsAndFrom(f)


	f.write("driver.get('https://www.google.com/')")
	f.write("print adsfasdf")
	f.close()

def rewrite(fname):
	f = open("metaCode/"+fname+".py","w")
	importsAndFrom(f)
	f.write("driver.get('https://www.google.com/')")
	f.close()
	return 0




def runProgram(fname):
	run = "python3 "+ "metaCode/"+fname + ".py"


	try:
		execfile(run)
	except:
		print("program failed")
		print("trying again")
		rewrite(fname)
		os.system(run)
		
		


def main():

	fname = "metaCodeTest"

	openFile(fname)

	helloWorld(fname) #write some code in the file

	runProgram(fname) # run file 








if __name__ == '__main__':
    main()
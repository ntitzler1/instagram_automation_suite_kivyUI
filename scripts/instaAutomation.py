""" 
This file contains functions which contain code to interact with instagram

Author: Nick Titzler
"""


#general imports
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



#Gobal Variable List
globalUserList = []
onePhotoLiked = []
twoPhotosLiked = []
threePhotosLiked = []
noPhotosLiked = []
driver = webdriver.Chrome('/usr/local/bin/chromedriver')


"""
~~~~~~~~~~~~~~~~ Selenium Control Functions ~~~~~~~~~~~~~~~~
"""

def likeLoop(userList):
        """
        takes a list of users, the first, third and fourth, and then processes the next user
        """
        time.sleep(3)
        global globalUserList
        global onePhotoLiked
        global twoPhotosLiked
        global threePhotosLiked
        global noPhotosLiked
        onePhotoBool = False
        TwoPhotoBool = False
        ThreePhotoBool = False
        
        # go to profile
        for i in range(len(userList)):
                onePhotoBool = False
                TwoPhotoBool = False
                ThreePhotoBool = False
                if i == 24:
                        print("25 users proccessed")
                elif i == 49:
                        print("50 users proccessed")
                elif i == 99:
                        print("100 users proccessed")
                elif i == 149:
                        print("150 users processed")
                elif i == 199:
                        print("200 users processed")
                elif i == 299:
                        print("300 users processed")
                
                
                try:
                    path = "https://www.instagram.com/" + userList[i] + "/"
                    driver.get(path)
                            
                    # open first pic
                    pic = driver.find_element_by_class_name("_9AhH0")
                    pic.click()

                    # like first pic
                    time.sleep(3)
                    like = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                    time.sleep(2) 
                    like.click()

                    # add user to onePhotoLiked
                    onePhotoLiked.append(userList[i])
                    onePhotoBool = True

                    # tab over
                    time.sleep(3)
                    tab = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
                    time.sleep(2)
                    tab.click()
                    time.sleep(2)
                    tab = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
                    time.sleep(2)
                    tab.click()

                    #like second pic
                    time.sleep(3)
                    like = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                    time.sleep(2) 
                    like.click()

                    # add user to twoPhotosLiked
                    twoPhotosLiked.append(userList[i])
                    TwoPhotoBool = True

                    time.sleep(3)
                    tab = driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a[2]")
                    time.sleep(2)
                    tab.click()
                            
                    time.sleep(4)
                    like = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                    time.sleep(2) 
                    like.click()

                            # add user to three photos liked
                    threePhotosLiked.append(userList[i])
                    ThreePhotoBool = True

                        #add user to global list of users that were successfully processed
                except:
                
                    if ((onePhotoBool == False) and (TwoPhotoBool == False) and (ThreePhotoBool == False)):
                            noPhotosLiked.append(userList[i])
                        
                                
        
                               

def login(user, password, userList):
	"""
	function logs into instagram given a user name and password
	#username.send_keys(user)
        driver.find_element_by_name("username")
	"""
	driver.get("https://www.instagram.com/")
	time.sleep(3)
	username = driver.find_element_by_name("username")
	passwordInput = driver.find_element_by_name("password")
	username.send_keys(user)
	passwordInput.send_keys(password)

	#click login
	time.sleep(3)
	log_cl = driver.find_element_by_class_name("L3NKy")
	log_cl.click()
	time.sleep(4) 

	#wait to call next function
	time.sleep(10)
	likeLoop(userList)


"""
~~~~~~~~~~~~~~~~ User Data Processing Functions ~~~~~~~~~~~~~~~~
"""
def parse(fp):
    """parse file name"""
    li = fp.split('/')
    return li[2][:-4]

def writeOut(client, fileName, userList):
    """
    the client file has this structure:

    Client Name
    Liked followers from accounts: [item,item]
    full user list: [(parentAccount)]
    no photo liked: [(item,parentAccount),(item,parentAccount)]
    one photo liked: [(item,parentAccount),(item,parentAccount)]
    two photo liked: [(item,parentAccount), (item,parentAccount)]
    three photo liked:  [(item,parentAccount), (item,parentAccount)]
    """
    global followers

    if not os.path.exists('../csvFiles/clientFiles/'+client):
        os.makedirs('../csvFiles/clientFiles/'+client)

    save_path = ""
    print("write out")

    f = open("../csvFiles/clientFiles/"+client +"/"+ "directory.txt","r")
    lines = f.readlines()
    f.close()


    with open("../csvFiles/clientFiles/"+client +"/"+ "directory.txt", "w") as f:
            #search for the entry
            finalWrite = []
            for i in range(len(lines)):
                item = lines[i]
                if fileName == lines[i].split(":")[0]:

                    edit = item.split(":")
                    edit[1] = str(len(userList) + int(edit[1]))
                    final = edit[0] + ":" + edit[1] + "\n"
                    finalWrite.append(str(final))
                else:
                    finalWrite.append(item)
            for item in finalWrite:
                f.write(item)



    with open("../csvFiles/clientFiles/"+client +"/"+ "fullUserList.txt", "a") as f:
        for item in userList:
            f.write("("+item +","+fileName+"),")
    
        #with open(os.path.join("../csvFiles/clientFiles/"+client +"/"+ client+".txt"),"w") as f:
    with open("../csvFiles/clientFiles/"+client +"/"+ "onePhotoLiked.txt", "a") as f:
        for item in onePhotoLiked:
            f.write("("+item +","+fileName+"),")
        #f.write(fileName)

    with open("../csvFiles/clientFiles/"+client +"/"+ "twoPhotosLiked.txt", "a") as f:
        for item in twoPhotosLiked:
            f.write("("+item +","+fileName+"),")

        #f.write("\n")
    with open("../csvFiles/clientFiles/"+client +"/"+ "threePhotosLiked.txt", "a") as f:
        for item in threePhotosLiked:
            f.write("("+item +","+fileName+"),")
        
    with open("../csvFiles/clientFiles/"+client +"/"+ "noPhotosLiked.txt", "a") as f:
        for item in noPhotosLiked:
            f.write("("+item +","+fileName+"),")
        
        
    

def checkDir(client, fileName):
    """
    return the number stored in the directory of the index of the last user processed
    """
    if not os.path.exists('../csvFiles/clientFiles/'+client):
        os.makedirs('../csvFiles/clientFiles/'+client)

    if not os.path.isfile("../csvFiles/clientFiles/"+client+"/directory.txt"):
        with open("../csvFiles/clientFiles/"+client+"/directory.txt","w") as f:
            pass

    #open directory.txt
    with open("../csvFiles/clientFiles/"+client +"/"+ "directory.txt", "r") as f:

        lines = f.readlines()
        
        # search dir for fileName
        for item in lines:
            if fileName == item.split(":")[0]:
                x = item.split(":")
                return int(x[1])

    #if item is not present write a new entry to the file with a zero as the number
    f = open("../csvFiles/clientFiles/"+client +"/"+ "directory.txt","a")
    f.write("\n")
    f.write(fileName+":0")
    f.close()
    return 0




        #else: return the number stored at the directory position


"""
~~~~~~~~~~~~~~~~ Argument Processing and Usage ~~~~~~~~~~~~~~~~
"""
def processUserList(arguments):
        """
        Will open CSV file from stdin, returns a the userList
        """
        userList = []
        fileName = "../csvFiles/followerLists/" + arguments
        
        try:

            with open(fileName, "r") as f:
                    allLines = f.readlines()                
                    for item in allLines:
                            userList.append(item.strip("\n"))
        except:
                print(arguments + " is not currently a csv file, now exiting")
                exit()
        
        
        return userList

def usage():
        print("error: fileName not found")
        print("usage: python3 instaAutomation.py clientName username password fileName.csv numToProcess")
        print("~~now exiting~~")
        driver.quit()
        exit()


"""
~~~~~~~~~~~~~~~~ Main Function ~~~~~~~~~~~~~~~~
"""

def main():
        
        start_time = time.time()
        
        args = sys.argv
        try:
            clientName = args[1]
            userName = args[2]
            password = args[3]
            fileName = args[4]
            numProcess = int(args[5])
        except:
            usage()

        
        userList = processUserList(fileName)

        

        #prune userList based on number specified
        prevNum = checkDir(clientName, parse(fileName))
        if len(userList[prevNum:]) < numProcess: 
            numProcess = len(userList)
            ct = len(userList[prevNum:])
        else:
            ct = numProcess

        userList = userList[prevNum:numProcess+prevNum]


        print("~~~~~~~~~~~~~ Now Running ~~~~~~~~~~~~~")
        print("   client:", clientName)
        print("   on followers:", fileName)
        print("   count to process:", ct)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # run function
        login(userName, password, userList)
        
        # write out
        writeOut(clientName, parse(fileName), userList)

        # Print photo arrays
        print("One Photo Liked:",len(onePhotoLiked))
        print("Two Photos Liked:",len(twoPhotosLiked))
        print("Three Photos Liked:",len(threePhotosLiked))
        print("No Photos Liked: ",len(noPhotosLiked))

        timer = time.time() - start_time
        print("---",numProcess," users processed in ", timer/60," minutes")
        
        print("~~~ now exiting ~~~~")
        driver.quit()
        
        

if __name__ == '__main__':
    main()


""" 
Functions that pull instagram followers from a given profile, and save them into a CSV

Author: Nick Titzler
"""

#general imports
import time
import sys
import os
from multiprocessing import Process


#selenium binding variables
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



#Gobal Variable List
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
followers =[]

"""
~~~~~~~~~~~~~~~~ Selenium Control Functions ~~~~~~~~~~~~~~~~
"""

# code adapted from: 
def pullFollowers(profileToBeAccessed, max):
    test = 0
    driver.get('https://www.instagram.com/' + profileToBeAccessed)
    followersLink = driver.find_element_by_css_selector('ul li a')
    followersLink.click()
    time.sleep(2)
    followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
    followersList.click()
    actionChain = webdriver.ActionChains(driver)
    while (numberOfFollowersInList < max):
        if test < 6:
            nesClick = driver.find_element_by_xpath('/html/body/div[4]/div/div')
            nesClick.click()
        test+=1
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
        print(numberOfFollowersInList)
        
    global followers
    for user in followersList.find_elements_by_css_selector('li'):
        userLink = user.find_element_by_css_selector('a').get_attribute('href')
        #print(userLink)
        followers.append(userLink)
        if (len(followers) == max):
            break
    return followers



                

def login(user, password, profileToBeAccessed, numProcess):
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
	time.sleep(2)
	res = pullFollowers(profileToBeAccessed, numProcess)
    



"""
~~~~~~~~~~~~~~~~ User Data Processing Functions ~~~~~~~~~~~~~~~~
"""

def writeOut(profile):
        """ will write out followers into a CSV """
        global followers
        save_path = ""
        print("write out")
        with open(os.path.join("../csvFiles/followerLists/" +profile[:len(profile)]+"Followers.txt"),"w") as f:
            for user in followers:
                f.write(user[26:len(user)-1]+"\n")



"""
~~~~~~~~~~~~~~~~ Argument Processing and Usage ~~~~~~~~~~~~~~~~
"""

def usage():
        print("error!")
        print("usage: python3 [insta profile link or username] [OPTION: num followers to pull] [category]")
        print("~~now exiting~~")
        exit()


"""
~~~~~~~~~~~~~~~~ Main Function ~~~~~~~~~~~~~~~~
"""

def main():
        userName = "johnsfunart"
        password = "77Kinder!"
        start_time = time.time()
        loginFailed = 0
        
        #takes given link or specifc user name
        print("lenProfile to be accessed:",sys.argv[1][:26])
        if len(sys.argv) < 2:
            usage()
        elif sys.argv[1][:26] == "https://www.instagram.com/":
            profileToBeAccessed = sys.argv[1]
            profileToBeAccessed = profileToBeAccessed[26:len(profileToBeAccessed) - 1]
        else:
            profileToBeAccessed = sys.argv[1]


        numProcess = 500 #default
        if len(sys.argv) == 3:
            numProcess = int(sys.argv[2])
        
        print("~~~~~~~~~~~~~ Now Running pullFollowers ~~~~~~~~~~~~~")
        print("   Account Pulling:",userName)
        print("   From user:",profileToBeAccessed)
        print("   Pulling Num:",numProcess)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        

        try:
            login(userName, password, profileToBeAccessed + "/", numProcess)
        except:
            loginFailed = 1

        if loginFailed:
            try:
                login(userName, password, profileToBeAccessed + "/", numProcess)
            except:
                print("total failure, try again")
                exit()

        writeOut(profileToBeAccessed)
        


        timer = time.time() - start_time
        print("---",numProcess," users processed in ", timer/60," minutes")
        
        driver.quit()
        
        

if __name__ == '__main__':
    main()


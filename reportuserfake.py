import time
import requests
import random 
import string
import re

import sys
import os, platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

servers=[
"35.196.231.162",
"34.83.203.177",
]

capabilities = {
    "browserName": "chrome",
    "version": "80.0",
    "enableVNC": True,
    "enableVideo": False
}

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# if platform.system() == 'Windows':
# 	chromepath = BASE_DIR + r'\chromedriver.exe'
# 	chromepath = chromepath.replace("\\","/")
# options = Options()
# driver = webdriver.Chrome(executable_path=chromepath,)

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agent = user_agent_rotator.get_random_user_agent()

def commented():
	chrome_options = Options()
	# options.add_argument(f'--proxy-server={self.proxy}')


	chrome_options.add_argument("user-agent="+user_agent+"")
	driver = webdriver.Remote(
		command_executor="http://"+ servers[0] +":4444/wd/hub",
		desired_capabilities=capabilities,
		options=chrome_options
		)

	driver.implicitly_wait(55)
	driver.set_page_load_timeout(55)
	print("BROWSER STARTED")



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if platform.system() == 'Windows':
	chromepath = BASE_DIR + r'\chromedriver.exe'
	chromepath = chromepath.replace("\\","/")
options = Options()
#options.add_argument(f'--proxy-server={self.proxy}')
options.add_argument("user-agent=" + user_agent + "")
driver = webdriver.Chrome(executable_path=chromepath, 
# options=options
)

driver.implicitly_wait(55)
driver.set_page_load_timeout(55)

print("BROWSER STARTED")

#The easiest way to hide the browser is to install PhantomJS.
#driver = webdriver.PhantomJS()

url = ""
user_email = ""
user_pass = ""
waitTime = 10


class FbReportUserProfile:

	def __init__(self, driver,url,email,password):
		self.driver = driver
		self.url = url
		self.email = email
		self.password = password

	def navigate(self,url):
		self.driver.get(url)

	def login(self,email,password,driver):
		try:
			emailelement = self.driver.find_element_by_name('email')
			passwordelement = self.driver.find_element_by_name('pass')
			emailelement.send_keys(self.email)
			time.sleep(3)
			passwordelement.send_keys(self.password)
			time.sleep(3)
			#logging in to the facebook using Selenium
			emailelement.send_keys(Keys.RETURN)

		except Exception as inst:
			print (type(inst))     # the exception instance
			print( inst.args)      # arguments stored in .args
			print( inst )
			print ("Please check your credential again.")

'''
	def browserWaitUntilForConditon(self,driver,time):
		try:
			element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.ID, "events_birthday_view")))
		except:
			print "Couldn't find birthday page, Please check the url"
			driver.quit()
'''

#Navigating to the url
fbReportUserProfile = FbReportUserProfile(driver,url,user_email,user_pass)
fbReportUserProfile.navigate(url)

# Logging in facebook by using email and password
fbReportUserProfile.login(user_email,user_pass,driver)
#facebookBirthdayWishes.browserWaitUntilForConditon(driver,waitTime)

time.sleep(10)
driver.find_element_by_xpath("//*[@id=\"u_0_10\"]/i").click()
driver.find_element_by_xpath("//*[@id=\"u_0_y\"]/div/ul/li[2]/a/span/span").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id=\"nfxQuestionNamedaccount\"]/label[1]").click()
driver.find_element_by_xpath("//*[@id=\"nfx_dialog_continue\"]").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id=\"nfxQuestionNamedfake\"]/label[1]").click()
driver.find_element_by_xpath("//*[@id=\"nfx_dialog_continue\"]").click()

time.sleep(2)
elemFound = driver.find_element_by_xpath("//a[@href='#'][@rel='async-post']")
ActionChains(driver).click(elemFound).perform()
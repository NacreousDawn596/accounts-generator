from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random, os, sys

def gen(file="credentials.txt"):
	options = webdriver.ChromeOptions()
	
	driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
	actions = ActionChains(driver)
	actions2 = ActionChains(driver)
	actions3 = ActionChains(driver)
	driver.get("https://discord.com/register")
	try:
	 driver.find_element("xpath", '/html/body/div/div[2]/div/div/form/div/div/div[1]/div[1]/div[2]').click() # Check if the register with phone number window appears
	except:
	  pass
	
	
	
	sleep(2)
	
	username = random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
	email = random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + '@' + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") +  '.' + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") 
	password = random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
	
	year = ['//*[@id="react-select-4-option-11"]', '//*[@id="react-select-4-option-12"]', '//*[@id="react-select-4-option-13"]', '//*[@id="react-select-4-option-14"]', '//*[@id="react-select-4-option-15"]', '//*[@id="react-select-4-option-16"]', '//*[@id="react-select-4-option-17"]', '//*[@id="react-select-4-option-18"]', '//*[@id="react-select-4-option-19"]', '//*[@id="react-select-4-option-20"]', '//*[@id="react-select-4-option-21"]', '//*[@id="react-select-4-option-22"]', '//*[@id="react-select-4-option-23"]', '//*[@id="react-select-4-option-24"]', '//*[@id="react-select-4-option-25"]', '//*[@id="react-select-4-option-26"]', '//*[@id="react-select-4-option-27"]', '//*[@id="react-select-4-option-28"]', '//*[@id="react-select-4-option-29"]', '//*[@id="react-select-4-option-30"]']
	
	months = ['//*[@id="react-select-2-option-0"]', '//*[@id="react-select-2-option-1"]', '//*[@id="react-select-2-option-2"]', '//*[@id="react-select-2-option-3"]', '//*[@id="react-select-2-option-4"]', '//*[@id="react-select-2-option-5"]', '//*[@id="react-select-2-option-6"]', '//*[@id="react-select-2-option-7"]', '//*[@id="react-select-2-option-8"]', '//*[@id="react-select-2-option-9"]', '//*[@id="react-select-2-option-10"]', '//*[@id="react-select-2-option-11"]']
	monthwords = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augustus', 'September', 'October', 'November', 'December']
	day = ['//*[@id="react-select-3-option-0"]', '//*[@id="react-select-3-option-1"]', '//*[@id="react-select-3-option-2"]', '//*[@id="react-select-3-option-3"]', '//*[@id="react-select-3-option-4"]', '//*[@id="react-select-3-option-5"]', '//*[@id="react-select-3-option-6"]', '//*[@id="react-select-3-option-7"]', '//*[@id="react-select-3-option-8"]', '//*[@id="react-select-3-option-9"]', '//*[@id="react-select-3-option-10"]', '//*[@id="react-select-3-option-11"]', '//*[@id="react-select-3-option-12"]', '//*[@id="react-select-3-option-13"]', '//*[@id="react-select-3-option-14"]', '//*[@id="react-select-3-option-15"]', '//*[@id="react-select-3-option-16"]', '//*[@id="react-select-3-option-17"]', '//*[@id="react-select-3-option-18"]', '//*[@id="react-select-3-option-19"]', '//*[@id="react-select-3-option-20"]', '//*[@id="react-select-3-option-21"]', '//*[@id="react-select-3-option-22"]', '//*[@id="react-select-3-option-23"]', '//*[@id="react-select-3-option-24"]', '//*[@id="react-select-3-option-25"]', '//*[@id="react-select-3-option-26"]', '//*[@id="react-select-3-option-27"]']
	
	driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[1]/div/input').click()
	driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[1]/div/input').send_keys(email)
	
	driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[2]/div/input').click()
	driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[2]/div/input').send_keys(username)
	
	driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[3]/div/input').click()
	driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[3]/div/input').send_keys(password)
	
	driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[1]").click()
	driver.find_element("xpath", random.choice(months)).click()
	actions.send_keys(Keys.ENTER)
	sleep(1)
	driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[2]").click()
	driver.find_element("xpath", random.choice(day)).click()
	actions.send_keys(Keys.ENTER)
	sleep(1)
	driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[3]").click()
	driver.find_element("xpath", random.choice(year)).click()
	actions.send_keys(Keys.ENTER)
	sleep(1)
	#actions.perform()
	
	try:
	  driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/label/input').click()
	except:
	  pass
	driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[6]/button').click()
	
	input('can you please fill the captcha and press enter when finished?')
	
	token = driver.execute_script('location.reload();var i=document.createElement("iframe");document.body.appendChild(i);return i.contentWindow.localStorage.token').strip('"') # Get the token
	
	
	sleep(5)
	
	print(f'''email: {email}
password: {password}
username: {username}:
token: {token}
saved in: {file}

-----------------------------------------------------------------------------------------------------------
	''')
	os.system(f'echo "{email}:{password}:{username}:{token}" >> {file}')
	
	sleep(5)
	driver.close()

if __name__ == "__main__":
	for i in range(0, int(sys.argv[1])):
		try: gen(sys.argv[2])
		except: gen()

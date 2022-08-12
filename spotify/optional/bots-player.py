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
from random import choice
from json import loads
from argparse import ArgumentParser


class botplayer():
	def __init__(self, driver):
		self.options = webdriver.ChromeOptions()
		self.options.headless = False
		self.options.add_experimental_option('excludeSwitches', ['disable-component-update'])
		self.driver = webdriver.Chrome(options=self.options, executable_path=driver)
		self.actions = ActionChains(self.driver)
		self.actions2 = ActionChains(self.driver)
		self.actions3 = ActionChains(self.driver)
		self.status = self.status(self.driver)

	def login(self, email, password):
		self.driver.get("https://accounts.spotify.com/en/login/")
		sleep(1)
		self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input").click()
		self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input").send_keys(email)
		self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/input").click()
		self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/input").send_keys(password)
		self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]/button").click()
		return self.driver

	class status:
		def __init__(self, driver):
			self.driver = driver
			self.webplayer = self.webplayer(self.driver)
		class webplayer():
			def __init__(self, driver):
				self.driver = driver
			def init(self):
				self.driver.find_element("xpath", "/html/body/div/div/div[2]/div/div/button[2]").click()
			def search(self, keyword):
				self.driver.find_element("xpath", "/html/body/div[4]/div/div[2]/nav/div[1]/ul/li[2]/a").click()
				sleep(2)
				self.driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input").click()
				self.driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input").send_keys(keyword)
				self.driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input").send_keys(Keys.ENTER)
				sleep(5)
				self.driver.find_element("xpath", '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div').click()
				#self.driver.find_element("xpath", '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/button').click()

if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument('--file', nargs='?', const=1, type=str, default="credentials.txt")
	parser.add_argument('-n', nargs='?', const=1, type=int, default="1")
	parser.add_argument('--driver', nargs='?', const=1, type=str, default="chromedriver")
	data = parser.parse_args()
	user_player = botplayer(data.driver)
	account = choice(loads(open(data.file, "r").read()))
	user_player.login(account["email"], account["password"])
	sleep(5)
	user_player.status.webplayer.init()
	sleep(5)
	user_player.status.webplayer.search("happy slutter")

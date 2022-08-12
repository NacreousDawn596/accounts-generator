import os

class Setup:
	def __init__(self, requirements="./requirements.txt"):
		os.system("sudo apt-get install wget")
		self.install = self.install(requirements)
	def clear(self):
		os.system("clear")
	class install:
		def __init__(self, requirements):
			self.req = requirements
		def python_libs(self):
			os.system(f"python3 -m pip install -r {self.req}")
		def chromedriver(self):
			version = os.popen("chromium --version").read().split()[1]
			os.system(f"wget https://chromedriver.storage.googleapis.com/{version}/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip")
			for path in os.popen("find ./ -type d").read().splitlines():
				os.system(f"cp chromedriver {path}")

if __name__ == "__main__":
	setup = Setup()
	setup.clear()
	setup.install.python_libs()
	setup.clear()
	setup.install.chromedriver()
	setup.clear()
	print("done!")

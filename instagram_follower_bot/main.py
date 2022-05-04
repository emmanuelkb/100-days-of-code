import time

from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "emmanuel_kb"
USERNAME = "emmanuel_kb_auto"
PASSWORD = "X3'6RPQ?^-CMnEe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.instagram.com/accounts/login/")
# element = driver.find_element_by_name("passwd")
time.sleep(10)
username = driver.find_element(by=By.NAME, value="username")
username.send_keys(USERNAME)

exit()



class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()






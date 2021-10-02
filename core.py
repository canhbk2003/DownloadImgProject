import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SCROLL_PAUSE_TIME = 0.5

local_folder = ""

driver = webdriver.Chrome()

class Config:
    def __init__(self):
        self.localFolder = ""
        self.uploadUrl = ""

    @property
    def local_folder(self):
        return self.localFolder

    @local_folder.setter
    def local_folder(self, folder):
        self.localFolder = folder

    @property
    def upload_url(self):
        return self.uploadUrl

    @upload_url.setter
    def upload_folder(self, uri):
        self.upload_url = uri

def scroll_down():

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def upload(local_foler):
    pass

def like():
    rand = random.randint(0, 100)
    img = driver.find_element_by_xpath('//*[@id="productDiv-Wall Art"]/a[{}]/img' %rand)

def findAllProduct():
    all = []
    all.append(driver.find_element_by_class_name('productDiv'))
    return all

def login(user, password):
    driver.get("https://fineartamerica.com/")
    button = driver.find_element_by_xpath('//*[@id="menuTopLogin"]/a')
    button.click()
    button = driver.find_element_by_xpath('//*[@id="maindiv"]/div/a[3]')
    button.click()
    edituser = driver.find_element_by_xpath('//*[@id="username"]')
    edituser.clear()
    edituser.send_keys(user)
    editpassword = driver.find_element_by_xpath('//*[@id="password"]')
    editpassword.clear()
    editpassword.send_keys(password)
    button = driver.find_element_by_xpath('//*[@id="logincollector"]/div/div[3]/a')
    button.click()
    home = driver.find_element_by_xpath('//*[@id="headerLogoImage"]')
    home.click()
    scroll_down()
    driver.refresh()
    #driver.close()

    a = []
    a = findAllProduct()
    print(len(a))

    #findAllProduct()
    # config = Config()
    # config.local_folder = "D:"
    # print(config.local_folder)

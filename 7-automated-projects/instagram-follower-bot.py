from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os, time
USERNAME = os.environ('USERNAME')
PASSWORD = os.environ('PASSWORD')
TARGET_ACCOUNT = 'chefsteps'
CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'

class InstaFollower:
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
  
  def login(self):
    self.driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)
    username = self.driver.find_element_by_name('username')
    username.send_keys(USERNAME)
    password = self.driver.find_element_by_name('password')
    password.send_keys(PASSWORD, Keys.ENTER)

  def find_followers(self):
    self.driver.get(f'https://www.instagram.com/{TARGET_ACCOUNT}/')
    time.sleep(5)
    followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a/div')
    followers.click()
    time.sleep(3)
    scroll = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
    for i in range(10):
      self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll)
      time.sleep(2)
    
  def follow(self):
    total = self.driver.find_elements_by_css_selector('li button')
    for button in total:
      try:
        button.click()
        time.sleep(1)
      except ElementClickInterceptedException:
        cancel = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        cancel.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time
USERNAME = 'wiiburcult'
PASSWORD = '615twitter'
CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'

class TwitterBot:
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    self.down = 150
    self.up = 50
  
  def get_internet_speed(self):
    self.driver.get('https://www.speedtest.net/')
    time.sleep(5)
    go_button = self.driver.find_element_by_css_selector('.start-button a')
    go_button.click()
    time.sleep(60)

    download = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
    upload = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
    time.sleep(3)
    self.driver.quit()
    return [download, upload]

  def tweet(self, speed, dirn):
    self.driver.get('https://twitter.com/i/flow/login')
    time.sleep(8)

    # login
    username = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(USERNAME, Keys.ENTER)
    time.sleep(5)
    password = self.driver.find_element_by_name('password')
    password.send_keys(PASSWORD, Keys.ENTER)
    time.sleep(8)

    # tweeting
    tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
    tweet_button.click()
    time.sleep(5)
    tweet = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
    tweet.send_keys(f'Hey Internet Provider, why is my internet speed {speed}{dirn} when I pay for {self.dirn}{dirn}?')
    time.sleep(3)
    send_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
    send_button.click()
    time.sleep(5)
    self.driver.quit()


bot = TwitterBot()
while True:
  speed = bot.get_internet_speed()
  if speed[0] < bot.down:
    bot.tweet(speed[0], 'down')
  elif speed[1] < bot.up:
    bot.tweet(speed[1], 'up')
  else:
    continue

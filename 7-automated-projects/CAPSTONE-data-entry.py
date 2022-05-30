from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time
CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'

class RentalListings:
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER)

  def get_listings(self, website):
    self.driver.get(website)
  
  def fill_form(self, form):
    self.driver.get(form)

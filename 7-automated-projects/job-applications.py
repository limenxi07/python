from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os, time
USERNAME = os.environ('USERNAME')
PASSWORD = os.environ('PASSWORD')
PHONE = os.environ('PHONE')

CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
driver.get('placeholder')

# sign in to linkedin account
sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()
time.sleep(5)
username_entry = driver.find_element_by_id('username')
username_entry.send_keys(USERNAME)
password_entry = driver.find_element_by_id('password')
password_entry.send_keys(PASSWORD)
password_entry.send_keys(Keys.ENTER)
time.sleep(5)

# submit job application
listings = driver.find_elements_by_css_selector('.job-card-container--clickable')
for listing in listings:
  listing.click()
  time.sleep(3)

  try: 
    apply = driver.find_element_by_css_selector('.jobs-s-apply button')
    apply.click()
    time.sleep(5)
    phone = driver.find_element_by_class_name('fb-single-line-text__input')
    if phone.text == '':
      phone.send_keys(PHONE)
    submit = driver.find_element_by_css_selector('footer button')

    # check for simple application process
    if submit.get_attribute('data-control-name') == 'continue_unify':
      close = driver.find_element_by_class_name('artdeco-modal__dismiss')
      close.click()
      time.sleep(3)
      discard = driver.find_element_by_class_name('artdeco-modal__confirm-dialog-btn')[1]
      discard.click()
      continue
    else:
      submit.click()
    
    # close application window
    time.sleep(3)
    close = driver.find_element_by_class_name('artdeco-modal__dismiss')
    close.click()

  except NoSuchElementException:
    continue

time.sleep(5)
driver.quit()
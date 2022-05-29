from selenium import webdriver
from selenium.webdriver.common.keys import Keys
CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)

driver.get('https://www.amazon.com/dp/B0863TXGM3?ref_=cm_sw_r_cp_ud_dp_D3A277PAJEA3B0E5JS99')
price = driver.find_element_by_id('priceblock-ourprice').get_attribute('placeholder')
price.click()
price.send_keys('sadfhjlaksdjf') # to type something into input
price.send_keys(Keys.ENTER) # to enter the search
driver.quit()
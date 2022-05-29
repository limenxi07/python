from selenium import webdriver
import time
CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')
items = [item.get_attribute('id') for item in driver.find_elements_by_css_selector('#store div')]
check_time = time.time() + 5

while True:
  cookie.click()
  if time.time() > check_time: # every 5s

    # get cookie count
    money = driver.find_element_by_id('money').text
    if ',' in money:
      cookie_count = int(money.replace(',', ''))

    # formatting item prices
    upgrades = {}
    item_prices = []
    all_prices = driver.find_elements_by_css_selector('#store b')
    for price in all_prices:
      if price.text != '':
        item_prices.append(price.text.split('-')[1].strip().replace(',', ''))
    for i in range(len(item_prices)):
      upgrades[item_prices[i]] = items[i]
    
    # purcahse upgrades
    buy_upgrades = {}
    for cost, id in upgrades.items():
      if cookie_count > cost:
        buy_upgrades[cost] = id
    buy_id = buy_upgrades[max(buy_upgrades)]
    driver.find_element_by_id(buy_id).click()

    check_time = time.time() + 5
  
  if time.time() > (time.time() + 60*5):
    print(driver.find_element_by_id('cps').text)
    break

driver.quit()
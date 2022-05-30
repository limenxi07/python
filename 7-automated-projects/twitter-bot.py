from selenium import webdriver
CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
driver.get('https://twitter.com/i/flow/login')

username = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

driver.quit()
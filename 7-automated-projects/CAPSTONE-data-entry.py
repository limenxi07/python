from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, time
CHROMEDRIVER = '/Users/limenxi/Documents/vscode/chromedriver'

class RentalListings:
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    self.links = []
    self.prices = []
    self.addresses = []


  def get_listings(self, website):
    response = requests.get(website, headers={
      'Accept-Language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    })
    soup = BeautifulSoup(response.text, 'html.parser')

    all_links = [link.get('href') for link in soup.select('li .list-card-top a')]
    for link in all_links:
      if 'http' not in link:
        link = 'https://www.zillow.com' + link
        self.links.append(link)
      else:
        self.links.append(link)

    all_prices = [price.getText() for price in soup.select('li .list-card-price')]
    for price in all_prices:
      if '+' in price:
        self.prices.append(price.split('+')[0])
      elif '/' in price:
        self.prices.append(price.split('/')[0])

    all_addresses = [address.getText() for address in soup.select('li .list-card-addr')]
    for address in all_addresses:
      if '|' in address:
        self.addresses.append(address.split('|')[1])
      else:
        self.addresses.append(address)
  

  def fill_form(self, form):
    self.driver.get(form)
    time.sleep(5)
    for i in range(len(self.addresses) - 1):
      try:
        address_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(self.addresses[i])
        price_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(self.prices[i])
        link_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(self.links[i])
        submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click()
        time.sleep(5)
        resubmit = self.driver.find_element_by_link_text('Submit another response')
        resubmit.click()
        time.sleep(5)
      except IndexError:
        break


bot = RentalListings()
bot.get_listings('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D')
bot.fill_form('https://forms.gle/6LkCBoEpc1e6Cors7')
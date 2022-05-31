import requests, smtplib, os
from bs4 import BeautifulSoup
PRODUCT_URL = 'https://www.amazon.com/dp/B0863TXGM3?ref_=cm_sw_r_cp_ud_dp_D3A277PAJEA3B0E5JS99'
PRODUCT_NAME = 'Sony Headphones'
PRICE_THRESHOLD = '300'
EMAIL = os.environ.get("EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# obtain regular price
response = requests.get(PRODUCT_URL, headers={
  'Accept-Language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}) # browser headers obtained from http://myhttpheader.com/
soup = BeautifulSoup(response.text, 'lxml')
price = int(soup.select_one('div div table td span .a-offscreen').getText()[1:].split('.')[0])
title = soup.select_one('#title #productTitle').getText()


# email alert
if price <= PRICE_THRESHOLD:
  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=EMAIL_PASSWORD)
    connection.sendmail(
      from_addr=EMAIL,
      to_addrs=EMAIL,
      msg=f'Subject: Amazon Price Alert for {PRODUCT_NAME}!\n\n{title} is now ${price}!\n{PRODUCT_URL}'
    )
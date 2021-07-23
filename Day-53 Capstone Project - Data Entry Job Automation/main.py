import time
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# BeautifulSoup
# Scrape data from zillow
url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
      "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122" \
      ".30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22" \
      "%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D" \
      "%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price" \
      "%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom" \
      "%22%3A12%7D "

header = {
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.107 Safari/537.36",
}

response = requests.get(url=url, headers=header)
zillow_website = response.text

soup = BeautifulSoup(zillow_website, "html.parser")
lists = soup.find_all(name="a", class_="list-card-link list-card-link-top-margin")
link_list = [i.get("href") for i in lists]
for i in range(len(link_list)):
    if not link_list[i].startswith("https"):
        link_list[i] = "https://www.zillow.com" + link_list[i]
pprint(link_list)

price_list = soup.find_all(name="div", class_="list-card-price")
price = [i.getText() for i in price_list]
pprint(price)

addr_list = soup.find_all(name="address", class_="list-card-addr")
address = [i.getText() for i in addr_list]
pprint(address)

# SELENIUM
# Create spreadsheet using google form
CHROME_WEBDRIVER_PATH = "D:\Development/chromedriver.exe"
driver = webdriver.Chrome(CHROME_WEBDRIVER_PATH)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfPTLvM5hJg4Mn1hyCHKnCVbj_Os2hxcpQGVxXyDBtRsL3cbw/viewform?usp"
           "=sf_link")

for i in range(7):
    time.sleep(1)
    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address[i])
    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price[i])
    link_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link_list[i])
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()
    time.sleep(1)
    submit_another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response.click()

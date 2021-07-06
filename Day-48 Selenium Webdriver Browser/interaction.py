from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_webdriver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element_by_css_selector("#articlecount a")
# count.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

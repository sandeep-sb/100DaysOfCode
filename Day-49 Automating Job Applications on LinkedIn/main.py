from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_webdriver_path = "D:\Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_webdriver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

driver.implicitly_wait(5)

signin = driver.find_element_by_class_name("nav__button-secondary")
signin.click()

driver.implicitly_wait(5)

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

easy_apply = driver.find_element_by_class_name("jobs-apply-button--top-card")
easy_apply.click()

driver.implicitly_wait(5)

phone_number = driver.find_element_by_tag_name("input")
phone_number.send_keys(PHONE_NUMBER)
next_button = driver.find_element_by_class_name("artdeco-button artdeco-button--2 artdeco-button--primary ember-view")

driver.implicitly_wait(3)
next_button.click()

driver.implicitly_wait(2)
next_button.click()

driver.implicitly_wait(2)
review = driver.find_element_by_class_name("artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
review.click()

submit_application = driver.find_element_by_class_name(
    "artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
submit_application.click()

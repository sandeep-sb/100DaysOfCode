from selenium import webdriver

chrome_webdriver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("ABCDEFG")
l_name = driver.find_element_by_name("lName")
l_name.send_keys("XYZ")
e_mail = driver.find_element_by_name("email")
e_mail.send_keys("ABCXYZ@gmail.com")
submit_button = driver.find_element_by_class_name("btn")
submit_button.click()

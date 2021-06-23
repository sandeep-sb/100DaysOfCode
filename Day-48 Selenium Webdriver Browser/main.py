from selenium import webdriver
chrome_webdriver_path = "D:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_webdriver_path)
driver.get("https://www.python.org/")
# # price = driver.find_element_by_id("priceblock_ourprice")
# # print(price.text)
#
# # search_bar = driver.find_element_by_name("q")
# # print(search_bar.get_attribute("role"))
#
# # documentaion_link = driver.find_element_by_css_selector(".documentation-widget a")
# # print(documentaion_link.text)
#
# jobs_link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[1]/div[4]/p[2]/a')
# print(jobs_link.text)

events_dates = driver.find_elements_by_css_selector(".event-widget time")
events_names = driver.find_elements_by_css_selector(".event-widget li a")
event = {}
for n in range(len(events_dates)):
    event[n] = {
        "time": events_dates[n].text,
        "name": events_names[n].text,
    }
print(event)


driver.quit()

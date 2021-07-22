from datetime import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

tryTime = 2

CHROME_WEBDRIVER_PATH = "D:\Development/chromedriver.exe"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(5)
        username = self.driver.find_element_by_name("username")
        username.send_keys("instaaccount")
        password = self.driver.find_element_by_name("password")
        password.send_keys("somerandompassword")
        log_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        log_in.click()

        self.driver.implicitly_wait(5)
        dont_save_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        dont_save_info.click()
        dont_save_info_2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        dont_save_info_2.click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps/')
        self.driver.implicitly_wait(5)
        followers_list = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_list.click()
        self.driver.implicitly_wait(5)

    def follow(self):
        f_body = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < 5:  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       f_body)
            self.driver.implicitly_wait()
            scroll += 1

        f_list = self.driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        print("fList len is {}".format(len(f_list)))

        print("ended")
        # self.driver.execute_script("window.scrollBy(0,2000)", "")
        # follow_button = self.driver.find_element_by_name("Follow")


bot = InstaFollower(CHROME_WEBDRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

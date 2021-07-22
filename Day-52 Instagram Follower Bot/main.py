import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
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

        modal = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        print(modal.text)
        for i in range(5):  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', modal)
            time.sleep(2)

    def follow(self):
        for i in range(1, 50):
            follow_buttons = self.driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button')
            try:
                follow_buttons.click()
                time.sleep(2)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_WEBDRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

from selenium import webdriver

chrome_webdriver_path = "D:\Development/chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.implicitly_wait(5)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        self.driver.implicitly_wait(45)

        self.driver.find_element_by_link_text("Back to test results").click()
        download_speed = self.driver.find_element_by_class_name("download-speed")
        self.down = download_speed.text
        upload_speed = self.driver.find_element_by_class_name("upload-speed")
        self.up = upload_speed.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.driver.implicitly_wait(3)
        username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys("sandeepsb04")
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys("8303608402")
        self.driver.implicitly_wait(2)
        log_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        log_in.click()

        compose_tweet = self.driver.find_element_by_class_name("public-DraftStyleDefault-ltr")
        compose_tweet.send_keys(
            f"Hey Internet Provider, my internet speed is {self.down}down/{self.up}up.  \n\n**This is a tweet by a bot**")
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()


bot = InternetSpeedTwitterBot(chrome_webdriver_path)
bot.get_internet_speed()
bot.tweet_at_provider()


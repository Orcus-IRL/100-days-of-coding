# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
#
# class Internet_speed_twitter_bot:
#     def __init__(self):
#         self.up_speed = None
#         self.down_speed = None
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_experimental_option("detach", True)
#         self.driver = webdriver.Chrome(chrome_options)
#         self.up = 150
#         self.down = 50
#
#     def get_internet_speed(self):
#         self.driver.get("https://www.speedtest.net/")
#         self.driver.find_element(By.CLASS_NAME, 'start-button').click()
#         time.sleep(100)
#         self.down_speed = self.driver.find_element(By.XPATH,
#                                                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
#         print("down:", self.down_speed)
#         self.up_speed = self.driver.find_element(By.XPATH,
#                                                  '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
#         print("up:", self.up_speed)
#
#     def tweet_at_provider(self):
#         self.driver.get("https://twitter.com/i/flow/login")
#         time.sleep(5)
#
#         username_entry = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
#         username_entry.click()
#         time.sleep(3)
#         username_entry.send_keys("tester12108", Keys.ENTER)
#
#         time.sleep(10)
#         password_entry = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
#         password_entry.click()
#         time.sleep(3)
#         password_entry.send_keys("Vijay@12345", Keys.ENTER)
#
#         time.sleep(10)
#         content = self.driver.find_element(By.XPATH,
#                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
#         time.sleep(3)
#         content.click()
#         message = "Hey Internet Provider, why is my internet speed", self.down_speed, "down/", self.up_speed, "up when i pay for", self.down, "down/", self.up, "up?"
#         print(message)
#         content.send_keys(message)
#         time.sleep(3)
#         tweet_button = self.driver.find_element(By.XPATH,
#                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
#         tweet_button.click()
#
#
# bot = Internet_speed_twitter_bot()
# bot.get_internet_speed()
# time.sleep(10)
# bot.tweet_at_provider()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()
        # time.sleep(3)

        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

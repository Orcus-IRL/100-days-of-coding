import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

similar_account = ""
username = ""
password = ""


class Insta_follower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        # username section
        uname_box = self.driver.find_element(By.CLASS_NAME,"_aa48")  # click the label of the input box if you want to type in the box
        uname_box.click()
        uname_box.send_keys(username, Keys.TAB)
        # password section
        pword_box = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label')  # click the label of the input box if you want to type in the box
        pword_box.click()
        pword_box.send_keys(password, Keys.ENTER)

        # clicking not now(save info) button
        time.sleep(8)
        si_not_now = self.driver.find_element(By.CLASS_NAME, "_ac8f")
        si_not_now.click()

        # click not now(turn on notification) button
        time.sleep(3)
        button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers/")
        time.sleep(5)

        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="._aano button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)

            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                time.sleep(1.1)


start = Insta_follower()
start.login()
time.sleep(2)
start.find_followers()
time.sleep(2)
start.follow()

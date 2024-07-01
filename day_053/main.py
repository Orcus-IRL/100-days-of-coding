import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
forms_link = 'forms link'


class DataEntry:
    def __init__(self):
        self.links = None
        self.prices = None
        self.address = None

    def scraping_data(self):
        response = requests.get(url='https://appbrewery.github.io/Zillow-Clone/')
        website_html = response.text
        soup = BeautifulSoup(website_html, "html.parser")

        # address
        all_address = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
        self.address = [str(addr.getText()).strip().replace("|", "") for addr in all_address]

        # price
        all_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        self.prices = [str(price.getText())[:6] for price in all_prices]

        # links
        all_links = soup.find_all(name='a', class_="StyledPropertyCardDataArea-anchor")
        self.links = [link.get("href") for link in all_links]

    def filling_forms(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)

        for n in range(len(self.links)):
            driver.get(forms_link)

            # address bar
            address_content = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(2)
            address_content.click()
            address_content.send_keys(self.address[n])

            # price bar
            price_content = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(1)
            price_content.click()
            price_content.send_keys(self.prices[n])

            # link bar
            link_content = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(1)
            link_content.click()
            link_content.send_keys(self.links[n])

            # submit button
            submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            time.sleep(1)
            submit_button.click()


DE = DataEntry()
DE.scraping_data()
time.sleep(2)
DE.filling_forms()

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

# menu = driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
event_time = driver.find_elements(By.CSS_SELECTOR, value='.last time')
event_time_list = []
for i in event_time:
    event_time_list.append(i.text)
# print(event_time_list)

event_data_list = []
for i in range(1):
    one = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
    event_data_list.append(one.text)
    two = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a')
    event_data_list.append(two.text)
    three = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/a')
    event_data_list.append(three.text)
    four = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/a')
    event_data_list.append(four.text)
    five = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/a')
    event_data_list.append(five.text)
# print(event_data_list)


events = {}
for n in range(len(event_time_list)):
    events[n] = {
        "time":event_time_list[n],
        "event":event_data_list[n]
    }
print(events)
# driver.close() #close only a single tab
driver.quit()  # close the entire selenium
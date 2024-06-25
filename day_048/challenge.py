from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Paul")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("walker")

email = driver.find_element(By.NAME, "email")
email.send_keys("paulwalker@gmail.com", Keys.ENTER)



# driver.close()

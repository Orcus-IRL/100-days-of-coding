# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(chrome_options)
# driver.get("https://orteil.dashnet.org/experiments/cookie/")
#
# # values that are needed
# cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
#
# buy_cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
# cursor_price = int(buy_cursor.text.replace("A", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# buy_grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
# grandma_price = int(buy_grandma.text.replace("A", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# buy_factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
# factory_price = int(buy_factory.text.replace("Produces", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# buy_mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
# mine_price = int(buy_mine.text.replace("Mines", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# buy_shipment = driver.find_element(By.XPATH,'//*[@id="buyShipment"]')
# shipment_price = int(buy_shipment.text.replace("Brings", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# buy_alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
# alchemy_lab_price = int(buy_alchemy_lab.text.replace("Turns", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# buy_portal = driver.find_element(By.XPATH,'//*[@id="buyPortal"]')
# portal_price = int(buy_portal.text.replace("Opens", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# buy_timemachine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
# time_machine_price = int(buy_timemachine.text.replace("Brings", "-").split("-")[1].replace(" ", "").replace(",", ""))
#
# import time
# timeout = time.time() + 5  # 5 seconds from now
# min_timeout = time.time() + 20
#
# while True:
#
#     money = driver.find_element(By.ID, "money")
#     money_text = int(money.text)
#     cookie.click()
#     # print(money_text)
#     if time.time() > min_timeout:
#         print("Exiting...")
#         break
#
#     elif time.time() > timeout:
#         if money_text >= time_machine_price:
#             buy_timemachine.click()
#             timeout = time.time() + 5
#         elif money_text >= portal_price:
#             buy_portal.click()
#             timeout = time.time() + 5
#         elif money_text >= alchemy_lab_price:
#             buy_alchemy_lab.click()
#             timeout = time.time() + 5
#         elif money_text >= shipment_price:
#             buy_shipment.click()
#             timeout = time.time() + 5
#         elif money_text >= mine_price:
#             buy_mine.click()
#             timeout = time.time() + 5
#         elif money_text >= factory_price:
#             buy_factory.click()
#             timeout = time.time() + 5
#         elif money_text >= grandma_price:
#             buy_grandma.click()
#             timeout = time.time() + 5
#         else:
#             buy_cursor.click()
#             timeout = time.time() + 5
#
#     else:
#         continue
#
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

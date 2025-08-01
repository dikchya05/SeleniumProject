from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serve_obj=Service("D:/Drivers/chromedriver-win32/chromedriver.exe")
driver= webdriver.Chrome(service= serve_obj)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window() ##maximize the browser windows

# # Wait a few seconds to observe the browser
# time.sleep(3)
#
#
# driver.find_element(By.NAME, "q").send_keys("Lenovo IdeaCentre")
# # Keep the browser open for a bit longer to observe the result
# time.sleep(10)



# Add a small delay to let the page load
time.sleep(3)
#Linked Text
# driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()


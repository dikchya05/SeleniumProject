from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj = Service(r"D:\Drivers\chromedriver-win32\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.get("https://www.daraz.com.np/#hp-just-for-you")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "About Daraz").click()

time.sleep(10)

#driver.close() ##close only one browser
driver.quit() ###close multiple browser

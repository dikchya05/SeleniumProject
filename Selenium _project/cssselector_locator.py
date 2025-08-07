from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj =Service("D:\Drivers\chromedriver-win32/chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

#tag and ID
driver.find_element(By.CSS_SELECTOR, "in  put[data-val-required=Please enter your email]").send_keys("Enter your email")


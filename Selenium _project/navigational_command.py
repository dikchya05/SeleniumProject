from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj= Service("D:\Drivers\chromedriver-win32/chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.get("https://www.daraz.com.np/#?")
driver.get("https://demo.nopcommerce.com/news")

driver.back() #daraz
driver.forward() #nopcommerce
driver.refresh()

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj= Service("D:\Drivers\chromedriver-win32/chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.get("https://www.daraz.com.np/#?")

print(driver.title) #Online Shopping in Nepal: Best Deals, Prices & Discounts - Daraz.com.np
print(driver.current_url) #https://www.daraz.com.np/#?
print(driver.page_source)

driver.quit()
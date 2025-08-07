from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serve_obj=Service("D:/Drivers/chromedriver-win32/chromedriver.exe")
driver= webdriver.Chrome(service= serve_obj)

driver.get("https://www.daraz.com.np/#?")
driver.maximize_window()

#Absolute xpath
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]").send_keys("Tshirt")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/form/div/div[2]/a").click()
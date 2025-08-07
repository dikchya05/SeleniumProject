from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj = Service(r"D:\Drivers\chromedriver-win32\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F?")
driver.maximize_window()

#is_displayed
# searchbox= driver.find_element(By.Xpath, "(//div[@class='search-box__bar--29h6'])[1]")
# print("Displayed status:", searchbox.is_displayed())
# print("enabled status:", searchbox.is_enabled())

#is_selector for radio button
male= driver.find_element(By.XPATH, "(//input[@id='gender-male'])")
female= driver.find_element(By.XPATH, "(//input[@id='gender-female'])")


print(male.is_selected())
print(female.is_selected())


male.click() #select male button

print("After selecting male raadio button")
print(male.is_selected())
print(female.is_selected())

female.click()
print("After selecting female raadio button")
print(male.is_selected())
print(female.is_selected())


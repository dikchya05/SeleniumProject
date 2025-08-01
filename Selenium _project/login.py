from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj =Service("D:/Drivers/chromedriver-win32/chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)

driver.get("http://opensource-demo.orangehrmlive.com/")

try:
    # Open OrangeHRM demo login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 10)

    # Wait for username input field to be visible and enter username
    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")

    # Wait for password input field to be visible and enter password
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.send_keys("admin123")

    # Wait for the login button to be clickable and click it
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()

    # Wait until the page title contains 'OrangeHRM' after login
    wait.until(EC.title_contains("OrangeHRM"))

    # Verify page title
    actual_title = driver.title
    expected_title = "OrangeHRM"

    if actual_title == expected_title:
        print("Login test passed")
    else:
        print("Login FAILED")

finally:
    driver.quit()
# Updated method to find elements
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element_by.id ("txtPassword").send_keys("admin123")
# driver.find_element_by.id( "btnLogin").click()
#
# act_title =driver.title
# exp_title="OrangeHRM"
#
#
# if act_title == exp_title:
#     print("Login test passed")
# else:
#     print("login FAILED")
#
# driver.close()


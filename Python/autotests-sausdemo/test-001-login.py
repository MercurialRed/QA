from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

time.sleep(2)
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("LOGIN PASS")
time.sleep(2)

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("PASSWORD PASS")
time.sleep(2)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("AUTHORIZATION PASS")

time.sleep(3)
driver.close()
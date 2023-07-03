from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_use"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("NEGATIVE LOGIN PASS")

time.sleep(3)
user_name.clear()
print("CLEAR USERNAME")
time.sleep(1)

driver.refresh()
print("REFRESH")
time.sleep(3)
driver.close()
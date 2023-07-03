import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
time.sleep(1)

menu.click()
time.sleep(1)
menu_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
menu_about.click()
time.sleep(5)

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = "screenshot-test-004-" + now_date + ".png"
driver.save_screenshot("C:\\Users\\Red\\Desktop\\Git\\autotests-sausdemo\\screenshots\\" + name_screenshot)

driver.back()
print("GO BACK")
time.sleep(3)
driver.forward()
print("FORWARD")

time.sleep(3)
driver.close()
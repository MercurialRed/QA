import datetime

import action as action
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()
print("OPEN BROWSER")
time.sleep(2)

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("AUTHORIZATION")

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
assert url == get_url
print("URL PASS")
time.sleep(2)

product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("PRODUCT '" + value_product_1 + " SELECTED. PRICE: " + value_price_product_1)
time.sleep(2)

cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print("ENTER CART")

cart_url = "https://www.saucedemo.com/cart.html"
get_cart_url = driver.current_url
assert cart_url == get_cart_url
print("CART URL PASS")
time.sleep(2)

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("CHECKOUT")

checkout_url = "https://www.saucedemo.com/checkout-step-one.html"
get_checkout_url = driver.current_url
assert checkout_url == get_checkout_url
print("CHECKOUT URL PASS")
time.sleep(2)

first_name_value = "qwe"
second_name_value = "zxc"
zip_code_value = "123"

first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys(first_name_value)
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys(second_name_value)
zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_code.send_keys(zip_code_value)
time.sleep(2)
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("CONTINUE")

checkout_finish_url = "https://www.saucedemo.com/checkout-step-two.html"
get_checkout_finish_url = driver.current_url
assert checkout_finish_url == get_checkout_finish_url
print("CHECKOUT FINISH URL PASS")
time.sleep(2)

checkout_check_item = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
value_checkout_check_item = checkout_check_item.text
assert value_checkout_check_item == value_product_1
checkout_check_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_checkout_check_price = checkout_check_price.text
assert value_checkout_check_price == value_price_product_1
button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
button_finish.click()
print("FINISH")
time.sleep(2)

complete_url = "https://www.saucedemo.com/checkout-complete.html"
get_complete_url = driver.current_url
assert complete_url == get_complete_url
print("COMPLETE")
time.sleep(3)

driver.close()

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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
password.send_keys((Keys.RETURN)) #Enter

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
assert url == get_url
print("URL PASS")

text_products = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_products = text_products.text
print(value_text_products + " <-- THIS IS THE TEXT")
assert value_text_products == "Products"
print("ASSERT PASS")
time.sleep(1)

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()
time.sleep(1)
filter.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
filter.send_keys(Keys.RETURN)
print("FILTER PASS")
time.sleep(2)

driver.execute_script("window.scrollTo(0, 500)")
action = ActionChains(driver)
print("SCROLL PASS")
time.sleep(2)

white_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(white_t_shirt).perform()
time.sleep(1)
white_t_shirt.click()
print("ADDED TO CART")

time.sleep(2)
driver.close()
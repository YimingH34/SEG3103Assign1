from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.lego.com/en-ca")
wait = WebDriverWait(driver, 30)

time.sleep(1)
continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
continue_btn.click()
time.sleep(1)

continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
continue_btn.click()



time.sleep(3)
search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
search.click()

search_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="search-input"]'))
)
search_input.click()
txt_input = driver.find_element(By.ID, "desktop-search-search-input")
txt_input.send_keys("yoshi")
txt_input.send_keys(Keys.ENTER)
time.sleep(1)

link = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//a[@data-test="product-leaf-title" and contains(., "Super Mario World")]')))
link.click()
cart = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "add-to-cart-skroll-cta"]')))
sleep(3)
cart.click()

time.sleep(3)
search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "view-my-bag"]')))
search.click()

price_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'span.sk-visually-hidden'))
)

print(price_element.text)

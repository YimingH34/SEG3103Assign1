import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
driver=  webdriver.Firefox()

driver.get("https://www.lego.com/en-ca")


print("test")
wait = WebDriverWait(driver,30)


continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
continue_btn.click()
time.sleep(3)

continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
continue_btn.click()

time.sleep(5)
search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
search.click()

txt_input = driver.find_element(By.ID,"desktop-search-search-input")

txt_input.send_keys("yoshi")
txt_input.send_keys(Keys.ENTER)
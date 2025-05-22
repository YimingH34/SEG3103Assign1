import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

driver=  webdriver.Edge()

def verifyTextExist(text):

    found_text = driver.find_elements(By.XPATH, "//*[contains(text(),'"+text+"')]")

    if len(found_text) > 0:
        assert True
    else:
        assert False, text+" not found on the page."

    return found_text

driver.get("https://www.lego.com/en-ca")
wait = WebDriverWait(driver,30)

time.sleep(3)
continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
continue_btn.click()
time.sleep(3)

continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
continue_btn.click()
time.sleep(3)

# step 1
help_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-analytics-title = "help"]')))
help_btn.click()

# step 2
contact_us = driver.find_elements(By.XPATH, "//a[@data-analytics-title='contact-us']")
contact_us[0].click()

#step 3
missing_bricks = driver.find_element(By.CSS_SELECTOR, "p[data-test='quick-link-text-3']")
missing_bricks.click()

#step 4
time.sleep(2)
missing_pieces = driver.find_element(By.CSS_SELECTOR, "span[data-test='replacement-parts-missing-parts-button']")
missing_pieces.click()

#step 5
set_search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test = "set-search-container-search-box-input"]')))
driver.execute_script("arguments[0].scrollIntoView();", set_search)

set_search.send_keys("super star destroyer")
set_search.send_keys(Keys.ENTER)

#step 6
time.sleep(3)
set_text = verifyTextExist('Executor Super Star Destroyer™')

#step 7
set_item = set_text[0].find_element(By.XPATH, "./ancestor::*[@data-test='set-search-container-results-item']")

select_piece = set_item.find_element(By.XPATH, "//div[@data-skroll='LinkWrapper']")
select_piece.click()

#step 8
time.sleep(3)
verifyTextExist("Your set")
verifyTextExist("Executor Super Star Destroyer™")

#step 9
pieces_link = driver.find_element(By.XPATH, "//a[@data-test='pieces-part-type-item']")
pieces_link.click()

#step 10
time.sleep(2)
piece_search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test = "piece-search-container-search-box-input"]')))
driver.execute_script("arguments[0].scrollIntoView();", piece_search)
piece_search.send_keys("6514224")

#step 11
time.sleep(2)
icon_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='piece-search-container-search-box-submit']")
icon_button.click()

#step 12
time.sleep(2)
piece_text = verifyTextExist("FLAT TILE 1X2")

#step 13
piece_item = piece_text[0].find_element(By.XPATH, "./ancestor::*[@data-test='piece-search-result']")

select_piece = piece_item.find_element(By.CSS_SELECTOR, "button[data-test='piece-select-link']")
select_piece.click()

#step 14
time.sleep(2)
verifyTextExist("FLAT TILE 1X2")
verifyTextExist("Your piece(s)")


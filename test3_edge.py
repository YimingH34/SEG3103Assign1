import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
driver=  webdriver.Edge()

driver.get("https://www.lego.com/en-ca")

def verifyTextExist(text):
    xpath = "//*[contains(normalize-space(.), '{}')]".format(text)
    found_text = driver.find_elements(By.XPATH, xpath)

    if len(found_text) > 0:
        print(f"Found: {text}")
        return found_text
    else:
        raise AssertionError(f" {text} not found on the page.")

print("test")
wait = WebDriverWait(driver,30)


continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
continue_btn.click()
time.sleep(3)

continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
continue_btn.click()
time.sleep(5)

# 1. Click on Help button
help_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-analytics-title = "help"]')))
help_btn.click()
time.sleep(5)

# 2. Click on "Building Instructions"
building_instr_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-analytics-title="find-building-instructions"]')))
building_instr_btn.click()
time.sleep(5)

# 3. Enter "75367" in the search bar and press Enter
search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test="building-instructions-search-bar-input-field"]')))
driver.execute_script("arguments[0].scrollIntoView();", search_input)
search_input.send_keys("75367")
search_input.send_keys(Keys.ENTER)
time.sleep(5)


# 4. Verify the set appears
verifyTextExist("75367 Venator-Class Republic Attack Cruiser™")

# 5. Click on "View Instructions"
view_instr = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="view-instructions-button"]')))
view_instr.click()
time.sleep(5)

# 6. Verify the correct set page is displayed
set_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@data-test='page-heading']")))

print("Set:", repr(set_header.text))
expected_name = "Venator-Class Republic Attack Cruiser™"
assert expected_name in set_header.text, f"Expected set name not found. Got: {set_header.text}"
print("Correct instructions page loaded.")

# 7. Click all four download buttons
download_btn = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '.pdf') and contains(text(), 'Download')]")))

if len(download_btn) >= 4:
    for i in range(4):
        download_btn[i].click()
        print(f"Clicked download button {i + 1}")
        time.sleep(2)

print("Test finished!!!")
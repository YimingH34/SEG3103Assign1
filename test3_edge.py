import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import unittest

class test3_edge(unittest.TestCase):

    def findElementWithText(self, text):

        found_text = self.driver.find_elements(By.XPATH, "//*[contains(text(),'"+text+"')]")

        if len(found_text) == 0:
            print(f" {text} not found on the page.")

        return found_text
    
    
    def setUp(self):

        self.driver = webdriver.Edge()
        self.driver.get("https://www.lego.com/en-ca")
        self.wait = WebDriverWait(self.driver, 30)


    def assertTextPresent(self, text):

        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.assertIn(text, body.text)

    def test_building_instructions_download(self):

        wait = self.wait
        driver = self.driver

        continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
        continue_btn.click()
        time.sleep(3)

        strictly_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
        strictly_btn.click()
        time.sleep(3)

        # 1. Click on Help button
        help_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-analytics-title = "help"]')))
        help_btn.click()
        time.sleep(3)

        # 2. Click on "Building Instructions"
        building_instr_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-analytics-title="find-building-instructions"]')))
        building_instr_btn.click()
        time.sleep(3)

        # 3. Enter "75367" in the search bar and press Enter
        search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test="building-instructions-search-bar-input-field"]')))
        driver.execute_script("arguments[0].scrollIntoView();", search_input)
        search_input.send_keys("75367")
        search_input.send_keys(Keys.ENTER)
        time.sleep(5)

        # 4. Verify the set appears
        expected_name = "75367"
        found_elements = self.findElementWithText(expected_name)
        self.assertGreater(len(found_elements), 0, f"Element with text '{expected_name}' not found")
        self.assertIn(expected_name, found_elements[0].text)

        # 5. Click on "View Instructions"
        view_instr = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="view-instructions-button"]')))
        view_instr.click()
        time.sleep(5)

        # 6. Verify the correct set page is displayed
        expected_name = "Venator-Class Republic Attack Cruiser™"
        found_elements = self.findElementWithText(expected_name)
        self.assertGreater(len(found_elements), 0, f"Element with text '{expected_name}' not found")
        self.assertIn(expected_name, found_elements[0].text)

        
        # 7. Click all four download buttons
        download_btns = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '.pdf') and contains(text(), 'Download')]")))
        self.assertGreaterEqual(len(download_btns), 4)

        for i in range(4):
            download_btns[i].click()
            print(f"Clicked download button {i + 1}")
            time.sleep(2)

        print("Test finished successfully.")

    def tearDown(self):
        self.driver.quit()
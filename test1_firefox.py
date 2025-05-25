from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import unittest



class test1_firefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.lego.com/en-ca")
        self.wait = WebDriverWait(self.driver, 30)

        options = Options()
        options.add_argument("--log-level=3")  # 3 = fatal only

        time.sleep(1)
        continue_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
        continue_btn.click()
        time.sleep(1)

        continue_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
        continue_btn.click()






    def test_is_in_cart(self):
        # step 1
        time.sleep(3)
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
        search.click()
        # step 2
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="search-input"]'))
        )
        search_input.click()

        # step 3
        txt_input = self.driver.find_element(By.ID, "desktop-search-search-input")
        txt_input.send_keys("yoshi")
        txt_input.send_keys(Keys.ENTER)
        time.sleep(1)

        # step4
        link = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-test="product-leaf-title" and contains(., "Super Mario World")]')))
        link.click()
        cart = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "add-to-cart-skroll-cta"]')))
        sleep(1)
        cart.click()


        # step 5
        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.assertIn("169.99", body.text)
        self.assertIn("Super Mario World", body.text)

        # step 6
        time.sleep(4)
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "view-my-bag"]')))
        search.click()
        time.sleep(2)

        # step 7
        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.assertIn("169.99", body.text)
        self.assertIn("Super Mario World", body.text)
        print("test case 1 on firefox works")


    def tearDown(self):
        self.driver.quit()

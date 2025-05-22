from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import unittest



class test1_chrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.lego.com/en-ca")
        self.wait = WebDriverWait(self.driver, 30)

        time.sleep(1)
        continue_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
        continue_btn.click()
        time.sleep(1)

        continue_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
        continue_btn.click()


    def test_search(self):
        print("starting test case 1")
        time.sleep(1)
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
        search.click()
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="search-input"]'))
        )
        self.assertTrue(search_input.is_displayed())



    def test_search_lego(self):
        print("starting test case 2")

        wait = WebDriverWait(self.driver, 30)
        time.sleep(1)
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
        search.click()

        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="search-input"]'))
        )
        search_input.click()
        txt_input = self.driver.find_element(By.ID, "desktop-search-search-input")
        time.sleep(1)
        txt_input.send_keys("yoshi")
        txt_input.send_keys(Keys.ENTER)
        time.sleep(1)

        link = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-test="product-leaf-title" and contains(., "Super Mario World")]')))
        self.assertTrue(link.is_displayed())


    def test_add_to_cart(self):
        print("starting test case 3")

        wait = WebDriverWait(self.driver, 30)
        time.sleep(3)
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
        search.click()

        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="search-input"]'))
        )
        search_input.click()
        txt_input = self.driver.find_element(By.ID, "desktop-search-search-input")
        txt_input.send_keys("yoshi")
        txt_input.send_keys(Keys.ENTER)
        time.sleep(1)

        link = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-test="product-leaf-title" and contains(., "Super Mario World")]')))
        link.click()
        cart = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "add-to-cart-skroll-cta"]')))
        self.assertTrue(cart.is_displayed())




    def test_is_in_cart(self):
        print("starting test case 4")

        time.sleep(3)
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
        search.click()

        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="search-input"]'))
        )
        search_input.click()
        txt_input = self.driver.find_element(By.ID, "desktop-search-search-input")
        txt_input.send_keys("yoshi")
        txt_input.send_keys(Keys.ENTER)
        time.sleep(1)

        link = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-test="product-leaf-title" and contains(., "Super Mario World")]')))
        link.click()
        cart = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "add-to-cart-skroll-cta"]')))
        sleep(1)
        cart.click()

        time.sleep(4)
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "view-my-bag"]')))
        search.click()
        time.sleep(2)

        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.assertIn("169.99", body.text)
        self.assertIn("Super Mario World", body.text)


    def tearDown(self):
        self.driver.quit()

# driver=  webdriver.Firefox()
# driver.get("https://www.lego.com/en-ca")
# print("test")
#
# wait = WebDriverWait(driver,30)
# continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
# continue_btn.click()
# time.sleep(3)
#
# continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Strictly Necessary']")))
# continue_btn.click()
#
# time.sleep(3)
# search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "search-input-button"]')))
# search.click()

# txt_input = driver.find_element(By.ID,"desktop-search-search-input")
#
# txt_input.send_keys("yoshi")
# txt_input.send_keys(Keys.ENTER)
#
# time.sleep(3)
# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//a[@data-test="product-leaf-title" and contains(., "Super Mario World")]'))
# )
# element.click()

# time.sleep(3)
# search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "add-to-cart-skroll-cta"]')))
# search.click()

# time.sleep(3)
# search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test = "view-my-bag"]')))
# search.click()


# check if qty = 1


# check if item exist
# check if price is 169.99

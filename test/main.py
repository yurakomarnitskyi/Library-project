import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)  # Implicit wait for 15 seconds

    def test_login_valid_credentials(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")

        # Use explicit wait to ensure elements are present
        wait = WebDriverWait(driver, 10)
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        username_input.send_keys("yura@gmail.com")

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys("47sifufu")

        login_submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        login_submit_button.click()

        logout_button = driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()

        self.assertTrue(wait.until(EC.presence_of_element_located((By.NAME, "email"))))

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

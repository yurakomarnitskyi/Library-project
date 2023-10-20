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

       
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys("yura@gmail.com")

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys("yura2001")
        

        login_submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        login_submit_button.click()
        time.sleep(4)

        logout_button = driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
        
        logout_button = driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
        
        
        time.sleep(4)
        
        self.assertTrue(wait.until(EC.presence_of_element_located((By.NAME, "email"))))
    
    @unittest.expectedFailure
    def test_login_not_valid_credentials(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
       
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys("yura@gmail.com")

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys("yu")
        time.sleep(4)
        

        login_submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        login_submit_button.click()
        
        self.assertTrue(wait.until(EC.presence_of_element_located((By.NAME, "Logout"))))
        
    
      
        
    def tearDown(self):
        time.sleep(4)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

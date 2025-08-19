from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class CheckoutPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill_info_and_continue(self, first: str, last: str, postal: str):
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)
        self.driver.find_element(By.ID, "continue").click()
      
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return self  

    def get_total_value(self) -> str:
        total_text = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text  
        m = re.search(r'([0-9]+(?:\.[0-9]+)?)', total_text)
        return m.group(1) if m else total_text.strip()


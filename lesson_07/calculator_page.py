from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver, wait_timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds: str):
        delay = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, label: str):
    
        xpath = f"//span[normalize-space(.)='{label}']"
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn.click()

    def wait_for_result(self, expected: str, timeout: int = 90) -> str:
       
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected)
        )
        
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

    def get_result(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
    
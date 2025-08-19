from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataTypesPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
    
        self.wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    def fill_field_by_name(self, name, value):
        elm = self.wait.until(EC.presence_of_element_located((By.NAME, name)))
        elm.clear()
        elm.send_keys(value)

    def submit(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        btn.click()

    def get_classes_by_id(self, element_id, timeout=15):
        elm = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        return elm.get_attribute("class")
    
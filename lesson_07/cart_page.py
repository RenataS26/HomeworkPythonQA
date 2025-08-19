
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from checkout_page import CheckoutPage

class CartPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_checkout(self) -> CheckoutPage:
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        return CheckoutPage(self.driver)

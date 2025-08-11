
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cart_page import CartPage

class InventoryPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_item(self, item_key: str):
       
        btn_id = f"add-to-cart-{item_key}"
        self.wait.until(EC.element_to_be_clickable((By.ID, btn_id))).click()

    def go_to_cart(self) -> CartPage:
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        return CartPage(self.driver)

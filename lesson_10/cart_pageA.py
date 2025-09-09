from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from checkout_pageA import CheckoutPage

class CartPage:
    def __init__(self, driver, timeout: int = 10):
        """
        Инициализация объекта страницы корзины.

        Args
        ----------
        driver : WebDriver
            Экземпляр Selenium WebDriver для управления браузером.
        timeout : int, optional
            Время ожидания элементов на странице в секундах (по умолчанию 10).
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_checkout(self) -> CheckoutPage:
        """
        Нажать на кнопку "Checkout" для перехода к оформлению заказа.

        Returns
        ----------
        CheckoutPage
            Объект страницы оформления заказа.
        """
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        return CheckoutPage(self.driver)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cart_pageA import CartPage

class InventoryPage:
    def __init__(self, driver, timeout: int = 10):
        """
        Инициализация страницы инвентаря.

        Args
        ----------
        driver : WebDriver
            Экземпляр Selenium WebDriver для работы с браузером.
        timeout : int, optional
            Время ожидания элементов на странице в секундах (по умолчанию 10).

        Returns
        ----------
        None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_item(self, item_key: str) -> None:
        """
        Добавить товар в корзину по его ключу.

        Args
        ----------
        item_key : str
            Ключ элемента, используемый для формирования id кнопки добавления товара.

        Returns
        ----------
        None
        """
        btn_id = f"add-to-cart-{item_key}"
        self.wait.until(EC.element_to_be_clickable((By.ID, btn_id))).click()

    def go_to_cart(self) -> CartPage:
        """
        Перейти на страницу корзины.

        Returns
        ----------
        CartPage
            Объект страницы корзины.
        """
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        return CartPage(self.driver)

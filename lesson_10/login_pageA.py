from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inventory_pageA import InventoryPage

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver, timeout: int = 10):
        """
        Инициализация страницы логина.

        Args
        ----------
        driver : WebDriver
            Экземпляр Selenium WebDriver для управления браузером.
        timeout : int, optional
            Время ожидания элементов на странице в секундах (по умолчанию 10).

        Returns
        ----------
        None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> 'LoginPage':
        """
        Открыть страницу логина по заданному URL.

        Args
        ----------
        (нет параметров, кроме self)

        Returns
        ----------
        LoginPage
            Возвращает экземпляр текущей страницы для цепочек вызовов.
        """
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str) -> InventoryPage:
        """
        Выполнить вход в систему с заданными логином и паролем.

        Args
        ----------
        username : str
            Имя пользователя для авторизации.
        password : str
            Пароль пользователя для авторизации.

        Returns
        ----------
        InventoryPage
            Возвращает объект страницы после успешного входа.
        """
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return InventoryPage(self.driver)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataTypesPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver, timeout: int = 10):
        """
        Инициализация объекта страницы с типами данных.

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

    def open(self) -> None:
        """
        Открыть страницу с заданным URL.

        Returns
        ----------
        None
        """
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    def fill_field_by_name(self, name: str, value: str) -> None:
        """
        Заполнить поле на странице по имени элемента.

        Args
        ----------
        name : str
            Атрибут name элемента формы.
        value : str
            Значение для ввода в поле.

        Returns
        ----------
        None
        """
        elm = self.wait.until(EC.presence_of_element_located((By.NAME, name)))
        elm.clear()
        elm.send_keys(value)

    def submit(self) -> None:
        """
        Нажать на кнопку отправки формы.

        Returns
        ----------
        None
        """
        btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        btn.click()

    def get_classes_by_id(self, element_id: str, timeout: int = 15) -> str:
        """
        Получить значение атрибута class у элемента по id.

        Args
        ----------
        element_id : str
            Значение атрибута id искомого элемента.
        timeout : int, optional
            Время ожидания элемента в секундах (по умолчанию 15).

        Returns
        ----------
        str
            Строка с классами элемента.
        """
        elm = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        return elm.get_attribute("class")

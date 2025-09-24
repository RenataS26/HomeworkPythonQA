import pytest
import allure
from login_pageA import LoginPage

@pytest.fixture
def driver():
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Покупка товаров")
@allure.epic("Покупка товаров")
@allure.feature("Оформление заказа на SauceDemo")
@allure.story("Проверка корректного оформления заказа и итоговой суммы")
def test_saucedemo_checkout(driver):
    with allure.step("Открываем страницу логина и авторизуемся"):
        login = LoginPage(driver).open()
        inventory = login.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        inventory.add_item("sauce-labs-backpack")
        inventory.add_item("sauce-labs-bolt-t-shirt")
        inventory.add_item("sauce-labs-onesie")

    with allure.step("Переходим в корзину и начинаем оформление заказа"):
        cart = inventory.go_to_cart()
        checkout = cart.click_checkout()

    with allure.step("Заполняем данные для оформления заказа и продолжаем"):
        checkout.fill_info_and_continue("Рената", "Спижарская", "601503")

    with allure.step("Получаем итоговую стоимость заказа и проверяем"):
        total_value = checkout.get_total_value()
        assert total_value == "58.29", f"Ожидаемая сумма 58.29, получено {total_value}"
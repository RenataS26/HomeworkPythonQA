import pytest
from login_page import LoginPage

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

def test_saucedemo_checkout(driver):
    login = LoginPage(driver).open()
    inventory = login.login("standard_user", "secret_sauce")

    # Добавляем товары
    inventory.add_item("sauce-labs-backpack")
    inventory.add_item("sauce-labs-bolt-t-shirt")
    inventory.add_item("sauce-labs-onesie")

    cart = inventory.go_to_cart()
    checkout = cart.click_checkout()

    checkout.fill_info_and_continue("Рената", "Спижарская", "601503")
    total_value = checkout.get_total_value()

    assert total_value == "58.29"


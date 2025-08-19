import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_checkout(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Рената")
    driver.find_element(By.ID, "last-name").send_keys("Спижарская")
    driver.find_element(By.ID, "postal-code").send_keys("601503")

    driver.find_element(By.ID, "continue").click()

 
    total_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    
    total_value = total_text.split("$")[-1]

    assert total_value == "58.29"
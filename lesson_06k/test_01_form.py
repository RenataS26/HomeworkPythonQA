import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_driver_path = r"C:\Users\Пользователь\Desktop\учеба\msedgedriver.exe"

@pytest.fixture
def driver():
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation_edge(driver):
    wait = WebDriverWait(driver, 10)
    #element = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    element = wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    # Заполнение полей формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставить пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать Submit
    driver.find_element(By.CSS_SELECTOR, ("button[type='submit']")).click()

   
    WebDriverWait(driver, 15).until(
         EC.presence_of_element_located((By.ID, "zip-code"))
              )
    #zip_code_field = WebDriverWait(driver, 20).until(
         #EC.visibility_of_element_located((By.ID, "zip"))
#)
    #driver.switch_to.frame()
    zip_code_field = driver.find_element(By.ID, "zip-code")

    WebDriverWait(driver, 20)
   
    zip_code_classes = zip_code_field.get_attribute("class")

    assert ("alert py-2 alert-danger" in zip_code_classes or "error" in zip_code_classes), "Zip code поле не подсвечено красным"

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert ("alert py-2 alert-success" in field_classes or "valid" in field_classes), f"Поле {field_id} не подсвечено зелёным"
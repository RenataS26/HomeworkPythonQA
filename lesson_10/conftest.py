import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_driver_path = r"C:\Users\Пользователь\Desktop\учеба\msedgedriver.exe"

@pytest.fixture
def driver():
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
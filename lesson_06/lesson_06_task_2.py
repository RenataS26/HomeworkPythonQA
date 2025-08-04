from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")

search_input=driver.find_element(By.CSS_SELECTOR,"#newButtonName" )
search_input.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
btn_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(btn_text)


driver.quit()

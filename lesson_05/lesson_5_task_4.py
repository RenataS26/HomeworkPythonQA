from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile

driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
sleep(2)

flash_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text
print(flash_message)

sleep(2)
driver.quit()
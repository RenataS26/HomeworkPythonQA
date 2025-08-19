import time
from calculator_page import CalculatorPage

def test_slow_calculator_delay_45(driver):
    page = CalculatorPage(driver)
    page.open()

    # установить задержку 45 секунд
    page.set_delay("45")

    # выполнить 7 + 8 =
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    # ожидаем результат (ждем с запасом максимум 70-90 с)
    result = page.wait_for_result("15", timeout=90)

    assert result == "15"
    
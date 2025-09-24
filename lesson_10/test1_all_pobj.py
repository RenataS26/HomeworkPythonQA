import pytest
import allure
from data_types_pageA import DataTypesPage

@allure.title("Авторизация")
@allure.epic("Проверка формы")
@allure.feature("Валидация формы с помощью POM")
@pytest.mark.usefixtures("driver")
def test_form_validation_pom(driver):
    with allure.step("Открываем страницу с формой"):
        page = DataTypesPage(driver)
        page.open()

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        # zip-код не заполняем
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    with allure.step("Заполняем поля формы"):
        for name, value in data.items():
            page.fill_field_by_name(name, value)

    with allure.step("Отправляем форму"):
        page.submit()

    with allure.step("Проверяем подсветку поля zip-code как ошибки"):
        zip_classes = page.get_classes_by_id("zip-code")
        assert ("alert py-2 alert-danger" in (zip_classes or "") or "error" in (zip_classes or "")), "Zip code поле не подсвечено красным"

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    with allure.step("Проверяем, что остальные поля подсвечены как валидные"):
        for field_id in fields_to_check:
            classes = page.get_classes_by_id(field_id)
            assert ("alert py-2 alert-success" in (classes or "") or "valid" in (classes or "")), f"Поле {field_id} не подсвечено зелёным"

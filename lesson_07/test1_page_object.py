from data_types_page import DataTypesPage

def test_form_validation_pom(driver):
    page = DataTypesPage(driver)
    page.open()

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        # "zip" or "zip-code" не заполняем
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in data.items():
        page.fill_field_by_name(name, value)

    page.submit()

    # Проверяем подсветку zip-code как ошибку
    zip_classes = page.get_classes_by_id("zip-code")
    assert ("alert py-2 alert-danger" in (zip_classes or "") or "error" in (zip_classes or "")), "Zip code поле не подсвечено красным"

    # Проверяем поля на валидность
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        classes = page.get_classes_by_id(field_id)
        assert ("alert py-2 alert-success" in (classes or "") or "valid" in (classes or "")), f"Поле {field_id} не подсвечено зелёным"

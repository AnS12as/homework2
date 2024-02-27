import pytest

from main import Category, Smartphone, Grass


@pytest.fixture
def category():
    return Category("Тестовая категория", "Описание тестовой категории")


def test_add_product_to_category(category):
    smartphone = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро")
    category.add_product(smartphone)
    assert len(category.products) == 1
    assert category.products[0] == smartphone


def test_get_products(category):
    smartphone = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро")
    grass = Grass("Kentucky Bluegrass", 10, "Садоводство", "USA", "14 days", "Зеленый")
    category.add_product(smartphone)
    category.add_product(grass)
    expected_output = f"{smartphone.name}, {smartphone.price} руб. Остаток: {smartphone.quantity} шт.\n{grass.name}, {grass.price} руб. Остаток: {grass.quantity} шт.\n"
    assert category.get_products() == expected_output


def test_add_non_product_to_category(category):
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_add_different_product_to_category(category):
    smartphone = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро")
    grass = Grass("Kentucky Bluegrass", 10, "Садоводство", "USA", "14 days", "Зеленый")
    with pytest.raises(TypeError):
        category.add_product(smartphone + grass)


if __name__ == "__main__":
    print("Все тесты пройдены!")

from main import Category, Product


def test_category():
    category = Category("Электроника", "Товары электроники")
    assert category.name == "Электроника"
    assert category.description == "Товары электроники"
    category.add_product("Смартфон")
    category.add_product("Ноутбук")
    assert category.get_products() == "Смартфон, 80 руб. Остаток: 15 шт.\nНоутбук, 80 руб. Остаток: 15 шт.\n"


def test_product():
    product = Product("Смартфон", "Мощный смартфон", 500, 10)
    assert product.name == "Смартфон"
    assert product.description == "Мощный смартфон"
    assert product.price == 500
    assert product.quantity == 10
    product.price = 600
    assert product.price == 600
    product.price = -100
    assert product.price == 600  # Цена не должна измениться
    product.price = 400
    assert product.price == 400

    products = []
    product1 = Product.create_product("Смартфон", "Мощный смартфон", 500, 10, products)
    products.append(product1)
    product2 = Product.create_product("Ноутбук", "Легкий и компактный ноутбук", 800, 5, products)
    products.append(product2)
    product3 = Product.create_product("Смартфон", "Мощный смартфон", 600, 8, products)
    assert product3.quantity == 18
    assert product3.price == 600

    product4 = Product("Планшет", "Мощный планшет", 700, 5)
    product4.price = 600  # Понижаем цену
    assert product4.price == 600
    product4.price = 800  # Попытка повысить цену
    assert product4.price == 600  # Цена не должна измениться

if __name__ == "__main__":
    test_category()
    test_product()
    print("Все тесты пройдены успешно")

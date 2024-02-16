import unittest
from main import Category, Product


class TestCategory(unittest.TestCase):
    def test_add_product(self):
        category = Category("Электроника")
        product1 = Product("Ноутбук", 1000, 10)
        product2 = Product("Смартфон", 800, 5)

        category.add_product(product1)
        category.add_product(product2)

        expected_output = "Ноутбук, 1000 руб. Остаток: 10 шт.\nСмартфон, 800 руб. Остаток: 5 шт.\n"
        self.assertEqual(category.get_products_info(), expected_output)

    def test_get_products_info(self):
        category = Category("Electronics")
        product1 = Product("Laptop", 1000, 10)
        product2 = Product("Smartphone", 800, 5)

        category.add_product(product1)
        category.add_product(product2)


class TestProduct(unittest.TestCase):
    def test_create_product(self):
        product1 = Product("Ноутбук", 1000, 10)
        product2 = Product("Смартфон", 800, 5)

        product_list = [product1, product2]

        # Создание нового товара с уже существующим именем
        new_product = Product.create_product("Ноутбук", 1200, 5, product_list)
        self.assertEqual(new_product.stock, 15)
        self.assertEqual(new_product.price, 1000)


if __name__ == '__main__':
    unittest.main()

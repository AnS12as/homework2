import unittest
from main import Category, Product


class TestCategory(unittest.TestCase):
    class TestCategory(unittest.TestCase):
        def test_string_representation(self):
            category = Category("Электроника")
            category.add_product(Product("Смартфон", 500, 10))
            category.add_product(Product("Ноутбук", 800, 5))
            expected_string = "Электроника, количество продуктов: 2"
            self.assertEqual(str(category), expected_string)

    def test_iteration(self):
        category = Category("Электроника")
        category.add_product(Product("Смартфон", 500, 10))
        category.add_product(Product("Ноутбук", 800, 5))
        expected_products = ["Смартфон, 500 руб. Остаток: 10 шт.", "Ноутбук, 800 руб. Остаток: 5 шт."]
        actual_products = [str(product) for product in category]
        self.assertEqual(actual_products, expected_products)


class TestProduct(unittest.TestCase):
    def test_string_representation(self):
        product = Product("Смартфон", 500, 10)
        expected_string = "Смартфон, 500 руб. Остаток: 10 шт."
        self.assertEqual(str(product), expected_string)

    def test_addition(self):
        product1 = Product("Смартфон", 500, 10)
        product2 = Product("Ноутбук", 800, 5)
        result = product1 + product2
        expected_result = Product("Combined Product", 500 * 10 + 800 * 5, 10 + 5)
        self.assertEqual(str(result), str(expected_result))


if __name__ == '__main__':
    unittest.main()

import unittest
from main import Category, Product


class TestCategoryAndProduct(unittest.TestCase):

    def test_category_initialization(self):
        category = Category("Electronics", "Electronics category")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronics category")
        self.assertEqual(category.products, [])

    def test_product_initialization(self):
        product = Product("Laptop", "High-performance laptop", 987.39, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "High-performance laptop")
        self.assertEqual(product.price, 987.39)
        self.assertEqual(product.quantity, 10)

    def test_count_products(self):
        category = Category("Electronics", "Electronics category")
        category.add_product(Product("Laptop", "High-performance laptop", 987.39, 10))
        category.add_product(Product("Smartphone", "Latest smartphone model", 599.99, 20))
        self.assertEqual(len(category.products), 2)

    def test_count_categories(self):
        # Создаем несколько категорий
        Category("Electronics", "Electronics category")
        Category("Clothing", "Clothing category")
        Category("Books", "Books category")
        self.assertEqual(Category.total_categories, 4)


if __name__ == '__main__':
    unittest.main()


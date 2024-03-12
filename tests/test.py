import unittest
from main import Smartphone, Grass, Category, Order


class TestSmartphone(unittest.TestCase):
    def test_smartphone_creation(self):
        smartphone = Smartphone("iPhone", 999, "Electronics", "High", "12 Pro", "256GB", "Silver", 5)
        self.assertEqual(smartphone.name, "iPhone")
        self.assertEqual(smartphone.price, 999)
        self.assertEqual(smartphone.category, "Electronics")
        self.assertEqual(smartphone.get_description(), "iPhone 12 Pro - 256GB, Silver, Performance: High")


class TestGrass(unittest.TestCase):
    def test_grass_creation(self):
        grass = Grass("Kentucky Bluegrass", 10, "Gardening", "USA", "14 days", "Green", 100)
        self.assertEqual(grass.name, "Kentucky Bluegrass")
        self.assertEqual(grass.price, 10)
        self.assertEqual(grass.category, "Gardening")
        self.assertEqual(grass.get_description(), "Kentucky Bluegrass - $10 - Gardening - USA - Green")


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", "Devices and gadgets")
        self.product = Smartphone("iPhone", 999, "Electronics", "High", "12 Pro", "256GB", "Silver", 5)

    def test_add_product(self):
        self.category.add_product(self.product)
        self.assertIn(self.product, self.category.products)

    def test_get_products(self):
        self.category.add_product(self.product)
        expected_output = "iPhone, 999 руб. Остаток: 5 шт.\n"
        self.assertEqual(self.category.get_products(), expected_output)


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.product = Smartphone("iPhone", 999, "Electronics", "High", "12 Pro", "256GB", "Silver", 5)
        self.order = Order(self.product, 2)

    def test_order_creation(self):
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.total_cost, 1998)

    def test_display_info(self):
        expected_output = "Order for 'iPhone' x 2 for $1998"
        self.assertEqual(self.order.display_info(), expected_output)


if __name__ == '__main__':
    unittest.main()

import unittest
from main import Category, Smartphone, Grass, Order


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", "Electronic devices")
        self.smartphone = Smartphone("iPhone", 999, "Electronics", "High", "12 Pro", "256GB", "Silver", 5)
        self.category.add_product(self.smartphone)

    def test_add_product(self):
        self.assertIn(self.smartphone, self.category.products)

    def test_get_products(self):
        products_info = self.category.get_products()
        self.assertIn("iPhone", products_info)


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.grass = Grass("Kentucky Bluegrass", 10, "Gardening", "USA", "14 days", "Green", 50)
        self.order = Order(self.grass, 5)

    def test_order_creation(self):
        self.assertEqual(self.order.product, self.grass)
        self.assertEqual(self.order.quantity, 5)
        self.assertEqual(self.order.total_cost, 50)

    def test_display_info(self):
        order_info = self.order.display_info()
        self.assertIn("Order for 'Kentucky Bluegrass'", order_info)
        self.assertIn("for $50", order_info)


if __name__ == '__main__':
    unittest.main()

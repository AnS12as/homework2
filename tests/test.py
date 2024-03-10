import unittest
from main import Grass, Category, Order


class TestGrass(unittest.TestCase):
    def setUp(self):
        self.grass = Grass("Kentucky Bluegrass", 10, "Gardening", "USA", "14 days", "Green", 20)

    def test_grass_creation(self):
        self.assertEqual(self.grass.name, "Kentucky Bluegrass")
        self.assertEqual(self.grass.price, 10)
        self.assertEqual(self.grass.quantity, 20)

class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Gardening", "All about gardening")
        self.grass = Grass("Kentucky Bluegrass", 10, "Gardening", "USA", "14 days", "Green", 20)

    def test_add_product(self):
        self.category.add_product(self.grass)
        self.assertIn(self.grass, self.category.products)

    def test_get_products(self):
        self.category.add_product(self.grass)
        products_info = self.category.get_products()
        self.assertIn("Kentucky Bluegrass", products_info)

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.grass = Grass("Kentucky Bluegrass", 10, "Gardening", "USA", "14 days", "Green", 20)
        self.order = Order(self.grass, 2)

    def test_order_creation(self):
        self.assertEqual(self.order.product, self.grass)
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.total_cost, 20)

    def test_display_info(self):
        info = self.order.display_info()
        self.assertIn("Order for 'Kentucky Bluegrass' info displayed.", info)


if __name__ == '__main__':
    unittest.main()


import unittest
from main import Category, Smartphone, Grass, Order, ZeroQuantityError


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", "Electronic devices")
        self.smartphone = Smartphone("iPhone", 999, "Electronics", "High", "12 Pro", "256GB", "Silver", 5)

    def test_add_product_success(self):
        self.category.add_product(self.smartphone)
        self.assertIn(self.smartphone, self.category.products)

    def test_add_product_failure(self):
        with self.assertRaises(ZeroQuantityError):
            zero_quantity_smartphone = Smartphone("Zero iPhone", 999, "Electronics", "Low", "No Model", "0GB", "Black",
                                                  0)
            self.category.add_product(zero_quantity_smartphone)


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.grass = Grass("Kentucky Bluegrass", 10, "Gardening", "USA", "14 days", "Green", 50)

    def test_order_creation_success(self):
        order = Order(self.grass, 2)
        self.assertEqual(order.product, self.grass)
        self.assertEqual(order.quantity, 2)

    def test_order_creation_failure(self):
        with self.assertRaises(ZeroQuantityError):
            Order(self.grass, 0)


class TestAveragePrice(unittest.TestCase):
    def test_calculate_average_price(self):
        category = Category("Gardening", "Garden products")
        grass1 = Grass("Grass1", 20, "Gardening", "USA", "10 days", "Green", 10)
        grass2 = Grass("Grass2", 30, "Gardening", "USA", "15 days", "Yellow", 15)
        category.add_product(grass1)
        category.add_product(grass2)
        self.assertEqual(category.calculate_average_price(), 25)


if __name__ == '__main__':
    unittest.main()

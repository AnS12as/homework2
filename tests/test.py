import unittest
from main import Smartphone, Grass, Category, Order


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро", 10)

    def test_smartphone_creation(self):
        self.assertEqual(self.smartphone.name, "iPhone")
        self.assertEqual(self.smartphone.price, 999)


class TestGrass(unittest.TestCase):
    def setUp(self):
        self.grass = Grass("Kentucky Bluegrass", 10, "Садоводство", "USA", "14 days", "Зеленый", 50)

    def test_grass_creation(self):
        self.assertEqual(self.grass.name, "Kentucky Bluegrass")
        self.assertEqual(self.grass.price, 10)


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Электроника", "Электронные устройства")
        self.smartphone = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро", 10)
        self.grass = Grass("Kentucky Bluegrass", 10, "Садоводство", "USA", "14 days", "Зеленый", 50)

    def test_add_product(self):
        self.category.add_product(self.smartphone)
        self.assertIn(self.smartphone, self.category._Category__products)

    def test_get_products(self):
        self.category.add_product(self.smartphone)
        self.assertIn("iPhone", self.category.get_products())


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро", 10)
        self.order = Order(self.smartphone, 2)

    def test_order_creation(self):
        self.assertEqual(self.order.total_cost, 1998)

    def test_display_info(self):
        info = self.order.display_info()
        self.assertIn("Заказ: iPhone", info)
        self.assertIn("Общая стоимость: $1998", info)


if __name__ == '__main__':
    unittest.main()

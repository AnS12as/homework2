class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # делаем список приватным
        Category.total_categories += 1

    def add_product(self, product):
        self.__products.append(product)

    def get_products(self):
        products_info = ""
        for product in self.__products:
            products_info += f"{product}, 80 руб. Остаток: 15 шт.\n"

category = Category("Электроника", "Товары электроники")
category.add_product("Смартфон")
category.add_product("Ноутбук")
print(category.get_products())


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

product1 = Product.create_product("Смартфон", "Мощный смартфон", 500, 10)
product2 = Product.create_product("Ноутбук", "Легкий и компактный ноутбук", 800, 5)

